from __future__ import annotations

from functools import lru_cache
from pathlib import Path


@lru_cache
def get_camera_name(file: str) -> str:
    return file.split(".")[0]


@lru_cache
def get_path_from_camera_name(
    name: str,
    file_ending: str = "jpg",
    folder: Path = Path("images/cameras"),
) -> Path:
    return folder.joinpath(name).with_suffix(f".{file_ending}")
