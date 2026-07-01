"""Exercise 13: functions.

Based on Microsoft Python for Beginners lesson "13 - Functions".

Replace each NotImplementedError with your own code, then run:

    python3 -m unittest tests.test_13_functions
"""

INVALID_OPERATION_MESSAGE = "Invalid operation please specify ADD or SUBTRACT"


def calculator(
    first_number: int | float | str,
    second_number: int | float | str,
    operation: str,
) -> float | str:
    """Return the result of adding or subtracting two numbers.

    operation should accept "add" or "subtract" in any letter case.
    Return INVALID_OPERATION_MESSAGE for unsupported operations.
    """
    first = float(first_number)
    second = float(second_number)

    normalized_operation = operation.lower()

    if normalized_operation == "add":
        return first + second
    elif normalized_operation == "subtract":
        return first - second
    else:
        return INVALID_OPERATION_MESSAGE
