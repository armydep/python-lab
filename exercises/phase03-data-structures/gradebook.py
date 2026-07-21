"""Exercise 3.3 — gradebook aggregation.

Input: list of (subject, score) tuples, e.g. [("math", 90), ("art", 75),
("math", 85)]. Use comprehensions where they help.

subject_averages -> {"math": 87.5, "art": 75.0}
best_subject     -> subject with the highest average ("math")
above(grades, threshold) -> sorted list of subjects whose average > threshold

Skills practiced:
- Grouping values into a dict of lists
- Dict comprehensions
- max(key=...) and sorted() with a filter
"""


def subject_averages(grades):
    scores_by_subject = {}

    for subject, score in grades:
        if subject not in scores_by_subject:
            scores_by_subject[subject] = []
        scores_by_subject[subject].append(score)

    return {
        subject: sum(scores) / len(scores)
        for subject, scores in scores_by_subject.items()
    }


def best_subject(grades):
    averages = subject_averages(grades)
    return max(averages, key=averages.get)


def above(grades, threshold):
    averages = subject_averages(grades)
    return sorted(
        subject
        for subject, average in averages.items()
        if average > threshold
    )
