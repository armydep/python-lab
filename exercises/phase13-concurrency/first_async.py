"""Exercise 13.4 — the event-loop model made visible (script).

async def fetch(name, delay): await asyncio.sleep(delay); return name.

1. Run three fetches SEQUENTIALLY (awaits in a row) — time it (~sum).
2. Run them CONCURRENTLY with asyncio.gather — time it (~max).
3. THE BIG ONE: replace one asyncio.sleep with time.sleep and rerun the
   concurrent version. Record what happened to the total time and write
   the explanation: what does blocking the loop do to every other task?

Skills practiced:
- async/await and asyncio.gather
- Sequential vs concurrent execution
- How blocking calls freeze the event loop
"""

import asyncio
import time


REQUESTS = (
    ("users", 1.0),
    ("posts", 2.0),
    ("comments", 3.0),
)


async def fetch(name: str, delay: float) -> str:
    """Simulate an asynchronous request."""
    print(f"Starting {name} ({delay:.1f}s)")
    await asyncio.sleep(delay)
    print(f"Finished {name}")
    return name


async def run_sequentially() -> list[str]:
    """Wait for each fetch to finish before starting the next one."""
    results = []
    for name, delay in REQUESTS:
        results.append(await fetch(name, delay))
    return results


async def run_concurrently() -> list[str]:
    """Start all fetches together and wait until all have finished."""
    results = await asyncio.gather(
        *(fetch(name, delay) for name, delay in REQUESTS)
    )
    return list(results)


async def fetch_with_blocking_sleep(name: str, delay: float) -> str:
    """Simulate one request using a blocking call."""
    print(f"Starting {name} ({delay:.1f}s, blocking)")
    time.sleep(delay)
    print(f"Finished {name}")
    return name


async def run_with_one_blocking_call() -> list[str]:
    """Run concurrent-looking tasks while one of them blocks the loop."""
    results = await asyncio.gather(
        fetch("users", 1.0),
        fetch_with_blocking_sleep("posts", 2.0),
        fetch("comments", 3.0),
    )
    return list(results)


async def main() -> None:
    print("Part 1 — sequential")
    start = time.perf_counter()
    sequential_results = await run_sequentially()
    sequential_seconds = time.perf_counter() - start
    print(
        f"Results: {sequential_results}\n"
        f"Sequential time: {sequential_seconds:.2f} seconds\n"
    )

    print("Part 2 — concurrent")
    start = time.perf_counter()
    concurrent_results = await run_concurrently()
    concurrent_seconds = time.perf_counter() - start
    print(
        f"Results: {concurrent_results}\n"
        f"Concurrent time: {concurrent_seconds:.2f} seconds\n"
    )

    print("Part 3 — one blocking call")
    start = time.perf_counter()
    blocking_results = await run_with_one_blocking_call()
    blocking_seconds = time.perf_counter() - start
    print(
        f"Results: {blocking_results}\n"
        f"Time with blocking call: {blocking_seconds:.2f} seconds"
    )


# time.sleep() does not yield control to the event loop. While "posts" is
# sleeping, the loop cannot resume "users" or even start "comments". Only
# after the blocking sleep returns can the other tasks make progress, so the
# two-second block and the later three-second async sleep take about five
# seconds instead of overlapping in about three.
if __name__ == "__main__":
    asyncio.run(main())
