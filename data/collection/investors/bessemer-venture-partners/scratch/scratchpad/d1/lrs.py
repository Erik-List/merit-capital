#!/usr/bin/env python3
"""Light Reading's own site search, titles + paths: python3 scratchpad/d1/lrs.py <query> [filter-regex]"""
import sys, re, html, subprocess, urllib.parse
q = sys.argv[1]
flt = sys.argv[2] if len(sys.argv) > 2 else "."
r = subprocess.run(["curl", "-sL", "-m", "40", "-A", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36",
                    "https://www.lightreading.com/search?q=" + urllib.parse.quote(q)], capture_output=True)
t = r.stdout.decode("utf-8", "replace")
seen = []
for m in re.finditer(r'<a[^>]+href="(/[a-z0-9-]+/[a-z0-9-]+)"[^>]*>([\s\S]*?)</a>', t):
    path, txt = m.group(1), re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", m.group(2)))).strip()
    if txt and (path, txt) not in seen and len(txt) > 8:
        seen.append((path, txt))
dates = re.findall(r'"articleDate":"([^"]+)"|data-testid="[^"]*date[^"]*"[^>]*>([^<]+)<', t)
print(f"## {q}: {len(seen)} links")
for p, x in seen:
    if re.search(flt, x + " " + p, re.I):
        print("  ", p, "|", x[:110])
