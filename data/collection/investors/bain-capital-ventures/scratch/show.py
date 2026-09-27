#!/usr/bin/env python3
"""Compact judge view: queue item + evidence pack per slug.
Usage: show.py slug [slug ...] | --batch N"""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
q = {i["slug"]: i for i in json.loads((HERE / "queue" / "queue.json").read_text())} \
    if (HERE / "queue" / "queue.json").exists() else {}
base = {r["slug"]: r for r in json.loads((HERE.parent / "companies" / "base.json").read_text())}
pk = json.loads((HERE / "evidence-pack.json").read_text())
nw = json.loads((HERE / "news-sweep.json").read_text()) if (HERE / "news-sweep.json").exists() else {}
import re as _re
_EXIT = _re.compile(r"(?i)acqui|buys|to buy|merge|ipo|goes public|shut|bankrupt|closes|lays off|valuation|unicorn|billion")
args = sys.argv[1:]
if args and args[0] == "--batch":
    b = json.loads((HERE / "queue" / f"batch-{int(args[1]):03d}.json").read_text())
    args = [i["slug"] for i in (b if isinstance(b, list) else b.get("items", []))]
for s in args:
    i, p, r = q.get(s, {}), pk.get(s, {}), base.get(s, {})
    print(f"\n### {s} | {i.get('name') or r.get('name')} | need={','.join(i.get('need', []))} | fs={i.get('first_seen') or r.get('first_seen')} "
          f"ec={i.get('evidence_class')} known={i.get('known')}")
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
        print("  site:", {k: v for k, v in p["site"].items() if v and k not in ("popover",)})
    if "crypto_site" in p:
        print("  crypto site:", p["crypto_site"])
    if "archive" in p:
        a = p["archive"]
        print("  archive:", ",".join(a["years"]), a.get("outcome") or "", a.get("location") or "",
              a.get("stage_bucket") or "", a.get("stage_wp") or "", a.get("site_status") or "",
              ("partners=" + ",".join(a.get("partners") or [])) if a.get("partners") else "",
              ("WORKED: " + a["worked_with"][:400]) if a.get("worked_with") else "")
    for x in p.get("posts", [])[:4]:
        print(f"  post {x['date'][:10]} {x['title'][:90]}")
        for sn in x.get("sentences", [])[:2]:
            print("      >", sn[:260].replace("\n", " "))
    for x in p.get("edgar_fulltext", [])[:2]:
        print("  fts:", x["registrant"], x["forms"], x["first"], (x["snippets"] or [""])[0][:300])
    for x in p.get("wikipedia", [])[:2]:
        print("  wiki:", x["article"], [y[:200] for y in x["sentences"][:2]])
    n = nw.get(s) or {}
    if n.get("status") == "error":
        print("  news: ERROR (re-run news-sweep)")
    hits = [it for it in n.get("items", []) if it.get("names") and (it.get("rounds") or it.get("amounts") or _EXIT.search(it["title"]))]
    for it in hits[-6:]:
        print(f"  news {it['date']} | {it['source']} | {it['title'][:150]}")
    for x in p.get("siblings", []):
        print(f"  sib {x['investor']}: {x['status']}/{x['range']}/{x['usd'] or '-'}@{x['asof'] or '-'} stage={x['stage']}({x['stage_src']}) "
              f"{x['city']},{x['country']} {x['focus']} v={x['verdict']}")
