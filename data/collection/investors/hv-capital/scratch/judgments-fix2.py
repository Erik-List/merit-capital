"""Impossible Cloud's graduation (PRO-104)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write, surfaces_lines, ASOF  # noqa: E402

F = ("the March 2023 EUR 7M seed only for Impossible Cloud GmbH; the later raises (EUR 28.8M July 2025, NGP Capital "
     "at $470M; 'Impossible Cloud Raises $34 Million', games.gg 2026-06-10, HV named) are Impossible Cloud Network's, "
     "the separate Swiss token-network entity, not this company's")
L = [cls("impossible-cloud", grad="not_graduated", grad_src="absence_check", grad_asof=ASOF, entry_date="2023-03",
         surfaces=surfaces_lines("impossible-cloud", F), flags=["ruling_open"],
         note="Enterprise cloud object storage, Hamburg. 'HV Capital and 1kx Leading a EUR 7M Seed Round' (Business Wire, "
              "2023-03-01; the firm's own entry date 2022-08-08 is the close). No later round of Impossible Cloud GmbH was "
              "found. The founders' Swiss sister entity, Impossible Cloud Network (ICN), raised EUR 28.8M in July 2025 "
              "(NGP Capital, $470M post-money) with HV participating; whether ICN's rounds count as this company's "
              "graduation is open for Erik (report.md). Read as separate companies, the row did not graduate.")]
write("fix-002", L)
