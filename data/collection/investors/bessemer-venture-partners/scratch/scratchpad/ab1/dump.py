import json, sys
from pathlib import Path
H = Path(__file__).resolve().parents[2]
slugs = json.loads((H/"queue"/"ab-priv-1.json").read_text())
cl = json.loads((H.parent/"companies"/"classification.json").read_text()); cl = cl.get("bessemer-venture-partners", cl)
rs = json.loads((H.parent/"companies"/"resolved.json").read_text()); rs = rs.get("bessemer-venture-partners", rs)
want = sys.argv[1:] or slugs
for s in want:
    st = {**(rs.get(s) or {}), **(cl.get(s) or {})}
    print("###", s)
    for k in ("status","valuation_range","valuation_usd","valuation_source","valuation_range_source","valuation_asof","valuation_citation",
              "entry_stage","entry_stage_source","entry_stage_citation","entry_stage_confidence","entry_date","flags","hq_country","hq_city","focus"):
        if st.get(k) not in (None,"",[]): print("  ",k,"=",st.get(k))
    for r in st.get("funding_rounds") or []: print("   round:", r)
    print("   note:", st.get("note"))
