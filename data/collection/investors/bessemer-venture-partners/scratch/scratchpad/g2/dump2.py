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
            nm=[i for i in its if i.get('names')]
            print(f"  [{k}] status={v.get('status')} n={len(its)} naming={len(nm)}")
            show = nm if len(its)>12 else its
            for it in show[:45]:
                print("     ",it.get('date'),"|N" if it.get('names') else "|-","|",(it.get('title') or '')[:140])
        print("  siblings:",json.dumps(g.get('siblings'))[:1200])
    it=bys.get(s) or {}
    print("  formd_graduation:",it.get('formd_graduation'))
    ge=it.get('graduation_evidence') or {}
    print("  mentions_total:",ge.get('mentions_total'))
    for m in (ge.get('mentions') or [])[:12]:
        print("     M:",json.dumps(m)[:260])
