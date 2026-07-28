# TaskForge Phase 6 Assignment

## Milestone

TaskForge v0.2 — durable JSON persistence and CSV interchange.

## Goal

Persist TaskForge tasks safely across CLI sessions, explicitly convert Python
types that JSON cannot represent, and support CSV export/import without
weakening the Phase 5 error boundary.

The dependency direction becomes:

```text
__main__ → cli → core
              └→ storage → errors
```

`core.py` remains independent of files and paths. The storage adapter owns
serialization and filesystem behavior; the CLI decides when to load and save.

## Phase 6 small exercises

Complete the exercises under `exercises/phase06-files-io/`:

1. `wordfreq.py`
2. `jsonround.py`
3. `logscan.py`
4. `csv_clean.py`
5. `treewalk.py`
6. `atomic.py`

Run:

```bash
python -m pytest -q exercises/phase06-files-io
```

## Starting point

Phase 5 is complete:

- The standalone Phase 6 exercise suite currently passes: `7 passed`.
- Expected domain failures use the `TaskForgeError` hierarchy.
- Core validation rejects invalid and duplicate tasks and unknown IDs.
- The CLI is the shared expected-error boundary.
- Unexpected programming errors are not swallowed.
- `abuse.py` demonstrates ten hostile public-API scenarios.
- Phase 5 and TaskForge tests pass.

## Task 1: add `StorageError`

Extend `src/taskforge/errors.py` with:

```text
TaskForgeError
└── StorageError
```

`StorageError` represents expected persistence failures that the CLI can
report through its existing `TaskForgeError` boundary. It must carry useful
path/context information and belong to the explicit public API if external
callers are expected to catch it.

Corrupt JSON must raise `StorageError` with the original
`json.JSONDecodeError` preserved as `__cause__`.

## Task 2: create the JSON storage adapter

Create:

```text
taskforge/src/taskforge/storage.py
```

Required public functions:

```python
load_tasks(path) -> list[dict]
save_tasks(path, tasks) -> None
```

Contracts:

- Accept `pathlib.Path` paths.
- Always use UTF-8 for text.
- A missing file loads as an empty task list.
- Saving creates missing parent directories.
- Task tags are stored in JSON as sorted lists.
- Loaded tag lists are converted back to sets.
- A save/load round trip preserves task data.
- Storage code contains no CLI input or printing.

Keep conversion logic explicit. JSON does not natively preserve Python sets.

## Task 3: make saving atomic

`save_tasks()` must not write directly over the target file.

Required flow:

```text
serialize/write temporary file in target directory
    ↓
flush and close successfully
    ↓
atomically replace target with temporary file
```

Use the atomic-write pattern practised in `atomic.py`, based on a temporary
file in `path.parent` and `os.replace`.

If serialization or writing fails, an existing target must remain unchanged.
Clean up abandoned temporary files when practical.

## Prepared storage tests

`tests/test_storage.py` already specifies the first storage contracts:

- Missing file returns `[]`.
- Save/load round trip is faithful.
- JSON stores tags as sorted lists.
- Save creates parent directories.
- Corrupt JSON raises chained `StorageError`.
- Failed save preserves the previous file.

Until `taskforge.storage` exists, this test module is skipped:

```bash
python -m pytest -q taskforge/tests/test_storage.py
```

Once the module is created, the tests become active and should initially
fail until each contract is implemented.

## Task 4: define the default data path

The CLI stores tasks at:

```text
~/.taskforge/tasks.json
```

Build this with `Path.home()` and `/`, not string concatenation. Directory
creation belongs in the storage boundary.

Keep the path definition centralized so tests and later configuration work do
not need to patch scattered constants.

## Task 5: connect persistence to the CLI

Update `src/taskforge/cli.py`:

- Load tasks once when the REPL starts.
- Missing storage begins with an empty list.
- Save after every successful mutating command.
- Do not save after read-only commands.
- Do not save when a mutating command fails.
- Let `StorageError` reach the existing `TaskForgeError` boundary.

Current mutating commands include `add` and `done`; CSV import will also
mutate stored tasks.

Avoid putting file operations into `core.py`.

## Task 6: add CSV export and import

Add CLI commands:

```text
export csv <path>
import csv <path>
```

Requirements:

- Use the `csv` module.
- Open CSV files with `newline=""` and `encoding="utf-8"`.
- Export every task field in a documented stable format.
- Encode tags so your own importer can reconstruct the original tag set.
- Import your own exported file without data loss.
- Skip malformed rows and report their line numbers.
- Valid rows should still import when other rows are malformed.
- Successful import triggers persistent JSON saving.

Keep CSV parsing/formatting out of the core domain operations. A separate
adapter module is appropriate if `cli.py` would otherwise own conversion
details.

## Task 7: refactor the Phase 1 quiz data

Move the Phase 1 quiz questions into a JSON file and update the quiz program
to load them from disk.

Requirements:

- Preserve existing quiz behavior.
- Use `pathlib`.
- Specify UTF-8 explicitly.
- Keep data separate from program logic.

This is independent of TaskForge persistence but is part of the Phase 6
roadmap assignment.

## Tests to add during implementation

After the storage adapter, add focused tests for:

- CLI loads existing tasks at startup.
- Successful mutation saves once.
- Failed mutation does not save.
- Read-only commands do not save.
- `StorageError` is reported and the REPL remains alive.
- CSV export/import round trips all task fields and tags.
- Bad CSV rows are skipped and reported with line numbers.

Prefer temporary paths and injected/patchable boundaries. Tests must never
write to the real `~/.taskforge` directory.

## Manual durability verification

In addition to pytest, prove the atomic guarantee manually:

1. Save a valid task file.
2. Introduce a deliberate failure during the next save.
3. Confirm the original file remains valid and unchanged.
4. Remove the deliberate failure.

Run CSV round-trip verification:

```text
export tasks → clear/in a separate store → import tasks → compare exactly
```

Tags must remain sets in memory after importing or loading.

## Completion criteria

Phase 6 TaskForge is complete when:

- All six Phase 6 small exercises pass.
- `StorageError` is typed, contextual, and chains JSON decode failures.
- Missing JSON loads as an empty task list.
- JSON save/load preserves every task field.
- Tags are sorted lists on disk and sets in memory.
- Saving is atomic and crash-safe.
- CLI sessions persist successful mutations.
- Failed and read-only commands do not trigger incorrect saves.
- CSV export/import round-trips tasks, including tags.
- Malformed CSV rows are skipped and reported.
- The quiz reads questions from JSON.
- All TaskForge tests pass without touching the real home directory.

## Recommended implementation order

1. Complete the six Phase 6 exercises.
2. Add and export `StorageError`.
3. Create `storage.py` with missing-file behavior.
4. Implement JSON conversion and round-trip behavior.
5. Make saving atomic.
6. Connect load/save to the CLI.
7. Add CSV export/import and tests.
8. Refactor the quiz data.
9. Run every Phase 6 and TaskForge test.
10. Commit and tag TaskForge v0.2.
