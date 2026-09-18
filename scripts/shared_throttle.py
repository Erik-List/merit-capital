"""Cross-process pacing for the external services every collection run hits.

Several investor sessions may run at once on one machine, and SEC, the
Internet Archive and Wikidata all meter the whole machine as one
client. Per-process sleeps therefore add up: two sessions at 8 requests per
second each are 16 against SEC's 10. This module keeps ONE token bucket per
service, persisted in a small lock file, so the aggregate rate across every
process stays under the ceiling and a single process behaves exactly as it
did before.

    from shared_throttle import wait, exclusive
    wait("sec")                 # sleep until this process's next slot
    with exclusive("cik-lookup"):   # one puller at a time for this service
        ...

Rates (requests per second) default to SEC 8.0, IA 1.0, Wikidata 0.67 and can
be overridden per service with MERIT_<SERVICE>_RATE. The lock directory is
machine-global and never inside the repository (an iCloud-synced or
per-worktree path would defeat it): ~/Library/Caches/merit-capital/locks on
macOS, the system temp dir elsewhere, MERIT_LOCK_DIR overrides both. If the
directory cannot be used the module warns once and falls back to an
in-process bucket with the same semantics.

Only the standard library is used. `flock` locks are per open file
description, so every call opens a fresh descriptor; they are released by the
kernel when a process dies, so no stale-lock handling is needed.
"""
from __future__ import annotations

import contextlib
import fcntl
import os
import sys
import tempfile
import threading
import time
from pathlib import Path

DEFAULT_RATES: dict[str, float] = {"sec": 8.0, "ia": 1.0, "wikidata": 0.67}

_warned = False
_local_lock = threading.Lock()
_local_slots: dict[str, float] = {}
_resolved: dict[str, Path | None] = {}   # lock dir per MERIT_LOCK_DIR value, probed once


def lock_dir() -> Path | None:
    """The machine-global lock directory, created on first use; None if unusable.

    Probed once per process with a SHARED, blocking lock: a shared lock never
    contends with another probe, so a second process arriving at the same
    instant is not mistaken for an unusable directory (a non-blocking
    exclusive probe did exactly that). Filesystems without flock still raise
    and trigger the per-process fallback.
    """
    global _warned
    env = os.environ.get("MERIT_LOCK_DIR", "")
    if env in _resolved:
        return _resolved[env]
    if env:
        d = Path(env).expanduser()
    elif sys.platform == "darwin":
        d = Path.home() / "Library" / "Caches" / "merit-capital" / "locks"
    else:
        d = Path(tempfile.gettempdir()) / "merit-capital-locks"
    try:
        d.mkdir(parents=True, exist_ok=True)
        with open(d / ".probe", "a+") as fh:
            fcntl.flock(fh.fileno(), fcntl.LOCK_SH)
            fcntl.flock(fh.fileno(), fcntl.LOCK_UN)
        _resolved[env] = d
    except OSError as e:
        if not _warned:
            print(f"shared_throttle: lock dir {d} unusable ({e}); pacing per process only",
                  file=sys.stderr)
            _warned = True
        _resolved[env] = None
    return _resolved[env]


def rate_of(service: str, rate: float | None = None) -> float:
    if rate is not None:
        return float(rate)
    env = os.environ.get(f"MERIT_{service.upper()}_RATE")
    if env:
        return float(env)
    return DEFAULT_RATES.get(service, 1.0)


def wait(service: str, rate: float | None = None) -> None:
    """Block until this process may make its next request to `service`.

    Token bucket with one slot per 1/rate seconds, shared across processes
    through the lock file: take the lock, read the next free slot, claim it,
    write the slot after it, release, then sleep outside the lock. Wall-clock
    time is used because it is the only clock comparable across processes.
    """
    r = rate_of(service, rate)
    interval = 1.0 / r if r > 0 else 0.0
    d = lock_dir()
    now = time.time()
    if d is None:
        with _local_lock:
            slot = max(now, _local_slots.get(service, 0.0))
            _local_slots[service] = slot + interval
    else:
        path = d / f"{service}.lock"
        with open(path, "a+") as fh:
            fcntl.flock(fh.fileno(), fcntl.LOCK_EX)
            try:
                fh.seek(0)
                raw = fh.read().strip()
                try:
                    prev = float(raw.split()[0]) if raw else 0.0
                except ValueError:
                    prev = 0.0
                slot = max(now, prev)
                fh.seek(0)
                fh.truncate()
                fh.write(f"{slot + interval:.6f} {os.getpid()}\n")
                fh.flush()
            finally:
                fcntl.flock(fh.fileno(), fcntl.LOCK_UN)
    delay = slot - time.time()
    if delay > 0:
        time.sleep(delay)


@contextlib.contextmanager
def exclusive(service: str, note_every: float = 30.0):
    """Hold `service` exclusively for the block (one puller at a time).

    For a service that cannot take parallel clients at all. While blocked,
    a note names the holder every `note_every` seconds so a waiting session
    knows why it is waiting.
    """
    d = lock_dir()
    if d is None:
        with _local_lock:
            yield
        return
    path = d / f"{service}.exclusive"
    with open(path, "a+") as fh:
        waited = 0.0
        while True:
            try:
                fcntl.flock(fh.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except OSError:
                if waited and waited % note_every < 0.5:
                    fh.seek(0)
                    holder = fh.read().strip() or "another process"
                    print(f"shared_throttle: waiting for {service} held by {holder}",
                          file=sys.stderr)
                time.sleep(0.5)
                waited += 0.5
        try:
            fh.seek(0)
            fh.truncate()
            fh.write(f"pid {os.getpid()} since {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            fh.flush()
            yield
        finally:
            fh.seek(0)
            fh.truncate()
            fh.flush()
            fcntl.flock(fh.fileno(), fcntl.LOCK_UN)
