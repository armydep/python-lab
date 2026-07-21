"""Exercise 6.1 — word frequencies from a file.

top_words(path, n=10) -> list of (word, count), most common first
(ties: alphabetical). Case-folded, punctuation stripped (string.punctuation
is enough). Always open with encoding="utf-8". FileNotFoundError: let it
propagate here; the __main__ demo catches it with a friendly message.

Skills practiced:
- Reading text files with explicit encoding='utf-8'
- Counting words with a dict/Counter
- Handling FileNotFoundError
"""

import string
import sys


def top_words(path, n=10):
    """Return the most frequent words, breaking count ties alphabetically."""
    frequencies = {}
    with open(path, encoding="utf-8") as file:
        for word in file.read().split():
            word = word.strip(string.punctuation).casefold()
            if word:
                frequencies[word] = frequencies.get(word, 0) + 1
    ordered = sorted(frequencies.items(), key=lambda item: (-item[1], item[0]))
    return ordered[:n]


if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "sample.txt"
    try:
        print(top_words(filename))
    except FileNotFoundError:
        print(f"File not found: {filename}")
