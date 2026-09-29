"""Run scripts/graduation-surfaces.py for HV without editing the shared script:
the firm alias ("HV Capital" OR "Holtzbrinck Ventures" OR "HV Holtzbrinck") is set
in the module's FIRM_TERMS at import, and each row's country comes from the firm's
own HQ field (live export, then the archived lists) where the classification has
none yet, so German rows get the de-DE edition too.
Usage: surfaces.py [--all | --slugs a,b | --all-seed]"""
import csv, importlib.util, json, re, sys
from pathlib import Path
H = Path(__file__).resolve().parent; INV = H.parent; ROOT = INV.parents[3]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec)
argv = sys.argv[1:]; sys.argv = sys.argv[:1]
spec.loader.exec_module(gs)
gs.FIRM_TERMS["hv-capital"] = '("HV Capital" OR "Holtzbrinck Ventures" OR "HV Holtzbrinck")'
CC = {"Germany": "DE", "United Kingdom": "GB", "United States of America": "US", "USA": "US", "Netherlands": "NL",
      "France": "FR", "Switzerland": "CH", "Spain": "ES", "Austria": "AT", "Denmark": "DK", "Singapore": "SG",
      "Philippines": "PH", "Canada": "CA", "Finland": "FI", "Croatia": "HR", "Italy": "IT", "Sweden": "SE",
      "UK": "GB", "England": "GB", "Russia": "RU", "India": "IN", "Brazil": "BR", "Israel": "IL", "Poland": "PL"}
def k(s): return re.sub(r"[^a-z0-9]", "", (s or "").lower())
hq = {}
for r in csv.DictReader(open(INV / "sources/site/portfolio-2026.csv", encoding="utf-8-sig")):
    hq[k(r["Name"])] = CC.get(r["HQ"].split(",")[-1].strip())
ev = json.loads((H / "archive-evidence.json").read_text())
for s, e in ev.items():
    for h in e.get("hq") or []:
        c = CC.get(h.split(",")[-1].strip())
        if c: hq.setdefault(k(s), c)
orig = gs.targets_for
def targets_for(investor, all_seed, slugs):
    out = orig(investor, all_seed, slugs)
    for slug, row in out.items():
        if not row.get("_country"):
            row["_country"] = hq.get(k(slug)) or hq.get(k(row.get("name")))
    return out
gs.targets_for = targets_for
if "--all" in argv:
    slugs = {r["slug"] for r in json.loads((INV / "companies/base.json").read_text())}
elif "--slugs" in argv:
    slugs = set(argv[argv.index("--slugs") + 1].split(","))
else:
    slugs = None
gs.run("hv-capital", "--all-seed" in argv, slugs, "--refresh" in argv)
