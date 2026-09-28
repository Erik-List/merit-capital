#!/usr/bin/env python3
"""S2A pass, first four Seed rows (PRO-77). A no carries the full absence test:
graduation_asof, the surfaces (firm, the company's Form D sequence, and the
publisher surfaces from graduation-surfaces.json), the entry past the window."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import cls, GRADLINES

ASOF = "2026-09-28"
L = []
# Form D absences: the entry is inside the layer's coverage (2008 on) and the rescan is more than 24 months later.
for slug, entry, fd_note in [
    ("connection-engine", "2010-06-25", "the company's Form D filings on EDGAR -> 2010-06-25 $1,158,287; 2011-06-24 $1,049,997; no later priced round at twice the entry"),
    ("freestyle-software-inc", "2015-04-28", "the company's Form D filings on EDGAR -> 2015-04-28 $4,975,000 (31 investors); no later filing"),
    ("xios-therapeutics", "2015-12-17", "the company's Form D filings on EDGAR -> 2015-12-17 $6,000,000; 2018-06-28 $1,500,000 offered ($1.0M sold); no later priced round at twice the entry"),
]:
    L.append(cls(slug, grad="not_graduated", grad_src="formd", grad_conf="medium", grad_asof=ASOF,
                 entry_date=entry, surfaces=GRADLINES(slug, formd_note=fd_note)))
# Boxer: no Form D after the seed; the dated search of the named surfaces found no later round before VMware
# bought the company (2015).
L.append(cls("boxer", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=ASOF,
             entry_date="2013-10",
             surfaces=GRADLINES("boxer", formd_note="the company's Form D filings on EDGAR -> 2013-10-15, the seed round only; no later filing",
                                extra=["company: Boxer's own announcements and the acquisition coverage -> the $3M seed (Silicon Hills News, 2013-10-22) is the only round named before VMware bought Boxer (2015)"])))
if __name__ == "__main__":
    jl.write("grad-001", L)
