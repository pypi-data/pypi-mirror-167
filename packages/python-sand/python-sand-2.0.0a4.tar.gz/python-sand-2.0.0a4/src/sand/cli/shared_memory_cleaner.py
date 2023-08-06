from __future__ import annotations

from argparse import ArgumentParser
from multiprocessing.shared_memory import SharedMemory


def _clean_shared_memory(names: list[str]) -> list[str]:
    cleanup_list = []

    for name in names:
        try:
            shared_memory = SharedMemory(name=name)
            shared_memory.unlink()
            cleanup_list.append(name)
        except:  # pylint: disable=bare-except
            pass

    return cleanup_list


def run() -> None:
    parser = ArgumentParser(description="Easily delete existing SharedMemory")

    parser.add_argument(
        "names",
        metavar="NAME",
        type=str,
        nargs="+",
        help="SharedMemory.name to cleanup",
    )

    args = parser.parse_args()

    cleaned = _clean_shared_memory(args.names)

    print(f"Cleaned {len(cleaned)} remaining shared memories, list:")
    print(cleaned)
