"""Exercise 14.3 — the profiling loop (script; the narrative IS the
deliverable).

1. Write a deliberately slow pipeline over synthetic data: nested-loop
   dedupe, a file re-read INSIDE the loop, a sort inside the loop.
2. python -m cProfile -s cumulative profile_me.py — paste the top rows as
   a comment.
3. Fix ONLY the #1 item. Re-profile, paste again. Repeat until
   diminishing returns. Keep every snapshot: the sequence of profiles +
   fixes is what you're practicing, not the final speed.

Skills practiced:
- cProfile
- Fixing the top hot spot, then re-profiling
"""

# TODO
