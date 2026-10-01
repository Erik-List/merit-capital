#!/usr/bin/env python3
"""Evidence pack for the judge and the research agents, one block per row:
the base row, the firm's archived fields (stage and thesis by capture, deal
partners, the firm's own sentence, the press links the firm attached to the
company page), the firm's own posts naming the row, the Google News headlines
the surfaces layer found, the sibling books' rows, and the queue item's needs.

Usage: python3 pack.py slug [slug ...]   |   python3 pack.py --group N
"""
import json
import re
import sys
from pathlib import Path

H = Path(__file__).resolve().parent
INV = H.parent


def _load(p, default):
    p = Path(p)
    return json.loads(p.read_text()) if p.exists() else default


BASE = {r["slug"]: r for r in _load(INV / "companies/base.json", [])}
EV = _load(INV / "sources/wayback/archive-evidence.json", {"companies": {}})["companies"]
PRESS = _load(INV / "sources/site/press-archive.json", {"posts": {}, "by_company": {}})
SIB = _load(H / "siblings.json", {})
SURF = _load(H / "graduation-surfaces.json", {})
LIVE = {re.sub(r"[^a-z0-9]+", "-", r["name"].lower()).strip("-"): r
        for r in _load(INV / "sources/site/companies-2026.json", {"rows": []})["rows"]}
GROUPS = _load(H / "research-groups.json", {})
_q = _load(H / "queue/queue.json", [])
_items = _q.get("items", _q) if isinstance(_q, dict) else _q
QUEUE = {i["slug"]: i for i in _items} if isinstance(_items, list) else {}


def ev_for(slug, name):
    if slug in EV:
        return EV[slug]
    k = re.sub(r"[^a-z0-9]", "", name.lower())
    for s, e in EV.items():
        if re.sub(r"[^a-z0-9]", "", e["name"].lower()) == k:
            return e
    return {}


def sentences(text, name, n=2):
    out = []
    for s in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9“\"])", text):
        if re.search(rf"(?<![A-Za-z0-9]){re.escape(name)}(?![A-Za-z0-9])", s, re.I):
            out.append(s.strip()[:320])
        if len(out) >= n:
            break
    return out


def block(slug):
    b = BASE.get(slug, {})
    name = b.get("name") or slug
    item = QUEUE.get(slug) or {}
    print(f"\n=== {slug} | {name} | first_seen {b.get('first_seen')} | archive years {b.get('wayback_years')} | tier {b.get('tier')}")
    if item:
        print(f"  needs: {item.get('need') or item.get('needs')} | evidence_class: {item.get('evidence_class')}")
    if b.get("partners_formd") or b.get("formd_span"):
        print(f"  FORM D: persons {b.get('partners_formd')} | span {b.get('formd_span')} | max round {b.get('formd_max_round_usd')} | {str(b.get('formd_links'))[:200]}")
    if b.get("edgar_forms"):
        print(f"  EDGAR: {b.get('edgar_forms')} {b.get('edgar_span')} CIK {b.get('edgar_cik')}")
    lv = LIVE.get(slug)
    if lv:
        print(f"  LIVE SITE 2026: shown on {lv['surfaces']} | {lv.get('website')}")
    e = ev_for(slug, name)
    if e:
        st = "; ".join(f"{k} ({min(v)}..{max(v)})" for k, v in e["stages"].items())
        th = ", ".join(e["theses"])
        pa = ", ".join(e["partners"])
        print(f"  ARCHIVE: first {e['first_capture'][:8]} last {e['last_capture'][:8]} | surfaces {list(e['surfaces'])}")
        print(f"           site stage field: {st or '-'} | thesis: {th or '-'} | deal partners: {pa or '-'}")
        print(f"           site: {', '.join(e['websites'][:2]) or '-'} | firm page slug: {', '.join(e['cms_slugs']) or '-'}")
        if e.get("intro"):
            print(f"           firm says: {e['intro'][:260]}")
        print(f"           first capture URL: {e['first_capture_url']}")
        for i in e.get("insights", [])[:6]:
            print(f"           LINKED {i.get('date')} {i.get('title', '')[:90]} | {i.get('external') or i.get('uri')}")
    for ps in (PRESS["by_company"].get(slug) or [])[:6]:
        p = PRESS["posts"][ps]
        ss = sentences(p["text"], name) or [p["text"][:200]]
        print(f"  FIRM POST {p['date'] or '?':10} {p['title'][:90]} | {p['capture_url']}")
        print(f"       > {ss[0][:300]}")
    g = SURF.get(slug) or {}
    heads = []
    for svc, v in (g.get("surfaces") or {}).items():
        for i in v.get("items") or []:
            if i.get("names") or svc == "googlenews_firm":
                heads.append((bool(i.get("rounds") or i.get("amounts")), i.get("date", "")[:10], svc, i))
    heads.sort(key=lambda x: (not x[0], x[1]))
    for has, d, svc, i in heads[:9]:
        print(f"  NEWS {d} {svc[:12]:12} {i.get('source', '')[:18]:18} {i.get('title', '')[:130]}")
    for s in SIB.get(slug) or []:
        usd = f" ${float(s['valuation_usd'])/1e9:.2f}B asof {s['valuation_asof']} cite {s['valuation_citation']}" if s.get("valuation_usd") else ""
        print(f"  SIBLING {s['investor']} ({s['name']}): {s['status']} / {s['valuation_range']}{usd} | HQ {s['hq_city']}, {s['hq_country']} | {s['focus']} | their entry {s['entry_stage']} {s['entry_date']} | {(s.get('note') or '')[:260]}")
    for k in ("formd_graduation", "graduation_evidence", "hq_country_claim", "acquirer", "formd_band_withheld"):
        if item.get(k):
            print(f"  item.{k}: {json.dumps(item[k], ensure_ascii=False)[:300]}")


def main():
    args = sys.argv[1:]
    if args and args[0] == "--group":
        slugs = GROUPS[args[1]]
    else:
        slugs = args
    for s in slugs:
        block(s)


if __name__ == "__main__":
    main()
