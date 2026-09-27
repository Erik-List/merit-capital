#!/usr/bin/env python3
"""Route judged lines to the batch each slug belongs to: split.py <file> [...]
writes/extends scratch/judge/bNNN.txt per batch (a line already present for a
slug is replaced), then prints which batches are complete."""
import json, sys, glob, re
from pathlib import Path
INV = Path(__file__).resolve().parents[2]
where = {}
for f in sorted(glob.glob(str(INV / "scratch/queue/batch-[0-9][0-9][0-9].json"))):
    n = int(re.search(r"batch-(\d+)", f).group(1))
    for it in json.load(open(f)):
        where[it["slug"]] = n
lines = {}
for src in sys.argv[1:]:
    for raw in open(src):
        if raw.strip() and not raw.lstrip().startswith("#"):
            lines[raw.split("|")[0].strip()] = raw.rstrip("\n")
by = {}
for s, l in lines.items():
    if s not in where:
        print("not in queue:", s); continue
    by.setdefault(where[s], {})[s] = l
for n, new in sorted(by.items()):
    p = INV / f"scratch/judge/b{n:03d}.txt"
    have = {}
    if p.exists():
        for raw in open(p):
            if raw.strip():
                have[raw.split("|")[0].strip()] = raw.rstrip("\n")
    have.update(new)
    p.write_text("\n".join(have.values()) + "\n")
    want = {it["slug"] for it in json.load(open(INV / f"scratch/queue/batch-{n:03d}.json"))}
    miss = want - set(have)
    print(f"b{n:03d}: {len(have)} lines, {'complete' if not miss else f'{len(miss)} missing'}")
