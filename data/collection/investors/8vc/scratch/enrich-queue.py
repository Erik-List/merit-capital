#!/usr/bin/env python3
"""Put the seat-dating evidence into the queue item, where the judge can use it.

COLLECTION.md §1 T4: "a seat is dated against the person's firm at filing time,
not against the roster", and §8: a class-1 layer the item does not carry is a
layer the grind cannot use. The queue ships `partners_formd` as bare names, so
the judge cannot tell an in-tenure seat from an out-of-tenure one without going
back to the roster per row.

Measured on this run: Ushur's 2018q3 Form D carries BHASKAR GHOSH, whose 8VC
tenure begins in 2020 (he was NerdWallet's VP Eng and an 8VC ADVISOR in 2018),
and the entry-stage band read that filing as 8VC's entry — Series A against the
firm's own post putting its entry at the 2020 Series B.

Adds per item:
  formd_attribution : [{person, quarter, accession, offering_usd, tenure,
                        in_tenure}], one row per person-filing pair
  out_of_tenure     : true where the EARLIEST attributed filing is out of tenure
                      — the rows where a band entry stage is most likely wrong

Idempotent; rewrites queue.json and the batch files.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

P = Paths("8vc")
QD = P.root / "scratch" / "queue"
sweep = json.loads((P.root / "sources" / "edgar" / "formd-sweep.json").read_text())
roster = json.loads((P.root / "sources" / "wayback" / "partner-roster.json").read_text())
base = json.loads(P.base_json.read_text())
rows = base["companies"] if isinstance(base, dict) and "companies" in base else base


def norm(s: str) -> str:
    return re.sub(r"[^a-z]", "", (s or "").lower())


tenure = {norm(p["name"]): (p["first_seen"], p["last_seen"]) for p in roster}
by_cik, by_name = {}, {}
for acc, v in sweep.items():
    rec = {"accession": acc, "issuer": v["issuer"], "cik": str(int(v["cik"])) if v.get("cik") else None,
           "offering_usd": int(v["total_offering"]) if (v.get("total_offering") or "").isdigit() else None,
           "persons": v.get("persons", [])}
    if rec["cik"]:
        by_cik.setdefault(rec["cik"], []).append(rec)
    by_name.setdefault(norm(v["issuer"]), []).append(rec)

slug_cik = {r["slug"]: (str(int(r["edgar_cik"])) if r.get("edgar_cik") else None) for r in rows}
slug_name = {r["slug"]: norm(r["name"]) for r in rows}


by_acc = {}
for acc, v in sweep.items():
    by_acc[acc] = {"accession": acc, "issuer": v["issuer"],
                   "offering_usd": int(v["total_offering"]) if (v.get("total_offering") or "").isdigit() else None,
                   "persons": v.get("persons", [])}
slug_accs = {r["slug"]: [a.strip() for a in (r.get("formd_accessions") or "").split(";") if a.strip()]
             for r in rows}


def attributions(slug: str) -> list[dict]:
    """Join on the accessions `build-company-base.py` already resolved for the row —
    the issuer NAME does not join (the sweep carries "USHUR, INC." against a base
    row named "Ushur") and many rows carry no CIK."""
    recs = [by_acc[a] for a in slug_accs.get(slug, []) if a in by_acc]
    if not recs:
        recs = by_cik.get(slug_cik.get(slug) or "", []) or by_name.get(slug_name.get(slug, ""), [])
    out = []
    for rec in recs:
        for p in rec["persons"]:
            y = int(p["quarter"][:4])
            t = tenure.get(norm(p["person"]))
            out.append({"person": p["person"], "quarter": p["quarter"], "accession": rec["accession"],
                        "offering_usd": rec["offering_usd"],
                        "tenure": f"{t[0]}-{t[1]}" if t else None,
                        "in_tenure": None if not t else (t[0] <= y <= t[1])})
    return sorted(out, key=lambda x: x["quarter"])


def fix(item: dict) -> dict:
    a = attributions(item["slug"])
    if a:
        item["formd_attribution"] = a
        item["out_of_tenure"] = a[0]["in_tenure"] is False
    else:
        item.pop("formd_attribution", None)
        item.pop("out_of_tenure", None)
    return item


q = [fix(it) for it in json.loads((QD / "queue.json").read_text())]
write_atomic(QD / "queue.json", json.dumps(q, indent=1, ensure_ascii=False))
for f in sorted(QD.glob("batch-*.json")):
    write_atomic(f, json.dumps([fix(it) for it in json.loads(f.read_text())], indent=1, ensure_ascii=False))

n = sum(1 for it in q if it.get("formd_attribution"))
bad = [it["slug"] for it in q if it.get("out_of_tenure")]
print(f"items with Form D attribution: {n}/{len(q)}")
print(f"earliest attributed filing OUT OF TENURE: {len(bad)}")
print("   ", ", ".join(sorted(bad)))
