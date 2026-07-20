"""Exercise 6.2 — JSON round-tripping.

Part A (script): build a dict containing a tuple, a set, and an int-keyed
dict; dump to JSON and load back; document every difference in comments.

Part B: to_jsonable(obj) / from_jsonable(obj) converters that make the
round trip FAITHFUL for dicts/lists containing tuples, sets, and int keys.
Any encoding scheme you like (e.g. tagged dicts {"__set__": [...]}) — the
test only checks: from_jsonable(json.loads(json.dumps(to_jsonable(x)))) == x.
"""


def to_jsonable(obj):
    raise NotImplementedError


def from_jsonable(obj):
    raise NotImplementedError
