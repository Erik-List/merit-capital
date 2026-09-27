#!/usr/bin/env python3
"""One evidence view per base row for the Headline judge (the Cherry / Atomico /
Balderton pattern): joins what this run built outside the shared pipeline to the
base rows by name and writes scratch/evidence-pack.json keyed by slug.

Joined: the Sanity CMS doc (fund pages, the firm's dated entries, outcome line,
location, founders, website, partners), the firm's own posts (60 CMS blog docs
2021-2026 with body text, 23 Substack posts) with the sentences that name the
company, the EDGAR full-text registrants, the Wikipedia insource sentences, and
the BV Capital archive rows (bvcapital.com 2008-2010 via Common Crawl)."""
from __future__ import annotations

import json
import re
import sys
import urllib.parse
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

P = Paths("headline")
SUFFIX = r"\b(inc|ltd|limited|gmbh|ag|ab|oy|sa|sas|bv|plc|llc|corp|corporation|co|kk|k\.k|the)\b\.?"
ROUND = re.compile(r"(pre-seed|seed|series [a-h]\b|growth round|secondary|tender|\$[\d.,]+ ?[mb]\b|€[\d.,]+ ?[mb]\b|[\d.,]+ ?(million|billion))", re.I)


def norm(s: str) -> str:
    s = (s or "").lower().replace("&", "and")
    s = re.sub(SUFFIX, "", s)
    return re.sub(r"[^a-z0-9]+", "", s)


def load(p: Path, default):
    return json.loads(p.read_text()) if p.exists() else default


def blocks_text(o) -> str:
    out = []

    def walk(x):
        if isinstance(x, dict):
            if x.get("_type") == "span" and x.get("text"):
                out.append(x["text"])
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    walk(o)
    return " ".join(out)


def main():
    base = load(P.base_json, [])
    cms = {}
    for r in load(P.site / "sanity-companies.json", {"rows": []})["rows"]:
        cms.setdefault(norm(r["name"]), r)
    posts = []
    for b in load(P.site / "sanity" / "blogPost.json", {"result": []})["result"]:
        slug = (b.get("slug") or {}).get("current")
        q = urllib.parse.quote(f'*[_type=="blogPost" && _id=="{b["_id"]}"]')
        posts.append({"date": b.get("date", "")[:10], "title": b.get("title", ""),
                      "url": (f"https://headline.com/founders/{slug}/" if slug else
                              f"https://iznipsfw.apicdn.sanity.io/v2021-10-21/data/query/production?query={q}"),
                      "text": blocks_text(b.get("flexibleContent"))})
    for s in load(P.site / "substack-archive.json", {"posts": []})["posts"]:
        posts.append({"date": (s.get("post_date") or "")[:10], "title": s.get("title") or "",
                      "url": s.get("canonical_url") or "", "text": " ".join(filter(None, [s.get("subtitle"), s.get("description")]))})
    fts = load(P.edgar / "fts-hits.json", {"registrants": []}).get("registrants", [])
    wiki = load(P.web / "wikipedia-insource.json", {})
    arts = wiki.get("articles") or wiki.get("rows") or []
    bv = {}
    for f in sorted((P.wayback / "parsed").glob("*.json")):
        for r in json.loads(f.read_text()):
            bv.setdefault(norm(r["name"]), []).append({"year": f.stem, "capture": r.get("capture_url"), "desc": r.get("description")})

    pack = {}
    for row in base:
        k = norm(row["name"])
        keys = {k} | {norm(n) for n in re.split(r"\s*[(/]\s*", row["name"]) if n}
        v = {}
        c = next((cms[x] for x in keys if x in cms), None)
        if c:
            v["cms"] = {x: c[x] for x in ("surface", "desks", "stages", "outcome", "subline", "location",
                                          "website", "partners", "description", "url", "hidden")}
        hits = []
        name_re = re.compile(r"\b" + re.escape(row["name"].split(" (")[0]) + r"\b", re.I)
        for p in posts:
            if name_re.search(p["title"]) or name_re.search(p["text"]):
                sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-Z])", p["text"])
                         if name_re.search(s) and ROUND.search(s)][:3]
                hits.append({"date": p["date"], "title": p["title"], "url": p["url"], "sentences": sents})
        if hits:
            v["posts"] = hits[:6]
        def reg_key(x):
            return norm(re.sub(r"\s*\(.*$", "", x.get("registrant") or ""))
        f = [x for x in fts if x.get("bucket") == "third_party"
             and any(len(kk) >= 4 and (reg_key(x) == kk or reg_key(x).startswith(kk) and len(reg_key(x)) - len(kk) <= 8)
                     for kk in keys)]
        if f:
            v["fts"] = [{"registrant": x["registrant"], "forms": x.get("forms"), "first": x.get("first_date"),
                         "context": [c for s in (x.get("snippets") or [])[:2] for c in (s.get("context") or [])[:1]],
                         "url": ((x.get("snippets") or [{}])[0]).get("url")}
                        for x in f]
        w = [a for a in arts if norm(a.get("title", "")) in keys]
        if w:
            v["wikipedia"] = [{"title": a.get("title"), "sentences": (a.get("sentences") or [])[:2]} for a in w]
        b = [x for kk in keys for x in bv.get(kk, [])]
        if b:
            v["bvcapital"] = sorted({x["year"] for x in b})
        pack[row["slug"]] = v
    write_atomic(HERE / "evidence-pack.json", json.dumps(pack, indent=1, ensure_ascii=False) + "\n")
    print(f"{len(pack)} rows; cms {sum('cms' in v for v in pack.values())}, posts {sum('posts' in v for v in pack.values())}, "
          f"fts {sum('fts' in v for v in pack.values())}, wiki {sum('wikipedia' in v for v in pack.values())}, bv {sum('bvcapital' in v for v in pack.values())}")


if __name__ == "__main__":
    main()
