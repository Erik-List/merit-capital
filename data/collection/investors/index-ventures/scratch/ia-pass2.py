#!/usr/bin/env python3
"""A SMALL second pass over the Internet Archive for the 2002-2007 database site: one capture per sector list per
year is enough, because every company page of a sector shows the whole sector list in its side menu. Picks at most
N targets (default 26) from the same CDX enumeration ia-pass.py uses, preferring the list pages themselves
(ivw_port_detail_all.cgi, typ=it / typ=ls) and then company pages spread across the id range of each year.
Four seconds between requests; stops at the first refusal. Results go into scratch/ia-pass.json like ia-pass.py's."""
import gzip, hashlib, json, re, sys, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parents[4] / "scripts"))
import ia, ia_fetch  # noqa: E402
N = int(sys.argv[1]) if len(sys.argv) > 1 else 26
OUT = HERE / "ia-pass.json"
res = json.loads(OUT.read_text()) if OUT.exists() else {}
enum = json.load(gzip.open(HERE.parents[4] / "data" / "filings" / "index-ventures" / "cdx-enum.json.gz", "rt"))["indexventures.com"]["rows"]
by = {}
for o, ts, sc, mt in enum:
    if sc != "200": continue
    u = o.replace("&amp;", "&"); low = u.lower()
    if "ivw_port_detail" in low or re.search(r"indexventures\.com(:80)?/portfolio$", low) or re.search(r"/index\.php/portfolio$", low) \
            or re.search(r"/portfolio/index/industry_id/2/company_status/(current|exited)$", low):
        by.setdefault(ts[:4], []).append((ts, u))
targets = []
for y in sorted(by):
    rows = sorted(set(by[y]))
    lists = [r for r in rows if "spgid=" not in r[1]]
    pages = sorted([r for r in rows if "spgid=" in r[1]], key=lambda r: int(re.search(r"spgid=(\d+)", r[1]).group(1)))
    if y == "2002":
        pages = [r for r in pages if re.search(r"spgid=(22|23)$", r[1])]            # the one sector list of Nov 2002 not read yet
    else:
        step = max(1, len(pages) // 4)
        pages = pages[::step][:5]
    targets += lists[:3] + pages
targets = [t for t in targets if res.get(f"{t[0]} {t[1]}", {}).get("status") != "ok"][:N]
print(len(targets), "targets:", [f"{t[0][:4]} {t[1][-34:]}" for t in targets], flush=True)
ok = 0
for ts, url in targets:
    if ia_fetch.blocked() > 0:
        print("IA cooldown, stopping", flush=True); break
    k = f"{ts} {url}"
    try:
        body = ia.replay(ts, url)
        res[k] = {"status": "ok", "bytes": len(body), "cache": hashlib.sha1(k.encode()).hexdigest() + ".html"}; ok += 1
    except Exception as e:
        res[k] = {"status": f"failed {str(e)[:80]}"}
        print("failed", k[:90], str(e)[:80], flush=True)
    OUT.write_text(json.dumps(res, indent=1))
    time.sleep(4)
print(ok, "fetched this pass;", sum(1 for v in res.values() if isinstance(v, dict) and v.get("status") == "ok"), "ok in all", flush=True)
