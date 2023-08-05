# pylint: disable=duplicate-code

""" The base class for how a platform will operate """
from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, Union

from kubernetes import client

from mcli.models import MCLIPlatform
from mcli.objects.secrets.platform_secret import SecretManager
from mcli.serverside.job.mcli_k8s_resource_requirements_typing import MCLIK8sResourceRequirements
from mcli.serverside.platforms.gpu_type import GPUType
from mcli.serverside.platforms.instance_type import InstanceType
from mcli.serverside.platforms.platform_instances import PlatformInstances
from mcli.utils.utils_kube import safe_update_optional_dictionary, safe_update_optional_list

if TYPE_CHECKING:
    from mcli.serverside.job.mcli_k8s_job import MCLIK8sJob, MCLIVolume
# types
Resources = Dict[str, int]
Description = Dict[str, Any]


class PriorityLabel(Enum):
    """Enum to specify the priority for a run.
    """
    low = 'scavenge'
    standard = 'standard'
    high = 'emergency'

    @classmethod
    def ensure_enum(cls, val: Union[str, PriorityLabel]) -> PriorityLabel:
        if isinstance(val, PriorityLabel):
            return val
        try:
            return PriorityLabel[val]
        except KeyError:
            pass

        raise ValueError(f'Unable to ensure {val} is a PriorityLabel Enum')

    def __str__(self):
        return str(self.value)


class InvalidPriorityError(Exception):
    """Raised if an invalid priority class is requested
    """
    requested_class: str
    valid_classes: List[str]
    platform: Optional[str]

    def __init__(self, requested_class: str, valid_classes: List[str], platform: Optional[str] = None):
        self.requested_class = requested_class
        self.valid_classes = valid_classes
        self.platform = platform
        super().__init__()

    def __str__(self) -> str:
        platform_message = f'Platform {self.platform + " " if self.platform else ""}does not support'
        if self.valid_classes:
            valid_classes = ', '.join(sorted(self.valid_classes))
            error_message = (f'{platform_message} priority class: {self.requested_class}. '
                             f'Must be one of: {valid_classes}')
        else:
            error_message = f'{platform_message} priority classes'

        return error_message


class PlatformSetupError(Exception):
    """Raised if platform setup failed
    """


class PlatformCreationError(Exception):
    """Raised if platform setup failed
    """


class PlatformResourceHandler():
    """ All Instance Related Functions """
    allowed_instances: PlatformInstances

    def get_instance_type(self, gpu_type: GPUType, gpu_num: int, cpus: Optional[int] = None) -> InstanceType:
        return self.allowed_instances.get_instance_type(
            gpu_type=gpu_type,
            gpu_num=gpu_num,
            cpus=cpus,
        )


class PlatformPriorityHandler():
    # priority class to use for the job
    priority_class_labels: Dict[str, str] = {}
    default_priority_class: Optional[str] = None  # If a priority class should be default, put it here.

    def get_priority_class_label(self, priority_class_override: Optional[str]) -> Optional[str]:
        priority_class = priority_class_override if priority_class_override else self.default_priority_class
        priority_class_label: Optional[str] = None
        if priority_class is not None:
            if priority_class not in self.priority_class_labels:
                raise InvalidPriorityError(priority_class, list(self.priority_class_labels))
            priority_class_label = self.priority_class_labels[priority_class]
        return priority_class_label


class PlatformProperties():
    mcli_platform: MCLIPlatform

    @property
    def namespace(self):
        return self.mcli_platform.namespace

    @property
    def kubernetes_context(self):
        return self.mcli_platform.kubernetes_context


