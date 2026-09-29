#!/usr/bin/env python3
"""Flatten the Sanity pull (sources/site/sanity/*.json) into the file_list sources
the pipeline reads: sources/site/company-list.json, team-pages.json and
news-text.json.

gv.com publishes two company lists from one dataset:
  /portfolio  646 `company` docs: name (an exited company carries a trailing
              " *"), sector and secondary sector, website, the deal partners
              (`investors`, refs to teamMember docs), the firm's own exit line
              (`acquiredBy`: "Acquired by Nebius, 2026", "NASDAQ: SNCE") and a
              `moreInfo` link (usually the acquisition announcement).
  /ai         112 `aiCompany` docs: name, website, category and the firm's own
              dated rounds ("Invested" / "Re-invested", month and year).
The union is one row per company: an /ai doc joins its /portfolio doc on the
website domain, else on the normalised name; the 10 /ai companies with no
/portfolio doc are rows of their own.

The /ai "Invested" date is the firm's own statement of when it first invested:
an anchor for first_seen and entry_date, never a stage label (COLLECTION.md 6,
"a bare year is an anchor, not a label"; decisions.md D7).
"""
import collections
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402

SITE = HERE.parent / "sources" / "site"
SAN = SITE / "sanity"
BASE = "https://www.gv.com"
PORTFOLIO = f"{BASE}/portfolio"
AI = f"{BASE}/ai"


def rows(name):
    return json.loads((SAN / name).read_text())["rows"]


def dom(u):
    if not u:
        return ""
    if not u.startswith("http"):
        u = "https://" + u
    d = urlparse(u).netloc.lower()
    return d.removeprefix("www.")


def norm(n):
    n = n.replace("*", "").strip().lower()
    n = re.sub(r"\b(inc|labs|ai|the|co|corp|ltd|llc|health|technologies|therapeutics)\b", "", n)
    return re.sub(r"[^a-z0-9]", "", n)


team = rows("teamMember.json")
people = {t["_id"]: (t.get("fullName") or "").replace("&nbsp;", " ").strip() for t in team}

companies = rows("company.json")
ai_docs = rows("aiCompany.json")

out = []
by_dom, by_name = {}, {}
dangling = collections.Counter()
for d in companies:
    raw = d.get("name") or ""
    exited = "*" in raw
    name = raw.replace("*", "").strip()
    refs = d.get("investor_refs") or []
    names = [people.get(r) for r in refs]
    dangling.update(r for r, n in zip(refs, names) if not n)
    exit_line = d.get("acquiredBy") if isinstance(d.get("acquiredBy"), str) else ""
    row = {
        "name": name,
        "id": d["_id"],
        "url": PORTFOLIO,
        "gv_lists": ["portfolio"],
        "sector": d.get("sector_title") or "",
        "secondary_sector": d.get("secondary_sector_title") or "",
        "sectors": [s for s in (d.get("sector_title"), d.get("secondary_sector_title")) if s],
        "company_site": d.get("website") or "",
        "partners": [n for n in names if n],
        "partner_refs_unresolved": sum(1 for n in names if not n),
        "exited": exited,
        "exit_line": exit_line.strip(),
        "more_info": d.get("moreInfo") if isinstance(d.get("moreInfo"), str) else "",
        "cms_created": d.get("_createdAt") or "",
        "contentful_archived": bool(d.get("contentfulArchived")),
        "ai_category": "",
        "ai_rounds": [],
        "ai_first_invested": "",
        "invest_year": "",
    }
    out.append(row)
    if dom(row["company_site"]):
        by_dom.setdefault(dom(row["company_site"]), row)
    by_name.setdefault(norm(name), row)

ai_only = 0
for d in ai_docs:
    rounds = sorted(({"type": r.get("investment_type"), "year": r.get("year"), "month": r.get("month")}
                     for r in d.get("rounds") or [] if r.get("year")),
                    key=lambda r: (r["year"], r["month"] or 0))
    inv = [r for r in rounds if r["type"] == "Invested"] or rounds
    first = f'{inv[0]["year"]}-{inv[0]["month"]:02d}' if inv and inv[0].get("month") else (str(inv[0]["year"]) if inv else "")
    tgt = by_dom.get(dom(d.get("website"))) or by_name.get(norm(d.get("name") or ""))
    if tgt is None:
        ai_only += 1
        tgt = {"name": (d.get("name") or "").strip(), "id": d["_id"], "url": AI, "gv_lists": [],
               "sector": "AI", "secondary_sector": "", "sectors": ["AI"],
               "company_site": d.get("website") or "", "partners": [], "partner_refs_unresolved": 0,
               "exited": False, "exit_line": "", "more_info": "", "cms_created": d.get("_createdAt") or "",
               "contentful_archived": False, "ai_category": "", "ai_rounds": [], "ai_first_invested": "",
               "invest_year": ""}
        out.append(tgt)
    tgt["gv_lists"].append("ai")
    tgt["ai_category"] = d.get("category") or ""
    tgt["ai_rounds"] = rounds
    tgt["ai_first_invested"] = first
    tgt["invest_year"] = first[:4]
    tgt["ai_id"] = d["_id"]

