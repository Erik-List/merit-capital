"""Fetch a page with a browser UA (no file saved) and print paragraphs matching a regex."""
import sys, re, subprocess, html
url, pat = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else r"valuation|valued|billion")
n = int(sys.argv[3]) if len(sys.argv) > 3 else 8
r = subprocess.run(["curl", "-sL", "-m", "40", "-A", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36",
                    "-H", "Accept: text/html,application/xhtml+xml", "-H", "Accept-Language: en-US,en;q=0.9", url], capture_output=True)
t = r.stdout.decode("utf-8", "replace")
print("HTTP bytes:", len(t))
m = re.search(r"<title[^>]*>(.*?)</title>", t, re.S | re.I)
print("TITLE:", html.unescape(m.group(1)).strip()[:200] if m else None)
for k in ("article:published_time", "datePublished", "og:updated_time"):
    m = re.search(k + r'["\']?\s*[:=]?\s*(?:content=)?["\']([^"\']{8,40})', t)
    if m: print(k, "=", m.group(1))
t = re.sub(r"<script[\s\S]*?</script>|<style[\s\S]*?</style>", " ", t)
paras = re.findall(r"<(?:p|li|h1|h2)[^>]*>([\s\S]*?)</(?:p|li|h1|h2)>", t)
seen = 0
for p in paras:
    p = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", p))).strip()
    if len(p) > 40 and re.search(pat, p, re.I):
        print("  >", p[:700]); seen += 1
        if seen >= n: break
print(f"[{seen} paragraph(s) shown of {len(paras)}]")
