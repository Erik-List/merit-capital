#!/usr/bin/env python3
"""Replay-path wayback layer (COLLECTION.md §5, the 2026-09 IA partial outage): parse the raw
portfolio-page captures fetched by hand (scratchpad/wb/*.html, copied into sources/wayback/raw/)
with the same era regexes config.json carries, into sources/wayback/parsed/<year>.json rows
{slug, name, path, snapshot_ts} (merged by slug+path so wayback-pull.py converges over them),
and read the firm's own per-card labels into sources/site/portfolio-2013-2015.json (usv:* attributes)
and sources/site/portfolio-2016-2019.json (card meta 'Series A, 2015'). The 2016-2018 cards carry no
company name: names resolve through the 2019 captures' title attribute (same blog-post slug), then
the card description's leading words, then a hand map (UNRESOLVED printed for review)."""
import json, re, html, shutil, sys
from pathlib import Path
SP = Path("/private/tmp/claude-501/-Users-erik-Developer-merit-capital/e3463019-81ac-497e-9be8-95891a480d43/scratchpad/wb")
I = Path("data/collection/investors/union-square-ventures")
RAW, PARSED, SITE = I / "sources/wayback/raw", I / "sources/wayback/parsed", I / "sources/site"
cfg = json.load(open(I / "config.json"))
eras = cfg["wayback"]["eras"]
def slug_of(name):
    s = re.sub(r"[^a-z0-9]+", "-", html.unescape(name).lower()).strip("-")
    return s or "x"
# file -> (year, timestamp (14 digits; approximate ones flagged), era path, exact)
FILES = {
 "p2005.html": (2005, "20051027035629", "/portfolio.html", True), "p2006.html": (2006, "20060105035542", "/portfolio.html", True),
 "p2007.html": (2007, "20070104163444", "/portfolio.html", True), "p2008.html": (2008, "20080106140213", "/portfolio.html", True),
 "p2009.html": (2009, "20090207011919", "/portfolio.html", True),
 "inv2010.html": (2010, "20100701000000", "/investments", False), "inv2011.html": (2011, "20110601000000", "/investments", False),
 "inv2012.html": (2012, "20120601000000", "/investments", False),
 "p2013.html": (2013, "20131013064812", "/portfolio", True), "p2014.html": (2014, "20140106204258", "/portfolio", True),
 "p2015.html": (2015, "20150102132424", "/portfolio", True), "p2015b.html": (2015, "20150701000000", "/portfolio", False),
 "p2016.html": (2016, "20160101143822", "/portfolio", True), "p2016b.html": (2016, "20160701000000", "/portfolio", False),
 "p2017.html": (2017, "20170412032446", "/portfolio", True), "p2017b.html": (2017, "20171101000000", "/portfolio", False),
 "p2018b.html": (2018, "20181201000000", "/portfolio", False),
 "p2019.html": (2019, "20190127193250", "/portfolio", True), "p2019b.html": (2019, "20190701000000", "/portfolio", False),
 "c2020.html": (2020, "20200112190949", "/companies/", True), "c2021.html": (2021, "20210115144729", "/companies/", True),
 "c2022.html": (2022, "20220117040249", "/companies/", True), "c2023.html": (2023, "20230109182727", "/companies/", True),
 "c2024.html": (2024, "20240601000000", "/companies/", False),
}
pat_for = {}
for e in eras:
    pat_for.setdefault(e["path"], []).append(e)
def era_pattern(path, year):
    for e in pat_for.get(path, []):
        if e["from"] <= year <= e["to"]:
            return e["pattern"]
    return None
CARD_RE = re.compile(r'<div class="card company-card">(.*?)<!-- /\.portfolio-card -->', re.S)
def parse_cards(h):
    out = []
    for c in CARD_RE.findall(h):
        def g(p):
            m = re.search(p, c, re.S); return html.unescape(m.group(1)).strip() if m else None
        out.append({"website": g(r'<a target="_blank" href="([^"]+)"'), "logo": g(r'<img src="([^"]+)"'),
                    "description": re.sub(r"\s+", " ", g(r'company-description">\s*(.*?)\s*</div>') or ""),
                    "meta": re.sub(r"\s+", " ", g(r'company-meta">\s*(.*?)\s*</div>') or ""),
                    "blog_slug": g(r'href="(?:https?://(?:www\.)?usv\.com)?/blog/([^"/]+)/?"'),
                    "title_name": g(r'title="Read more about our investment in ([^"]+)"'), "alt_name": g(r'alt="([^"]+) logo"')})
    return out
# section split for 2017 (Current / Exited)
def card_sections(h):
    secs = re.split(r'<h2 class="[^"]*">([^<]+)</h2>', h)
    out = {}
    if len(secs) > 1:
        for i in range(1, len(secs), 2):
            out[secs[i].strip()] = secs[i + 1]
    return out
# 1) name map from the 2019 captures
name_by_blog = {}
for f in ("p2019.html", "p2019b.html"):
    for c in parse_cards(open(SP / f, encoding="utf-8", errors="replace").read()):
        if c["blog_slug"] and (c["title_name"] or c["alt_name"]):
            name_by_blog.setdefault(c["blog_slug"], c["title_name"] or c["alt_name"])
HAND = json.loads((I / "scratch/card-name-map.json").read_text()) if (I / "scratch/card-name-map.json").exists() else {}
def name_from_desc(d):
    m = re.match(r"^(.{2,40}?)(?:'s\b|’s\b| is | are | was | were | helps | makes | builds | provides | enables | empowers | connects | lets | allows | offers | creates | combines | operates | develops | brings | gives | uses | runs | powers | turns | delivers | designs |, | – | - |: )", d)
    return m.group(1).strip() if m else None
