"""Compact evidence view per queue batch. Usage: pack.py <batch-no> [--full]"""
import csv, json, re, sys
from pathlib import Path
H = Path(__file__).resolve().parent
INV = H.parent
ev = json.loads((H / "archive-evidence.json").read_text())
live = {}
for r in csv.DictReader(open(INV / "sources/site/portfolio-2026.csv", encoding="utf-8-sig")):
    live[re.sub(r"[^a-z0-9]", "", r["Name"].lower())] = r
def k(s): return re.sub(r"[^a-z0-9]", "", s.lower())
b = json.loads((H / f"queue/batch-{int(sys.argv[1]):03d}.json").read_text())
full = "--full" in sys.argv
for it in b:
    e = ev.get(it["slug"]) or next((v for s, v in ev.items() if k(s) == k(it["slug"]) or k(it["name"]) in map(k, v["names"])), None)
    l = live.get(k(it["name"])) or live.get(k(it["slug"]))
    out = [f"## {it['slug']} | {it['name']} | need={','.join(it['need'])}"]
    if l:
        out.append(f"  LIVE: entry {l['HV Entry']} | {l['Funding']} | at-entry {l['Stage at Entry']} | now {l['Stage']} | {l['Status']} | HQ {l['HQ']} | founded {l['Founded']} | {l['Description'][:110]} | {l['Website']}")
    if e:
        yrs = ",".join(f"{y}:{'/'.join(s)[:7]}" for y, s in e["listed"].items())
        out.append(f"  ARCH: {yrs} | inv {e['invest_dates'] or e['invest_years']} | fd {e['founded']} | p {e['partners']} | hq {e['hq']} | web {e['websites'][:1]}")
        if full:
            for t in e["texts"][:1]:
                out.append(f"  TEXT: {t['text'][:500]}")
    kn = {kk: vv for kk, vv in (it.get("known") or {}).items() if vv not in (None, "", [])}
    if kn: out.append(f"  KNOWN: {json.dumps(kn, ensure_ascii=False)[:400]}")
    if it.get("rounds") or it.get("formd_graduation"): out.append(f"  FORMD: {json.dumps(it.get('rounds'))[:300]} grad={json.dumps(it.get('formd_graduation'))[:200]}")
    if it.get("edgar_forms"): out.append(f"  EDGAR: {it['edgar_forms']} {it['edgar_links'][:120]}")
    if it.get("acquirer") or it.get("former_unicorn"): out.append(f"  acq={it.get('acquirer')} unicorn={it.get('former_unicorn')}")
    print("\n".join(out))

# ---- surfaces view (appended): headlines naming the company, per row
def surf(slug, n=6):
    try:
        g = json.loads((H / "graduation-surfaces.json").read_text()).get(slug) or {}
    except Exception:
        return []
    out = []
    for svc, v in (g.get("surfaces") or {}).items():
        for i in (v.get("items") or []):
            if i.get("names"):
                out.append((i.get("date") or "")[:10] + f" [{svc[:6]}|{(i.get('source') or '')[:14]}] " + (i.get("title") or "")[:150] + " {" + ",".join(i.get("rounds") or []) + "} " + (i.get("url") or i.get("link") or ("gid:" + (i.get("gid") or "")[-10:])))
    sib = g.get("siblings") or []
    nm = (g.get("query_name") or slug).lower()
    rel = [o for o in out if re.search(r"\b" + re.escape(nm) + r"\b", o.lower()) and (re.search(r"\{[^}]+\}", o) or re.search(r"holtzbrinck|hv capital|hv holtzbrinck", o.lower()))]
    firm = [o for o in rel if re.search(r"holtzbrinck|hv capital", o.lower())]
    rest = [o for o in rel if o not in firm]
    return sorted(set(firm))[:n] + sorted(set(rest))[:n] + [f"SIB {s.get('investor')}: {s.get('entry_stage')} {s.get('entry_stage_source')} {s.get('entry_stage_citation') or ''} | st={s.get('status')} band={s.get('valuation_range')} | grad={s.get('seed_to_a_graduation')} {s.get('graduation_citation') or ''} | {(s.get('note') or '')[:160]}" for s in sib[:3]]
if "--surf" in sys.argv:
    for it in b:
        print(f"== {it['slug']}")
        for line in surf(it["slug"], 10):
            print("   ", line)
