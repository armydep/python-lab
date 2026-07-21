"""Exercise 2.1 — describe(*numbers) -> (minimum, maximum, mean).

Raise ValueError on empty input. Then call it with a list using unpacking:
describe(*data). See roadmap Phase 2.

Skills practiced:
- *args variadic parameters
- Returning multiple values as a tuple
- Raising ValueError on bad input; call-site unpacking with *
"""


def describe(*numbers):
    if len(numbers) == 0:
        raise ValueError
    return min(numbers), max(numbers), sum(numbers) / len(numbers)
