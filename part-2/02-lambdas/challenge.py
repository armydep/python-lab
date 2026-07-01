"""Exercise 02: lambdas.

Based on Microsoft More Python for Beginners lesson "02 - Lambdas".

Replace each NotImplementedError with your own code, then run:

    python3 -m unittest tests.test_02_lambdas
"""

from typing import Any


def sort_by_field(records: list[dict[str, Any]], field: str) -> list[dict[str, Any]]:
    """Return a new list of records sorted by field using a lambda key.

    Do not mutate the input list.
    """
    raise NotImplementedError


def sort_by_name_length(names: list[str]) -> list[str]:
    """Return a new list of names sorted from shortest to longest.

    Practice using a lambda as the sort key.
    """
    raise NotImplementedError


def square_all(numbers: list[int | float]) -> list[int | float]:
    """Return a new list with each number squared.

    Practice using map() with a lambda.
    """
    raise NotImplementedError


def keep_even(numbers: list[int]) -> list[int]:
    """Return a new list containing only the even numbers.

    Practice using filter() with a lambda.
    """
    raise NotImplementedError
