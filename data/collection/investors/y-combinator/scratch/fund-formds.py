#!/usr/bin/env python3
"""YC's own fund-vehicle Form D filings, from the local quarterly bulk zips.

Same shape as the USV run's scratch/fund-formds.py: every accession whose
issuer CIK is an own-desk entity in entities.json, with the filing's named
related persons kept as filing-grade roster corroboration per vintage.
"""
import csv, io, json, sys, zipfile
from collections import defaultdict
from pathlib import Path
sys.path.insert(0, "scripts")
from paths import Paths, write_atomic  # noqa: E402

SLUG = "yc"
p = Paths(SLUG)
ents = json.loads(p.entities.read_text())
own = {str(int(e["cik"])) for e in ents if e.get("desk") not in (None, "external")}
print(f"own-desk CIKs: {len(own)}")

out = {"_readme": {
    "note": ("Y Combinator's own fund-vehicle Form D filings from the local quarterly bulk "
             "zips (data/filings/form-d/), every accession whose issuer CIK is an own-desk "
             "entity of entities.json. related_persons are the filing's named executive "
             "officers, directors and promoters — filing-grade roster corroboration per "
             "vintage. NOTE: four vehicles in YC's Form ADV Section 7.B appear in NO EDGAR "
             "filing at all (Y Combinator Fund I and II, YCVC Fund I, YCVC W14), so this "
             "sweep is not the whole fund ladder; the ADV is."),
    "built": "2026-09-07"}}

zips = sorted(Path("data/filings/form-d").glob("*.zip"))
hits = 0
for z in zips:
    try:
        zf = zipfile.ZipFile(z)
    except Exception:
        continue
    # members are namespaced by quarter, e.g. "2024Q2_d/ISSUERS.tsv"
    def member(base):
        for n in zf.namelist():
            if n.upper().endswith("/" + base) or n.upper() == base:
                return n
        return None
    iss, off, rel = member("ISSUERS.TSV"), member("OFFERING.TSV"), member("RELATEDPERSONS.TSV")
    if not iss:
        continue
    def rows(member):
        if not member: return []
        with zf.open(member) as fh:
            return list(csv.DictReader(io.TextIOWrapper(fh, "utf-8", errors="replace"), delimiter="\t"))
    mine = {}
    for r in rows(iss):
        cik = str(r.get("CIK") or r.get("cik") or "").lstrip("0")
        if cik in own:
            mine[r.get("ACCESSIONNUMBER") or r.get("accessionnumber")] = {
                "issuer": r.get("ENTITYNAME") or r.get("entityname"),
                "cik": cik, "quarter": z.stem,
                "state": r.get("STATEORCOUNTRY") or r.get("stateorcountry"),
                "city": r.get("CITY") or r.get("city"),
                "related_persons": [], "sold": None, "total_offering": None}
    if not mine:
        continue
    for r in rows(off):
        a = r.get("ACCESSIONNUMBER") or r.get("accessionnumber")
        if a in mine:
            mine[a]["sold"] = r.get("TOTALAMOUNTSOLD") or r.get("totalamountsold")
            mine[a]["total_offering"] = r.get("TOTALOFFERINGAMOUNT") or r.get("totalofferingamount")
    for r in rows(rel):
        a = r.get("ACCESSIONNUMBER") or r.get("accessionnumber")
        if a in mine:
            nm = " ".join(x for x in [r.get("FIRSTNAME") or r.get("firstname"),
                                      r.get("LASTNAME") or r.get("lastname")] if x).strip()
            if nm:
                mine[a]["related_persons"].append(nm)
    out.update(mine); hits += len(mine)
    print(f"  {z.stem}: {len(mine)}")
write_atomic(p.edgar / "fund-formds.json", json.dumps(out, indent=1, ensure_ascii=False))
print(f"wrote fund-formds.json — {hits} own-vehicle filings")
