"""Tests for Phase 8. Skipped until you implement each exercise.

Skills practiced:
- Reading a pytest suite as the spec for phase 8 iteration
"""

import pytest

from countdown import Countdown, countdown_gen, desugared
from fib import fib, first_n, first_above
import pipeline
from chunks import chunked
from groupby_trap import counts_by_key


def test_countdown_class():
    assert list(Countdown(3)) == [3, 2, 1]


def test_countdown_is_single_use():
    c = Countdown(3)
    list(c)
    assert list(c) == []  # a true iterator exhausts


def test_countdown_gen():
    g = countdown_gen(3)
    assert next(g) == 3          # lazy: nothing computed until asked
    assert list(g) == [2, 1]


def test_desugared():
    assert desugared(countdown_gen(3)) == [3, 2, 1]
    assert desugared([]) == []


def test_fib():
    assert first_n(6) == [1, 1, 2, 3, 5, 8]
    assert first_above(100) == 144


LOG = (
    "2026-07-20T10:00:00 INFO started\n"
    "\n"
    "2026-07-20T10:00:01 ERROR db down\n"
    "2026-07-20T10:00:02 ERROR disk full\n"
)


def test_pipeline(tmp_path):
    f = tmp_path / "server.log"
    f.write_text(LOG, encoding="utf-8")
    messages = pipeline.to_messages(
        pipeline.only_errors(pipeline.parse(pipeline.read_lines(f)))
    )
    assert not isinstance(messages, list)  # must be lazy
    assert list(messages) == ["db down", "disk full"]


def test_pipeline_stages_are_lazy(tmp_path):
    f = tmp_path / "server.log"
    f.write_text(LOG, encoding="utf-8")
    for stage_result in (
        pipeline.read_lines(f),
        pipeline.parse(iter([])),
        pipeline.only_errors(iter([])),
    ):
        assert iter(stage_result) is iter(stage_result)  # iterator, not container


def test_chunked():
    assert list(chunked([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]
    assert list(chunked((x for x in range(4)), 4)) == [[0, 1, 2, 3]]
    assert list(chunked([], 3)) == []


def test_chunked_bad_size():
    with pytest.raises(ValueError):
        list(chunked([1], 0))


def test_counts_by_key_on_unsorted_input():
    pairs = [("b", 1), ("a", 1), ("b", 2), ("c", 1), ("a", 3)]
    assert counts_by_key(pairs) == {"a": 2, "b": 2, "c": 1}
