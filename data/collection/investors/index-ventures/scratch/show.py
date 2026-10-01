#!/usr/bin/env python3
"""Compact judge view: queue item + evidence pack + headlines + siblings, one block per row.
Usage: show.py <batch-number|slug...> [--from N --to M]"""
import json, sys, re
from pathlib import Path
H = Path(__file__).resolve().parent
q = {i["slug"]: i for i in json.load(open(H / "queue" / "queue.json"))}
ev = json.load(open(H / "evidence-pack.json"))
sib = json.load(open(H / "siblings.json")) if (H / "siblings.json").exists() else {}
NB = {}
for _f in sorted(H.glob("news-bulk*.json")):
    NB.update({k: v for k, v in json.load(open(_f)).items() if v.get("status") == "ok"})
led = json.load(open(H.parent / "companies" / "membership-ledger.json"))
led = led.get("index-ventures", led)
argv = sys.argv[1:]
lo = int(argv[argv.index("--from") + 1]) if "--from" in argv else 0
hi = int(argv[argv.index("--to") + 1]) if "--to" in argv else 999
args = [a for i, a in enumerate(argv) if not a.startswith("--") and (i == 0 or argv[i - 1] not in ("--from", "--to"))]
slugs = []
for a in args:
    if a.isdigit():
        b = json.load(open(H / "queue" / f"batch-{int(a):03d}.json"))
        slugs += [i["slug"] for i in (b["items"] if isinstance(b, dict) else b)]
    else:
        slugs.append(a)
slugs = slugs[lo:hi]


def vals(a, f, n=2):
    return ";".join(",".join(v) if isinstance(v, list) else str(v) for v in [x["value"] for x in (a.get(f) or [])][:n])


for s in slugs:
    i = q.get(s, {}); e = ev.get(s, {}); st = e.get("site") or {}; a = e.get("archive") or {}
    v = (led.get(s) or {}).get("verdict") if isinstance(led, dict) else None
    if v == "not_member":
        print(f"## {s} | NOT_MEMBER (done)"); continue
    wb = (i.get("wayback_years") or "").split(",")
    print(f"## {s} | {i.get('name') or e.get('name')} | fs{i.get('first_seen')} wb{wb[0][-2:] if wb[0] else ''}-{wb[-1][-2:] if wb[-1] else ''} | need {','.join(x.replace('hq_','').replace('valuation_range','val').replace('entry_stage','stage').replace('seed_to_a_graduation','grad') for x in i.get('need', []))}")
    if st:
        print(f" S team={','.join(st.get('partners') or [])} sec={','.join(st.get('sectors_page') or [])} backed={','.join(st.get('backed') or [])} "
              f"reg={','.join(st.get('regions') or [])} tag={st.get('list_tag') or ''} web={re.sub('https?://(www[.])?','',st.get('website') or '').strip('/')} :: {(st.get('description') or '').split(': ',1)[-1][:90]}")
    if a:
        print(f" A st={vals(a,'status_site')} stagef={vals(a,'stage_filter')} team={vals(a,'partners')} sec={vals(a,'sectors',1)} hq={vals(a,'hq')} born={vals(a,'born_in',1)} tag={vals(a,'list_tag')}")
        d = vals(a, "description", 1)
        if d and not st: print(f"   > {d[:150]}")
    k = dict(i.get("known") or {})
    for kk in ("entry_stage_source",):
        if kk in k: k["src"] = k.pop(kk)
    extra = []
    if i.get("hq_country_claim"): extra.append("country=CLAIM")
    if i.get("former_unicorn"): extra.append(f"former_unicorn={i['former_unicorn'].get('exit_reason')}/{i['former_unicorn'].get('last_valuation_usd')}")
    if i.get("formd_band_withheld"): extra.append(f"band_withheld={i['formd_band_withheld'].get('band')}")
    if i.get("formd_graduation"): extra.append(f"formd_grad={i['formd_graduation'].get('seed_to_a_graduation')}")
    if k or extra: print(f" K {json.dumps(k, ensure_ascii=False)[:200]} {' '.join(extra)}")
    if i.get("rounds"): print(" F " + " ".join(f"{r['q'][:6]}:" + (f"${r['usd']/1e6:.1f}M" if r.get('usd') else '?') for r in i["rounds"]) + f" pf={i.get('partners_formd') or '-'} inc={i.get('year_inc') or ''} {i.get('issuer_city') or ''}")
    ps = e.get("posts") or []
    for p in ps[:2]:
        print(f" P {p.get('date')} {p['title'][:80]}")
        for x in (p.get("sents") or [])[:1]: print(f"   > {x[:170]}")
    if len(ps) > 2: print(f"   (+{len(ps) - 2} posts: " + "; ".join(f"{p.get('date')} {p['title'][:40]}" for p in ps[2:5]) + ")")
    for n in (e.get("news") or [])[:2]:
        print(f" N {n.get('date')} {n.get('title','')[:105]}")
    nb = (NB.get(i.get("name") or "") or {}).get("items") or []
    hl = sorted([x for x in nb if x.get("rounds") or x.get("amounts") or re.search(r"(?i)acqui|ipo|shut|seed|series|raises|funding|valuation|bankrupt", x["title"])], key=lambda x: x["date"])
    idx = [x for x in hl if "index" in x["title"].lower()]
    rest = [y for y in hl if y not in idx]
    pick = idx[:1] + rest[:1] + rest[-2:] if len(rest) > 3 else idx[:1] + rest
    seen = set()
    for x in pick[:4]:
        if x["title"] in seen: continue
        seen.add(x["title"])
        print(f" H {x['date']} {x['source'][:14]}: {x['title'][:115]}")
    for f in (e.get("fts") or [])[:1]: print(f" T {f['registrant']} {f['first']} {' '.join(list(f['forms'])[:6])}")
    sb = [x for x in sib.get(s, []) if x.get("verdict") != "not_member" and x["status"]]
    if sb: print(" X " + " | ".join(f"{x['investor'][:9]}:{x['status']}/{x['range']}/{(str(round(float(x['usd'])/1e9,2))+'B') if x['usd'] else '-'}@{x['asof'] or '-'}/{x['stage']}/{x['city']},{x['country']}/{x['focus'][:12]}" for x in sb[:3]))
