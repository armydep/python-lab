"""Exercise 14.1 — membership cost, measured (script).

10_000 needle lookups against a list vs a set vs dict keys, at container
sizes 1_000 / 10_000 / 100_000, using timeit. Print a small table; in
comments, name the growth shape of each column (linear? constant?) and
connect it to the Phase 3 warning about `in list` inside loops.

Skills practiced:
- Measuring membership cost: list vs set vs dict
- timeit; big-O in practice
"""

from collections.abc import Container
from statistics import median
from timeit import repeat


CONTAINER_SIZES = (1_000, 10_000, 100_000)
NUMBER_OF_LOOKUPS = 10_000
REPEATS = 3


def count_matches(needles: list[int], container: Container[int]) -> int:
    """Return how many needles are present in a container."""
    return sum(needle in container for needle in needles)


def measure_membership(needles: list[int], container: Container[int]) -> float:
    """Return the median duration of one 10,000-lookup run."""
    timings = repeat(
        lambda: count_matches(needles, container),
        number=1,
        repeat=REPEATS,
    )
    return median(timings)


def benchmark_size(size: int) -> tuple[float, float, float]:
    """Benchmark list, set, and dictionary membership at one size."""
    values = list(range(size))
    value_set = set(values)
    value_dict = dict.fromkeys(values)

    # Spread successful lookups across the whole range. For sizes below
    # NUMBER_OF_LOOKUPS some needles repeat, but every container performs
    # exactly the same 10,000 membership tests.
    needles = [
        index * size // NUMBER_OF_LOOKUPS
        for index in range(NUMBER_OF_LOOKUPS)
    ]

    list_seconds = measure_membership(needles, values)
    set_seconds = measure_membership(needles, value_set)
    dict_seconds = measure_membership(needles, value_dict)

    expected_matches = NUMBER_OF_LOOKUPS
    assert count_matches(needles, values) == expected_matches
    assert count_matches(needles, value_set) == expected_matches
    assert count_matches(needles, value_dict) == expected_matches

    return list_seconds, set_seconds, dict_seconds


def main() -> None:
    print(
        f"{'Size':>10} | {'List (ms)':>12} | "
        f"{'Set (ms)':>12} | {'Dict (ms)':>12}"
    )
    print("-" * 57)

    for size in CONTAINER_SIZES:
        timings = benchmark_size(size)
        milliseconds = (seconds * 1_000 for seconds in timings)
        list_ms, set_ms, dict_ms = milliseconds
        print(
            f"{size:>10,} | {list_ms:>12.3f} | "
            f"{set_ms:>12.3f} | {dict_ms:>12.3f}"
        )


# List membership is O(n): it scans references from the beginning until it
# finds an equal value (or reaches the end), so its time grows linearly with
# container size. Set and dictionary membership are O(1) on average because
# their hash tables locate a key without scanning every element.
#
# Therefore, `needle in a_list` inside another loop can turn otherwise linear
# work into O(n²). If ordering and duplicates are not part of the membership
# requirement, build a set once and perform the repeated lookups against it.
if __name__ == "__main__":
    main()
