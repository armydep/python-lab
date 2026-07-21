"""Exercise 3.2 — invert a mapping.

invert_roles({"alice": "admin", "bob": "user", "carol": "admin"})
-> {"admin": ["alice", "carol"], "user": ["bob"]}   (insertion order kept)

Write it twice: once with a plain dict + setdefault, once with
collections.defaultdict (invert_roles_dd). Same output either way.

Skills practiced:
- dict.setdefault
- collections.defaultdict
- Inverting a mapping into a dict of lists
"""

from collections import defaultdict

def invert_roles(users):
    roles = {}
    for user, role in users.items():
        roles.setdefault(role, []).append(user)
    return roles


def invert_roles_dd(users):
    roles = defaultdict(list)
    for user, role in users.items():
        roles[role].append(user)
    return roles