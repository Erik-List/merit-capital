#!/usr/bin/env python3
"""Open a sweep headline: decode its Google News id to the publisher's URL, fetch the page and print
the passages naming Coatue and round words. Usage: open-hit.py <slug> <title substring> [extra regex]"""
import html, importlib.util, json, re, subprocess, sys, time
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]; INV = ROOT / "data/collection/investors/coatue"
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec); argv = sys.argv[1:]; sys.argv = sys.argv[:1]; spec.loader.exec_module(gs)
slug, sub = argv[0], argv[1].lower(); extra = argv[2] if len(argv) > 2 else None
S = json.load(open(INV / "scratch/stage-sweep.json"))
h = next((h for h in S[slug]["hits"] if sub in h["title"].lower()), None)
if not h: sys.exit(f"no hit {sub!r} for {slug}")
url = gs.decode(h["gid"])
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
p = subprocess.run(["curl", "-sL", "-m", "40", "-A", UA, "-w", "\n%{http_code}", url or ""], capture_output=True)
b = p.stdout.decode("utf-8", "replace"); code = b.rsplit("\n", 1)[-1]
t = html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>|<style.*?</style>", "", b, flags=re.S | re.I))); t = re.sub(r"\s+", " ", t)
print(f"{slug} | {h['date']} | HTTP {code} | {url}")
pats = ["Coatue"] + ([extra] if extra else [])
for pat in pats:
    last = -999; n = 0
    for m in re.finditer(pat, t):
        if m.start() - last < 350: continue
        last = m.start(); n += 1
        print(f"   [{pat}] ...{t[max(0, m.start() - 220):m.start() + 230]}...")
        if n >= 3: break
    if n == 0: print(f"   [{pat}] no hit")
