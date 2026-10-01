#!/usr/bin/env python3
"""Index the firm's own WordPress posts (sources/site/raw/posts.json) into sources/site/posts.json:
per post its date, title, URL, categories, the company the title names ("Etched: ..." or
"Meet Glean"), and the sentences that name a round, a lead or an investment, kept whole
(decimals intact: "$5.1M" must not split, COLLECTION.md s5)."""
import html, json, re
from pathlib import Path
HERE = Path(__file__).resolve().parent
RAW = HERE.parent / "sources" / "site" / "raw"
cats = {c["id"]: html.unescape(c["name"]) for c in json.load(open(RAW / "categories.json"))}
ROUND = re.compile(r"\b(pre-seed|seed|series [a-h]\b|round|led|lead|leading|co-led|invest(ed|ing|ment)?|partner(ed|ing)? with|"
                   r"back(ed|ing)|financing|raise[sd]?|fund(ing|ed))\b", re.I)
def text(h):
    h = re.sub(r"<(script|style)[\s\S]*?</\1>", " ", h or "", flags=re.I)
    h = re.sub(r"</(p|h\d|li|div)>", "\n", h, flags=re.I)
    return html.unescape(re.sub(r"<[^>]+>", " ", h))
def sentences(t):
    t = re.sub(r"[ \t\r\f\v]+", " ", t)
    out = []
    for para in t.split("\n"):
        para = para.strip()
        if not para:
            continue
        # split on sentence ends, never inside a decimal ("$5.1M") or an initial ("U.S.")
        out += [s.strip() for s in re.split(r"(?<![0-9A-Z]\.[0-9A-Z])(?<=[.!?])\s+(?=[A-Z\"“])", para) if s.strip()]
    return out
rows = []
for p in json.load(open(RAW / "posts.json")):
    title = html.unescape(p["title"]["rendered"]).strip()
    m = re.match(r"^(?:Meet |Welcoming )?([^:|]+?)(?::| \+ | is joining | \|)", title) or re.match(r"^Meet (.+)$", title)
    company = m.group(1).strip() if m else ""
    body = text(p.get("content", {}).get("rendered", ""))
    rs = [s for s in sentences(body) if ROUND.search(s)][:25]
    rows.append({"date": p["date"][:10], "title": title, "url": p["link"],
                 "categories": [cats.get(c) for c in p.get("categories", [])],
                 "company": company, "round_sentences": rs, "chars": len(body)})
(HERE.parent / "sources" / "site" / "posts.json").write_text(json.dumps({
    "_readme": "The firm's WordPress posts (wp/v2/posts, pulled 2026-09-30), indexed by scratch/post-index.py.",
    "rows": rows}, indent=1, ensure_ascii=False) + "\n")
print(len(rows), "posts;", sum(1 for r in rows if r["round_sentences"]), "with round sentences")
