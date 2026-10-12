#!/usr/bin/env python3
"""grep a cached/throttled SEC doc: python3 sg.py <url> <regex> [width] [max]"""
import sys, re
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
sys.argv, argv = sys.argv[:1], sys.argv[1:]
import secget
t = secget.get(argv[0])
w = int(argv[2]) if len(argv) > 2 else 400
mx = int(argv[3]) if len(argv) > 3 else 10
n = 0; last = -10**9
for m in re.finditer(argv[1], t, re.I):
    if m.start() - last < w: continue
    last = m.start()
    s = max(0, m.start() - w // 2)
    print("...", re.sub(r"\s+", " ", t[s:s + w]), "...\n"); n += 1
    if n >= mx: break
print(f"[{n} shown; {len(t)} chars]")
