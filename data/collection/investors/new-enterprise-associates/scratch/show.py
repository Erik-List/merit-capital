#!/usr/bin/env python3
"""Compact judge view: queue item + evidence pack per slug (NEA). Usage: show.py slug [slug ...] | --batch N"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
q = {i["slug"]: i for i in json.loads((HERE / "queue" / "queue.json").read_text())} \
    if (HERE / "queue" / "queue.json").exists() else {}
base = {r["slug"]: r for r in json.loads((HERE.parent / "companies" / "base.json").read_text())}
pk = json.loads((HERE / "evidence-pack.json").read_text())
nw = json.loads((HERE / "news-sweep.json").read_text()) if (HERE / "news-sweep.json").exists() else {}
_EXIT = re.compile(r"(?i)acqui|buys|to buy|merge|ipo|goes public|shut|bankrupt|closes|lays off|valuation|unicorn|billion|series|seed|raises|funding")
args = sys.argv[1:]
if args and args[0] == "--batch":
    b = json.loads((HERE / "queue" / f"batch-{int(args[1]):03d}.json").read_text())
    args = [i["slug"] for i in (b if isinstance(b, list) else b.get("items", []))]
for s in args:
    i, p, r = q.get(s, {}), pk.get(s, {}), base.get(s, {})
    print(f"\n### {s} | {i.get('name') or r.get('name')} | need={','.join(i.get('need', []))} | fs={i.get('first_seen') or r.get('first_seen')} "
          f"tier={r.get('tier')} ec={i.get('evidence_class')} known={ {k: v for k, v in (i.get('known') or {}).items() if v not in (None, '', [])} }")
    if i.get("rounds"):
        print("  formd rounds (quarter, usd):", [(x.get('q') or x.get('date'), x.get('usd') or x.get('amount')) for x in i["rounds"]][:8],
              "| grad:", i.get("formd_graduation"))
    if r.get("partners_formd"):
        print("  formd partners:", r.get("partners_formd"), "| roles", r.get("formd_roles"), "| span", r.get("formd_span"),
              "| max round", r.get("formd_max_round_usd"), "| links", (r.get("formd_links") or "")[:220])
    for k in ("former_unicorn", "acquirer", "formd_band_withheld", "hq_country_claim", "site_entry_stage", "site_invest_year"):
        if i.get(k):
            print(f"  {k}:", i.get(k))
    if r.get("edgar_links"):
        print("  edgar:", r.get("edgar_forms"), r.get("edgar_span"), (r.get("edgar_links") or "")[:200])
    if "site" in p:
        print("  site:", p["site"])
    if "archive" in p:
        a = p["archive"]
        print("  archive:", a["first"], "-", a["last"], f"({len(a['years'])} yrs)", a.get("eras"), a.get("reports_2008") or "",
              "| yr", a.get("invest_year", ""), "| stage", a.get("stage_site", ""), "|", a.get("investment_status", ""),
              "|", a.get("exit", ""), "|", (a.get("about") or "")[:200])
        if a.get("latest"):
            print("    latest:", a["latest"])
    if p.get("nea_filings"):
        print("  NEA vehicle filings:", p["nea_filings"])
    for x in p.get("posts", [])[:4]:
        print(f"  post {x['date']} [{x['kind']}] {x['title'][:90]} {x['url']} {x.get('article_link') or ''}")
        for sn in x.get("sentences", [])[:2]:
            print("      >", sn[:300].replace("\n", " "))
    for x in p.get("edgar_fulltext", [])[:2]:
        print("  fts:", x["registrant"], x["forms"], x["first"])
        for sn in x["snippets"][:2]:
            print("      >", sn[:350])
    for x in p.get("wikipedia", [])[:2]:
        print("  wiki:", x["article"], [y[:220] for y in x["sentences"][:2]])
    n = nw.get(s) or {}
    hits = [it for it in n.get("items", []) if it.get("names") and (it.get("rounds") or it.get("amounts") or _EXIT.search(it["title"]))]
    for it in hits[-8:]:
        print(f"  news {it['date']} | {it['source']} | {it['title'][:160]}")
    for x in p.get("siblings", []):
        print(f"  sib {x['investor']}: {x['status']}/{x['range']}/{x['usd'] or '-'}@{x['asof'] or '-'} stage={x['stage']}({x['stage_src']}) "
              f"{x['city']},{x['country']} {x['focus']} v={x['verdict']}")
    notes = r.get("notes") or []
    for nt in (notes.split("; ") if isinstance(notes, str) else notes)[:3]:
        print("  note:", str(nt)[:200])
