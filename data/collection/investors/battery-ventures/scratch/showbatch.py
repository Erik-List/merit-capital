#!/usr/bin/env python3
"""Print a queue batch compactly for judging, with the firm's own evidence attached.

Adds three things the raw queue item does not carry:
  LISTS=   which site surfaces hold the row. A row whose ONLY surface is the
           compliance list has first_seen 2021 -- the year of that page's
           FIRST CAPTURE, not the investment year -- so fs must not be read as
           an entry date for it.
  EXITED   the compliance list's own '*' marker ("Denotes an exited investment")
  ann:     Battery's own post naming a round for this company, with the
           sentence, read under the Menlo rule (class 1 for the round it NAMES).
"""
import json,re,sys
from pathlib import Path
B=Path("data/collection/investors/battery-ventures")
Q=B/"scratch/queue"
site={r["name"]:r for r in json.load(open(B/"sources/site/companies.json"))}
comp={r["name"]:r for r in json.load(open(B/"sources/site/compliance-list.json"))["rows"]}
ann=json.load(open(B/"sources/site/announcements.json"))["rows"]
KEY=re.compile(r"[^.]*?\b(?:first invest|initially invest|we invested|Battery (?:led|invested|first|acquired)|led (?:the|its|their)|our (?:first|initial)|acquired|majority|buyout|take-private)[^.]*\.",re.I)
def anns_for(name):
    out=[]
    if len(name)<4: return out
    for a in ann:
        if re.search(r"\b"+re.escape(name)+r"\b",a["title"],re.I) and (a["rounds_named"] or a["asserts_entry"]):
            s=KEY.findall(a.get("excerpt") or "")
            out.append((a["date"],",".join(a["rounds_named"]),a["asserts_entry"],
                        (s[0][:190] if s else a["title"][:90])))
    return out[:2]
for b in sys.argv[1:]:
    d=json.load(open(Q/f"batch-{int(b):03d}.json"))
    print(f"######## BATCH {int(b):03d}  ({len(d)} rows)")
    for r in d:
        s=site.get(r["name"]); c=comp.get(r["name"])
        bits=[f"[{r['slug']}]", r['name']]
        if r.get('first_seen'): bits.append(f"fs={r['first_seen']}")
        if r.get('site_invest_year'): bits.append(f"INV={r['site_invest_year']}")
        if r.get('site_entry_stage'): bits.append(f"STAGE={r['site_entry_stage']}")
        if s:
            ls=",".join(s.get("lists") or [])
            bits.append("LISTS="+(ls or "-"))
            if s.get("site_status"): bits.append(f"st='{s['site_status'][:44]}'")
            if s.get("site_location"): bits.append(f"loc={s['site_location'][:30]}")
        if c and c.get("exited"): bits.append("EXITED*")
        if c and c.get("ticker"): bits.append(f"{c.get('exchange')}:{c['ticker']}")
        if c and c.get("successor"): bits.append(f"succ={c['successor'][:28]}")
        if c and c.get("legal_name") and c["legal_name"]!=r["name"]: bits.append(f"legal={c['legal_name'][:40]}")
        bits.append(f"tier={r['tier']}")
        if r.get('formd_span'): bits.append(f"formd={r['formd_span']} max=${r.get('formd_max_round_usd')}")
        if r.get('partners_formd'): bits.append(f"pFD={r['partners_formd'][:44]}")
        if r.get('issuer_city'): bits.append(f"city={r['issuer_city']},{r.get('issuer_state')}")
        if r.get('year_inc'): bits.append(f"inc={r['year_inc']}")
        if r.get('former_unicorn'): bits.append("FORMER_UNICORN")
        if r.get('known'): bits.append(f"known={json.dumps(r['known'])[:120]}")
        if r.get('rounds'): bits.append(f"rounds={json.dumps(r['rounds'])[:130]}")
        bits.append("NEED="+",".join(r['need']))
        print("  "+" | ".join(bits))
        for dt,rd,en,sent in anns_for(r["name"]):
            print(f"       ann {dt} rounds=[{rd}] entry={en}: {sent}")
