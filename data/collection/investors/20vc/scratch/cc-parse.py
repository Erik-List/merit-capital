#!/usr/bin/env python3
"""Parse the archived 20VC portfolio pages (Common Crawl captures of
thetwentyminutevc.com/portfolio/<slug>/, 2022-2024, under
data/filings/commoncrawl/20vc/) into sources/wayback/parsed/<year>.json in the
shape wayback-pull.py writes (slug, name, path, snapshot_ts, capture_url).

The podcast site ran a WordPress "portfolio" post type from January 2022 until
2024: one bare page per company, titled "<Name> - 20VC", posted by Nicolas
Susco (2022-01-24) or Kieran Hill (2022-08-03/05). The archive index page
renders episodes, not companies, so the list is the set of per-company pages.
The page title is the firm's own rendering and names the row (the slug does
not: "divy" is titled Noh, "fygo" Roadflex, "6262" Alloy, "6270" Sorare).
Year files MERGE, keyed slug+path (COLLECTION.md s5). A placeholder card
("Stealth") names no company and is configured out (wayback.non_company_slugs).
"""
import html, json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic, Paths  # noqa: E402
RAW = HERE.parents[4] / "data" / "filings" / "commoncrawl" / "20vc"
PARSED = HERE.parent / "sources" / "wayback" / "parsed"
PARSED.mkdir(parents=True, exist_ok=True)
man = json.loads((HERE.parent / "sources" / "wayback" / "cc-manifest.json").read_text())
skip = set(Paths("20vc").config()["wayback"]["non_company_slugs"])


def slug_of(name): return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


by_year: dict[int, dict] = {}
failed = []
for key, m in sorted(man.items()):
    if m.get("status") != "ok":
        continue
    url = m["url"]
    mm = re.search(r"/portfolio/([^/?#]+)/?$", url)
    if not mm or mm.group(1) in ("page",) or mm.group(1).isdigit() and False:
        continue
    site_slug = mm.group(1)
    t = (RAW / key).read_text(encoding="utf-8", errors="replace")
    title = html.unescape(re.sub(r"\s+", " ", (re.findall(r"<title>(.*?)</title>", t, re.S) or [""])[0])).strip()
    if not title.endswith(" - 20VC") or title.startswith("Portfolios Archive"):
        continue
    name = title[: -len(" - 20VC")].strip()
    if not name:
        failed.append(key)
        continue
    slug = slug_of(name)
    if slug in skip or site_slug in skip:
        continue
    posted = re.findall(r"Posted on ([0-9]{1,2}(?:st|nd|rd|th) \w+ \d{4}) by ([^<|]+?)(?:<|\|)", re.sub(r"<[^>]+>", "|", t))
    year = int(m["timestamp"][:4])
    row = {"slug": slug, "name": name, "site_slug": site_slug,
           "path": f"/portfolio/{site_slug}/", "snapshot_ts": m["timestamp"],
           "capture_url": m["capture_url"], "surface": f"commoncrawl:{m['crawl']}",
           "page_posted": posted[0][0] if posted else "", "page_author": posted[0][1].strip() if posted else ""}
    cur = by_year.setdefault(year, {})
    k = (slug, row["path"])
    if k not in cur or row["snapshot_ts"] < cur[k]["snapshot_ts"]:
        cur[k] = row
for year, rows in sorted(by_year.items()):
    f = PARSED / f"{year}.json"
    old = {(r["slug"], r["path"]): r for r in (json.loads(f.read_text()) if f.exists() else [])}
    old.update(rows)
    write_atomic(f, json.dumps(sorted(old.values(), key=lambda r: r["slug"]), indent=1, ensure_ascii=False) + "\n")
    print(year, len(old), "rows")
print("failed:", failed)
