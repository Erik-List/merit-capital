#!/usr/bin/env python3
"""Flatten NEA's Statamic pull into the file_list sources site-portfolio.py reads.

  sources/site/company-list.json  one row per published portfolio entry
  sources/site/team-pages.json    one row per team entry (published and draft,
                                  the drafts marked; only published rows are the
                                  live team, drafts are departed people)

Every field is the firm's own: the name as rendered, the first-invested year,
the stage label (carried as `stage_site`; whether it labels a row is scored
before it is declared in site_api.entry_stage_fields), the status and exit line,
the deal team and board members (NEA people, joined as `partners`), and the
firm's category and theme tags.
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parents[3] / "scripts"))
from paths import write_atomic  # noqa: E402

ST = ROOT / "sources" / "site" / "statamic"
BASE = "https://www.nea.com"
SUFFIX = re.compile(r",\s*(MD|PhD|Ph\.D\.|MBA|JD|DVM|MPH|PharmD)\b.*$", re.I)


def person(name: str) -> str:
    return SUFFIX.sub("", html.unescape(name or "")).strip()


def text(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html.unescape(s or ""))).strip()


def lab(v):
    return (v or {}).get("label") or ""


def companies():
    rows = json.load(open(ST / "portfolio.json"))["rows"]
    out = []
    for r in sorted(rows, key=lambda r: r["title"].lower()):
        cats = [c["title"] for c in (r.get("company_category") or [])]
        themes = [t for t in [lab(r.get("theme"))] + [lab(t) for t in (r.get("additional_theme") or [])]
                  if t and t != "Unset"]
        deal = [person(p["title"]) for p in (r.get("team") or [])]
        board = [person(p["title"]) for p in (r.get("board_members") or [])]
        obs = [person(p["title"]) for p in (r.get("board_member_observer") or [])]
        out.append({
            "name": html.unescape(r["title"]).strip(),
            "url": BASE + r["url"],
            "statamic_id": r["id"],
            "site_slug": r["slug"],
            "sectors": cats + themes,
            "categories": cats,
            "themes": themes,
            "partners": list(dict.fromkeys(deal + board + obs)),
            "deal_team": deal,
            "board_members": board,
            "board_observers": obs,
            "invest_year": r.get("first_invested") or "",
            "stage_site": lab(r.get("company_stage")),
            "status_site": lab(r.get("company_status_value")),
            "exit_line": " ".join(x for x in (r.get("company_status"), r.get("company_status_line_two")) if x),
            "investment_type": lab(r.get("investment_type")),
            "force_current": bool(r.get("force_current")),
            "company_site": r.get("external_url") or "",
            "description": text(r.get("short_description") or r.get("description")),
            "cms_date": r.get("date") or "",
        })
    return out


def team():
    out = []
    for fn, published in (("team.json", True), ("team-draft.json", False)):
        for r in json.load(open(ST / fn))["rows"]:
            units = [u["title"] for u in (r.get("team_unit") or [])] if isinstance(r.get("team_unit"), list) \
                else ([r["team_unit"]["title"]] if r.get("team_unit") else [])
            out.append({
                "name": person(r["title"]),
                "cms_name": r["title"],
                "slug": r["slug"],
                "url": BASE + (r.get("url") or f"/team/{r['slug']}"),
                "title": r.get("job_title") or "",
                # A draft is an unpublished (departed) person: kept as roster evidence, never
                # as the live team, so its group is one no bucket maps and no roster filter keeps.
                "group": (units[0] if units else "") if published else "Former",
                "units": units,
                "published": published,
                "linkedin_url": r.get("linkedin_url") or "",
                "x_url": r.get("twitter_url") or "",
                "cms_date": r.get("date") or "",
            })
    return out


def main():
    c = companies()
    write_atomic(ROOT / "sources" / "site" / "company-list.json", json.dumps({
        "_readme": "NEA's published portfolio (917 Statamic portfolio entries, statamic.nea.com/graphql, "
                   "pulled by scratch/pull-statamic.py), flattened by scratch/shape-site.py. Drafts are not "
                   "listings and are not here (sources/site/statamic/portfolio-draft.json).",
        "rows": c}, indent=1, ensure_ascii=False))
    t = team()
    write_atomic(ROOT / "sources" / "site" / "team-pages.json", json.dumps({
        "_readme": "NEA's team collection: published entries are the live team; draft entries are unpublished "
                   "(departed) people, kept as roster evidence without dates.",
        "rows": t}, indent=1, ensure_ascii=False))
    print(len(c), "companies;", len(t), "team rows (", sum(x["published"] for x in t), "published )")


if __name__ == "__main__":
    main()
