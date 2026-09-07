#!/usr/bin/env python3
"""Fold the archived per-company page reads back into the parsed wayback rows.

`cdx_company_pages` enumerates /portfolio/<slug> from the CDX index and never
opens the page, so 175 of Khosla's 429 slugs land unnamed and none carries the
firm's own sector or investment year. scratch/company-pages.py reads those
bodies; this folds the result into sources/wayback/parsed/<year>.json, in the
three fields build-company-base.py already reads from a parsed row:

  name         so the row is published as the firm rendered it. COLLECTION.md
               §5.1a: a capture slug never names a row -- and Khosla's book is
               full of one-word slugs (block, rocket, go, fresh, even, plum,
               swift, castle) that a slugified display would get wrong in the
               First Round Wikidata way.
  filters      the firm's own /portfolio/<sector> categories, comma-joined, the
               same shape the wayback sector filters use on other sites.
  invest_year  the firm's own <table class=dates> "Invested" year. Read as a
               CLOSE year, never an announcement date (COLLECTION.md §6, the
               Menlo rule), and scored on the golden set before it may label.

Fixing this in the PARSED SOURCE rather than through site_api is deliberate:
the archived page is the same publisher making the same claim as the live site,
so it belongs in the same column, and routing it through site_api instead would
count one source twice and lift every archived row from tier B to tier A.
(COLLECTION.md §5.1's First Round rule: parsed-source fixes over merges.)

Re-runnable. Usage: python3 scratch/wayback-merge-pages.py
"""
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
PARSED = HERE / "sources" / "wayback" / "parsed"
PAGES = HERE / "sources" / "wayback" / "company-pages.json"


def main():
    if not PAGES.exists():
        sys.exit(f"no {PAGES} — run scratch/company-pages.py first")
    pages = json.load(open(PAGES))["companies"]
    named = sum(1 for v in pages.values() if v and v.get("name"))
    print(f"company-pages: {len(pages)} slugs, {named} named")

    n_name = n_cat = n_year = 0
    for f in sorted(PARSED.glob("*.json")):
        rows = json.load(open(f))
        changed = False
        for r in rows:
            p = pages.get(r["slug"])
            if not p:
                continue
            if p.get("name") and not r.get("name"):
                r["name"] = p["name"]
                n_name += 1
                changed = True
            cats = p.get("categories_site") or []
            if cats and not r.get("filters"):
                r["filters"] = ",".join(cats)
                n_cat += 1
                changed = True
            if p.get("site_invest_year") and not r.get("invest_year"):
                r["invest_year"] = p["site_invest_year"]
                n_year += 1
                changed = True
        if changed:
            f.write_text(json.dumps(rows, indent=1))
    print(f"filled: {n_name} names, {n_cat} category sets, {n_year} invest years")

    allslugs, unnamed = set(), set()
    for f in sorted(PARSED.glob("*.json")):
        for r in json.load(open(f)):
            allslugs.add(r["slug"])
            if not r.get("name"):
                unnamed.add(r["slug"])
    unnamed -= {s for s in allslugs if any(
        r.get("name") for f in PARSED.glob("*.json") for r in json.load(open(f))
        if r["slug"] == s)}
    print(f"parsed rows: {len(allslugs)} slugs, {len(unnamed)} still unnamed")
    if unnamed:
        print("  " + ", ".join(sorted(unnamed)[:40]))


if __name__ == "__main__":
    main()
