"""PRO-162 A/B pass, part 1: the public rows' market caps and the stale Attentive mark (COLLECTION.md s7).
Caps read 2026-09-27 from stockanalysis.com (as of 2026-09-25); Lime's is the siblings' Coatue/IVP citation."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, W = jl.cls, jl.W
V = {"valuation_range_source": "web_verified"}
L = [
    cls("lime", rng="1b_plus", usd=1900000000, val_src="web_verified", asof="2026-09-25",
        val_cite="https://stockanalysis.com/stocks/lime/market-cap/", extra=V,
        note="Shared e-bikes and scooters (Neutron Holdings; San Francisco). BCV's listing gives 2019 (Sarah Smith); Wikipedia records "
             "BCV in the $170M Uber-led round of May 2020; both are late rounds, so Growth. IPO on Nasdaq (LIME) in June 2026; market "
             "cap $1.9B as of 2026-09-25 (stockanalysis.com), aligned with Coatue and IVP."),
    cls("acv", rng="1b_plus", usd=1780000000, val_src="web_verified", asof="2026-09-25",
        val_cite="https://stockanalysis.com/stocks/acva/market-cap/", extra=V, clear=["cite_pending"],
        note="Wholesale used-car auction marketplace (Buffalo), IPO March 2021 (NASDAQ: ACVA). BCV's funds are Bain Capital Venture Fund "
             "2019 and BCV 2019-MD Primary (ACV's investors' rights agreement, S-1 exhibit 10.1, "
             "https://www.sec.gov/Archives/edgar/data/1637873/000119312521060598/d34258dex101.htm), so BCV entered after the February "
             "2018 $31M Series C, which Bessemer, Tribeca, SoftBank NY and Armory Square led without BCV: a Growth entry. Market cap "
             "$1.78B as of 2026-09-25 (stockanalysis.com)."),
    cls("rapid7", status="public", rng="below_1b", usd=783200000, val_src="web_verified", asof="2026-09-25",
        val_cite="https://stockanalysis.com/stocks/rpd/market-cap/", stage="Series A", stage_src="model", stage_conf="medium",
        stage_cite=W("Rapid7, Inc."), entry_date="2008-09", flags=["stage_disputes_band"], clear=["cite_pending"],
        note="Security analytics (Boston). 'In September 2008, Rapid7 received its first institutional funding, a $7 million investment "
             "from Bain Capital Ventures' (Wikipedia; Ben Holzman on the board since August 2008, its S-1): the first institutional round "
             "of a bootstrapped company, read as its Series A. The Form D band read a 2010 filing as Seed. IPO July 2015 (NASDAQ: RPD); "
             "market cap $783M as of 2026-09-25 (stockanalysis.com)."),
    cls("attentive", usd=5000000000, val_src="web_verified", asof="2021-06", rng="1b_plus",
        val_cite="https://www.pymnts.com/news/retail/2021/attentive-acquires-conversational-b2c-text-messaging-firm-tone/", extra=V,
        flags=["stale"],
        note="Mobile messaging for commerce (New York). BCV led the Series A (its own post, 2018-03-14), which the filings also give. Mark: "
             "the $470M Series E of March 2021 (Wikipedia), which PYMNTS (June 2021) reports made Attentive 'a $5 billion unicorn'; no "
             "priced round since (an IPO was postponed in 2023), so $5B, stale, aligned with Atomico. Sequoia's $2.7B (2025) is an "
             "uncited secondary estimate, which Rule A does not let band a row."),
]
if __name__ == "__main__":
    jl.write("ab-1", L)
