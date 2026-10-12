import json,sys,glob,os
from pathlib import Path
INV=Path("/Users/erik/Developer/merit-capital/data/collection/investors")
sib=json.load(open(INV/"kleiner-perkins/scratch/siblings.json"))
cache={}
def cls(inv):
    if inv not in cache:
        p=INV/inv/"companies/classification.json"
        c=json.load(open(p)) if p.exists() else {}
        cache[inv]=c.get(inv,c)
    return cache[inv]
for s in sys.argv[1:]:
    print("=====",s)
    for x in sib.get(s,[]):
        inv=x["investor"]
        # find row by slug or name
        c=cls(inv)
        row=c.get(s)
        if row is None:
            for k,v in c.items():
                if isinstance(v,dict) and (v.get("name")==x.get("name")):
                    row=v;break
        row=row or {}
        print(f"-- {inv}: {x['status']}/{x['range']}/{x['usd']}@{x['asof']} cite={x['val_cite']} stage={x['stage']}({x['stage_src']}) {x['city']},{x['country']}")
        if row.get("entry_stage_citation"): print("   stage_cite:",row.get("entry_stage_citation"), row.get("entry_date"))
        if row.get("note"): print("   note:",row["note"][:700])
