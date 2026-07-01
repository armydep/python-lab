# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A personal Python-learning repo working through Microsoft's "Python for Beginners" (`part-1/`) and "More Python for Beginners" (`part-2/`) courses, plus some standalone exercises. Pure standard library — `pyproject.toml` declares no dependencies, and `uv.lock` has no packages. Requires Python >= 3.13.

## Commands

Each part (`part-1/`, `part-2/`) is a self-contained test root: run `unittest` from inside that part's directory, not from the repo root — each part has its own `tests` package, and running discovery from the repo root would make `tests.test_12_loops` (part-1) and `tests.test_02_lambdas` (part-2) collide as duplicate top-level module names.

```bash
# Run every test in one part
cd part-1 && python3 -m unittest discover
cd part-2 && python3 -m unittest discover

# Run one topic's tests (from inside that part's directory)
python3 -m unittest tests.test_12_loops

# Run a single test method
python3 -m unittest tests.test_12_loops.LoopsChallengeTest.test_first_even_numbers

# Run an example script directly (from the repo root)
python3 part-1/examples/hello.py
```

There is no lint/build step — this is exercise code, not a package meant to be installed.

## Layout and conventions

- `part-1/`, `part-2/` — one per source course; each mirrors the same internal layout:
  - `examples/` — runnable, already-complete sample code (only present in `part-1/` so far).
  - `exercises/` — numbered files (`01_numbers.py`, ...) with functions to implement; edit these in place.
  - `NN-topic/` folders — one per lesson topic, holding a `challenge.py` whose functions/classes intentionally raise `NotImplementedError` until solved. The number matches the source course's lesson number (part-1 uses `python-for-beginners/NN - Topic/`, part-2 uses `more-python-for-beginners/NN - Topic/`). Some folders have extra local modules (e.g. `part-1/15-packages/helpers.py`, imported directly by that folder's `challenge.py`).
  - `tests/test_NN_topic.py` — the checks for each corresponding topic/exercise folder, importable as `tests.test_NN_topic` only when run from inside that part's directory.

**Numeric folder names aren't valid Python package/module names**, so topic challenge files can't be imported with a normal `import` statement. `<part>/tests/helpers.py:load_challenge(folder)` works around this: it loads `<folder>/challenge.py` via `importlib.util.spec_from_file_location`, using a module name like `challenge_16_calling_apis`. Every `tests/test_NN_*.py` file calls this helper at module scope (e.g. `loops = load_challenge("12-loops")`) rather than importing the challenge module directly. `part-1/tests/test_arrays.py` predates this helper and duplicates the same `importlib` dance inline for `part-1/11-collections/arrays.py` — follow the `load_challenge` pattern for anything new instead of copying that inline version.

`part-1/16-calling-apis` calls an external Computer Vision-style API but its tests never hit the network: `test_16_calling_apis.py` spins up a local `http.server.HTTPServer` with a mock handler and points `analyze_image()` at it. Similarly, `part-2/09-asynchronous-programming` is a stdlib-only rewrite of the source lesson's `requests`/`aiohttp` HTTP demo — it uses `asyncio.sleep()` to simulate slow I/O instead of adding a third-party dependency, keeping the whole repo dependency-free.

Some `part-1` test classes carry a `@unittest.skip("Disabled while focusing on 12-loops.")` (active on some, commented out on others) so work can focus on one topic at a time without unrelated suites failing. Check for this before assuming a topic's tests are broken or passing — an active skip means the suite isn't actually being exercised.

Not every `part-2` challenge follows the "full function stub" pattern: topics centered on defining classes (`03-classes`, `04-inheritance`, `05-mixins`) ship a minimal class skeleton plus a textual assignment in the module docstring, rather than a stub per method — read the docstring for the actual spec on those.
