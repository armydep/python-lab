"""Exercise 09: asynchronous programming.

Based on Microsoft More Python for Beginners lesson
"09 - Asynchronous programming".

The original lesson fetches URLs with requests/aiohttp. This exercise
simulates the same "slow I/O" shape with asyncio.sleep() so it stays
dependency-free.

Replace each NotImplementedError with your own code, then run:

    python3 -m unittest tests.test_09_asynchronous_programming
"""

import asyncio


async def load_data(delay: float) -> str:
    """Simulate a slow load: wait delay seconds, then return a result string.

    Return the string f"data-after-{delay}s".
    """
    raise NotImplementedError


async def load_all(delays: list[float]) -> list[str]:
    """Run load_data(delay) for every delay in delays concurrently.

    Use asyncio.gather() and return the results in the same order as delays.
    """
    raise NotImplementedError


def run_all(delays: list[float]) -> list[str]:
    """Synchronously run load_all(delays) with asyncio.run() and return the result."""
    raise NotImplementedError
