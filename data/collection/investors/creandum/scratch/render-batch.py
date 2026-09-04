#!/usr/bin/env python3
"""Print one queue batch's items with their evidence pack, compactly, for the judge."""
import json, sys, re
from pathlib import Path
I = Path("data/collection/investors/creandum")
pack = json.loads((I / "scratch/evidence-pack.json").read_text())
batch = json.loads((I / "scratch/queue" / sys.argv[1]).read_text())
for it in batch:
    p = pack[it["slug"]]
    s = p["site"] or {}; a = p["archive_2017_2023"] or {}
    print(f"### {it['slug']} | {p['name']} | need {it['need']} | known {it.get('known') or {}} | first {p['first_seen']} | tier {p['tier']}")
    print(f"  site: date {s.get('invest_year')} state {s.get('state')} exited {s.get('exited')} types {s.get('sectors')} leads {s.get('partners')} url {s.get('url')} founded {(s.get('foundedDate') or '')[:4]} founders {(s.get('founderName') or '')[:60]}")
    if a: print(f"  2017-23: invested {a.get('invest_year')} status {a.get('status_site')} type {a.get('type')} partners {a.get('partners')} url {a.get('url')} founded {a.get('founded')} years {a.get('years_listed')} | {(a.get('story') or '')[:140]}")
    for x in p["stories"][:3]:
        sn = [t for t in x["snips"] if re.search(r"seed|series|round|led|lead|secondary|acqui|IPO|exit", t, re.I)][:2]
        print(f"  story {x['date']} {x['title'][:55]} rel={x['related']}")
        for t in sn: print(f"     - {t[:200]}")
    for x in p["announcements"][:2]:
        sn = [t for t in x["snips"] if re.search(r"seed|series|round|led|lead|financing|acqui", t, re.I)][:1]
        if sn: print(f"  news {x['year']} {x['title'][:50]}: {sn[0][:180]}")
    for w in p["wikipedia"]:
        for t in w["sentences"][:2]: print(f"  wiki: {t[:200]}")
    if p["formd_rounds"]: print(f"  formd: {sorted([(r['sale'] or r['q'], r['usd']) for r in p['formd_rounds']])}")
    if it.get("rounds"): pass
    print()
