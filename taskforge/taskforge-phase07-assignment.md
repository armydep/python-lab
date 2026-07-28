# TaskForge Phase 7 Assignment

## Milestone

TaskForge v0.3a — object-oriented domain model and repository boundary.

## Goal

Refactor TaskForge from dict-based task records plus module-level storage
functions into a small object model with swappable repositories.

The behavior should stay the same from the user's perspective:

- Same REPL commands.
- Same default JSON file location.
- Same expected-error boundary in the CLI.
- Same CSV import/export capability.

The architecture changes so the CLI talks to a repository interface instead of
directly owning a raw `list[dict]`.

Target dependency direction:

```text
__main__ → cli → repository → models → errors
              └→ csv_adapter
```

`core.py` can either be removed after migration or kept temporarily as a
compatibility wrapper. It should not remain the primary domain model.

## Phase 7 small exercises

The OOP exercises live under:

```text
exercises/phase07-oop/
```

Current baseline:

```bash
cd taskforge
UV_CACHE_DIR=/tmp/taskforge-uv-cache uv run --with pytest python -m pytest -q ../exercises/phase07-oop
```

Expected:

```text
12 passed
```

## Starting point

Phase 6 is complete:

- TaskForge persists tasks to JSON.
- Saves are atomic.
- CSV export/import round-trips task fields and tags.
- `StorageError` belongs to the `TaskForgeError` hierarchy.
- CLI is still the expected-error boundary.
- Current TaskForge tasks are plain dictionaries:

```python
{
    "id": int,
    "title": str,
    "done": bool,
    "tags": set[str],
    "priority": int,
}
```

Phase 7 changes that representation to `Task` objects.

## Task 1: create the domain model

Create:

```text
src/taskforge/models.py
```

Required model:

```python
class Priority(enum.IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


@dataclass
class Task:
    id: int | None
    title: str
    done: bool = False
    tags: set[str] = field(default_factory=set)
    priority: Priority = Priority.MEDIUM
    created_at: datetime = field(default_factory=...)
```

Requirements:

- Use `dataclasses`.
- Use `field(default_factory=set)` for tags.
- Use `field(default_factory=...)` for `created_at`.
- Reject empty or whitespace-only titles in `__post_init__`.
- Preserve the current title rule: validation checks stripped content, but the
  original title text is stored unchanged.
- Reject unsupported priority values with `InvalidTask`.
- Normalize valid priority inputs to `Priority`.
- `Task.complete()` marks the task done.
- `Task.matches(query)` returns whether the task matches a text/tag query.
- `Task.to_dict()` returns JSON-safe data.
- `Task.from_dict(data)` restores a `Task` from saved data.

JSON compatibility requirements:

- Tags serialize as sorted lists.
- Tags load back as sets.
- Priority serializes as an integer.
- `created_at` serializes as an ISO 8601 string.
- `from_dict(to_dict(task))` preserves task data.

## Task 2: create the repository abstraction

Create:

```text
src/taskforge/repository.py
```

Required classes:

```python
class TaskRepository(ABC):
    add(task: Task) -> Task
    get(task_id: int) -> Task
    remove(task_id: int) -> None
    list() -> list[Task]
    save() -> None
```

Implement:

- `MemoryRepository`
- `JsonRepository(path)`

Repository responsibilities:

- Own the task collection.
- Assign IDs to new tasks.
- Keep the next ID counter encapsulated.
- Reject duplicate titles with `DuplicateTask`.
- Raise `TaskNotFound` for unknown IDs.
- Preserve successful mutation semantics from Phase 6.

`JsonRepository` responsibilities:

- Load existing tasks from the JSON path.
- Save atomically.
- Use UTF-8.
- Missing file starts empty.
- Preserve the Phase 6 JSON file format, with any new fields documented.
- Raise `StorageError` for expected persistence failures.

## Task 3: migrate storage behavior into `JsonRepository`

Move the durable persistence behavior from `storage.py` into `JsonRepository`.

Preserve:

- Missing file returns an empty collection.
- Saving creates parent directories.
- Saving uses a temp file in the target directory.
- Saving flushes/closes successfully before replace.
- `os.replace` performs the final atomic replacement.
- Failed save preserves the previous file.
- Corrupt JSON raises `StorageError` with the original
  `json.JSONDecodeError` preserved as `__cause__`.

