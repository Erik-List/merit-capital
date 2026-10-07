"""Compact view of queue items for the judge. usage: view.py [--unjudged] [--batch N] [--slugs a,b] [--need key]"""
import json, sys
from pathlib import Path
H = Path(__file__).resolve().parent
q = json.loads((H / "queue/queue.json").read_text()); items = q if isinstance(q, list) else q["items"]
menu = json.loads((H.parent / "sources/wayback/site-menu-2013.json").read_text())["companies"]
bn = {v["name"].lower(): v["category"] for v in menu.values()}
a = sys.argv[1:]
TIGHT = "--tight" in a
if "--batch" in a:
    b = json.loads((H / f"queue/batch-{int(a[a.index('--batch')+1]):03d}.json").read_text()); b = b if isinstance(b, list) else b["items"]
    keep = {i["slug"] for i in b}; items = [i for i in items if i["slug"] in keep]
if "--slugs" in a:
    keep = set(a[a.index("--slugs")+1].split(",")); items = [i for i in items if i["slug"] in keep]
if "--unjudged" in a: items = [i for i in items if "membership" in i["need"]]
if "--judged" in a: items = [i for i in items if "membership" not in i["need"]]
if "--need" in a: items = [i for i in items if a[a.index("--need")+1] in i["need"]]
ab = {"membership": "M", "status": "st", "hq_city": "ci", "hq_country": "co", "entry_stage": "es", "valuation_range": "vr", "seed_to_a_graduation": "gr"}
for i in items:
    r = sorted(i.get("rounds") or [], key=lambda x: x["q"])
    rounds = ",".join(f"{x['q'][2:6]}:{(x.get('usd') or 0)/1e6:.1f}" for x in r[:6])
    k = i.get("known") or {}
    known = ",".join(f"{kk[:6]}={str(v)[:14]}" for kk, v in k.items() if kk not in ("entry_date",))
    g = i.get("formd_graduation") or {}
    w = i.get("formd_band_withheld") or {}
    print(" | ".join(x for x in [
        i["slug"], i["name"] if i["name"].lower().replace(" ", "-") != i["slug"] else "", i.get("evidence_class", ""),
        f"fs{i.get('first_seen','')}", f"wb{i['wayback_years']}" if i.get("wayback_years") else "",
        f"cat:{bn[i['name'].lower()]}" if i["name"].lower() in bn else "",
        f"P:{i['partners_formd']}" if i.get("partners_formd") else "",
        f"R:{rounds}" if rounds else "", f"ent{i.get('entry_date','')}" if i.get("entry_date") else "",
        f"{i.get('issuer_city','').title()},{i.get('issuer_state','')[:10]}" if i.get("issuer_city") else "",
        f"inc{i['year_inc']}" if i.get("year_inc") else "", f"K:{known}" if known and not TIGHT else "",
        f"G:{g.get('seed_to_a_graduation')}" if g else "", f"band-withheld:{w.get('band')}" if w else "",
        f"acq:{i['acquirer']}" if i.get("acquirer") else "", f"uni:{i['former_unicorn']}" if i.get("former_unicorn") else "",
        "need:" + ",".join(ab.get(n, n) for n in i["need"])] if x))
print(len(items), "items")
