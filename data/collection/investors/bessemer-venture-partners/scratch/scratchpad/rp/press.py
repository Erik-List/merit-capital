#!/usr/bin/env python3
"""press.py [keys-prefix]: titles in news-extra-rp.json whose text matches no base name."""
import json, re, sys
from pathlib import Path
H = Path(__file__).resolve().parents[2]
b = json.load(open(H.parent / "companies" / "base.json"))
d = json.load(open(H / "news-extra-rp.json"))
def norm(s): return re.sub(r"[^a-z0-9 ]", "", (s or "").lower())
names = set()
for r in b:
    n = norm(r["name"]); names.add(n)
    n2 = re.sub(r"\b(inc|llc|ltd|corp|corporation|technologies|labs|ai|health|security|io|com)\b", "", n).strip()
    if len(n2) >= 4: names.add(n2)
    names.add(norm(r["slug"].replace("-", " ")))
names = {n for n in names if len(n) >= 4}
pref = sys.argv[1] if len(sys.argv) > 1 else "rp-20"
seen = set(); out = []
for k, v in d.items():
    if not any(k.startswith(p) for p in pref.split(",")): continue
    for i in v:
        t = i["title"]
        if t in seen: continue
        seen.add(t)
        nt = " " + norm(t) + " "
        if any((" " + n + " ") in nt or (" " + n + "s ") in nt for n in names): continue
        if not re.search(r"(?i)bessemer|bvp", t + " " + i.get("query", "")): continue
        out.append((i["date"], i["source"], t))
print(len(seen), "titles;", len(out), "with no base name")
for x in sorted(out): print(" ", x[0], "|", x[1][:22], "|", x[2][:170])
