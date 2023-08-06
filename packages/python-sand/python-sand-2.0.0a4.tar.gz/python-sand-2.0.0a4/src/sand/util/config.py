from typing import Optional

from sand.config import CameraConfig, GroupConfig, SandConfig


def get_camera_config_by_camera_name(
    global_config: SandConfig, camera_name: str
) -> Optional[CameraConfig]:
    for cam in global_config.cameras:
        if cam.name == camera_name:
            return cam
    return None


def get_group_config_by_group_name(
    global_config: SandConfig, group_name: str
) -> Optional[GroupConfig]:
    for group in global_config.groups:
        if group.name == group_name:
            return group
    return None
