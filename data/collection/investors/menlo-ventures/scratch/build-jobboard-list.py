#!/usr/bin/env python3
"""jobs.menlovc.com (Getro) -> sources/site/jobboard.json.

A first-party company list independent of the portfolio CMS (COLLECTION.md 5,
the Thrive precedent). It carries only companies currently hiring, so it is a
precision surface for the live book rather than a recall surface for the
history -- but it does list rows the portfolio CMS does not, and each of those
is a candidate the recall probe would otherwise have to find.

Names come from the rendered /companies page (server-rendered by Getro, one
`.company-name-text` per card); the sitemap is the completeness check.
"""
import json, re, subprocess, sys, time
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126 Safari/537.36")
BASE = "https://jobs.menlovc.com"


def curl(url: str) -> str:
    return subprocess.run(["curl", "-sL", "--max-time", "120", "-H", f"User-Agent: {UA}", url],
                          capture_output=True, check=True).stdout.decode("utf-8", "replace")


def main() -> None:
    p = Paths("menlo-ventures")
    sm = curl(f"{BASE}/sitemap.xml")
    slugs = sorted({m.group(1) for m in
                    (re.match(r"https://jobs\.menlovc\.com/companies/([^/]+)/?$", loc)
                     for loc in re.findall(r"<loc>([^<]+)</loc>", sm)) if m})
    cache = Path(__file__).resolve().parent / "jobboard-pages"
    cache.mkdir(exist_ok=True)
    rows = []
    for i, slug in enumerate(slugs, 1):
        f = cache / f"{slug}.html"
        if not f.exists():
            write_atomic(f, curl(f"{BASE}/companies/{slug}"))
            time.sleep(0.6)
        h = f.read_text(encoding="utf-8", errors="replace")
        name, domain, tags, founded = slug, None, [], None
        j = h.find(f'"slug":"{slug}"')
        if j > 0:
            before = h[max(0, j - 40000):j]
            nm = re.findall(r'"name":"((?:[^"\\]|\\.)*)"', before)
            if nm:
                name = json.loads(f'"{nm[-1]}"')
            after = h[j:j + 1200]
            fd = re.search(r'"founded":"?(\d{4})"?', h[max(0, j - 200):j])
            founded = int(fd.group(1)) if fd else None
            dm = re.search(r'"domain":"([^"]*)"', after)
            domain = dm.group(1) if dm else None
            tm = re.search(r'"industryTags":\[([^\]]*)\]', after)
            if tm:
                tags = [json.loads(x) for x in re.findall(r'"(?:[^"\\]|\\.)*"', tm.group(1))]
        rows.append({"name": name, "slug": slug, "url": f"{BASE}/companies/{slug}",
                     "domain": domain, "sectors": tags, "founded": founded})
        if i % 40 == 0:
            print(f"  {i}/{len(slugs)}")
    out = {"_readme": ("Built by scratch/build-jobboard-list.py: every company slug in "
                       "jobs.menlovc.com/sitemap.xml, with the display name read off "
                       "that company's own Getro page (the /companies index renders only "
                       "the first 12 cards and loads the rest by infinite scroll). "
                       "First-party company list, currently-hiring companies only -- "
                       "precision for the live book, not recall for the history."),
           "source_url": f"{BASE}/companies",
           "rows": rows}
    write_atomic(p.site / "jobboard.json", json.dumps(out, indent=1) + "\n")
    print(f"job-board companies: {len(rows)}")


if __name__ == "__main__":
    main()
