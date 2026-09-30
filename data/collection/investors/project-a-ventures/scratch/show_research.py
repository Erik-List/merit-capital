"""Compact view of research-g*.json rows for the judge."""
import json, sys, glob
from pathlib import Path
H = Path(__file__).resolve().parent
rows = {}
for f in sorted(glob.glob(str(H / "research-g*.json"))):
    if f.endswith("groups.json"):
        continue
    try:
        d = json.load(open(f))
    except Exception:
        continue
    for k, v in d.items():
        if isinstance(v, dict):
            rows[k] = v
want = sys.argv[1:]
if want == ["--list"]:
    print(" ".join(sorted(rows))); sys.exit()
done = set(want[1:]) if want and want[0] == "--except" else None
for k, v in rows.items():
    if want and done is None and k not in want:
        continue
    if done is not None and k in done:
        continue
    e = v.get("entry") or {}
    g = v.get("graduation") or {}
    va = v.get("valuation") or {}
    print(f"== {k} | {v.get('name')} | {v.get('status')} | {v.get('hq_city')}, {v.get('hq_country')} | {v.get('focus')} | conf {v.get('confidence')}")
    print(f"   entry: {e.get('date')} {e.get('round')} {e.get('amount')} lead={e.get('lead')} named={e.get('project_a_named')} | {e.get('citation')}")
    if e.get("quote"): print(f"     q: {e['quote'][:170]}")
    if e.get("entry_asserted"): print(f"     asserted: {str(e['entry_asserted'])[:170]}")
    if g.get("later_round"):
        print(f"   grad: {g.get('later_round')} {g.get('date')} | {g.get('citation')} | {str(g.get('quote'))[:120]}")
    elif g.get("none_found"):
        print(f"   grad: none found; searched {len(g.get('searched') or [])} surfaces")
    print(f"   status: {v.get('status_detail','')[:200]} | {v.get('status_citation')}")
    if va and va.get("range") not in (None, "below_1b"): print(f"   VAL: {va}")
    for r in (v.get("rounds") or [])[:6]:
        print(f"     r {r.get('date')} {r.get('round')} {r.get('amount_usd')} fir={r.get('firm_in_round')} {str(r.get('source'))[:90]}")
    print(f"   notes: {str(v.get('notes'))[:260]}")
