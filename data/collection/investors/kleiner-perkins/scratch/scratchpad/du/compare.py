import json
blind=json.load(open("scratchpad/du/blind.json"))
res=json.load(open("../companies/resolved.json"))
cl=json.load(open("../companies/classification.json"))
print(type(cl), len(cl))
def merged(s):
    d=dict(res.get(s) or {}); d.update(cl.get(s) or {}); return d
F=("status","valuation_range","entry_stage","hq_country","hq_city","focus")
dis=[]
for s,b in blind.items():
    m=merged(s)
    for f in F:
        if (b[f] or None)!=(m.get(f) or None):
            dis.append((s,f,b[f],m.get(f)))
for d in dis: print(d)
print(len(dis))
json.dump(dis, open("scratchpad/du/dis-raw.json","w"), indent=1)
