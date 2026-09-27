#!/usr/bin/env python3
"""Eras 1 and 2 of the firm's archived site, read into the shape
wayback-pull.py writes (sources/wayback/parsed/<year>.json, rows keyed
slug+path, merged rather than replaced).

  era 1 (2000): portfolio_list.asp, 'AN ALPHABETICAL LISTING': one <p><B>Name</B>
                per company with its chief executive, site and a sentence.
  era 2 (2006 to 2008): one page per company, portfolio_<name>.php, enumerated
                from the CDX index (scratch/cdx/*.json).
Raw pages are under scratch/wayback-old/. Usage: python3 .../scratch/wayback-old-eras.py"""
import json, re, html, sys
from pathlib import Path
INV = Path(__file__).resolve().parents[1]
ROOT = INV.parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import write_atomic  # noqa: E402
PARSED = INV / "sources/wayback/parsed"
PARSED.mkdir(parents=True, exist_ok=True)


def slug_of(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def merge(year, rows):
    p = PARSED / f"{year}.json"
    old = json.loads(p.read_text()) if p.exists() else []
    seen = {(r["slug"], r.get("path")) for r in old}
    add = [r for r in rows if (r["slug"], r.get("path")) not in seen]
    write_atomic(p, json.dumps(sorted(old + add, key=lambda r: r["slug"]), indent=1, ensure_ascii=False))
    print(year, "+", len(add), "rows, file holds", len(old) + len(add))


# era 1
ts = "20000407122555"
t = (INV / "scratch/wayback-old/20000407_portfolio_list.asp.html").read_text(encoding="latin-1")
body = t[t.find("AN ALPHABETICAL LISTING"):]
rows = []
for m in re.finditer(r"(?is)<p>\s*<B>(.*?)</B>(.*?)(?=<p>\s*<B>|</td>|$)", body):
    name = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", m.group(1)))).strip()
    rest = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", m.group(2)))).strip()
    if not name or len(name) > 70:
        continue
    site = re.search(r'(?i)href="(http[^"]+)"', m.group(2))
    rows.append({"slug": slug_of(name), "name": name, "path": "/portfolio_list.asp", "snapshot_ts": ts,
                 "capture_url": f"https://web.archive.org/web/{ts}/http://www.insightpartners.com:80/portfolio_list.asp",
                 "site": site.group(1) if site else None, "description": rest[:400]})
merge(2000, rows)
for r in rows:
    print("   ", r["name"], "|", (r["description"] or "")[:90])

# era 2
cdx = json.load(open(INV / "scratch/cdx/all-to-2012.json")) + json.load(open(INV / "scratch/cdx/portfolio-pages.json"))
by_year = {}
for r in cdx:
    m = re.search(r"/portfolio_([a-z0-9_]+)\.php", r[1], re.I)
    if not m or m.group(1).lower() in ("frame", "list"):
        continue
    y = int(r[0][:4])
    by_year.setdefault(y, {})[m.group(1).lower()] = {
        "slug": m.group(1).lower().replace("_", "-"), "path": f"/portfolio_{m.group(1).lower()}.php", "snapshot_ts": r[0],
        "capture_url": f"https://web.archive.org/web/{r[0]}/{r[1]}"}
for y, d in sorted(by_year.items()):
    merge(y, list(d.values()))
    print("   ", y, sorted(d))
