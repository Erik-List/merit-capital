"""Filing addresses of every candidate own entity (SEC submissions API, through the machine-wide SEC throttle) into
scratch/entity-addresses.json: the namesake check for the 'BVP' and 'Deer' filers (COLLECTION.md s5.3: explicit
external patterns first; a namesake that shares the firm's name pattern is caught by its address)."""
import json, subprocess, sys, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
import shared_throttle
UA = "Merit Capital research erik@meritcapit.al"
ents = json.loads((HERE.parent / "entities.json").read_text())
out_p = HERE / "entity-addresses.json"
out = json.loads(out_p.read_text()) if out_p.exists() else {}
for e in ents:
    cik = str(e["cik"])
    if cik in out:
        continue
    shared_throttle.wait("sec")
    r = subprocess.run(["curl", "-s", "-m", "40", "-H", f"User-Agent: {UA}", f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json"], capture_output=True)
    try:
        d = json.loads(r.stdout)
    except ValueError:
        print("FAILED", cik, e["name"]); continue
    a = d.get("addresses", {})
    rec = d.get("filings", {}).get("recent", {})
    out[cik] = {"name": d.get("name"), "business": a.get("business"), "mailing": a.get("mailing"),
                "forms": sorted(set(rec.get("form", [])))[:12], "first": min(rec.get("filingDate") or [""]),
                "last": max(rec.get("filingDate") or [""]), "n": len(rec.get("form", [])), "former": [f.get("name") for f in d.get("formerNames", [])]}
    out_p.write_text(json.dumps(out, indent=1))
fmt = lambda a: ", ".join(str(a.get(k) or "") for k in ("street1", "city", "stateOrCountry")) if a else ""
for e in sorted(ents, key=lambda e: (e["desk"], e["name"])):
    o = out.get(str(e["cik"]), {})
    print(e["desk"], "|", e["name"], "|", fmt(o.get("business")), "|", o.get("first"), o.get("last"), o.get("n"), o.get("forms"))
