#!/usr/bin/env python3
"""Lead's fixes from the city check (duty 9 on the blind check's city class; PRO-75, 2026-09-29): operating rows with
a solid SEC match compared with their current EDGAR business address. Most differences are an officer's or a
registered agent's address and change nothing; two are current filings of the company itself."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl  # noqa: E402

jl.write("fixes-11", [
    jl.cls("ethos", city="Austin", city_src="formd_address",
           note="City check 2026-09-29: the listed company's own SEC filings of September 2026 give its business "
                "address in Austin, Texas (Ethos Technologies Inc., CIK 1788451), as the Accel and General Catalyst "
                "rows read."),
    jl.cls("strella-biotechnology", city="Philadelphia", city_src="formd_address",
           note="City check 2026-09-29: the company's own Form D of August 2026 gives Philadelphia (Strella "
                "Biotechnology, Inc., CIK 1810011).")])
