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
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        current = self.n
        self.n -= 1
        return current

def countdown_gen(n):
    while n > 0:
        yield n
        n -= 1


def desugared(iterable):
    """Collect items into a list using only iter()/next() — no for loop."""
    iterator = iter(iterable)
    result = []
    while True:
        try:
            item = next(iterator)
            result.append(item)
        except StopIteration:
            break
    return result
