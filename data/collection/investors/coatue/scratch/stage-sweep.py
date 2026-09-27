#!/usr/bin/env python3
"""Undetermined-stage sweep (duty 9, 2026-09-27): one Google News search per row whose entry
stage is undetermined, '"<name>" Coatue', keeping headlines that carry a round word or an amount.
Writes scratch/stage-sweep.json {slug: [{date, source, title, gid}]}. Paced by the shared throttle."""
import csv, importlib.util, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]; INV = ROOT / "data/collection/investors/coatue"
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec); sys.argv = sys.argv[:1]; spec.loader.exec_module(gs)
SKIP = {"decidehq", "dialect", "syrn", "geneva"}
ALIAS = {"brud": "Lil Miquela", "radpod": "Twenty Labs", "deepnote": "Deepnote", "iconic-hearts": "Sendit", "dagster-labs": "Elementl",
         "the-supplant-company": "Supplant", "atma-sciences": "Gizmo app", "open": "Open breathwork", "flex": "Flex rent", "origin": "Origin financial",
         "arch": "Arch private investments", "nate": "Nate shopping app", "karat": "Karat card creators", "haystack": "Haystack intranet", "saturn": "Saturn app students",
         "canal": "Canal ecommerce", "codi": "Codi office", "titan": "Titan invest app", "lighter": "Lighter exchange", "graphy": "Graphy charts", "ara": "Ara screens"}
rows = [r for r in csv.DictReader(open(INV / "companies/base.csv")) if r["entry_stage"] == "undetermined" and r["slug"] not in SKIP]
out = {}
for r in rows:
    name = r["name"]; q = f'"{name}" Coatue'
    res = gs.googlenews(q, name)
    keep = []
    if res["status"] == "ok":
        for i in res["items"]:
            if i["rounds"] or i["amounts"]:
                keep.append({"date": i["date"], "source": i["source"], "title": i["title"], "gid": i["gid"], "names": bool(i["names"])})
    out[r["slug"]] = {"name": name, "query": q, "status": res["status"], "n": res.get("n"), "hits": keep}
    alias = ALIAS.get(r["slug"])
    if alias:
        res2 = gs.googlenews(f'"{alias}" Coatue', alias)
        if res2["status"] == "ok":
            out[r["slug"]]["hits"] += [{"date": i["date"], "source": i["source"], "title": i["title"], "gid": i["gid"], "names": bool(i["names"]), "alias": alias}
                                       for i in res2["items"] if i["rounds"] or i["amounts"]]
    print(f"{r['slug']:28s} {res['status']:6s} n={res.get('n')} hits={len(out[r['slug']]['hits'])}", flush=True)
(INV / "scratch/stage-sweep.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