class GenericK8sPlatform(
        PlatformResourceHandler,
        PlatformPriorityHandler,
        PlatformProperties,
):
    """ A Generic Platform implementation """

    interactive: bool = False
    pod_group_scheduler: Optional[str] = None

    @staticmethod
    def get_k8s_context_map() -> Dict[str, Type[GenericK8sPlatform]]:
        # pylint: disable-next=import-outside-toplevel
        from mcli.serverside.platforms.overrides import (AWSPlatform, AzurePlatform, COTAPlatform, GCPPlatform,
                                                         Microk8sPlatform, R1Z1Platform, R1Z2Platform, R1Z4Platform,
                                                         R4Z1Platform, R7Z1Platform, R7Z2Platform, R7Z3Platform,
                                                         R7Z4Platform, R99Z1Platform)

        # pylint: disable-next=invalid-name
        context_map: Dict[str, Type[GenericK8sPlatform]] = {
            'aws-research-01': AWSPlatform,
            'azure-research-01': AzurePlatform,
            'gcp-research-01': GCPPlatform,
            'colo-research-01': COTAPlatform,
            'microk8s': Microk8sPlatform,
            'r1z1': R1Z1Platform,
            'r1z2': R1Z2Platform,
            'r1z4': R1Z4Platform,
            'r4z1': R4Z1Platform,
            'r7z1': R7Z1Platform,
            'r7z2': R7Z2Platform,
            'r7z3': R7Z3Platform,
            'r7z4': R7Z4Platform,
            'r99z1': R99Z1Platform,
        }
        return context_map

    @classmethod
    def from_mcli_platform(cls, mcli_platform: MCLIPlatform) -> GenericK8sPlatform:
        context_map = GenericK8sPlatform.get_k8s_context_map()
        if mcli_platform.kubernetes_context not in context_map:
            raise PlatformCreationError()
        k8s_platform = context_map[mcli_platform.kubernetes_context]
        return k8s_platform(mcli_platform=mcli_platform)

    def __init__(self, mcli_platform: MCLIPlatform) -> None:
        self.mcli_platform = mcli_platform
        self.secret_manager = SecretManager(mcli_platform=mcli_platform)
        self.interactive = False
        super().__init__()

    def setup(self) -> bool:
        """Setup the platform for future use.

        This method should be implemented by any platform that requires user-specific setup to be performed on
        MCLIPlatform creation. This should be idempotent, such that if the setup is already completed, this should be
        a no-op.

        Raises:
            PlatformSetupError: Raised if setup failure prevents use of the platform
        """
        return True

    def get_annotations(self, instance_type: InstanceType) -> Dict[str, str]:
        del instance_type
        return {}

    def get_volumes(self) -> List[MCLIVolume]:
        # pylint: disable-next=import-outside-toplevel
        from mcli.serverside.job.mcli_k8s_job import MCLIVolume

        return [
            MCLIVolume(
                volume=client.V1Volume(
                    name='dshm',
                    empty_dir=client.V1EmptyDirVolumeSource(medium='Memory'),
                ),
                volume_mount=client.V1VolumeMount(
                    name='dshm',
                    mount_path='/dev/shm',
                ),
            ),
        ]

    def get_tolerations(self, instance_type: InstanceType) -> List[Dict[str, str]]:
        del instance_type
        return []

    def get_selectors(self, instance_type: InstanceType) -> Dict[str, str]:
        return instance_type.selectors

    def get_resource_requirements(self, instance_type: InstanceType) -> MCLIK8sResourceRequirements:
        return instance_type.resource_requirements

    def prepare_kubernetes_job_for_platform(
        self,
        kubernetes_job: MCLIK8sJob,
        instance_type: InstanceType,
        priority_class: Optional[str] = None,
    ) -> None:
        """Modifies a MCLIK8sJob with the proper specs of the Platform

        Args:
            kubernetes_job: The MCLIK8sJob object to that represents the K8s job
            instance_type: The instance type to use on the platform
            priority_class: An optional priority class to assign the job to
        """
        kubernetes_job.metadata.namespace = self.namespace
        kubernetes_job.spec.backoff_limit = 0
        kubernetes_job.pod_spec.node_selector.update(self.get_selectors(instance_type))
        kubernetes_job.pod_spec.container.resources = self.get_resource_requirements(instance_type)

        volumes = self.get_volumes()
        for volume in volumes:
            kubernetes_job.add_volume(volume)

        annotations = self.get_annotations(instance_type=instance_type)
        pts = kubernetes_job.pod_template_spec
        pts.metadata.annotations = safe_update_optional_dictionary(pts.metadata.annotations, annotations)

        pod_spec = kubernetes_job.pod_spec
        pod_spec.priority_class_name = self.get_priority_class_label(priority_class_override=priority_class)
        pod_spec.tolerations = safe_update_optional_list(pod_spec.tolerations, self.get_tolerations(instance_type))

        pod_spec.restart_policy = 'Never'
        pod_spec.host_ipc = True

        # Add secrets to job
        self.secret_manager.add_secrets_to_job(kubernetes_job=kubernetes_job)
