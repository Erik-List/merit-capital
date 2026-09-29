#!/usr/bin/env python3
"""Fetch article URLs and print the sentences that name Northzone or a round (for verifying a citation
before it is written). Cached in data/filings/northzone/articles. Usage: read-articles.py url..."""
import hashlib, re, subprocess, sys, html
from pathlib import Path
C = Path(__file__).resolve().parents[5] / "data" / "filings" / "northzone" / "articles"; C.mkdir(parents=True, exist_ok=True)
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
for u in sys.argv[1:]:
    f = C / (hashlib.sha1(u.encode()).hexdigest() + ".html")
    if not f.exists():
        r = subprocess.run(["curl", "-sL", "--max-time", "30", "-A", UA, u], capture_output=True)
        f.write_bytes(r.stdout)
    t = html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>|<style.*?</style>", "", f.read_text(errors="replace"), flags=re.S)))
    t = re.sub(r"\s+", " ", t)
    s = [x for x in re.split(r"(?<=[.!?])\s+", t) if re.search(r"(?i)northzone|seed|series [a-f]\b|\bround\b|led by|valuation", x)]
    print("==", u[:110], f"({len(t)} chars)")
    for x in s[:5]: print("   >", x[:260])
