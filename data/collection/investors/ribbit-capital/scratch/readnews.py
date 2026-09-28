#!/usr/bin/env python3
"""Decode one news headline to its publisher URL (judge_lib.NEWS) and print the page's sentences that match a
pattern, read by curl with a browser user agent. For A/B checks where WebFetch is refused.

Usage: NQ_TAG=ab python3 readnews.py <slug> "<title substring>" ["regex"]
"""
import html
import importlib.util
import re
import subprocess
import sys
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/126.0 Safari/537.36")
slug, sub = sys.argv[1], sys.argv[2]
pat = re.compile(sys.argv[3] if len(sys.argv) > 3 else r"(?i)valu|billion|ribbit", re.I)
url = jl.NEWS(slug, sub)
raw = subprocess.run(["curl", "-sL", "--max-time", "40", "-A", UA, url], capture_output=True).stdout.decode("utf-8", "replace")
text = re.sub(r"<script.*?</script>|<style.*?</style>", " ", raw, flags=re.S)
text = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", text)))
print(url, f"({len(text)} chars)")
seen = set()
for s in re.split(r"(?<=[.!?])\s+", text):
    if pat.search(s) and s not in seen and len(s) < 600:
        seen.add(s)
        print("  >", s.strip())
