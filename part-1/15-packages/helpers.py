"""Small helper module for Exercise 15."""


def display(message: str, is_warning: bool = False) -> str:
    """Return a display string for message.

    The Microsoft example prints the warning and message. Returning a string
    keeps this exercise easy to test.
    """
    if is_warning:
        return f"Warning!!\n{message}"
    return message
