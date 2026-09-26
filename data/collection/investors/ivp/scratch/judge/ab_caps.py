import json
from jl import *
caps=json.load(open("../caps/caps.json"))
def band(u):
    return "100b_plus" if u>=1e11 else "10b_plus" if u>=1e10 else "1b_plus" if u>=1e9 else "below_1b"
L=[]
for slug,c in caps.items():
    usd=c["usd"]; note_extra=""
    if slug=="wise":
        usd=11834364577
        note_extra=" GBP 8.93B @ ECB 2026-09-25 (GBP/EUR 0.86045, EUR/USD 1.1403) = $11.83B (scripts/fx-convert.py); LSE listing, so no SEC float."
    b=band(usd)
    edge=""
    for e in (1e9,1e10,1e11):
        if abs(usd-e)/e<=0.05: edge=f" Within 5% of the ${e/1e9:.0f}B band edge."
    d={"slug":slug,"status":"public","valuation_usd":usd,"valuation_source":"web_verified","valuation_citation":c["url"],
       "valuation_asof":c["asof"],"valuation_range":b,"valuation_confidence":"high",
       "note":f"A/B cap pass: market cap ${usd/1e9:.2f}B as of {c['asof']} (stockanalysis.com), superseding the float layer's reading.{note_extra}{edge}"}
    L.append(d)
# point fixes from the in-flight verify
L.append({"slug":"compass","status":"public","note":"Compass is listed (NYSE: COMP); the float layer's acquired reading is stale."})
L.append({"slug":"niantic","valuation_usd":None,"valuation_source":None,"valuation_asof":None,"note":"The unicorn-list figure is cleared: Niantic's games business was sold to Scopely in 2025, so the row reads acquired with no standalone mark."})
L.append({"slug":"superhuman","hq_country":"US","hq_country_source":"model_knowledge","hq_country_confidence":"high","flags":["model_disputes_source"],"note":"Country US; the Wikidata string belonged to Grammarly's article."})
L.append({"slug":"inspirato","valuation_range":"below_1b","note":"Acquired, so below $1B with no standalone mark, as First Round carries."})
write("../queue/ab-caps.out.jsonl", L)