# Two docs sharing one display name would fold into one base row (the base keys rows by name):
# the second takes its domain in brackets (the shared-names rule, Erik 2026-09-24).
n = collections.Counter(r["name"].lower() for r in out)
seen = collections.Counter()
for r in out:
    k = r["name"].lower()
    if n[k] > 1:
        seen[k] += 1
        if seen[k] > 1 and dom(r["company_site"]):
            r["name"] = f'{r["name"]} ({dom(r["company_site"])})'
out.sort(key=lambda r: r["name"].lower())
write_atomic(SITE / "company-list.json", json.dumps({
    "_readme": "Flattened by scratch/shape-site.py from sources/site/sanity/company.json (the /portfolio "
               "list, 646 docs) and aiCompany.json (the /ai list, 112 docs), joined on website domain then "
               "normalised name. exited = the trailing ' *' the firm puts on exited companies; exit_line is "
               "the firm's own acquiredBy text; partners are the teamMember docs the CMS links as the deal "
               "partners (refs to people no longer on the team do not resolve and are counted in "
               "partner_refs_unresolved); ai_first_invested is the firm's own first 'Invested' month on /ai.",
    "rows": out}, indent=1, ensure_ascii=False) + "\n")

# ---- team: the investing team, operations and advisors, with the CMS group as the bucket key
tout = []
for t in team:
    slug = (t.get("slug") or {}).get("current") if isinstance(t.get("slug"), dict) else t.get("slug")
    grp = "; ".join(t.get("team") or []) if isinstance(t.get("team"), list) else (t.get("team") or "")
    # 43 staff carry no CMS group (executive business partners, finance, legal, engineering). An explicit
    # unmapped label keeps them out of the profile; without it site-portfolio.py falls back to title rules,
    # which read "Executive Business Partner" as an investing title.
    grp = grp or "Staff (no CMS group)"
    tout.append({"name": people[t["_id"]], "slug": slug or "", "url": f"{BASE}/team/{slug}" if slug else "",
                 "title": (t.get("jobTitle") or "").strip(), "group": grp,
                 "location": t.get("investorsLocation") or "",
                 "linkedin_url": t.get("linkedin") or "", "x_url": t.get("twitter") or "",
                 "sectors": t.get("sector_titles") or [],
                 "bio": (t.get("bio_text") or "").strip(),
                 "deal_count": sum(1 for r in out if people[t["_id"]] in r["partners"])})
tout.sort(key=lambda r: r["name"].lower())
write_atomic(SITE / "team-pages.json", json.dumps({
    "_readme": "Flattened by scratch/shape-site.py from sources/site/sanity/teamMember.json (109 docs; the "
               "CMS `team` group is Investing Team, Operations or Advisors, and 43 staff carry none). "
               "deal_count = /portfolio docs that link the person as a deal partner.",
    "rows": tout}, indent=1, ensure_ascii=False) + "\n")

# ---- the firm's own posts, as plain text, for the judge (POST() citations)
nout = []
for a in rows("newsArticle.json"):
    slug = (a.get("slug") or {}).get("current") if isinstance(a.get("slug"), dict) else a.get("slug")
    nout.append({"slug": slug, "url": f"{BASE}/news/{slug}", "date": (a.get("date") or "")[:10],
                 "title": a.get("title") or "", "subheading": a.get("subHeading") or "",
                 "authors": a.get("author_names") or [],
                 "body": ((a.get("meta_text") or "") + "\n" + (a.get("body_text") or "")).strip()})
nout.sort(key=lambda r: r["date"])
write_atomic(SITE / "news-text.json", json.dumps({
    "_readme": "The firm's own posts (sources/site/sanity/newsArticle.json), plain text, by date.",
    "rows": nout}, indent=1, ensure_ascii=False) + "\n")

print(len(out), "company rows;", ai_only, "only on /ai;", len(tout), "people;", len(nout), "posts")
print("unresolved partner refs:", sum(dangling.values()), "refs to", len(dangling), "people")
print(collections.Counter(r["group"] for r in tout))
print(collections.Counter(p for r in out for p in r["partners"]).most_common(40))
print("rows with partners:", sum(1 for r in out if r["partners"]), " exited:", sum(r["exited"] for r in out))
