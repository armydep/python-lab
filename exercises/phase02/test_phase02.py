"""Tests for Phase 2. Skipped until you implement each exercise."""

import pytest

from stats import describe
from greet import greet
from make_counter import make_counter
from dispatch import calculate
from apply_n import apply_n, apply_n_recursive
import textstats


def test_describe():
    assert describe(3, 1, 2) == (1, 3, 2.0)
    assert describe(*[5]) == (5, 5, 5.0)


def test_describe_empty_raises():
    with pytest.raises(ValueError):
        describe()


def test_greet():
    assert greet("Ada") == "Hello, Ada!"
    assert greet("Ada", greeting="Hi", punctuation="?") == "Hi, Ada?"


def test_greet_enforces_parameter_kinds():
    with pytest.raises(TypeError):
        greet("Ada", "Hi")          # greeting is keyword-only
    with pytest.raises(TypeError):
        greet(name="Ada")           # name is positional-only


def test_make_counter_counts():
    c = make_counter()
    assert [c(), c(), c()] == [1, 2, 3]


def test_counters_are_independent():
    a, b = make_counter(), make_counter()
    a(), a()
    assert b() == 1


def test_calculate():
    assert calculate("add", 2, 3) == 5
    assert calculate("div", 8, 2) == 4


def test_calculate_unknown_op():
    with pytest.raises(ValueError):
        calculate("pow", 2, 3)


def test_apply_n():
    assert apply_n(lambda x: x * 2, 3, 2) == 12
    assert apply_n(str.upper, "hi", 1) == "HI"
    assert apply_n_recursive(lambda x: x * 2, 3, 0) == 3
    assert apply_n_recursive(lambda x: x + 1, 0, 5) == 5


def test_word_count():
    assert textstats.word_count("the quick brown fox") == 4
    assert textstats.word_count("") == 0


def test_find_words():
    text = "banana bat apple bar"
    assert textstats.find_words(text, starts_with="ba") == ["banana", "bat", "bar"]
    assert textstats.find_words(text, min_length=5) == ["banana", "apple"]


def test_run_dispatches():
    result = textstats.run("a bb ccc", "words")
    assert result == {"words": 3}


def test_run_unknown_name():
    with pytest.raises(ValueError):
        textstats.run("text", "nope")
