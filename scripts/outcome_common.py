"""Shared by outcome-run.py and make-outcome-html.py: base loading and the one
overlay merge, so verify, export and the review surface cannot drift apart."""
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE_DIR = ROOT / "data" / "aggregation" / "company-base"


def load_base(investor: str) -> list[dict]:
    """Rows of the live Company Base (no pinned snapshot; see outcome-run.py)."""
    path = BASE_DIR / f"{investor}.csv"
    if not path.exists():
        sys.exit(f"no company base at {path}")
    return list(csv.DictReader(open(path)))


def merge_rows(rows: list[dict], resolved: dict, cls: dict) -> dict[str, dict]:
    """slug -> deterministic record overlaid with the batch classification.

    Flags are additive across layers: a batch answer must not be able to clear
    a deterministic flag (duplicate, boundary, ...) by emitting its own list.
    Everything else is a per-key override.
    """
    merged = {}
    for row in rows:
        det, overlay = resolved.get(row["slug"], {}), cls.get(row["slug"], {})
        rec = {**det, **overlay,
               "flags": sorted(set(det.get("flags") or [])
                               | set(overlay.get("flags") or []))}
        merged[row["slug"]] = rec
    return merged
