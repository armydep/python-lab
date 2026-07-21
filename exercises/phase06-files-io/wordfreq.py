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


def top_words(path, n=10):
    raise NotImplementedError


if __name__ == "__main__":
    pass  # demo with a friendly FileNotFoundError message
