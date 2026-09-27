#!/usr/bin/env python3
"""Flatten BCV's own insight posts (Sanity `insights`, 346) to text and index
which portfolio companies each one names, with the round sentences, into
scratch/insights-pack.json. The firm's own announcement is class 1 for the
round it NAMES (COLLECTION.md 6: an announcement asserts an ENTRY only where
it says so in words), so the pack keeps the sentences, not a verdict.
"""
import json, re
from pathlib import Path

B = Path(__file__).resolve().parent.parent
rows = json.loads((B / "sources/site/sanity-insights.json").read_text())["rows"]
comps = json.loads((B / "sources/site/company-pages.json").read_text())["rows"]
cats = {d["_id"]: (d.get("title") or d.get("name")) for d in
        json.loads((B / "sources/site/sanity-stages.json").read_text())["rows"]}
ROUND = re.compile(r"\b(pre-seed|seed|series [a-h]\b|series [a-h]-?\d|growth|led|lead|co-led|invest(ed|ing|ment)|round|raise[sd]?|funding)\b", re.I)

def text(post):
    out = []
    for b in post.get("blogBuilder") or []:
        if b.get("_type") == "block":
            out.append("".join(c.get("text", "") for c in b.get("children") or []))
        elif b.get("_type") == "quote":
            out.append(str(b.get("text") or ""))
    return "\n".join(x for x in out if x.strip())

posts = []
for p in rows:
    body = text(p)
    posts.append({"id": p["_id"], "title": p.get("title") or "", "slug": (p["slug"].get("current") if isinstance(p.get("slug"), dict) else p.get("slug")) or "",
                  "date": p.get("publishDate") or (p.get("_createdAt") or "")[:10],
                  "category": [cats.get(c.get("_ref")) for c in (p.get("category") or []) if isinstance(c, dict)],
                  "body": body})
idx = {}
for c in comps:
    name = c["name"]
    base = re.sub(r"\s*\(.*?\)\s*", " ", name).strip()
    if len(base) < 3:
        continue
    pat = re.compile(r"(?<![A-Za-z0-9])" + re.escape(base) + r"(?![A-Za-z0-9])", re.I if len(base) > 5 else 0)
    hits = []
    for p in posts:
        blob = p["title"] + "\n" + p["body"]
        if not pat.search(blob):
            continue
        sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-Z])", blob) if pat.search(s) and ROUND.search(s)]
        hits.append({"title": p["title"], "date": p["date"], "url": f"https://baincapitalventures.com/insight/{p['slug']}/",
                     "in_title": bool(pat.search(p["title"])), "sentences": sents[:6]})
    if hits:
        idx[c["slug"]] = sorted(hits, key=lambda h: (not h["in_title"], h["date"]))[:8]
(B / "scratch/insights-pack.json").write_text(json.dumps(idx, indent=1, ensure_ascii=False) + "\n")
(B / "sources/site/insights-text.json").write_text(json.dumps({"_readme": "Flattened by scratch/insights-pack.py from sanity-insights.json.", "rows": posts}, indent=1, ensure_ascii=False) + "\n")
print(len(idx), "companies named in", len(posts), "posts;", sum(1 for v in idx.values() if any(h["in_title"] for h in v)), "in a title")
