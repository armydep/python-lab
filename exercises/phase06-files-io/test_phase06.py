"""Tests for Phase 6. File tests use tmp_path — never your real files.

Skills practiced:
- Reading a pytest suite (with tmp_path) as the spec for phase 6
"""

import json
import os

import pytest

from wordfreq import top_words
from jsonround import to_jsonable, from_jsonable
from logscan import count_levels, last_errors
from csv_clean import clean_csv
from treewalk import py_files_by_size
from atomic import atomic_write_text


def test_top_words(tmp_path):
    f = tmp_path / "text.txt"
    f.write_text("The cat sat. The cat ran! A dog sat.", encoding="utf-8")
    assert top_words(f, n=2) == [("cat", 2), ("sat", 2)]


def test_json_roundtrip_faithful():
    original = {"point": (1, 2), "tags": {"a", "b"}, "by_id": {1: "one"}}
    wire = json.loads(json.dumps(to_jsonable(original)))
    assert from_jsonable(wire) == original


LOG = """2026-07-20T10:00:00 INFO started
2026-07-20T10:00:01 ERROR db down
2026-07-20T10:00:02 WARNING slow query
2026-07-20T10:00:03 ERROR db still down
2026-07-20T10:00:04 INFO recovered
"""


def test_logscan(tmp_path):
    f = tmp_path / "server.log"
    f.write_text(LOG, encoding="utf-8")
    assert count_levels(f) == {"INFO": 2, "ERROR": 2, "WARNING": 1}
    errors = last_errors(f, n=1)
    assert errors == ["2026-07-20T10:00:03 ERROR db still down"]


def test_csv_clean(tmp_path):
    src, dst = tmp_path / "in.csv", tmp_path / "out.csv"
    src.write_text(
        "name,age\n  alice , 30\n\nbob,\ncarol,25\n", encoding="utf-8"
    )
    skipped = clean_csv(src, dst)
    assert skipped  # bob's row lacks age
    cleaned = dst.read_text(encoding="utf-8")
    assert "alice,30" in cleaned.replace("\r", "")
    assert "carol,25" in cleaned.replace("\r", "")
    assert "bob" not in cleaned


def test_py_files_by_size(tmp_path):
    (tmp_path / "big.py").write_text("x = 1\n" * 100, encoding="utf-8")
    sub = tmp_path / "pkg"
    sub.mkdir()
    (sub / "small.py").write_text("pass\n", encoding="utf-8")
    (tmp_path / "not_python.txt").write_text("ignore me", encoding="utf-8")
    result = py_files_by_size(tmp_path)
    names = [p.name for p, _ in result]
    assert names == ["big.py", "small.py"]
    assert result[0][1] > result[1][1]


def test_atomic_write_success(tmp_path):
    target = tmp_path / "data.txt"
    atomic_write_text(target, "hello")
    assert target.read_text(encoding="utf-8") == "hello"
    atomic_write_text(target, "goodbye")
    assert target.read_text(encoding="utf-8") == "goodbye"


def test_atomic_write_preserves_original_on_failure(tmp_path, monkeypatch):
    target = tmp_path / "data.txt"
    target.write_text("precious", encoding="utf-8")

    def broken_replace(src, dst):
        raise OSError("disk on fire")

    monkeypatch.setattr(os, "replace", broken_replace)
    with pytest.raises(OSError):
        atomic_write_text(target, "new content")
    assert target.read_text(encoding="utf-8") == "precious"
