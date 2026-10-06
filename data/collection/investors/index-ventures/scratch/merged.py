"""The merged view (COLLECTION.md s8): resolved.json overlaid with classification.json, over the slugs in base.json, with
the ledger verdict. `python3 merged.py` prints the visible slice ($1B+ or public members); import `view()` elsewhere."""
import json, sys
from pathlib import Path
R = Path(__file__).resolve().parents[1]
def view():
    base = json.loads((R / "companies/base.json").read_text()); base = base["companies"] if isinstance(base, dict) else base
    res = json.loads((R / "companies/resolved.json").read_text()) if (R / "companies/resolved.json").exists() else {}
    cl = json.loads((R / "companies/classification.json").read_text())
    led = json.loads((R / "companies/membership-ledger.json").read_text())["index-ventures"]["verdicts"]
    out = {}
    for b in base:
        s = b["slug"]; r = dict(res.get(s) or {}); o = cl.get(s) or {}
        flags = (set(r.get("flags") or []) | set(o.get("flags") or [])) - set(o.get("cleared_flags") or [])
        r.update({k: v for k, v in o.items() if k != "flags"}); r["flags"] = sorted(flags)
        r["name"] = b["name"]; r["verdict"] = (led.get(s) or {}).get("verdict"); r["_base"] = b
        out[s] = r
    return out
if __name__ == "__main__":
    V = view()
    vis = {s: r for s, r in V.items() if r["verdict"] == "member" and (r.get("status") == "public" or (r.get("valuation_usd") or 0) >= 1e9 or r.get("valuation_range") in ("1b_plus", "10b_plus", "100b_plus"))}
    print(len(vis), "visible rows")
    for s, r in sorted(vis.items(), key=lambda kv: -(kv[1].get("valuation_usd") or 0)):
        print(f"{s[:24]:24s} {str(r.get('status'))[:8]:8s} {r.get('valuation_range') or '-':10s} {(r.get('valuation_usd') or 0)/1e9:8.2f}B {str(r.get('valuation_asof'))[:10]:10s} {str(r.get('valuation_source'))[:13]:13s} {str(r.get('entry_stage'))[:8]:8s}/{str(r.get('entry_stage_source'))[:11]:11s} {','.join(r['flags'])[:60]:60s} {(r.get('valuation_citation') or '')[:60]}")
