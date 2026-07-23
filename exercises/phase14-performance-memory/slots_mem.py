"""Exercise 14.4 — memory, measured with tracemalloc (script).

One million small task-like objects, three representations: a regular
dataclass, a dataclass with slots=True, a plain tuple. Measure peak memory
for each with tracemalloc (build, snapshot, report bytes/object). In
comments: the ranking, the trade-offs, and why sys.getsizeof alone would
have lied to you.

Skills practiced:
- __slots__ memory savings
- Measuring with tracemalloc
"""

import gc
import tracemalloc
from collections.abc import Callable
from dataclasses import dataclass
from typing import TypeAlias, TypeVar


NUMBER_OF_TASKS = 1_000_000
T = TypeVar("T")


@dataclass
class RegularTask:
    """Task whose fields are stored in a per-instance attribute dictionary."""

    title: str
    priority: int
    completed: bool


@dataclass(slots=True)
class SlottedTask:
    """Task whose fields are stored in fixed slots."""

    title: str
    priority: int
    completed: bool


# A plain tuple has the same values in the same order, but it has no field
# names at runtime. The alias documents what each position means.
TaskTuple: TypeAlias = tuple[str, int, bool]


def make_task_tuple(title: str, priority: int, completed: bool) -> TaskTuple:
    """Construct the plain-tuple task representation."""
    return title, priority, completed


def measure_peak_memory(
    factory: Callable[[str, int, bool], T],
) -> tuple[int, float]:
    """Return peak allocated bytes and peak bytes per task."""
    gc.collect()
    tracemalloc.start()

    tasks = [
        factory("Task", 1, False)
        for _ in range(NUMBER_OF_TASKS)
    ]

    _, peak_bytes = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Keep the objects alive until after the peak has been recorded.
    assert len(tasks) == NUMBER_OF_TASKS
    return peak_bytes, peak_bytes / NUMBER_OF_TASKS


def main() -> None:
    representations = (
        ("Regular dataclass", RegularTask),
        ("Slotted dataclass", SlottedTask),
        ("Plain tuple", make_task_tuple),
    )

    print(
        f"{'Representation':<20} | "
        f"{'Peak MiB':>10} | {'Bytes/object':>12}"
    )
    print("-" * 49)

    for name, factory in representations:
        peak_bytes, bytes_per_object = measure_peak_memory(factory)
        peak_mib = peak_bytes / (1024 * 1024)
        print(
            f"{name:<20} | {peak_mib:>10.2f} | "
            f"{bytes_per_object:>12.2f}"
        )


# Measured ranking on this CPython build: regular dataclass > tuple > slotted
# dataclass. A regular instance has a separate attribute dictionary. A slotted
# instance avoids that dictionary and, for these three fields, is even smaller
# than the tuple object. A tuple is still compact, but its positions are less
# descriptive and its values cannot be reassigned. Exact byte counts can vary
# by Python version and platform.
#
# sys.getsizeof() reports only an object's shallow size. It can omit separate
# allocations such as a regular instance's __dict__, as well as the list
# holding all the objects. tracemalloc observes the complete allocation made
# while each collection is built, giving a more meaningful comparison.
if __name__ == "__main__":
    main()
