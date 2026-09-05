#!/usr/bin/env python3
"""After a batch records: null the band-derived graduation on rows whose judged stage is not Seed, and flag
cohort_unverified on Seed rows whose graduation leg came from knowledge. Writes and records fix-<n>.out.jsonl."""
import json, subprocess, sys
from pathlib import Path
I = Path("/Users/erik/Developer/merit-capital/data/collection/investors/union-square-ventures")
res = json.load(open(I / "resolved.json")); cls = json.load(open(I / "classification.json"))
fix = []
for slug, c in cls.items():
    merged = {**res.get(slug, {}), **{k: v for k, v in c.items() if v is not None}}
    if merged.get("entry_stage") and merged["entry_stage"] != "Seed" and merged.get("seed_to_a_graduation") is not None:
        fix.append({"slug": slug, "who": "agent-judge-pro86", "seed_to_a_graduation": None, "graduation_source": None, "graduation_confidence": None, "note": "graduation nulled: the entry is not Seed (band-derived cohort membership retired)"})
    if merged.get("entry_stage") == "Seed" and merged.get("graduation_source") == "model" and "cohort_unverified" not in (c.get("flags") or []):
        fix.append({"slug": slug, "who": "agent-judge-pro86", "flags": ["cohort_unverified"], "note": "cohort leg from knowledge, not yet verified"})
n = len(list((I / "scratch/queue").glob("fix-*.out.jsonl"))) + 1
out = I / "scratch/queue" / f"fix-{n:03d}.out.jsonl"
if fix:
    out.write_text("\n".join(json.dumps(x) for x in fix) + "\n")
    print("fixes:", [(x["slug"], "grad-null" if "seed_to_a_graduation" in x else "cohort-flag") for x in fix])
    subprocess.run([sys.executable, "/Users/erik/Developer/merit-capital/scripts/run.py", "record", "--investor", "union-square-ventures", str(out)], check=True)
else:
    print("no fixes needed")
