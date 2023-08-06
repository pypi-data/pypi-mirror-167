from __future__ import annotations

from sand.datatypes import CalPoints, Color, Image, Point
from sand.util.image import draw_x


def draw_calibration_points(
    map_image: Image,
    points: CalPoints,
    active_point_index: int = -1,
    draw_source: bool = False,
) -> Image:
    def draw(map_image: Image, points: list[Point]) -> None:
        for pid, point in enumerate(points):
            if pid == active_point_index:
                map_image = draw_x(
                    map_image, point.x, point.y, Color(255, 0, 0), line_width=4, size=50
                )
            else:
                map_image = draw_x(
                    map_image, point.x, point.y, Color(0, 0, 0), line_width=4, size=50
                )

    if draw_source:
        draw(map_image, points.source_points)
    draw(map_image, points.target_points)
    return map_image


def draw_active_calibration_point(map_image: Image, point: Point) -> None:
    draw_x(map_image, point.x, point.y, Color(255, 0, 0), line_width=2)
