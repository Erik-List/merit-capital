#!/usr/bin/env python3
"""Ribbit's live site: the Rebels list and the team, read from the Next.js
page bundles (the rendered pages carry names only; the bundles carry the
company URL and the founders per row, and the team's LinkedIn per person).

ribbitcap.com is Next.js (App Router). /rebels renders one row per company
("Company | Founder A., Founder B.") from an array in the page chunk
static/chunks/app/rebels/page-<hash>.js; /team renders names from an array in
static/chunks/app/team/page-<hash>.js. Neither page carries a year, a stage, a
sector or a title.

Writes sources/site/rebels.json (file_list source for site-portfolio.py) and
sources/site/team-pages.json (team_sources), and keeps the fetched pages and
bundles beside them so the pull is reproducible from disk.

Usage: python3 scratch/pull-site.py [--offline]
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

P = Paths("ribbit-capital")
SITE = P.site
BASE = "https://ribbitcap.com"
UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"


def get(url: str) -> str:
    out = subprocess.run(["curl", "-sL", "--max-time", "60", "-A", UA, url],
                         capture_output=True, check=True).stdout
    return out.decode("utf-8", errors="replace")


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def js_str(s: str) -> str:
    # A JS string literal is JSON except for escapes JSON lacks (\' and \xNN,
    # which the minifier emits for accented founder names: "Jan M\xf8ller").
    s = re.sub(r"\\x([0-9a-fA-F]{2})", r"\\u00\1", s.replace("\\'", "'"))
    return json.loads('"' + s + '"')


def bundle(page: str, offline: bool) -> str:
    html_path = SITE / f"{page}.html"
    js_path = SITE / f"{page}-page.js"
    if offline:
        return js_path.read_text()
    html = get(f"{BASE}/{page}")
    write_atomic(html_path, html)
    m = re.search(rf'static/chunks/app/{page}/page-[a-z0-9]+\.js[^"]*', html)
    if not m:
        sys.exit(f"no {page} page chunk in {BASE}/{page}")
    js = get(f"{BASE}/_next/{m.group(0)}")
    write_atomic(js_path, js)
    return js


def main() -> None:
    offline = "--offline" in sys.argv
    js = bundle("rebels", offline)
    rows = []
    for m in re.finditer(
            r'\{name:"((?:[^"\\]|\\.)*)",founderNames:\[(.*?)\],'
            r'companyUrl:(null|"(?:[^"\\]|\\.)*")', js):
        name = js_str(m.group(1)).strip()
        founders = [js_str(f) for f in re.findall(r'"((?:[^"\\]|\\.)*)"', m.group(2))]
        cu = None if m.group(3) == "null" else js_str(m.group(3)[1:-1])
        rows.append({"name": name, "slug": slugify(name), "url": f"{BASE}/rebels",
                     "company_url": cu, "founders": founders})
    # The rendered page is the check: every row it shows must have parsed.
    shown = re.findall(r'data-type="scrollable-list-item"', (SITE / "rebels.html").read_text())
    if len(shown) != len(rows):
        sys.exit(f"parsed {len(rows)} rows but the page renders {len(shown)}")
    write_atomic(SITE / "rebels.json", json.dumps(
        {"_readme": "Ribbit's live Rebels list, parsed from the /rebels page chunk by "
                    "scratch/pull-site.py; url is the listing, company_url and founders "
                    "are the firm's own per-row fields.",
         "rows": rows}, indent=1, ensure_ascii=False) + "\n")

    js = bundle("team", offline)
    team = []
    for m in re.finditer(r'\{name:("(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\'),url:"((?:[^"\\]|\\.)*)"', js):
        raw = m.group(1)
        name = raw[1:-1] if raw.startswith("'") else js_str(raw[1:-1])
        name = name.replace('"', '“', 1).replace('"', '”', 1) if '"' in name else name
        link = js_str(m.group(2))
        team.append({"name": name, "slug": slugify(re.sub(r'[“”"].*?[“”"]\s*', "", name)),
                     "url": f"{BASE}/team", "linkedin_url": link if "linkedin.com" in link else None})
    write_atomic(SITE / "team-pages.json", json.dumps(
        {"_readme": "Ribbit's live team page, parsed from the /team page chunk by "
                    "scratch/pull-site.py. The site publishes names and LinkedIn links only, "
                    "no titles and no groups.",
         "rows": team}, indent=1, ensure_ascii=False) + "\n")
    print(f"rebels: {len(rows)} rows; team: {len(team)} people")


if __name__ == "__main__":
    main()
