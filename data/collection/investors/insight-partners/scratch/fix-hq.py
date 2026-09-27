#!/usr/bin/env python3
"""Re-apply the hand correction of the firm's office record after build-firm-profile.py.

firm-offices.py reads the contact page's 'Headquarters 1114 Avenue of the Americas, 36th Floor
New York 10036' as the city 'Floor' in the state 'New York' (its US address pattern takes a
state name before the ZIP), so every build publishes 'Floor, NY'. The page names the New York
office, the Form ADV principal office. This script corrects the stored record and re-applies
the rule; remove it once the spawned fix to firm-offices.py lands.
Usage: python3 data/collection/investors/insight-partners/scratch/fix-hq.py"""
import importlib.util, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402
spec = importlib.util.spec_from_file_location("fo", ROOT / "scripts" / "firm-offices.py")
fo = importlib.util.module_from_spec(spec); spec.loader.exec_module(fo)
p = Paths("insight-partners")
rec = json.loads(p.offices.read_text())
for o in rec.get("site", {}).get("offices", []):
    if o["place"] == "Floor, NY":
        o["place"] = "New York, NY"
        o["corrected"] = ("by hand: firm-offices.py read '36th Floor New York 10036' as the city 'Floor' in "
                          "the state 'New York'; the page's headquarters is the New York office, the Form ADV "
                          "principal office")
write_atomic(p.offices, json.dumps(rec, indent=1, ensure_ascii=False) + "\n")
st = fo.statement_of(p)
hq = fo.decide(rec, st)
inv = json.loads(p.investor.read_text()); inv["hq_location"] = hq["value"]
src = json.loads(p.investor_sources.read_text()); src["fields"]["hq_location"] = fo.hq_field(rec, hq, st)
write_atomic(p.investor, json.dumps(inv, indent=2, ensure_ascii=False) + "\n")
write_atomic(p.investor_sources, json.dumps(src, indent=2, ensure_ascii=False) + "\n")
print("hq", hq["value"], hq["won_by"])