`storage.py` may remain as a compatibility wrapper during the refactor, but
the preferred architecture is repository-based persistence.

## Task 4: update the CLI to depend on the repository interface

Update:

```text
src/taskforge/cli.py
```

Requirements:

- `main()` should accept a `TaskRepository`.
- The default CLI should use `JsonRepository(DEFAULT_DATA_PATH)`.
- Command handlers should operate through repository methods.
- The CLI should not know JSON serialization details.
- The CLI should not mutate a raw task list directly.
- Save after successful mutating commands.
- Do not save after read-only commands.
- Do not save when a mutating command fails.
- Keep catching `TaskForgeError` at the command-dispatch boundary.
- Do not catch generic `Exception`.

Current command behavior must remain:

```text
add <title>
done <id>
ls
ls <tag>
stats
export csv <path>
import csv <path>
version
quit
```

## Task 5: update CSV import/export for `Task` objects

Update `csv_adapter.py` so it works with `Task` objects instead of plain
dictionaries.

Requirements:

- Keep using the `csv` module.
- Open CSV files with `newline=""` and `encoding="utf-8"`.
- Keep a documented stable CSV format.
- Import your own exported file without data loss.
- Skip malformed rows and report their line numbers.
- Valid rows still import when other rows are malformed.
- Imported tasks should become `Task` instances.
- Successful import should replace repository contents or use a clearly
  documented merge strategy.

Recommended strategy for Phase 7:

```text
import csv <path> replaces the repository's current task collection with the
valid rows from the file, then saves JSON.
```

This matches the Phase 6 implementation and avoids silent ID collisions.

## Task 6: public API update

Update:

```text
src/taskforge/__init__.py
```

Expose intentionally public Phase 7 names:

- `Task`
- `Priority`
- `TaskRepository`
- `MemoryRepository`
- `JsonRepository`
- existing public errors

Decide whether old dict-oriented core functions remain public compatibility
APIs. If they remain, add tests that prove they still work. If they are
removed, update tests and document the breaking change.

## Tests to add during implementation

Add focused tests for:

- `Task` rejects invalid titles.
- `Task` protects mutable tag defaults.
- `Task.complete()` updates state.
- `Task.matches()` handles title/tag queries.
- `Task.to_dict()` / `Task.from_dict()` round-trip.
- `Priority` accepts expected values and rejects invalid values.
- `MemoryRepository.add()` assigns IDs.
- `MemoryRepository` rejects duplicate titles.
- `MemoryRepository.get/remove()` raise `TaskNotFound` for unknown IDs.
- `JsonRepository` loads existing tasks.
- `JsonRepository.save()` is atomic.
- CLI works against a fake or memory repository.
- CLI still does not save after failed/read-only commands.
- CSV export/import round-trips `Task` objects.

## Manual verification

Run:

```bash
cd taskforge
UV_CACHE_DIR=/tmp/taskforge-uv-cache uv run --with pytest python -m pytest -q ../exercises/phase07-oop tests
```

Then manually verify:

```bash
UV_CACHE_DIR=/tmp/taskforge-uv-cache uv run python -m taskforge
```

Try:

```text
add Ship OOP refactor
ls
done 1
stats
export csv /tmp/taskforge-phase7.csv
quit
```

Restart the CLI and confirm the task is still present.

## Completion criteria

Phase 7 TaskForge is complete when:

- Phase 7 OOP exercise tests pass.
- TaskForge uses `Task` objects internally.
- Task invariants live on the model.
- Repositories own storage and ID assignment.
- CLI depends on the repository interface, not a raw task list.
- JSON persistence remains durable and atomic.
- CSV import/export still round-trips tasks.
- `core.py` is either removed, reduced to compatibility wrappers, or clearly
  documented as deprecated.
- All TaskForge tests pass.
- The CLI behaves identically from the user's perspective.

## Recommended implementation order

1. Add `models.py` with `Priority` and `Task`.
2. Add model tests.
3. Add `repository.py` with `TaskRepository` and `MemoryRepository`.
4. Add repository tests.
5. Implement `JsonRepository` by reusing Phase 6 storage behavior.
6. Migrate CLI command handlers to repository methods.
7. Update CSV adapter for `Task` objects.
8. Update public API exports.
9. Run Phase 7 exercise tests and TaskForge tests.
10. Update `design_diagram.md` with the Phase 7 architecture.
11. Commit and tag TaskForge v0.3a.

