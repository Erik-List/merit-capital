"""Compact graduation judge view over the re-prepared queue: python3 gshow.py [--from N --to M] [--slugs a,b]"""
import json, sys, re
from pathlib import Path
items = []
for f in sorted(Path(__file__).with_name("queue").glob("batch-*.json")):
    items += json.loads(f.read_text())
a = sys.argv
lo = int(a[a.index("--from") + 1]) if "--from" in a else 0
hi = int(a[a.index("--to") + 1]) if "--to" in a else len(items)
want = set(a[a.index("--slugs") + 1].split(",")) if "--slugs" in a else None
ROUND = re.compile(r"series [a-f]\b|seed|acqui|shut|raises|raised|funding|secures|lands|closes|\$\d|€\d|£\d|bankrupt|administration|merge", re.I)
for n, i in enumerate(items):
    if want and i["slug"] not in want: continue
    if not want and not (lo <= n < hi): continue
    k = i.get("known") or {}
    print(f"## {n} {i['slug']} | {i['name']} | need {','.join(x.replace('seed_to_a_graduation','grad').replace('valuation_range','val').replace('entry_stage','stage').replace('hq_','') for x in i['need'])}")
    print(f"   K {k.get('status')} {k.get('entry_stage')}/{k.get('entry_stage_source')} entry={k.get('entry_date')} {k.get('hq_country')} | {(k.get('note') or '')[:230]}")
    fg = i.get("formd_graduation")
    if fg: print("   F", {x: fg[x] for x in fg if x in ("seed_to_a_graduation", "entry_offering_usd", "entry_date", "next_offering_usd", "next_quarter", "reason")})
    ge = i.get("graduation_evidence") or {}
    for s in ge.get("siblings") or []:
        print("   X", json.dumps(s, ensure_ascii=False)[:330])
    name = (ge.get("query_name") or i["name"]).lower()
    ms = [m for m in ge.get("mentions") or [] if name.split()[0] in m["title"].lower() and (m.get("rounds") or m.get("amounts") or ROUND.search(m["title"]))]
    seen = set(); out = []
    for m in sorted(ms, key=lambda m: m.get("date") or ""):
        t = m["title"][:60].lower()
        if t in seen: continue
        seen.add(t); out.append(m)
    for m in out[:7]:
        print(f"   M {m.get('date')} [{m['surface'][:4]}] {m['title'][:150]}")
    if len(out) > 7: print(f"   (+{len(out)-7} more)")
