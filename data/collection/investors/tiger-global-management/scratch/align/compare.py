"""Tiger Global (PRO-167) vs the sibling books at ingest: (1) every accepted rule-10 pair in
companies/cross-rulings.json with both rows as they stand now; (2) same-status, same-band shared rows
whose figure is more than 20% off a NEWER Tiger mark (rule 10 checks status and band only)."""
import csv, json, sys, importlib.util
from pathlib import Path
ROOT = Path(__file__).resolve().parents[6]
INV = ROOT / "data/collection/investors"
spec = importlib.util.spec_from_file_location("runmod", ROOT / "scripts/run.py")
sys.argv = ["run.py"]
runmod = importlib.util.module_from_spec(spec); spec.loader.exec_module(runmod)
ck = runmod.cross_key
def rows(inv):
    p = INV / inv / "companies/base.csv"
    return {r["slug"]: r for r in csv.DictReader(open(p))} if p.exists() else {}
T = rows("tiger-global-management")
def show(r):
    return f'{r["status"]:<9}{r["valuation_range"]:<10}{(r["valuation_usd"] or "-"):>16} {r["valuation_asof"] or "-":<11}'
C = json.load(open(INV / "tiger-global-management/companies/cross-rulings.json"))
print("== accepted pairs")
for p in C["accepted"]:
    a, b = p["rows"]
    inv, s = b.split(":")
    t, o = T.get(a.split(":")[1]), rows(inv).get(s)
    if not o: print(f"   {b}: MISSING in sibling"); continue
    same = (t["status"], t["valuation_range"], t["valuation_usd"], t["valuation_asof"]) == (o["status"], o["valuation_range"], o["valuation_usd"], o["valuation_asof"])
    inflight = (INV / inv / "scratch/in-flight.json").exists()
    print(f'{"SAME" if same else "DIFF"} {b:<45} T {show(t)} | O {show(o)}{" IN-FLIGHT" if inflight else ""}')
print("== same status+band, figure >20% off a newer Tiger mark")
tk = {ck(r["name"]): r for r in T.values()}
for d in sorted(INV.iterdir()):
    if d.name == "tiger-global-management" or not (d / "companies/base.csv").exists(): continue
    for s, o in rows(d.name).items():
        t = tk.get(ck(o["name"])) or (T.get(s) if T.get(s) and ck(T[s]["name"]) == ck(o["name"]) else None)
        if not t or (t["status"], t["valuation_range"]) != (o["status"], o["valuation_range"]): continue
        try: tv, ov = float(t["valuation_usd"]), float(o["valuation_usd"])
        except ValueError: continue
        if (t["valuation_asof"] or "") > (o["valuation_asof"] or "") and abs(tv - ov) / max(tv, ov) > 0.2:
            print(f'   {d.name}:{s:<30} T {show(t)} | O {show(o)}')
