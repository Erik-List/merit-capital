#!/usr/bin/env python3
"""The firm's own round statements per company: every sentence in ICONIQ's posts
(sources/site/posts.json, live site; plus the archived growth posts in
scratch/cc-raw) that names the company and a round word, a lead, an amount or a
valuation. Read-only; feeds the judge (a firm post is class 1 for the round it
names, and asserts an ENTRY only where it says so in words, COLLECTION.md 6).
Usage: python3 .../scratch/post-rounds.py <name> [<name> ...]
"""
import html as H, json, re, sys
from pathlib import Path
INV = Path(__file__).resolve().parents[1]
ROUND = re.compile(r"(Series [A-K]\b|seed round|pre-seed|growth round|funding round|financing|\bled\b|co-led|co-lead|leading (?:the|their|its)|valuation|first invested|initial investment|first partnered|partnered with [A-Z][^ ]* since|since 20\d\d|tender|secondary)", re.I)


def posts():
    for p in json.load(open(INV / "sources/site/posts.json"))["posts"]:
        yield p.get("date", ""), p["url"], p.get("title", ""), p.get("text", "")
    raw = INV / "scratch/cc-raw"
    seen = set()
    for meta in sorted(raw.glob("*/*.json")):
        m = json.loads(meta.read_text())
        u = m["url"]
        if not re.search(r"/growth/(updates|insights)/|iconiqgrowth\.com/[a-z0-9-]{12,}/?$", u) or u in seen:
            continue
        seen.add(u)
        h = meta.with_suffix(".html").read_text(errors="replace")
        h = re.sub(r"<script.*?</script>|<style.*?</style>", " ", h, flags=re.S)
        t = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", h)))
        yield m["timestamp"][:8], u, "", t


def main():
    names = sys.argv[1:]
    allposts = list(posts())
    for name in names:
        pat = re.compile(r"\b" + re.escape(name) + r"\b", re.I)
        print(f"==== {name}")
        seen = set()
        for date, url, title, text in allposts:
            if not pat.search(title + " " + text):
                continue
            sents = re.split(r"(?<=[.!?])\s+(?=[A-Z])", text)
            for s in sents:
                if not (pat.search(s) and ROUND.search(s)) or len(s) > 600:
                    continue
                k = re.sub(r"\W+", "", s.lower())[:120]
                if k in seen:
                    continue
                seen.add(k)
                print(f"  [{date}] {s[:300]}  <{url}>")


if __name__ == "__main__":
    main()
