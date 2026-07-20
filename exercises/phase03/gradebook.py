"""Exercise 3.3 — gradebook aggregation.

Input: list of (subject, score) tuples, e.g. [("math", 90), ("art", 75),
("math", 85)]. Use comprehensions where they help.

subject_averages -> {"math": 87.5, "art": 75.0}
best_subject     -> subject with the highest average ("math")
above(grades, threshold) -> sorted list of subjects whose average > threshold
"""


def subject_averages(grades):
    raise NotImplementedError


def best_subject(grades):
    raise NotImplementedError


def above(grades, threshold):
    raise NotImplementedError
