#!/usr/bin/env python3
"""find.py frag [frag...]: search base.json (name, slug, notes), excluded.json, and identity merges."""
import json, sys, re
from pathlib import Path
C = Path(__file__).resolve().parents[3] / "companies"
b = json.load(open(C / "base.json"))
ex = []
p = C / "excluded.json"
if p.exists():
    ex = json.load(open(p))
    if isinstance(ex, dict): ex = ex.get("rows") or ex.get("excluded") or list(ex.values())
def norm(s): return re.sub(r"[^a-z0-9]", "", (s or "").lower())
for q in sys.argv[1:]:
    n = norm(q)
    hits = [(r["slug"], r["name"], r.get("first_seen")) for r in b if n in norm(r["name"]) or n in norm(r["slug"]) or q.lower() in (r.get("notes") or "").lower()]
    xh = []
    for r in ex:
        if isinstance(r, dict) and (n in norm(r.get("name")) or n in norm(r.get("slug"))):
            xh.append((r.get("slug"), r.get("name"), r.get("reason") or r.get("desk") or r.get("verdict")))
    print(f"{q!r}: base={hits[:8]} excluded={xh[:5]}")
