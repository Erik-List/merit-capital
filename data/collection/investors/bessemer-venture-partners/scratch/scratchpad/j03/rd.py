import sys, re, html, subprocess
url, pat = sys.argv[1], sys.argv[2]
w = int(sys.argv[3]) if len(sys.argv) > 3 else 350
r = subprocess.run(["curl", "-sL", "-m", "40", "--compressed", "-A", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36", "-H", "Accept: text/html", url], capture_output=True)
t = r.stdout.decode("utf-8", "replace")
t = re.sub(r"<script[\s\S]*?</script>|<style[\s\S]*?</style>", " ", t)
x = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t)))
print(f"[{len(x)} chars]")
n = 0
last = -10**9
for m in re.finditer(pat, x, re.I):
    if m.start() - last < w: continue
    last = m.start()
    print("...", x[max(0, m.start() - w):m.start() + w], "...\n")
    n += 1
    if n >= 4: break
