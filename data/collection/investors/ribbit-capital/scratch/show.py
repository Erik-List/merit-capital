#!/usr/bin/env python3
"""Compact judge view: queue item + evidence pack + news per slug.
Usage: show.py slug [slug ...] | --batch N"""
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
led = json.loads((HERE.parent / "companies" / "membership-ledger.json").read_text())["ribbit-capital"]["verdicts"]
_EXIT = re.compile(r"(?i)acqui|buys|to buy|merge|ipo|goes public|listing|shut|bankrupt|closes|lays off|valuation|unicorn|billion|series|seed|raises|funding")
args = sys.argv[1:]
if args and args[0] == "--batch":
    b = json.loads((HERE / "queue" / f"batch-{int(args[1]):03d}.json").read_text())
    args = [i["slug"] for i in (b if isinstance(b, list) else b.get("items", []))]
for s in args:
    i, p, r = q.get(s, {}), pk.get(s, {}), base.get(s, {})
    v = led.get(s, {}).get("verdict", "UNJUDGED")
    print(f"\n### {s} | {i.get('name') or r.get('name')} | verdict={v} | need={','.join(i.get('need', []))} | "
          f"fs={i.get('first_seen') or r.get('first_seen')} known={i.get('known')}")
    if i.get("rounds"):
        print("  formd rounds:", [(x.get('date'), x.get('amount') or x.get('total_sold'), x.get('position')) for x in i["rounds"]][:6],
              "| grad:", i.get("formd_graduation"))
    if i.get("partners_formd") or r.get("partners_formd"):
        print("  formd partners:", i.get("partners_formd") or r.get("partners_formd"), i.get("issuer_city"), i.get("issuer_state"),
              "inc", i.get("year_inc"), "| links", (i.get("formd_links") or r.get("formd_links") or "")[:160])
    if i.get("edgar_forms") or r.get("edgar_forms"):
        print("  edgar:", i.get("edgar_forms") or r.get("edgar_forms"))
    if i.get("former_unicorn") or i.get("acquirer") or i.get("formd_band_withheld"):
        print("  unicorn/acq/band:", i.get("former_unicorn"), i.get("acquirer"), i.get("formd_band_withheld"))
    if "site" in p:
        print("  site (Rebels):", p["site"])
    if "archive" in p:
        a = p["archive"]
        print("  archive:", ",".join(a["years"]), "|", a.get("name"), "|", a.get("company_url") or "", "|",
              a.get("country_label") or "", "|", (a.get("about") or "")[:160])
    for x in p.get("spv", []):
        print(f"  spv {x['code']} {x['quarter']} sold={x['sold']} round={x['round_as_coded']} ({x['decode']}) {x['vehicle']}")
    for x in p.get("13f", []):
        print(f"  13f {x['name']} {x['first']}..{x['last']} max ${x['max_usd']:,.0f}")
    for x in p.get("edgar_fulltext", [])[:2]:
        print("  fts:", x["registrant"], x["forms"], x["first"], (x["snippets"] or [""])[0][:300])
    for x in p.get("wikipedia", [])[:2]:
        print("  wiki:", x["article"], [y[:220] for y in x["sentences"][:2]])
    n = nw.get(s) or {}
    if n.get("status") == "error":
        print("  news: ERROR (re-run news-sweep)")
    hits = [it for it in n.get("items", []) if it.get("names") and _EXIT.search(it["title"])]
    for it in hits[-8:]:
        print(f"  news {it['date']} | {it['source']} | {it['title'][:150]}")
    for x in p.get("siblings", []):
        print(f"  sib {x['investor']}: {x['status']}/{x['range']}/{x['usd'] or '-'}@{x['asof'] or '-'} stage={x['stage']}({x['stage_src']}) "
              f"{x['city']},{x['country']} {x['focus']} v={x['verdict']}")
