#!/usr/bin/env python3
"""Read every northzone.com/insights/<slug> post in sitemap.xml: title, date,
type label, body text and the portfolio pages it links. Writes
sources/site/insights.json. Raw pages in data/filings/northzone/insights-raw."""
import json, re, subprocess, time, html as H, os
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT.parents[2] / "filings" / "northzone" / "insights-raw"
RAW.mkdir(parents=True, exist_ok=True)
UA = "Mozilla/5.0 (MeritCapitalResearch; erik@meritcapit.al)"
def get(url, dest):
    if dest.exists() and dest.stat().st_size > 1000:
        return dest.read_text()
    for i in range(3):
        r = subprocess.run(["curl", "-sS", "-f", "-L", "--max-time", "30", "-A", UA, url], capture_output=True)
        if r.returncode == 0:
            dest.write_text(r.stdout.decode("utf-8", "replace")); time.sleep(0.35)
            return dest.read_text()
        time.sleep(3)
    return ""
sm = (ROOT.parents[2] / "filings" / "northzone" / "site-raw" / "sitemap.xml").read_text()
urls = sorted(set(u for u in re.findall(r"<loc>([^<]+)</loc>", sm) if "/insights/" in u))
WP = json.loads((ROOT / "scratch" / "wp-posts-index.json").read_text())
rows = []
for u in urls:
    slug = u.rstrip("/").rsplit("/", 1)[1]
    h = get(u, RAW / f"{slug}.html")
    if not h:
        rows.append({"url": u, "slug": slug, "failed": True}); continue
    title = re.search(r"<title>([^<]*)</title>", h)
    rt = re.search(r'class="text-rich-text w-richtext">(.*?)</div>\s*</div>', h, flags=re.S)
    body_txt = " ".join(H.unescape(x.strip()) for x in re.sub(r"<[^>]+>", "\n", rt.group(1)).split("\n") if x.strip()) if rt else ""
    view = re.search(r'<a[^>]+href="(https?://(?!northzone\.com)[^"]+)"[^>]*>(?:(?!</a>).)*?View article', h, flags=re.S)
    body = re.sub(r"<script.*?</script>|<style.*?</style>|<nav.*?</nav>|<footer.*?</footer>", "", h, flags=re.S)
    lines = [H.unescape(l.strip()) for l in re.sub(r"<[^>]+>", "\n", body).split("\n") if l.strip()]
    kind = next((l for l in lines[:40] if l in ("Press", "Perspective", "News", "Portfolio news", "Podcast", "Announcement", "Insight", "Investment", "Opinion")), None)
    rows.append({"url": u, "slug": slug,
                 "title": H.unescape(title.group(1)).rsplit(" - Northzone", 1)[0].strip() if title else None,
                 "kind": kind, "date_wp": (WP.get(slug) or [None])[0],
                 "article_url": view.group(1) if view else None,
                 "portfolio_links": sorted(set(re.findall(r'href="/portfolio/([^"?#]+)"', h))),
                 "body": body_txt[:12000]})
out = ROOT / "sources" / "site" / "insights.json"
tmp = str(out) + ".t"
open(tmp, "w").write(json.dumps({"_readme": "northzone.com/insights, every post in sitemap.xml, read by scratch/insights-scrape.py on " + time.strftime("%Y-%m-%d") + ". body is the post's rich-text block; article_url is the outbound press article of a Press post; date_wp is the post's date from its archived WordPress URL /YYYY/MM/DD/<slug>/ (scratch/wp-posts-index.json), null where the post was never on the WordPress site; the page itself prints no date of its own.", "rows": rows}, indent=1, ensure_ascii=False))
os.replace(tmp, out)
print(len(rows), "posts", sum(1 for r in rows if r.get("failed")), "failed")
