#!/usr/bin/env python3
"""Repair notes lost to record's note-join defect (a line recorded twice keeps only its new sentence; memory
record-note-join-bug, run.py around line 1633). Rebuilds each affected row's note by replaying every recorded
queue/*.out.jsonl in recording order (file mtime) with record's own join rule (" | ", skip a sentence already in the
note), and writes the rebuilt notes directly into classification.json under the book's record lock, so a restore does
not itself go through record and re-trigger the defect.
Usage: python3 repair-notes.py <out-file-stem> [...]   (the files that were recorded twice; e.g. s1b)
       --dry  print the diffs only
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402
from shared_throttle import exclusive  # noqa: E402

INV = HERE.parent
SLUG = "new-enterprise-associates"


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry" in sys.argv
    affected = set()
    for stem in args:
        for line in (HERE / "queue" / f"{stem}.out.jsonl").read_text().splitlines():
            if line.strip():
                d = json.loads(line)
                if "verdict" not in d:
                    affected.add(d["slug"])
    files = sorted((HERE / "queue").glob("*.out.jsonl"), key=lambda f: f.stat().st_mtime)
    rebuilt = {}
    for f in files:
        for line in f.read_text().splitlines():
            if not line.strip():
                continue
            d = json.loads(line)
            if "verdict" in d or d["slug"] not in affected or not d.get("note"):
                continue
            cur = rebuilt.get(d["slug"])
            if not cur:
                rebuilt[d["slug"]] = d["note"]
            elif d["note"] not in cur:
                rebuilt[d["slug"]] = f"{cur} | {d['note']}"
    with exclusive(f"record-{SLUG}"):
        p = INV / "companies" / "classification.json"
        raw = json.loads(p.read_text())
        cls = raw.get(SLUG, raw) if isinstance(raw, dict) and SLUG in raw else raw
        changed = 0
        for s, note in rebuilt.items():
            if s in cls and cls[s].get("note") != note:
                if dry:
                    print(f"{s}\n  now:  {cls[s].get('note')}\n  back: {note}\n")
                cls[s]["note"] = note
                changed += 1
        if not dry and changed:
            write_atomic(p, json.dumps(raw, indent=1, sort_keys=True))
    print(f"{len(affected)} affected rows; {changed} notes {'would change' if dry else 'restored'}")


if __name__ == "__main__":
    main()
