#!/usr/bin/env python3
"""Compact judge cards for one queue batch: the queue item's own evidence plus
what General Catalyst's other sources say about the row (the grid card and
company page, the /list entry, the firm's posts, the Form D rounds, the
sibling books, Wikipedia). Read-only.

Usage: python3 data/collection/investors/general-catalyst/scratch/cards.py <batch-file|all> [slug ...]
       --full adds the post sentences
"""
import json
import re
import sys
from pathlib import Path

INV = Path(__file__).resolve().parents[1]
FULL = "--full" in sys.argv


def load(p, key=None, default=None):
    try:
        d = json.load(open(p))
    except (OSError, ValueError):
        return default if default is not None else {}
    return d.get(key, d) if key and isinstance(d, dict) else d


def nkey(n):
    n = (n or "").lower()
    n = re.sub(r"\(.*?\)", " ", n)
    n = re.sub(r"[^a-z0-9 ]+", " ", n)
    return re.sub(r"\s+", "", n)


UNION = load(INV / "sources/site/companies.json", default=[])
BY_NAME = {}
for r in UNION:
    BY_NAME.setdefault(nkey(r["name"]), r)
GRID = {r["slug"]: r for r in load(INV / "sources/site/company-pages.json", "rows", [])}
POSTS = load(INV / "scratch/posts-by-company.json")
SIB = load(INV / "scratch/siblings.json")
WIKI = {}
for a in load(INV / "sources/web/wikipedia-insource.json", "articles", []):
    if a.get("in_base") and a.get("sentences"):
        WIKI.setdefault(a["in_base"], []).append((a["url"], a["sentences"][0]))
PRE = load(INV / "scratch/judge/prefill.json")
BASE = {r["slug"]: r for r in load(INV / "companies/base.json", default=[])}


def short(s, n=160):
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    return s if len(s) <= n else s[: n - 1] + "…"


def site_row(it):
    return BY_NAME.get(nkey(it["name"])) or {}


def card(it):
    out = []
    s = site_row(it)
    g = GRID.get(s.get("grid_slug") or "") or (GRID.get(s.get("slug") or "") if "company-pages" in (s.get("lists") or []) else {})
    need = ",".join(x[:4] for x in it["need"])
    head = f"## {it['slug']} | {it['name']} | {it['evidence_class']} | need {need}"
    if g:
        fl = "".join(k for k, f in (("A", "flag_active"), ("I", "flag_ipo"), ("Q", "flag_acquired"),
                                      ("C", "flag_creation"), ("V", "flag_cvf"), ("S", "flag_seed")) if g.get(f))
        dom = re.sub(r"^https?://(www\.)?", "", g.get("company_site") or "").strip("/")
        head += (f" | GRID since={g.get('backed_since') or '-'} flags={fl or '-'} {g.get('region') or '-'}"
                 f" inv={', '.join(g.get('partners')[:3]) or '-'} | {'/'.join(g.get('sectors')[:2])} | {dom}")
    out.append(head)
    if s.get("legal_name"):
        extra = " ".join(f"{k}={s[k]}" for k in ("ticker", "former_name", "alias", "token", "vehicle_tag", "held_via") if s.get(k))
        out.append(f"   LIST: {s['legal_name']}" + (f" [{extra}]" if extra else ""))
    elif "company-pages" in (s.get("lists") or []):
        out.append("   LIST: (not on /list)")
    if g and g.get("description"):
        out.append("   desc: " + short(g["description"], 110))
    pr = PRE.get(it["slug"]) or {}
    if pr:
        out.append("   PROP " + short(json.dumps(pr), 200))
    ev = []
    b = BASE.get(it["slug"]) or {}
    if it.get("edgar_forms"):
        ev.append(f"edgar {it['edgar_forms']} first {b.get('first_seen') or ''}")
    if it.get("partners_formd"):
        ev.append(f"formd[{short(it['partners_formd'], 60)}] {short(it.get('formd_links'), 70)} @{it.get('issuer_city')},{it.get('issuer_state')} inc {it.get('year_inc') or '-'}")
    if it.get("wayback_years"):
        ev.append(f"wayback {it['wayback_years']}")
    if it.get("former_unicorn"):
        ev.append("former_unicorn " + short(json.dumps(it["former_unicorn"]), 140))
    if it.get("acquirer"):
        ev.append(f"wikidata acquirer {it['acquirer']}")
    if it.get("formd_band_withheld"):
        ev.append("band_withheld " + short(json.dumps(it["formd_band_withheld"]), 120))
    if ev:
        out.append("   " + " | ".join(ev))
    if it.get("known"):
        kn = {k: v for k, v in it["known"].items() if k not in ("entry_stage_source",)}
        out.append("   pre: " + short(json.dumps(kn), 220))
    if it.get("formd_graduation"):
        out.append("   formd_grad: " + short(json.dumps(it["formd_graduation"]), 220))
    gs = (s.get("grid_slug") or s.get("slug")) if s else None
    for n, p in enumerate(POSTS.get(gs or "", []) or [], 1):
        if n > 4 and not FULL:
            break
        out.append(f"   post@{n} {p['date']} {short(p['title'], 80)}")
        for x in p["sentences"][: (4 if FULL else 1)]:
            out.append("      > " + short(x, 240 if FULL else 150))
    for u, sent in (WIKI.get(it["slug"]) or [])[:1]:
        out.append(f"   wiki {short(sent, 180)} <{u.replace('https://en.wikipedia.org/wiki/', 'wp:')}>")
    sibs = SIB.get(it["slug"]) or []
    if sibs:
        best = sorted(sibs, key=lambda x: (x["valuation_asof"] or "", x["valuation_usd"] or ""), reverse=True)[0]
        v = f"${float(best['valuation_usd']) / 1e9:.2f}B@{best['valuation_asof']}" if best["valuation_usd"] else ""
        out.append(f"   sibs[{len(sibs)}:{','.join(sorted({x['investor'][:8] for x in sibs}))}] {'/'.join(sorted({x['status'] for x in sibs}))} "
                   f"{best['valuation_range']} {v} | hq {sorted({(x['hq_city'] or '?') + ',' + x['hq_country'] for x in sibs})[:2]} "
                   f"| {sorted({x['focus'] for x in sibs if x['focus']})[:2]} | {short(best['note'], 110)}")
    return "\n".join(out)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    arg = args[0]
    items = load(INV / "scratch/queue/queue.json", default=[]) if arg == "all" else json.load(open(arg))
    want = set(args[1:])
    for it in items:
        if want and it["slug"] not in want:
            continue
        print(card(it))
