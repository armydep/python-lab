"""Exercise 13.3 — processes for CPU-bound work (script).

A CPU-heavy function (e.g. sum of squares up to 10**7), run 4 times:
sequential vs ThreadPoolExecutor vs ProcessPoolExecutor — all timed.
Threads won't help; processes will. Write the two-line GIL explanation.
NOTE: the ProcessPool part MUST live under if __name__ == "__main__":
— write in a comment what happens on spawn-platforms without the guard.

Skills practiced:
- ProcessPoolExecutor for CPU-bound work
- GIL limits on threads; the __main__ guard for multiprocessing
"""

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from time import perf_counter
from typing import Callable, ParamSpec, TypeVar


UPPER_BOUND = 10**7
NUMBER_OF_TASKS = 4
MAX_WORKERS = 4

P = ParamSpec("P")
T = TypeVar("T")


def sum_of_squares(upper_bound: int = UPPER_BOUND) -> int:
    """Return the sum of the squares below ``upper_bound``."""
    return sum(number * number for number in range(upper_bound))


def run_sequentially(
    upper_bound: int = UPPER_BOUND,
    number_of_tasks: int = NUMBER_OF_TASKS,
) -> list[int]:
    """Run every CPU-bound task in the current process."""
    return [sum_of_squares(upper_bound) for _ in range(number_of_tasks)]


def run_with_threads(
    upper_bound: int = UPPER_BOUND,
    number_of_tasks: int = NUMBER_OF_TASKS,
    max_workers: int = MAX_WORKERS,
) -> list[int]:
    """Run the CPU-bound tasks using a thread pool."""
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        return list(
            executor.map(sum_of_squares, [upper_bound] * number_of_tasks)
        )


def run_with_processes(
    upper_bound: int = UPPER_BOUND,
    number_of_tasks: int = NUMBER_OF_TASKS,
    max_workers: int = MAX_WORKERS,
) -> list[int]:
    """Run the CPU-bound tasks using separate worker processes."""
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        return list(
            executor.map(sum_of_squares, [upper_bound] * number_of_tasks)
        )


def measure(
    operation: Callable[P, T], /, *args: P.args, **kwargs: P.kwargs
) -> tuple[T, float]:
    """Run an operation and return its result and elapsed seconds."""
    start = perf_counter()
    result = operation(*args, **kwargs)
    return result, perf_counter() - start


def main() -> None:
    sequential_results, sequential_seconds = measure(run_sequentially)
    threaded_results, threaded_seconds = measure(run_with_threads)
    process_results, process_seconds = measure(run_with_processes)

    # Checking the results keeps the benchmark honest: all three approaches
    # must have completed the same work.
    assert sequential_results == threaded_results == process_results

    print(f"Sequential:   {sequential_seconds:.2f} seconds")
    print(f"Thread pool:  {threaded_seconds:.2f} seconds")
    print(f"Process pool: {process_seconds:.2f} seconds")


# In standard GIL-enabled CPython, only one thread at a time can execute this
# Python bytecode, so threads do not make the CPU-bound calculation parallel.
# Processes have separate interpreters and separate GILs, allowing tasks to
# execute in parallel when multiple CPU cores are available.
#
# The process-pool call is reached only through this guard. On platforms that
# start workers with "spawn", an unguarded call would be executed again when
# each child imports this module, recursively creating more processes and
# eventually raising a multiprocessing bootstrapping RuntimeError.
if __name__ == "__main__":
    main()
