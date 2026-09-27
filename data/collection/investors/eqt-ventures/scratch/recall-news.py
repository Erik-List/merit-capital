#!/usr/bin/env python3
"""Recall probe, press layer: Google News headlines naming EQT Ventures as an investor, one query per
phrase per year (graduation-surfaces.py's googlenews, shared throttle), companies read off the headline
and diffed against the base. Output: ../sources/web/recall-news.json"""
import importlib.util, json, re, sys, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec); sys.argv = sys.argv[:1]; spec.loader.exec_module(gs)
base = {re.sub(r"[^a-z0-9]", "", r["name"].lower()): r["slug"] for r in json.loads((HERE.parent / "companies/base.json").read_text())}
out = {"queries": [], "items": []}
for y in range(2016, 2027):
    for ph in ['"led by EQT Ventures"', '"EQT Ventures" leads', '"EQT Ventures" raises']:
        q = f'{ph} after:{y}-01-01 before:{y}-12-31'
        res = gs.googlenews(q, "EQT Ventures")
        out["queries"].append({"q": q, "status": res["status"], "n": res.get("n")})
        for i in res.get("items", []):
            t = i["title"]
            m = re.match(r"^(.{2,60}?)\s+(?:raises|secures|lands|nets|bags|closes|gets|scores|snags|picks up|announces|closed|raised|secured)\b", t, re.I)
            name = m.group(1).strip(" '\"") if m else None
            key = re.sub(r"[^a-z0-9]", "", (name or "").lower())
            out["items"].append({"year": y, "date": i["date"], "source": i["source"], "title": t, "name": name,
                                 "in_base": base.get(key), "gid": i.get("gid")})
        time.sleep(0.5)
(HERE.parent / "sources/web").mkdir(exist_ok=True)
(HERE.parent / "sources/web/recall-news.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
seen = {}
for i in out["items"]:
    if i["name"] and not i["in_base"]:
        seen.setdefault(i["name"], i)
print(sum(1 for q in out["queries"] if q["status"] == "ok"), "of", len(out["queries"]), "queries ok;", len(out["items"]), "items")
for n, i in sorted(seen.items()):
    print(f"  {i['date']} | {n} | {i['title'][:130]}")
