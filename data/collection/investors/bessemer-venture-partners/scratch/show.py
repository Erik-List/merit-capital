#!/usr/bin/env python3
"""Compact judge view: queue item + evidence pack per slug (Bessemer). Usage: show.py slug [slug ...] | --batch N"""
import json
import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
q = {i["slug"]: i for i in json.loads((HERE / "queue" / "queue.json").read_text())} \
    if (HERE / "queue" / "queue.json").exists() else {}
base = {r["slug"]: r for r in json.loads((HERE.parent / "companies" / "base.json").read_text())}
pk = json.loads((HERE / "evidence-pack.json").read_text())
_cl = json.loads((HERE.parent / "companies" / "classification.json").read_text()) if (HERE.parent / "companies" / "classification.json").exists() else {}
CL = _cl.get("bessemer-venture-partners", _cl)
_rs = json.loads((HERE.parent / "companies" / "resolved.json").read_text()) if (HERE.parent / "companies" / "resolved.json").exists() else {}
RS = _rs.get("bessemer-venture-partners", _rs)
nw = json.loads((HERE / "news-sweep.json").read_text()) if (HERE / "news-sweep.json").exists() else {}
_EXIT = re.compile(r"(?i)acqui|buys|to buy|merge|ipo|goes public|shut|bankrupt|closes|lays off|valuation|unicorn|billion|series|seed|raises|funding")
args = sys.argv[1:]
if args and args[0] == "--list":
    args = json.loads((HERE / "queue" / args[1]).read_text())
if args and args[0] == "--batch":
    b = json.loads((HERE / "queue" / f"batch-{int(args[1]):03d}.json").read_text())
    args = [i["slug"] for i in (b if isinstance(b, list) else b.get("items", []))]
for s in args:
    i, p, r = q.get(s, {}), pk.get(s, {}), base.get(s, {})
    st = {} if os.environ.get("BLIND") else {**(RS.get(s) or {}), **(CL.get(s) or {})}
    print(f"\n### {s} | {i.get('name') or r.get('name')} | need={','.join(i.get('need', []))} | fs={i.get('first_seen') or r.get('first_seen')} "
          f"tier={r.get('tier')} ec={i.get('evidence_class')} known={ {} if os.environ.get('BLIND') else {k: v for k, v in (i.get('known') or {}).items() if v not in (None, '', [])} }")
    if st:
        print("  stored:", {k: st.get(k) for k in ("status", "valuation_range", "valuation_usd", "entry_stage", "entry_stage_source", "entry_date",
                                              "seed_to_a_graduation", "hq_country", "hq_city", "focus", "flags") if st.get(k) not in (None, "", [])})
        if st.get("note"):
            print("  stored note:", str(st["note"])[:400])
    if i.get("rounds"):
        print("  formd rounds (quarter, usd):", [(x.get('q') or x.get('date'), x.get('usd') or x.get('amount')) for x in i["rounds"]][:8],
              "| grad:", i.get("formd_graduation"))
    if r.get("partners_formd"):
        print("  formd partners:", r.get("partners_formd"), "| roles", r.get("formd_roles"), "| span", r.get("formd_span"),
              "| max round", r.get("formd_max_round_usd"), "| links", (r.get("formd_links") or "")[:220])
    for k in ("former_unicorn", "acquirer", "formd_band_withheld", "hq_country_claim", "site_invest_year"):
        if i.get(k):
            print(f"  {k}:", i.get(k))
    if r.get("edgar_links"):
        print("  edgar (Bessemer vehicles' own filings):", r.get("edgar_forms"), r.get("edgar_span"), (r.get("edgar_links") or "")[:200])
    if "site" in p:
        print("  site:", p["site"])
    if "archive" in p:
        a = p["archive"]
        print("  archive:", a["first"], "-", a["last"], f"({len(a['years'])} yrs)", a.get("eras"),
              "| invest_year", a.get("invest_year", ""), "| invest_date", a.get("invest_date", ""), "| exit_year", a.get("exit_year", ""),
              "| partners", a.get("partners", ""), "| listed as", a.get("listed_as", ""), "| acquirer", a.get("acquirer", ""),
              "| ticker", a.get("ticker", ""), "| fka", a.get("fka", ""), "|", a.get("geography", ""), "| india_list" if a.get("india_list") else "",
              "| first capture", a.get("first_capture", ""))
        if a.get("about"):
            print("      about:", a["about"][:500])
        if a.get("about_older"):
            print("      about (older):", a["about_older"][:400])
        if a.get("top_exit_note"):
            print("      top exits:", a["top_exit_note"][:500])
    if p.get("history"):
        print("  history page (firm's own, 2008):", p["history"]["capture_url"])
        for h in p["history"]["paragraphs"]:
            print("      >", h[:420])
    if p.get("pre2008"):
        o = p["pre2008"]
        print("  pre-2008 site (Internet Archive):", o.get("years"), "| partner", o.get("partners", ""), "| sector", o.get("sectors", ""),
              "| first capture", o.get("first_capture", ""))
        for h in (o.get("texts") or [])[:2]:
            print("      >", h[:420])
    if p.get("bvp_filings"):
        print("  Bessemer vehicle filings:", p["bvp_filings"])
    for x in p.get("posts", [])[:4]:
        print(f"  post {x['date']} [{x['kind']}] {x['title'][:90]} {x['url']}" + (f" | memo: {x['memo']}" if x.get("memo") else ""))
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
