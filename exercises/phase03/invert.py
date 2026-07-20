"""Exercise 3.2 — invert a mapping.

invert_roles({"alice": "admin", "bob": "user", "carol": "admin"})
-> {"admin": ["alice", "carol"], "user": ["bob"]}   (insertion order kept)

Write it twice: once with a plain dict + setdefault, once with
collections.defaultdict (invert_roles_dd). Same output either way.
"""


def invert_roles(users):
    raise NotImplementedError


def invert_roles_dd(users):
    raise NotImplementedError
