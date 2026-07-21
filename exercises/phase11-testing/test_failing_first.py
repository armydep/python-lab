"""Your TDD test file for roman_numeral — grow it case by case (11.5).

A few final-state checks are provided so the finished kata is verified;
your own incremental tests should come above them.

Skills practiced:
- Parametrized final-state tests
- Growing a test suite case by case
"""

import pytest

from failing_first import roman_numeral

# --- your incremental TDD tests go here ---


@pytest.mark.parametrize(
    ("n", "expected"),
    [(1, "I"), (4, "IV"), (9, "IX"), (14, "XIV"), (40, "XL"),
     (90, "XC"), (400, "CD"), (1994, "MCMXCIV"), (3999, "MMMCMXCIX")],
)
def test_roman_final(n, expected):
    assert roman_numeral(n) == expected


@pytest.mark.parametrize("n", [0, -1, 4000])
def test_roman_out_of_range(n):
    with pytest.raises(ValueError):
        roman_numeral(n)
