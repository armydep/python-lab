"""Exercise 13.2 — threads for I/O-bound work (script).

Simulate 10 'downloads' (time.sleep(0.5) each): sequential loop vs
ThreadPoolExecutor(max_workers=5). Measure both with time.perf_counter.
In comments: explain the ~5x speedup, and precisely why the GIL did NOT
prevent it (where is the GIL released?).

Skills practiced:
- ThreadPoolExecutor for I/O-bound work
- Why the GIL doesn't block overlapping I/O
"""

from concurrent.futures import ThreadPoolExecutor
from time import perf_counter, sleep
from typing import Callable, ParamSpec, TypeVar


NUMBER_OF_DOWNLOADS = 10
DOWNLOAD_SECONDS = 0.5
MAX_WORKERS = 5

P = ParamSpec("P")
T = TypeVar("T")


def download(item: int, delay: float = DOWNLOAD_SECONDS) -> int:
    """Simulate downloading one item and return its identifier."""
    sleep(delay)
    return item


def download_sequentially(number_of_downloads: int = NUMBER_OF_DOWNLOADS,delay: float = DOWNLOAD_SECONDS) -> list[int]:
    """Run all simulated downloads one after another."""
    return [download(item, delay) for item in range(number_of_downloads)]


def download_with_threads(number_of_downloads: int = NUMBER_OF_DOWNLOADS,
        delay: float = DOWNLOAD_SECONDS,max_workers: int = MAX_WORKERS) -> list[int]:
    """Run simulated downloads concurrently in a thread pool."""
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        return list(executor.map(download,range(number_of_downloads),[delay] * number_of_downloads))


def measure(operation: Callable[P, T], /, *args: P.args, **kwargs: P.kwargs) -> tuple[T, float]:
    """Run an operation and return both its result and elapsed seconds."""
    start = perf_counter()
    result = operation(*args, **kwargs)
    return result, perf_counter() - start


def main() -> None:
    _, sequential_seconds = measure(download_sequentially)
    _, threaded_seconds = measure(download_with_threads)

    print(f"Sequential: {sequential_seconds:.2f} seconds")
    print(f"Thread pool: {threaded_seconds:.2f} seconds")
    print(f"Speedup: {sequential_seconds / threaded_seconds:.1f}x")


if __name__ == "__main__":
    main()


# Sequential execution takes about 10 * 0.5 = 5 seconds. Five workers can
# overlap five sleeps at a time, so the ten downloads finish in two batches,
# taking about 1 second: approximately a 5x speedup.
#
# The GIL protects execution of Python bytecode, but sleep() is implemented as
# a blocking system call and CPython releases the GIL while waiting inside it.
# Thus, while one worker is asleep, another worker can acquire the GIL and
# start its own download. Real blocking I/O APIs generally release the GIL for
# the same reason, allowing their wait times to overlap.
