"""Exercise 14.5 — caching: the win and the trap (script).

1. An expensive pure function (recursive fib or a slow computation) called
   with repeating args in a loop: time it, add functools.cache, time again
   — record the numbers.
2. The trap: show a case where caching is WRONG — a function whose result
   depends on mutable state or time. Demonstrate the stale result and
   write the rule: what must be true of a function before you cache it?

Skills practiced:
- functools.cache wins
- When caching is wrong (mutable or time-dependent results)
"""

from collections.abc import Callable
from functools import cache
from time import perf_counter
from typing import TypeVar


FIBONACCI_INPUTS = (30, 31, 32, 30, 31, 32)
T = TypeVar("T")


def fibonacci(number: int) -> int:
    """Calculate a Fibonacci number with intentionally repeated work."""
    if number < 2:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


@cache
def cached_fibonacci(number: int) -> int:
    """Calculate Fibonacci while remembering results by argument."""
    if number < 2:
        return number
    return cached_fibonacci(number - 1) + cached_fibonacci(number - 2)


def measure(operation: Callable[[], T]) -> tuple[T, float]:
    """Return an operation's result and elapsed seconds."""
    start = perf_counter()
    result = operation()
    return result, perf_counter() - start


def run_fibonacci_calls(
    function: Callable[[int], int],
) -> list[int]:
    """Call a Fibonacci implementation with repeating arguments."""
    return [function(number) for number in FIBONACCI_INPUTS]


# This mutable value is a hidden input to the function below.
tax_settings = {"rate": 0.10}


def price_with_tax(price: float) -> float:
    """Calculate a price using the current mutable tax setting."""
    return price * (1 + tax_settings["rate"])


@cache
def incorrectly_cached_price_with_tax(price: float) -> float:
    """Demonstrate caching a function with a hidden mutable dependency."""
    return price * (1 + tax_settings["rate"])


def demonstrate_stale_cache() -> None:
    """Show that a cache can return a result that is no longer correct."""
    price = 100.0
    tax_settings["rate"] = 0.10
    incorrectly_cached_price_with_tax.cache_clear()

    first = incorrectly_cached_price_with_tax(price)
    tax_settings["rate"] = 0.20
    stale = incorrectly_cached_price_with_tax(price)
    current = price_with_tax(price)

    print("\nPart 2 — the caching trap")
    print(f"At 10% tax:             {first:.2f}")
    print(f"Cached after 20% tax:   {stale:.2f}  <- stale")
    print(f"Correct after 20% tax:  {current:.2f}")


def main() -> None:
    uncached_results, uncached_seconds = measure(
        lambda: run_fibonacci_calls(fibonacci)
    )

    cached_fibonacci.cache_clear()
    cached_results, cached_seconds = measure(
        lambda: run_fibonacci_calls(cached_fibonacci)
    )

    assert uncached_results == cached_results

    print("Part 1 — caching a pure function")
    print(f"Without cache: {uncached_seconds:.6f} seconds")
    print(f"With cache:    {cached_seconds:.6f} seconds")
    print(f"Speedup:       {uncached_seconds / cached_seconds:,.1f}x")
    print(f"Cache info:    {cached_fibonacci.cache_info()}")

    demonstrate_stale_cache()


# Cache a function only when the same arguments always produce the same
# result and the result has no hidden dependency on mutable state, time, I/O,
# randomness, or other external conditions. Its arguments must also be
# hashable because functools.cache stores results in a dictionary.
if __name__ == "__main__":
    main()
