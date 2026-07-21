"""Exercise 6.2 — JSON round-tripping.

Part A (script): build a dict containing a tuple, a set, and an int-keyed
dict; dump to JSON and load back; document every difference in comments.

Part B: to_jsonable(obj) / from_jsonable(obj) converters that make the
round trip FAITHFUL for dicts/lists containing tuples, sets, and int keys.
Any encoding scheme you like (e.g. tagged dicts {"__set__": [...]}) — the
test only checks: from_jsonable(json.loads(json.dumps(to_jsonable(x)))) == x.

Skills practiced:
- json dump/load
- Lossy JSON round-tripping (tuple/set/int keys)
- Writing faithful converters
"""

import json


def to_jsonable(obj):
    """Convert supported Python containers into JSON-safe tagged values."""
    if isinstance(obj, tuple):
        return {"__type__": "tuple", "items": [to_jsonable(x) for x in obj]}
    if isinstance(obj, set):
        return {"__type__": "set", "items": [to_jsonable(x) for x in obj]}
    if isinstance(obj, dict):
        items = [[to_jsonable(k), to_jsonable(v)] for k, v in obj.items()]
        return {"__type__": "dict", "items": items}
    if isinstance(obj, list):
        return [to_jsonable(x) for x in obj]
    return obj


def from_jsonable(obj):
    """Restore Python containers previously produced by ``to_jsonable``."""
    if isinstance(obj, list):
        return [from_jsonable(x) for x in obj]
    if not isinstance(obj, dict) or "__type__" not in obj:
        return obj
    items = obj["items"]
    if obj["__type__"] == "tuple":
        return tuple(from_jsonable(x) for x in items)
    if obj["__type__"] == "set":
        return {from_jsonable(x) for x in items}
    if obj["__type__"] == "dict":
        return {from_jsonable(k): from_jsonable(v) for k, v in items}
    raise ValueError(f"unknown encoded type: {obj['__type__']}")


if __name__ == "__main__":
    original = {
        "point": (10, 20),
        "tags": {"python", "json"},
        "users": {1: "Alice", 2: "Bob"},
    }

    try:
        json.dumps(original)
    except TypeError as error:
        print("Normal JSON encoding failed:", error)

    encoded = json.dumps(original, default=list)
    restored = json.loads(encoded)
    print("Original:", original)
    print("JSON:", encoded)
    print("Restored:", restored)

    # Observations:
    # 1. json.dumps cannot normally serialize a set; it raises TypeError.
    # 2. default=list lets this experiment continue, but the set becomes a
    #    list and loses its type (its element order is not guaranteed).
    # 3. The tuple is encoded as a JSON array and loads back as a list.
    # 4. Integer dictionary keys load back as strings because JSON object keys
    #    must be strings. The restored object is therefore not equal to the
    #    original object.
