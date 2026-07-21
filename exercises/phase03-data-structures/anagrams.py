"""Exercise 3.5 — group anagrams.

group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) returns a dict
keyed by "".join(sorted(word)) with lists of the original words:
{"aet": ["eat", "tea", "ate"], "ant": ["tan", "nat"], "abt": ["bat"]}

Skills practiced:
- Grouping by a computed key
- sorted() on a string
- Building a dict of lists
"""


def group_anagrams(words):
    groups = {}

    for word in words:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)

    return groups
