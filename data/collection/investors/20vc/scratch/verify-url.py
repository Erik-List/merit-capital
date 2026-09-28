#!/usr/bin/env python3
"""Fetch a URL and print the sentences naming the firm (and optional extra
terms), so a citation is used only after its page is read. Records every check
in scratch/research/url-checks.json (url -> status, sentences).
Usage: python3 verify-url.py URL [URL ...] [--terms "seed|Series A"]"""
import html, json, re, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
OUT = HERE / "research" / "url-checks.json"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")
args = sys.argv[1:]
extra = ""
if "--terms" in args:
    i = args.index("--terms"); extra = args[i + 1]; del args[i:i + 2]
pat = re.compile(r"20\s?VC|Twenty ?Minute|Stebbings" + (("|" + extra) if extra else ""), re.I)
data = json.loads(OUT.read_text()) if OUT.exists() else {}
for url in args:
    try:
        r = subprocess.run(["curl", "-s", "-L", "--max-time", "30", "-A", UA, "-w", "\n%{http_code}", url],
                           capture_output=True, timeout=45)
        body, _, code = r.stdout.decode("utf-8", "replace").rpartition("\n")
    except subprocess.TimeoutExpired:
        body, code = "", "timeout"
    t = re.sub(r"<(script|style|noscript)\b.*?</\1>", " ", body, flags=re.S | re.I)
    t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t)))
    sents = [s.strip() for s in re.split(r"(?<=[.!?])(?<!\d\.)\s+", t) if pat.search(s) and 15 < len(s) < 600]
    data[url] = {"http": code, "sentences": sents[:10]}
    print(f"== [{code}] {url}")
    for s in sents[:6]:
        print("   >", s[:320])
OUT.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
