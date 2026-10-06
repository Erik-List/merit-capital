#!/usr/bin/env python3
"""FTS third-party registrants absent from the base, pre-classified by filing shape, sharded for triage
(RECALL-FTS-BRIEF.md). Classes, in triage order: holder-table (S-1/F-1/424B/10-12G/S-4 with an ownership table),
merger (S-4/DEFM14A/425/8-K/SC TO), proxy (DEF 14A/10-K only: director bios or 5% holders), spac (blank-check
names), fund-noise (N-PX/N-CSR/485/N-Q/497: LP-side, auto-reject), other.
Writes fts-candidates.json {"_readme", "rows": [{registrant, cik, forms, first_date, cls, shard}]}."""
import json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
regs = json.loads((HERE.parent / "sources/edgar/fts-hits.json").read_text())["registrants"]
base = json.loads((HERE.parent / "companies/base.json").read_text())
SUF = r"\b(inc|ltd|limited|llc|corp|corporation|co|company|the|plc|holdings|group|sa|nv|ag)\b\.?"
def norm(s):
    s = re.sub(r"\(.*?\)", " ", (s or "").lower().replace("&", "and"))
    return re.sub(r"[^a-z0-9]+", "", re.sub(SUF, "", re.sub(r"/[a-z]{2}/?$", "", s)))
names = {norm(r["name"]) for r in base} | {norm(r["slug"].replace("-", " ")) for r in base}
rows = []
for r in regs:
    if r.get("bucket") != "third_party":
        continue
    n = norm(r["registrant"])
    if n in names or any(len(n) > 5 and (k.startswith(n) or n.startswith(k)) and len(k) > 5 for k in names):
        continue
    f = set(r["forms"])
    nm = r["registrant"].lower()
    if f <= {"N-PX", "N-CSR", "N-CSRS", "485BPOS", "485APOS", "N-Q", "497", "497K", "N-30D", "NPORT-P", "N-2", "N-14", "40-17G"} or \
            re.search(r"\b(trust|funds?|portfolios?|etf|variable|series)\b", nm):
        cls = "fund-noise"
    elif re.search(r"acquisition (corp|co|company|holdings)|\bspac\b|capital venture acquisition", nm):
        cls = "spac"
    elif f & {"S-1", "S-1/A", "F-1", "F-1/A", "424B4", "424B1", "424B3", "10-12G", "10-12G/A", "DRS", "SB-2"}:
        cls = "holder-table"
    elif f & {"S-4", "S-4/A", "DEFM14A", "PREM14A", "425", "SC TO-T", "SC 14D9", "8-K", "F-4"}:
        cls = "merger"
    elif f & {"DEF 14A", "10-K", "10-K405", "PRE 14A", "20-F"}:
        cls = "proxy"
    else:
        cls = "other"
    rows.append({"registrant": r["registrant"], "cik": r["cik"], "forms": r["forms"], "first_date": r["first_date"], "cls": cls})
order = {"holder-table": 0, "merger": 1, "other": 2, "proxy": 3, "spac": 4, "fund-noise": 5}
rows.sort(key=lambda r: (order[r["cls"]], r["first_date"]))
triage = [r for r in rows if r["cls"] != "fund-noise"]
N = int(sys.argv[1]) if len(sys.argv) > 1 else 4
for i, r in enumerate(triage):
    r["shard"] = i % N
for r in rows:
    r.setdefault("shard", None)
(HERE / "fts-candidates.json").write_text(json.dumps({"_readme": __doc__, "rows": rows}, indent=1) + "\n")
import collections
print(len(rows), "absent from the base;", collections.Counter(r["cls"] for r in rows), "; shards", collections.Counter(r["shard"] for r in triage))
