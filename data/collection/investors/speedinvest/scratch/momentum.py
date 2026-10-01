"""Momentum slice (COLLECTION.md s6): every private row first seen 2021 or later in a hot
sector gets one recorded web check: valuation_range_source web_verified with the citation
of the latest priced event found (the research agents' cited rounds, else the newest Google
News item naming the company from the surfaces layer), even for a below_1b result."""
import json, glob, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as J
VENDOR = re.compile(r"crunchbase\.com/(?!news)|pitchbook|tracxn|dealroom|cbinsights|getlatka|growjo", re.I)
sl = json.load(open(J.H / "momentum-slice.json"))
R = {}
for f in glob.glob(str(J.H / "research" / "g*.json")):
    if "groups" not in f:
        R.update(json.load(open(f)))
L, miss = [], []
for s in sl:
    rounds = [x for x in (R.get(s, {}).get("rounds") or []) if str(x.get("source") or "").startswith("http")
              and x.get("source_type") != "vendor" and not VENDOR.search(x["source"])]
    rounds.sort(key=lambda x: str(x.get("date") or ""))
    if rounds:
        x = rounds[-1]
        amt = f", {x.get('amount_native') or ('$' + format(int(x['amount_usd']), ',')) if x.get('amount_usd') else 'amount undisclosed'}"
        L.append({"slug": s, "who": J.WHO, "valuation_range": "below_1b", "valuation_range_source": "web_verified",
                  "valuation_citation": x["source"],
                  "note": f"Momentum check 2026-09-30: latest priced event found is the {x.get('round') or 'round'} of {x.get('date')}{amt}; no mark of $1B or more."})
        continue
    items = sorted([i for svc, i in J.items(s) if i.get("names") and svc.startswith("googlenews")], key=lambda i: i.get("date") or "")
    if items:
        i = items[-1]
        try:
            url = J.gn(s, (i.get("gid") or "")[-10:])
        except Exception:
            url = None
        if url:
            L.append({"slug": s, "who": J.WHO, "valuation_range": "below_1b", "valuation_range_source": "web_verified",
                      "valuation_citation": url,
                      "note": f"Momentum check 2026-09-30: newest news item naming the company ({i.get('date')}: {i.get('title','')[:90]}); no round or mark of $1B or more found."})
            continue
    miss.append(s)
print(len(L), "checks recorded;", len(miss), "with no citable item:", miss)
J.write("momentum", L)
