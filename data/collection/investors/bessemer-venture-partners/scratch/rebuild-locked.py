#!/usr/bin/env python3
"""Run the base rebuild while judges may be recording: holds the same machine-wide lock `run.py record` takes
(shared_throttle.exclusive("record-<slug>")), so the rebuild's overlay re-key (a read-modify-write of
classification.json, resolved.json and the ledger) cannot drop a judge's answer. Before the build it writes
scratch/recall-additions.json into the ledger's recall_additions (once; idempotent by slug).
Usage: python3 rebuild-locked.py <log name>"""
import json, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from shared_throttle import exclusive  # noqa: E402
from paths import Paths, write_atomic  # noqa: E402
SLUG = "bessemer-venture-partners"
P = Paths(SLUG)
log = HERE / (sys.argv[1] if len(sys.argv) > 1 else "build.log")
with exclusive(f"record-{SLUG}"):
    led = json.loads(P.ledger.read_text())
    bucket = led[SLUG]
    have = {a["slug"] for a in bucket.setdefault("recall_additions", [])}
    adds = json.loads((HERE / "recall-additions.json").read_text())
    new = [a for a in adds if a["slug"] not in have]
    if new:
        bucket["recall_additions"].extend(new)
        write_atomic(P.ledger, json.dumps(led, indent=1, ensure_ascii=False) + "\n")
    print(f"recall additions in the ledger: {len(bucket['recall_additions'])} ({len(new)} new)", flush=True)
    with open(log, "w") as f:
        rc = subprocess.run([sys.executable, str(ROOT / "scripts" / "build-company-base.py"), SLUG], stdout=f, stderr=subprocess.STDOUT, cwd=ROOT).returncode
    print("build exit", rc, flush=True)
