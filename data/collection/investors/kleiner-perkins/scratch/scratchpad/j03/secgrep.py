#!/usr/bin/env python3
"""secgrep.py URL 'regex' [width]: fetch an SEC doc (cached), strip html, print matches with context."""
import sys, re, subprocess, hashlib, html
from pathlib import Path
u, pat = sys.argv[1], sys.argv[2]
w = int(sys.argv[3]) if len(sys.argv) > 3 else 300
C = Path(__file__).parent / "sec" / (hashlib.md5(u.encode()).hexdigest() + ".txt")
if not C.exists():
    raw = subprocess.run(["curl", "-s", "-A", "merit-capital research erik@meritcapit.al", u], capture_output=True).stdout.decode("latin-1")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"\s+", " ", t)
    C.write_text(t)
t = C.read_text()
print(len(t), "chars")
n = 0
for m in re.finditer(pat, t, re.I):
    s = max(0, m.start() - w); e = min(len(t), m.end() + w)
    print("---", t[s:e])
    n += 1
    if n >= int(sys.argv[4] if len(sys.argv) > 4 else 12): break
