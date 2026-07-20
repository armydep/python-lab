"""Tests for Phase 9. Skipped until you implement each exercise."""

import os
import time

import pytest

from timing import timed
from logged import logged
from retry_deco import retry
from memo import memoize
from timer_cm import Timer, timer
from chdir_cm import working_directory


def test_timed_passes_result_and_metadata():
    @timed
    def add(a, b):
        "adds"
        return a + b

    assert add(2, 3) == 5
    assert add.__name__ == "add"
    assert add.__doc__ == "adds"
    assert add.last_elapsed >= 0


def test_logged_prints_and_passes_through(capsys):
    @logged(prefix="XX")
    def double(x):
        return x * 2

    assert double(4) == 8
    out = capsys.readouterr().out
    assert "XX" in out and "double" in out
    assert double.__name__ == "double"


def make_flaky(fail_times, exc=OSError):
    state = {"n": 0}

    def flaky():
        state["n"] += 1
        if state["n"] <= fail_times:
            raise exc("boom")
        return "ok"

    flaky.state = state
    return flaky


def test_retry_decorator_retries():
    flaky = make_flaky(2)
    wrapped = retry(attempts=3, on=(OSError,))(flaky)
    assert wrapped() == "ok"
    assert flaky.state["n"] == 3


def test_retry_decorator_gives_up():
    flaky = make_flaky(9)
    wrapped = retry(attempts=3, on=(OSError,))(flaky)
    with pytest.raises(OSError):
        wrapped()
    assert flaky.state["n"] == 3


def test_retry_decorator_ignores_other_errors():
    flaky = make_flaky(9, exc=KeyError)
    wrapped = retry(attempts=3, on=(OSError,))(flaky)
    with pytest.raises(KeyError):
        wrapped()
    assert flaky.state["n"] == 1


def test_memoize_caches():
    calls = []

    @memoize
    def square(x):
        calls.append(x)
        return x * x

    assert square(4) == 16
    assert square(4) == 16
    assert square(5) == 25
    assert calls == [4, 5]  # second square(4) came from the cache


def test_timer_class_records_elapsed():
    with Timer() as t:
        time.sleep(0.01)
    assert t.elapsed >= 0.01


def test_timer_class_records_on_exception():
    t = Timer()
    with pytest.raises(ValueError):
        with t:
            time.sleep(0.01)
            raise ValueError("body failed")
    assert t.elapsed >= 0.01  # elapsed recorded despite the exception


def test_timer_contextmanager_variant():
    with timer():
        pass  # implementation-defined result; just must not blow up


def test_working_directory_restores(tmp_path):
    before = os.getcwd()
    with working_directory(tmp_path):
        assert os.getcwd() == str(tmp_path)
    assert os.getcwd() == before


def test_working_directory_restores_on_exception(tmp_path):
    before = os.getcwd()
    with pytest.raises(ValueError):
        with working_directory(tmp_path):
            raise ValueError("boom")
    assert os.getcwd() == before
