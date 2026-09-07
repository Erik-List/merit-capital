#!/usr/bin/env python3
"""Widen the partner roster with the firm's own deal attributions.

`partner-roster.py` builds tenure windows from the years a person's PROFILE
PAGE was captured, which on Greylock is wrong in both directions and by
decades: the site publishes its founders as "Emeritus", so Bill Elfers (who
co-founded the firm in 1965 and died in 2016) reads first_seen 2022, while a
partner who left in 2022 but stays on an alumni page reads last_seen 2026.
COLLECTION.md §8 already warns that a capture window is a proxy and that the
variants must be collapsed with their basis before the base is built.

Greylock publishes a better witness: its own listings name the GREYLOCK PARTNER
on each company, and each company carries the firm's own YEAR FUNDED.  So a
partner's window is bounded below by the earliest deal the firm attributes to
them and above by the latest capture that still attributes one -- evidence,
not memory.  This unions those windows into partner-roster.json, keeps the
richer of the two where both exist, and records the basis per person.

Run AFTER partner-roster.py, before build-company-base.py.
"""
import json, pathlib, re
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[5]
INV = ROOT / "data/collection/investors/greylock"
ROSTER = INV / "sources/wayback/partner-roster.json"
CARDS = INV / "sources/site/archive-cards.json"

# One entry per person: partner-roster.py unions by slug, so a person under two
# spellings is two people to the tenure filter (COLLECTION.md §8, First Round).
ALIASES = {"dave-strohm": "david-strohm", "wade-chambers-2": "wade-chambers",
           "don-sullivan": "donald-sullivan"}

ERA_YEAR = {"2005-2010 coldfusion": None, "2011-2014 rails": None}


def slugify(name):
    s = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return ALIASES.get(s, s)


def main():
    cards = json.loads(CARDS.read_text())["rows"]
    seen = defaultdict(lambda: {"years": set(), "deals": [], "capture": set()})
    for c in cards:
        for p in c.get("partners") or []:
            if not p or len(p) > 40:
                continue
            e = seen[slugify(p)]
            e.setdefault("name", p)
            if c.get("invest_year"):
                e["years"].add(int(c["invest_year"]))
            e["deals"].append(c["name"])
            for s in c.get("sources") or []:
                m = re.search(r"\((\d{4})", s)
                if m:
                    e["capture"].add(int(m.group(1)))
    roster = json.loads(ROSTER.read_text()) if ROSTER.exists() else []
    by = {}
    for r in roster:
        by[ALIASES.get(r["slug"], r["slug"])] = r        # collapse variants
    for slug, e in seen.items():
        yrs = sorted(e["years"])
        first = yrs[0] if yrs else min(e["capture"] or [2005])
        last = max(list(e["capture"]) + ([yrs[-1]] if yrs else []))
        basis = (f"{len(e['deals'])} deals attributed by the firm's own listings"
                 + (f", {yrs[0]}-{yrs[-1]}" if yrs else "")
                 + f"; listings captured {min(e['capture'])}-{max(e['capture'])}"
                 if e["capture"] else "")
        cur = by.get(slug)
        if cur:
            cur["first_seen"] = min(cur.get("first_seen", first), first)
            cur["last_seen"] = max(cur.get("last_seen", last), last)
            cur["years_seen"] = sorted(set(cur.get("years_seen", [])) | e["capture"] | set(yrs))
            cur["snapshots"] = max(cur.get("snapshots", 0), len(e["deals"]))
            cur.setdefault("sources", []).append("archive-attribution")
            cur["attribution_basis"] = basis
        else:
            by[slug] = {"slug": slug, "name": e["name"],
                        "years_seen": sorted(e["capture"] | set(yrs)),
                        "first_seen": first, "last_seen": last,
                        "snapshots": len(e["deals"]),
                        "sources": ["archive-attribution"],
                        "attribution_basis": basis}
    # Names that are on the site team but are not investors and carry no deal
    # attribution. partner-roster.py's site_team_groups filter cannot see them
    # (their Sanity `category` is empty) and its not_a_person list only reaches
    # CDX-derived slugs, so the prune happens here -- the First Round rule that
    # a people namespace is checked for what it actually contains before it is
    # swept. Left in, each confirmed a false member off a common-name Form D
    # match: John Delaney -> Alliance Partners LLC, Julie Smith -> Carbon Health
    # and e-Scape Bio.
    NOT_INVESTORS = {"cyrus-pinto", "dwane-hamilton", "john-delaney",
                     "julie-smith", "katy-amaya"}
    for slug in list(by):
        if slug in NOT_INVESTORS and "archive-attribution" not in (by[slug].get("sources") or []):
            del by[slug]
    out = sorted(by.values(), key=lambda r: r["slug"])
    ROSTER.write_text(json.dumps(out, indent=1))
    added = [s for s in seen if s not in {ALIASES.get(r["slug"], r["slug"]) for r in roster}]
    print(f"roster now {len(out)} people ({len(roster)} before); "
          f"{len(seen)} carry the firm's own deal attribution, {len(added)} of them new")
    for r in out:
        if "archive-attribution" in (r.get("sources") or []):
            print(f"  {r['slug']:24} {r['first_seen']}-{r['last_seen']}  {r.get('attribution_basis','')[:78]}")


if __name__ == "__main__":
    main()
