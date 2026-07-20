"""Exercise 2.1 — describe(*numbers) -> (minimum, maximum, mean).

Raise ValueError on empty input. Then call it with a list using unpacking:
describe(*data). See roadmap Phase 2.
"""


def describe(*numbers):
    if len(numbers) == 0:
        raise ValueError
    return min(numbers), max(numbers), sum(numbers) / len(numbers)
