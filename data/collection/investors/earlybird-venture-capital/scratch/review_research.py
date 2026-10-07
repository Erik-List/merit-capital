#!/usr/bin/env python3
"""Compact one-row-per-company view of a research group, for the judge's review."""
import json, sys, re
from urllib.parse import urlparse
H = __import__("pathlib").Path(__file__).resolve().parent
def host(u):
    try: return urlparse(u).netloc.replace("www.", "")[:28] if u else "-"
    except Exception: return "?"
g = sys.argv[1]
d = json.load(open(H / "research" / f"{g}.json"))
only = set(sys.argv[2].split(",")) if len(sys.argv) > 2 else None
for s, r in d.items():
    if only and s not in only: continue
    e = r.get("entry") or {}
    gr = r.get("graduation")
    v = r.get("valuation") or {}
    grs = "-"
    if isinstance(gr, dict):
        grs = f"{gr.get('later_round')} {gr.get('date')} [{host(gr.get('citation'))}]" if gr.get("later_round") else ("none_found" if gr.get("none_found") else str(gr)[:40])
    print(f"{s} | E: {e.get('round')} {e.get('date')} {e.get('amount') or ''} lead={str(e.get('lead'))[:22]} named={e.get('earlybird_named')} [{host(e.get('citation'))}]"
          f" | G: {grs} | S: {r.get('status')} {r.get('status_date') or ''} [{host(r.get('status_citation'))}]"
          f" | V: {v.get('range')} {v.get('usd') or ''} {v.get('asof') or ''} | {r.get('hq_city')},{r.get('hq_country')} | {r.get('focus')} | conf {r.get('confidence')}"
          + (f" | FLAG {r.get('membership_flag')}: {str(r.get('membership_detail'))[:260]}" if r.get("membership_flag") else ""))
    if "--notes" in sys.argv:
        print("     ", (r.get("notes") or "")[:300], "| entry_asserted:", str(e.get("entry_asserted"))[:200])
