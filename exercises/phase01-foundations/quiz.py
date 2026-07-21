"""Phase 1 larger assignment — Terminal Quiz Game.

A multiple-choice quiz that runs in the terminal.

Requirements:
  - Questions live in a list of tuples at the top of this file, e.g.
    ("What does // do?", ["true division", "floor division", "modulo",
    "power"], "b") — at least 8 questions, about Phase 1 material (write
    them yourself; writing questions IS studying).
  - Shuffle question order (random.shuffle).
  - Accept answers a–d; re-prompt on anything else without counting it wrong.
  - Track the score; at the end show a percentage and a letter grade using
    `match` or an elif chain.
  - `--reverse` mode (check sys.argv for now): show the ANSWER text, the user
    picks which QUESTION it belongs to. This must reuse the same question
    data — restructure, don't copy-paste.

Completion check (from the roadmap): survives hostile input — letters where
numbers are expected, empty input, EOF if you're feeling thorough.

Note: in Phase 6 you will move the questions into a JSON file — keep the
data separate from the logic with that in mind.

Skills practiced:
- Loops, branching, and elif/match-based grading
- Lists of tuples as a data table separate from logic
- random.shuffle and hostile-input handling
"""

import random
import sys

QUESTIONS = [
    (
        "What does // do with two numbers?",
        ["true division", "floor division", "modulo", "power"],
        "b",
    ),
    (
        "Which operator gives the remainder after division?",
        ["//", "%", "**", "/"],
        "b",
    ),
    (
        "What does input() return?",
        ["an int", "a float", "a string", "a bool"],
        "c",
    ),
    (
        "Which loop is best when you want to repeat until a condition changes?",
        ["for", "while", "match", "import"],
        "b",
    ),
    (
        "What does str.isdigit() check?",
        [
            "whether a string contains only digit characters",
            "whether a number is even",
            "whether a value is a float",
            "whether a string is empty",
        ],
        "a",
    ),
    (
        "Which function converts a valid numeric string like '42' to an integer?",
        ["str()", "float()", "int()", "bool()"],
        "c",
    ),
    (
        "What does random.shuffle(items) do?",
        [
            "returns a sorted copy of items",
            "changes item order in place",
            "removes duplicates from items",
            "chooses the first item",
        ],
        "b",
    ),
    (
        "What does the elif keyword mean?",
        ["else if", "end loop if", "equal if", "except if"],
        "a",
    ),
]

LETTERS = ["a", "b", "c", "d"]


def answer_index(correct_letter: str) -> int:
    """Return the option index for an answer letter."""
    return LETTERS.index(correct_letter)


def correct_answer_text(question: tuple[str, list[str], str]) -> str:
    """Return the answer text for one question tuple."""
    _, options, correct_letter = question
    return options[answer_index(correct_letter)]


def letter_grade(percentage: float) -> str:
    """Return a letter grade for a numeric percentage."""
    if percentage >= 90:
        return "A"
    if percentage >= 80:
        return "B"
    if percentage >= 70:
        return "C"
    if percentage >= 60:
        return "D"
    return "F"


def read_answer() -> str | None:
    """Read an answer letter, re-prompting until it is valid.

    Returns None on EOF so the quiz can end cleanly instead of crashing.
    """
    while True:
        try:
            answer = input("Your answer (a-d): ").strip().lower()
        except EOFError:
            print()
            return None

        if answer in LETTERS:
            return answer

        print("Please enter a, b, c, or d.")


def print_options(options: list[str]) -> None:
    """Print four answer options labeled a-d."""
    for letter, option in zip(LETTERS, options):
        print(f"  {letter}) {option}")


def ask_normal_question(question: tuple[str, list[str], str]) -> bool | None:
    """Ask one normal-mode question and return whether the user was correct."""
    question_text, options, correct_letter = question

    print()
    print(question_text)
    print_options(options)

    answer = read_answer()
    if answer is None:
        return None

    return answer == correct_letter


def reverse_choices(
    question: tuple[str, list[str], str],
    all_questions: list[tuple[str, list[str], str]],
) -> tuple[list[str], str]:
    """Build shuffled reverse-mode choices and return them with correct letter."""
    correct_question_text = question[0]
    distractors = [
        other_question[0]
        for other_question in all_questions
        if other_question[0] != correct_question_text
    ]
    random.shuffle(distractors)

    choices = [correct_question_text, *distractors[:3]]
    random.shuffle(choices)

    correct_letter = LETTERS[choices.index(correct_question_text)]
    return choices, correct_letter


def ask_reverse_question(
    question: tuple[str, list[str], str],
    all_questions: list[tuple[str, list[str], str]],
) -> bool | None:
    """Ask one reverse-mode question and return whether the user was correct."""
    answer_text = correct_answer_text(question)
    choices, correct_letter = reverse_choices(question, all_questions)

    print()
    print(f"Which question has this answer? {answer_text!r}")
    print_options(choices)

    answer = read_answer()
    if answer is None:
        return None

    return answer == correct_letter


def run_quiz(reverse: bool = False) -> None:
    """Run the quiz and print the final score."""
    questions = QUESTIONS.copy()
    random.shuffle(questions)

    score = 0
    answered = 0

    for question in questions:
        if reverse:
            result = ask_reverse_question(question, QUESTIONS)
        else:
            result = ask_normal_question(question)

        if result is None:
            print("Quiz ended early.")
            break

        answered += 1
        if result:
            score += 1
            print("Correct.")
        else:
            print("Incorrect.")

    if answered == 0:
        print("No questions answered.")
        return

    percentage = score / answered * 100
    grade = letter_grade(percentage)

    print()
    print(f"Score: {score}/{answered}")
    print(f"Percentage: {percentage:.1f}%")
    print(f"Grade: {grade}")


def main() -> None:
    """Run the terminal quiz game."""
    reverse = "--reverse" in sys.argv[1:]
    run_quiz(reverse)


if __name__ == "__main__":
    main()
