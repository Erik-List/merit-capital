"""The `formd:` line of an absence test (COLLECTION.md s6) for rows the base carries no Form D for.
EDGAR's full-text search does NOT index Form D issuers (measured 2026-10-06: 'Dahlia Labs' returns nothing with forms=D
while the company has two 2024 filings), so an empty full-text result is a failed lookup, never an absence. This reads
the entity-name table instead (data/collection/shared/sec/cik-lookup-data.txt, every EDGAR filer name) and, for each
entity whose name starts with the query, the filing index (data.sec.gov/submissions) for forms D and D/A.
    python3 formd-lookup.py "<name prefix>" ...   -> scratch/formd-lookup.json {query: {entities:[{name,cik,formd:[...]}]}}"""
import json, re, subprocess, sys, time
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from shared_throttle import wait
UA = "Merit Capital Research erik@meritcapit.al"
TABLE = ROOT / "data/collection/shared/sec/cik-lookup-data.txt"
out_p = Path(__file__).with_name("formd-lookup.json")
out = json.loads(out_p.read_text()) if out_p.exists() else {}
out = {k: v for k, v in out.items() if "entities" in v}       # drop the refused full-text results
norm = lambda s: re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()
want = {q: norm(q) for q in sys.argv[1:] if q not in out}
found = {q: [] for q in want}
if want:
    with open(TABLE, errors="replace") as f:
        for line in f:
            name, _, rest = line.rpartition(":")[0].rpartition(":")
            n = norm(name)
            for q, nq in want.items():
                if n == nq or n.startswith(nq + " "):
                    found[q].append((name, rest))
for q, ents in found.items():
    rec = {"table": "cik-lookup-data.txt (EDGAR entity names, file dated 2026-08-10)", "entities": []}
    for name, cik in ents[:6]:
        wait("sec")
        r = subprocess.run(["curl", "-s", "-m", "60", "-A", UA, f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json"], capture_output=True)
        try:
            d = json.loads(r.stdout)["filings"]["recent"]
            fd = sorted((dt, fm, a) for fm, dt, a in zip(d["form"], d["filingDate"], d["accessionNumber"]) if fm in ("D", "D/A"))
            rec["entities"].append({"name": name, "cik": cik, "status": "ok", "forms": sorted(set(d["form"]))[:12],
                                    "formd": [{"date": a, "form": b, "adsh": c} for a, b, c in fd]})
        except Exception as e:
            rec["entities"].append({"name": name, "cik": cik, "status": "error", "error": f"rc={r.returncode} {e}"})
        time.sleep(0.2)
    out[q] = rec
out_p.write_text(json.dumps(out, indent=1) + "\n")
for q in sys.argv[1:]:
    v = out[q]; print("##", q, "->", len(v["entities"]), "entities")
    for e in v["entities"]:
        print("   ", e["name"], e["cik"], e["status"], [f"{x['date']} {x['form']}" for x in e.get("formd", [])], (e.get("forms") or [])[:6])
