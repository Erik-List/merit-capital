#!/usr/bin/env python3
"""Replace a row's note in classification.json, under record's own lock.

`record` appends a new note to an existing one with " | " (run.py cmd_record), which is right for a delta and wrong
for a rewrite: a fixed row then reads its old, superseded note first. This writes the final note for the rows a fix
pass rewrote, in record's own file format, and nothing else.

Usage: python3 scratch/set-notes.py notes.json   ({slug: "note"})
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402
from shared_throttle import exclusive  # noqa: E402

P = Paths("ribbit-capital")


def main() -> None:
    notes = json.loads(Path(sys.argv[1]).read_text())
    with exclusive(f"record-{P.slug}"):
        cls = json.loads(P.classification.read_text())
        rows = cls
        for k in ("ribbit-capital", "rows"):
            if isinstance(rows, dict) and k in rows and isinstance(rows[k], dict):
                rows = rows[k]
        for slug, note in notes.items():
            if slug not in rows:
                sys.exit(f"{slug}: not in classification.json")
            rows[slug]["note"] = note
        write_atomic(P.classification, json.dumps(cls, indent=1, sort_keys=True))
    print(f"notes replaced: {sorted(notes)}")


if __name__ == "__main__":
    main()
