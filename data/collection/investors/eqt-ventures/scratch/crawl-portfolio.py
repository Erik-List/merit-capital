#!/usr/bin/env python3
"""Read every eqtgroup.com portfolio page's key facts (EQT Ventures run, PRO-163).

eqtgroup.com is Next.js (app router) over a private Sanity dataset
(30p7so6x / eqt-public-web-prod, zero documents without a token), so the
ladder's step 2 is closed and the rows come from the RSC payload each page
ships (step 3). The listing page carries only the CURRENT portfolio (356);
the sitemap (/api/sitemap.xml) carries 639 company pages, the other 290
being exited companies whose page stays up. Every page's `keyFacts`
(fund items, entry year as `launchYear`, exit, sector, country) and its
`snowflakeFunds` (fund name, entry, exit, market, sector, per fund) are
read; raw pages go to data/filings/eqt-ventures/site-raw/ (gitignored).

Usage: crawl-portfolio.py [--refetch]
"""
import json, re, sys, time, subprocess
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from rsc import rsc_stream, rsc_records, find_objs
ROOT = HERE.parents[4]
RAW = ROOT / "data/filings/eqt-ventures/site-raw"
OUT = HERE.parent / "sources/site/eqtgroup-portfolio-pages.json"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
sm = (ROOT / "data/filings/eqt-ventures/sitemap-2026-09-27.xml").read_text()
urls = sorted(set(u for u in re.findall(r'<loc>(https://eqtgroup.com/about/current-portfolio/[^<]+)</loc>', sm) if '/funds/' not in u))

LABELS = {"Sector", "Country", "Fund", "Funds", "Entry", "Exit", "Website", "Description",
          "Responsible advisor", "Responsible advisors"}
def parse_page(slug, url, html):
    """Key Facts as the page renders them: label lines followed by value lines."""
    import html as H
    t = re.sub(r"<script.*?</script>", "", html, flags=re.S)
    t = re.sub(r"<style.*?</style>", "", t, flags=re.S)
    t = H.unescape(re.sub(r"<[^>]+>", "\n", t))
    lines = [l.strip() for l in t.split("\n") if l.strip()]
    title = re.search(r"<title>([^<]+)</title>", html)
    title = H.unescape(title.group(1)) if title else ""
    kind = "former" if "Former EQT Portfolio" in title else ("current" if "Portfolio" in title else "other")
    facts, cur = {}, None
    try:
        k0 = lines.index("Key Facts")
    except ValueError:
        k0 = None
    tagline = None
    if k0 is not None:
        # heading block: breadcrumb 'Current Portfolio', '/', name, [Divestment], name, tagline...
        head = lines[:k0]
        tagline = head[-1] if head else None
        for l in lines[k0 + 1:]:
            if l in ("Do You Want to Know More?", "Contact us"):
                break
            if l in LABELS:
                cur = l.rstrip("s") if l.startswith("Responsible") else ("Fund" if l == "Funds" else l)
                facts.setdefault(cur, [])
                continue
            if cur:
                facts[cur].append(l)
            else:
                # older layout: the fund names sit directly under "Key Facts",
                # before the first label, with no "Fund" label of their own
                facts.setdefault("Fund", []).append(l)
    web = None
    m = re.search(r'Website</[^>]+>.*?<a[^>]+href="(https?://[^"]+)"', html, re.S)
    if m: web = H.unescape(m.group(1))
    name = re.search(r"<h1[^>]*>([^<]+)", html)
    return {
        "slug": slug, "url": url, "name": H.unescape(name.group(1)).strip() if name else None,
        "page_kind": kind, "divestment_label": "Divestment" in lines[:k0 or 0],
        "funds": list(dict.fromkeys(facts.get("Fund", []))), "entry_year": (facts.get("Entry") or [None])[0],
        "exit_year": (facts.get("Exit") or [None])[0], "sector": (facts.get("Sector") or [None])[0],
        "country": (facts.get("Country") or [None])[0], "advisors": facts.get("Responsible advisor", []),
        "description": " ".join(facts.get("Description", [])) or None, "tagline": tagline,
        "website": web, "page_title": title,
    }

refetch = '--refetch' in sys.argv
rows, failed = [], []
for i, u in enumerate(urls):
    slug = u.rsplit('/', 1)[1]
    f = RAW / f"{slug}.html"
    if refetch or not f.exists() or f.stat().st_size < 20000:
        r = subprocess.run(["curl", "-sL", "--max-time", "40", "-A", UA, "-o", str(f), "-w", "%{http_code}", u], capture_output=True, text=True)
        time.sleep(0.6)
        if r.stdout.strip() != "200":
            failed.append((slug, r.stdout.strip())); continue
    html = f.read_text(encoding="utf-8", errors="replace")
    rows.append(parse_page(slug, u, html))
    if i % 50 == 0:
        print(f"{i}/{len(urls)} rows={len(rows)} failed={len(failed)}", flush=True)
OUT.write_text(json.dumps({"_readme": __doc__, "read": time.strftime("%Y-%m-%d"), "rows": rows, "failed": failed}, indent=1, ensure_ascii=False))
print("rows", len(rows), "failed", len(failed), failed[:20])
