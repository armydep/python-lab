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


@pytest.mark.skip(reason="TODO: write the textstats test suite (Phase 11.1)")
def test_placeholder():
    ...
