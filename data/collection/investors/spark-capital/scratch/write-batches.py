#!/usr/bin/env python3
"""Assemble scratch/queue/batch-NNN.out.jsonl from the judgment parts (dicts J keyed by slug)."""
import importlib.util, json, sys, glob
from pathlib import Path
I = Path("/Users/erik/Developer/merit-capital/data/collection/investors/spark-capital")
J = {}
for f in sorted(glob.glob(str(I / "scratch/judgments-*.py"))):
    spec = importlib.util.spec_from_file_location(Path(f).stem, f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); J.update(m.J)
print("judgments:", len(J))
only = sys.argv[1:]
for b in sorted(I.glob("scratch/queue/batch-*.json")):
    if ".out" in b.name or (only and b.stem not in only): continue
    items = json.loads(b.read_text()); lines = []; missing = []
    for it in items:
        r = J.get(it["slug"]); v = J.get("verdict:" + it["slug"])
        if r is None and v is None: missing.append(it["slug"]); continue
        if v: lines.append(v)                      # a not_member row gets its verdict line and nothing else
        if r is not None: lines.append(r)
    out = b.with_name(b.name.replace(".json", ".out.jsonl"))
    out.write_text("\n".join(json.dumps(l, ensure_ascii=False) for l in lines) + "\n")
    print(f"{out.name}: {len(lines)} lines; missing {missing}")
