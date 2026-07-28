# TaskForge Phase 5 Assignment

## Milestone

TaskForge v0.2a — robust core.

## Goal

Give TaskForge a typed domain-error hierarchy, validate invalid task input at
the core boundary, and make the CLI the single place that translates expected
domain failures into friendly user-facing messages.

The dependency direction remains:

```text
__main__ → cli → core → errors
```

The inner modules raise errors but never print or terminate the application.
The CLI catches expected TaskForge errors because it is the application
boundary.

## Phase 5 small exercises

Complete and verify the exercises under `exercises/phase05-exceptions/`:

1. `safe_convert.py`
2. `retry.py`
3. `hierarchy.py`
4. `finally_order.py`
5. `eafp_vs_lbyl.py`

Run them with:

```bash
python -m pytest -q exercises/phase05-exceptions
```

## Starting point

Phase 4 is complete:

- TaskForge uses an installable `src` layout.
- The project is installed in editable mode.
- The public v0.1 operations are exported by `taskforge`.
- `taskforge` and `python -m taskforge` launch the same REPL.
- The `version` command reads `taskforge.__version__`.
- Phase 4 and TaskForge tests pass.

## Completed task 1: create the domain-error hierarchy

Create:

```text
taskforge/src/taskforge/errors.py
```

Required hierarchy:

```text
TaskForgeError
├── TaskNotFound
├── InvalidTask
└── DuplicateTask
```

Contracts:

- `TaskForgeError` is the common base for expected TaskForge domain errors.
- `TaskNotFound` carries the requested `task_id`.
- `InvalidTask` carries a human-readable validation `reason`.
- `DuplicateTask` carries the conflicting task `title`.
- Each error must produce a useful one-line message when converted to `str`.

Decide which error classes belong to the package's public API and make those
exports explicit in `taskforge/__init__.py`.

## Completed task 2: validate core input

Update `src/taskforge/core.py` so invalid domain input raises the new typed
errors.

Required validation:

- An empty or whitespace-only title raises `InvalidTask`.
- A negative priority raises `InvalidTask`.
- Adding a duplicate title raises `DuplicateTask`.
- Completing an unknown ID raises `TaskNotFound`.
- Removing an unknown ID raises `TaskNotFound`.

Core rules:

- Core functions never print.
- Core functions never call `exit`.
- Core functions do not catch errors they cannot fix.
- Do not replace domain errors with generic `Exception`.
- Preserve the existing mutate-versus-return contracts.

Document whether duplicate-title comparison is case-sensitive and whether
surrounding title whitespace is normalized or merely validated. Use the same
rule consistently.

## Completed task 3: make the CLI the error boundary

Update `src/taskforge/cli.py`.

Wrap command dispatch with one narrow handler:

```text
TaskForgeError → friendly one-line CLI message → REPL continues
```

Requirements:

- Catch `TaskForgeError` at the command-dispatch boundary.
- Keep the REPL alive after expected domain errors.
- Continue handling command-syntax conversion errors meaningfully.
- Do not catch `Exception`.
- Unexpected programming errors must still escape with a traceback.

The CLI may print errors; `core.py` and `errors.py` may not.

## Completed task 4: create the hostile-input script

Create:

```text
taskforge/src/taskforge/abuse.py
```

Drive at least ten hostile inputs through the public `taskforge` API. Cover
the required error categories, including:

- Empty title
- Whitespace-only title
- Negative priority
- Duplicate title
- Repeated duplicate attempt
- Completing an unknown ID
- Removing an unknown ID
- Invalid values at relevant public boundaries
- Valid operations after earlier failures
- Multiple failures caught independently

For each expected failure, print:

- The operation being attempted
- The caught exception type
- Its friendly message

Use a stable label beginning with `CASE ` for each hostile case so the
diagnostic output and its black-box test remain easy to scan. After all
expected failures, perform a valid operation and print
`VALID AFTER FAILURES: OK` to prove earlier failures did not corrupt the
application state.

The script must catch specific TaskForge domain errors, not a bare exception.
It is a manual diagnostic script; Phase 11 later converts this behavior into
a comprehensive automated suite.

## Tests to add now

Although the roadmap calls `abuse.py` the main Phase 5 verification artifact,
the current TaskForge project already has pytest coverage. Add focused tests
for stable contracts:

- Error inheritance
- Exception data attributes
- Exception messages
- Empty-title rejection
- Negative-priority rejection
- Duplicate-title rejection
- Unknown-ID completion and removal
- CLI handling of `TaskForgeError`
- REPL continuation after an expected domain error
- Unexpected errors are not swallowed

Keep tests independent of the module-level ID counter wherever exact ID
values are not part of the behavior under test.

Run:

```bash
python -m pytest -q taskforge/tests
```

## Manual verification

Run the hostile-input script:

```bash
python -m taskforge.abuse
```

Run the installed CLI:

```bash
taskforge
```

Try expected failures and confirm that each produces one friendly line and
returns to the prompt.

Temporarily introduce a genuine programming bug in a command handler and
confirm that it still crashes with a traceback. Remove the deliberate bug
after verifying the boundary.

## Completion criteria

Phase 5 TaskForge is complete when:

- `errors.py` contains the required hierarchy.
- Domain errors carry the required contextual data.
- Core validation maps each invalid case to the correct error type.
- Core code contains no printing or process exits.
- The CLI catches `TaskForgeError` at one clear boundary.
- The CLI does not catch generic `Exception`.
- Expected domain failures do not terminate the REPL.
- Genuine programming bugs are not hidden.
- `abuse.py` demonstrates at least ten hostile inputs.
- All Phase 5 exercise tests pass.
- All TaskForge tests pass.

## Recommended implementation order

1. Complete the small Phase 5 exercises.
2. Add and test the exception hierarchy.
3. Add one core validation rule at a time.
4. Update tests after each rule.
5. Add the CLI error boundary.
6. Write and run `abuse.py`.
7. Run all Phase 5 and TaskForge tests.
8. Commit and tag the completed milestone.
