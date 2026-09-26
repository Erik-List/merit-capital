"""PRO-79 A/B pass (COLLECTION.md 7) on the visible slice ($1B+ or public),
2026-09-26. Pass A: every value has its confirming citation (market caps
re-read today). Pass B: scratch/ab-sweep.py read the press after each value's
date for a newer round, sale, down round or move; the momentum slice (recent
below-$1B rows, Erik 2026-09-04) was checked the same way. What changed:"""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, rnd = jl.cls, jl.rnd
SA = "https://stockanalysis.com/stocks/{}/market-cap/"
DAY = "2026-09-25"

L = []
L.append(cls("attentive", rng="1b_plus", usd=5000000000, val_src="web_verified", asof="2021-06",
             val_cite="https://www.pymnts.com/news/retail/2021/attentive-acquires-conversational-b2c-text-messaging-firm-tone/",
             val_conf="medium", flags=["stale"],
             note="A/B: the Sep 2020 $2.2B was superseded - 'In March 2021, the company raised an additional $470 million in a Series E funding round' (Wikipedia) and PYMNTS (Jun 2021) calls Attentive 'a $5 billion unicorn' fresh off that raise; no priced round since (an IPO was postponed in 2023) -> $5B, stale",
             rounds=[rnd("2021-03", "Series E", 470000000, None, None, "https://www.pymnts.com/news/retail/2021/attentive-acquires-conversational-b2c-text-messaging-firm-tone/")]))
L.append(cls("compass", rng="1b_plus", usd=7110000000, val_src="web_verified", asof=DAY,
             val_cite=SA.format("comp"), val_conf="high",
             note="A/B: market cap $7.11B on 2026-09-25 (StockAnalysis), re-read"))
L.append(cls("klarna", rng="1b_plus", usd=4850000000, val_src="web_verified", asof=DAY,
             val_cite=SA.format("klar"), val_conf="high",
             note="A/B: market cap $4.85B on 2026-09-25 (StockAnalysis), down from ~$7.5B in August"))
L.append(cls("hinge-health", rng="1b_plus", usd=7710000000, val_src="web_verified", asof=DAY,
             val_cite=SA.format("hnge"), val_conf="high",
             note="A/B: market cap $7.71B on 2026-09-25 (StockAnalysis), re-read"))
L.append(cls("lime", rng="1b_plus", usd=1900000000, val_src="web_verified", asof=DAY,
             val_cite=SA.format("lime"), val_conf="high", clear=["cite_pending"],
             note="A/B: market cap $1.9B on 2026-09-25 (StockAnalysis, Neutron Holdings, LIME) - the cited market cap the row owed"))
L.append(cls("lendinvest", rng="below_1b", usd=53579324, val_src="web_verified", asof=DAY,
             val_cite="https://stockanalysis.com/quote/lon/LINV/market-cap/", val_conf="high",
             note="A/B: market cap GBP 40.43M on 2026-09-25 (StockAnalysis; $53.6M at the ECB rate of that day)"))
L.append(cls("the-exploration-company", rng="1b_plus", usd=2000000000, val_src="web_verified", asof="2026-07-27",
             val_cite="https://thenextweb.com/news/exploration-company-300m-raise-spacex-rival", val_conf="low",
             note="A/B momentum check: the FT reported the round in talks at a $2B valuation (The Next Web, Jul 2026; MarketScreener: about EUR 1.75B), and it closed in Sep 2026 larger, at $450M, with no price disclosed - the only figure on record for this priced event, both readings above $1B, hence low confidence"))
L.append(cls("bird", note="A/B: Bird announced in Feb 2025 that it would move most operations out of the Netherlands (Reuters), but the Nov 2025 and May 2026 coverage still calls it Amsterdam-based; its Sep 2026 $450M raise is debt (Bloomberg), not a priced equity round - the 2021 $3.8B mark stands, stale"))
L.append(cls("starkware", note="A/B: no priced round since the May 2022 $8B; the Apr 2026 layoffs and restructuring are not collapse evidence under COLLECTION.md 6"))
L.append(cls("deepl", note="A/B: no priced round since May 2024; IPO preparation was reported in Oct 2025 and a 25% staff cut in May 2026 - neither re-prices the row"))
L.append(cls("upside-foods", note="A/B: no priced round since Apr 2022; layoffs 2024-2025 and a Jun 2026 bid for a shuttered plant do not re-price the row"))

if __name__ == "__main__":
    jl.write("ab-001", L)
