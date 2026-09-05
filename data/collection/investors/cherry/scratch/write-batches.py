#!/usr/bin/env python3
"""Assemble scratch/queue/batch-NNN.out.jsonl from the judgment parts (one dict of records keyed by slug)."""
import importlib.util, json, sys
from pathlib import Path
I = Path("data/collection/investors/cherry")
J = {}
for n in (1, 2, 3, 4):
    spec = importlib.util.spec_from_file_location(f"j{n}", I / f"scratch/judgments-{n}.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); J.update(m.J)
print("judgments:", len(J))
for b in sorted(I.glob("scratch/queue/batch-*.json")):
    if ".out" in b.name: continue
    items = json.loads(b.read_text()); lines = []; missing = []
    for it in items:
        r = J.get(it["slug"])
        if r is None: missing.append(it["slug"]); continue
        lines.append(r)
    out = b.with_name(b.name.replace(".json", ".out.jsonl"))
    out.write_text("\n".join(json.dumps(l, ensure_ascii=False) for l in lines) + "\n")
    print(f"{out.name}: {len(lines)} lines; missing {missing}")
