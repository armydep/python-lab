# Running Tests

Quick reference for running the exercise tests in this repo.

Phase folders are named `phaseNN-<topic>` (e.g. `phase02-functions`,
`phase07-oop`). Use the full folder name in paths — or tab-complete `phase07`
and let the shell finish it.

## One-time setup

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
```

Re-activate the venv (`source .venv/bin/activate`) in every new terminal.

## Run tests per phase

From the repo root, one command per phase:

```bash
pytest exercises/phase02-functions/          # Phase 2 only
pytest exercises/phase03-data-structures/    # Phase 3 only
# ...
pytest exercises/phase15-design-architecture/

pytest exercises/                            # all phases at once
```

Full folder list:

```
phase01-foundations                 phase09-decorators-context-managers
phase02-functions                   phase10-typing
phase03-data-structures             phase11-testing
phase04-modules-packages            phase12-debugging-logging-stdlib
phase05-exceptions                  phase13-concurrency
phase06-files-io                    phase14-performance-memory
phase07-oop                         phase15-design-architecture
phase08-iterators-generators
```

## How to read the output

Unimplemented exercises show as **skipped** (`s`), not failed — the stubs
raise `NotImplementedError`, and `exercises/conftest.py` converts that into a
skip. So the workflow per phase is:

```bash
pytest exercises/phase05-exceptions/ -rs     # -rs lists each skip + reason = your to-do list
# ...implement an exercise...
pytest exercises/phase05-exceptions/         # its tests flip skipped -> passed (or failed; fix + rerun)
```

A phase's coding exercises are **done** when its test file shows
`0 skipped, 0 failed`.

Script-style exercises (`predict.py`, the profiling and asyncio experiments)
have no tests — verify those by running them directly, e.g.:

```bash
python exercises/phase13-concurrency/first_async.py
```

## Useful variants

```bash
pytest exercises/phase06-files-io/ -k atomic   # only tests matching a name
pytest exercises/phase09-decorators-context-managers/ -x   # stop at first failure
pytest exercises/phase11-testing/ --pdb        # drop into the debugger on failure
pytest exercises/ -q                           # one-line summary of everything
pytest exercises/ -rs                          # everything, listing what's still skipped
```

## Phase-specific notes

- **Phase 10 (typing):** pytest only checks runtime behavior. The real gate is
  the type checker — run it per file:
  ```bash
  mypy --strict exercises/phase10-typing/optional_chain.py
  ```
- **Phase 11 (testing):** this phase inverts the pattern — the test files there
  are stubs *you* fill in (that's the exercise). The provided
  `test_failing_first.py` verifies your finished `roman_numeral` kata.
- **Phases 13–14 (concurrency, performance):** mostly measurement scripts with
  no tests by design. The deliverable is the numbers and explanations you
  record in the file comments.

## Skills tags

Every exercise file's docstring ends with a **Skills practiced** section
listing exactly what it drills — open a file to see what you're about to
practice, or skim a phase folder to preview its focus.

## Coverage (optional)

`pytest-cov` is installed. To see coverage for a phase's target code:

```bash
pytest exercises/phase02-functions/ --cov=exercises/phase02-functions
```

In Phase 11 you'll target TaskForge coverage (>=85%) once the package exists:

```bash
pytest --cov=taskforge
```
