"""Exercise 14.2 — string building, measured (script).

Build a 100_000-piece string three ways: += in a loop, "".join(list),
io.StringIO. Time each at sizes 10k/50k/100k. Explain in comments why +=
is quadratic (immutability -> full copy per step) and which you'd use by
default.

Skills practiced:
- String-building cost: += vs join vs StringIO
- Why += in a loop is quadratic
"""

from collections.abc import Callable
from io import StringIO
from statistics import median
from timeit import repeat


SIZES = (10_000, 50_000, 100_000)
REPEATS = 5
PIECE = "abcdefghij"


def build_with_plus_equals(pieces: list[str]) -> str:
    """Build a string using repeated += operations."""
    result = ""
    for piece in pieces:
        result += piece
    return result


def build_with_join(pieces: list[str]) -> str:
    """Build a string with one join operation."""
    return "".join(pieces)


def build_with_string_io(pieces: list[str]) -> str:
    """Build a string by writing pieces to an in-memory text stream."""
    buffer = StringIO()
    for piece in pieces:
        buffer.write(piece)
    return buffer.getvalue()


def measure(builder: Callable[[list[str]], str], pieces: list[str]) -> float:
    """Return the median duration for one complete build."""
    timings = repeat(lambda: builder(pieces), number=1, repeat=REPEATS)
    return median(timings)


def benchmark_size(size: int) -> tuple[float, float, float]:
    """Benchmark all builders with the same input pieces."""
    pieces = [PIECE] * size

    expected = build_with_join(pieces)
    assert build_with_plus_equals(pieces) == expected
    assert build_with_string_io(pieces) == expected

    return (
        measure(build_with_plus_equals, pieces),
        measure(build_with_join, pieces),
        measure(build_with_string_io, pieces),
    )


def main() -> None:
    print(
        f"{'Pieces':>10} | {'+= loop (ms)':>14} | "
        f"{'join (ms)':>12} | {'StringIO (ms)':>14}"
    )
    print("-" * 61)

    for size in SIZES:
        plus_seconds, join_seconds, string_io_seconds = benchmark_size(size)
        print(
            f"{size:>10,} | {plus_seconds * 1_000:>14.3f} | "
            f"{join_seconds * 1_000:>12.3f} | "
            f"{string_io_seconds * 1_000:>14.3f}"
        )


# Strings are immutable, so concatenation may need to allocate a new string
# and copy the accumulated content on every iteration. Copying lengths
# 1 + 2 + ... + n gives O(n²) work in the general case. CPython can optimize
# local `+=` when it knows no other reference observes the old string, so a
# particular CPython run may look closer to linear; code should not depend on
# that implementation detail.
#
# Use "".join(pieces) by default when all pieces are already available: it
# computes the final size and performs one allocation. StringIO is useful when
# pieces are produced incrementally or through a file-like writing interface.
if __name__ == "__main__":
    main()
