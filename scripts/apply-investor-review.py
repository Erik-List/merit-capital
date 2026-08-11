#!/usr/bin/env python3
"""Merge exported firm-profile decisions into the durable human layer.

Usage: python3 scripts/apply-investor-review.py ~/Downloads/investor-decisions.json

Decisions are stored in data/aggregation/investors/review-decisions.json. The
collector must consult this file on every rebuild: a human correction outranks
anything a run derives, and re-running the collector must never silently
overwrite one.
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INV = ROOT / "data" / "aggregation" / "investors"


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    incoming = json.load(open(Path(sys.argv[1]).expanduser()))
    new = incoming.get("decisions", incoming)

    store_path = INV / "review-decisions.json"
    store = json.load(open(store_path)) if store_path.exists() else {}

    added = changed = 0
    for slug, fields in new.items():
        bucket = store.setdefault(slug, {})
        for field, rec in fields.items():
            if field not in bucket:
                added += 1
            elif bucket[field] != rec:
                changed += 1
            bucket[field] = rec

    store_path.write_text(json.dumps(store, indent=2, sort_keys=True) + "\n")
    print(f"{added} new, {changed} changed -> {store_path.relative_to(ROOT)}")

    rejected = [(s, f) for s, fs in store.items()
                for f, r in fs.items() if r.get("verdict") == "no"]
    if rejected:
        print(f"\n{len(rejected)} field(s) rejected and awaiting correction:")
        for slug, field in rejected:
            note = store[slug][field].get("note") or "no note"
            print(f"  {slug}.{field}: {note}")

    subprocess.run([sys.executable, str(ROOT / "scripts" / "make-investor-review.py")],
                   check=True)


if __name__ == "__main__":
    main()
