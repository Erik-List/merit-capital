import csv, glob, json, re, sys
from pathlib import Path
ROOT = Path('/Users/erik/Developer/merit-capital')
def loose(s):
    s = re.sub(r"\b(inc|ltd|limited|gmbh|ab|sa|plc|llc|corp|corporation|co|group|holdings|technologies|technology|labs)\b\.?", "", (s or "").lower())
    return re.sub(r"[^a-z0-9]+", "", s)
names = {"k2-space":"K2 Space","labelbox":"Labelbox","magic-leap":"Magic Leap","mashgin":"Mashgin","mind-robotics":"Mind Robotics","mirendil":"Mirendil","modern-health":"Modern Health","motive":"Motive","netlify":"Netlify","newlimit":"NewLimit","newsela":"Newsela","nexthop-ai":"Nexthop AI","openevidence":"OpenEvidence","parallel":"Parallel","persona":"Persona","pilot":"Pilot","plaid":"Plaid","productboard":"Productboard","profound":"Profound","qumulo":"Qumulo","rebellion-defense":"Rebellion Defense","rippling":"Rippling","rogo":"Rogo","saronic-technologies":"Saronic Technologies","sierra":"Sierra","stord":"Stord","stripe":"Stripe","synthesia":"Synthesia","teleport":"Teleport","together-ai":"Together.ai","toss":"Toss","transcarent":"Transcarent","turo":"Turo","viz-ai":"Viz.ai","watershed":"Watershed","waymo":"Waymo","xendit":"Xendit"}
want = set(sys.argv[1:]) or set(names)
keys = {loose(v): k for k, v in names.items() if k in want}
keys.update({"togetherai": "together-ai", "together": "together-ai", "vizai":"viz-ai","viz":"viz-ai","saronic":"saronic-technologies","nexthop":"nexthop-ai","vivarepublica":"toss","keeptruckin":"motive","k2":"k2-space"})
keys = {k:v for k,v in keys.items() if v in want}
for f in sorted(glob.glob(str(ROOT / "data/collection/investors/*/companies/base.csv"))):
    inv = f.split("/investors/")[1].split("/")[0]
    if inv == "kleiner-perkins": continue
    for r in csv.DictReader(open(f)):
        k = loose(r["name"])
        if k in keys:
            print(f"{keys[k]} | {inv} | {r['name']} | {r['status']}/{r['valuation_range']}/{r['valuation_usd']}@{r['valuation_asof']} | vcite={r.get('valuation_citation')} | stage={r['entry_stage']}({r['entry_stage_source']}) {r.get('entry_stage_citation','')} | {r['hq_city']},{r['hq_country']}")
