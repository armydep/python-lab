# Python Practice Project

This project is set up for learning Python with small examples, exercises, and
tests. Practice is split into parts, one per Microsoft course:

- `part-1/` — based on [Python for Beginners](https://github.com/microsoft/c9-python-getting-started/tree/master/python-for-beginners).
- `part-2/` — based on [More Python for Beginners](https://github.com/microsoft/c9-python-getting-started/tree/master/more-python-for-beginners).

Each part is self-contained and follows the same layout:

- `examples/` contains runnable code samples (currently only in `part-1/`).
- `exercises/` contains files you edit while practicing.
- `NN-topic/` folders (e.g. `12-loops/`, `02-lambdas/`) each hold a
  `challenge.py` file for that topic.
- `tests/` contains the checks for that part's exercises and topic folders.

## How to Run

Each part has its own `tests/` package, so run `unittest` from inside that
part's directory rather than from the repo root.

```bash
# Part 1: run every test
cd part-1
python3 -m unittest discover

# Part 2: run every test
cd part-2
python3 -m unittest discover
```

Run one topic at a time while you practice (from inside that part's
directory):

```bash
# Part 1 examples
python3 -m unittest tests.test_12_loops
python3 -m unittest tests.test_18_decorators

# Part 2 examples
python3 -m unittest tests.test_02_lambdas
python3 -m unittest tests.test_09_asynchronous_programming
```

Run a single test method:

```bash
python3 -m unittest tests.test_12_loops.LoopsChallengeTest.test_first_even_numbers
```

Run an example script directly (from the repo root):

```bash
python3 part-1/examples/hello.py
python3 part-1/examples/basics.py
```

You can also run any example directly from PyCharm by opening the file and
clicking the run button.

## Work On Exercises

Start with:

```bash
part-1/exercises/01_numbers.py
```

Replace the `TODO` implementations with your code, then run that part's
tests as described above. If all tests pass, your solution works for the
included checks.

## Topic Challenges

### Part 1 — Python for Beginners

- `part-1/11-collections/`
- `part-1/12-loops/`
- `part-1/13-functions/`
- `part-1/14-function-parameters/`
- `part-1/15-packages/`
- `part-1/16-calling-apis/`
- `part-1/17-json/`
- `part-1/18-decorators/`

### Part 2 — More Python for Beginners

- `part-2/02-lambdas/`
- `part-2/03-classes/`
- `part-2/04-inheritance/`
- `part-2/05-mixins/`
- `part-2/06-managing-the-file-system/`
- `part-2/07-reading-and-writing-files/`
- `part-2/08-managing-external-resources/`
- `part-2/09-asynchronous-programming/`

Each folder contains a `challenge.py` file with functions or classes for you
to implement. These files intentionally raise `NotImplementedError` until
you solve them.

## Add More Practice

For each new topic within a part:

1. Add a `NN-topic/` folder with a `challenge.py` file.
2. Add a matching test file in that part's `tests/` folder.
3. (`part-1/` only, so far) Add an example in `examples/`.
