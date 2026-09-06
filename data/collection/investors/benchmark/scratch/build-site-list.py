#!/usr/bin/env python3
"""The firm's last published portfolio list, as a site_api file_list source.

benchmark.com has published nothing since 2013, so there is no live surface to
read: the `site_listing` evidence class is archival. The 2010-2013 WordPress
/companies/ cards are the firm's own final list — published after both desk
splits, so it doubles as the home-desk attribution (decisions.md D4.1) — and
this rebuilds it from the parsed wayback years, with the listing years and the
CMS slug per company. Reproducible from sources/wayback/parsed.
"""
import json, sys
from collections import defaultdict
sys.path.insert(0, "scripts")
from paths import Paths, write_atomic                                  # noqa: E402

P = Paths("benchmark")
PATH = "/companies/"
rows = defaultdict(lambda: {"years": set(), "name": None, "slug": None})
for f in sorted((P.wayback / "parsed").glob("*.json")):
    year = int(f.stem)
    for r in json.loads(f.read_text()):
        if r.get("path") != PATH:
            continue
        e = rows[r["slug"]]
        e["years"].add(year); e["slug"] = r["slug"]
        if r.get("name"):
            e["name"] = r["name"]

out = [{"name": v["name"] or v["slug"], "slug": v["slug"],
        "url": f"http://www.benchmark.com/company/{v['slug']}/",
        "listing_years": sorted(v["years"]), "desk": "us"}
       for _, v in sorted(rows.items())]
write_atomic(P.root / "sources" / "site" / "companies-2010-2013.json", json.dumps(
    {"_readme": "The firm's own /companies/ logo cards, 2010-2013 (the last list "
                "benchmark.com ever published), rebuilt from sources/wayback/parsed "
                "by scratch/build-site-list.py. Name and slug are the site's own "
                "rendering (<img alt> and the /company/<slug>/ href).",
     "companies": out}, indent=1) + "\n")
print(f"{len(out)} companies, years {sorted({y for v in rows.values() for y in v['years']})}")
