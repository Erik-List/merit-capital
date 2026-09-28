import json, sys
import glob
d = {}
for f in sorted(glob.glob("data/collection/investors/20vc/scratch/research/rounds*.json")):
    d.update(json.load(open(f)))
for s in sys.argv[1:]:
    r = d.get(s)
    if not r:
        print("?? not yet", s); continue
    print(f"######## {s} | {r['status']} | {len(r['items'])} read")
    for it in r["items"]:
        print(f"  {it['date']} {it['source']}: {it['title'][:120]} [{it['read']}]")
        print(f"     {it['link']}")
        for x in it["sentences"][:6]: print(f"       > {x[:260]}")
    for d_, t in r.get("other_titles", [])[:8]: print(f"  - {d_} {t}")
