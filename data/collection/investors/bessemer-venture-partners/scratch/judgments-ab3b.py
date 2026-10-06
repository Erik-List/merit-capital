"""A/B pass, public rows (ab3), part b: rows 21 to 40 of queue/ab-public.json, priced on 2026-10-06."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / "scratchpad" / "ab3"))
import judge_lib as jl
from ab3common import P

L = []
L.append(P("ncino", "NASDAQ: NCNO", ", re-read from the figure of 2026-09-25; the same band as the Insight row."))
L.append(P("nephroplus", "NSE: NEPHROPLUS (Nephrocare Health Services)", ", re-read from the figure of 2026-10-01."))
L.append(P("pagerduty", "NYSE: PD",
           ", replacing the July 2025 float; the same band as the a16z, Accel and Y Combinator rows."))
L.append(P("pinterest", "NYSE: PINS",
           ", replacing the June 2025 float; the same band as the a16z and Kleiner Perkins rows."))
L.append(P("procore", "NYSE: PCOR",
           ", replacing the June 2025 float; the same band as the ICONIQ and Tiger Global rows."))
L.append(P("qualys", "NASDAQ: QLYS", ", replacing the June 2025 float; the same band."))
L.append(P("rigetti-computing", "NASDAQ: RGTI",
           ", replacing the June 2025 float; the same band as the Lux, Sutter Hill and Y Combinator rows."))
L.append(P("rocket-lab", "NASDAQ: RKLB",
           ", replacing the June 2025 float; the Khosla row still carries that float ($14.9B), the same band."))
L.append(P("servicetitan", "NASDAQ: TTAN", ", replacing the July 2025 float; the same band as the sibling books."))
L.append(P("shopify", "NASDAQ: SHOP",
           ", replacing the June 2025 float; the same band as the Felicis and Insight rows."))
L.append(P("spire", "NYSE: SPIR (Spire Global)", ", replacing the June 2025 float; still below $1B."))
L.append(P("stubhub", "NYSE: STUB (StubHub Holdings)", ", re-read from the figure of 2026-10-01."))
L.append(P("swiggy", "NSE: SWIGGY",
           ", re-read from the figure of 2026-10-01; the same band as the Accel and Coatue rows."))
L.append(P("tigo-energy", "NASDAQ: TYGO", ", re-read from the figure of 2026-10-01."))
L.append(P("toast", "NYSE: TOST",
           ", replacing the June 2025 float; the same band as the GV, TCV and Tiger Global rows."))
L.append(P("tscan-therapeutics", "NASDAQ: TCRX",
           ", replacing the June 2025 float; below $1B as in the GV book."))
L.append(P("twilio", "NYSE: TWLO",
           ", replacing the June 2025 float; the same band as the sibling books."))
L.append(P("urban-company", "NSE: URBANCO",
           ", re-read from the figure of 2026-10-01; the Accel row (private, below_1b) should read public and 1b_plus "
           "on this listing, as the Tiger Global row does."))
L.append(P("velo3d", "NASDAQ: VELO",
           ", replacing the June 2025 float; below $1B as in the Khosla book."))
L.append(P("verastem", "NASDAQ: VSTM", ", replacing the June 2025 float; still below $1B."))

assert len({x["slug"] for x in L}) == len(L) == 20
if __name__ == "__main__":
    jl.write("ab3b", L, record="--dry" not in sys.argv)
    if "--dry" in sys.argv:
        for x in L:
            print(x["slug"], "|", x.get("status"), x.get("valuation_range"), x.get("valuation_usd"), "|", x["note"])
