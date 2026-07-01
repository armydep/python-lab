"""Exercise 01: numbers.

Edit the functions below, then run:

    python3 -m unittest discover
"""


def add(a: int | float, b: int | float) -> int | float:
    """Return the sum of a and b."""
    return a + b


def square(number: int | float) -> int | float:
    """Return number multiplied by itself."""
    return number * number


def is_even(number: int) -> bool:
    """Return True when number is even, otherwise False."""
    return number % 2 == 0


def celsius_to_fahrenheit(celsius: int | float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32
