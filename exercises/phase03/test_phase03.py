"""Tests for Phase 3. Skipped until you implement each exercise."""

from dedupe import dedupe_seen, dedupe_fromkeys
from invert import invert_roles, invert_roles_dd
from gradebook import subject_averages, best_subject, above
from matrix import transpose_comp, transpose_zip
from anagrams import group_anagrams
from set_ops import in_both, only_first, in_either

USERS = {"alice": "admin", "bob": "user", "carol": "admin"}
GRADES = [("math", 90), ("art", 75), ("math", 85), ("art", 85), ("cs", 100)]


def test_dedupe_both_ways():
    data = ["b", "a", "b", "c", "a"]
    assert dedupe_seen(data) == ["b", "a", "c"]
    assert dedupe_fromkeys(data) == ["b", "a", "c"]
    assert data == ["b", "a", "b", "c", "a"]  # input not mutated


def test_invert():
    expected = {"admin": ["alice", "carol"], "user": ["bob"]}
    assert invert_roles(USERS) == expected
    assert dict(invert_roles_dd(USERS)) == expected


def test_gradebook():
    assert subject_averages(GRADES) == {"math": 87.5, "art": 80.0, "cs": 100.0}
    assert best_subject(GRADES) == "cs"
    assert above(GRADES, 85) == ["cs", "math"]


def test_transpose():
    m = [[1, 2], [3, 4], [5, 6]]
    expected = [[1, 3, 5], [2, 4, 6]]
    assert transpose_comp(m) == expected
    assert transpose_zip(m) == expected


def test_anagrams():
    groups = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert groups["aet"] == ["eat", "tea", "ate"]
    assert groups["ant"] == ["tan", "nat"]
    assert groups["abt"] == ["bat"]


def test_set_ops():
    a, b = ["ann", "bo", "cy"], ["bo", "cy", "dee"]
    assert in_both(a, b) == {"bo", "cy"}
    assert only_first(a, b) == {"ann"}
    assert in_either(a, b) == {"ann", "bo", "cy", "dee"}
