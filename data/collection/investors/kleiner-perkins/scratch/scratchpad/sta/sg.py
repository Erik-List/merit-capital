#!/usr/bin/env python3
"""sg.py <url> [regex] [width] [max]: distinct windows around regex matches in an SEC doc (via secget.get, throttled+cached)."""
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import secget
url = sys.argv[1]
rx = sys.argv[2] if len(sys.argv) > 2 else r"Kleiner|KPCB"
w = int(sys.argv[3]) if len(sys.argv) > 3 else 500
mx = int(sys.argv[4]) if len(sys.argv) > 4 else 12
t = secget.get(url)
last = -10**9; n = 0
for m in re.finditer(rx, t, re.I):
    if m.start() < last + w:   # skip overlapping windows
        continue
    s = max(0, m.start() - w // 3)
    print(f"[{m.start()}] ...", re.sub(r"\s+", " ", t[s:s + w]), "...\n")
    last = m.start(); n += 1
    if n >= mx: break
print(f"[{n} windows; doc {len(t)} chars]")
