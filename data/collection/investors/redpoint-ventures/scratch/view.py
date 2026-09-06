#!/usr/bin/env python3
"""Compact evidence view for judging: the queue item joined to everything the
site, announcement and predecessor-book layers know about the row."""
import json, sys, re
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parents[5] / "scripts"))
from paths import Paths
P = Paths("redpoint-ventures")
enr = json.load(open(P.root / "scratch" / "row-evidence.json"))
def show(items):
    for i in items:
        e = enr.get(i["slug"], {})
        need = ",".join(i["need"])
        print(f"### {i['slug']}  |  {i['name']}  | need: {need} | tier {i.get('tier')} | {i.get('evidence_class')}")
        bits = []
        if i.get("first_seen"): bits.append(f"first_seen={i['first_seen']}")
        if i.get("wayback_years"): bits.append(f"wb={i['wayback_years']}")
        if e.get("listing_years"): bits.append(f"listyrs={e['listing_years']}")
        if i.get("sector"): bits.append(f"sector={i['sector']}")
        if e.get("sectors"): bits.append(f"site_sectors={e['sectors']}")
        if i.get("partners_site"): bits.append(f"partner={i['partners_site']}")
        if e.get("partners"): bits.append(f"card_partner={e['partners']}")
        if i.get("site_url") or e.get("url"): bits.append(f"url={(i.get('site_url') or e.get('url'))[:46]}")
        if bits: print("   " + " | ".join(bits))
        b2 = []
        for k in ("site_stage","invest_year","site_location","site_status","site_active_state","ticker","acquirer","display","_name_basis"):
            if e.get(k) not in (None,"",[],{}): b2.append(f"{k}={e[k]}")
        if b2: print("   " + " | ".join(b2))
        if e.get("description"): print(f"   desc: {e['description'][:150]}")
        if e.get("excerpt"): print(f"   EXCERPT: {re.sub(chr(10),' ',e['excerpt'])[:300]}")
        for a in (e.get("announcements") or [])[:3]: print(f"   ANN: {a}")
        for w in (e.get("wikipedia") or [])[:1]: print(f"   WIKI: {w}")
        if e.get("previous_by_partners"): print("   *** ALSO IN 'Previous Investments by Redpoint Partners' (decisions.md D5)")
        ev = []
        for k in ("formd_span","formd_max_round_usd","edgar_forms","edgar_span","formd_accessions","issuer_city","issuer_state","year_inc","former_unicorn"):
            if i.get(k) not in (None,"",[],{}): ev.append(f"{k}={i[k]}")
        if ev: print("   " + " | ".join(ev))
        if i.get("rounds"): print(f"   rounds: {i['rounds'][:6]}")
        if i.get("known"): print(f"   known: {i['known']}")
        print()
if __name__ == "__main__":
    a = sys.argv[1]
    if a.startswith("slugs:"):
        want = set(a.split(":",1)[1].split(","))
        q = json.load(open(P.queue/"queue.json"))
        show([i for i in q if i["slug"] in want])
    else:
        show(json.load(open(P.queue/f"batch-{int(a):03d}.json")))
