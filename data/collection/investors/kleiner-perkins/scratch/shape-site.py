#!/usr/bin/env python3
"""Flatten the live WordPress `company` and `person` collections (sources/site/raw/, pulled by
pull-wp.py) into the file_list sources site-portfolio.py reads:
  sources/site/company-list.json  one row per published company page
  sources/site/team-pages.json    one row per published person page
The firm states per company: its first-investment stage (Early / Growth), a since-year, Current or
Prior (timing), the company's current stage (Early / Growth / IPO / Acquired) and, for exits, the
acquirer in since_caption."""
import html, json, re
from pathlib import Path
HERE = Path(__file__).resolve().parent
SITE = HERE.parent / "sources" / "site"
RAW = SITE / "raw"
st = {s["id"]: html.unescape(s["name"]) for s in json.load(open(RAW / "stage.json"))}
se = {s["id"]: html.unescape(s["name"]) for s in json.load(open(RAW / "sector.json"))}
roles = {s["id"]: html.unescape(s["name"]) for s in json.load(open(RAW / "person_role.json"))}
def txt(s): return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()
rows = []
for r in json.load(open(RAW / "company.json")):
    a = r.get("acf") or {}
    fi = [st.get(x.get("f_i_stage")) for x in (a.get("first_investment_stage") or []) if x.get("f_i_stage")]
    cur = [st.get(x.get("c_stage")) for x in (a.get("current_stage") or []) if x.get("c_stage")]
    rows.append({
        "name": txt(r["title"]["rendered"]),
        "url": r["link"],
        "wp_id": r["id"],
        "site_slug": r["slug"],
        "sectors": [se.get(i) for i in (r.get("sector") or []) if se.get(i)],
        "stage_site": fi[0] if len(fi) == 1 else (";".join(fi) or None),
        "current_stage": ";".join(c for c in cur if c) or None,
        "timing": a.get("timing"),
        "invest_year": (a.get("since_text") or "").strip() or None,
        "acquirer": txt(a.get("since_caption")) or None,
        "company_site": a.get("website_url") or None,
        "founders": [f.get("name") for f in (a.get("founders") or []) if f.get("name")],
        "description": txt(a.get("modal_description") or a.get("subhead") or a.get("tagline")) or None,
        "footnote": txt(a.get("footnote")) or None,
        "cms_date": r.get("date"),
    })
(SITE / "company-list.json").write_text(json.dumps({
    "_readme": "kleinerperkins.com WordPress REST (/wp-json/wp/v2/company, 416 published entries), pulled 2026-09-30 by "
               "scratch/pull-wp.py and flattened by scratch/shape-site.py. stage_site is the firm's own "
               "first_investment_stage (Early or Growth); invest_year its since_text; timing Current or Prior; "
               "current_stage the company's stage now; acquirer the since_caption on exits.",
    "rows": rows}, indent=1, ensure_ascii=False) + "\n")
team = []
for r in json.load(open(RAW / "person.json")):
    a = r.get("acf") or {}
    team.append({"name": txt(r["title"]["rendered"]), "url": r["link"], "slug": r["slug"],
                 "title": roles.get(a.get("role")), "linkedin_url": a.get("linkedin_url") or None,
                 "x_url": a.get("x_url") or None, "bio": txt(a.get("bio"))[:600] or None})
(SITE / "team-pages.json").write_text(json.dumps({
    "_readme": "kleinerperkins.com WordPress REST (/wp-json/wp/v2/person, 30 published people; role from the "
               "person_role taxonomy), pulled 2026-09-30 by scratch/pull-wp.py, flattened by scratch/shape-site.py.",
    "rows": team}, indent=1, ensure_ascii=False) + "\n")
print(len(rows), "companies;", len(team), "people")
