#!/usr/bin/env python3
"""Compact judge cards for one queue batch: the queue item's own evidence plus
what Insight's other sources say about the row (the site panel, the firm's
posts, the Form D rounds, the unicorn list, the sibling books). Read-only.

Usage: python3 data/collection/investors/insight-partners/scratch/cards.py <batch-file|all> [slug ...]
       --full adds the post sentences
"""
import json
import re
import sys
from pathlib import Path

INV = Path(__file__).resolve().parents[1]
ROOT = INV.parents[3]
FULL = "--full" in sys.argv


def load(p, key=None, default=None):
    try:
        d = json.load(open(p))
    except (OSError, ValueError):
        return default if default is not None else {}
    return d.get(key, d) if key and isinstance(d, dict) else d


SITE = {r["url"].rstrip("/"): r for r in load(INV / "sources/site/company-pages.json", "rows", [])}
POSTS = load(INV / "scratch/posts-by-company.json")
SIB = load(INV / "scratch/siblings.json")
NEWS = load(INV / "sources/web/control-surfaces.json", "rows", {})
WIKI = {}
for a in load(INV / "sources/web/wikipedia-insource.json", "articles", []):
    if a.get("in_base") and a.get("sentences"):
        WIKI.setdefault(a["in_base"], []).append((a["url"], a["sentences"][0]))
F13 = load(INV / "sources/edgar/13f-holdings.json", "issuers", {})
PRE = load(INV / "scratch/judge/prefill.json")


def short(s, n=160):
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    return s if len(s) <= n else s[: n - 1] + "…"


def card(it):
    out = []
    s = SITE.get((it.get("site_url") or "").rstrip("/"))
    need = ",".join(x[:4] for x in it["need"])
    head = f"## {it['slug']} | {it['name']} | {it['evidence_class']} | need {need}"
    if s:
        head += (f" | SITE init={s['initial_investment'] or '-'} {s['site_status'][:7]} loc={s['location'] or '-'}"
                 f" team={', '.join(s['partners'][:4]) or '-'} | {'/'.join(s['sectors'][:3])}"
                 f" | {(s.get('company_site') or '').replace('https://', '').replace('http://', '').replace('www.', '').strip('/')}")
    out.append(head)
    if s and s.get("description"):
        out.append("   desc: " + short(s["description"], 75))
    pr = PRE.get(it["slug"]) or {}
    bits = []
    if pr.get("entry_stage"):
        bits.append(f"stage={pr['entry_stage']}({pr.get('entry_stage_word')})")
    if pr.get("focus"):
        bits.append(f"focus={pr['focus']}")
    if pr.get("hq_city") or pr.get("hq_country"):
        bits.append(f"hq={pr.get('hq_city') or '?'},{pr.get('hq_country')}")
    if pr.get("control_hint"):
        bits.append(f"CONTROL? {pr['control_hint']}")
    if bits:
        out.append("   PROP " + " ".join(bits))
    if s and s.get("investment_journey"):
        out.append("   journey: " + short(s["investment_journey"], 300))
    if s and s.get("milestones"):
        out.append("   milestones: " + short(" | ".join(s["milestones"]), 200))
    ev = []
    if it.get("edgar_forms"):
        ev.append(f"edgar {it['edgar_forms']} first {it.get('first_seen')}")
    if it.get("partners_formd"):
        rounds = ";".join(f"{(r.get('q') or '')[:6]}:{(r.get('usd') or 0) / 1e6:.0f}M" for r in (it.get("rounds") or [])[:7])
        ev.append(f"formd[{it['partners_formd']}] {it.get('formd_span')} @{it.get('issuer_city')},{it.get('issuer_state')} inc {it.get('year_inc') or '-'} rounds {rounds}")
    if it.get("former_unicorn"):
        ev.append("former_unicorn " + short(json.dumps(it["former_unicorn"]), 140))
    if it.get("acquirer"):
        ev.append(f"wikidata acquirer {it['acquirer']}")
    if it.get("formd_band_withheld"):
        ev.append("band_withheld " + short(json.dumps(it["formd_band_withheld"]), 120))
    if ev:
        out.append("   " + " | ".join(ev))
    if it.get("known"):
        kn = {k: v for k, v in it["known"].items() if k not in ("entry_stage_source", "hq_country")}
        out.append("   pre: " + short(json.dumps(kn), 200))
    if it.get("formd_graduation"):
        out.append("   formd_graduation: " + short(json.dumps(it["formd_graduation"]), 230))
    if s:
        for n, p in enumerate((POSTS.get(s["slug"]) or []), 1):
            if n > 6 and not FULL:
                break
            if not (p["round_words"] or p["control_words"] or p["amounts"]) and not FULL:
                continue
            out.append(f"   post@{n} {p['date']} {short(p['title'], 95)} [{','.join(p['round_words'][:3])}|{','.join(p['control_words'][:3])}]")
            if FULL:
                for x in p["sentences"][:3]:
                    out.append("      > " + short(x, 260))
    if s:
        nw = NEWS.get(s["slug"]) or {}
        ctl = [i for i in (nw.get("items") or []) if i.get("control_by_firm")]
        for i in ctl[:2]:
            out.append(f"   CTRL-NEWS {i['date']} {short(i['title'], 120)}")
        for i in (nw.get("news") or [])[-2:]:
            out.append(f"   news {i['date']} {short(i["title"], 100)}")
    for u, sent in (WIKI.get(it["slug"]) or [])[:1]:
        out.append(f"   wiki {short(sent, 200)} <{u.replace('https://en.wikipedia.org/wiki/', 'wp:')}>")
    sibs = SIB.get(it["slug"]) or []
    if sibs:
        best = sorted(sibs, key=lambda x: (x["valuation_asof"] or "", x["valuation_usd"] or ""), reverse=True)[0]
        v = f"${float(best['valuation_usd']) / 1e9:.2f}B@{best['valuation_asof']} <{short(best['valuation_citation'], 90)}>" if best["valuation_usd"] else ""
        out.append(f"   sibs[{len(sibs)}] {best['name']} | {'/'.join(sorted({x['status'] for x in sibs}))} {best['valuation_range']} {v} [{best['investor']}]"
                   f" | hq {sorted({(x['hq_city'] or '?') + ',' + x['hq_country'] for x in sibs})[:2]} | {sorted({x['focus'] for x in sibs if x['focus']})[:2]}")
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
