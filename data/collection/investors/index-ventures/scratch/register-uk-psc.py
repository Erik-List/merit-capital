#!/usr/bin/env python3
"""Second step of the UK register sweep: for each row matched to a legal entity (scratch/register-uk-map.json, the
judge's identity decisions), read the company profile and its persons with significant control. A corporate
controller whose name is not the company's own group is the register's trace of a sale. Writes
sources/registers/companies-house/uk-entities.json."""
import json, re, sys
from pathlib import Path
H = Path(__file__).resolve().parent; R = H.parent
sys.path.insert(0, str(H))
import companies_house as ch
MAP = json.loads((H / "register-uk-map.json").read_text())
OUT = R / "sources/registers/companies-house/uk-entities.json"
out = json.loads(OUT.read_text()) if OUT.exists() else {}
from ch_psc import pscs  # noqa: E402
for slug, number in MAP.items():
    if slug in out and not sys.argv[1:]: continue
    if sys.argv[1:] and slug not in sys.argv[1:]: continue
    try:
        p = ch.company(number); ps = pscs(number)
    except ch.Unavailable as e:
        print("UNAVAILABLE", slug, e); continue
    out[slug] = {"number": number, "profile": p, "pscs": ps, "checked": "2026-10-06"}
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False))
    corp = [x for x in ps if x["kind"] == "corporate" and x["status"] == "active"]
    print(f"{slug:24s} {p['name'][:30]:30s} {p['status'][:22]:22s} inc {p['incorporated']} | corp PSC: " + ("; ".join(f"{x['name']} ({x['notified']})" for x in corp) or "-") + f" | office {p['registered_office'][:50]}", flush=True)
