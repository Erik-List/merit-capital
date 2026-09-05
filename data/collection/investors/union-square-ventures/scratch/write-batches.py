#!/usr/bin/env python3
"""Assemble scratch/queue/batch-NNN.out.jsonl from the judgment parts (one dict J of records keyed by slug per judgments-N.py)."""
import importlib.util, json, sys, glob
from pathlib import Path
I = Path("/Users/erik/Developer/merit-capital/data/collection/investors/union-square-ventures")
J = {}
for f in sorted(glob.glob(str(I / "scratch/judgments-*.py"))):
    spec = importlib.util.spec_from_file_location(Path(f).stem, f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); J.update(m.J)
print("judgments:", len(J))
want = sys.argv[1:]  # batch numbers to write, e.g. 001
ledger = json.load(open(I / "base-verification.json"))
inv = ledger.get("union-square-ventures", ledger)
verd = inv.get("verdicts", inv) if isinstance(inv, dict) else {}
for b in sorted(I.glob("scratch/queue/batch-*.json")):
    if ".out" in b.name: continue
    if want and b.stem.split("-")[1] not in want: continue
    items = json.loads(b.read_text()); lines = []; missing = []
    for it in items:
        r = J.get(it["slug"])
        if r is None:
            if verd.get(it["slug"], {}).get("verdict") == "not_member": continue  # retired by an earlier verdict
            missing.append(it["slug"]); continue
        lines.extend(r if isinstance(r, list) else [r])
    out = b.with_name(b.name.replace(".json", ".out.jsonl"))
    out.write_text("\n".join(json.dumps(l, ensure_ascii=False) for l in lines) + "\n")
    print(f"{out.name}: {len(lines)} lines; missing {missing}")
