#!/usr/bin/env python3
"""Desk lineage for Benchmark rows, read off the firm's own listing surfaces.

decisions.md D4, mechanically: benchmark.com published separate portfolio
pages per desk (Silicon Valley / Europe / Israel) from 2003 to 2009, and one
undifferentiated list before and after. So a slug's desk is decided by which
era paths carried it:

  1. On the POST-SPLIT list (/companies/, 2010-2013, published after Balderton
     2007 and Benchmark Israel VC 2007 became separate firms) -> `us`.
     The firm's own claim on its own book outranks every earlier page.
  2. Else on a home-desk page (/Silicon_Valley/Silicon_Valley_Portfolio.html
     2003-2005, /portfolio/worldwide/sv.shtml 2005-2009) -> `us`.
  3. Else on a Europe page only -> `europe`; on an Israel page only -> `israel`.
     (Both -> the desk with more listing years; ties -> `europe`, reported.)
  4. Else (union pages only: p-alpha, Portfolio_By_Location, worldwide.shtml)
     -> `us`, the home desk, which is also the build's own default.

Writes the `desk` array of identity-merges.json (merging with whatever else
that file holds) and prints the partitioned names for the report.
"""
import json, sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, "scripts")
from paths import Paths, write_atomic                                # noqa: E402

P = Paths("benchmark")
US_POST_SPLIT = "/companies/"
US_DESK = {"/portfolio/worldwide/sv.shtml",
           "/Silicon_Valley/Silicon_Valley_Portfolio.html"}
EUROPE = {"/Europe/Europe_Portfolio.html", "/portfolio/worldwide/europe.shtml"}
ISRAEL = {"/Israel/Israel_Portfolio.html", "/portfolio/worldwide/israel.shtml"}

paths_by_slug: dict[str, set] = defaultdict(set)
years_by_slug_path: dict[tuple, set] = defaultdict(set)
names: dict[str, str] = {}
for f in sorted((P.wayback / "parsed").glob("*.json")):
    year = int(f.stem)
    for r in json.loads(f.read_text()):
        paths_by_slug[r["slug"]].add(r.get("path"))
        years_by_slug_path[(r["slug"], r.get("path"))].add(year)
        if r.get("name") and r["slug"] not in names:
            names[r["slug"]] = r["name"]

desks, tie = {}, []
for slug, paths in paths_by_slug.items():
    if US_POST_SPLIT in paths or (US_DESK & paths):
        desks[slug] = "us"
        continue
    eu = EUROPE & paths
    il = ISRAEL & paths
    if eu and il:
        ny_eu = len({y for p in eu for y in years_by_slug_path[(slug, p)]})
        ny_il = len({y for p in il for y in years_by_slug_path[(slug, p)]})
        desks[slug] = "israel" if ny_il > ny_eu else "europe"
        tie.append((slug, ny_eu, ny_il, desks[slug]))
    elif eu:
        desks[slug] = "europe"
    elif il:
        desks[slug] = "israel"
    else:
        desks[slug] = "us"

# The file is keyed by investor slug (build-company-base.py reads
# json[SLUG]); everything else in this investor's block is preserved.
doc = json.loads(P.identity_merges.read_text()) if P.identity_merges.exists() else {}
block = doc.setdefault("benchmark", {})
block["desk"] = [{"slug": s, "lineage": d} for s, d in sorted(desks.items()) if d != "us"]
block.setdefault("merges", [])
block.setdefault("never_merge", [])
block["_readme"] = (
    "The `desk` array is written by scratch/derive-desks.py from the parsed "
    "wayback era paths (decisions.md D2-D4): Benchmark's own site published "
    "per-desk portfolio pages, so the Europe (Balderton from 2007) and Israel "
    "(Benchmark Israel VC 2007 Ltd) rows are separable from the home book by "
    "the path that listed them. Re-runnable; `merges` and `never_merge` are "
    "curated by hand and preserved.")
write_atomic(P.identity_merges, json.dumps(doc, indent=1) + "\n")

from collections import Counter
print(Counter(desks.values()))
for d in ("europe", "israel"):
    rows = sorted(s for s, v in desks.items() if v == d)
    print(f"\n{d} ({len(rows)}): " + ", ".join(names.get(s, s) for s in rows))
if tie:
    print("\nlisted on both desks:", tie)
