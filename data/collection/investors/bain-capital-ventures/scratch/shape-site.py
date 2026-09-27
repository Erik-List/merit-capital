#!/usr/bin/env python3
"""Flatten the Sanity pull (sources/site/sanity-*.json) into the two file_list
sources the pipeline reads: sources/site/company-pages.json and team-pages.json.

Portfolio docs carry the firm's own year of investment, a stage tag list
(Seed / Early / Growth, plus the outcome tags IPO and Acquired), sector
"domains", HQ location, founded year, website and partner references to team
docs. The partner refs are resolved to names here so the base build can carry
them as partners_site.
"""
import json, re
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent / "sources" / "site"
BASE = "https://baincapitalventures.com"


def rows(name):
    return json.loads((SITE / name).read_text())["rows"]


team = rows("sanity-team.json")
people = {t["_id"]: f'{t.get("firstname","").strip()} {t.get("last_name","").strip()}'.strip()
          for t in team}
# external "partner" docs (co-authors, operators) resolve too, for completeness
for d in rows("sanity-partners.json"):
    people.setdefault(d["_id"], f'{d.get("firstname","").strip()} {d.get("lastname","").strip()}'.strip())

out = []
for d in rows("sanity-portfolio.json"):
    stages = [s for s in (d.get("stage_names") or []) if s]
    entry = [s for s in stages if s in ("Seed", "Early", "Growth")]
    outcome = [s for s in stages if s in ("IPO", "Acquired")]
    slug = (d.get("slug") or {}).get("current") or ""
    out.append({
        "name": (d.get("title") or "").strip(),
        "slug": slug,
        "id": d["_id"],
        "url": f"{BASE}/portfolio/{slug}/" if slug else "",
        "invest_year": d.get("year_of_investment") or "",
        "site_stage": entry,
        "site_outcome": outcome,
        "sectors": d.get("domain_names") or [],
        "location": d.get("location") or "",
        "founded": d.get("founded") or "",
        "company_site": d.get("company_website") or "",
        "about": (d.get("about") or d.get("short_description") or "").strip(),
        "popover": (d.get("popover") or "").strip(),
        "partners": [people.get(p["_ref"], "") for p in (d.get("partner") or []) if p.get("_ref")],
        "wp_id": d.get("wpId") or "",
        "ai_flag": bool(d.get("ai")),
    })
# Two CMS docs can carry one title for two companies ("Adaptive": Adaptive Security at /portfolio/adaptive/,
# the home-health Adaptive at /portfolio/adaptive-health/). The base keys rows by name, so a shared title would
# fold them into one row. The doc whose CMS slug is the plain name keeps it; the other takes its domain in
# brackets (the shared-names rule, Erik 2026-09-24).
from collections import Counter
from urllib.parse import urlparse
_n = Counter(r["name"].lower() for r in out)
for r in out:
    if _n[r["name"].lower()] > 1 and r["slug"] != re.sub(r"[^a-z0-9]+", "-", r["name"].lower()).strip("-"):
        dom = urlparse(r["company_site"]).netloc.removeprefix("www.")
        if dom:
            r["name"] = f'{r["name"]} ({dom})'
out.sort(key=lambda r: r["name"].lower())
(SITE / "company-pages.json").write_text(json.dumps({
    "_readme": "Flattened by scratch/shape-site.py from sanity-portfolio.json (the live CMS, "
               "280 docs). invest_year is the firm's own year_of_investment; site_stage is the "
               "stage tag (Seed / Early / Growth) and site_outcome the outcome tag (IPO / "
               "Acquired); partners are the team docs the CMS links as the deal partners.",
    "rows": out}, indent=1) + "\n")

groups = {g["_id"]: g.get("name") for g in rows("sanity-teamgroups.json")}
positions = {p["_id"]: p.get("name") or p.get("title") for p in rows("sanity-positions.json")}
tout = []
for t in team:
    name = people[t["_id"]]
    socials = t.get("social_links") or []
    li = x = ""
    for s in socials if isinstance(socials, list) else []:
        u = ((s.get("cta") or {}).get("url") or s.get("url") or "") if isinstance(s, dict) else ""
        if "linkedin.com" in u and not li:
            li = u
        if ("twitter.com" in u or "x.com/" in u) and not x:
            x = u
    def refs(v):
        v = v if isinstance(v, list) else [v] if isinstance(v, dict) else []
        return [x.get("_ref") for x in v if isinstance(x, dict) and x.get("_ref")]
    grp = "; ".join(g for g in (groups.get(r) for r in refs(t.get("teamgroup"))) if g)
    pos = "; ".join(q for q in (positions.get(r) for r in refs(t.get("position"))) if q)
    slug = (t.get("slug") or {}).get("current") or ""
    tout.append({"name": name, "slug": slug, "url": f"{BASE}/team/{slug}/" if slug else "",
                 "title": pos, "group": grp, "location": t.get("location") or "",
                 "linkedin_url": li, "x_url": x,
                 "companies": [], "wp_id": t.get("wpId") or ""})
tout.sort(key=lambda r: r["name"].lower())
(SITE / "team-pages.json").write_text(json.dumps({
    "_readme": "Flattened by scratch/shape-site.py from sanity-team.json (66 docs, four groups).",
    "rows": tout}, indent=1) + "\n")
print(len(out), "companies;", len(tout), "people")
import collections
print(collections.Counter(r["group"] for r in tout))
print(collections.Counter(r["title"] for r in tout).most_common(20))
print(sum(1 for r in out if r["partners"]), "companies with partners")
print(collections.Counter(p for r in out for p in r["partners"]).most_common(40))
