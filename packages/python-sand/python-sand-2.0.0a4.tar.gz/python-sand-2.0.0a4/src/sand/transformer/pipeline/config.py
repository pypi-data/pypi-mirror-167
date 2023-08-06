from __future__ import annotations

from overrides import overrides

from sand.config import SandConfig
from sand.config.config import ConfigTransformerConfig
from sand.datatypes import CalPoints, Topic
from sand.interfaces.config import ConfigurationManager
from sand.interfaces.synchronization import SandNode
from sand.util.config import get_group_config_by_group_name

original_transformations: dict[str, CalPoints] = {}


class ConfigTransformer(
    SandNode,
    ConfigurationManager[ConfigTransformerConfig],
):
    def __init__(
        self,
        global_config: SandConfig,
    ) -> None:
        SandNode.__init__(self, global_config.communication)
        ConfigurationManager.__init__(self, self, global_config)

        self.subscribe_topic(
            "+/+/data/position",
            self.push_position,
        )

    @overrides
    def select_config(self, global_config: SandConfig) -> ConfigTransformerConfig:
        return global_config.config_transformer

    def push_position(self, topic: Topic, position: dict[str, int]) -> None:
        split_topic = topic.split("/")
        group = split_topic[1]
        self.log.d(f"new position {group=}", "push_position")
        scale = self.config.scale
        group_config = get_group_config_by_group_name(self.global_config, group)
        if group_config is None:
            self.log.d("group_config is None", "push_position")
            return
        posx = (
            position["x_position"] * scale + group_config.offset_x
            if group_config.transform_x
            else 0
        )
        posy = (
            position["y_position"] * scale + group_config.offset_y
            if group_config.transform_y
            else 0
        )
        _posz = (
            position["z_position"] * scale + group_config.offset_z
            if group_config.transform_z
            else 0
        )

        group_names = [dx.name for dx in self.global_config.groups]

        for cam in self.global_config.cameras:
            if cam.group == group and group in group_names:
                if cam.name not in original_transformations:
                    original_transformations[cam.name] = cam.transformation
                new_target_transformation = [
                    (dx.x + posx, dx.y + posy)
                    for dx in original_transformations[cam.name].target_points
                ]
                # publish new transformation
                self.log.d(
                    f"new position camera:{cam.name} group:{cam.group} original:{original_transformations[cam.name].target_points} new:{new_target_transformation}",
                    "push_position",
                )
                topic = f"{ConfigurationManager.__name__}/{cam.name}/data/cameras/transformation_target_points"
                self.publish(
                    str(new_target_transformation),
                    topic,
                )
