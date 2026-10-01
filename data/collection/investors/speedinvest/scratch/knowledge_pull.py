"""Pull every www.speedinvest.com/knowledge/<slug> post (sitemap) into
sources/site/knowledge-posts.json: url, title, date, category, author, body text.
The firm's own posts are its announcement archive (COLLECTION.md s6: class 1 for
the round a post NAMES; an ENTRY only where the post says so in words)."""
import re, json, html, subprocess, time, sys, datetime
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
from paths import write_atomic
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128 Safari/537.36"
HERE = Path(__file__).resolve().parent
RAW = HERE / "knowledge-raw"; RAW.mkdir(exist_ok=True)
sm = (HERE / "sitemap.xml").read_text()
urls = [u for u in re.findall(r"<loc>([^<]+)</loc>", sm) if "/knowledge/" in u]
def get(u, dest):
    if dest.exists() and dest.stat().st_size > 5000: return dest.read_text(errors="replace")
    for _ in range(3):
        r = subprocess.run(["curl", "-sSL", "--max-time", "60", "-A", UA, u], capture_output=True)
        if r.returncode == 0 and len(r.stdout) > 5000:
            dest.write_bytes(r.stdout); time.sleep(0.5); return r.stdout.decode("utf-8", "replace")
        time.sleep(3)
    return ""
def text(s):
    s = re.sub(r"<(script|style|svg).*?</\1>", "", s, flags=re.S)
    s = re.sub(r"<br\s*/?>|</p>|</h\d>|</li>", "\n", s)
    t = html.unescape(re.sub(r"<[^>]+>", " ", s))
    t = re.sub(r"[ \t‍\xa0]+", " ", t)
    return re.sub(r"\n\s*\n+", "\n", t).strip()
rows = []
for i, u in enumerate(urls):
    slug = u.rstrip("/").rsplit("/", 1)[-1]
    s = get(u, RAW / f"{slug}.html")
    if not s:
        rows.append({"url": u, "status": "FAILED"}); continue
    title = re.search(r"<title>(.*?)</title>", s, re.S)
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S)
    date = re.search(r">([A-Z][a-z]+ \d{1,2}, 20\d\d)<", s)
    body = re.search(r'class="[^"]*(?:rich-text|w-richtext)[^"]*"[^>]*>(.*?)</div>\s*</div>', s, re.S)
    rt = "\n".join(text(m) for m in re.findall(r'<div[^>]*class="[^"]*w-richtext[^"]*"[^>]*>(.*?)</div>', s, re.S))
    cats = re.findall(r'href="/blog-categories/([^"]+)"', s)
    rows.append({"url": u, "slug": slug, "title": text(h1.group(1)) if h1 else (html.unescape(title.group(1)) if title else None),
                 "date": datetime.datetime.strptime(date.group(1), "%B %d, %Y").date().isoformat() if date else None,
                 "categories": sorted(set(cats)), "body": rt[:40000]})
    if i % 25 == 0: print(i, len(urls), file=sys.stderr)
write_atomic(HERE.parent / "sources" / "site" / "knowledge-posts.json", json.dumps(
    {"_readme": "www.speedinvest.com/knowledge/<slug> (Webflow blog, all sitemap URLs) pulled by scratch/knowledge_pull.py " + datetime.date.today().isoformat() + "; body = the post's rich-text blocks.",
     "rows": rows}, indent=1, ensure_ascii=False))
print(len(rows), sum(1 for r in rows if r.get("status") == "FAILED"), "failed")
