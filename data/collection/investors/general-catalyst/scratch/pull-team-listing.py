#!/usr/bin/env python3
"""Add the /team listing's own fields to sources/site/team-pages.json.

The /team grid (Webflow, ten a page under ?81b8f179_page=N) is where the firm
states each person's title, department, sectors and office; the /team/<slug>
pages carry only a bio. This walks every listing page (cached under
scratch/site-raw/team-listing-pN.html) and writes title, group (the
department), sectors and location onto each row of team-pages.json, keyed by
slug. People the listing carries without a page, or the reverse, are reported.
"""
import html
import json
import re
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

P = Paths("general-catalyst")
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126 Safari/537.36")


def fetch(page: int) -> str:
    cache = HERE / "site-raw" / f"team-listing-p{page}.html"
    if cache.exists() and cache.stat().st_size:
        return cache.read_text(errors="replace")
    r = subprocess.run(["curl", "-sL", "--max-time", "60", "-A", UA,
                        f"https://www.generalcatalyst.com/team?81b8f179_page={page}"], capture_output=True)
    body = r.stdout.decode("utf-8", errors="replace")
    cache.write_text(body)
    time.sleep(0.3)
    return body


def main() -> None:
    listed: dict[str, dict] = {}
    page = 1
    while True:
        h = fetch(page)
        blocks = h.split('role="listitem" class="team_collection-block w-dyn-item"')[1:]
        new = 0
        for b in blocks:
            s = re.search(r'href="/team/([^"#?]+)"', b)
            if not s or s.group(1) in listed:
                continue
            n = re.search(r'id="name" class="text-size-medium">([^<]+)<', b)
            t = re.search(r'text-wight-semibold line-height">([^<]*)<', b)
            d = re.search(r'fs-list-field="department"[^>]*>([^<]*)<', b)
            listed[s.group(1)] = {
                "name": html.unescape(n.group(1)).strip() if n else "",
                "title": html.unescape(t.group(1)).strip() if t else "",
                "group": html.unescape(d.group(1)).strip() if d else "",
                "sectors": [html.unescape(x).strip() for x in re.findall(r'fs-list-field="sectors">([^<]+)<', b)],
                "location": [html.unescape(x).strip() for x in re.findall(r'fs-list-field="location">([^<]+)<', b)],
                "listing_page": page,
            }
            new += 1
        if not blocks or not new or f"81b8f179_page={page + 1}" not in h:
            break
        page += 1
    tp = P.site / "team-pages.json"
    d = json.load(open(tp))
    seen = set()
    for r in d["rows"]:
        L = listed.get(r["slug"])
        if L:
            r.update({k: L[k] for k in ("title", "group", "sectors", "location")})
            r["name"] = r.get("name") or L["name"]
            seen.add(r["slug"])
        else:
            r.setdefault("title", "")
            r.setdefault("group", "")
    for slug, L in listed.items():
        if slug not in seen:
            d["rows"].append({"slug": slug, "url": f"https://www.generalcatalyst.com/team/{slug}", "name": L["name"],
                              "title": L["title"], "group": L["group"], "sectors": L["sectors"],
                              "location": L["location"], "lines": [], "linkedin_url": "", "x_url": "",
                              "companies": [], "listing_only": True})
    d["_listing"] = f"https://www.generalcatalyst.com/team ({page} listing pages, {len(listed)} people)"
    write_atomic(tp, json.dumps(d, indent=1, ensure_ascii=False) + "\n")
    from collections import Counter
    print(f"listing pages {page}, people {len(listed)}; pages without a listing row: "
          f"{sum(1 for r in d['rows'] if not r.get('group'))}")
    print(Counter(r.get("group") for r in d["rows"]).most_common())


if __name__ == "__main__":
    main()
