# Python Practice Project

This project is set up for learning Python with small examples, exercises, and tests.

## Layout

- `examples/` contains runnable code samples.
- `exercises/` contains files you edit while practicing.
- `tests/` contains checks for exercise solutions.

## Run Examples

```bash
python3 examples/hello.py
python3 examples/basics.py
```

You can also run any example directly from PyCharm by opening the file and clicking the run button.

## Work On Exercises

Start with:

```bash
exercises/01_numbers.py
```

Replace the `TODO` implementations with your code, then run:

```bash
python3 -m unittest discover
```

If all tests pass, your solution works for the included checks.

## Topic Challenges

Additional challenge folders are organized by topic:

- `12-loops/`
- `13-functions/`
- `14-function-parameters/`
- `15-packages/`
- `16-calling-apis/`
- `17-json/`
- `18-decorators/`

Each folder contains a `challenge.py` file with functions for you to
implement. These files intentionally raise `NotImplementedError` until you
solve them.

Run one topic at a time while you practice:

```bash
python3 -m unittest tests.test_12_loops
python3 -m unittest tests.test_13_functions
python3 -m unittest tests.test_14_function_parameters
python3 -m unittest tests.test_15_packages
python3 -m unittest tests.test_16_calling_apis
python3 -m unittest tests.test_17_json
python3 -m unittest tests.test_18_decorators
```

After you solve all active exercises, run the full test suite:

```bash
python3 -m unittest discover
```

## Add More Practice

For each new topic:

1. Add an example in `examples/`.
2. Add an exercise file in `exercises/`.
3. Add tests in `tests/`.
