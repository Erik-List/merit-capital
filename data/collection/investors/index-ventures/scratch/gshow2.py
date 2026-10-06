"""Tighter graduation view: only headlines naming a Series A+ round or an end, 4 per row."""
import json, sys, re
from pathlib import Path
items = []
for f in sorted(Path(__file__).with_name("queue").glob("batch-*.json")):
    items += json.loads(f.read_text())
a = sys.argv
lo = int(a[a.index("--from") + 1]); hi = int(a[a.index("--to") + 1])
SER = re.compile(r"series [a-f]\b", re.I); END = re.compile(r"acqui|shut|bankrupt|administration|merge|wind", re.I)
for n, i in enumerate(items):
    if not (lo <= n < hi) or i["need"] != ["seed_to_a_graduation"]: continue
    k = i.get("known") or {}
    print(f"## {n} {i['slug']} | {k.get('status')} {k.get('entry_stage_source')} entry={k.get('entry_date')} {k.get('hq_country')} | {(k.get('note') or '')[:185]}")
    fg = i.get("formd_graduation")
    if fg: print("   F", fg.get("seed_to_a_graduation"), fg.get("entry_date"), fg.get("entry_offering_usd"), "->", fg.get("next_quarter"), fg.get("next_offering_usd"), fg.get("reason") or "")
    ge = i.get("graduation_evidence") or {}
    for s in ge.get("siblings") or []:
        if s.get("seed_to_a_graduation") or s.get("entry_date"):
            print(f"   X {s['investor'][:12]} {s.get('entry_stage')} {s.get('entry_date')} {s.get('seed_to_a_graduation')} {s.get('graduation_source')} {(s.get('graduation_citation') or '')[:90]}")
    name = (ge.get("query_name") or i["name"]).lower().split()[0]
    ms = [m for m in ge.get("mentions") or [] if name in m["title"].lower()]
    seen = set(); out = []
    for m in sorted(ms, key=lambda m: m.get("date") or ""):
        t = m["title"][:50].lower()
        if t in seen: continue
        seen.add(t)
        if SER.search(m["title"]) or END.search(m["title"]) or re.search(r"seed", m["title"], re.I): out.append(m)
    for m in out[:5]:
        print(f"   M {m.get('date')} {m['title'][:120]}")
