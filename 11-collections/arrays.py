"""Exercise 11: arrays.

Edit the functions below, then run:

    python3 -m unittest discover
"""

from array import array


def make_scores(values: list[int | float]) -> array:
    """Return a floating-point array containing the given score values."""
    return array("d", [score for score in values])


def add_score(scores: array, score: int | float) -> array:
    """Append score to scores and return the same array."""
    scores.append(score)
    return scores


def average_score(scores: array) -> float:
    """Return the average score, or 0.0 when scores is empty."""
    raise NotImplementedError


def highest_score(scores: array) -> int | float | None:
    """Return the highest score, or None when scores is empty."""
    raise NotImplementedError


def first_even_numbers(count: int) -> array:
    """Return an integer array with the first count non-negative even numbers."""
    raise NotImplementedError


def to_list(values: array) -> list[int | float]:
    """Convert an array to a regular Python list."""
    raise NotImplementedError
