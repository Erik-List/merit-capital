#!/usr/bin/env python3
"""Atomico's archived listing eras, written from evidence already on disk.

The Internet Archive refused this machine for most of 2026-09-26 (two
machine-wide cooldowns), but the CDX index of atomico.com had been read in full
at kickoff (scratch-pad cdx-domain.txt / cdx-p-z.txt: every captured URL with
its FIRST capture timestamp, collapse=urlkey) and one listing capture per
early era had been fetched. That is exactly the evidence wayback-pull.py's
`cdx_company_pages` and `listing_regex` parsers produce, so this writes the
same per-year shape into sources/wayback/parsed/<year>.json. wayback-pull.py
MERGES into these files (keyed slug+path, existing rows win), so a later
archive run adds years rather than replacing anything.

Per-company page eras (first capture year of each page):
  /portfolios/atomico-ventures-i/<slug>  2011-2012 (fund I, the founders' capital)
  /portfolios/atomico-ii/<slug>          2011-2012 (fund II)
  /portfolio/<slug>                      2012-2019
  /partnerships/<slug>                   2018-2021
  /investments/<slug>                    2019-2021
  /partners/<slug>                       2021-2026
  /ourportfolio/<slug>.xml               2008
Listing captures with names (raw kept under sources/wayback/raw/):
  2008 /portfolio.php, 2010 /portfolio_companies.php (fund II),
  2010 /portfolio_atomicoi.php (fund I), 2011 /portfolios, 2012 /portfolio
"""
from __future__ import annotations

import json
import re
import shutil
import sys
from html import unescape
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

P = Paths("atomico")
SP = Path("/private/tmp/claude-501/-Users-erik-Developer-merit-capital/"
          "7d8e9a00-bfd0-4e09-8d4e-1b30f898d60e/scratchpad/atomico")
CFG = P.config()["wayback"]
NON = set(CFG["non_company_slugs"])

ERAS = [  # (url-key regex, path prefix, from, to)
    (r"^com,atomico\)/portfolios/atomico-ventures-i/([a-z0-9.-]+)$", "/portfolios/atomico-ventures-i", 2011, 2012),
    (r"^com,atomico\)/portfolios/atomico-ii/([a-z0-9.-]+)$", "/portfolios/atomico-ii", 2011, 2012),
    (r"^com,atomico\)/portfolio/([a-z0-9.%-]+)$", "/portfolio", 2012, 2019),
    (r"^com,atomico\)/partnerships/([a-z0-9-]+)$", "/partnerships", 2018, 2021),
    (r"^com,atomico\)/investments/([a-z0-9-]+)$", "/investments", 2019, 2021),
    (r"^com,atomico\)/partners/([a-z0-9-]+)$", "/partners", 2021, 2026),
    (r"^com,atomico\)/ourportfolio/([a-z0-9]+)\.xml$", "/ourportfolio", 2008, 2008),
]
LISTINGS = [  # (sample file, era path, capture timestamp, regex with name/slug)
    ("2008-portfolio.php", "/portfolio.php", "20080919090920",
     r'href="portfolio\.php\?port_id=\d+"[^>]*>(?P<name>[^<]+)</a>'),
    ("2010-portfolio_companies.php", "/portfolio_companies.php", "20100405170556",
     r'href="portfolio_companies\.php\?port_id=\d+"[^>]*>(?P<name>[^<]+)</a>'),
    ("2010-portfolio_atomicoi.php", "/portfolio_atomicoi.php", "20100325073919",
     r'href="portfolio_atomicoIcompanies\.php\?port_id=\d+"[^>]*>(?P<name>[^<]+)</a>'),
    ("2011-portfolios.html", "/portfolios", "20110223094959",
     r'href="http://www\.atomico\.com/portfolios/atomico-(?:ii|ventures-i)/(?P<slug>[a-z0-9.-]+)/"[^>]*>(?P<name>[^<]+)</a>'),
    ("2012-portfolio.html", "/portfolio", "20120831180330",
     r'href="http://www\.atomico\.com/portfolio/(?P<slug>[a-z0-9.-]+)"[^>]*>(?P<name>[^<]+)</a>'),
]


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def main():
    years: dict[int, dict] = {}
    lines = []
    for f in ("cdx-domain.txt", "cdx-p-z.txt"):
        lines += (SP / f).read_text().splitlines()
    n_pages = 0
    for rx, path, y0, y1 in ERAS:
        for ln in lines:
            parts = ln.split()
            if len(parts) < 3 or parts[2] not in ("200", "301", "302"):
                continue
            m = re.match(rx, parts[0])
            if not m:
                continue
            slug = unescape(m.group(1)).replace("%20", "").strip("-. ")
            if not slug or slug in NON or slug.startswith("--"):
                continue
            ts = parts[1]
            y = int(ts[:4])
            if not y0 <= y <= y1:
                continue
            key = (slug, f"{path}/{slug}")
            years.setdefault(y, {})[key] = {"slug": slug, "path": f"{path}/{slug}", "snapshot_ts": ts,
                                            "source": "cdx-index-first-capture"}
            n_pages += 1
    n_list = 0
    raw_dir = P.wayback / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    for fname, path, ts, rx in LISTINGS:
        src = SP / fname
        if not src.exists():
            continue
        y = int(ts[:4])
        dest = raw_dir / f"{y}-{path.strip('/').replace('/', '-')}.html"
        if not dest.exists():
            shutil.copy(src, dest)
        html = src.read_text(errors="replace")
        for m in re.finditer(rx, html):
            name = " ".join(unescape(m.group("name")).split()).rstrip(" *")
            if not name or name.upper().startswith("ATOMICO VENTURES") or name in ("View companies", "Our Portfolio"):
                continue
            slug = (m.groupdict().get("slug") or slugify(name)).strip("-")
            if slug in NON:
                continue
            key = (slug, path)
            years.setdefault(y, {})[key] = {"slug": slug, "name": name, "path": path, "snapshot_ts": ts,
                                            "source": "listing-capture"}
            n_list += 1
    parsed = P.wayback / "parsed"
    parsed.mkdir(parents=True, exist_ok=True)
    for y, rows in sorted(years.items()):
        dest = parsed / f"{y}.json"
        merged = {(r["slug"], r.get("path")): r
                  for r in (json.loads(dest.read_text()) if dest.exists() else [])}
        for k, r in rows.items():
            merged.setdefault(k, r)
        write_atomic(dest, json.dumps(sorted(merged.values(), key=lambda r: (r["slug"], r.get("path") or "")),
                                      indent=1) + "\n")
        print(f"  {y}: {len(rows)} rows")
    print(f"per-company page rows {n_pages}, listing rows {n_list}, years {sorted(years)}")


if __name__ == "__main__":
    main()
