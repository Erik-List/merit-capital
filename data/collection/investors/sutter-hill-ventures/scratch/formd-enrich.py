#!/usr/bin/env python3
"""Every related person, with address and all three role slots, on every
accession the roster sweep (formd-sweep.json) or the address sweep matched.

The roster sweep keeps a name and RELATIONSHIP_1; the judge needs the address
the person filed from (the firm's office, the issuer's, another firm's) and
the other people on the filing to resolve a common name once per cluster
(COLLECTION.md §3, cluster-first).

Output: scratch/formd-persons.json  accession -> [ {person, roles, street, city, state} ]
"""
import csv, io, json, sys, zipfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402
P = Paths("sutter-hill-ventures")
accs = set(json.load(open(P.edgar / "formd-sweep.json"))) | set(json.load(open(P.edgar / "formd-address-sweep.json")))
out = {}
for z in sorted((ROOT / "data/filings/form-d").glob("*.zip")):
    with zipfile.ZipFile(z) as zf:
        rp = next((n for n in zf.namelist() if n.upper().endswith("RELATEDPERSONS.TSV")), None)
        if not rp:
            continue
        with zf.open(rp) as f:
            for row in csv.DictReader(io.TextIOWrapper(f, encoding="utf-8", errors="replace"), delimiter="\t"):
                a = row["ACCESSIONNUMBER"]
                if a not in accs:
                    continue
                out.setdefault(a, []).append({
                    "person": " ".join(f"{row.get('FIRSTNAME') or ''} {row.get('MIDDLENAME') or ''} {row.get('LASTNAME') or ''}".split()),
                    "roles": [row.get(k) for k in ("RELATIONSHIP_1", "RELATIONSHIP_2", "RELATIONSHIP_3") if row.get(k)],
                    "clarification": row.get("RELATIONSHIPCLARIFICATION") or "",
                    "street": " ".join(f"{row.get('STREET1') or ''} {row.get('STREET2') or ''}".split()),
                    "city": row.get("CITY") or "", "state": row.get("STATEORCOUNTRY") or ""})
write_atomic(P.scratch / "formd-persons.json", json.dumps(out, indent=1) + "\n")
print(len(out), "accessions")
