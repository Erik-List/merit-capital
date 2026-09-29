#!/usr/bin/env python3
"""Supplement entities.json from the SEC CIK lookup table (PRO-167).

edgar-entities.py seeds the registry from the EDGAR company-name search
(cgi-bin/browse-edgar?company=...), and on 2026-09-29 that endpoint answered
every query with the new smart-search landing page instead of a results table,
so the seed returned nothing and the registry held only what the Form D pooled
filers and the co-filer closure found (27 of Tiger's vehicles; PIP I to VII, the
FB and LinkedIn holdcos, the crossover funds, the PIP 1 series and Tiger Veda
were missing). This reads the same names from the local lookup table
(data/collection/shared/sec/cik-lookup-data.txt), classifies each with the
investor's own desk rules, and adds the missing ones as confirmed rows with
source `cik-lookup`. Re-run it after any edgar-entities.py run, which rebuilds
the registry from scratch and drops rows it did not find itself.
"""
import json, re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, SEC_CACHE, write_atomic  # noqa: E402

P = Paths("tiger-global-management")
cfg = P.config()
rules = [(r["desk"], [re.compile(p) for p in r["patterns"]]) for r in cfg["desks"]["classify"]]
PAT = re.compile(r"^(tiger global|tiger technology|tiger veda|internet fund (iii|iv|v|vi|vii)\b)", re.I)
EXTERNAL_PAT = re.compile(r"(tiger global|tiger veda)", re.I)


def desk_of(name):
    n = name.lower()
    for d, pats in rules:
        if any(p.search(n) for p in pats):
            return d
    return "unknown"


def role_of(name):
    n = name.lower()
    if "management" in n:
        return "management"
    if "performance" in n or "partners, l" in n or "holding" in n:
        return "fund"
    return "fund"


ents = json.loads(P.entities.read_text())
have = {e["cik"] for e in ents}
added = []
seen = {}
for line in (SEC_CACHE / "cik-lookup-data.txt").open(encoding="latin-1"):
    parts = line.rstrip("\n").rsplit(":", 2)
    if len(parts) < 3:
        continue
    name, cik = parts[0].strip(), str(int(parts[1]))
    if not (PAT.search(name) or EXTERNAL_PAT.search(name)):
        continue
    # keep the longest rendering per CIK
    if cik not in seen or len(name) > len(seen[cik]):
        seen[cik] = name
for cik, name in sorted(seen.items(), key=lambda x: x[1]):
    d = desk_of(name)
    if d == "unknown":
        # a name carrying the brand that no desk rule claims: a third-party feeder
        # or a namesake; kept out of crawling
        d = "external"
    if cik in have:
        continue
    row = {"cik": cik, "name": name, "desk": d, "vehicle_role": role_of(name),
           "sources": ["cik-lookup"], "confirmed": True}
    ents.append(row)
    added.append(row)
ents.sort(key=lambda r: (r["desk"], r["name"].lower()))
write_atomic(P.entities, json.dumps(ents, indent=1) + "\n")
print(f"added {len(added)} entities (total {len(ents)})")
for r in added:
    print(f"  {r['cik']:>8} {r['desk']:8} {r['name']}")
