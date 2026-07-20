"""Exercise 2.2 — parameter kinds.

Implement greet so that greet("Ada") -> "Hello, Ada!" and
greet("Ada", greeting="Hi", punctuation="?") -> "Hi, Ada?".

Then, in the comments below, try every call form and record which raise
TypeError and why: greet("Ada", "Hi") / greet(name="Ada") / greet("Ada",
greeting="Hi").
"""


def greet(name, /, *, greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"


# Call-form experiments (record result or exact TypeError message):
# greet("Ada", "Hi")          -> TypeError: greet() takes 1 positional argument but 2 were given
# greet(name="Ada")           -> TypeError: greet() got some positional-only arguments passed as keyword arguments: 'name'
# greet("Ada", greeting="Hi") -> "Hi, Ada!"
