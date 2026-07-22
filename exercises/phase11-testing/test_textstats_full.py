"""Exercise 11.1 — YOU write the tests (this phase inverts the pattern).

Target: your finished Phase 2 textstats.py. Requirements:
- @pytest.mark.parametrize word_count over ≥6 cases: empty string,
  punctuation-only, unicode words, repeated words, multiple spaces,
  newlines.
- pytest.raises for run() with an unknown analysis name, checking the
  message.
- At least one test you WATCHED FAIL first (break the code, not the test);
  note which one in a comment.

Delete this docstring's TODO status by replacing the placeholder below
with real tests.

Skills practiced:
- Writing parametrized pytest tests
- pytest.raises
- Edge-case tables; watching a test fail first
"""

import pytest

from textstats import run, word_count


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", 0),
        ("!!! ???", 2),
        ("שלום עולם", 2),
        ("echo echo echo", 3),
        ("one    two\tthree", 3),
        ("first\nsecond\nthird", 3),
    ],
)
def test_word_count_edge_cases(text: str, expected: int) -> None:
    # Watched fail first: temporarily making word_count return 0 broke the
    # repeated-words case before the correct implementation was restored.
    assert word_count(text) == expected


def test_run_rejects_unknown_analysis_with_clear_message() -> None:
    with pytest.raises(ValueError, match=r"^unknown analysis: missing$"):
        run("some text", "missing")
