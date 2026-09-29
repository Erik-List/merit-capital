"""Duty 9 class sweep (PRO-104): the 47 rows left 'unknown', settled from registers and press (German recipe, D9)."""
import json
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write  # noqa: E402

H = Path(__file__).resolve().parent
cl = json.loads((H.parent / "companies/classification.json").read_text())
out = json.loads((H / "sweep-status-out.json").read_text())
DONE = {"eating-with-the-chefs", "fettspielen-de", "hitfox-group", "kyte", "musicplayr"}  # duty 7 recorded these
OVERRIDE = {
    "loots": ("defunct", "The operator fishwoodco GmbH went insolvent in 2019-10 and was deleted in 2025-10; the founder "
                         "runs the brand on under a new company, with no documented sale out of the insolvency, so the "
                         "row reads defunct (D9)."),
    "virtual-nights": ("defunct", "The operator virtual:nights:media Ltd went insolvent on 2024-10-01 (AG Essen); a new "
                                  "Virtual Nights Media GmbH registered in 2026-06 runs the magazine, with no documented "
                                  "sale, so the row reads defunct (D9)."),
    "mercavus": ("defunct", "Faire bought mercavus in Feb 2022 (deutsche-startups) and shut the platform, while HV Fund VII "
                            "stayed on the register's shareholder list in 2025: a team-and-asset deal, which never decides "
                            "status (the acqui-hire rule), so the row reads defunct."),
    "tutoria": ("acquired", "acq. (100%) by Holtzbrinck Digital, the parent's internet arm, 2010-08 (deutsche-startups): a "
                            "sale to the publishing group, as D2 reads StudiVZ."),
}
L = []
for r in out:
    s = r["slug"]
    if s in DONE or r["status"] == "unknown":
        continue
    status = r["status"]
    event = r.get("event", "").rstrip(".")
    if s in OVERRIDE:
        status, sentence = OVERRIDE[s]
    else:
        sentence = event[0].upper() + event[1:] + "."
    old = cl.get(s, {}).get("note") or ""
    old = re.sub(r"\s*(Its|The company's) later (corporate )?state (was|is) not (found|established)\.?", "", old).strip()
    note = (old + " " if old else "") + sentence
    kw = {}
    if r.get("hq_city") and not cl.get(s, {}).get("hq_city"):
        kw["city"] = r["hq_city"]
    L.append(cls(s, status=status, rng="below_1b", note=note,
                 clear=["city_unknown"] if kw.get("city") else (),
                 extra={"status_citation": r["status_citation"]}, **kw))
write("status-sweep-001", L)
print(len(L))
