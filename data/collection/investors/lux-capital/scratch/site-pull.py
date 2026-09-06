#!/usr/bin/env python3
"""Pull luxcapital.com's Webflow surfaces into the run's file_list sources.

The sitemap enumerates every /companies/<slug>, /people/<slug> and
/advisors/<slug> page; each company page server-renders the firm's own
description, its industries taxonomy, a Milestones block whose first line is
"Lux investment: <year>" (the firm's own entry year -- verified against three
known deals before it feeds first_seen, COLLECTION.md §5), the founders and
the comma-joined slugs of the Lux people who own the relationship (the
per-deal partner attribution the judge uses to resolve Form D clusters).

Writes sources/site/webflow-companies.json and team-webflow.json.
"""
import json
import re
import subprocess
import sys
import time
from html import unescape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
BASE = "https://www.luxcapital.com"


def get(url: str, dest: Path) -> str:
    if dest.exists():
        return dest.read_text(encoding="utf-8", errors="replace")
    for attempt in range(3):
        try:
            out = subprocess.run(
                ["curl", "-sfL", "--compressed", "--max-time", "60",
                 "-H", f"User-Agent: {UA}", url],
                capture_output=True, check=True).stdout.decode("utf-8", errors="replace")
            write_atomic(dest, out)
            time.sleep(0.25)
            return out
        except subprocess.CalledProcessError:
            time.sleep(2)
    return ""


def texts(block: str) -> list[str]:
    return [unescape(re.sub(r"<[^>]+>", "", p)).replace("‍", "").strip()
            for p in re.findall(r"<p[^>]*>(.*?)</p>", block, re.S)]


def detail_items(html: str) -> dict:
    """The company-details_item label -> its <p> values."""
    out = {}
    for m in re.finditer(
            r'class="company-details_item".*?class="text-style-mono-caps[^"]*">'
            r'([^<]+)</div>.*?class="company-details_text[^"]*">(.*?)</div>',
            html, re.S):
        label = unescape(m.group(1)).strip().lower()
        out[label] = [t for t in texts(m.group(2)) if t]
    return out


def parse_company(slug: str, html: str) -> dict:
    """The page's own record only.

    A company page renders the detail block and <h1> first, then a
    "Similar companies" collection whose cards carry the same
    company_embed-slug / company_partner-slugs / details markup as the main
    record — so a document-wide regex reads a neighbour's fields (30 rows
    published Auris Health's "Acquired by J&J" before this was caught). The
    main record is everything above section_related; the partner slugs are
    taken from the card whose embedded slug is this page's own.
    """
    cut = html.find('class="section_related"')
    main = html[:cut] if cut > 0 else html
    name = re.search(r'<h1 class="company-detail_title">([^<]*)</h1>', main)
    cats = re.findall(r'fs-cmsfilter-field="category">([^<]+)</div>', main)
    blurb = ""
    m = re.search(r'class="company-detail_text[^"]*"[^>]*>(.*?)</div>', main, re.S)
    if not m:
        m = re.search(r'class="text-rich-text w-richtext">(.*?)</div>', main, re.S)
    if m:
        ps = [t for t in texts(m.group(1))
              if t and "Lorem" not in t and "consectetur" not in t]
        blurb = ps[0] if ps else ""
    site = ""
    for href in re.findall(r'<a href="(https?://[^"]+)"[^>]*class="button_component[^"]*"', main):
        if "luxcapital.com" not in href:
            site = href
            break
    # partner attribution: the card whose own embed slug is this page's
    partners = []
    for card in re.findall(r'(?s)company_embed-slug w-embed"><input[^>]*value="([^"]*)"'
                           r'(.{0,3000}?)company_partner-slugs">([^<]*)<', html):
        if card[0].strip() == slug:
            partners = [x.strip() for x in card[2].split(",") if x.strip()]
            break
    d = detail_items(main)
    ms = [x.replace("\xa0", " ") for x in d.get("milestones", [])]
    year = founded = None
    exits = []
    for line in ms:
        y = re.search(r"Lux investment:\s*(\d{4})", line, re.I)
        if y:
            year = int(y.group(1))
            continue
        f = re.search(r"Lux founded:\s*(\d{4})", line, re.I)
        if f:
            founded = int(f.group(1))
            continue
        if re.match(r"\s*(Acquired|IPO|Publicly listed|Merged|Shut down|Closed)", line, re.I):
            exits.append(line.strip())
    return {
        "slug": slug,
        "name": unescape(name.group(1)).strip() if name else None,
        "url": site or None,
        "description": blurb or None,
        "sectors_site": sorted({c.strip() for c in cats if c.strip()}) or
                        list(d.get("industries", [])),
        "lux_investment_year": year,
        "lux_founded_year": founded,
        "exit_milestones": exits,
        "milestones": ms,
        "founders": d.get("founders", []),
        "team_slugs": partners,
    }


def main():
    p = Paths("lux-capital")
    raw = p.scratch / "site-raw"
    raw.mkdir(parents=True, exist_ok=True)
    sm = get(f"{BASE}/sitemap.xml", raw / "sitemap.xml")
    urls = re.findall(r"<loc>([^<]+)</loc>", sm)
    comp = [u for u in urls if "/companies/" in u]
    people = [u for u in urls if "/people/" in u or "/advisors/" in u]
    print(f"sitemap: {len(comp)} companies, {len(people)} people")

    rows = []
    for i, u in enumerate(comp, 1):
        slug = u.rstrip("/").rsplit("/", 1)[-1]
        html = get(u, raw / f"company-{slug}.html")
        if not html:
            print(f"  MISS {slug}")
            continue
        rows.append(parse_company(slug, html))
        if i % 40 == 0:
            print(f"  {i}/{len(comp)}")
    write_atomic(p.site / "webflow-companies.json",
                 json.dumps({"_readme": "luxcapital.com Webflow company pages, "
                             "enumerated from sitemap.xml and parsed by "
                             "scratch/site-pull.py", "rows": rows}, indent=1))
    print(f"companies: {len(rows)} rows, "
          f"{sum(1 for r in rows if r['lux_investment_year'])} with a Lux investment year, "
          f"{sum(1 for r in rows if r['team_slugs'])} with partner attribution")

    team = []
    for u in people:
        slug = u.rstrip("/").rsplit("/", 1)[-1]
        html = get(u, raw / f"person-{slug}.html")
        if not html:
            continue
        nm = re.search(r'<h1[^>]*>([^<]*)</h1>', html)
        title = re.search(r'class="[^"]*person[^"]*title[^"]*"[^>]*>([^<]*)<', html, re.I)
        team.append({"slug": slug, "name": unescape(nm.group(1)).strip() if nm else
                     slug.replace("-", " ").title(),
                     "title": unescape(title.group(1)).strip() if title else None,
                     "group": "advisor" if "/advisors/" in u else "team",
                     "url": u})
    write_atomic(p.site / "team-webflow.json",
                 json.dumps({"_readme": "luxcapital.com /people and /advisors pages",
                             "rows": team}, indent=1))
    print(f"team: {len(team)} people")


if __name__ == "__main__":
    main()
