#!/usr/bin/env python3
"""Read a press page in memory (no file saved) and print the sentences matching a regex: rd.py <url> <regex> [max]"""
import sys, re, html, subprocess
url, rx = sys.argv[1], sys.argv[2]
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 12
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
r = subprocess.run(["curl", "-sL", "-m", "40", "-A", UA, "-H", "Accept-Language: en-US,en;q=0.9", "-w", "\n%{http_code}", url], capture_output=True)
body = r.stdout.decode("utf-8", "replace")
body, _, code = body.rpartition("\n")
t = re.sub(r"<script[\s\S]*?</script>|<style[\s\S]*?</style>", " ", body)
ttl = re.search(r"<title[^>]*>(.*?)</title>", body, re.S)
t = html.unescape(re.sub(r"<[^>]+>", " ", t))
t = re.sub(r"\s+", " ", t)
print(f"http {code}; {len(t)} chars; title: {html.unescape(ttl.group(1)).strip()[:150] if ttl else ''}")
n = 0; last = -10**9
W = 260
for m in re.finditer(rx, t, re.I):
    if m.start() - last < W: continue
    last = m.start()
    print("  >", t[max(0, m.start() - W):m.start() + W]); n += 1
    if n >= mx: break
