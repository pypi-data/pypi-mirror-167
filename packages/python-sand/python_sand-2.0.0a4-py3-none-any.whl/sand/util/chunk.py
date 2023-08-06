from __future__ import annotations

from itertools import chain
from math import floor
from typing import Any, Iterable, Sequence


def chunk(
    items: Sequence[Any],
    chunk_count: int,
    chunk_index: int,
) -> Iterable[int]:
    """Gives an Iterable of indexes corresponding to the {chunk_index}.

    It is guaranteed that there will be exactly {chunk_count} chunks. If the
    ratio does not come out evenly, the *last* chunk will contain the
    difference.

    It is not guaranteed that the chunks will be balanced. This depends on
    {len(items)} and {chunk_count}. The last chunk is technically able to
    contain up to {chunk_count - 1} items more than others.

    Returns an Iterable[int], this means if you exhaust it once it will not
    necessarily reset. If you want to iterate multiple times over the specific
    chunk, use:

        list(chunk([1, 2, 3, 4], 2, 1))

    """
    camera_count = len(items)
    indices = range(camera_count)

    if chunk_count > camera_count:
        raise ValueError(f"{chunk_count=} cannot be higher than {camera_count=}")

    if chunk_count < 2:
        # only one gpu or no multi -> one big group
        return indices

    chunk_size = floor(camera_count / chunk_count)
    chunks = [
        indices[index : index + chunk_size]
        for index in range(0, camera_count, chunk_size)
    ]

    if chunk_index == chunk_count - 1:
        # last one
        return chain(*chunks[chunk_index:])

    return chunks[chunk_index]
