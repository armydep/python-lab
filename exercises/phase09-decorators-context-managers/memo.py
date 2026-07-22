"""Exercise 9.4 — memoization.

Hand-roll @memoize with a dict keyed by args (positional args only is
fine). What breaks with unhashable args? Try it, note it.
Then compare with functools.lru_cache on fib(35) — time both, record
numbers in a comment.

Skills practiced:
- Hand-rolled memoization
- functools.lru_cache
- Limits with unhashable arguments
"""

from functools import wraps

def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    wrapper.cache = cache
    return wrapper