#!/usr/bin/env python3
"""Print the round-naming sentences of Perspectives posts (raw pages, gz) or archived news items.
Usage: postgrep.py <substring of slug/title> [...]   (prefix n: searches the archived news instead)"""
import gzip, html as H, json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent; REPO = ROOT.parents[3]
RAW = REPO / "data" / "filings" / "index-ventures" / "perspectives-raw"
CC = REPO / "data" / "filings" / "commoncrawl" / "index-ventures"
posts = [r for r in json.load(open(ROOT / "sources" / "site" / "perspectives.json"))["rows"] if not r.get("missing")]
news = json.load(open(ROOT / "sources" / "wayback" / "news-archive.json"))["rows"]
man = None
RW = re.compile(r"(?i)\b(pre-?seed|seed|series [a-h]\b|first round|second round|growth round|led by|co-led|we led|lead(?:ing)? (?:the|their|its|a)|invest(?:ed|ing|ment|or)|round|valu(?:ed|ation)|acquir|backed|partner(?:ed|ing|ship)? with)")
def text_of(body):
    main = body[body.find('<article role="main"'):] if '<article role="main"' in body else body
    ps = [re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", "", p))).strip() for p in re.findall(r"<(?:p|h2|h3|li)[^>]*>(.*?)</(?:p|h2|h3|li)>", main.split("<footer")[0], flags=re.S)]
    return " ".join(p for p in ps if p)
def rd(p):
    g = Path(str(p) + ".gz")
    return gzip.open(g, "rt", errors="replace").read() if g.exists() else p.read_text(errors="replace")
for a in sys.argv[1:]:
    if a.startswith("n:"):
        sub = a[2:].lower()
        for r in [r for r in news if sub in (r.get("title") or "").lower()][:3]:
            print(f"## NEWS {r.get('date')} {r['title'][:100]}")
            for s in (r.get("round_sentences") or [])[:4]: print("   >", s[:300])
        continue
    hits = [r for r in posts if a.lower() in (r["slug"] + " " + (r.get("title") or "")).lower()]
    for r in hits[:2]:
        t = text_of(rd(RAW / f"{r['slug'][:180]}.html"))
        ss = [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-Z\"“(])", t) if RW.search(s) and "In this post:" not in s and "Facebook Linkedin Share" not in s]
        ss = sorted(ss, key=lambda s: -(len(re.findall(r"(?i)series [a-h]\b|seed|led|index|\$|€|£", s))))[:3]
        print(f"## {r['date']} {r['slug'][:70]} ({len(hits)} hit)")
        for s in ss: print("   >", s[:260])
    if not hits: print("## no post:", a)
