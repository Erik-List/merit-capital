import json,sys
gs=json.load(open('graduation-surfaces.json'))
q=json.load(open('queue/queue.json'))
bys={i.get('slug'):i for i in q if isinstance(i,dict)}
for s in sys.argv[1:]:
    print("=====",s)
    g=gs.get(s)
    if not g: print("  NO SURFACES")
    else:
        print("  name:",g.get('name'),"| query_name:",g.get('query_name'),"| asof:",g.get('asof'),"| country:",g.get('country'))
        for k,v in (g.get('surfaces') or {}).items():
            its=v.get('items',[])
            print(f"  [{k}] status={v.get('status')} q={v.get('query')!r} n={len(its)}")
            for it in its[:12]:
                print("     ",it.get('date'),"|N" if it.get('names') else "|-","|",(it.get('title') or '')[:130])
        print("  siblings:",json.dumps(g.get('siblings'))[:800])
    it=bys.get(s) or {}
    print("  formd_graduation:",it.get('formd_graduation'))
    ge=it.get('graduation_evidence')
    print("  graduation_evidence keys:",(list(ge.keys()) if isinstance(ge,dict) else ge))
