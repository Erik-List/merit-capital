#!/usr/bin/env python3
"""One evidence view per base row for the grind: the firm's own company page
(Partnered year, Founded, status, stage word, location, team, founders,
website, description), every insights post that links the company page or
names it in its title (kind, archived WordPress date, press article URL, the
first 400 characters of its body), the partners on the Form D sweep, and the
full-text sweep registrants that name the company. Output
scratch/evidence-pack.json keyed by base slug; citations are read from here
by key, never typed (Balderton's lesson: 19 hand-completed URLs were wrong)."""
import json, re
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
base = json.load(open(ROOT / "companies" / "base.json"))
site = {r["url"]: r for r in json.load(open(ROOT / "sources" / "site" / "companies-list.json"))["rows"]}
ins = json.load(open(ROOT / "sources" / "site" / "insights.json"))["rows"]
fts = json.load(open(ROOT / "sources" / "edgar" / "fts-hits.json"))["registrants"]
def loose(s):
    return re.sub(r"[^a-z0-9]+", "", re.sub(r"\b(inc|ltd|ab|as|gmbh|limited|corp|llc|bv|oy|aps|sa|se|plc)\b\.?", "", (s or "").lower()))
out = {}
for r in base:
    s = site.get(r.get("site_url") or "")
    page_slug = (r.get("site_url") or "").rstrip("/").rsplit("/", 1)[-1]
    k = loose(r["name"])
    posts = []
    for p in ins:
        t = (p.get("title") or "")
        hit = page_slug and page_slug in (p.get("portfolio_links") or [])
        if not hit and len(k) >= 4:
            hit = bool(re.search(r"(?<![a-z0-9])" + re.escape(k) + r"(?![a-z0-9])", loose(t).replace("", "")) or k in loose(t))
        if hit:
            posts.append({"url": p["url"], "kind": p.get("kind"), "date": p.get("date_wp"), "title": t,
                          "article": p.get("article_url"), "body": (p.get("body") or "")[:400]})
    out[r["slug"]] = {
        "name": r["name"], "tier": r.get("tier"), "first_seen": r.get("first_seen"),
        "site": ({k2: s.get(k2) for k2 in ("url", "invest_year", "founded_year", "status_site", "stage_site_word",
                  "unicorn_tag", "location_site", "partners", "founders", "website", "description")} if s else None),
        "partners_formd": r.get("partners_formd"), "formd_links": r.get("formd_links"),
        "posts": sorted(posts, key=lambda x: x["date"] or "9999"),
        "fts": [{"registrant": f["registrant"], "forms": f["forms"], "first": f["first_date"],
                 "url": f["filings"][0]["url"]} for f in fts if k and len(k) >= 4 and k in loose(f["registrant"])],
    }
(HERE / "evidence-pack.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
print(len(out), "rows;", sum(1 for v in out.values() if v["posts"]), "with posts;",
      sum(len(v["posts"]) for v in out.values()), "post links")
