#!/usr/bin/env python3
"""Pull the investor's current portfolio and team from their own site's API.

Why this layer exists: the three SEC/archive layers all structurally miss recent
private companies. The modern portfolio page is JS-rendered with no per-company
URLs, so the Wayback CDX trick cannot enumerate it; and many current startups
raise under Section 4(a)(2) rather than Reg D, so they file no Form D at all
(Etched and Rillet file nothing — only third-party SPVs do). Neither has IPO'd,
so EDGAR is silent too.

The site's own CMS is the authoritative answer. sequoiacap.com runs WordPress
with an open REST API exposing `company`, `team-member` and `founder` post types.

Reusable pattern for any investor site, in order of preference:
  1. WordPress REST   /wp-json/wp/v2/types -> find the post type -> paginate it
  2. Next.js          __NEXT_DATA__ script tag, or /_next/data/<build>/*.json
  3. Any SPA          watch XHR in the browser pane, then call that endpoint
  4. Last resort      render the page headless and parse the DOM

Output: data/aggregation/sources/site/companies.json, team.json
"""
import json
import subprocess
import sys
import time
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "aggregation" / "sources" / "site"
UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
BASE = "https://www.sequoiacap.com/wp-json/wp/v2"
PER_PAGE = 100


def get(url: str) -> list:
    for attempt in range(4):
        try:
            out = subprocess.run(
                ["curl", "-sf", "--max-time", "60", "-H", f"User-Agent: {UA}", url],
                capture_output=True, check=True).stdout
            return json.loads(out)
        except (subprocess.CalledProcessError, json.JSONDecodeError):
            time.sleep(1.5 * (attempt + 1))
    return []


def fetch_type(rest_base: str) -> list[dict]:
    rows, page = [], 1
    while True:
        batch = get(f"{BASE}/{rest_base}?per_page={PER_PAGE}&page={page}")
        if not batch:
            break
        rows.extend(batch)
        if len(batch) < PER_PAGE:
            break
        page += 1
        time.sleep(0.3)
    return rows


def categories_from(class_list) -> list[str]:
    return sorted({c[len("category-"):] for c in (class_list or [])
                   if c.startswith("category-")})


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    raw = fetch_type("company")
    companies = [{
        "name": unescape(c["title"]["rendered"]).strip(),
        "slug": c["slug"],
        "sectors": categories_from(c.get("class_list")),
        "url": c.get("link"),
        "published": (c.get("date") or "")[:10],
        "modified": (c.get("modified") or "")[:10],
    } for c in raw if c.get("title", {}).get("rendered")]
    companies.sort(key=lambda c: c["name"].lower())
    (OUT / "companies.json").write_text(json.dumps(companies, indent=1) + "\n")

    team = fetch_type("team-member")
    people = [{
        "name": unescape(t["title"]["rendered"]).strip(),
        "slug": t["slug"],
        "url": t.get("link"),
    } for t in team if t.get("title", {}).get("rendered")]
    people.sort(key=lambda p: p["name"].lower())
    (OUT / "team.json").write_text(json.dumps(people, indent=1) + "\n")

    from collections import Counter
    sect = Counter(s for c in companies for s in c["sectors"])
    print(f"companies: {len(companies)}   team members: {len(people)}")
    print("  top sectors:", dict(sect.most_common(8)))
    print("  sample:", [c["name"] for c in companies[:6]])


if __name__ == "__main__":
    main()
