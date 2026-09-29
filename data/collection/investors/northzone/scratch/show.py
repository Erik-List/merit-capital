#!/usr/bin/env python3
"""Compact judge view: queue item + evidence pack + siblings, one block per row.
Usage: show.py <batch-number|slug...> [--posts N]"""
import json, sys, re
from pathlib import Path
H = Path(__file__).resolve().parent
q = {i["slug"]: i for i in json.load(open(H / "queue" / "queue.json"))}
ev = json.load(open(H / "evidence-pack.json"))
sib = json.load(open(H / "siblings.json"))
BODY = {r["url"]: r.get("body") or "" for r in json.load(open(H.parent / "sources" / "site" / "insights.json"))["rows"]}
RW = re.compile(r"(?i)\b(pre-seed|seed|series [a-f]\b|round|led by|co-led|leads?|invest(?:ed|ing|ment)|[$€£]\s?\d[\d.,]*\s?(?:m|million|bn|billion)?|\d[\d.,]*\s?(?:m|million)\s?(?:eur|usd|sek|nok|gbp)?)")
args = [a for a in sys.argv[1:] if not a.startswith("--")]
NP = 8
slugs = []
for a in args:
    if a.isdigit():
        slugs += [i["slug"] for i in json.load(open(H / "queue" / f"batch-{int(a):03d}.json"))["items"]] if isinstance(json.load(open(H / "queue" / f"batch-{int(a):03d}.json")), dict) else [i["slug"] for i in json.load(open(H / "queue" / f"batch-{int(a):03d}.json"))]
    else:
        slugs.append(a)
SKIP = {"slug", "name", "need", "known", "rounds", "site_url", "wayback_first_link", "formd_links", "formd_accessions",
        "edgar_links", "evidence_class", "tier", "first_seen", "sector", "partners_site", "partners_formd", "site_invest_year",
        "site_entry_stage", "entry_quarter", "wayback_years", "edgar_forms", "formd_span"}
for s in slugs:
    i = q.get(s, {}); e = ev.get(s, {}); st = e.get("site") or {}
    print(f"## {s} | {i.get('name') or e.get('name')} | tier {i.get('tier')} | fs {i.get('first_seen')} | need {','.join(i.get('need', []))}")
    if st:
        print(f"   site: P{st.get('invest_year')} F{st.get('founded_year')} {st.get('status_site')} {st.get('stage_site_word')}"
              f"{' UNICORN' if st.get('unicorn_tag') else ''} {st.get('location_site')} team={','.join(st.get('partners') or [])} "
              f"web={st.get('website')} :: {(st.get('description') or '')[:110]}")
    if i.get("known"): print(f"   known: {i['known']}")
    if i.get("rounds"): print("   formd: " + " ".join(f"{r['q'][:6]}:" + (f"${r['usd']/1e6:.1f}M" if r.get('usd') else '?') for r in i["rounds"]) + f" pf={i.get('partners_formd') or '-'} inc={i.get('year_inc')} {i.get('issuer_city')}")
    extra = {k: v for k, v in i.items() if k not in SKIP and v not in (None, "", [], {})}
    if extra: print("   item: " + json.dumps(extra, ensure_ascii=False)[:400])
    for p in (e.get("posts") or [])[:NP]:
        art = re.sub(r"https?://(www\.)?", "", p.get("article") or "")[:60]
        print(f"   post {p.get('date')} {p.get('kind') or '-'} {p['title'][:90]} {('-> ' + art) if art else ''}")
        b = BODY.get(p["url"], "")
        if b and p.get("kind") != "Press":
            sents = [x for x in re.split(r"(?<=[.!?])\s+", b) if re.search(r"(?i)pre-seed|seed|series [a-f]\b|\bround\b|led by|co-led|we led|leading", x)]
            for x in sents[:3]: print(f"      > {x[:230]}")
    if len(e.get("posts") or []) > NP: print(f"   (+{len(e['posts']) - NP} more posts)")
    for f in e.get("fts") or []: print(f"   fts: {f['registrant']} {f['first']} {f['forms']}")
    for x in sib.get(s, []): print(f"   sib {x['investor']}: {x['status']}/{x['range']}/{x['usd'] or '-'}@{x['asof'] or '-'}/{x['stage']}({x['stage_src']})/{x['city']},{x['country']}/{x['focus']}")
