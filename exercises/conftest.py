"""Shared pytest setup for all exercise phases.

- Puts every phase directory on sys.path so tests can import exercise
  modules directly (e.g. `import stats`) no matter which subset you run.
- Turns NotImplementedError into a SKIP: stub exercises raise it, so their
  tests show as skipped until you implement them — then turn green.

Run everything:      pytest exercises/
Run one phase:       pytest exercises/phase02/
See what's left:     pytest exercises/ -rs
"""

import sys
from pathlib import Path

import pytest

HERE = Path(__file__).parent
for phase_dir in sorted(HERE.glob("phase*")):
    if phase_dir.is_dir():
        sys.path.insert(0, str(phase_dir))


@pytest.hookimpl(wrapper=True)
def pytest_runtest_call(item):
    try:
        return (yield)
    except NotImplementedError:
        pytest.skip("exercise not implemented yet")
