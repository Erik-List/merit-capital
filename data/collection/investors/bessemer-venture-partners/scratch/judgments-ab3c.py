"""A/B pass, public rows (ab3), part c: rows 41 to 60 of queue/ab-public.json, priced on 2026-10-06."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / "scratchpad" / "ab3"))
import judge_lib as jl
from ab3common import P, fig, ASOF

L = []
L.append(P("verisign", "NASDAQ: VRSN",
           ", re-read from the figure of 2026-10-01; the same band as the Kleiner Perkins row."))
L.append(P("weave", "NYSE: WEAV",
           ", replacing the June 2025 float; Francisco Partners signed a definitive agreement in August 2026 to buy "
           "the company for $7.40 a share in cash, about $650M of equity, not closed on 2026-10-06 (StockAnalysis "
           "news feed), so the row stays public until the closing and reads acquired from then."))
L.append(P("wix", "NASDAQ: WIX",
           ", re-read from the figure of 2026-10-01; the same band as the Benchmark and Insight rows."))
L.append(P("xanadu", "NASDAQ: XNDU",
           ", re-read from the figure of 2026-10-01; the same band as the Tiger Global row."))
L.append(P("yelp", "NYSE: YELP",
           ", with companiesmarketcap.com reading $0.98B the same week; it replaces the June 2025 float of $1.42B and "
           "sits within 5% of the $1B band edge, below it, so the band drops to below_1b, and the Benchmark row "
           "(1b_plus on a June 2025 float) should follow."))
L.append(P("american-superconductor", "NASDAQ: AMSC",
           ", re-read from the figure of 2026-10-01; the same band as the Kleiner Perkins row."))
L.append(jl.cls("clean-max-energy-solutions",
                note=f"A/B {ASOF}: the cap of 2026-10-06 was re-read and is unchanged; a second search again showed "
                     "Venture Intelligence listing Bessemer among the company's investors from May 2011 (its page did "
                     "not load), so the identification with the listed Clean Max Enviro Energy Solutions stands."))
L.append(jl.verdict(
    "cogent-communications", "not_member",
    "Not a Bessemer position: the row is the buyer of a portfolio company's assets (the sale-consideration class, "
    "Erik 2026-09-22; decisions.md R6 and D5). The firm's list carried PSINet from 2000 to January 2019 (investment "
    "1993, exit 1995), and its February 2019 list names Cogent Communications in PSINet's place, with no investment "
    "year and no partner. PSINet filed for Chapter 11 on 2001-06-01 and Cogent, founded in 1999, bought most of its "
    "United States assets in April 2002 (Wikipedia, PSINet), seven years after the firm's exit. No Bessemer round in "
    "Cogent is on record and the EDGAR full-text sweep finds no Cogent filing naming a Bessemer fund. The Bessemer "
    "position is the row psinet.",
    ec="web", conf="medium", cite=jl.W("PSINet")))
L.append(P("dick-s-sporting-goods", "NYSE: DKS", ", replacing the August 2025 float; the same band."))
L.append(P("fold", "NASDAQ: FLD (Fold Holdings)", ", replacing the June 2025 float; still below $1B."))
L.append(P("gartner-group", "NYSE: IT (Gartner)",
           ", replacing the June 2025 float of $30.3B; still in the 10b_plus band."))
L.append(P("il-fs-transportation-networks", "BSE: 533177",
           "; still listed while the IL&FS group resolution runs, and the row now carries the figure."))
L.append(P("ionis-pharmaceuticals", "NASDAQ: IONS",
           ", replacing the June 2025 float; the same band as the Sutter Hill row."))
L.append(P("onmobile", "NSE: ONMOBILE (OnMobile Global)", "; the row now carries the figure."))
L.append(P("orient-green-power", "NSE: GREENPOWER", "; the row now carries the figure."))
L.append(P("parametric-technology", "NASDAQ: PTC",
           ", replacing the March 2025 float; Schneider Electric agreed on about 2026-10-05 to buy PTC for $205 a "
           "share in cash (StockAnalysis news feed), not closed, so the row stays public until the closing and reads "
           "acquired from then."))
L.append(jl.cls("proteon-therapeutics", status="acquired", rng="below_1b", city="Waltham", city_src="web_verified",
                flags=("model_disputes_source",),
                note=f"A/B {ASOF} (duties 4 and 8): after its lead drug missed its phase 3 endpoint, Proteon agreed on "
                     "2019-09-23 to combine with ArTara Therapeutics in a reverse merger (GlobeNewswire: "
                     f"{jl.NEWS('proteon-therapeutics', 'Agree to Combine')}; Wikipedia: "
                     f"{jl.W('Proteon Therapeutics')}); the registrant is now Protara Therapeutics (NASDAQ: TARA, "
                     f"market cap {fig('proteon-therapeutics')}, StockAnalysis), a different business, so the row "
                     "reads acquired (reverse merger with ArTara, agreed 2019), the prefilled float, the successor's, "
                     "is dropped, and the city returns to Proteon's own Waltham."))
L.append(P("shriram-epc", "NSE: SEPC (SEPC Limited)", "; the figure of the status note is now on the row."))
L.append(P("sonus-networks", "NASDAQ: RBBN (Ribbon Communications)", ", re-read from the figure of 2026-10-01."))
L.append(P("trinet", "NYSE: TNET (TriNet Group)", ", replacing the June 2025 float; the same band."))

assert len({x["slug"] for x in L}) == len(L) == 20
if __name__ == "__main__":
    jl.write("ab3c", L, record="--dry" not in sys.argv)
    if "--dry" in sys.argv:
        for x in L:
            print(x["slug"], "|", x.get("verdict"), x.get("status"), x.get("valuation_range"), x.get("valuation_usd"), "|", x.get("note") or x.get("basis"))
