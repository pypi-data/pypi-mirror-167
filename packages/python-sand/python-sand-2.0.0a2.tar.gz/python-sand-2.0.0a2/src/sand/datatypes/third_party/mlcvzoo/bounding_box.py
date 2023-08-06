""" Class for Bounding Box Annotation"""

from dataclasses import dataclass

from .box import Box
from .class_identifier import ClassIdentifier


@dataclass
class BoundingBox:
    class_identifier: ClassIdentifier
    box: Box
    score: float
    difficult: bool
    occluded: bool
    content: str

    @property
    def class_id(self) -> int:
        return self.class_identifier.class_id

    @property
    def class_name(self) -> str:
        return self.class_identifier.class_name
