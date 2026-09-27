#!/usr/bin/env python3
"""The firm's own announcement archive: stories.eqtventures.com (Framer, live,
172 article URLs in its sitemap, read 2026-09-27). Each page is fetched once
(raw under data/filings/eqt-ventures/stories-raw/, gitignored) and reduced to
title, date, body text and outbound company links. The blog carries EQT
Ventures posts (2016 onward, including the migrated Medium posts), and since
2025 also EQT Growth and Scaleup Europe Fund posts: the desk of each post is
read from its words, never assumed (decisions.md D2, D3).

Output: ../sources/site/stories.json
"""
import html as H, json, re, subprocess, sys, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import write_atomic  # noqa: E402
RAW = ROOT / "data/filings/eqt-ventures/stories-raw"
OUT = HERE.parent / "sources/site/stories.json"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
sm = (ROOT / "data/filings/eqt-ventures/stories-sitemap-2026-09-27.xml").read_text()
urls = [u for u in re.findall(r"<loc>([^<]+)</loc>", sm) if "/articles/" in u]
MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec"
rows, failed = [], []
for u in urls:
    slug = u.rsplit("/", 1)[1]
    f = RAW / (re.sub(r"[^A-Za-z0-9._-]+", "_", slug)[:180] + ".html")
    if not f.exists() or f.stat().st_size < 5000:
        r = subprocess.run(["curl", "-sL", "--max-time", "40", "-A", UA, "-o", str(f), "-w", "%{http_code}", u],
                           capture_output=True, text=True)
        time.sleep(0.8)
        if r.stdout.strip() != "200":
            failed.append([u, r.stdout.strip()]); continue
    h = f.read_text(encoding="utf-8", errors="replace")
    body = re.sub(r"<script.*?</script>|<style.*?</style>", "", h, flags=re.S)
    links = sorted(set(H.unescape(x) for x in re.findall(r'href="(https?://[^"]+)"', body)
                       if not re.search(r"eqtventures\.com|eqtgroup\.com|framer|linkedin\.com/company/eqt|twitter\.com/eqtventures|x\.com/eqtventures|instagram|youtube", x)))
    t = H.unescape(re.sub(r"<[^>]+>", "\n", body))
    lines = [l.strip() for l in t.split("\n") if l.strip()]
    title = re.search(r"<title>([^<]+)</title>", h)
    date = None
    for l in lines[:80]:
        m = re.fullmatch(rf"(?:{MONTHS})\.? \d{{1,2}},? \d{{4}}|\d{{1,2}} (?:{MONTHS}) \d{{4}}|\d{{4}}-\d{{2}}-\d{{2}}", l)
        if m:
            date = l; break
    text = "\n".join(lines)
    rows.append({"url": u, "slug": slug, "title": H.unescape(title.group(1)) if title else None,
                 "date_text": date, "text": text[:20000], "links": links})
write_atomic(OUT, json.dumps({"_readme": __doc__, "read": time.strftime("%Y-%m-%d"),
                              "rows": rows, "failed": failed}, indent=1, ensure_ascii=False))
print("rows", len(rows), "failed", len(failed))
