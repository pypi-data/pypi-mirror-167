from __future__ import annotations

from sand.datatypes import Box, Point
from sand.datatypes.third_party.mlcvzoo import BoundingBox


def approximation(box: Box) -> Box:
    delta_x = box.lower_left.x - box.lower_right.x
    delta_y = box.lower_left.y - box.lower_right.y
    upper_left = Point(box.lower_left.x - delta_y, box.lower_left.y - delta_x)
    upper_right = Point(box.lower_right.x - delta_y, box.lower_right.y - delta_x)
    return Box(upper_left, upper_right, box.lower_right, box.lower_left)


def get_box_center(box: Box) -> Point:
    delta_x = box.lower_right.x - box.upper_left.x
    delta_y = box.lower_right.y - box.upper_left.y
    delta_x_half = delta_x / 2
    delta_y_half = delta_y / 2
    lower_mid = Point(
        int(box.upper_left.x + delta_x_half), int(box.upper_left.y + delta_y_half)
    )
    return lower_mid


def scale_point_list(
    points: list[Point], scale_x: float, scale_y: float
) -> list[Point]:
    return list(
        map(
            lambda point: Point(int(point.x * scale_x), int(point.y * scale_y)),
            points,
        ),
    )


def scale_transformed_boxes(
    transformed_boxes: list[Box], scale_x: float, scale_y: float
) -> list[Box]:
    return list(
        map(
            lambda b: Box(
                lower_right=Point(
                    x=int(b.lower_right.x * scale_x),
                    y=int(b.lower_right.y * scale_y),
                ),
                lower_left=Point(
                    x=int(b.lower_left.x * scale_x),
                    y=int(b.lower_left.y * scale_y),
                ),
                upper_right=Point(
                    x=int(b.upper_right.x * scale_x),
                    y=int(b.upper_right.y * scale_y),
                ),
                upper_left=Point(
                    x=int(b.upper_left.x * scale_x),
                    y=int(b.upper_left.y * scale_y),
                ),
            ),
            transformed_boxes,
        ),
    )


def bounding_box_to_point_list(
    bounding_box: BoundingBox, image_size: tuple[int, int]
) -> list[Point]:
    bbox = bounding_box.box

    # print(bbox.xmin, bbox.ymin, bbox.xmax, bbox.ymax)
    # |-----------------------|
    # |[0]                 [1]|
    # |                       |
    # |                       |
    # |                       |
    # |                       |
    # |                       |
    # |[3]                 [2]|
    # |-----------------------|
    # So folks... this diagram is in POV of the camera, not in any relation to the crane.
    # In theory are point 2 and 3 near ne crane.
    # So most of the time thats the bottom line of a Person and use to correct boxes for cameras with flat view point.
    def get_point(xcoord: int, ycoord: int) -> Point:
        yvalue = ycoord
        xvalue = xcoord
        if ycoord >= image_size[1]:
            yvalue = image_size[1] - 1
        if xcoord >= image_size[0]:
            xvalue = image_size[0] - 1
        return Point(int(xvalue), int(yvalue))

    return [
        get_point(bbox.xmin, bbox.ymin),
        get_point(bbox.xmax, bbox.ymin),
        get_point(bbox.xmax, bbox.ymax),
        get_point(bbox.xmin, bbox.ymax),
    ]
