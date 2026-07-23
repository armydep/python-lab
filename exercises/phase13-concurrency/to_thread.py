"""Exercise 13.7 — escaping to blocking code (script).

An async main runs a 'heartbeat' task printing a dot every 0.2s, alongside
a blocking function (time.sleep(2) standing in for your JSON load):
1. Call the blocking function DIRECTLY inside async — the heartbeat
   freezes. Observe and record.
2. Wrap it in await asyncio.to_thread(...) — the heartbeat keeps beating.
Record both outputs; one sentence on when you'll need this in FastAPI.

Skills practiced:
- asyncio.to_thread for blocking calls
- Keeping the event loop responsive
"""

import asyncio
import time


HEARTBEAT_INTERVAL = 0.2
BLOCKING_SECONDS = 2.0


def load_json_blocking() -> str:
    """Stand in for a synchronous file or database operation."""
    print("Blocking work started")
    time.sleep(BLOCKING_SECONDS)
    print("Blocking work finished")
    return "loaded data"


async def heartbeat(stop: asyncio.Event, start_time: float) -> None:
    """Print regularly while the event loop remains responsive."""
    while not stop.is_set():
        elapsed = time.perf_counter() - start_time
        print(f". heartbeat at {elapsed:.1f}s")
        await asyncio.sleep(HEARTBEAT_INTERVAL)


async def run_blocking_call_directly() -> None:
    """Call synchronous blocking work directly from async code."""
    print("Part 1 — blocking call directly in async code")
    start_time = time.perf_counter()
    stop = asyncio.Event()
    heartbeat_task = asyncio.create_task(heartbeat(stop, start_time))

    # Let the heartbeat run briefly before blocking the event loop.
    await asyncio.sleep(0.6)
    result = load_json_blocking()
    print(f"Result: {result}")

    # Let it run again so the gap in heartbeat timestamps is visible.
    await asyncio.sleep(0.6)
    stop.set()
    await heartbeat_task


async def run_blocking_call_in_thread() -> None:
    """Move synchronous blocking work off the event-loop thread."""
    print("\nPart 2 — blocking call with asyncio.to_thread")
    start_time = time.perf_counter()
    stop = asyncio.Event()
    heartbeat_task = asyncio.create_task(heartbeat(stop, start_time))

    await asyncio.sleep(0.6)
    result = await asyncio.to_thread(load_json_blocking)
    print(f"Result: {result}")

    await asyncio.sleep(0.6)
    stop.set()
    await heartbeat_task


async def main() -> None:
    await run_blocking_call_directly()
    await run_blocking_call_in_thread()


# Observed output contains a gap of about two seconds between heartbeat
# messages. Calling time.sleep() on the event-loop thread prevents every
# coroutine on that loop from running until the blocking call returns.
#
# With asyncio.to_thread(), the blocking function runs in a worker thread,
# while the event-loop thread remains free to run the heartbeat. In FastAPI,
# use this approach when an async endpoint must call a synchronous, blocking
# library such as a file loader or a database client.
if __name__ == "__main__":
    asyncio.run(main())
