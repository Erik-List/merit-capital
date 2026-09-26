#!/usr/bin/env python3
"""One evidence view per base row, for the judge (the Cherry / Atomico pattern).

Joins what this run built outside the shared pipeline — the live card, the
firm's news posts, the UK officer graph, the EDGAR full-text hits, the
Wikipedia sentences — to the base rows by name, and writes
scratch/evidence-pack.json keyed by slug.

Usage: python3 evidence-pack.py
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

P = Paths("balderton-capital")
SUFFIX = r"\b(inc|ltd|limited|gmbh|ab|oy|sa|sas|bv|plc|llc|corp|corporation|co|group|holdings|technologies|technology|software|international|global|labs|the)\b\.?"


def norm(s: str) -> str:
    s = (s or "").lower().replace("&", "and")
    s = re.sub(SUFFIX, "", s)
    return re.sub(r"[^a-z0-9]+", "", s)


def load(p: Path, default):
    return json.loads(p.read_text()) if p.exists() else default


def main():
    base = load(P.base_json, [])
    cards = {norm(r["name"]): r for r in load(P.site / "companies-facetwp.json", {"rows": []})["rows"]}
    posts = load(P.site / "news.json", {"posts": []})["posts"]
    graph = load(P.sources / "registers" / "companies-house" / "officer-graph.json", [])
    fts = load(P.edgar / "fts-hits.json", {"registrants": []})["registrants"]
    wiki = load(P.web / "wikipedia-insource.json", {})
    arts = wiki.get("articles") or wiki.get("rows") or []
    seats = {}
    for s in graph:
        seats.setdefault(norm(s["company"]), []).append(s)
    pack = {}
    for row in base:
        k = norm(row["name"])
        if not k:
            continue
        v = {}
        c = cards.get(k)
        if c:
            v["card"] = {f: c.get(f) for f in ("round_label", "stage_site", "invest_year", "status_site",
                                               "location_text", "sectors", "description", "website")}
        rel = []
        name_re = re.compile(r"(?<![a-z0-9])" + re.escape(row["name"].lower()) + r"(?![a-z0-9])")
        for p in posts:
            if norm(p.get("lead_name") or "") == k or (len(k) > 3 and name_re.search(p["title"].lower())):
                rel.append({"date": p["date"], "title": p["title"], "url": p["url"],
                            "round_words": p.get("round_words"), "amounts": p.get("amounts"),
                            "excerpt": p.get("excerpt", "")[:400]})
        rel.sort(key=lambda p: p["date"])
        if rel:
            v["posts"] = rel
        st = seats.get(k) or []
        if not st and len(k) > 5:
            for kk, vv in seats.items():
                if kk.startswith(k) or k.startswith(kk) and len(kk) > 5:
                    st = vv
                    break
        if st:
            v["uk_seats"] = [{"partner": s["partner"], "company": s["company"], "number": s["number"],
                              "status": s["status"], "appointed": s["appointed"], "resigned": s["resigned"],
                              "office": s["office_addr"]} for s in st]
        f_hits = []
        for r in fts:
            if r["bucket"] not in ("third_party", "ownership_forms"):
                continue
            if norm(r["registrant"].split("  (")[0]) == k:
                ctx = []
                for sn in r.get("snippets") or []:
                    ctx += sn.get("context") or []
                f_hits.append({"registrant": r["registrant"], "first": r["first_date"], "last": r["last_date"],
                               "forms": r["forms"], "bucket": r["bucket"],
                               "urls": [f["index"] for f in r["filings"][:3]],
                               "context": [re.sub(r"\s+", " ", x)[:400] for x in ctx[:3]]})
        if f_hits:
            v["fts"] = f_hits
        w = []
        for a in arts:
            if (a.get("base_slug") == row["slug"]) or norm(re.sub(r"\s*\(.*?\)$", "", a.get("title", ""))) == k:
                w.append({"title": a.get("title"), "sentences": (a.get("sentences") or a.get("snippets") or [])[:3],
                          "url": a.get("url")})
        if w:
            v["wikipedia"] = w
        if v:
            pack[row["slug"]] = v
    write_atomic(HERE / "evidence-pack.json", json.dumps(pack, indent=1, ensure_ascii=False) + "\n")
    n = len(pack)
    print(f"evidence pack: {n} of {len(base)} rows carry extra evidence "
          f"(card {sum('card' in v for v in pack.values())}, posts {sum('posts' in v for v in pack.values())}, "
          f"uk seats {sum('uk_seats' in v for v in pack.values())}, fts {sum('fts' in v for v in pack.values())}, "
          f"wikipedia {sum('wikipedia' in v for v in pack.values())})")


if __name__ == "__main__":
    main()
