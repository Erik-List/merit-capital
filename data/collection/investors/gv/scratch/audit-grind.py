#!/usr/bin/env python3
"""Post-grind audit for the GV run (PRO-75): reads the MERGED view (resolved.json overlaid by classification.json,
over the live base; COLLECTION.md s8) and lists what the next passes need.

  unclassified   member rows with an open need (the judges' misses)
  prefill        rows whose status still comes from a deterministic pre-fill that a sibling book contradicts
  mixed          the five rows whose evidence packs mixed two companies before the never_merge fix
  seed_open      Seed / Pre-Seed rows without a decided S2A status (the graduation pass)
  momentum       private rows first seen 2021+ in the hot sectors, with or without a recorded check
  visible        every $1B+ or public row (the A/B pass)
Output: scratch/audit-grind.json and a printed summary.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

P = Paths("gv")
base = {r["slug"]: r for r in json.loads(P.base_json.read_text())}
led = json.loads(P.ledger.read_text())["gv"]["verdicts"]
res = json.loads(P.resolved.read_text())
res = res.get("gv", res) if isinstance(res, dict) else {}
cla = json.loads(P.classification.read_text())
cla = cla.get("gv", cla)
cla = cla.get("rows", cla) if isinstance(cla, dict) else {}
sib = json.loads((HERE / "siblings.json").read_text()) if (HERE / "siblings.json").exists() else {}
q = {i["slug"]: i for i in json.loads((HERE / "queue" / "queue.json").read_text())}
TWINS = {"rosa-foods-inc", "denver-technologies-inc", "noho-dental-inc", "asset-blue-pharmacy-services-inc"}
HOT = {"AI & Applied AI", "Fintech & Payments", "Data Infrastructure", "DevTools & APIs"}


def merged(s):
    m = dict(res.get(s) or {})
    m.update({k: v for k, v in (cla.get(s) or {}).items() if v is not None})
    return m


out = {"unclassified": [], "prefill": [], "mixed": [], "seed_open": [], "momentum": [], "visible": []}
for s, r in base.items():
    if (led.get(s) or {}).get("verdict") != "member" or s in TWINS:
        continue
    m = merged(s)
    need = [n for n in (q.get(s) or {}).get("need", []) if n != "membership"]
    open_ = [n for n in need if n not in m or m.get(n) in (None, "")]
    if "hq_city" in open_ and "city_unknown" in (m.get("flags") or []):
        open_.remove("hq_city")
    if s not in cla:
        out["unclassified"].append(s)
    st = m.get("status")
    sst = {x.get("status") for x in sib.get(s, []) if x.get("status")}
    if st and sst and st not in sst and s not in cla:
        out["prefill"].append((s, st, sorted(sst)))
    if s in ("secret-escapes", "astrid", "bloom-institute-of-technology", "spruce-finance", "sense"):
        out["mixed"].append((s, m.get("status"), m.get("entry_stage"), (m.get("note") or "")[:160]))
    if m.get("entry_stage") in ("Seed", "Pre-Seed") and m.get("seed_to_a_graduation") not in (
            "graduated", "not_graduated", "censored"):
        out["seed_open"].append(s)
    fs = str(r.get("first_seen") or "")[:4]
    if st == "private" and fs.isdigit() and int(fs) >= 2021 and m.get("focus") in HOT:
        checked = bool(re.search(r"(?i)momentum|checked|no \$1b|no priced round", m.get("note") or "")) or \
            m.get("valuation_range_source") == "web_verified"
        out["momentum"].append((s, checked))
    if st == "public" or m.get("valuation_range") in ("1b_plus", "10b_plus", "100b_plus"):
        out["visible"].append((s, st, m.get("valuation_range"), m.get("valuation_usd"), m.get("valuation_asof"),
                               m.get("valuation_source")))
write_atomic(HERE / "audit-grind.json", json.dumps(out, indent=1, ensure_ascii=False) + "\n")
print({k: len(v) for k, v in out.items()})
print("momentum checked:", sum(1 for _, c in out["momentum"] if c), "of", len(out["momentum"]))
for k in ("prefill", "mixed"):
    for x in out[k]:
        print(k, x)
