#!/usr/bin/env python3
"""Merge exported outcome-review decisions into the durable layer, then rebuild.

Mirrors `scripts/apply-review.py`. Decisions live in
data/aggregation/outcomes/outcome-decisions.json and are re-applied over the
classification on every rebuild, so a human pass survives re-running the
deterministic layers.

A rejected row is one the reviewer judged wrong or not a portfolio company. It
keeps its evidence but is excluded from every derived figure, which is what makes
the aggregate defensible: nothing silently disappears, it is marked.

Usage: python3 scripts/apply-outcomes.py ~/Downloads/outcome-decisions.json [investor-slug]
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "aggregation" / "outcomes"


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = Path(sys.argv[1]).expanduser()
    investor = sys.argv[2] if len(sys.argv) > 2 else "sequoia-capital"

    incoming = json.load(open(src))
    new = incoming.get("decisions", incoming)

    store_path = OUT / "outcome-decisions.json"
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
    decided = sum(1 for r in bucket.values() if r.get("d") in ("confirmed", "rejected"))
    print(f"decisions merged: +{added} new, {changed} changed, "
          f"{len(bucket)} total ({decided} confirmed/rejected)")

    subprocess.run([sys.executable, str(ROOT / "scripts" / "make-outcome-html.py"), investor],
                   check=True)
    print("review.html rebuilt with decisions applied")


if __name__ == "__main__":
    main()
