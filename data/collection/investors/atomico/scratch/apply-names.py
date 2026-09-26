#!/usr/bin/env python3
"""Published names under COLLECTION.md §8 (Erik 2026-09-24), applied at the source.

The firm renders some brands in capitals or lower case ("EVRYTHNG", "REKKI",
"accuRx", "tem.") and the 2008-2012 listings carry their own stylings
("DECA", "Heysan!", "wunderLOOP", "CMUNE"). §8: a word read letter by letter
keeps its capitals, every other word takes normal case, a mixed-case spelling
the company uses stays, legal suffixes go. The build has no display-name
override for a single row, so the map is applied in the parsed sources (the
First Round precedent for archive filename variants), keeping the firm's own
rendering as `name_site` so the evidence is not lost.

Idempotent. Run before site-portfolio.py and build-company-base.py.
"""
from __future__ import annotations

import glob
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

P = Paths("atomico")
NAMES = {
    "EVRYTHNG": "Evrythng", "DECA": "Deca", "REKKI": "Rekki", "DRIVETRIBE": "Drivetribe",
    "CMUNE": "Cmune", "Heysan!": "Heysan", "wunderLOOP": "Wunderloop", "tem.": "Tem",
    "accuRx": "Accurx", "AccuRx": "Accurx", "arculus": "Arculus", "fon": "Fon", "FON": "Fon",
    "scoutbee": "Scoutbee", "deeploi": "Deeploi", "QuitGenius": "Quit Genius",
    "ZocDoc": "Zocdoc", "6wunderkinder": "6Wunderkinder", "mydeco": "Mydeco",
    "Pedidos Ya": "PedidosYa", "PEDIDOS YA": "PedidosYa", "rdio": "Rdio",
    "ChemistDirect": "Chemist Direct", "Callosum ": "Callosum", "Openfx": "OpenFX",
    "Pactum Ai": "Pactum AI",
}


def fix(rows: list[dict]) -> int:
    n = 0
    for r in rows:
        nm = r.get("name")
        if nm and nm.strip() in NAMES and NAMES[nm.strip()] != nm:
            r.setdefault("name_site", nm)
            r["name"] = NAMES[nm.strip()]
            n += 1
    return n


def main():
    total = 0
    for f in (P.site / "cms-partners.json", P.site / "jobboard-companies.json"):
        d = json.loads(f.read_text())
        n = fix(d["rows"])
        write_atomic(f, json.dumps(d, indent=1, ensure_ascii=False) + "\n")
        print(f"{f.name}: {n} names")
        total += n
    for f in sorted(glob.glob(str(P.wayback / "parsed" / "*.json"))):
        rows = json.loads(Path(f).read_text())
        n = fix(rows)
        if n:
            write_atomic(Path(f), json.dumps(rows, indent=1) + "\n")
            print(f"{Path(f).name}: {n} names")
        total += n
    print(f"published-name rule applied to {total} source rows")


if __name__ == "__main__":
    main()
