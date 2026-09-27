#!/usr/bin/env python3
"""Look a term up in the site's companies (name, site, description) and the
firm's posts (title, and the body sentences around the term). Read-only.
Usage: python3 .../scratch/find.py <term> [<term> ...]   (each term on its own)"""
import json, re, sys
from pathlib import Path
INV = Path(__file__).resolve().parents[1]
comps = json.load(open(INV / "sources/site/company-pages.json"))["rows"]
posts = json.load(open(INV / "sources/site/posts.json"))["rows"]
for term in sys.argv[1:]:
    rx = re.compile(r"(?<![A-Za-z0-9])" + re.escape(term), re.I)
    print(f"=== {term}")
    for c in comps:
        if rx.search(c["name"]) or rx.search(c.get("company_site") or "") or rx.search((c.get("description") or "")[:400]):
            print(f"  SITE {c['slug']} | {c['name']} | init={c['initial_investment'] or '-'} {c['site_status'][:7]} | {c['location']} | {', '.join(c['partners'][:3])} | {(c.get('company_site') or '')[:40]}")
    n = 0
    for p in posts:
        if rx.search(p["title"]):
            print(f"  POST {p['date'][:10]} {p['title'][:120]} <{p['url']}>")
            n += 1
        elif rx.search(p["body"]) and n < 2:
            m = rx.search(p["body"])
            ctx = re.sub(r"\s+", " ", p["body"][max(0, m.start() - 160): m.end() + 200])
            print(f"  body {p['date'][:10]} {p['title'][:70]} :: …{ctx}…")
            n += 1
        if n >= 3:
            break
