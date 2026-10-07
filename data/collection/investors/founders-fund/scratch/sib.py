"""What sibling books say about a company: status, band, figure, as-of, citation, city.
usage: sib.py name1,name2,...   (matches on a loose name key against every other investor's published rows)"""
import csv, json, re, sys
from pathlib import Path
INV = Path(__file__).resolve().parents[2]
def k(s): return re.sub(r"[^a-z0-9]", "", re.sub(r"\b(inc|corp|corporation|llc|ltd|technologies|labs|holdings|the)\b\.?", "", s.lower()))
want = {k(n): n for n in sys.argv[1].split(",")}
hits = {w: [] for w in want}
for d in sorted(INV.iterdir()):
    if d.name == "founders-fund" or not (d / "companies/base.csv").exists(): continue
    try: cl = json.loads((d / "companies/classification.json").read_text())
    except Exception: cl = {}
    for r in csv.DictReader(open(d / "companies/base.csv", encoding="utf-8")):
        kk = k(r.get("name", ""))
        if kk in want:
            c = cl.get(r.get("slug"), {})
            hits[kk].append((r.get("valuation_asof") or "", d.name, r.get("status"), r.get("valuation_range"), r.get("valuation_usd"),
                             c.get("valuation_citation") or "", r.get("hq_city"), r.get("hq_country")))
for kk, hs in hits.items():
    if not hs: print(f"{want[kk]}: -"); continue
    hs.sort(reverse=True)
    a = hs[0]
    others = "; ".join(f"{h[1]}:{h[2]}/{h[3]}/{(float(h[4])/1e9 if h[4] else 0):.2f}@{h[0]}" for h in hs[1:4])
    print(f"{want[kk]}: {a[1]} {a[2]}/{a[3]} ${(float(a[4])/1e9 if a[4] else 0):.2f}B asof {a[0]} | {a[6]},{a[7]} | {a[5][:110]} || {others}")
