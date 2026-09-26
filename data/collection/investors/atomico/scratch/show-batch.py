#!/usr/bin/env python3
"""Compact per-row evidence view for one queue batch (reading aid for the judge)."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import Paths  # noqa: E402

P = Paths("atomico")
n = int(sys.argv[1])
only = set(sys.argv[2:])
batch = json.loads((P.queue / f"batch-{n:03d}.json").read_text())
pack = json.loads((HERE / "evidence-pack.json").read_text())
resolved = json.loads(P.resolved.read_text()) if P.resolved.exists() else {}
for it in batch:
    s = it["slug"]
    if only and s not in only:
        continue
    v = pack.get(s, {})
    c = v.get("cms") or {}
    out = [f"## {s} | {it['name']} | tier {it['tier']} fs {it['first_seen']} wy {it['wayback_years']} | need {','.join(it['need'])}"]
    if c:
        out.append(f"  CMS {c.get('invest_year')} {c.get('stage_site')} {c.get('status_site')} [{c.get('location_site')}] lead={c.get('lead')} web={c.get('website')}")
        out.append(f"      {(c.get('pretitle') or '')[:90]} | {(c.get('subtitle') or '')[:160]}")
        if c.get("news"):
            out.append(f"      news: {c['news'][:3]}")
    b = v.get("board")
    if b:
        out.append(f"  BOARD {b.get('url')} stage={b.get('stage_board')} founded={b.get('founded_board')} emp={b.get('approx_employees')}")
    for p in (v.get("posts") or [])[:4]:
        out.append(f"  POST {p['date']} | {p['title'][:90]} | {', '.join(p.get('round_words') or [])[:160]}")
    uk = v.get("uk_register")
    if uk:
        pr = uk.get("profile") or {}
        out.append(f"  UK {uk['number']} {pr.get('name')} {pr.get('status')} inc {pr.get('incorporated')} dis {pr.get('dissolved')} named {uk.get('first_named')} after {uk.get('last_not_named')}")
        for st in (uk.get("seats") or [])[:4]:
            out.append(f"     seat {st['person']} {st['appointed']}->{st['resigned'] or ''} {'F' if st['firm_address'] else ''}")
    for f in v.get("fts") or []:
        out.append(f"  FTS {f['registrant']} {f['first']} {f['forms']} {(f.get('context') or [''])[0][:200]}")
    if v.get("edgar"):
        out.append(f"  EDGAR {v['edgar']}")
    if it.get("rounds"):
        out.append(f"  FORMD rounds {it['rounds']} entry {it.get('entry_date')} grad {it.get('formd_graduation')}")
    r = resolved.get(s) or {}
    pre = {k: r.get(k) for k in ("status", "valuation_usd", "valuation_source", "valuation_range",
                                 "hq_country", "hq_country_source", "entry_stage", "entry_stage_source",
                                 "flags") if r.get(k)}
    if pre:
        out.append(f"  PREFILL {pre}")
    print("\n".join(out))
