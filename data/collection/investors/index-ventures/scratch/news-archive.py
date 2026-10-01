#!/usr/bin/env python3
"""The firm's archived news, 1999-2019, from the Common Crawl captures of
indexventures.com (sources/wayback/cc-manifest.json):
  2008-2013 PHP site   /news/index/news_id/<n>: one press release or cutting per
                       page (h2#news-title, h4#news-date, body); every news page
                       also lists dated titles in <ul id="results">.
  2013      /blog/index/...: the firm's blog posts.
  2014-2019 Drupal     /news-room/news|blog|index-insight/<slug>.
One row per item with its capture URL (the citation where the live site dropped
the page), date, title, kind, the sentences that name a round, and the base
companies its title names. Output sources/wayback/news-archive.json.
An announcement is class 1 for the round it NAMES; it asserts an entry only
where it says so in words (COLLECTION.md s6)."""
import html as H, json, re
from datetime import datetime
from pathlib import Path
def read_raw(f):
    """Raw captures are gzipped on disk (2026-10-01: the machine ran out of space mid-run)."""
    import gzip
    g = Path(str(f) + ".gz")
    if g.exists():
        return gzip.open(g, "rt", errors="replace").read()
    return f.read_text(errors="replace") if f.exists() else None


ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[3]
CCRAW = REPO / "data" / "filings" / "commoncrawl" / "index-ventures"
WB = ROOT / "sources" / "wayback"
ROUND = re.compile(r"\b(pre-?seed|seed|series [A-K]\b|first round|second round|third round|fourth round|round of|growth (?:stage|funding|round|capital|investment)|"
                   r"financing|funding|invests? in|invested in|investment in|led by|raises?|raised|secures?|closes?|\$\s?\d[\d.,]*\s?(?:m\b|million|bn|billion)|"
                   r"€\s?\d[\d.,]*\s?(?:m\b|million)|£\s?\d[\d.,]*\s?(?:m\b|million)|acquire[sd]?|acquisition|ipo\b|initial public offering)", re.I)


def clean(s):
    return re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def iso(s):
    s = clean(s).replace(",", "")
    for fmt in ("%B %d %Y", "%b %d %Y", "%d %B %Y", "%d %b %Y", "%m/%d/%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(s, fmt).strftime("%Y-%m-%d")
        except ValueError:
            pass
    return None


def sents(text):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-Z\"“])", text) if s.strip() and ROUND.search(s)]


def loose(s):
    s = re.sub(r"\(.*?\)", "", s or "")
    return re.sub(r"[^a-z0-9]+", "", re.sub(r"\b(inc|ltd|limited|corp|corporation|llc|sa|plc|com)\b\.?", "", s.lower()))


man = json.loads((WB / "cc-manifest.json").read_text())
items = {}          # id -> row
for key, v in sorted(man.items()):
    if v.get("status") != "ok":
        continue
    path = re.sub(r"https?://(www\.)?indexventures\.com(:80|:443)?", "", v["url"], flags=re.I).split("?")[0]
    path = re.sub(r"^/index\.php", "", path)
    f = CCRAW / key
    if read_raw(f) is None:
        continue
    cap = v["capture_url"]; ts = v["timestamp"]
    if path.startswith("/news") and not path.startswith("/news-room"):
        body = read_raw(f)
        # listing items: dated titles (kept when the item's own page was never captured)
        for nid, d, t in re.findall(r'href="/news/index/news_id/(\d+)"[^>]*>\s*<h4>(.*?)</h4>\s*<p>(.*?)</p>', body, flags=re.S):
            k = f"news_id/{nid}"
            row = items.setdefault(k, {"id": k, "kind": "news", "date": iso(d), "title": clean(t), "capture_url": cap, "ts": ts, "listing_only": True})
        m = re.search(r"/news/index/news_id/(\d+)", path)
        t = re.search(r'<h2 id="news-title">(.*?)</h2>\s*<h4 id="news-date">(.*?)</h4>(.*?)</div>', body, flags=re.S)
        if m and t:
            k = f"news_id/{m.group(1)}"
            text = " ".join(clean(p) for p in re.findall(r"<p[^>]*>(.*?)</p>", t.group(3), flags=re.S))
            old = items.get(k, {})
            if old.get("listing_only", True) or ts < old.get("ts", "9"):
                items[k] = {"id": k, "kind": "news", "date": iso(t.group(2)) or old.get("date"), "title": clean(t.group(1)),
                            "capture_url": cap, "ts": ts, "lede": text[:500], "round_sentences": sents(text)[:8]}
        continue
    m = re.fullmatch(r"/news-room/(news|blog|index-insight|index-likes|events)/([^/]+)/?", path) or re.fullmatch(r"/(blog)/index/post_id/(\d+)[^/]*/?.*", path)
    if m:
        body = read_raw(f)
        t = re.search(r"<title>(.*?)</title>", body, flags=re.S)
        title = re.split(r"\s+\|\s+Index Ventures", clean(t.group(1)) if t else "")[0]
        title = re.sub(r"^Index Ventures\s*[-|:]\s*(Blog\s*[-|:]\s*)?", "", title)
        if not title or re.search(r"page not found", title, flags=re.I):
            continue
        d = re.search(r'(?:datetime|content)="(\d{4}-\d{2}-\d{2})', body) or re.search(r'class="[^"]*date[^"]*"[^>]*>\s*([^<]{6,30})<', body)
        date = (d.group(1) if d and re.match(r"\d{4}-", d.group(1)) else iso(d.group(1)) if d else None)
        main = body[body.find("<h1"):] if "<h1" in body else body
        text = " ".join(clean(p) for p in re.findall(r"<p[^>]*>(.*?)</p>", main, flags=re.S))
        k = f"{m.group(1)}/{m.group(2)}"
        if k not in items or ts < items[k]["ts"]:
            items[k] = {"id": k, "kind": m.group(1), "date": date, "title": title, "capture_url": cap, "ts": ts,
                        "lede": text[:500], "round_sentences": sents(text)[:8]}

base_p = ROOT / "companies" / "base.json"
names = {}
if base_p.exists():
    for r in json.load(open(base_p)):
        k = loose(r["name"])
        if len(k) >= 4:
            names[k] = r["slug"]
rows = []
for it in items.values():
    lt = loose(it["title"])
    it["company_keys"] = sorted({s for k, s in names.items() if k in lt})
    rows.append(it)
rows.sort(key=lambda r: (r.get("date") or "", r["id"]))
(WB / "news-archive.json").write_text(json.dumps({"_readme": __doc__, "rows": rows}, indent=1, ensure_ascii=False) + "\n")
import collections
print(len(rows), "items;", sum(1 for r in rows if not r.get("listing_only")), "with a page;", sum(1 for r in rows if r["company_keys"]), "name a base company")
print(sorted(collections.Counter((r.get("date") or "none")[:4] for r in rows).items()))
