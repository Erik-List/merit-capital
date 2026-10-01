"""Stale sibling rows aligned from the Speedinvest run (PRO-84) in its own ingest (COLLECTION.md s9; Erik 2026-09-29).
Adapted from Project A's kit (PRO-102). One classification line per stale row, written to scratch/align/<book>.jsonl
and recorded ONCE into that book with `run.py record --investor <book>` (the record note-join bug). Each line cites the
underlying evidence, never Speedinvest's own site.

The pairs are the `accepted` rulings of companies/cross-rulings.json. Aligned here:
- accel:luko read `private`; Allianz Direct bought the business out of receivership in January 2024.
- seedcamp:fleksy, fraugster, stowga read `unknown`; wefox read 1b_plus on the July 2022 Series D.
Not aligned, and reported (report.md section 15):
- y-combinator (diligent, june): the book fails its own gate before any write (the readback against its committed
  base shows one row missing and one extra, both named Metadata; drift this run did not make).
- a16z:june: the row is a bare name on a16z's investment list and nothing in a16z's book says which June it is
  (june.so, or the June oven that Weber bought, for which `acquired` would be right). Left for Erik.

Usage: python3 align.py [--dry] [book ...]
"""
import json, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
WHO = "agent-align-pro84"
TAG = "Aligned 2026-09-30 from the Speedinvest run (PRO-84, rule 10)"

LINES = {
    "accel": [{
        "slug": "luko", "who": WHO, "status": "acquired",
        "status_citation": "https://techcrunch.com/2024/01/25/luko-insurtech-allianz-direct/",
        "note": f"{TAG}: Luko went into receivership in late 2023 after Admiral withdrew its offer, and Allianz Direct "
                "bought the business for EUR 4.3M in January 2024 (TechCrunch 2024-01-25): insolvency followed by a "
                "sale of the business reads acquired, as in the EQT Ventures and Speedinvest books.",
    }],
    "seedcamp": [
        {"slug": "fleksy", "who": WHO, "status": "defunct",
         "status_citation": "https://find-and-update.company-information.service.gov.uk/company/09691012/insolvency",
         "note": f"{TAG}: ThingThing Ltd (UK 09691012) has been in members' voluntary liquidation since 2025-11-24 "
                 "(Companies House); the apps were delisted and no sale of the business was found: defunct."},
        {"slug": "fraugster", "who": WHO, "status": "defunct",
         "status_citation": "https://www.northdata.com/Fraugster%20Services%20GmbH,%20Berlin/Amtsgericht%20Charlottenburg%20(Berlin)%20HRB%20195228%20B",
         "note": f"{TAG}: insolvency proceedings over Fraugster Services GmbH opened at the Charlottenburg court on "
                 "2023-01-17 and the company has been in liquidation since March 2023 (Berlin register through North "
                 "Data); no sale found: defunct."},
        {"slug": "stowga", "who": WHO, "status": "acquired",
         "status_citation": "https://x.com/TeamStowga/status/1465710153282428962",
         "note": f"{TAG}: bought by Value Chain Lab, announced by the company itself on 2021-11-30 (its own X post); "
                 "the legal entity was struck off in August 2022: acquired."},
        {"slug": "wefox", "who": WHO, "valuation_range": "below_1b", "valuation_usd": None,
         "valuation_asof": "2024-06", "valuation_range_source": "web_verified", "valuation_source": "web_verified",
         "valuation_citation": "https://www.insurancejournal.com/news/international/2024/06/14/779529.htm",
         "note": f"{TAG}: the $4.5B Series D mark of July 2022 yields to documented collapse. In June 2024 the Series D "
                 "lead backed a sale at an enterprise value of at most EUR 550M (Insurance Journal, 2024-06-14), and "
                 "only unpriced rescue financing followed: below $1B."},
    ],
}

if __name__ == "__main__":
    dry = "--dry" in sys.argv
    only = [a for a in sys.argv[1:] if not a.startswith("--")]
    for inv, lines in sorted(LINES.items()):
        if only and inv not in only:
            continue
        p = HERE / f"{inv}.jsonl"
        p.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in lines))
        print(f"== {inv}: {len(lines)} line(s) -> {p.name}")
        if dry:
            continue
        r = subprocess.run([sys.executable, "scripts/run.py", "record", "--investor", inv, str(p)], cwd=ROOT,
                           capture_output=True, text=True)
        print((r.stdout + r.stderr).strip()[-800:])
        if r.returncode:
            sys.exit(f"record failed for {inv}; stopping")
