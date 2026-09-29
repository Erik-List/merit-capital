#!/usr/bin/env python3
"""Google News through graduation-surfaces.py's own googlenews() (paced, uncapped): python3 scratch/gn.py "query" [needle] [--n 10] [--decode k]"""
import importlib.util, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
args = [a for a in sys.argv[1:]]
n = 10
if "--n" in args:
    n = int(args[args.index("--n") + 1]); del args[args.index("--n"):args.index("--n") + 2]
dec = None
if "--decode" in args:
    dec = int(args[args.index("--decode") + 1]); del args[args.index("--decode"):args.index("--decode") + 2]
sys.argv = ["x"]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts/graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec); spec.loader.exec_module(gs)
q = args[0]; needle = args[1] if len(args) > 1 else q.split('"')[1] if '"' in q else q.split()[0]
res = gs.googlenews(q, needle)
items = sorted(res.get("items") or [], key=lambda i: i.get("date") or "")
print(res.get("status"), len(items))
for k, i in enumerate(items[-n:]):
    link = i.get("link") or ""
    if dec is not None and (dec == -1 or k == dec) and i.get("gid"):
        link = gs.decode(i["gid"]) if hasattr(gs, "decode") else link
    print(f"  {(i.get('date') or '')[:10]} {(i.get('title') or '')[:140]} {link}")
