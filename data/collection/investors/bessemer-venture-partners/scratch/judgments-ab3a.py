"""A/B pass, public rows (ab3), part a: rows 1 to 20 of queue/ab-public.json, priced on 2026-10-06."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / "scratchpad" / "ab3"))
import judge_lib as jl
from ab3common import P, fig, CAPS, ASOF

L = []
L.append(P("acv-auctions", "NYSE: ACVA",
           ", replacing the June 2025 float; Copart agreed in September 2026 to buy the company for $10.50 a share in "
           "cash and its tender offer, since extended, had not closed (StockAnalysis news feed), so the row stays "
           "public until the closing and reads acquired from then."))
L.append(P("allscripts", "Veradigm, the renamed Allscripts, was suspended from Nasdaq on 2024-02-29 (Wikipedia) and "
           "is quoted over the counter as MDRX",
           "; read public on that quote, as the sibling books read companies quoted over the counter, and below $1B "
           "either way."))
L.append(P("box", "NYSE: BOX", ", replacing the July 2025 float; the same band as the four sibling books."))
L.append(P("bright-horizons-family-solutions", "NYSE: BFAM", ", re-read from the figure of 2026-10-01."))
L.append(P("bumble", "NASDAQ: BMBL",
           ", replacing the June 2025 float; below $1B as in the Accel and Headline books."))
L.append(P("ciena", "NYSE: CIEN",
           ", re-read from the figure of 2026-10-01; the Lightspeed row holds the same band and the wrong country "
           "(CA for US)."))
L.append(P("criteo", "NASDAQ: CRTO", ", re-read from the figure of 2026-10-01 and still below $1B."))
L.append(P("disco", "NYSE: LAW (CS Disco)", ", re-read from the figure of 2026-10-01."))
L.append(P("docusign", "NASDAQ: DOCU", ", re-read from the figure of 2026-10-01; the same band as the six sibling books."))
L.append(P("enjoei", "B3: ENJU3", "; the row now carries the figure."))
L.append(P("fiverr", "NYSE: FVRR", ", re-read from the figure of 2026-10-01; below $1B as in the Accel book."))
L.append(jl.cls("flex-pharma-inc", status="acquired", rng="below_1b", flags=("model_disputes_source",),
                note=f"A/B {ASOF} (duties 4 and 8): Flex Pharma's shareholders approved a reverse merger with Salarius "
                     "Pharmaceuticals in July 2019 after its drug failed (The Business Journals, 2019-07-15: "
                     f"{jl.NEWS('flex-pharma-inc', 'reverse-merger')}); the registrant became Salarius and, in January "
                     f"2026, Decoy Therapeutics (NASDAQ: DCOY, market cap {fig('flex-pharma-inc')}, StockAnalysis), a "
                     "different business, so the row reads acquired (reverse merger with Salarius, 2019) and the "
                     "prefilled float, the successor shell's, is dropped."))
L.append(P("fractyl-health", "NASDAQ: GUTS",
           ", replacing the June 2025 float; below $1B as in the General Catalyst and GV books."))
L.append(P("hinge-health", "NYSE: HNGE",
           ", replacing the pre-filled float of $1.5B; the same band as the five sibling books."))
L.append(P("homefirst", "NSE: HOMEFIRST", ", re-read from the figure of 2026-10-01."))
L.append(P("indian-energy-exchange", "NSE: IEX",
           ", within 5% of the $1B band edge and below it; the Lightspeed row ($1.11B of September 2026, 1b_plus) "
           "should read below_1b on this figure."))
L.append(P("kymera-therapeutics", "NASDAQ: KYMR", ", replacing the pre-filled float; the same band."))
L.append(P("life360", "NASDAQ: LIF (also ASX: 360)", ", replacing the June 2025 float; the same band."))
L.append(P("matrimony-com", "NSE: MATRIMONY", ", re-read from the figure of 2026-10-01."))
L.append(P("motilal-oswal", "NSE: MOTILALOFS", ", re-read from the figure of 2026-10-01."))

assert len({x["slug"] for x in L}) == len(L) == 20
if __name__ == "__main__":
    jl.write("ab3a", L, record="--dry" not in sys.argv)
    if "--dry" in sys.argv:
        for x in L:
            print(x["slug"], "|", x.get("status"), x.get("valuation_range"), x.get("valuation_usd"), "|", x["note"])
