"""List member rows with open needs (queue need minus what classification.json holds)."""
import json, sys
from pathlib import Path
R = Path(__file__).resolve().parents[1]
led = json.loads((R / "companies/membership-ledger.json").read_text())["index-ventures"]["verdicts"]
cl = json.loads((R / "companies/classification.json").read_text())
KEY = {"status": "status", "hq_country": "hq_country", "hq_city": "hq_city", "entry_stage": "entry_stage", "valuation_range": "valuation_range",
       "seed_to_a_graduation": "seed_to_a_graduation", "membership": None}
out = {}
for f in sorted((R / "scratch/queue").glob("batch-*.json")):
    for i in json.loads(f.read_text()):
        s = i["slug"]; v = (led.get(s) or {}).get("verdict")
        if v == "not_member":
            continue
        c = cl.get(s) or {}
        known = i.get("known") or {}
        miss = []
        for n in i["need"]:
            if n == "membership":
                if v != "member": miss.append("membership")
                continue
            if n == "hq_city" and "city_unknown" in (c.get("flags") or []): continue
            if c.get(KEY[n]) in (None, ""):
                if n == "seed_to_a_graduation" and c.get("entry_stage") not in (None, "Seed", "Pre-Seed"): continue
                miss.append(n)
        if miss:
            out[s] = (f.name[6:9], miss, c.get("entry_stage"))
want = sys.argv[1] if len(sys.argv) > 1 else None
for s, (b, m, st) in sorted(out.items(), key=lambda x: (x[1][1], x[0])):
    if want and want not in m: continue
    print(b, s, ",".join(m), "| stage:", st)
print(len(out), "rows open")
