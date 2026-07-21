"""Phase 2 larger assignment — Text Statistics Toolkit.

Pure functions only: no printing, no input, no global mutable state; max 15
lines per function; every function gets a docstring with an example.

run(text, *names, **options) dispatches through ANALYSES by name and
returns {name: result}. Unknown name -> ValueError. See roadmap Phase 2.

Skills practiced:
- Pure functions (no I/O, no global state)
- Keyword-only options
- A name->function registry and dispatcher
- Comprehensions and dict building
"""


def word_count(text):
    return len(text.split())


def char_frequencies(text, *, ignore_case=True, ignore_spaces=True):
    """Return a dict counting characters in text.

    Example: char_frequencies("A a") returns {"a": 2} by default.
    """
    if ignore_case:
        text = text.lower()

    frequencies = {}
    for char in text:
        if ignore_spaces and char.isspace():
            continue
        frequencies[char] = frequencies.get(char, 0) + 1

    return frequencies


def longest_words(text, n=5):
    """Return the n longest words, longest first.

    Example: longest_words("a three seven", n=2) returns ["three", "seven"].
    """
    words = text.split()
    return sorted(words, key=len, reverse=True)[:n]

def average_word_length(text):
    """Return the average word length.

    Example: average_word_length("a bb ccc") returns 2.0.
    """
    words = text.split()
    if not words:
        return 0

    return sum(map(len, words)) / len(words)


def find_words(text, *, starts_with=None, min_length=0):
    """Return words matching the optional prefix and minimum length.

    Example: find_words("bat apple bar", starts_with="ba") returns ["bat", "bar"].
    """
    words = text.split()
    result = []

    for word in words:
        if starts_with is not None and not word.startswith(starts_with):
            continue
        if len(word) < min_length:
            continue
        result.append(word)

    return result


ANALYSES = {
    "words": word_count,
    "chars": char_frequencies,
    "longest": longest_words,
    "average_length": average_word_length,
    "find": find_words,
}


def run(text, *names, **options):
    """Run named analyses on text and return a dict of results.

    Example: run("a bb ccc", "words") returns {"words": 3}.
    """
    results = {}

    for name in names:
        if name not in ANALYSES:
            raise ValueError(f"unknown analysis: {name}")
        results[name] = ANALYSES[name](text, **options)

    return results
