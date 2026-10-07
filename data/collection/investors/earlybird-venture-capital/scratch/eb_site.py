#!/usr/bin/env python3
"""Read earlybird.com (Framer) into sources/site/companies-2026.json and team-2026.json.

The site is a Framer build: no REST endpoint, the list page ships every row
as an anchor (`./companies/<slug>`: name, optional "Spotlights", status,
stage, location, sector tags) and Framer's own search index
(`<meta name="framer-search-index">`, one JSON for the whole site) carries the
text of every company page: description, "Founded: Y / Invested: Y", founders,
HQ, the investment team, and the firm's own "Digital East Fund*" marker with
its disclaimer. Escalation ladder step 5 (COLLECTION.md s5): parse what the
page ships. Raw inputs are kept under sources/site/raw/ so the parse is
reproducible offline:  python3 scratch/eb_site.py [--fetch]
"""
from __future__ import annotations

import html
import json
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "sources/site/raw"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
READ = time.strftime("%Y-%m-%d")

NAV = {"EARLYBIRD", "EARLYBIRD HEALTH", "Back to companies", "THE PORTFOLIO",
       "OUR PORTFOLIO",
       "Meet the companies creating groundbreaking change.",
       "Meet the companies we\u2019ve backed on their way to creating groundbreaking change.",
       "Company", "Spotlight", "Status", "Stage", "Location"}
SITES = {
    "main": {"site": "https://earlybird.com", "raw": "", "out": "companies-2026.json",
             "label": "earlybird.com"},
    "health": {"site": "https://health.earlybird.com", "raw": "health",
               "out": "health-2026.json", "label": "health.earlybird.com"},
}
STAGES = {"Pre-Seed", "Seed", "Series A", "Series B", "Series C", "Growth",
          "Late Stage", "Series D"}
STATUSES = {"Active", "Exit", "IPO", "Acquired", "Public"}


def curl(url: str, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["curl", "-sL", "-A", UA, "-o", str(dst), url], check=True)
    time.sleep(0.4)


def fetch(SITE: str, RAW: Path) -> None:
    curl(f"{SITE}/sitemap.xml", RAW / "sitemap.xml")
    curl(f"{SITE}/companies", RAW / "companies.html")
    curl(f"{SITE}/members", RAW / "members.html")
    home = RAW / "home.html"
    curl(f"{SITE}/", home)
    m = re.search(r'framer-search-index" content="([^"]+)', home.read_text())
    if not m:
        sys.exit("no framer-search-index meta on the homepage")
    curl(m.group(1), RAW / "searchIndex.json")
    (RAW / "searchIndex.url").write_text(m.group(1) + "\n")


def list_rows(RAW: Path) -> dict[str, dict]:
    s = (RAW / "companies.html").read_text()
    rows: dict[str, dict] = {}
    for slug, inner in re.findall(
            r'<a[^>]+href="\./companies/([^"]+)"[^>]*>(.*?)</a>', s, flags=re.S):
        parts = [p.strip() for p in html.unescape(
            re.sub(r"<[^>]+>", "|", inner)).split("|") if p.strip()]
        if not parts or slug in rows:
            continue
        row = {"name": parts[0], "spotlight": False, "status_site": None,
               "stage_site": None, "location_list": None, "categories": []}
        rest = parts[1:]
        if rest and rest[0] == "Spotlights":
            row["spotlight"] = True
            rest = rest[1:]
        if rest and rest[0] in STATUSES:
            row["status_site"] = rest.pop(0)
        if rest and rest[0] in STAGES:
            row["stage_site"] = rest.pop(0)
        if rest:
            row["location_list"] = rest.pop(0)
        row["categories"] = rest
        rows[slug] = row
    return rows


def detail(page: dict) -> dict:
    ps = [p for p in page["p"] if p not in NAV]
    out: dict = {"description": None, "founded": None, "invest_year": None,
                 "founders": [], "hq_site": None, "partners_site": [],
                 "fund_marker": None}
    i = next((k for k, p in enumerate(ps) if p in ("The company", "PORTFOLIO")), None)
    if i is None:
        return out
    body = ps[i + 1:]
    stop = next((k for k, p in enumerate(body) if p.startswith(
        "Got an idea that could change the world")), len(body))
    body = body[:stop]
    desc, k = [], 0
    while k < len(body) and body[k] != "Milestones":
        desc.append(body[k])
        k += 1
    out["description"] = " ".join(desc).strip() or None
    section = None
    for p in body[k:]:
        if p == "Milestones":
            section = "milestones"
            continue
        if p in ("Founders", "Founder", "Leadership Team"):
            section = "founders"
            continue
        if p == "HQ":
            section = "hq"
            continue
        if p in ("Investment Team", "Earlybird Deal Team"):
            section = "team"
            continue
        if p.endswith("Fund*"):
            out["fund_marker"] = p.rstrip("*").strip()
            continue
        if section == "milestones":
            m = re.search(r"Founded:\s*(\d{4})", p)
            if m:
                out["founded"] = int(m.group(1))
            m = re.search(r"Invested:\s*(\d{4})", p)
            if m:
                out["invest_year"] = int(m.group(1))
            m = re.search(r"Exit(?:ed)?:\s*(\d{4})", p)
            if m:
                out["exit_year"] = int(m.group(1))
            out.setdefault("milestones_raw", p)
        elif section == "founders":
            out["founders"].extend(x.strip() for x in p.split("\n") if x.strip())
        elif section == "hq":
            out["hq_site"] = p
        elif section == "team":
            out["partners_site"].extend(x.strip() for x in p.split("\n") if x.strip())
    return out


