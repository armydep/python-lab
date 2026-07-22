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

import os
from pathlib import Path

import pytest

from atomic import atomic_write_text


def test_replace_failure_preserves_original_and_removes_temp_file(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    target = tmp_path / "data.txt"
    target.write_text("original content", encoding="utf-8")

    def fail_replace(source: str, destination: Path) -> None:
        raise OSError("simulated replace failure")

    monkeypatch.setattr(os, "replace", fail_replace)

    with pytest.raises(OSError, match="simulated replace failure"):
        atomic_write_text(target, "new content")

    assert target.read_text(encoding="utf-8") == "original content"
    assert list(tmp_path.iterdir()) == [target]


def test_missing_parent_directory_raises_without_creating_it(
    tmp_path: Path,
) -> None:
    missing_directory = tmp_path / "missing"
    target = missing_directory / "data.txt"

    with pytest.raises(FileNotFoundError):
        atomic_write_text(target, "content")

    assert not missing_directory.exists()
    assert not target.exists()
