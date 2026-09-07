#!/usr/bin/env python3
"""Curate partner-roster.json before the base is built. Re-runnable.

Two defects, both named in decisions.md and both fatal to
build-company-base.py's ex-partner rule if left alone:

D10 -- one person under two slugs is two people to the tenure filter
       (COLLECTION.md §8, First Round 2026-09-06). Collapse to one entry with
       the UNION window and record the basis. Khosla's five:
       kanu-gulati/kanupriya-gulati, avisha-mehra/avisha-mehra-naganath,
       kathy-chan/kathy-h-chan, tamara-tompkins/tamara-l-tompkins, and
       qa-irene-au, a staging artifact of irene-au.

D11 -- the CDX pattern reaches /team/<first-last> and /team-member/<first-last>
       only, so the roster starts in 2014. Khosla's first decade used
       /people_<initials>.html (2010-2013) and /<lastname>.html (2006-2009), and
       a 2014+ roster structurally misses the partner-anchored Form D filings of
       exactly the years the cleantech book was built. Those names are resolved
       by scratch/pre2014-roster.py from the page titles and folded in here with
       their capture years.

Not people: `the-designer-fund` (a program page in the same namespace) and
`qa-irene-au` (a staging artifact) are dropped, not merged.

Usage: python3 scratch/roster-curate.py
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
ROSTER = HERE / "sources" / "wayback" / "partner-roster.json"
PRE2014 = HERE / "sources" / "wayback" / "pre2014-people.json"

# canonical slug -> variants folded into it
MERGES = {
    "kanupriya-gulati": ["kanu-gulati"],
    "avisha-mehra-naganath": ["avisha-mehra"],
    "kathy-h-chan": ["kathy-chan"],
    "tamara-l-tompkins": ["tamara-tompkins"],
    "irene-au": ["qa-irene-au"],
}
DROP = {"the-designer-fund", "designer-fund", "df"}
# initials/lastname pages that are not a person, or whose title fetch degraded
# to the site's generic title; the name is taken from the sibling capture year.
PRE2014_FIX = {
    "people_df": None,                 # "the designer fund" -- a program, not a person
    "people_ra": "Ramy Adeeb",         # /adeeb.html resolves the same person
    "people_sk": "Samir Kaul",
    "people_ss": "Shirish Sathaye",
    "people_rk": "Ryan Kottenstette",
    "people_dm": "David Mann",
    "people_ac": "Andrew Chung",
    "early_vinod": "Vinod Khosla",
    "early_white": None,               # title degraded to boilerplate; no such partner confirmed
}


def slugify(n):
    return re.sub(r"[^a-z0-9]+", "-", n.lower()).strip("-")


def main():
    people = json.load(open(ROSTER))
    by = {p["slug"]: p for p in people}

    merged = []
    for canon, variants in MERGES.items():
        if canon not in by:
            continue
        c = by[canon]
        for v in variants:
            if v not in by:
                continue
            o = by.pop(v)
            if v == "qa-irene-au":                       # staging artifact, not a window
                c.setdefault("_curation", []).append(f"dropped staging duplicate {v}")
                merged.append((canon, v, "dropped (staging artifact)"))
                continue
            c["years_seen"] = sorted(set(c.get("years_seen", [])) | set(o.get("years_seen", [])))
            c["first_seen"] = min(x for x in (c.get("first_seen"), o.get("first_seen")) if x)
            c["last_seen"] = max(x for x in (c.get("last_seen"), o.get("last_seen")) if x)
            c["snapshots"] = (c.get("snapshots") or []) + (o.get("snapshots") or [])
            c["sources"] = sorted(set(c.get("sources", [])) | set(o.get("sources", [])))
            c.setdefault("_curation", []).append(
                f"union window with duplicate slug {v} (COLLECTION.md §8, two-spellings rule)")
            merged.append((canon, v, f"union -> {c['first_seen']}-{c['last_seen']}"))

    for s in list(by):
        if s in DROP:
            by.pop(s)

    added = []
    if PRE2014.exists():
        pre = json.load(open(PRE2014))["people"]
        for key, rec in pre.items():
            name = PRE2014_FIX.get(key, rec.get("name"))
            if name is None and key in PRE2014_FIX:
                continue
            if not name or len(name.split()) < 2 or "khosla ventures" in name.lower():
                continue
            name = " ".join(w if w.isupper() else w.capitalize() for w in name.split())
            slug = slugify(name)
            yr = int(rec["year"])
            if slug in by:
                p = by[slug]
                p["years_seen"] = sorted(set(p.get("years_seen", [])) | {yr})
                p["first_seen"] = min(p["first_seen"], yr) if p.get("first_seen") else yr
                p["sources"] = sorted(set(p.get("sources", [])) | {rec["source"]})
                p.setdefault("_curation", []).append(
                    f"first_seen pulled back to {p['first_seen']} from {rec['path']} "
                    f"({rec['year']}) — pre-2014 namespace, COLLECTION.md §5.2")
                added.append((slug, f"window extended to {p['first_seen']}"))
            else:
                by[slug] = {"slug": slug, "name": name, "years_seen": [yr],
                            "first_seen": yr, "last_seen": yr, "snapshots": [],
                            "sources": [rec["source"]],
                            "_curation": [f"pre-2014 roster, resolved from {rec['path']} "
                                          f"({rec['year']}); decisions.md D11"]}
                added.append((slug, f"NEW {yr}"))

    out = sorted(by.values(), key=lambda p: p["slug"])
    ROSTER.write_text(json.dumps(out, indent=1))
    print(f"merged {len(merged)} duplicate slugs:")
    for c, v, how in merged:
        print(f"   {v:26s} -> {c:26s} {how}")
    print(f"pre-2014 folded in: {len(added)}")
    for s, how in added:
        print(f"   {s:26s} {how}")
    print(f"roster now {len(out)} people, coverage "
          f"{min(p['first_seen'] for p in out if p.get('first_seen'))}–"
          f"{max(p['last_seen'] for p in out if p.get('last_seen'))}")


if __name__ == "__main__":
    main()
