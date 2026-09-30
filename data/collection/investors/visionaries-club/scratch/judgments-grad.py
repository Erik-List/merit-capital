#!/usr/bin/env python3
"""Graduation decisions for the Seed rows past the 24-month window (PRO-103).
Surfaces come from scripts/graduation-surfaces.py as carried into the queue by
`prepare` (graduation_evidence); the firm and Form D lines are the judge's own
checks, stated as searched. Writes queue/batch-grad.out.jsonl."""
import json
from judge_lib import line, write, HERE

Q = {i["slug"]: i for i in json.loads((HERE / "queue" / "queue.json").read_text())}
ASOF = "2026-09-30"


def surf_lines(slug: str) -> list[str]:
    ge = Q[slug]["graduation_evidence"]
    out = []
    ments = ge.get("mentions", [])
    for name, s in ge["surfaces"].items():
        mine = []
        seen = set()
        for m in ments:
            if m["surface"] == name and m["title"] not in seen:
                seen.add(m["title"])
                mine.append(f"{m['date']} {m['title'][:90]}")
        tail = "; ".join(mine[-2:]) if mine else "no headline naming the company"
        out.append(f"{name}: {s['query']} -> {s['n']} items; {tail}")
    for sib in ge.get("siblings", []) or []:
        out.append(f"sibling:{sib['investor']}: its row for {sib['name']} -> {sib.get('seed_to_a_graduation')} "
                   f"({sib.get('graduation_source')}, as of {sib.get('graduation_asof')})")
    return out


def no(slug, firm, formd=None, note=""):
    surfaces = [f"firm: {firm}"] + ([f"formd: {formd}"] if formd else []) + surf_lines(slug)
    return line(slug, seed_to_a_graduation="not_graduated", graduation_source="absence_check",
                graduation_asof=ASOF, graduation_surfaces=surfaces, graduation_confidence="medium",
                note=note or None)


R = [
    no("courtcorrect",
       "visionaries.vc portfolio 2023-2026 and editorial pages for CourtCorrect -> the Nov 2021 seed only",
       note="No later round found in the surfaces run 2026-09-30 (nor on 20VC's row, not_graduated 2026-09-28); still operating"),
    no("h-company",
       "visionaries.vc portfolio 2024-2026 and editorial pages for H Company -> the May 2024 seed only",
       note="No later round found (French press through Sept 2026 covers product launches, the founders' departures and a Nvidia partnership, no raise); Accel and Creandum read the same"),
    no("qonversion",
       "visionaries.vc portfolio 2023-2026 for Qonversion -> the Dec 2021 seed only",
       "EDGAR company search 'Qonversion' (Form D) -> no filer",
       note="No later round found in the surfaces run 2026-09-30"),
    no("secjur",
       "visionaries.vc portfolio 2023-2026 for Secjur -> the Dec 2022 seed; a Nov 2024 round with no amount or round name (research note) cannot graduate the row",
       note="No named later round found; Handelsblatt's Dec 2022 piece (athlete investors Mario Götze and Nico Rosberg) covers the seed itself"),
    no("cosmic-aerospace",
       "tomorrow.vc (2024-2026) and its Medium posts for Cosmic Aerospace -> the Feb 2024 seed only",
       "EDGAR company search 'Cosmic Aerospace' (Form D) -> no filer",
       note="No later round found; every 2024 headline is the $4.5M seed"),
    no("tactic",
       "visionaries.vc portfolio 2023 for Tactic -> the March 2022 seed; removed from the firm's list after 2023",
       note="No later round found; the surfaces are noisy on a common word (the 2022-05 'Tactic' seed and the 2023 TaxBit deal are the US crypto-accounting company on Lux's row, ruled distinct), and the UK entity's Dec 2022 share allotment names no round"),
    line("sirenopt", seed_to_a_graduation="graduated", graduation_source="web_verified",
         graduation_citation="https://www.sec.gov/Archives/edgar/data/2029046/000202904626000004/primary_doc.xml",
         graduation_confidence="medium",
         note="Graduated on the unnamed-round test: SirenOpt Inc.'s Form D of 2026-09-18 (first sale 2026-09-10) reports $19,428,895 sold of a $32.4M offering, 2.0x the $9,642,402 its seed Form D reported (0002029046-24-000002, first sale 2024-06-28) and above $5M (COLLECTION.md s6); the Oct 2025 $6.5M round was below the test"),
]
write("batch-grad.out.jsonl", R)
