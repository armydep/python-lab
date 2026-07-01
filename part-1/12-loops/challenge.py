"""Exercise 12: loops.

Based on Microsoft Python for Beginners lesson "12 - Loops".

Replace each NotImplementedError with your own code, then run:

    python3 -m unittest tests.test_12_loops
"""


def collect_names(names: list[str]) -> list[str]:
    """Return a new list containing each name in the same order.

    Practice using a for loop.
    """
    result: list[str] = []

    for name in names:
        result.append(name)

    return result



def indexes_for_items(items: list[object]) -> list[int]:
    """Return the valid indexes for items.

    Example: ["a", "b", "c"] should return [0, 1, 2].
    Practice using a while loop and len().
    """
    indexes = []
    for i in range(len(items)):
        indexes.append(i)
    return indexes


def first_even_numbers(count: int) -> list[int]:
    """Return the first count non-negative even numbers.

    Example: count=5 should return [0, 2, 4, 6, 8].
    Practice using range().
    """
    result: list[int] = []

    for number in range(count):
        result.append(number * 2)

    return result


def total_numbers(numbers: list[int | float]) -> int | float:
    """Return the sum of all numbers.

    Practice looping over numeric values and keeping a running total.
    """
    total: int | float = 0

    for number in numbers:
        total += number

    return total
