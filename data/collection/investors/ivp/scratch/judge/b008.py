from jl import *
L=[]; V=[]
def row(slug, **k):
    d={"slug":slug}
    for x in k.pop("parts",[]): d.update(x)
    d.update(k); L.append(d)
def v(slug, verdict, cls, conf, basis, cite=None):
    d={"slug":slug,"verdict":verdict,"evidence_class":cls,"confidence":conf,"who":"agent","basis":basis}
    if cite: d["citation"]=cite
    V.append(d)
v("surf-air-global-ltd","member","formd_adjudicated","medium","Director-of-record pattern: Dennis Phelps, an IVP managing director in tenure (on IVP's fund Form Ds 2010-2024), is director of record on Surf Air Global's 2018 Form D ($9.1M sold), and the issuer resolves to a real operating company (Surf Air, the membership airline, now Surf Air Mobility). No IVP listing names it: an unannounced position, flagged for the A/B pass.")
v("unifi-software-inc","not_member","formd_adjudicated","high","T4 seat dating: Roseanne Wincek's seat on Unifi Software's 2015-Q1 filing (first sale November 2014) predates her joining IVP (announced spring 2015, after the SoFi and Pindrop investments on the firm's own news list); a prior-firm seat, and IVP never listed Unifi.")
v("whaleshark-media-inc","member","formd_adjudicated","high","WhaleShark Media, Inc. (Austin, incorporated 2007) renamed itself RetailMeNot, Inc. in 2013; RetailMeNot is on IVP's own 2013-2019 lists (Year Invested 2011) and Jules Maltz is director of record on the 2011 filing. Same investment as the retailmenot row: merge recorded.")
row("surf-air-global-ltd", status="public", parts=[country("US"), city("Los Angeles","model_knowledge","medium")], valuation_range="below_1b", flags=["needs_review"],
    note="Surf Air (Surf Air Mobility since its 2023 direct listing, NYSE: SRFM), regional air travel, Los Angeles (Santa Monica at the 2018 filing). Member on the director-of-record pattern (Dennis Phelps, 2018); to be confirmed in the A/B pass. Small cap, below $1B.")
row("turnstone-systems-inc", status="defunct", parts=[country("US"), city("Santa Clara"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Turnstone Systems, DSL equipment, Santa Clara CA. IPO 2000; wound down and liquidated in 2003, as Benchmark carries. IVP funds filed 13Gs and Form 4s 2001-2003, and it is on Redpoint's previous-by-partners list (IVP's book); entry round not on record.")
row("whaleshark-media-inc", status="acquired", parts=[city("Austin")], valuation_range="below_1b", flags=["identity_conflated"], entry_stage="Growth", entry_stage_source="model", entry_stage_confidence="medium",
    note="WhaleShark Media is RetailMeNot's former name; the retailmenot row is this company (merge recorded, applies at the rebuild). IVP's 2011 round was a $150M growth financing.")
write("../queue/batch-008.out.jsonl", L+V)
