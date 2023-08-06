from __future__ import annotations

from random import randrange

from sand.datatypes import Color

group_colors: dict[str, Color] = {}


def get_group_colors_dict() -> dict[str, Color]:
    return group_colors


def get_group_color(group_name: str) -> Color:
    if group_name in group_colors:
        return group_colors[group_name]
    red = randrange(256)
    green = randrange(256)
    blue = randrange(256)
    group_colors[group_name] = Color(red, green, blue)
    return group_colors[group_name]


def get_lidar_color(lidar_name: str) -> Color:
    red = 0
    green = 255
    blue = int(lidar_name[1]) * 50
    if lidar_name[7] == "a":
        red = 255
    return Color(blue, green, red)
