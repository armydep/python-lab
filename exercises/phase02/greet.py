"""Exercise 2.2 — parameter kinds.

Implement greet so that greet("Ada") -> "Hello, Ada!" and
greet("Ada", greeting="Hi", punctuation="?") -> "Hi, Ada?".

Then, in the comments below, try every call form and record which raise
TypeError and why: greet("Ada", "Hi") / greet(name="Ada") / greet("Ada",
greeting="Hi").
"""


def greet(name, /, *, greeting="Hello", punctuation="!"):
    raise NotImplementedError


# Call-form experiments (record result or exact TypeError message):
# greet("Ada", "Hi")        ->
# greet(name="Ada")         ->
# greet("Ada", greeting="Hi") ->
