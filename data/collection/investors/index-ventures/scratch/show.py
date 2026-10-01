#!/usr/bin/env python3
"""Compact judge view: queue item + evidence pack + siblings, one block per row.
Usage: show.py <batch-number|slug...> [--posts N]"""
import json, sys, re
from pathlib import Path
H = Path(__file__).resolve().parent
q = {i["slug"]: i for i in json.load(open(H / "queue" / "queue.json"))}
ev = json.load(open(H / "evidence-pack.json"))
sib = json.load(open(H / "siblings.json")) if (H / "siblings.json").exists() else {}
args = [a for a in sys.argv[1:] if not a.startswith("--")]
NP = 5
slugs = []
for a in args:
    if a.isdigit():
        b = json.load(open(H / "queue" / f"batch-{int(a):03d}.json"))
        slugs += [i["slug"] for i in (b["items"] if isinstance(b, dict) else b)]
    else:
        slugs.append(a)
SKIP = {"slug", "name", "need", "known", "rounds", "site_url", "wayback_first_link", "formd_links", "formd_accessions",
        "edgar_links", "evidence_class", "tier", "first_seen", "sector", "partners_site", "partners_formd", "site_invest_year",
        "site_entry_stage", "entry_quarter", "wayback_years", "edgar_forms", "formd_span", "graduation_evidence"}


def vals(a, f, n=3):
    return [x["value"] for x in (a.get(f) or [])][:n]


for s in slugs:
    i = q.get(s, {}); e = ev.get(s, {}); st = e.get("site") or {}; a = e.get("archive") or {}
    print(f"## {s} | {i.get('name') or e.get('name')} | tier {i.get('tier')} | fs {i.get('first_seen')} | wb {i.get('wayback_years') or ''} | need {','.join(i.get('need', []))}")
    if st:
        print(f"   site: team={','.join(st.get('partners') or [])} sec={','.join(st.get('sectors_page') or [])} backed={st.get('backed')} "
              f"reg={st.get('regions')} tag={st.get('list_tag')} web={st.get('website')} :: {(st.get('description') or '')[:130]}")
    if a:
        yrs = sorted({x["ts"][:4] for f in a.values() for x in f})
        print(f"   arch {yrs[0]}-{yrs[-1]}: desk={vals(a,'desk')} status={vals(a,'status_site')} stagef={vals(a,'stage_filter')} team={vals(a,'partners')} "
              f"sec={vals(a,'sectors',2)} hq={vals(a,'hq',2)} born={vals(a,'born_in',1)} tag={vals(a,'list_tag')} tags={vals(a,'tags',1)} geo={vals(a,'geography',1)}")
        d = vals(a, "description", 1)
        if d: print(f"      > {str(d[0])[:200]}")
    if i.get("known"): print(f"   known: {i['known']}")
    if i.get("rounds"): print("   formd: " + " ".join(f"{r['q'][:6]}:" + (f"${r['usd']/1e6:.1f}M" if r.get('usd') else '?') for r in i["rounds"]) + f" pf={i.get('partners_formd') or '-'} inc={i.get('year_inc')} {i.get('issuer_city')}")
    extra = {k: v for k, v in i.items() if k not in SKIP and v not in (None, "", [], {})}
    if extra: print("   item: " + json.dumps(extra, ensure_ascii=False)[:420])
    for p in (e.get("posts") or [])[:NP]:
        print(f"   post {p.get('date')} {p['title'][:100]}")
        for x in (p.get("sents") or [])[:2]: print(f"      > {x[:240]}")
    if len(e.get("posts") or []) > NP: print(f"   (+{len(e['posts']) - NP} more posts)")
    for n in (e.get("news") or [])[:4]:
        print(f"   news {n.get('date')} {n.get('title','')[:110]}")
    for f in (e.get("fts") or [])[:3]: print(f"   fts: {f['registrant']} {f['first']} {f['forms']}")
    for x in sib.get(s, []): print(f"   sib {x['investor']}: {x['status']}/{x['range']}/{x['usd'] or '-'}@{x['asof'] or '-'}/{x['stage']}({x['stage_src']})/{x['city']},{x['country']}/{x['focus']}")
