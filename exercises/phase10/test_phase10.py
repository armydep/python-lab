"""Tests for Phase 10 (runtime behavior; the typing itself is checked by
running mypy --strict over this directory — see each file's docstring)."""

import pytest

from optional_chain import find_user, shout_name_guarded, shout_name_or_raise
from generic_first import first


def test_find_user():
    assert find_user(1) == "ada"
    assert find_user(99) is None


def test_shout_name_guarded():
    assert shout_name_guarded(1) == "ADA"
    assert shout_name_guarded(99) == "NOBODY"


def test_shout_name_or_raise():
    assert shout_name_or_raise(2) == "BOB"
    with pytest.raises(KeyError):
        shout_name_or_raise(99)


def test_first():
    assert first([3, 1]) == 3
    assert first([], default=0) == 0
    assert first(iter(()),) is None
