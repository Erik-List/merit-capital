"""TechCrunch's own search: print result links whose URL matches a regex."""
import sys, re, subprocess, urllib.parse
q, pat = sys.argv[1], sys.argv[2]
r = subprocess.run(["curl", "-sL", "-m", "40", "-A", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128.0 Safari/537.36",
                    "https://techcrunch.com/?s=" + urllib.parse.quote_plus(q)], capture_output=True)
t = r.stdout.decode("utf-8", "replace")
for u in dict.fromkeys(re.findall(r'href="(https://techcrunch\.com/20\d\d/[^"]+)"', t)):
    if re.search(pat, u, re.I):
        print(u)
