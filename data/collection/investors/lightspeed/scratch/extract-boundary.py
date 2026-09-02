#!/usr/bin/env python3
"""LSIP boundary evidence from lsvp.com's own rendered surfaces (ruling 2).

The main companies page renders BOTH firms' rows with the site's own
attribution attribute (`data-investor="lsvp|lsip|both"`); the team page
takes a server-side `?firm=lsip` param. companies.json keeps only
lsvp/both rows (config `require`); this script preserves the excluded
side — the lsip-only company cards and the LSIP roster — as judge and
recall-probe instruments:

  sources/site/lsip-companies.json   65 lsip-only cards (their fields)
  sources/site/lsip-people.json      the ?firm=lsip roster

Usage: python3 data/collection/investors/lightspeed/scratch/extract-boundary.py
"""
import json
import re
import subprocess
import sys
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths  # noqa: E402

UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
P = Paths("lightspeed")


def get(url: str) -> str:
    return subprocess.run(
        ["curl", "-sfL", "--max-time", "90", "-H", f"User-Agent: {UA}", url],
        capture_output=True, check=True).stdout.decode("utf-8", errors="replace")


def field(block: str, pat: str) -> str | None:
    m = re.search(pat, block, re.S)
    return unescape(re.sub(r"\s+", " ", m.group(1))).strip() if m else None


def main() -> None:
    P.site.mkdir(parents=True, exist_ok=True)

    html = get("https://lsvp.com/companies/")
    rows = []
    for block in re.split(r"<li data-appear-list ", html)[1:]:
        if field(block, r'data-investor="([^"]+)"') != "lsip":
            continue
        rows.append({
            "site_slug": field(block, r'data-company-id="([^"]+)"'),
            "name": field(block, r"<h5>\s*([^<]+?)\s*<"),
            "url": field(block, r'<a href="([^"]+)"'),
            "founded": field(block, r"<strong>Founded</strong>\s*<span>([^<]*)</span>"),
            "stage_invested": field(block, r"Invested</strong>\s*<span>([^<]*)</span>"),
            "backed_since": field(block, r"Since</strong>\s*<span>([^<]*)</span>"),
            "status_site": field(block, r"<strong>Status</strong>\s*<span>([^<]*)</span>"),
        })
    (P.site / "lsip-companies.json").write_text(json.dumps({
        "_readme": "lsip-only cards from https://lsvp.com/companies/ "
                   "(data-investor='lsip'; 'both' rows are LSVP listings and "
                   "live in companies.json). Boundary evidence for ruling 2: "
                   "these are NOT LSVP site listings.",
        "rows": rows}, indent=1) + "\n")
    print(f"lsip-companies.json: {len(rows)} rows")

    html = get("https://lsvp.com/lightspeed-team/?firm=lsip")
    people = []
    for block in re.split(r'<a href="https://lsvp\.com/team-member/', html)[1:]:
        slug = field(block, r"^([a-z0-9-]+)/")
        name = field(block, r'text-primary-link--bold">([^<]+)</div>')
        if slug and name:
            people.append({"slug": slug, "name": name,
                           "role": field(block, r'text-details--reg">\s*([^<]+?)\s*</div>')})
    (P.site / "lsip-people.json").write_text(json.dumps({
        "_readme": "https://lsvp.com/lightspeed-team/?firm=lsip (server-side "
                   "firm filter). LSIP roster: NOT sweep targets; a Form D "
                   "attribution to one of these names is LSIP evidence, not "
                   "LSVP (ruling 2).",
        "rows": people}, indent=1) + "\n")
    print(f"lsip-people.json: {len(people)} people")


if __name__ == "__main__":
    main()
