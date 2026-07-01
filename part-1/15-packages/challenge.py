"""Exercise 15: packages and modules.

Based on Microsoft Python for Beginners lesson "15 - Packages".

Replace each NotImplementedError with your own code, then run:

    python3 -m unittest tests.test_15_packages
"""

from helpers import display


def load_display_function():
    """Import and return the display function from helpers.py."""
    return display


def display_message(message: str) -> str:
    """Use helpers.display() to return a normal message."""
    return display(message)


def display_warning(message: str) -> str:
    """Use helpers.display() to return a warning message."""
    return display(message, True)
