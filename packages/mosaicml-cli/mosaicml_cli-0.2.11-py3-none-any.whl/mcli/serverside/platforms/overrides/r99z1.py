""" R99Z1 Platform Definition """
from typing import Optional

from mcli.serverside.platforms.gpu_type import GPUType
from mcli.serverside.platforms.platform import GenericK8sPlatform
from mcli.serverside.platforms.platform_instances import (LocalPlatformInstances, PlatformInstanceGPUConfiguration,
                                                          PlatformInstances)
from mcli.utils.utils_kube_labels import label

a100_config = PlatformInstanceGPUConfiguration(
    gpu_type=GPUType.A100_40GB,
    gpu_nums=[8, 16, 32, 64, 128, 256],
    gpu_selectors={label.mosaic.cloud.INSTANCE_SIZE: label.mosaic.instance_size_types.OCI_GB4_8},
    cpus=128,
    cpus_per_gpu=16,
    memory=2048,
    memory_per_gpu=256,
    storage=8000,
    storage_per_gpu=1000,
    multinode_rdma_roce=1,
)

cpu_config = PlatformInstanceGPUConfiguration(
    gpu_type=GPUType.NONE,
    gpu_nums=[0],
)

R99Z1_INSTANCES = LocalPlatformInstances(gpu_configurations=[a100_config, cpu_config])


class R99Z1Platform(GenericK8sPlatform):
    """ R99Z1 Platform Overrides """

    allowed_instances: PlatformInstances = R99Z1_INSTANCES

    pod_group_scheduler: Optional[str] = 'scheduler-plugins-scheduler'
