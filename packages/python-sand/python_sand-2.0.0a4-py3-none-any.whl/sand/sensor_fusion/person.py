from __future__ import annotations

from numpy import cos, sin

from sand.datatypes import Box, Point
from sand.datatypes.scale import Scale
from sand.sensor_fusion.collision import Collision
from sand.sensor_fusion.heatmap import HeatMap
from sand.util.boxes import get_box_center


class PersonChecker:
    def __init__(
        self,
        heat_map: HeatMap,
        collision: Collision,
        scale: Scale,
    ):
        self.scale = scale
        self.collision = collision
        self.heat_map = heat_map
        self.person_radius = int(self.scale.scale_avg * 75)

    def test(self, box: Box) -> bool:
        center = get_box_center(box)
        collisions = 0
        for angle in range(0, 360, 10):
            point = Point(
                int(
                    self.person_radius * cos(angle) + center.x * self.scale.scale_width
                ),
                int(
                    self.person_radius * sin(angle) + center.y * self.scale.scale_height
                ),
            )
            self.heat_map.add_point_to_heat_map(point)
            collisions += int(self.collision.check_collision(point, "person"))
        return collisions > 0
