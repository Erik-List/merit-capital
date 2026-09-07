#!/usr/bin/env python3
"""Score the two candidate entry_stage layers against the stage golden key.

COLLECTION.md §4: "Score every candidate evidence layer for the guarded column
against the key, and promote or demote it by its score before the grind trusts
it. A layer that was never scored is not a label."

Layer A: the live Sanity CMS `stage` enum (277 rows).
Layer B: the <p class=circles> ladder on the 2011-2019 archived listings, first
         element (151 rows).

Both are mapped into the published taxonomy first (Pre-Seed | Seed | Series A |
Growth), because that is the column that publishes: a Series B-vs-C
disagreement is not a taxonomy miss and must not be scored as one.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TAXO = {"pre-seed": "Pre-Seed", "seed": "Seed", "series a": "Series A"}


def taxonomy(round_word: str | None) -> str | None:
    if not round_word:
        return None
    w = round_word.strip().lower()
    if w in TAXO:
        return TAXO[w]
    if re.match(r"^series [b-z]$", w) or w in {"common", "growth"}:
        return "Growth"
    return None


def key_norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def main() -> None:
    site = ROOT / "sources" / "site"
    cms = {}
    for r in json.loads((site / "sanity-companies.json").read_text())["rows"]:
        cms[key_norm(r["name"])] = r
        cms.setdefault(key_norm(r.get("slug") or ""), r)
    cir = {}
    for r in json.loads((site / "wayback-circles.json").read_text())["companies-circles"]:
        cir[key_norm(r.get("name") or "")] = r
        cir.setdefault(key_norm(r["slug"]), r)

    golden = json.loads((ROOT / "golden.json").read_text())
    rows = golden["stage_golden_set"]["rows"]

    score = {"cms": [0, 0], "circles": [0, 0]}   # [right, answered]
    misses = {"cms": [], "circles": []}
    print(f"{'row':20} {'key':10} {'CMS':10} {'circles':10}")
    print("-" * 56)
    for g in rows:
        k = key_norm(g["slug"])
        want = g["answer"]
        a = taxonomy((cms.get(k) or {}).get("site_stage"))
        b = taxonomy((cir.get(k) or {}).get("site_entry_stage"))
        for name, got in (("cms", a), ("circles", b)):
            if got is None:
                continue
            score[name][1] += 1
            if got == want:
                score[name][0] += 1
            else:
                misses[name].append((g["slug"], want, got))
        flag = ""
        if a and b and a != b:
            flag = "  <- layers disagree"
        print(f"{g['slug'][:20]:20} {want:10} {str(a):10} {str(b):10}{flag}")

    print()
    for name in ("cms", "circles"):
        right, n = score[name]
        pct = f"{100*right/n:.0f}%" if n else "n/a"
        print(f"  layer {name:8}: {right}/{n} ({pct})")
        for slug, want, got in misses[name]:
            print(f"      MISS {slug}: key={want} layer={got}")

    # Agreement over the whole overlap, not just the key: the gate's rule is
    # that agreement is what earns class 1, so its size is the thing to report.
    overlap = [k for k in cms if k in cir and taxonomy(cms[k].get("site_stage"))
               and taxonomy(cir[k].get("site_entry_stage"))]
    seen, agree, disagree = set(), 0, []
    for k in overlap:
        name = cms[k]["name"]
        if name in seen:
            continue
        seen.add(name)
        a, b = taxonomy(cms[k]["site_stage"]), taxonomy(cir[k]["site_entry_stage"])
        if a == b:
            agree += 1
        else:
            disagree.append((name, a, b))
    print(f"\n  full overlap: {len(seen)} companies, {agree} agree, "
          f"{len(disagree)} disagree")
    for name, a, b in sorted(disagree):
        print(f"      {name}: cms={a} circles={b}")


if __name__ == "__main__":
    main()
