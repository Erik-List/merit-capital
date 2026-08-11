#!/usr/bin/env python3
"""Merge exported review decisions into the durable human layer, then rebuild.

Usage: python3 scripts/apply-review.py ~/Downloads/decisions.json [investor-slug]

Decisions are stored in data/aggregation/company-base/review-decisions.json and
re-applied by build-company-base.py on every rebuild, so human review survives
re-running the source collectors.
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CB = ROOT / "data" / "aggregation" / "company-base"


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = Path(sys.argv[1]).expanduser()
    investor = sys.argv[2] if len(sys.argv) > 2 else "sequoia-capital"
    incoming = json.load(open(src))
    new = incoming.get("decisions", incoming)

    store_path = CB / "review-decisions.json"
    store = json.load(open(store_path)) if store_path.exists() else {}
    bucket = store.setdefault(investor, {})

    added = changed = 0
    for slug, rec in new.items():
        prev = bucket.get(slug)
        if prev is None:
            added += 1
        elif prev != rec:
            changed += 1
        bucket[slug] = rec

    store_path.write_text(json.dumps(store, indent=1, sort_keys=True) + "\n")
    print(f"decisions merged: +{added} new, {changed} changed, {len(bucket)} total")

    subprocess.run([sys.executable, str(ROOT / "scripts" / "build-company-base.py")], check=True)
    subprocess.run([sys.executable, str(ROOT / "scripts" / "make-review-html.py"), investor], check=True)
    print("CSV + review.html rebuilt with human decisions applied")


if __name__ == "__main__":
    main()
