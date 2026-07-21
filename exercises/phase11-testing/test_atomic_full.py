"""Exercise 11.2 — enforce Phase 6's atomicity claim forever.

Using tmp_path: prove atomic_write_text leaves the original file intact
when the write fails partway (monkeypatch os.replace or make the temp-file
write blow up). Also add: target in a directory that doesn't exist — decide
and pin the behavior (error? create?).

Skills practiced:
- The tmp_path fixture
- monkeypatch
- Testing failure paths
"""

import pytest


@pytest.mark.skip(reason="TODO: write the atomic-write test suite (Phase 11.2)")
def test_placeholder():
    ...
