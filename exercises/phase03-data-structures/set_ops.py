"""Exercise 3.6 — set operations on username lists.

Each function takes two lists and returns a set — ONE expression each,
using set operators (&, -, |).

Skills practiced:
- Set operators & - |
- Single-expression solutions
"""


def in_both(first, second):
    return set(first) & set(second)


def only_first(first, second):
    return set(first) - set(second)


def in_either(first, second):
    return set(first) | set(second)
