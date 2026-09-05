#!/usr/bin/env python3
"""Write one compact evidence render per queue batch (scratch/render-batch-NNN.txt) from
scratch/evidence-pack.json + the queue item's needs, so the grind reads one file per batch."""
import json, glob, re
from pathlib import Path
I = Path("/Users/erik/Developer/merit-capital/data/collection/investors/union-square-ventures")
pack = json.load(open(I / "scratch/evidence-pack.json"))
def render(e, need):
    out = [f"## {e['name']} ({e['slug']}) tier {e['tier']} first_seen {e['first_seen']} wb {e['wayback_years']} NEED {','.join(need)}"]
    lv = e.get("live")
    if lv:
        out.append(f"LIVE: {lv.get('first_investment')} | exit={lv.get('exit_detail')!r} status={lv.get('status_site')} sectors={lv.get('sectors')} | {(lv.get('excerpt') or '')[:160]} | site {lv.get('url')}")
    for k in ("archived_2013_2015", "archived_2016_2019"):
        if e.get(k):
            caps = e[k]; last = caps[sorted(caps)[-1]]
            if k.endswith("2015"): out.append(f"ARCH13-15 {sorted(caps)[0]}..{sorted(caps)[-1]}: series={last.get('series')} year={last.get('year')} city={last.get('city')} cats={last.get('categories')} status={last.get('status_class')}")
            else: out.append(f"ARCH16-19 {sorted(caps)[0]}..{sorted(caps)[-1]}: meta={last.get('meta')} section={last.get('section')} site={last.get('website')}")
    fd = e.get("formd_partners") or ""
    if e.get("edgar_forms") or fd or e.get("formd_span"):
        out.append(f"EDGAR forms={e.get('edgar_forms')} | FormD partners={fd} span={e.get('formd_span')} max=${e.get('formd_max_round_usd')} links={(e.get('formd_links') or '')[:160]}")
    if e.get("formd_rounds"): out.append("ROUNDS: " + "; ".join(f"{r.get('quarter')} ${r.get('offering_usd')} sold ${r.get('sold_usd')} {r.get('issuer') or ''}"[:70] for r in e["formd_rounds"][:8]))
    d = e.get("deterministic") or {}
    keys = {k: v for k, v in d.items() if k in ("status", "valuation_usd", "valuation_source", "valuation_asof", "is_public", "entry_stage", "entry_stage_source", "hq_country", "hq_country_source", "seed_to_a_graduation", "prior_rounds", "flags", "cik") and v not in (None, [], "")}
    if keys: out.append("DET: " + json.dumps(keys, ensure_ascii=False))
    if e.get("notes"): out.append("NOTES: " + str(e["notes"])[:200])
    for p in e["posts"][:5]:
        out.append(f"POST {p['date']} {'*' if p['linked'] else ''}{p['title'][:70]} <{p['url'].replace('https://www.usv.com/writing/', '/w/')}>")
        out += ["   - " + s[:240] for s in p["sentences"][:3]]
    for w in e["wikipedia"][:2]: out.append(f"WIKI {w['title']}: " + " | ".join(x[:200] for x in w["sentences"][:2]))
    for f in e["fts"][:2]: out.append(f"FTS {f['registrant']} {f['first_date']} {f['forms']}")
    return "\n".join(out)
for bf in sorted(glob.glob(str(I / "scratch/queue/batch-*.json"))):
    if ".out" in bf: continue
    items = json.load(open(bf))
    txt = "\n\n".join(render(pack[it["slug"]], it["need"]) for it in items if it["slug"] in pack)
    out = I / "scratch" / ("render-" + Path(bf).stem + ".txt")
    out.write_text(txt)
    print(out.name, len(items), "items", len(txt), "chars")
