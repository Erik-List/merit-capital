#!/usr/bin/env python3
"""One compact block per queue row: what the judge needs, nothing else."""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import Paths  # noqa: E402
P = Paths("balderton-capital")
n = int(sys.argv[1]); lo = int(sys.argv[2]) if len(sys.argv) > 2 else 0; hi = int(sys.argv[3]) if len(sys.argv) > 3 else 999
batch = json.loads((P.queue / f"batch-{n:03d}.json").read_text())[lo:hi]
pack = json.loads((HERE / "evidence-pack.json").read_text())
sib = json.loads((HERE / "siblings.json").read_text())
ABBR = {"membership": "M", "status": "st", "hq_country": "co", "hq_city": "ci", "entry_stage": "es", "valuation_range": "vr", "seed_to_a_graduation": "gr"}
for it in batch:
    s = it["slug"]; v = pack.get(s, {}); c = v.get("card")
    head = f"## {s} | {it['name']} | fs {it['first_seen']} | {it.get('evidence_class')} | need {','.join(ABBR.get(x, x) for x in it['need'])}"
    out = [head]
    if c:
        out.append(f"  C {c['round_label']} | {c['status_site']} | {c['location_text']} | {','.join(c['sectors'])} | {c['description'][:90]}")
    elif it.get("wayback_first_link"):
        out.append(f"  W {it.get('wayback_years')} {it['wayback_first_link'][-50:]}")
    for p in (v.get("posts") or [])[:3]:
        out.append(f"  P {p['date']} {p["title"][:66]} [{','.join(p.get('round_words') or [])}] {p['url'].replace('https://www.balderton.com/news/', '')[:48]}")
    for st in (v.get("uk_seats") or [])[:2]:
        out.append(f"  U {st['number']} [{st['status']}] {st['partner'].split(',')[0]} {st['appointed']}->{st['resigned'] or ''}")
    for w in (v.get("wikipedia") or [])[:1]:
        if w["sentences"]:
            out.append(f"  K {w['sentences'][0][:170]}")
    for f in (v.get("fts") or [])[:1]:
        out.append(f"  F {f['registrant'][:30]} {f['first'][:4]} {list(f['forms'])[:4]}")
    if it.get("rounds"):
        out.append(f"  D {it.get('partners_formd')} {[(r['q'][:6], round((r['usd'] or 0) / 1e6, 1)) for r in it['rounds']][:5]} [{it.get('issuer_city')},{it.get('issuer_state')}]")
    elif it.get("partners_formd"):
        out.append(f"  D {it.get('partners_formd')}")
    if it.get("known"):
        out.append(f"  known {it['known']}")
    if s in sib:
        out.append("  S " + "; ".join(f"{x['investor']}:{x['status']}/{x['range']}/{x['stage']}/{x['city']},{x['country']}" for x in sib[s][:3]))
    print("\n".join(out))
