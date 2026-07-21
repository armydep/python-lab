"""Exercise 3.1 — deduplicate preserving order, two ways.

dedupe_seen uses a seen-set + loop; dedupe_fromkeys uses dict.fromkeys.
Both: ["b","a","b","c","a"] -> ["b","a","c"].
"""


def dedupe_seen(items):
    seen = set()
    result = []

    for item in items:
        if item in seen:
            continue
        seen.add(item)
        result.append(item)

    return result


def dedupe_fromkeys(items):
    return list(dict.fromkeys(items))
