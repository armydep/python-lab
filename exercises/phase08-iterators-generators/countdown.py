"""Exercise 8.1 — the iteration protocol by hand, once.

Countdown(3) iterates 3, 2, 1 — class-based, implementing BOTH __iter__
and __next__ (single-use, like a real iterator). Then countdown_gen(n):
the same thing as a 3-line generator.

Finally, in desugared() below: iterate countdown_gen(3) WITHOUT a for
loop — while + next() + except StopIteration — collecting into a list.

Skills practiced:
- The iterator protocol (__iter__ / __next__)
- Generator functions
- Desugaring a for loop into next() + StopIteration
"""


class Countdown:
    def __init__(self, n):
        raise NotImplementedError


def countdown_gen(n):
    raise NotImplementedError


def desugared(iterable):
    """Collect items into a list using only iter()/next() — no for loop."""
    raise NotImplementedError
