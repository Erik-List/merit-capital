#!/usr/bin/env python3
"""Find and retire iCloud sync-conflict copies ("name 2.ext", "name 3.ext").

The repository lived under an iCloud-synced folder; when several sessions
wrote thousands of small files at once, the sync engine preserved the
version it could not reconcile as a numbered copy next to the canonical
file. Every copy has a canonical sibling and, where the two differ, the copy
is the older snapshot. This script never deletes: it classifies, and with
--apply it MOVES copies into a dated folder in ~/.Trash.

Dry run by default:
    python3 scripts/clean-conflict-copies.py            # classify and list
    python3 scripts/clean-conflict-copies.py --apply    # move IDENTICAL copies
    python3 scripts/clean-conflict-copies.py --apply --include-differing

Classes:
    IDENTICAL  byte-equal to the canonical file            (moved with --apply)
    DIFFERS    differs from the canonical                  (--include-differing)
    ORPHAN     no canonical sibling exists                 (never touched)
"""
import argparse
import filecmp
import re
import shutil
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCAN = ("data", "scripts")
COPY_RE = re.compile(r"^(?P<stem>.+) (?P<n>\d+)(?P<ext>\.[^.]+)$")


def classify() -> dict[str, list[tuple[Path, Path | None]]]:
    out: dict[str, list[tuple[Path, Path | None]]] = {
        "IDENTICAL": [], "DIFFERS": [], "ORPHAN": []}
    for top in SCAN:
        base = ROOT / top
        if not base.exists():
            continue
        for p in sorted(base.rglob("*")):
            if not p.is_file():
                continue
            m = COPY_RE.match(p.name)
            if not m:
                continue
            canon = p.with_name(m["stem"] + m["ext"])
            if not canon.exists():
                out["ORPHAN"].append((p, None))
            elif filecmp.cmp(p, canon, shallow=False):
                out["IDENTICAL"].append((p, canon))
            else:
                out["DIFFERS"].append((p, canon))
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true",
                    help="move IDENTICAL copies to ~/.Trash (dry run without it)")
    ap.add_argument("--include-differing", action="store_true",
                    help="with --apply, also move DIFFERS copies")
    ap.add_argument("--list", action="store_true",
                    help="print every path, not only counts and the non-identical ones")
    args = ap.parse_args()

    groups = classify()
    total = sum(len(v) for v in groups.values())
    print(f"conflict copies under {', '.join(SCAN)}: {total}")
    for k in ("IDENTICAL", "DIFFERS", "ORPHAN"):
        print(f"  {k:9s} {len(groups[k])}")
    if not total:
        return

    for k in ("DIFFERS", "ORPHAN"):
        for p, canon in groups[k]:
            age = ""
            if canon is not None:
                age = "older" if p.stat().st_mtime < canon.stat().st_mtime else "NEWER"
            print(f"  {k:9s} {p.relative_to(ROOT)}  {age}")
    if args.list:
        for p, _ in groups["IDENTICAL"]:
            print(f"  IDENTICAL {p.relative_to(ROOT)}")

    if not args.apply:
        print("\ndry run: nothing moved (use --apply)")
        return

    dest_root = Path.home() / ".Trash" / f"merit-capital-conflict-copies-{time.strftime('%Y%m%d-%H%M%S')}"
    todo = list(groups["IDENTICAL"])
    if args.include_differing:
        todo += groups["DIFFERS"]
    moved = 0
    for p, _ in todo:
        rel = p.relative_to(ROOT)
        dest = dest_root / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(p), str(dest))
        moved += 1
    print(f"\nmoved {moved} file(s) to {dest_root}")
    left = sum(len(v) for v in classify().values())
    print(f"remaining conflict copies: {left}"
          + ("" if left == 0 else "  (DIFFERS/ORPHAN kept; see above)"))
    if left and not args.include_differing and groups["DIFFERS"]:
        print("re-run with --include-differing to move the DIFFERS copies too")


if __name__ == "__main__":
    sys.exit(main())
