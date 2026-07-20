"""Exercise 11.4 — fakes vs mocks.

Write notify_overdue(repo, clock, notifier) in this file: for every task
whose due < clock.now(), call notifier.send(task). Then test it twice:
1. With hand-rolled fakes — a fixed clock, a recording notifier (a list).
2. With unittest.mock.MagicMock + assert_called_once_with.
Compare readability in comments. No patching should be needed — that's
the design lesson.
"""

import pytest


def notify_overdue(repo, clock, notifier):
    raise NotImplementedError


@pytest.mark.skip(reason="TODO: write both test variants (Phase 11.4)")
def test_placeholder():
    ...
