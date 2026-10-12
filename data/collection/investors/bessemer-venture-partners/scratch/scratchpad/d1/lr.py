#!/usr/bin/env python3
"""Print the text of a web page (no file kept): python3 scratchpad/d1/lr.py <url> [regex|BODY] [width]
BODY prints the article body from the start (Light Reading: after the nav). A regex prints up to 3 windows."""
import sys, re, html, subprocess
u = sys.argv[1]
pat = sys.argv[2] if len(sys.argv) > 2 else "BODY"
w = int(sys.argv[3]) if len(sys.argv) > 3 else 1500
r = subprocess.run(["curl", "-sL", "-m", "40", "-A", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36", u], capture_output=True)
t = r.stdout.decode("utf-8", "replace")
t = re.sub(r"<script[\s\S]*?</script>|<style[\s\S]*?</style>", " ", t)
t = html.unescape(re.sub(r"<[^>]+>", " ", t)); t = re.sub(r"\s+", " ", t)
i = t.rfind("Light Reading Resource Library")
if i > 0:
    t = t[i + 30:]
    j = t.find("Read more about")
    k = t.find("You May Also Like")
    cut = min([x for x in (j, k) if x > 0] or [len(t)])
    t = t[:cut]
print(f"[{len(t)} chars] {u}")
if pat == "BODY":
    print(t[:w])
else:
    n = 0
    for m in re.finditer(pat, t, re.I):
        s = max(0, m.start() - w // 3)
        print("...", t[s:s + w], "...\n"); n += 1
        if n >= 3: break
