#!/usr/bin/env python3
"""The merged view (resolved.json overlaid with classification.json, filtered
to base slugs that are members) and the visible slice of it."""
import json, sys
from pathlib import Path
INV = Path(__file__).resolve().parents[2]
base = json.load(open(INV / "companies/base.json"))
rows = base["rows"] if isinstance(base, dict) and "rows" in base else base
res = json.load(open(INV / "companies/resolved.json"))
cla = json.load(open(INV / "companies/classification.json"))
led = json.load(open(INV / "companies/membership-ledger.json"))
led = led.get("insight-partners", led)
verd = led.get("verdicts", led)


def merged():
    out = {}
    for r in rows:
        s = r["slug"]
        v = verd.get(s) if isinstance(verd, dict) else None
        m = dict(res.get(s) or {})
        for k, val in (cla.get(s) or {}).items():
            if k == "flags":
                m["flags"] = sorted(set((m.get("flags") or []) + (val or [])))
            elif val is not None or k not in m:
                m[k] = val
        m["_name"] = r["name"]
        m["_verdict"] = (v or {}).get("verdict") if isinstance(v, dict) else v
        m["_first_seen"] = r.get("first_seen")
        m["_sector"] = r.get("sector")
        out[s] = m
    return out


if __name__ == "__main__":
    M = merged()
    mem = {s: m for s, m in M.items() if m["_verdict"] == "member" and m.get("status")}
    what = sys.argv[1] if len(sys.argv) > 1 else "summary"
    if what == "summary":
        import collections
        print("members classified", len(mem))
        print(collections.Counter(m.get("valuation_range") for m in mem.values()))
        print("needs_web_value", sum("needs_web_value" in (m.get("flags") or []) for m in mem.values()))
        print("public", sum(m.get("status") == "public" for m in mem.values()))
    elif what == "nw":
        for s, m in sorted(mem.items()):
            if "needs_web_value" in (m.get("flags") or []):
                print(s, "|", m["_name"], "|", m.get("status"), "|", (m.get("note") or "")[:160])
    elif what == "public":
        for s, m in sorted(mem.items()):
            if m.get("status") == "public":
                print(s, "|", m["_name"], "|", m.get("valuation_range"), m.get("valuation_usd"), m.get("valuation_source"), m.get("valuation_asof"), "|", m.get("valuation_citation"))
    elif what == "big":
        for s, m in sorted(mem.items()):
            if m.get("valuation_range") in ("1b_plus", "10b_plus", "100b_plus"):
                print(s, "|", m["_name"], "|", m.get("status"), m.get("valuation_usd"), m.get("valuation_source"), m.get("valuation_asof"), "|", m.get("entry_stage"), m.get("entry_stage_source"), "|", m.get("valuation_citation"), "|", ",".join(m.get("flags") or []))
