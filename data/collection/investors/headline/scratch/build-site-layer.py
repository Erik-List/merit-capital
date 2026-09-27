"""Build Headline's site layer from its public Sanity dataset.

headline.com is a Gatsby site over Sanity project `iznipsfw` (dataset
`production`), whose public query API serves the whole dataset:
  https://iznipsfw.apicdn.sanity.io/v2021-10-21/data/query/production?query=*[_type=="company"]
The raw per-type dumps are in sources/site/sanity/<type>.json (pulled
2026-09-27); the rendered portfolio grid is sources/site/portfolio-page-data.json
(Gatsby's own /page-data/portfolio/page-data.json, 211 company nodes).

Writes:
  sources/site/sanity-companies.json  one row per company doc that the live site shows,
      on the portfolio grid (surface "portfolio") or only in a team member's
      portfolio list on /team/<member>/ (surface "team_page"), plus the CMS docs
      the site hides (surface "cms_hidden", url = the Sanity query for that doc):
      a CMS flag is not a verdict (COLLECTION.md s5), so those rows are judged.
  sources/site/team-cards.json  the team, one row per teamMember doc.

Fields carried per company: the fund pages that reference it (`desks`: US, EU,
Global Growth, Asia, Brazil), the firm's own dated stage list (`stages`: phase
and year per fund entry, e.g. "Early 2019; Growth 2021"), its earliest entry
(`stage_site_first`, `invest_year`), outcome and ticker line, location, founders,
website, sectors, and the investors who list it on their team pages
(`partners`)."""
import json
import re
import urllib.parse
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SITE = HERE / "sources" / "site"
S = SITE / "sanity"


def load(t):
    return json.loads((S / f"{t}.json").read_text())["result"]


companies = load("company")
funds = {x["_id"]: x["title"] for x in load("fund")}
regions = {x["_id"]: x["title"] for x in load("region")}
sectors = {x["_id"]: x["title"] for x in load("sector")}
team_groups = {x["_id"]: x["title"] for x in load("team") + load("investmentTeam") + load("specialistTeam")}
members = load("teamMember")
grid = json.loads((SITE / "portfolio-page-data.json").read_text())["result"]["data"]["companies"]["nodes"]
rendered = {c["_id"] for c in grid}
by_id = {c["_id"]: c for c in companies}


def ref(x, key):
    v = x.get(key) or {}
    return v.get("_ref") if isinstance(v, dict) else None


listed_by = {}
for m in members:
    for r in m.get("portfolio", []):
        rid = r.get("_ref") or ref(r, "company")
        if rid:
            listed_by.setdefault(rid, []).append(m)

rows = []
for c in companies:
    cid = c["_id"]
    slug = (c.get("slug") or {}).get("current")
    lister = listed_by.get(cid, [])
    if cid in rendered:
        surface = "portfolio"
        url = f"https://headline.com/portfolio/{slug}/" if slug else "https://headline.com/portfolio/"
    elif lister:
        surface = "team_page"
        ms = (lister[0].get("slug") or {}).get("current")
        url = f"https://headline.com/team/{ms}/"
    else:
        surface = "cms_hidden"
        q = f'*[_type=="company" && _id=="{cid}"]'
        url = ("https://iznipsfw.apicdn.sanity.io/v2021-10-21/data/query/production?query="
               + urllib.parse.quote(q))
    stages = sorted(((s.get("phase") or "").strip(), str(s.get("year") or "").strip())
                    for s in c.get("stages", []))
    dated = [s for s in stages if re.match(r"^\d{4}", s[1])]
    first = min(dated, key=lambda s: s[1][:4]) if dated else (stages[0] if stages else ("", ""))
    outcome = "; ".join(f"{o.get('phase','')} {o.get('year','')}".strip() for o in c.get("outcome", []))
    sd = c.get("structuredData") or {}
    rows.append({
        "name": c["title"].strip(),
        "url": url,
        "cms_id": cid,
        "cms_slug": slug or "",
        "surface": surface,
        "hidden": bool(c.get("hidden")),
        "desks": [funds.get(ref(x, "fund"), "?") for x in c.get("fund", [])],
        "regions": [regions.get(ref(x, "region"), "?") for x in c.get("regions", [])],
        "sectors": [sectors.get(ref(x, "sector"), "?") for x in c.get("sectors", [])],
        "stages": "; ".join(f"{p} {y}".strip() for p, y in stages),
        "stage_site_first": first[0],
        "invest_year": first[1][:4] if re.match(r"^\d{4}", first[1]) else "",
        "outcome": outcome,
        "subline": (c.get("subline") or "").strip(),
        "location": (c.get("location") or "").strip(),
        "founders": c.get("founders") or [],
        "website": sd.get("url") or "",
        "description": ((c.get("seo") or {}).get("description") or "").strip(),
        "partners": [m["name"] for m in lister],
    })

rows.sort(key=lambda r: r["name"].lower())
(SITE / "sanity-companies.json").write_text(json.dumps({
    "_readme": __doc__,
    "source": "https://iznipsfw.apicdn.sanity.io/v2021-10-21/data/query/production (pulled 2026-09-27)",
    "count": len(rows),
    "rows": rows,
}, indent=1, ensure_ascii=False) + "\n")

team = []
for m in members:
    groups = [team_groups.get(ref(x, "team"), "?") for x in m.get("team", [])]
    inv = [team_groups.get(ref(x, "team"), "?") for x in m.get("investmentTeam", [])]
    spec = [team_groups.get(ref(x, "team"), "?") for x in m.get("specialistTeam", [])]
    links = {(l.get("text") or "").lower(): l.get("url") for l in m.get("socialLinks", [])}
    ms = (m.get("slug") or {}).get("current")
    team.append({
        "name": m["name"].strip(),
        "url": f"https://headline.com/team/{ms}/" if ms else "https://headline.com/team/",
        "title": (m.get("role") or "").strip(),
        "group": (groups[0] if groups else ""),
        "investment_team": inv,
        "specialist_team": spec,
        "region": [regions.get(ref(x, "region"), "?") for x in m.get("region", [])],
        "linkedin_url": next((u for k, u in links.items() if "linkedin" in k or "linkedin.com" in (u or "")), ""),
        "x_url": next((u for k, u in links.items() if k in ("x", "twitter") or "x.com/" in (u or "") or "twitter.com/" in (u or "")), ""),
        "companies": [by_id[r.get("_ref") or ref(r, "company")]["title"]
                      for r in m.get("portfolio", []) if (r.get("_ref") or ref(r, "company")) in by_id],
    })
team.sort(key=lambda r: r["name"])
(SITE / "team-cards.json").write_text(json.dumps({
    "_readme": "Headline team from the Sanity teamMember docs (sources/site/sanity/teamMember.json, 2026-09-27); "
               "group is the site's own team (Investors / Specialists / Advisory Board), title the CMS role.",
    "count": len(team), "rows": team}, indent=1, ensure_ascii=False) + "\n")

from collections import Counter
print("companies:", len(rows), Counter(r["surface"] for r in rows))
print("first stage:", Counter(r["stage_site_first"] for r in rows).most_common())
print("team:", len(team), Counter(t["group"] for t in team))
