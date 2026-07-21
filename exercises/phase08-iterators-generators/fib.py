"""Exercise 8.3 — infinite generators.

fib() yields 1, 1, 2, 3, 5, 8... forever. first_n(n) returns the first n
as a list (use itertools.islice — no loop counter). first_above(limit)
returns the first Fibonacci number > limit.

Skills practiced:
- Infinite generators
- itertools.islice
- Lazy first-match search
"""


import itertools


def fib():
    previous = 1
    current = 1

    while True:
        yield previous
        previous, current = current, previous + current


def first_n(n):
    return list(itertools.islice(fib(), n))


def first_above(limit):
    for num in fib():
        if num > limit:
            return num
    raise ValueError("No Fibonacci number found above the limit")
