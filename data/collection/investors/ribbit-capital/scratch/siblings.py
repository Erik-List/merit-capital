#!/usr/bin/env python3
"""What sibling books already say about the companies in this base (rule 10 alignment
aid): status, band, figure with as-of, entry stage, HQ. Output scratch/siblings.json."""
import csv, glob, json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
def loose(s):
    s = re.sub(r"\b(inc|ltd|limited|gmbh|ab|sa|plc|llc|corp|corporation|co|group|holdings|technologies|technology|labs)\b\.?", "", (s or "").lower())
    return re.sub(r"[^a-z0-9]+", "", s)
mine = json.load(open(HERE.parent / "companies" / "base.json"))
keys = {loose(r["name"]): r["slug"] for r in mine}
out = {}
for f in sorted(glob.glob(str(ROOT / "data/collection/investors/*/companies/base.csv"))):
    inv = f.split("/investors/")[1].split("/")[0]
    if inv == "ribbit-capital":
        continue
    for r in csv.DictReader(open(f)):
        k = loose(r["name"])
        if k in keys and len(k) > 2:
            out.setdefault(keys[k], []).append({"investor": inv, "name": r["name"], "status": r["status"],
                "range": r["valuation_range"], "usd": r["valuation_usd"], "asof": r["valuation_asof"],
                "val_cite": r["valuation_citation"], "stage": r["entry_stage"], "stage_src": r["entry_stage_source"],
                "city": r["hq_city"], "country": r["hq_country"], "focus": r["focus"], "verdict": r["membership_verdict"]})
json.dump(out, open(HERE / "siblings.json", "w"), indent=1, ensure_ascii=False)
print(len(out), "of", len(mine), "rows are shared with a sibling book")
for s, v in sorted(out.items()):
    print(s, "|", "; ".join(f"{x['investor']}:{x['status']}/{x['range']}/{x['usd'] or '-'}@{x['asof'] or '-'}/{x['stage']}/{x['city']},{x['country']}/{x['focus']}" for x in v))
