# python-lab

Hands-on practice repo for the [Python Learning Roadmap](PYTHON_ROADMAP.md) —
a 15-phase, project-driven path from beginner to senior backend engineer,
followed later by a FastAPI roadmap.

## Layout

```
python-lab/
├── PYTHON_ROADMAP.md   # the full roadmap: read the approach section first
├── NOTES.md            # your running notes, struggle log, quiz answers
├── exercises/
│   ├── conftest.py     # shared pytest setup (see below)
│   └── phase01..15/    # one folder per phase; stubs describe each task
└── taskforge/          # the evolving project (starts in Phase 3)
```

All 15 phases are scaffolded. Stubs contain requirements (docstrings) and
`raise NotImplementedError` bodies — never solutions. Phases 13–14 are
mostly measurement scripts (timing/profiling), so they have few tests by
design; phase 11 is the phase where *you* write the tests.

## How to work

1. Read the current phase in `PYTHON_ROADMAP.md` (docs skim ≈ 30–60 min).
2. Complete the exercise stubs in `exercises/phaseNN/` — type every line
   yourself; the stubs contain requirements, never solutions.
3. Do the phase's larger assignment.
4. Take the phase quiz from memory; log answers and gaps in `NOTES.md`.
5. Commit as you go; push for review before moving to the next phase.

## Setup (Phase 1, first task)

```bash
python3 -m venv .venv
source .venv/bin/activate
python --version   # expect 3.12+
pip install -r requirements-dev.txt
```

## Tests

Each phase ships with a pytest suite. Unimplemented exercises **skip**
(the stubs raise `NotImplementedError`, which `exercises/conftest.py`
converts to a skip); as you implement, tests turn green — your progress
bar is the skip count going down.

```bash
pytest exercises/              # everything
pytest exercises/phase03/      # one phase
pytest exercises/ -rs          # show what's still skipped/left
```

A phase's exercises are done when its test file passes with zero skips
(plus the script-style tasks, which are verified by their own
predict-then-run comments).
