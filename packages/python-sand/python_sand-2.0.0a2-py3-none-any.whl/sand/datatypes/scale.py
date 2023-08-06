from __future__ import annotations

from .types import CalPoints, Dimensions, Image, Point


class Scale:
    def __init__(
        self, input_dimension: Dimensions, output_dimension: Dimensions
    ) -> None:
        self.input_dimension = input_dimension
        self.output_dimension = output_dimension
        self.scale_height = output_dimension.height / input_dimension.height
        self.scale_width = output_dimension.width / input_dimension.width
        self.scale_avg = (self.scale_width + self.scale_height) / 2

    def __str__(self) -> str:
        return (
            f"{self.scale_width} = {self.output_dimension.width} / {self.input_dimension.width} | scale_width = output_width / input_width | "
            f"{self.scale_height} = {self.output_dimension.height} / {self.input_dimension.height} | scale_height = output_height / input_height  "
        )

    def scale_target_calpoints(self, calpoints: CalPoints) -> list[Point]:
        target_points = []
        for point in calpoints.target_points:
            target_points.append(
                Point(int(point.x * self.scale_width), int(point.y * self.scale_height))
            )
        return target_points

    def scale_source_calpoints(self, calpoints: CalPoints) -> list[Point]:
        source_points = []
        for point in calpoints.source_points:
            source_points.append(
                Point(int(point.x * self.scale_avg), int(point.y * self.scale_avg))
            )
        return source_points

    def scale_calpoints(self, calpoints: CalPoints) -> CalPoints:
        return CalPoints(
            self.scale_source_calpoints(calpoints),
            self.scale_target_calpoints(calpoints),
        )

    def scaled_avg_image_dimensions(self, image: Image) -> Dimensions:
        width = int(image.shape[1] * self.scale_avg)
        height = int(image.shape[0] * self.scale_avg)
        return Dimensions(height=height, width=width)

    def scaled_image_dimensions(self, image: Image) -> Dimensions:
        width = int(image.shape[1] * self.scale_width)
        height = int(image.shape[0] * self.scale_height)
        return Dimensions(height=height, width=width)
