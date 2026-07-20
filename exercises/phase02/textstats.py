"""Phase 2 larger assignment — Text Statistics Toolkit.

Pure functions only: no printing, no input, no global mutable state; max 15
lines per function; every function gets a docstring with an example.

run(text, *names, **options) dispatches through ANALYSES by name and
returns {name: result}. Unknown name -> ValueError. See roadmap Phase 2.
"""


def word_count(text):
    raise NotImplementedError


def char_frequencies(text, *, ignore_case=True, ignore_spaces=True):
    raise NotImplementedError


def longest_words(text, n=5):
    raise NotImplementedError


def average_word_length(text):
    raise NotImplementedError


def find_words(text, *, starts_with=None, min_length=0):
    raise NotImplementedError


ANALYSES = {
    # "words": word_count, ...
}


def run(text, *names, **options):
    raise NotImplementedError
