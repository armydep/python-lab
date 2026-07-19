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
│   └── phase01/        # one folder per phase; stubs describe each task
└── taskforge/          # the evolving project (created in Phase 3)
```

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
```
