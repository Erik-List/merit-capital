#!/usr/bin/env python3
"""Assertions over the built Company Base. Repeatable for any investor.

Each check prints PASS/FAIL with the observed value, so a regression is visible
rather than needing to be eyeballed. Exit code 1 if any assertion fails.
"""
import csv
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CB = ROOT / "data" / "aggregation" / "company-base"
ED = ROOT / "data" / "aggregation" / "sources" / "edgar"
ENT = ROOT / "data" / "aggregation" / "entities"
UA = "Merit Capital research erik@meritcapit.al"

results: list[tuple[bool, str, str]] = []


def check(ok: bool, label: str, detail: str = "") -> None:
    results.append((bool(ok), label, detail))


def http_ok(url: str) -> bool:
    try:
        code = subprocess.run(
            ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-L",
             "--max-time", "30", "-H", f"User-Agent: {UA}", url],
            capture_output=True, check=True).stdout.decode().strip()
        return code.startswith("2")
    except subprocess.CalledProcessError:
        return False


def main() -> None:
    rows = list(csv.DictReader(open(CB / "sequoia-capital.csv")))
    names = {r["name"].lower() for r in rows}
    ec = json.load(open(ED / "edgar-companies.json"))
    ec_names = {c["name"].lower() for c in ec}
    entities = json.load(open(ENT / "sequoia-capital.json"))
    ent_ciks = {e["cik"] for e in entities}

    # 1 — text-mention leak gone
    check("soros fund management llc" not in names and
          not any("soros" in n for n in ec_names),
          "text-mention leak gone (SOROS absent)",
          f"base rows: {len(rows)}")

    # 2 — co-filer leak gone
    leaks = [n for n in ("scgf iii management llc", "scgf iv management lp",
                         "scgf v management, l.p.", "francisco partners ii lp",
                         "tcv vii lp", "pequot capital management inc",
                         "saif partners iv l.p.")
             if n in names]
    check(not leaks, "co-filer leak gone (no GP/management vehicles in base)",
          f"leaked: {leaks}" if leaks else "none")

    # 3 — every base row's subject CIK is not one of our own entities
    own = [r["name"] for r in rows if r.get("edgar_cik") and r["edgar_cik"] in ent_ciks]
    check(not own, "no own-vehicle appears as a company", f"found: {own[:5]}")

    # 4 — known positions retained
    want = ["airbnb", "amplitude", "23andme", "aruba", "barracuda"]
    missing = [w for w in want if not any(w in n for n in names)]
    check(not missing, "known positions retained", f"missing: {missing}" if missing else "all present")

    # 5 — lineage partition
    other_p = CB / "other-desk-companies.csv"
    if other_p.exists():
        other = list(csv.DictReader(open(other_p)))
        onames = {r["name"].lower() for r in other}
        moved = [w for w in ("dada", "burning rock", "zto", "bona film")
                 if any(w in n for n in onames)]
        check(len(other) > 0, "lineage partition produced other-desk file",
              f"{len(other)} rows moved; matched samples: {moved}")
        overlap = names & onames
        check(not overlap, "no row in both base and other-desk", f"overlap: {list(overlap)[:5]}")
    else:
        check(False, "other-desk-companies.csv exists", "missing")

    # 6 — evidence links resolve
    el = [r["edgar_links"].split("; ")[0] for r in rows
          if r.get("edgar_links")][:3]
    fl = [r["formd_links"].split("; ")[0] for r in rows if r.get("formd_links")][:2]
    bad = [u for u in el + fl if not http_ok(u)]
    check(not bad and (el or fl), "sampled evidence links return 2xx",
          f"{len(el)} edgar + {len(fl)} formd sampled; bad: {bad}")

    # 7 — every row with EDGAR forms has EDGAR links
    gap = [r["name"] for r in rows if r["edgar_forms"] and not r.get("edgar_links")]
    check(not gap, "edgar_links populated wherever edgar_forms present",
          f"{len(gap)} gaps: {gap[:5]}")

    # 8 — regex sweep: no name-based filters left
    src = ""
    for f in ("edgar-companies.py", "build-company-base.py"):
        src += (ROOT / "scripts" / f).read_text()
    banned = [t for t in ("FILER_PAT", "is_issuer", "FUNDISH", "hongshan|peak xv") if t in src]
    check(not banned, "name-based filter regexes deleted", f"still present: {banned}")

    # 9 — review surface regenerated and consistent
    html = (CB / "review.html").read_text(encoding="utf-8", errors="replace")
    check(f'"{rows[0]["name"]}"' in html or rows[0]["name"] in html,
          "review.html regenerated from current base",
          f"{len(html)//1024} KB")

    width = max(len(l) for _, l, _ in results)
    fails = 0
    for ok, label, detail in results:
        fails += not ok
        print(f"  {'PASS' if ok else 'FAIL'}  {label:<{width}}  {detail}")
    print(f"\n{len(results)-fails}/{len(results)} passed")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
