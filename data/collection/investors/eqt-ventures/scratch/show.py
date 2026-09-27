#!/usr/bin/env python3
"""Compact judge view: queue item + evidence pack per slug. Usage: show.py slug [slug ...] | --batch N"""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
q = {i["slug"]: i for i in json.loads((HERE / "queue" / "queue.json").read_text())}
pk = json.loads((HERE / "evidence-pack.json").read_text())
args = sys.argv[1:]
if args and args[0] == "--batch":
    b = json.loads((HERE / "queue" / f"batch-{int(args[1]):03d}.json").read_text())
    args = [i["slug"] for i in (b if isinstance(b, list) else b.get("items", []))]
for s in args:
    i, p = q.get(s, {}), pk.get(s, {})
    print(f"\n### {s} | {i.get('name')} | need={','.join(i.get('need', []))} | fs={i.get('first_seen')} known={i.get('known')}")
    if i.get("rounds"): print("  formd rounds:", [(r.get('date'), r.get('amount') or r.get('total_sold'), r.get('position')) for r in i["rounds"]][:6], "| grad:", i.get("formd_graduation"))
    if i.get("partners_formd"): print("  formd partners:", i["partners_formd"], i.get("issuer_city"), i.get("issuer_state"), "inc", i.get("year_inc"))
    if i.get("former_unicorn") or i.get("acquirer"): print("  unicorn/acq:", i.get("former_unicorn"), i.get("acquirer"))
    if "site" in p: print("  site:", {k: v for k, v in p["site"].items() if v})
    if "archive" in p:
        a = p["archive"]; print("  archive:", a["years"], "dates", a["announced_dates"][:3], "closing" if a["closing_dated"] else "", "EXIT" if a["exit_flag"] else "", a["geography"], a["industry"], a["stage_card"], (a["description"] or "")[:80])
    for x in p.get("posts", [])[:5]:
        print(f"  post {x['date']} [{x.get('fund_voice')}] {x['title'][:90]} rw={x.get('round_words')} amt={x.get('amounts')}")
        for sn in x.get("sentences", [])[:2]: print("      >", sn[:260])
    for x in p.get("edgar_fulltext", [])[:2]: print("  fts:", x["registrant"], x["form"], x["date"], x["context"][:220])
    for x in p.get("wikipedia", [])[:2]: print("  wiki:", x["article"], [y[:200] for y in x["sentences"][:2]])
    for x in p.get("siblings", []): print(f"  sib {x['investor']}: {x['status']}/{x['range']}/{x['usd'] or '-'}@{x['asof'] or '-'} stage={x['stage']}({x['stage_src']}) {x['city']},{x['country']} {x['focus']} v={x['verdict']}")
