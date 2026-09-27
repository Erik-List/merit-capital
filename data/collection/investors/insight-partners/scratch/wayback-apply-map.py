#!/usr/bin/env python3
"""Apply scratch/wayback-name-map.json to sources/wayback/parsed/*.json: every parsed row whose
slug the map names takes the target base row's name (kept beside it as `name_source` for the
record), so the base build joins the capture to that row instead of minting a row named after a
slug variant (COLLECTION.md §5). Idempotent. Usage: python3 wayback-apply-map.py"""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402
I = HERE.parent
MAP = json.loads((HERE / "wayback-name-map.json").read_text())
m = MAP["map"]
new_names = {k: v for k, v in MAP.get("names", {}).items() if not k.startswith("_")}
b = json.loads((I / "companies" / "base.json").read_text())
rows = b["rows"] if isinstance(b, dict) else b
name = {r["slug"]: r["name"] for r in rows}
# a target may have left the base at the rebuild (a control or not_member row): its name is
# kept from excluded.json, then from the base copy taken before the rebuild
for extra in (I / "companies" / "excluded.json", HERE / "base-before-rebuild.json"):
    if extra.exists():
        e = json.loads(extra.read_text())
        for r in (e["rows"] if isinstance(e, dict) and "rows" in e else e if isinstance(e, list) else []):
            if isinstance(r, dict) and r.get("slug") and r.get("name"):
                name.setdefault(r["slug"], r["name"])
n = 0
for f in sorted((I / "sources" / "wayback" / "parsed").glob("*.json")):
    d = json.loads(f.read_text())
    for r in d:
        t = m.get(r["slug"])
        want = name[t] if t else new_names.get(r["slug"])
        if want and r.get("name") != want:
            if r.get("name") and "name_source" not in r:
                r["name_source"] = r["name"]
            r["name"] = want
            n += 1
    write_atomic(f, json.dumps(d, indent=1, ensure_ascii=False) + "\n")
print(n, "parsed rows renamed onto base rows")
