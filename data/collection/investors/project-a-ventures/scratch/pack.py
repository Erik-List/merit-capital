#!/usr/bin/env python3
"""Evidence pack for the judge, one block per row: the live CMS fields, the archive
fields (Contentful 2020-24, per-company pages 2012-19, listings), the firm's own
posts that name the row (with the sentences naming it), the Google News / TechCrunch /
Crunchbase News headlines the surfaces layer found (round and exit words first),
and the queue item's open needs.

Usage: python3 pack.py slug [slug ...]   |   python3 pack.py --batch N (queue order)
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as J  # noqa: E402

QUEUE = J.H / "queue" / "queue.json"
BASE = {r["slug"]: r for r in json.loads((J.INV / "companies/base.json").read_text())}


def sentences(text, name, n=3):
    out = []
    for s in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", text):
        if re.search(rf"(?<![A-Za-z0-9]){re.escape(name)}(?![A-Za-z0-9])", s, re.I):
            out.append(s.strip()[:300])
        if len(out) >= n:
            break
    return out


def block(slug, item=None):
    b = BASE.get(slug, {})
    name = b.get("name") or slug
    print(f"\n=== {slug} | {name} | first_seen {b.get('first_seen')} | wb {b.get('wayback_years')} | tier {b.get('tier')}")
    if item:
        print("  needs:", item.get("need") or item.get("needs"), "| ev:", item.get("evidence_class"))
    lv = J.live(slug, name)
    if lv:
        print(f"  CMS: invest {lv.get('invest_year')} | round {lv.get('stage_at_entry_site')} | {lv.get('fund_site')} | "
              f"{lv.get('status_site')} | HQ {lv.get('hq_city_site')}, {lv.get('hq_country_site')} | founded {lv.get('founded')} | "
              f"partners {lv.get('partners')} | {lv.get('industries')} | {lv.get('website')}")
        print(f"       {(lv.get('description') or '')[:220]}")
    e = J.ev(slug)
    if e:
        f = e.get("fields") or {}
        keep = ["cf_status", "cf_founded", "cf_investment", "cf_investment_type", "cf_location", "cf_segment",
                "cf_subheadline", "page_investment", "page_founded", "page_location", "page_exit_line",
                "former_flag", "tile_label"]
        bits = []
        for k in keep:
            if f.get(k):
                bits.append(f"{k[3:] if k.startswith('cf_') else k}={' || '.join(list(f[k])[:2])[:120]}")
        print("  ARCH: " + " | ".join(bits))
        if e.get("date_of_investment"):
            print(f"  dateOfInvestment: {e['date_of_investment']['value']} ({e['date_of_investment']['capture_ts'][:8]})")
        print(f"  archive: {e.get('years')}")
    ps = sorted(J.posts_for(slug).items(), key=lambda x: (name.lower() not in x[1]["title"].lower(), x[1]["date"] or "z"))
    for k, p in ps[:5]:
        ss = sentences(p["text"], name) or [p["text"][:200]]
        print(f"  POST {p['date'] or '?':10} {k[:60]} | {p['title'][:90]}")
        for s in ss[:1]:
            print(f"       > {s[:240]}")
    g = J.SURF.get(slug) or {}
    heads = []
    for svc, v in (g.get("surfaces") or {}).items():
        for i in v.get("items") or []:
            if i.get("names") or svc == "googlenews_firm":
                heads.append((bool(i.get("rounds") or i.get("amounts")), i.get("date", "")[:10], svc, i))
    heads.sort(key=lambda x: (not x[0], x[1]))
    for has, d, svc, i in heads[:9]:
        gid = (i.get("gid") or i.get("url") or "")[-10:]
        print(f"  NEWS {d} {svc[:10]:10} [{gid}] {i.get('source', '')[:18]:18} {i.get('title', '')[:130]}")
    for s in g.get("siblings") or []:
        print(f"  SIBLING {s.get('investor')}: stage {s.get('entry_stage')} ({s.get('entry_stage_source')}) {s.get('entry_date','')} grad {s.get('seed_to_a_graduation','')} | {(s.get('note') or '')[:140]}")
    if item:
        for k in ("formd_graduation", "graduation_evidence", "site_entry_stage", "site_invest_year", "entry_date"):
            if item.get(k):
                print(f"  item.{k}: {json.dumps(item[k], ensure_ascii=False)[:300]}")


def main():
    args = sys.argv[1:]
    q = json.loads(QUEUE.read_text()) if QUEUE.exists() else []
    items = q.get("items", q) if isinstance(q, dict) else q
    by = {i["slug"]: i for i in items} if isinstance(items, list) else {}
    if args and args[0] == "--batch":
        n = int(args[1]); size = int(args[2]) if len(args) > 2 else 15
        slugs = [i["slug"] for i in items][n * size:(n + 1) * size]
    else:
        slugs = args
    for s in slugs:
        block(s, by.get(s))


if __name__ == "__main__":
    main()
