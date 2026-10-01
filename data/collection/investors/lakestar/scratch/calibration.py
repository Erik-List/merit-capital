"""Calibration table (PRO-108 done-when): this book against the archetype-B siblings, read from each book's
published base.csv (members only, unnameable rows out of every metric)."""
import csv, sys
from pathlib import Path
INV = Path(__file__).resolve().parents[2]
BOOKS = ["lakestar", "cherry", "creandum", "hv-capital", "balderton-capital", "point-nine", "project-a-ventures", "northzone"]
print("| Book | Rows | Acquired | Defunct | Private | $1B+ | S2A |\n|---|---|---|---|---|---|---|")
for b in BOOKS:
    rows = [r for r in csv.DictReader(open(INV / b / "companies/base.csv"))
            if r.get("membership_verdict") == "member" and r.get("valuation_range") != "undetermined"]
    n = len(rows)
    if not n:
        print(f"| {b} | not exported |"); continue
    st = lambda s: sum(1 for r in rows if r["status"] == s) / n
    big = sum(1 for r in rows if r["valuation_range"] in ("1b_plus", "10b_plus", "100b_plus")) / n
    seed = [r for r in rows if r["entry_stage"] == "Seed"]
    g = sum(1 for r in seed if r["seed_to_a_graduation"] == "graduated")
    ng = sum(1 for r in seed if r["seed_to_a_graduation"] == "not_graduated")
    s2a = f"{g}/{g+ng} = {g/(g+ng):.0%}" if g + ng else "-"
    print(f"| {b} | {n} | {st('acquired'):.0%} | {st('defunct'):.0%} | {st('private'):.0%} | {big:.1%} | {s2a} |")
