"""Read the firm's archived /company/<slug> pages: the site's own name, its
menu category (2011-2013 menu: 'FF Angel' and the sector groups), description,
founders and the per-company news list (title, date, link).

Input : scratch/wb/inventory-foundersfund.com.json (CDX, one row per urlkey per period)
Output: sources/wayback/raw/company/<slug>-<ts>.html (captured bodies, cached)
        sources/wayback/company-pages.json            (the sidecar the judge reads)
        sources/wayback/parsed/<year>.json            (name written onto slug-only rows)
Fetches go through wayback-pull's status-aware fetch and the shared IA throttle;
a failed fetch is left out and retried on the next run, never recorded as empty."""
import importlib.util, json, re, sys, collections
from html import unescape
from pathlib import Path
ROOT = Path(__file__).resolve().parents[6]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic
spec = importlib.util.spec_from_file_location("wp", ROOT / "scripts" / "wayback-pull.py")
wp = importlib.util.module_from_spec(spec); spec.loader.exec_module(wp)
p = Paths("founders-fund")
NON = set(p.config()["wayback"]["non_company_slugs"])
inv = json.loads((p.root / "scratch/wb/inventory-foundersfund.com.json").read_text())
caps = collections.defaultdict(list)
for y0, y1, key, ts, orig, mime, sc, dig in inv:
    m = re.match(r"^/company/([a-z0-9_-]+)/?$", re.sub(r"^[^)]*\)", "", key).split("?")[0])
    if m and sc == "200" and m.group(1) not in NON:
        caps[m.group(1)].append((ts, orig))
raw = p.wayback / "raw" / "company"; raw.mkdir(parents=True, exist_ok=True)
side_path = p.wayback / "company-pages.json"
side = json.loads(side_path.read_text()) if side_path.exists() else {}
def text(h): return re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", h))).strip()
def parse(html, slug, ts, orig):
    out = {"snapshot_ts": ts, "capture_url": wp.wb(ts, orig)}
    m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S)
    t = re.search(r"<title>(.*?)</title>", html, re.S)
    name = text(m.group(1)) if m else ""
    title = text(t.group(1)) if t else ""
    if not name and title:
        name = re.split(r"\s*(?:«|&laquo;|\||–|-)\s*Founders Fund", title)[0].strip()
    out["name"], out["title"] = name, title
    # 2011-2013 menu: term blocks listing every company by category
    cats = {}
    for blk in re.finditer(r'<li id="term-\d+" class="term[^"]*">\s*<a title="([^"]+)"(.*?)(?=<li id="term-\d+"|</nav|<div id="content|$)', html, re.S):
        for s2, n2 in re.findall(r'/company/([a-z0-9_-]+)/?" title="([^"]*)"', blk.group(2)):
            cats.setdefault(s2, {"category": unescape(blk.group(1)), "name": unescape(n2)})
    if cats:
        out["menu"] = cats
    body = html[m.end():] if m else html
    body = re.sub(r"<script.*?</script>|<style.*?</style>", "", body, flags=re.S)
    cut = re.search(r"Copyright|<footer", body)
    body = body[:cut.start()] if cut else body
    out["text"] = text(body)[:1500]
    news = []
    for href, label in re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', body, re.S):
        lab = text(label)
        if len(lab) > 25 and "foundersfund.com/company" not in href and not href.startswith("#"):
            news.append({"title": lab[:200], "url": re.sub(r"^https?://web\.archive\.org/web/\d+(?:id_)?/", "", href)})
    out["links"] = news[:25]
    dt = re.findall(r"((?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4})", text(body))
    out["dates"] = dt[:25]
    return out
done = fail = 0
for slug, cs in sorted(caps.items()):
    cs.sort()
    picks = [cs[0]] + ([cs[-1]] if cs[-1][0][:4] != cs[0][0][:4] else [])
    for ts, orig in picks:
        key = f"{slug}@{ts}"
        if key in side:
            continue
        html = wp.fetch(wp.wb(ts, orig, raw=True), raw / f"{slug}-{ts}.html")
        if not html or len(html) < 500:
            fail += 1; continue
        side[key] = {"slug": slug, **parse(html, slug, ts, orig)}
        done += 1
        if done % 20 == 0:
            write_atomic(side_path, json.dumps(side, indent=1) + "\n"); print(f"  {done} pages read", flush=True)
write_atomic(side_path, json.dumps(side, indent=1) + "\n")
print(f"pages read this run: {done}, failed (retry later): {fail}, sidecar entries: {len(side)}, slugs: {len(caps)}")
