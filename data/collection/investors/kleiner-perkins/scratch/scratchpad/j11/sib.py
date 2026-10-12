import json, sys, re
from pathlib import Path
ROOT = Path("/Users/erik/Developer/merit-capital/data/collection/investors")
pat = re.compile(sys.argv[1], re.I)
keys = sys.argv[2].split(",") if len(sys.argv) > 2 else ["status","valuation_usd","valuation_asof","valuation_citation","entry_stage","entry_stage_source","entry_stage_citation","entry_date","hq_city","note","funding_rounds"]
for inv in sorted(ROOT.iterdir()):
    if inv.name == "kleiner-perkins": continue
    f = inv / "companies" / "classification.json"
    if not f.exists(): continue
    d = json.loads(f.read_text())
    rows = d.values() if isinstance(d, dict) else d
    for r in rows:
        if not isinstance(r, dict): continue
        if pat.fullmatch(r.get("name") or "") or pat.fullmatch(r.get("slug") or ""):
            print("==", inv.name, r.get("slug"), r.get("name"))
            for k in keys:
                if r.get(k) not in (None, "", []):
                    print("  ", k, ":", json.dumps(r.get(k), ensure_ascii=False)[:700])
