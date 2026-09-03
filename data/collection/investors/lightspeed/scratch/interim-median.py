#!/usr/bin/env python3
"""PRO-69 interim entry-round median (pre-base, §11).

Method (the Accel pre-base corroboration shape): over the partner-anchored
Form D sweep, keep issuers whose name matches a company on the firm's own
site list (LSVP-participating rows only), anchor each issuer at its EARLIEST
partner-matched filing (the entry proxy; the first filed round is a ceiling
on entry recency), and take the median of that round's total_sold across
issuers with a priced (nonzero) amount. Interim until the base lands; the
final median recomputes over membership-verified rows with full issuer round
histories (formd-issuer-rounds.py).

Usage: python3 scratch/interim-median.py
"""
import json
import re
import statistics
from pathlib import Path

HERE = Path(__file__).resolve().parent
INV = HERE.parent

def norm(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[,.]", " ", s)
    s = re.sub(r"\b(inc|corp|corporation|co|llc|l\.l\.c|ltd|limited|holdings?|labs?|technologies|technology|tech|systems?|software|ai|io|com|hq)\b", " ", s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return " ".join(s.split())

def main() -> None:
    sweep = json.loads((INV / "sources/edgar/formd-sweep.json").read_text())
    comp = json.loads((INV / "sources/site/companies.json").read_text())
    rows = comp["companies"] if isinstance(comp, dict) and "companies" in comp else comp
    site = {}
    for r in rows:
        if (r.get("investor") or "lsvp") in ("lsvp", "both"):
            site[norm(r["name"])] = r["name"]

    own_re = re.compile(json.loads((INV / "config.json").read_text())["profile"]["own_vehicle_pattern"], re.I)

    per_issuer = {}
    for acc, rec in sweep.items():
        issuer = rec.get("issuer") or ""
        if own_re.search(issuer):
            continue  # the firm's own vehicles are not portfolio rounds
        key = norm(issuer)
        if key not in site:
            continue
        year = int(rec["quarter"][:4]) if rec.get("quarter") else None
        sold = rec.get("total_sold")
        try:
            sold = int(float(sold)) if sold not in (None, "", "Indefinite") else None
        except ValueError:
            sold = None
        cur = per_issuer.get(key)
        if cur is None or (year or 9999) < (cur["year"] or 9999):
            per_issuer[key] = {"issuer": issuer, "site_name": site[key],
                               "year": year, "sold": sold, "accession": acc}

    priced = {k: v for k, v in per_issuer.items() if v["sold"]}
    vals = sorted(v["sold"] for v in priced.values())
    print(f"site-confirmed issuers in sweep: {len(per_issuer)}; priced entries: {len(vals)}")
    if not vals:
        return
    med = statistics.median(vals)
    def pct(p):
        return vals[min(len(vals) - 1, int(p * len(vals)))]
    print(f"median entry round: ${med:,.0f}")
    print(f"p10 ${pct(.10):,} | p25 ${pct(.25):,} | p75 ${pct(.75):,} | p90 ${pct(.90):,}")
    (HERE / "interim-median.json").write_text(json.dumps({
        "method": "earliest partner-anchored Form D per site-confirmed issuer, priced rounds only",
        "issuers_matched": len(per_issuer), "priced": len(vals),
        "median": med, "p10": pct(.10), "p25": pct(.25), "p75": pct(.75), "p90": pct(.90),
        "entries": sorted(priced.values(), key=lambda v: -(v["sold"] or 0)),
    }, indent=1))
    print("wrote scratch/interim-median.json")

if __name__ == "__main__":
    main()
