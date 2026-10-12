import json, sys, re
from pathlib import Path
INV = Path("/Users/erik/Developer/merit-capital/data/collection/investors")
def key(n):
    n = re.sub(r"[.,'’]", "", (n or "").lower())
    n = re.sub(r"\b(inc|corp|corporation|co|ltd|llc|plc|labs|technologies|technology|ai|io|com|software|holdings|group)\b", "", n)
    return re.sub(r"[^a-z0-9]+", " ", n).strip()
want = {key(a) for a in sys.argv[1:]}
full = "--full" in sys.argv
for d in sorted(INV.iterdir()):
    if d.name == "kleiner-perkins": continue
    b = d/"companies/base.json"; c = d/"companies/classification.json"
    if not b.exists() or not c.exists(): continue
    try:
        base = json.loads(b.read_text()); cl = json.loads(c.read_text())
    except Exception: continue
    for r in base:
        if key(r.get("name")) in want:
            x = cl.get(r["slug"], {})
            keys = ["status","valuation_range","valuation_usd","valuation_asof","valuation_citation","entry_stage","entry_stage_source","entry_stage_citation","entry_date","hq_city","hq_country","focus","seed_to_a_graduation","graduation_citation"]
            print(f"== {d.name}:{r['slug']} ({r.get('name')})")
            for k in keys:
                if x.get(k) not in (None,""): print(f"   {k}: {x[k]}")
            if x.get("funding_rounds"): print("   rounds:", json.dumps(x["funding_rounds"])[:1200])
            if x.get("note"): print("   note:", x["note"][:900 if not full else 5000])
