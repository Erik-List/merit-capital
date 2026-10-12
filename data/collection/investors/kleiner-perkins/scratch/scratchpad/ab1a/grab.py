import sys, re, subprocess, html
url, pat = sys.argv[1], sys.argv[2]
n = int(sys.argv[3]) if len(sys.argv) > 3 else 12
r = subprocess.run(["curl", "-sL", "--max-time", "30", "-A", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36", url], capture_output=True)
t = r.stdout.decode("utf-8", "ignore")
t = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", t)
t = html.unescape(re.sub(r"(?s)<[^>]+>", " ", t))
t = re.sub(r"\s+", " ", t)
print(f"[{len(t)} chars] {url}")
seen = set()
for s in re.split(r"(?<=[.!?])\s+", t):
    if re.search(pat, s, re.I) and s not in seen and len(s) < 900:
        seen.add(s); print("  >", s.strip()[:700]); n -= 1
        if n <= 0: break
