"""Exercise 2.3 — closures.

make_counter() returns a function that returns 1, 2, 3... on successive
calls (closure + nonlocal). Two counters made separately must not share
state.
"""


def make_counter():
    val = 0
    def counter():
        nonlocal val
        val = val + 1
        return val
    return counter
