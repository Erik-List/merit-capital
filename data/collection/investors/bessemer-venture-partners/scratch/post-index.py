#!/usr/bin/env python3
"""Index the firm's own posts from the Sanity export (sources/site/sanity/: memo, newsArticle, researchPost) into
sources/site/posts.json: per post its date, title, subtitle, URL, kind, the companies the CMS associates with it,
and the sentences that name a round, a lead or an investment, kept whole (decimals intact: "$5.1M" must not split,
COLLECTION.md s5). Memos are the firm's own investment recommendations, published years later (bvp.com/memos)."""
import json, re
from pathlib import Path
HERE = Path(__file__).resolve().parent
S = HERE.parent / "sources" / "site"
L = lambda t: json.loads((S / "sanity" / f"{t}.json").read_text())["result"]
cid = {c["_id"]: c["name"].strip() for c in L("company")}
ROUND = re.compile(r"\b(pre-seed|seed|series [a-h]\b|round|led|lead|leading|co-led|invest(ed|ing|ment|or)?|partner(ed|ing)? with|"
                   r"back(ed|ing)|financing|raise[sd]?|fund(ing|ed)|valuation|pre-money|post-money)\b", re.I)
def text(blocks):
    out = []
    for b in blocks or []:
        if isinstance(b, dict) and b.get("_type") == "block":
            out.append("".join(ch.get("text", "") for ch in b.get("children") or []))
    return "\n".join(out)
def sentences(t):
    t = re.sub(r"[ \t\r\f\v]+", " ", t)
    out = []
    for para in t.split("\n"):
        para = para.strip()
        if para:
            out += [s.strip() for s in re.split(r"(?<![0-9A-Z]\.[0-9A-Z])(?<=[.!?])\s+(?=[A-Z\"“])", para) if s.strip()]
    return out
rows = []
for kind, seg in (("memo", "memos"), ("newsArticle", "news"), ("researchPost", "atlas")):
    for p in L(kind):
        slug = (p.get("slug") or {}).get("current")
        body = text(p.get("body"))
        hdr = p.get("header") or {}
        head = " ".join(str(hdr.get(k) or "") for k in ("date", "from", "re"))
        sub = p.get("subtitle") or ""
        rs = [s for s in sentences((sub + "\n" if sub else "") + body) if ROUND.search(s)][:30]
        rows.append({"date": (p.get("publishedAt") or p.get("_createdAt") or "")[:10], "kind": kind, "title": (p.get("title") or "").strip(),
                     "subtitle": sub, "url": f"https://www.bvp.com/{seg}/{slug}", "slug": slug,
                     "companies": [cid[a["_ref"]] for a in p.get("associatedCompanies") or [] if a.get("_ref") in cid],
                     "memo_header": head.strip() or None, "round_sentences": rs, "chars": len(body)})
rows.sort(key=lambda r: r["date"])
(S / "posts.json").write_text(json.dumps({
    "_readme": "The firm's own posts (bvp.com memos, news and Atlas research), read 2026-10-01 from the site's Sanity dataset and indexed by scratch/post-index.py.",
    "rows": rows}, indent=1, ensure_ascii=False) + "\n")
print(len(rows), "posts;", sum(1 for r in rows if r["round_sentences"]), "with round sentences;", sum(1 for r in rows if r["companies"]), "with associated companies")