parsed = {}   # year -> {(slug,path): row}
labels_2013 = {}   # name -> attrs by year
labels_cards = {}  # name -> {year: meta}
unresolved = []
for f, (year, ts, path, exact) in FILES.items():
    src = SP / f
    if not src.exists():
        print("missing", f); continue
    h = open(src, encoding="utf-8", errors="replace").read()
    shutil.copy(src, RAW / f"{year}-{f}")
    rows = parsed.setdefault(year, {})
    pat = era_pattern(path, year)
    n = 0
    if pat and not (path == "/portfolio" and 2016 <= year <= 2018):
        for m in re.finditer(pat, h):
            d = m.groupdict(); name = html.unescape(d.get("name") or "").strip()
            slug = slug_of(name) if name else d.get("slug")
            if not name and not slug: continue
            rows.setdefault((slug, path), {"slug": slug, "name": name or None, "path": path, "snapshot_ts": ts, **({} if exact else {"ts_approx": True})}); n += 1
    if path == "/portfolio" and 2013 <= year <= 2015:
        for m in re.finditer(r'<div class="([^"]*company-container[^"]*)"([^>]*)>', h):
            cls, attrs = m.group(1), m.group(2)
            a = dict(re.findall(r'(usv[:-][a-z_]+)="([^"]*)"', attrs))
            name = html.unescape(a.get("usv-investment", "")).strip()
            if not name: continue
            labels_2013.setdefault(name, {})[str(year) + ("b" if f.endswith("b.html") else "")] = {
                "series": a.get("usv:investment_series"), "year": a.get("usv:investment_date"), "city": a.get("usv:city"),
                "categories": a.get("usv:investment_categories"), "status_class": "past" if " past" in cls else "current", "snapshot_ts": ts}
    if path == "/portfolio" and 2016 <= year <= 2019:
        secs = card_sections(h)
        for sec, body in (secs.items() if secs else [("", h)]):
            for c in parse_cards(body):
                dom = re.sub(r"^https?://(www\.)?", "", c["website"] or "").split("/")[0].lower()
                name = c["title_name"] or c["alt_name"] or name_by_blog.get(c["blog_slug"] or "") or HAND.get(dom)
                if not name:
                    name = name_from_desc(re.sub(r"<[^>]+>", "", c["description"] or ""))
                    if not name:
                        unresolved.append((year, c["blog_slug"], c["website"], c["description"][:80])); continue
                    unresolved.append((year, c["blog_slug"], c["website"], "DESC->" + name))
                labels_cards.setdefault(name, {})[str(year) + ("b" if f.endswith("b.html") else "")] = {
                    "meta": c["meta"], "section": sec, "website": c["website"], "blog_slug": c["blog_slug"], "snapshot_ts": ts}
                if 2016 <= year <= 2018:
                    slug = slug_of(name)
                    rows.setdefault((slug, path), {"slug": slug, "name": name, "path": path, "snapshot_ts": ts, **({} if exact else {"ts_approx": True})}); n += 1
    print(f"{f}: year {year} path {path} -> {n} rows (year total {len(rows)})")
for year, rows in sorted(parsed.items()):
    out = PARSED / f"{year}.json"
    prev = {(r["slug"], r["path"]): r for r in json.load(open(out))} if out.exists() else {}
    if 2016 <= year <= 2018:
        prev = {k: v for k, v in prev.items() if k[1] != "/portfolio"}
    prev.update(rows)
    out.write_text(json.dumps(sorted(prev.values(), key=lambda r: (r["path"], r["slug"])), indent=1, ensure_ascii=False))
    print(f"wrote {out.name}: {len(prev)} rows")
(SITE / "portfolio-2013-2015.json").write_text(json.dumps({"_readme": "usv.com/portfolio 2013-2015 (Bootstrap site): per-card usv:* attributes — the firm's own entry-round label (usv:investment_series), entry year (usv:investment_date), city and categories, plus the card's current/past class — read from the Internet Archive captures 2013-10-13, 2014-01-06, 2015-01-02 and ~2015-07 by scratch/parse-snapshots.py on 2026-09-05. A first-party stage label as of 2013-2015, scored on the calibration gate before use.", "rows": [{"name": n, "slug": slug_of(n), "by_capture": v} for n, v in sorted(labels_2013.items())]}, indent=1, ensure_ascii=False))
(SITE / "portfolio-2016-2019.json").write_text(json.dumps({"_readme": "usv.com/portfolio 2016-2019 (card site): per-card meta '<round>, <year>' (the firm's own entry-round label and year), section (Current/Exited Investments where the capture had sections), website and the blog-post slug the 'More' button linked, read from the Internet Archive captures 2016-01-01, ~2016-07, 2017-04-12, ~2017-11, ~2018-12, 2019-01-27, ~2019-07 by scratch/parse-snapshots.py on 2026-09-05. Names come from the 2019 captures' title attribute (same blog slug), else the description's leading words or scratch/card-name-map.json.", "rows": [{"name": n, "slug": slug_of(n), "by_capture": v} for n, v in sorted(labels_cards.items())]}, indent=1, ensure_ascii=False))
print("labels_2013 names", len(labels_2013), "| labels_cards names", len(labels_cards))
print("UNRESOLVED / DESC-derived:")
for u in unresolved: print("  ", u)
