#!/usr/bin/env python3
"""One evidence view per base row, for the judge (the Cherry pattern).

run.py's queue items carry the base row's own fields; everything this run
built outside the shared pipeline (the CMS record, the firm's posts, the UK
register layers, the full-text hits) is joined here by name and written to
scratch/evidence-pack.json, keyed by slug, plus a compact text rendering per
batch for reading.

Usage: python3 evidence-pack.py            (all base rows)
       python3 evidence-pack.py --batch N  (render the rows of queue batch N)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

P = Paths("atomico")
ROUND_RE = re.compile(r"(?i)\b(pre-?seed|seed|series [a-h]\b(?: extension)?|growth round|"
                      r"\$[\d.,]+ ?(?:m|mn|million|bn|b|billion)\b|€[\d.,]+ ?(?:m|million|bn)|"
                      r"£[\d.,]+ ?(?:m|million|bn)|led by|co-led|leading|lead(?:s|ing)? (?:the|its|their)|"
                      r"first invest|initial investment|we invested|backed .{0,40} in 20\d\d)")


def norm(s: str) -> str:
    s = (s or "").lower()
    s = re.sub(r"\b(inc|ltd|limited|gmbh|ab|oy|sa|sas|bv|plc|llc|corp|corporation|co)\b\.?", "", s)
    return re.sub(r"[^a-z0-9]+", "", s)


def load(p: Path, default):
    return json.loads(p.read_text()) if p.exists() else default


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", type=int)
    args = ap.parse_args()
    base = load(P.base_json, [])
    cms = {norm(r["name"]): r for r in load(P.site / "cms-partners.json", {"rows": []})["rows"]}
    cms_slug = {r["slug"]: r for r in load(P.site / "cms-partners.json", {"rows": []})["rows"]}
    board = {norm(r["name"]): r for r in load(P.site / "jobboard-companies.json", {"rows": []})["rows"]}
    posts = load(P.site / "insights.json", {"rows": []})["rows"]
    graph = load(P.sources / "registers" / "companies-house" / "officer-graph.json", {"people": {}})
    bt = load(P.sources / "registers" / "companies-house" / "backtrace.json", {"companies": {}})["companies"]
    uk_map = {k: v[0] for k, v in load(P.sources / "registers" / "companies-house" / "company-map.json",
                                       {"map": {}})["map"].items()}
    fts = load(P.edgar / "fts-hits.json", {"registrants": []})["registrants"]
    older = load(P.site / "archive-eras.json", {"rows": []})["rows"]
    older_by = {}
    for r in older:
        older_by.setdefault(norm(r["name"]), []).append(r)

    seats_by_num = {}
    for person in graph["people"].values():
        for s in person["seats"]:
            if s.get("firm_entity"):
                continue
            seats_by_num.setdefault(s["company_number"], []).append(
                {"person": person["name"], "appointed": s["appointed"], "resigned": s["resigned"],
                 "firm_address": s["firm_address"], "company": s["company_name"],
                 "status": s["company_status"]})

    pack = {}
    for row in base:
        k = norm(row["name"])
        keys = {k} | {norm(x) for x in (row.get("aliases") or [])}
        c = cms.get(k) or cms_slug.get(row["slug"])
        rel_posts = []
        for p in posts:
            hay = " ".join([p.get("title") or "", " ".join(p.get("partners_linked") or [])]).lower()
            if (c and c["slug"] in (p.get("partners_linked") or [])) or \
                    re.search(r"\b" + re.escape(row["name"].lower()) + r"\b", hay):
                snip = [m.group(0) for m in ROUND_RE.finditer(p.get("text") or "")][:8]
                rel_posts.append({"title": p.get("title"), "date": p.get("date"), "url": p.get("url"),
                                  "capture": p.get("capture"), "round_words": snip})
        num = uk_map.get(row["slug"])
        f_hits = []
        for r in fts:
            if r.get("bucket") != "third_party":
                continue
            if k and (k in norm(r["registrant"]) or any(k in norm(" ".join(s.get("context") or []))
                                                       for s in r.get("snippets") or [])):
                f_hits.append({"registrant": r["registrant"], "first": r["first_date"],
                               "forms": r["forms"],
                               "context": [c2[:300] for s in r.get("snippets") or []
                                           for c2 in (s.get("context") or [])
                                           if k in norm(c2)][:2]})
        pack[row["slug"]] = {
            "name": row["name"], "first_seen": row.get("first_seen"),
            "wayback_years": row.get("wayback_years"), "site_url": row.get("site_url"),
            "cms": ({x: c.get(x) for x in ("invest_year", "lead", "stage_site", "status_site",
                                            "location_site", "themes", "website", "pretitle",
                                            "subtitle", "url", "capture", "years_listed")}
                    | {"body": (c.get("body") or "")[:500],
                       "news": [n.get("title") for n in c.get("news") or []]}) if c else None,
            "board": board.get(k),
            "older_eras": older_by.get(k),
            "posts": rel_posts,
            "uk_register": ({"number": num, **{x: (bt.get(num) or {}).get(x) for x in
                                               ("first_named", "last_not_named")},
                             "profile": (bt.get(num) or {}).get("profile"),
                             "seats": seats_by_num.get(num)} if num else None),
            "fts": f_hits,
            "edgar": {x: row.get(x) for x in ("edgar_forms", "edgar_links", "formd_links",
                                              "partners_formd", "formd_span", "formd_max_round_usd")
                      if row.get(x)},
        }
    write_atomic(HERE / "evidence-pack.json", json.dumps(pack, indent=1, ensure_ascii=False) + "\n")
    print(f"evidence pack: {len(pack)} rows; cms {sum(1 for v in pack.values() if v['cms'])}, "
          f"posts {sum(1 for v in pack.values() if v['posts'])}, "
          f"uk {sum(1 for v in pack.values() if v['uk_register'])}, "
          f"fts {sum(1 for v in pack.values() if v['fts'])}")
    if args.batch:
        b = json.loads((P.queue / f"batch-{args.batch:03d}.json").read_text())
        out = []
        for it in b:
            v = pack.get(it["slug"], {})
            out.append(f"### {it['slug']} | {v.get('name')} | need {it.get('need')}")
            out.append(json.dumps({k2: v2 for k2, v2 in v.items() if v2 not in (None, [], {}, "")},
                                  ensure_ascii=False)[:2500])
        (HERE / f"evidence-batch-{args.batch:03d}.txt").write_text("\n".join(out))
        print(f"rendered batch {args.batch}: {len(b)} rows -> evidence-batch-{args.batch:03d}.txt")


if __name__ == "__main__":
    main()
