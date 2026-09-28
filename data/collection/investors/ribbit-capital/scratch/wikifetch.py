#!/usr/bin/env python3
"""Fetch plain-text Wikipedia extracts into scratch/wiki/<Title>.txt: python3 wikifetch.py "Title" ... [--grep word]"""
import json, subprocess, sys, urllib.parse
from pathlib import Path
D = Path(__file__).resolve().parent / "wiki"
args = sys.argv[1:]
g = None
if "--grep" in args:
    i = args.index("--grep"); g = args[i + 1].lower(); args = args[:i] + args[i + 2:]
for t in args:
    u = ("https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&redirects=1&format=json&titles="
         + urllib.parse.quote(t))
    r = json.loads(subprocess.run(["curl", "-s", "-A", "merit-capital research (erik@meritcapit.al)", u], capture_output=True, text=True).stdout)
    pages = r.get("query", {}).get("pages", {})
    txt = next(iter(pages.values())).get("extract", "") if pages else ""
    red = r.get("query", {}).get("redirects")
    if txt:
        (D / (t.replace(" ", "_") + ".txt")).write_text(txt)
    print(f"== {t} ({len(txt)} chars){' -> ' + red[0]['to'] if red else ''}")
    if g and txt:
        import re
        for s in re.split(r"(?<=[.!?])\s+", txt):
            if any(k in s.lower() for k in g.split("|")):
                print("   ", s[:400])
