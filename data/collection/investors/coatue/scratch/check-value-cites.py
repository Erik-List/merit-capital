#!/usr/bin/env python3
"""Re-fetch the valuation citation of every private $1B+ row and check the page names the company
(first word of the name, or the part before a bracket). Pages that block or render by script are listed apart."""
import csv, html, re, subprocess, time
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
rows = [r for r in csv.DictReader(open("data/collection/investors/coatue/companies/base.csv")) if r["status"] == "private" and r["valuation_range"] in ("1b_plus", "10b_plus", "100b_plus")]
blocked, missing, ok = [], [], 0
for r in rows:
    u = r["valuation_citation"]; name = r["name"]
    keys = {re.split(r"[ (,]", name)[0].lower(), name.lower().replace(" ", "-"), name.lower()}
    slugkey = r["slug"].split("-")[0]
    urlhit = any(k.replace(" ", "-") in u.lower() for k in keys | {slugkey})
    p = subprocess.run(["curl", "-sL", "-m", "30", "-A", UA, "-w", "\n%{http_code}", u], capture_output=True)
    b = p.stdout.decode("utf-8", "replace"); code = b.rsplit("\n", 1)[-1]
    t = html.unescape(re.sub(r"<[^>]+>", " ", b)).lower()
    if code != "200":
        (blocked if urlhit else missing).append((r["slug"], code, u))
    elif any(k in t for k in keys):
        ok += 1
    else:
        missing.append((r["slug"], code, u))
    time.sleep(0.3)
print(f"{len(rows)} rows: {ok} name found; {len(blocked)} blocked but the address names the company; {len(missing)} to read")
for m in missing: print("  READ", m[0], m[1], m[2][:120])
