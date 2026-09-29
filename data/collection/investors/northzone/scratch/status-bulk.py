#!/usr/bin/env python3
"""Status layer for the archive-era rows: one Google News query per company for an exit, shutdown or later
rename. Output scratch/status-bulk.json (appended)."""
import importlib.util, json, re, sys
from pathlib import Path
H = Path(__file__).resolve().parent; ROOT = H.parents[4]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec); argv, sys.argv = sys.argv[1:], sys.argv[:1]; spec.loader.exec_module(gs)
out = json.loads((H / "status-bulk.json").read_text()) if (H / "status-bulk.json").exists() else {}
for name in argv:
    if out.get(name, {}).get("status") == "ok": continue
    r = gs.googlenews(f'"{name}" acquired OR acquires OR acquisition OR bankruptcy OR insolvency OR "shuts down" OR closes OR raises', name)
    if r["status"] != "ok":
        out[name] = {"status": "failed"}; continue
    its = [i for i in r["items"] if i["names"]]
    out[name] = {"status": "ok", "n": r["n"], "items": [{"date": i["date"], "title": i["title"][:170], "gid": i["gid"]} for i in its[:25]]}
    (H / "status-bulk.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
for name in argv:
    v = out.get(name, {})
    sel = [i for i in v.get("items", []) if re.search(r"(?i)acqui|bankrupt|insolv|shut|close|merge|raises|buys|sold|rebrand", i["title"])]
    print("##", name, v.get("status"), "|", " ; ".join(f"{i['date']} {i['title'][:100]}" for i in sorted(sel, key=lambda x: x["date"])[:4]))
