"""Flatten the Sanity export (sources/site/sanity/, pull-sanity.py) into the two file_list sources the pipeline reads:
sources/site/company-list.json (one row per `company` document) and sources/site/team-pages.json (one row per
`bvpTeamMember`). Deal partners are the company's `investors` references resolved to names; sectors are the
referenced sector labels. Usage: python3 shape-site.py"""
import json
from pathlib import Path
S = Path(__file__).resolve().parents[1] / "sources" / "site"
L = lambda t: json.loads((S / "sanity" / f"{t}.json").read_text())["result"]
co, tm, sec = L("company"), L("bvpTeamMember"), L("sector")
tid = {t["_id"]: t for t in tm}
sid = {s["_id"]: s.get("label") for s in sec}
def text(blocks):
    return " ".join(ch.get("text", "") for b in blocks or [] if isinstance(b, dict) for ch in b.get("children") or []).strip()
rows = []
for c in co:
    slug = (c.get("slug") or {}).get("current")
    mig = c.get("migration") or {}
    rows.append({
        "name": c["name"].strip(), "url": f"https://www.bvp.com/portfolio/{slug}", "site_slug": slug,
        "sectors": [sid[s["_ref"]] for s in c.get("sectors") or [] if sid.get(s["_ref"])],
        "stage_site": " | ".join(c.get("stagePartnered") or []), "invest_year": c.get("partneredYear"),
        "status_site": c.get("status"), "regions": c.get("regions") or [],
        "partners": [tid[i["_ref"]]["name"].strip() for i in c.get("investors") or [] if i["_ref"] in tid],
        "founded_year": c.get("foundedYear"), "company_site": c.get("website"),
        "description": c.get("shortDescription"), "ticker": c.get("stockTicker"), "exchange": c.get("exchange"),
        "acquirer": c.get("acquiredBy"), "acquisition_date": c.get("acquisitionDate"), "location": c.get("location"),
        "legacy_url": mig.get("legacyUrl"), "wp_id": mig.get("wpId"), "cms_created": c.get("_createdAt"),
        "cms_updated": c.get("_updatedAt")})
rows.sort(key=lambda r: r["name"].lower())
out = {"_readme": "bvp.com portfolio, read 2026-10-01 from the site's Sanity dataset (project 2e9xvz8g, production) through its "
       "public query API by scratch/pull-sanity.py and flattened by scratch/shape-site.py. stage_site is the CMS "
       "stagePartnered, invest_year the CMS partneredYear, partners the CMS investors references (Bessemer team "
       "members on the deal), status_site the CMS status (active / public / acquired).", "rows": rows}
(S / "company-list.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False) + "\n")
deals = {}
for c in co:
    for i in c.get("investors") or []:
        deals.setdefault(i["_ref"], []).append(c["name"])
team = []
for t in tm:
    slug = (t.get("slug") or {}).get("current")
    role = t.get("companyRole")
    team.append({"name": t["name"].strip(), "slug": slug, "url": f"https://www.bvp.com/team/{slug}",
                 "title": (t.get("companyTitle") or "").strip(), "role": role, "is_alumni": bool(t.get("isAlumni")),
                 "is_partner": bool(t.get("partner")), "office": (t.get("location") or [None])[0],
                 "linkedin_url": t.get("linkedinUrl"), "x_url": t.get("xUrl"),
                 "deals": len(deals.get(t["_id"], [])), "deal_names": sorted(deals.get(t["_id"], [])),
                 "group": "alumni" if t.get("isAlumni") else (role or "unlisted"),
                 "bio": text(t.get("bio"))[:600]})
team.sort(key=lambda r: r["name"].lower())
(S / "team-pages.json").write_text(json.dumps(team, indent=1, ensure_ascii=False) + "\n")
from collections import Counter
print(len(rows), "companies;", len(team), "people;", Counter(t["group"] for t in team))
