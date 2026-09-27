#!/usr/bin/env python3
"""Compact per-row evidence view for one queue batch (reading aid for the judge).
Usage: show-batch.py <n> [slug ...]"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import Paths  # noqa: E402

P = Paths("headline")
n = int(sys.argv[1])
only = set(sys.argv[2:])
batch = json.loads((P.queue / f"batch-{n:03d}.json").read_text())
pack = json.loads((HERE / "evidence-pack.json").read_text())
for it in batch:
    s = it["slug"]
    if only and s not in only:
        continue
    v = pack.get(s, {})
    out = [f"## {s} | {it['name']} | t{it['tier']} fs {it['first_seen']} | ev {it.get('evidence_class')} | need {','.join(it['need'])} | known {json.dumps(it.get('known') or {})}"]
    c = v.get("cms")
    if c:
        out.append(f"  CMS {c['surface']} desks={c['desks']} stages=[{c['stages']}] out=[{c['outcome']}{c['subline']}] loc={c['location']} web={c['website']} partners={c['partners']}")
        if c.get("description"):
            out.append(f"      {c['description'][:160]}")
    if v.get("bvcapital"):
        out.append(f"  BV  bvcapital.com {v['bvcapital']} {it.get('wayback_first_link','')[:110]}")
    for p in (v.get("posts") or [])[:4]:
        out.append(f"  POST {p['date']} | {p['title'][:90]} | {p['url']}")
        for se in p["sentences"][:2]:
            out.append(f"       > {se[:220]}")
    for f in v.get("fts") or []:
        out.append(f"  FTS  {f['registrant'][:40]} {str(f['first'])[:10]} {f['forms']} | {(f.get('context') or [''])[0][:200]}")
    for w in v.get("wikipedia") or []:
        out.append(f"  WIKI {w['title']}: {(w['sentences'] or [''])[0][:220] if w['sentences'] else ''}")
    if it.get("rounds"):
        out.append(f"  FORMD {it.get('partners_formd')} rounds {[(r['q'][:6], round(r['usd']/1e6, 2) if r.get('usd') else None) for r in it['rounds']]} entry {it.get('entry_date')} grad {it.get('formd_graduation')} [{it.get('issuer_city')}, {it.get('issuer_state')}] inc {it.get('year_inc')}")
    elif it.get("partners_formd"):
        out.append(f"  FORMD {it.get('partners_formd')} {it.get('formd_links', '')[:110]}")
    if it.get("formd_band_withheld"):
        out.append(f"  BANDWITHHELD {it['formd_band_withheld']}")
    if it.get("edgar_forms"):
        out.append(f"  EDGAR {it['edgar_forms']} {it.get('edgar_links', '')[:100]}")
    for k in ("unicorn", "former_unicorn", "acquirer", "public_float", "wikidata"):
        if it.get(k):
            out.append(f"  {k.upper()} {json.dumps(it[k])[:200]}")
    if it.get("graduation_evidence"):
        ge = it["graduation_evidence"]
        heads = [h.get("title", "")[:90] + " (" + str(h.get("date", ""))[:10] + ")" for h in (ge.get("headlines") or [])[:4]]
        out.append(f"  GRAD {ge.get('status') or ''} {heads}")
    print("\n".join(out))
