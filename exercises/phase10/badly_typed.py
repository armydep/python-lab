"""Exercise 10.6 — when typing exposes bad design (checker exercise).

Write get_names(data, as_string=False) that returns a comma-joined str
when as_string else a list[str]. Try to annotate it honestly
(-> str | list[str]) and watch every CALLER need isinstance checks.

Then refactor into two functions (get_names / get_names_joined) and note
in a comment why the design — not the annotation — was the problem.
"""

# TODO
