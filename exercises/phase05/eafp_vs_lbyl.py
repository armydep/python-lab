"""Exercise 5.5 — EAFP vs LBYL (script, no test).

Read cfg["db"]["port"] from a nested dict three ways:
1. LBYL: `in` checks at each level
2. EAFP: try/except KeyError
3. .get chains with defaults

Run each against: a complete cfg, cfg missing "db", cfg missing "port".
In comments: which reads best? Which can silently hide a real bug (typo in
a key)? Which would you use in TaskForge and why?
"""

# TODO
