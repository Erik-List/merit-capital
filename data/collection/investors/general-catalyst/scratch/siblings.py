#!/usr/bin/env python3
"""What the sibling investors' published bases say about General Catalyst rows:
scratch/siblings.json, slug -> [sibling facts], joined on the loose name key
(and the CIK where both sides carry one). Read for the judge's cards and for
aligning status and band with siblings from the start (verify invariant 10).
A sibling row is a HINT with its own citation, never evidence of General Catalyst
membership. Usage: python3 .../scratch/siblings.py"""
import csv, glob, json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
INV = ROOT / "data/collection/investors/general-catalyst"
def key(n):
    n = (n or "").lower(); n = re.sub(r"\(.*?\)", " ", n); n = re.sub(r"[^a-z0-9 ]+", " ", n)
    n = re.sub(r"\b(inc|corp|corporation|co|ltd|llc|lp|plc|holdings?|group|technologies|technology|labs?|the|hq|ai|io|com|global|industries|systems)\b", " ", n)
    return re.sub(r"\s+", "", n)
KEEP = ["status", "valuation_range", "valuation_usd", "valuation_asof", "valuation_source", "valuation_citation", "entry_stage",
        "entry_stage_source", "entry_stage_citation", "entry_date", "hq_city", "hq_country", "focus", "first_seen", "flags", "note"]
sib = {}
for f in sorted(glob.glob(str(ROOT / "data/collection/investors/*/companies/base.csv"))):
    slug = f.split("/")[-3]
    if slug == "general-catalyst": continue
    inflight = (Path(f).parents[1] / "scratch/in-flight.json").exists()
    with open(f, newline="") as fh:
        for r in csv.DictReader(fh):
            if r.get("membership_verdict") == "not_member": continue
            rec = {"investor": slug, "in_flight": inflight, "name": r["name"]}
            rec.update({k: (r.get(k) or "") for k in KEEP})
            rec["note"] = rec["note"][:500]
            sib.setdefault(key(r["name"]), []).append(rec)
base = json.load(open(INV / "companies/base.json"))
rows = base if isinstance(base, list) else list(base.values())
out = {}
for r in rows:
    k = key(r["name"])
    if k and len(k) >= 3 and k in sib:
        out[r["slug"]] = sib[k]
(INV / "scratch/siblings.json").write_text(json.dumps(out, indent=1))
print(len(out), "of", len(rows), "rows have sibling facts")
