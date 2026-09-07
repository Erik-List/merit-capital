#!/usr/bin/env python3
"""Resolve the two first-party entry-round layers into one `site_entry_stage`.

decisions.md R3 set the evidence order after the calibration gate scored both
layers (circles 5/5; CMS enum 17/18). This applies that order mechanically and
writes ONE value per company, which is what build-company-base.py and the
queue can carry (`site_entry_stage` is a single field, and COLLECTION.md §8's
Menlo rule is that a class-1 layer the queue item does not carry is a layer
the grind cannot use).

    both layers agree      -> that value                     (class 1)
    circles only           -> circles                        (class 1)
    CMS only               -> CMS                            (class 1, medium)
    layers DISAGREE        -> nothing is written              (judge decides)

The last line is the point: leaving the field empty is what puts the row back
in front of the judge with a citation attempt, instead of publishing one
layer's guess. Three rows are in that state (BrightRoll, Ginkgo Bioworks,
Opendoor) and they are listed in the output for the report.

The value written is the round word as the firm writes it; the judge maps it
into the published taxonomy (Pre-Seed | Seed | Series A | Growth).
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "sources" / "site"

TAXO = {"pre-seed": "Pre-Seed", "seed": "Seed", "series a": "Series A"}


def taxonomy(word: str | None) -> str | None:
    """Map a round word into the published taxonomy; None if unmappable."""
    if not word:
        return None
    w = word.strip().lower()
    if w in TAXO:
        return TAXO[w]
    if re.match(r"^series [b-z]$", w) or w in {"common", "growth"}:
        return "Growth"
    return None


def key(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def main() -> None:
    cms = {}
    for r in json.loads((SITE / "sanity-companies.json").read_text())["rows"]:
        if r.get("site_stage"):
            cms[key(r["name"])] = (r["name"], r["site_stage"])

    cir = {}
    for r in json.loads((SITE / "wayback-circles.json").read_text())["companies-circles"]:
        nm = r.get("name") or r["slug"]
        if r.get("site_entry_stage"):
            cir[key(nm)] = (nm, r["site_entry_stage"], r.get("ladder"))

    rows, conflicts = [], []
    basis_counts: Counter = Counter()
    for k in sorted(set(cms) | set(cir)):
        a = cms.get(k)
        b = cir.get(k)
        name = (a or b)[0]
        ta = taxonomy(a[1]) if a else None
        tb = taxonomy(b[1]) if b else None

        if ta and tb and ta != tb:
            conflicts.append((name, a[1], b[1], (b[2] if b else None)))
            basis_counts["conflict_withheld"] += 1
            continue
        if tb:
            value, basis = b[1], ("both_agree" if ta else "circles_only")
        elif ta:
            value, basis = a[1], "cms_only"
        else:
            basis_counts["unmappable"] += 1
            continue
        basis_counts[basis] += 1
        rows.append({
            "name": name,
            "site_entry_stage": value,
            "stage_basis": basis,
            "stage_ladder": b[2] if b else None,
        })

    (SITE / "entry-stage-layer.json").write_text(json.dumps({
        "_readme":
            "One resolved entry-round claim per company, from the two "
            "first-party layers, under decisions.md R3's evidence order. "
            "`stage_basis` says which layer carried it: both_agree, "
            "circles_only, or cms_only. Rows where the layers DISAGREE are "
            "deliberately absent so the queue asks the judge -- they are "
            "listed under _conflicts. Written by "
            "scratch/build-entry-stage-layer.py; fetches nothing.",
        "_conflicts": [
            {"name": n, "cms": c, "circles": w, "ladder": l}
            for n, c, w, l in conflicts],
        "_list": "companies-entry-stage",
        "rows": rows,
    }, indent=1, ensure_ascii=False) + "\n")

    print(f"wrote entry-stage-layer.json: {len(rows)} companies")
    for b, n in basis_counts.most_common():
        print(f"  {b:20} {n}")
    print(f"  conflicts withheld from the layer ({len(conflicts)}):")
    for n, c, w, l in conflicts:
        print(f"      {n}: cms={c!r} circles={w!r} ladder={l}")


if __name__ == "__main__":
    main()
