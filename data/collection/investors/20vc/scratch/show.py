import json, sys
ev = json.load(open("data/collection/investors/20vc/scratch/evidence-pack.json"))
for slug in sys.argv[1:]:
    e = ev.get(slug)
    if not e:
        print("?? unknown slug", slug); continue
    c = e["card"] or {}
    print(f"######## {slug} | {e['name']} | card: {c.get('one_liner')} | {c.get('sector_1')}/{c.get('sector_2')} | exit={c.get('exit_site')} | {c.get('website')} | added {str(c.get('cms_created'))[:10]} | archive {e['archive_years']}")
    if e["prefill"]: print("   prefill:", json.dumps(e["prefill"])[:250])
    for n in (e.get("notes") or []):
        if "recall addition" in n: print("   note:", n[:300])
    for s in e["siblings"][:5]:
        print(f"   SIB {s['inv']}: {s['status']} {s['valuation_range']} {s['valuation_usd']} {s['entry_stage']} {s['entry_date']} {s['hq_country']}/{s['hq_city']} {s['focus']} | {s['note'][:200]}")
    for p in e["press"][:8]:
        print(f"   P {p['date']} {p['src']}: {p['s'][:330]}")
        print(f"      {p['link']}")
