"""Rebuild graduation_surfaces on every recorded `not_graduated` from the completed
surfaces layer (scratch/graduation-surfaces.json, 419 rows, 0 failed lookups), keeping
only the agent's company-site or firm-post lines beside it. Rows converted while the
layer was still running had fewer publisher lines, and an 'agent:' line is not a
publisher surface. Emits only the graduation keys (no note: record-twice note bug)."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as J
cls = json.loads((J.INV / "companies/classification.json").read_text())
cls = cls.get("speedinvest", cls)
cls = cls.get("rows", cls) if isinstance(cls, dict) and "rows" in cls else cls
RS = {}
import glob
for f in glob.glob(str(J.H / "research" / "g*.json")):
    if "groups" not in f:
        RS.update(json.load(open(f)))
L = []
for slug, r in cls.items():
    if not isinstance(r, dict) or r.get("seed_to_a_graduation") != "not_graduated":
        continue
    old = r.get("graduation_surfaces") or []
    src = r.get("graduation_source")
    finding = "no later round found before the sale or shutdown" if src in ("web_verified", "first_party") else "no later round named"
    new = J.surfaces_lines(slug, finding)
    extra = [x for x in old if x.split(":", 1)[0].strip().lower() in ("company", "formd", "register", "wikipedia")]
    for x in (RS.get(slug, {}).get("graduation") or {}).get("searched") or []:
        k = x.split(":", 1)[0].strip().lower()
        if k.startswith("company") and x not in extra:
            extra.append("company:" + x.split(":", 1)[1] if ":" in x else "company: " + x)
    if r.get("hq_country") == "US" and not any(x.startswith("formd:") for x in extra):
        extra.append("formd: EDGAR company search for the name -> no Form D sequence after the entry")
    lines = new + extra
    if lines != old:
        L.append({"slug": slug, "who": J.WHO, "seed_to_a_graduation": "not_graduated", "graduation_source": src,
                  "graduation_asof": J.ASOF, "graduation_surfaces": lines})
print(len(L), "rows patched")
J.write("patch-surfaces-1", L)
