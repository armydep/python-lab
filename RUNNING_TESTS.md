# Running Tests

Quick reference for running the exercise tests in this repo.

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
pytest exercises/phase02/          # Phase 2 only
pytest exercises/phase03/          # Phase 3 only
# ...
pytest exercises/phase15/          # Phase 15 only

pytest exercises/                  # all phases at once
```

## How to read the output

Unimplemented exercises show as **skipped** (`s`), not failed — the stubs
raise `NotImplementedError`, and `exercises/conftest.py` converts that into a
skip. So the workflow per phase is:

```bash
pytest exercises/phase05/ -rs      # -rs lists each skip + reason = your to-do list
# ...implement an exercise...
pytest exercises/phase05/          # its tests flip skipped -> passed (or failed; fix + rerun)
```

A phase's coding exercises are **done** when its test file shows
`0 skipped, 0 failed`.

Script-style exercises (`predict.py`, the profiling and asyncio experiments)
have no tests — verify those by running them directly, e.g.:

```bash
python exercises/phase13/first_async.py
```

## Useful variants

```bash
pytest exercises/phase06/ -k atomic     # only tests matching a name
pytest exercises/phase09/ -x            # stop at the first failure
pytest exercises/phase11/ --pdb         # drop into the debugger on failure
pytest exercises/ -q                    # one-line summary of everything
pytest exercises/ -rs                   # everything, listing what's still skipped
```

## Phase-specific notes

- **Phase 10 (typing):** pytest only checks runtime behavior. The real gate is
  the type checker — run it per file:
  ```bash
  mypy --strict exercises/phase10/optional_chain.py
  ```
- **Phase 11 (testing):** this phase inverts the pattern — the test files there
  are stubs *you* fill in (that's the exercise). The provided
  `test_failing_first.py` verifies your finished `roman_numeral` kata.
- **Phases 13–14 (concurrency, performance):** mostly measurement scripts with
  no tests by design. The deliverable is the numbers and explanations you
  record in the file comments.

## Coverage (optional)

`pytest-cov` is installed. To see coverage for a phase's target code:

```bash
pytest exercises/phase02/ --cov=exercises/phase02
```

In Phase 11 you'll target TaskForge coverage (>=85%) once the package exists:

```bash
pytest --cov=taskforge
```
