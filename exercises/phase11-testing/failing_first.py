"""Exercise 11.5 — TDD: red / green / refactor.

Implement roman_numeral(n) -> str for 1..3999 STRICTLY test-first:
1. RED: write one failing test in test_failing_first.py, run it, see red.
2. GREEN: minimal code here to pass. 3. Repeat, growing cases (4, 9, 40,
1994...). Commit at each red/green step so git history shows the cycle.
Out-of-range -> ValueError.

Skills practiced:
- Test-driven development (red / green / refactor)
"""


def roman_numeral(n: int) -> str:
    if not 1 <= n <= 3999:
        raise ValueError("n must be between 1 and 3999")

    values = (
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    )
    result = []

    for value, numeral in values:
        count, n = divmod(n, value)
        result.append(numeral * count)

    return "".join(result)
