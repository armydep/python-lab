"""Exercise 14.6 — generators as a memory strategy (script).

Generate a 10-million-line synthetic file of numbers (once, to tmp). Sum
them two ways: loading all lines into a list vs streaming with a
generator. Measure peak memory of each with tracemalloc; record the
numbers. Then: name one thing the LIST version can do that the generator
version cannot (the price of streaming).

Skills practiced:
- Generators as a memory strategy
- tracemalloc peak comparison
"""

import gc
import tracemalloc
from collections.abc import Callable, Iterator
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import TypeVar


NUMBER_OF_LINES = 10_000_000
T = TypeVar("T")


def generate_number_file(path: Path, number_of_lines: int) -> None:
    """Write numbers incrementally without constructing a large list."""
    with path.open("w", encoding="utf-8") as file:
        file.writelines(f"{number}\n" for number in range(number_of_lines))


def sum_with_list(path: Path) -> int:
    """Load every parsed number into memory, then sum the list."""
    with path.open(encoding="utf-8") as file:
        numbers = [int(line) for line in file]
    return sum(numbers)


def read_numbers(path: Path) -> Iterator[int]:
    """Yield one parsed number at a time."""
    with path.open(encoding="utf-8") as file:
        for line in file:
            yield int(line)


def sum_with_generator(path: Path) -> int:
    """Sum numbers while keeping only the current item in memory."""
    return sum(read_numbers(path))


def measure_peak_memory(
    operation: Callable[[Path], T], path: Path
) -> tuple[T, int]:
    """Return an operation's result and peak traced memory."""
    gc.collect()
    tracemalloc.start()
    try:
        result = operation(path)
        _, peak_bytes = tracemalloc.get_traced_memory()
        return result, peak_bytes
    finally:
        tracemalloc.stop()


def main() -> None:
    with TemporaryDirectory() as temporary_directory:
        path = Path(temporary_directory) / "numbers.txt"
        print(f"Generating {NUMBER_OF_LINES:,} lines...")
        generate_number_file(path, NUMBER_OF_LINES)

        list_total, list_peak = measure_peak_memory(sum_with_list, path)
        generator_total, generator_peak = measure_peak_memory(sum_with_generator, path)

    assert list_total == generator_total

    print(f"Sum: {list_total:,}")
    print(
        f"{'Approach':<12} | {'Peak MiB':>12} | "
        f"{'Bytes/line':>12}"
    )
    print("-" * 43)
    for name, peak_bytes in (
        ("List", list_peak),
        ("Generator", generator_peak),
    ):
        print(
            f"{name:<12} | {peak_bytes / (1024 * 1024):>12.2f} | "
            f"{peak_bytes / NUMBER_OF_LINES:>12.2f}"
        )


# The list retains all parsed integers, so its memory grows O(n). The
# generator yields one integer at a time and releases it after sum consumes
# it, so its auxiliary memory stays O(1) as the file grows.
#
# In exchange for that low memory use, a generator is single-pass: unlike the
# list, it cannot be indexed, traversed backward, or iterated again without
# reopening/recomputing the source.
if __name__ == "__main__":
    main()
