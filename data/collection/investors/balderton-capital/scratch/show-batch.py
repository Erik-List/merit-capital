#!/usr/bin/env python3
"""Compact per-row evidence view for one queue batch (reading aid for the judge)."""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import Paths  # noqa: E402
P = Paths("balderton-capital")
n = int(sys.argv[1]); only = set(sys.argv[2:])
batch = json.loads((P.queue / f"batch-{n:03d}.json").read_text())
pack = json.loads((HERE / "evidence-pack.json").read_text())
for it in batch:
    s = it["slug"]
    if only and s not in only:
        continue
    v = pack.get(s, {})
    out = [f"## {s} | {it['name']} | tier {it['tier']} fs {it['first_seen']} wy {it.get('wayback_years')} | ev {it.get('evidence_class')} | need {','.join(it['need'])}"]
    c = v.get("card")
    if c:
        out.append(f"  CARD {c['round_label']} | {c['status_site']} | {c['location_text']} | {','.join(c['sectors'])} | {c['website']}")
        out.append(f"       {c['description'][:150]}")
    elif it.get("wayback_first_link"):
        out.append(f"  WB   {it['wayback_first_link']}")
    for p in (v.get("posts") or [])[:5]:
        out.append(f"  POST {p['date']} | {p['title'][:95]} | {','.join(p.get('round_words') or [])} {','.join(p.get('amounts') or [])[:40]}")
        out.append(f"       {p['url']}")
    for st in (v.get("uk_seats") or [])[:4]:
        out.append(f"  UK   {st['number']} {st['company'][:34]} [{st['status']}] {st['partner'].split(',')[0]} {st['appointed']}->{st['resigned'] or ''} {'OFFICE' if st['office'] else ''}")
    for f in v.get("fts") or []:
        out.append(f"  FTS  {f['registrant'][:40]} {f['first'][:4]}-{f['last'][:4]} {f['forms']} | {(f.get('context') or [''])[0][:180]}")
    for w in v.get("wikipedia") or []:
        out.append(f"  WIKI {w['title']}: {(w['sentences'] or [''])[0][:200] if w['sentences'] else ''}")
    if it.get("rounds"):
        out.append(f"  FORMD {it.get('partners_formd')} rounds {it['rounds']} entry {it.get('entry_date')} grad {it.get('formd_graduation')} [{it.get('issuer_city')}, {it.get('issuer_state')}]")
    elif it.get("partners_formd"):
        out.append(f"  FORMD {it.get('partners_formd')} {it.get('formd_links','')[:100]}")
    if it.get("edgar_forms"):
        out.append(f"  EDGAR {it['edgar_forms']} {it.get('edgar_links','')[:100]}")
    if it.get("known"):
        out.append(f"  KNOWN {it['known']}")
    if it.get("graduation_evidence"):
        ge = it["graduation_evidence"]
        heads = [h.get("title", "")[:90] + " (" + str(h.get("date", ""))[:10] + ")" for h in (ge.get("headlines") or [])[:4]]
        out.append(f"  GRAD {ge.get('status') or ''} {heads}")
    if it.get("former_unicorn") or it.get("unicorn"):
        out.append(f"  UNICORN {it.get('unicorn')} former={it.get('former_unicorn')}")
    print("\n".join(out))
