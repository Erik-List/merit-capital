#!/usr/bin/env python3
"""Re-fetch agent-reported citation URLs and check each page loads and names what it is cited for.
Usage: verify-urls.py <out.jsonl> <field> <keyword-mode>   keyword-mode: coatue | city | none"""
import html, json, re, subprocess, sys, time
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
path, field, mode = sys.argv[1], sys.argv[2], sys.argv[3]
bad = 0
for l in open(path):
    r = json.loads(l); u = r.get(field)
    if not u: continue
    p = subprocess.run(["curl", "-sL", "-m", "40", "-A", UA, "-w", "\n%{http_code}", u], capture_output=True)
    body = p.stdout.decode("utf-8", "replace"); code = body.rsplit("\n", 1)[-1]; time.sleep(0.5)
    t = html.unescape(re.sub(r"<[^>]+>", " ", body))
    kw = {"coatue": "Coatue", "city": r.get("hq_city") or "", "none": ""}[mode]
    ok = code == "200" and (not kw or kw.lower() in t.lower())
    if not ok:
        bad += 1; print(f"  {r['slug']:24s} HTTP {code} keyword {'found' if kw and kw.lower() in t.lower() else 'MISSING'} ({kw}) {u}")
print(f"checked {path.split('/')[-1]}: {bad} to look at")