def run(key: str, do_fetch: bool) -> None:
    cfg = SITES[key]
    SITE, raw = cfg["site"], (RAW / cfg["raw"] if cfg["raw"] else RAW)
    if do_fetch or not (raw / "searchIndex.json").exists():
        fetch(SITE, raw)
    idx = json.loads((raw / "searchIndex.json").read_text())
    sitemap = re.findall(r"<loc>([^<]+)", (raw / "sitemap.xml").read_text())
    slugs = [u.rsplit("/companies/", 1)[1] for u in sitemap if "/companies/" in u]
    listed = list_rows(raw)
    from urllib.parse import unquote
    idx = {unquote(k): v for k, v in idx.items()}
    slugs = [unquote(x) for x in slugs]
    listed = {unquote(k): v for k, v in listed.items()}
    index_slugs = [k.split("/companies/", 1)[1] for k in idx if k.startswith("/companies/")]
    rows = []
    for slug in sorted(set(slugs) | set(listed) | set(index_slugs)):
        page = idx.get(f"/companies/{slug}")
        row = {"slug_site": slug, "url": f"{SITE}/companies/{slug}",
               "in_sitemap": slug in slugs, "on_list_page": slug in listed,
               "surface": cfg["label"]}
        row.update(listed.get(slug, {}))
        if page:
            row.update(detail(page))
            if not row.get("name"):
                row["name"] = page["h1"][-1]
            row["name_page"] = page["h1"][-1]
        else:
            row["no_search_index_entry"] = True
        row["digital_east"] = row.get("fund_marker") == "Digital East Fund"
        rows.append(row)
    disclaimer = next((p for page in idx.values() for p in page["p"]
                       if "investment decision for this company" in p), None)
    out = {
        "_readme": (
            "%s read %s by scratch/eb_site.py: the Framer list page "
            "(/companies anchors: name, Spotlights, status, stage, location, "
            "sector tags) joined on slug with Framer's search index "
            "(description, Founded / Invested years, founders, HQ, investment "
            "team, the 'Digital East Fund*' marker). Raw inputs under "
            "sources/site/raw/." % (cfg["label"], READ)),
        "read": READ,
        "digital_east_disclaimer": disclaimer,
        "rows": rows,
    }
    dst = ROOT / "sources/site" / cfg["out"]
    dst.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(f"{len(rows)} rows -> {dst.relative_to(ROOT)}")
    print("  on list page:", sum(r["on_list_page"] for r in rows),
          "| in sitemap:", sum(r["in_sitemap"] for r in rows),
          "| digital east:", sum(r["digital_east"] for r in rows),
          "| no index entry:", sum(bool(r.get("no_search_index_entry")) for r in rows))


def main() -> None:
    for key in SITES:
        run(key, "--fetch" in sys.argv)


if __name__ == "__main__":
    main()


# ---- team (appended 2026-10-06): the members list page of both sites ----
GROUPS = {"Investment Team", "Venture Partners", "Investor Relations", "Operations",
          "Team", "Partners", "Advisors", "Venture Partner", "Health Team"}
OFFICES = {"Berlin", "Munich", "London", "Milan", "Cologne", "CEE", "Dublin", "Paris", "Lausanne"}


def team(key: str) -> list[dict]:
    from urllib.parse import unquote
    cfg = SITES[key]
    raw = RAW / cfg["raw"] if cfg["raw"] else RAW
    s = (raw / "members.html").read_text()
    idx = {unquote(k): v for k, v in json.loads((raw / "searchIndex.json").read_text()).items()}
    rows, seen = [], set()
    for slug, inner in re.findall(
            r'<a[^>]+href="\./members/([^"]+)"[^>]*>(.*?)</a>', s, flags=re.S):
        slug = unquote(slug)
        if slug in seen:
            continue
        seen.add(slug)
        parts = [p.strip() for p in html.unescape(
            re.sub(r"<[^>]+>", "|", inner)).split("|") if p.strip()]
        if len(parts) < 2:
            continue
        page = idx.get(f"/members/{slug}")
        import unicodedata
        name = unicodedata.normalize("NFC", page["h1"][-1] if page else parts[-2])
        parts = [unicodedata.normalize("NFC", x) for x in parts]
        title = parts[-1] if parts[-1] != name else None
        groups = [p for p in parts if p in GROUPS]
        offices = [p for p in parts if p in OFFICES]
        tags = [p for p in parts if p not in GROUPS and p not in OFFICES
                and p not in (name, title)]
        rows.append({"name": name, "slug": slug,
                     "url": f"{cfg['site']}/members/{slug}",
                     "title": title, "group": groups[0] if groups else None,
                     "groups_all": groups, "location": offices[0] if offices else None,
                     "focus_tags": tags, "surface": cfg["label"]})
    return rows


def write_team() -> None:
    for key, out in (("main", "team-2026.json"), ("health", "team-health-2026.json")):
        rows = team(key)
        dst = ROOT / "sources/site" / out
        dst.write_text(json.dumps({
            "_readme": "%s/members read %s by scratch/eb_site.py: one card per person "
                       "(group, office, focus tags, name, title)." % (SITES[key]["label"], READ),
            "rows": rows}, indent=1, ensure_ascii=False) + "\n")
        print(f"{len(rows)} people -> {dst.relative_to(ROOT)}")


if __name__ == "__main__":
    write_team()
