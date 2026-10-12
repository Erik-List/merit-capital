import sys, re, html, subprocess
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
url = sys.argv[1]; kws = sys.argv[2:]
r = subprocess.run(["curl", "-sL", "-m", "40", "-A", UA, "-H", "Accept: text/html", "-w", "\n__HTTP__%{http_code}", url], capture_output=True)
t = r.stdout.decode("utf-8", "ignore")
code = t.rsplit("__HTTP__", 1)[-1]
t = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", t)
m = re.search(r"(?is)<title>(.*?)</title>", t)
print("HTTP", code, "| TITLE:", html.unescape(m.group(1)).strip()[:160] if m else None)
x = html.unescape(re.sub(r"<[^>]+>", " ", t)); x = re.sub(r"\s+", " ", x)
print("LEN", len(x))
for k in kws:
    for mm in list(re.finditer(re.escape(k), x, re.I))[:4]:
        print(f"  [{k}] ...{x[max(0, mm.start()-260):mm.end()+260]}...")
