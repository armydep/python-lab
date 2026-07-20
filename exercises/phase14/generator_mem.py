"""Exercise 14.6 — generators as a memory strategy (script).

Generate a 10-million-line synthetic file of numbers (once, to tmp). Sum
them two ways: loading all lines into a list vs streaming with a
generator. Measure peak memory of each with tracemalloc; record the
numbers. Then: name one thing the LIST version can do that the generator
version cannot (the price of streaming).
"""

# TODO
