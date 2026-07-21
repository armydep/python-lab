"""Exercise 2.4 — dispatch table.

A calculator where operations live in the OPERATIONS dict mapping "add",
"sub", "mul", "div" to functions (some lambda, some def). No if/elif chains
anywhere in this file.

calculate(op, a, b) looks up and applies; unknown op -> ValueError;
division by zero may propagate ZeroDivisionError.

Skills practiced:
- Functions as first-class values
- Dict dispatch instead of if/elif chains
- lambda vs def
"""

OPERATIONS = {
    "add": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a / b,
}


def calculate(op, a, b):
    if op not in OPERATIONS:
        raise ValueError(f"unknown operation: {op}")

    return OPERATIONS[op](a, b)
