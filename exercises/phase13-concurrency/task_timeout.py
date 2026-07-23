"""Exercise 13.5 — timeouts and partial failure (script).

Five tasks with random delays (0.1–2s):
1. Run them under asyncio.timeout(1.0) (or wait_for) — handle
   TimeoutError; what happened to the unfinished tasks?
2. Make one task raise; compare gather(...) vs
   gather(..., return_exceptions=True) — print exactly what comes back in
   each case and label the items.

Skills practiced:
- asyncio timeouts (wait_for / timeout)
- gather(return_exceptions=True)
"""

import asyncio
import random


NUMBER_OF_TASKS = 5
TIMEOUT_SECONDS = 1.0
RANDOM_SEED = 42


async def do_work(
    name: str, delay: float, should_fail: bool = False
) -> str:
    """Simulate one asynchronous task."""
    print(f"{name}: started, needs {delay:.2f}s")
    try:
        await asyncio.sleep(delay)
    except asyncio.CancelledError:
        print(f"{name}: cancelled before completion")
        raise

    if should_fail:
        print(f"{name}: failed")
        raise ValueError(f"{name} could not produce a result")

    print(f"{name}: completed")
    return f"{name} result"


async def run_with_timeout() -> None:
    """Run five tasks together, allowing at most one second in total."""
    rng = random.Random(RANDOM_SEED)
    delays = [rng.uniform(0.1, 2.0) for _ in range(NUMBER_OF_TASKS)]
    tasks = [
        asyncio.create_task(
            do_work(f"Task {index}", delay), name=f"Task {index}"
        )
        for index, delay in enumerate(delays, start=1)
    ]

    try:
        async with asyncio.timeout(TIMEOUT_SECONDS):
            results = await asyncio.gather(*tasks)
            print(f"All results: {results}")
    except TimeoutError:
        print(f"\nTimed out after {TIMEOUT_SECONDS:.1f}s")

    print("\nFinal task states:")
    for task in tasks:
        if task.cancelled():
            status = "cancelled"
        elif task.done():
            status = f"completed -> {task.result()!r}"
        else:
            status = "still pending"
        print(f"{task.get_name()}: {status}")


def create_failure_demo_tasks(label: str) -> list[asyncio.Task[str]]:
    """Create five fresh tasks, with Task 2 configured to fail."""
    rng = random.Random(RANDOM_SEED)
    delays = [rng.uniform(0.1, 0.5) for _ in range(NUMBER_OF_TASKS)]
    return [
        asyncio.create_task(
            do_work(
                f"{label} Task {index}",
                delay,
                should_fail=index == 2,
            ),
            name=f"{label} Task {index}",
        )
        for index, delay in enumerate(delays, start=1)
    ]


async def compare_gather_error_handling() -> None:
    """Compare gather's default behavior with return_exceptions=True."""
    print("\nDefault gather:")
    tasks = create_failure_demo_tasks("Default")
    try:
        results = await asyncio.gather(*tasks)
        print(f"gather returned: {results}")
    except ValueError as error:
        print(f"gather raised: {type(error).__name__}: {error}")
        print("No result list was returned.")

    # Default gather propagates the first exception but does not cancel the
    # other tasks. Wait for them here so their output cannot leak into the
    # next, independent demonstration.
    await asyncio.gather(*tasks, return_exceptions=True)

    print("\ngather(return_exceptions=True):")
    tasks = create_failure_demo_tasks("Collected")
    results = await asyncio.gather(*tasks, return_exceptions=True)

    for task, result in zip(tasks, results, strict=True):
        if isinstance(result, BaseException):
            print(
                f"{task.get_name()}: exception -> "
                f"{type(result).__name__}: {result}"
            )
        else:
            print(f"{task.get_name()}: value -> {result!r}")


async def main() -> None:
    print("Part 1 — timeout and cancellation")
    await run_with_timeout()

    print("\nPart 2 — partial failure")
    await compare_gather_error_handling()


# When the timeout expires, it cancels the task executing the gather().
# gather() propagates that cancellation to its unfinished child tasks.
# Tasks that finished before the deadline keep their results; unfinished
# tasks receive CancelledError and are shown as cancelled below.
#
# By default, gather() immediately propagates the first exception and returns
# no result list; its other awaitables are not automatically cancelled.
# With return_exceptions=True, it waits for every task and returns exceptions
# in the result list at the same positions as the failed awaitables.
if __name__ == "__main__":
    asyncio.run(main())
