"""A per-session cap on GV's concurrent Google News clients (PRO-75, at the Tiger Global session's request,
2026-09-29). The machine-wide googlenews bucket (scripts/shared_throttle.py) keeps the total rate at 1 request/s but
has no per-session fairness: every waiting process races for each slot, so a session with 15 waiting clients takes
15 of 16 slots. Every GV entry point that calls Google News (nq.py, news.py, news-sweep.py, judge_lib.NEWS decode)
first takes one of SLOTS local slot locks, so GV never holds more than SLOTS places in the shared queue.

Usage:  with gvslot.slot(): res = gs.googlenews(...)
"""
import contextlib
import fcntl
import os
import time
from pathlib import Path

SLOTS = 2
LOCKS = Path.home() / "Library" / "Caches" / "merit-capital" / "locks"


@contextlib.contextmanager
def slot():
    LOCKS.mkdir(parents=True, exist_ok=True)
    while True:
        for i in range(SLOTS):
            fd = os.open(LOCKS / f"gv-googlenews-slot-{i}.lock", os.O_RDWR | os.O_CREAT, 0o644)
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                os.close(fd)
                continue
            try:
                yield i
            finally:
                fcntl.flock(fd, fcntl.LOCK_UN)
                os.close(fd)
            return
        time.sleep(0.5)
