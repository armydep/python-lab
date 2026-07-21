"""Exercise 11.3 — fixture composition (write in this file).

Build: fixture sample_tasks (a list of Task dicts or objects) -> fixture
full_repo depending on sample_tasks (a MemoryRepository preloaded with
them). Tests use full_repo. Add a yield-fixture that asserts an invariant
at TEARDOWN: no duplicate ids exist after any test ran.

This targets your TaskForge code — import from your package once Phase 7
is done (pip install -e . makes it importable from anywhere).

Skills practiced:
- Fixtures and fixture composition
- yield fixtures for teardown assertions
"""

import pytest


@pytest.mark.skip(reason="TODO: write fixtures + tests (Phase 11.3)")
def test_placeholder():
    ...
