#!/usr/bin/env python3
"""Pull careers.atomico.com (Getro) as a first-party company list (adapted from Lux).

COLLECTION.md §5: a firm's job board is a first-party company list, and on a
deep-tech book it reaches companies the marketing site drops (Lux's live
/companies page carries 215 rows; the board carries 190, and the archive holds
312 board slugs across 2019-2026). The board's own `stage` field is NEVER a
stage label -- it scored 0/10 on Thrive's gate and is kept only as an
unscored extra, judged on the golden set before anything trusts it.

Enumerated from sitemap_companies.xml; each company page ships its record in
__NEXT_DATA__ (name, domain, description, stage, topics).

Writes sources/site/jobboard-companies.json.
"""
import json
import re
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
BASE = "https://careers.atomico.com"


def get(url: str, dest: Path) -> str:
    if dest.exists():
        return dest.read_text(encoding="utf-8", errors="replace")
    for _ in range(3):
        try:
            out = subprocess.run(["curl", "-sfL", "--compressed", "--max-time", "60",
                                  "-H", f"User-Agent: {UA}", url],
                                 capture_output=True, check=True).stdout.decode(
                                     "utf-8", errors="replace")
            write_atomic(dest, out)
            time.sleep(0.2)
            return out
        except subprocess.CalledProcessError:
            time.sleep(2)
    return ""


def record(html: str) -> dict | None:
    """The board's own record for this page's company (pageProps.company).

    initialState.companyDetails carries only {id, jobs} on a detail page, and
    initialState.companies.found is the listing slice, so neither answers here.
    """
    m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',
                  html, re.S)
    if not m:
        return None
    c = json.loads(m.group(1)).get("props", {}).get("pageProps", {}).get("company")
    return c if isinstance(c, dict) and c.get("name") else None


def main():
    p = Paths("atomico")
    raw = p.scratch / "jobs-raw"
    raw.mkdir(parents=True, exist_ok=True)
    sm = get(f"{BASE}/sitemap.xml", raw / "sitemap.xml")
    # The board's sitemap lists every job page too (/companies/<slug>/jobs/<id>);
    # only the company pages themselves are the list.
    urls = [u for u in re.findall(r"<loc>([^<]+)</loc>", sm)
            if re.search(r"/companies/[^/]+/?$", u)]
    print(f"board sitemap: {len(urls)} companies")
    rows, misses = [], []
    for i, u in enumerate(urls, 1):
        slug = u.rstrip("/").rsplit("/", 1)[-1]
        html = get(u, raw / f"{slug}.html")
        rec = record(html) if html else None
        if not rec:
            misses.append(slug)
            continue
        rows.append({"slug": slug, "name": rec.get("name"),
                     "url": rec.get("websiteUrl") or (
                         f"https://{rec['domain']}" if rec.get("domain") else None),
                     "description": (rec.get("description") or "")[:600] or None,
                     "founded_board": rec.get("founded"),
                     "org_type_board": rec.get("orgType"),
                     "stage_board": rec.get("stage"),
                     "topics_board": rec.get("topics") or rec.get("bizModels") or [],
                     "approx_employees": rec.get("approxEmployees")})
        if i % 50 == 0:
            print(f"  {i}/{len(urls)}")
    write_atomic(p.site / "jobboard-companies.json", json.dumps(
        {"_readme": "careers.atomico.com (Getro board, the firm's own subdomain), enumerated "
                    "from sitemap.xml (/companies/<slug>) and parsed from each page's __NEXT_DATA__ "
                    "by scratch/jobboard-pull.py. stage_board is the board's own field and "
                    "is NOT a stage label (COLLECTION.md §5, Thrive: 0/10 on the gate).",
         "rows": sorted(rows, key=lambda r: r["slug"])}, indent=1))
    print(f"board: {len(rows)} rows, {len(misses)} unparsed {misses[:10]}")


if __name__ == "__main__":
    main()
