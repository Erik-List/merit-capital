#!/usr/bin/env python3
"""Compact judge cards for one queue batch: the queue item's own evidence plus
what IVP's other sources say about the row (the firm's live page, the CC
archive fields, the firm's announcements, the archived news, Redpoint's
previous-by-partners seed). Read-only; prints to stdout.

Usage: python3 data/collection/investors/ivp/scratch/cards.py <batch-file> [slug ...]
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

INV = Path(__file__).resolve().parents[1]
ROOT = INV.parents[3]


def norm(n: str) -> str:
    n = (n or "").lower()
    n = re.sub(r"\b(inc|corp|corporation|llc|ltd|co|company|the)\b\.?", "", n)
    return re.sub(r"[^a-z0-9]+", "", n)


def load(p, key="rows"):
    try:
        d = json.load(open(p))
    except (OSError, ValueError):
        return []
    return d.get(key, []) if isinstance(d, dict) else d


LIVE = {norm(r["name"]): r for r in load(INV / "sources/site/company-pages.json")}
LIVE_SLUG = {r["slug"]: r for r in LIVE.values()}
CC = {norm(r["name"]): r for r in load(INV / "sources/site/cc-listings.json")}
POSTS = {}
try:
    POSTS = json.load(open(INV / "scratch/posts-by-company.json"))
except (OSError, ValueError):
    pass
CCPOSTS = load(INV / "sources/site/cc-posts.json")
RP = {norm(r.get("name", "")) for r in load(ROOT / "data/collection/investors/redpoint-ventures/sources/web/previous-by-partners.json")}
SIB = {}
try:
    SIB = json.load(open(INV / "scratch/siblings.json"))
except (OSError, ValueError):
    pass


def loose(n: str) -> str:
    n = (n or "").lower()
    n = re.sub(r"\(.*?\)", "", n)
    n = re.sub(r"\b(inc|corp|corporation|llc|ltd|co|company|the|plc|gmbh|ab|sa)\b\.?", "", n)
    return re.sub(r"[^a-z0-9]+", "", n)


FTS = {}
try:
    fts = json.load(open(INV / "sources/edgar/fts-hits.json"))
    for r in (fts.get("registrants") or fts.get("rows") or []) if isinstance(fts, dict) else fts:
        FTS[norm(r.get("name") or r.get("registrant") or "")] = r
except (OSError, ValueError):
    pass


def short(s, n=160):
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    return s if len(s) <= n else s[: n - 1] + "…"


def card(it: dict) -> str:
    k = norm(it.get("name"))
    out = [f"## {it.get('slug')} | {it.get('name')} | need={','.join(it.get('need') or [])} | class={it.get('evidence_class')} tier={it.get('tier')} first_seen={it.get('first_seen')}"]
    lv = LIVE.get(k) or LIVE_SLUG.get(it.get("slug"))
    if lv:
        out.append(f"  LIVE {lv['url']} | {lv.get('site_status')} | {'; '.join(lv.get('moments') or [])} | {short(lv.get('headline'),90)} | site={lv.get('company_site')} | lead={short(lv.get('leadership'),60)} | team={', '.join(lv.get('partners') or [])}")
        for p in POSTS.get(lv["slug"], [])[:3]:
            out.append(f"  POST {p['date']} {p['url']} :: {short(' | '.join(p['sentences']) or p['title'], 260)}")
    cc = CC.get(k)
    if cc:
        out.append(f"  CC {cc['cc_first']}..{cc['cc_last']} | invested={cc.get('invest_year')} | status={short(cc.get('site_status') or cc.get('outcome'),90)} | loc={cc.get('location')} | lead={short(cc.get('leadership'),50)} | {short(cc.get('description'),100)} | site={cc.get('company_site')}")
    if k in RP:
        out.append("  SEED: on Redpoint's previous-by-partners list (founders' Brentwood/IVP book)")
    for f in ("site_url", "wayback_first_link", "wayback_years", "site_invest_year", "sector", "partners_site",
              "partners_formd", "edgar_forms", "edgar_span", "edgar_links", "formd_span", "formd_max_round_usd",
              "formd_links", "issuer_city", "issuer_state", "year_inc", "former_unicorn", "entry_date", "notes"):
        v = it.get(f)
        if v not in (None, "", [], {}):
            out.append(f"  {f}: {short(v, 220)}")
    if it.get("rounds"):
        out.append("  rounds: " + short("; ".join(f"{r.get('date') or r.get('filed')}:{r.get('amount') or r.get('total_sold')}" for r in it["rounds"][:8]), 220))
    if it.get("formd_graduation"):
        out.append("  formd_graduation: " + short(json.dumps(it["formd_graduation"]), 260))
    kn = it.get("known")
    if kn:
        out.append("  KNOWN(siblings): " + short(json.dumps({x: kn.get(x) for x in ("status", "valuation_range", "valuation_usd", "valuation_citation", "hq_country", "hq_city", "entry_stage", "note") if kn.get(x)}), 520))
    for sb in SIB.get(loose(it.get("name")), [])[:3]:
        out.append(f"  SIB[{sb['inv']}] {sb.get('status')} {sb.get('valuation_range')} usd={sb.get('valuation_usd')} asof={sb.get('valuation_asof')} src={sb.get('valuation_source')} cite={short(sb.get('valuation_citation'),110)} | {sb.get('hq_city')},{sb.get('hq_country')} | stage={sb.get('entry_stage')}")
    ge = it.get("graduation_evidence")
    if ge:
        ms = ge.get("mentions") or []
        out.append(f"  GRAD_EVIDENCE asof={ge.get('asof')} " + short(" || ".join(f"{m.get('date')} {m.get('title')}" for m in ms[:5]), 400))
    for p in CCPOSTS:
        if k and len(k) > 3 and k in norm(p.get("title", "")):
            out.append(f"  CCPOST {p['captured']} {p['url']} :: {short(p['title'], 120)}")
            break
    return "\n".join(out)


def main() -> None:
    batch = json.load(open(sys.argv[1]))
    items = batch if isinstance(batch, list) else batch.get("items", [])
    want = set(sys.argv[2:])
    for it in items:
        if want and it.get("slug") not in want:
            continue
        print(card(it))


if __name__ == "__main__":
    main()
