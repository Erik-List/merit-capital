"""PRO-161 grind, batch-005 (stone-ridge .. zestmoney; the Form D-only rows of this batch were ruled in
judgments-members-1.py, ibod-company-inc folds into root at the rebuild and forusall-inc waits for the 2019-2020
archive). Evidence: show.py, Google News (nq.py, decoded), WebFetch of the press items cited, one WebSearch
(Synaptic)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd, SITE, ARCH, W, NEWS, SPV = jl.cls, jl.verdict, jl.rnd, jl.SITE, jl.ARCH, jl.W, jl.NEWS, jl.SPV
L = []

PRN_TOP = "https://www.prnewswire.com/news-releases/the-open-platform-is-first-unicorn-in-web3-ecosystem-in-telegram-at-1bn-valuation-302497955.html"
FORTUNE_TEMPO = "https://fortune.com/crypto/2025/10/17/stripe-paradigm-tempo-series-a-5-billion-thrive-capital-greenoaks-joshua-kushner/"
COVERAGER_VIVID = "https://coverager.com/fintech-startup-vivid-money-raises-17-6m/"
ENTRACKR_ZEST = "https://entrackr.com/2019/04/zestmoney-20-mn-funding-quona-capital/"
INC42_ZEST = "https://inc42.com/features/what-broke-zestmoney-how-indias-bnpl-poster-child-lost-its-zest/"
PRN_SYNAPTIC = "https://www.prnewswire.com/in/news-releases/synaptic-raises-20mn-in-series-b-funding-round-from-valor-equity-partners-816477167.html"
IAPD_YOSHI = "https://adviserinfo.sec.gov/firm/summary/339574"

L.append(cls("stone-ridge", status="private", rng="below_1b", country="US", city="New York", focus="Fintech & Payments",
    stage="undetermined",
    note="Stone Ridge Asset Management (New York), the alternative-investment manager Ross Stevens founded in 2012; the firm lists it "
         "with its founder. No source names the round or the date Ribbit entered, and the holding company has no priced event "
         "(Rule A): no round at or above $1B found (news sweep 2026-09-28). Its bitcoin arm NYDIG is a separate row."))
L.append(cls("stripe", status="private", rng="100b_plus", usd=159000000000, val_src="web_verified", val_cite=W("Stripe, Inc."),
    asof="2026-02", extra={"valuation_range_source": "web_verified"}, city="South San Francisco", focus="Fintech & Payments",
    stage="Growth", stage_src="model", stage_conf="medium", stage_cite=SPV("ST-IC"), entry_date="2021",
    flags=["model_disputes_source"],
    note="Payments infrastructure, dual-headquartered in South San Francisco and Dublin (Wikipedia). The pre-filled 'acquired' is a "
         "wrong join: Stripe is private, valued at $159B in its February 2026 tender offer (Wikipedia). Ribbit's first dated Stripe "
         "vehicle is ST-IC Ribbit Opportunity V (Form D, 2021 Q2, $15.1M sold); the ADV adds ST-H (the Series H of March 2021, $600M "
         "at $95B) and ST-TO (a tender). Stripe was past its Series G by then, so the entry is Growth whichever 2021 round it was; the "
         "firm lists Stripe only from 2025."))
L.append(cls("synaptic", status="private", rng="below_1b", country="US", city="San Francisco", focus="SaaS",
    stage="undetermined",
    note="Alternative-data platform for investors, spun out of Vy Capital in 2016 by Anurag Abbott and Rohit Razdan, with offices in "
         "India and the US (the company's Series B release). 'Previously raised $6 million from Ribbit Capital, Felicis Ventures, and Vy "
         "Capital Management' across its seed and Series A, so Ribbit's round cannot be told apart; $20M Series B led by Valor Equity "
         "Partners (2022-05-31). No round at or above $1B found (news sweep 2026-09-28).",
    rounds=[rnd(None, "Seed and Series A", 6000000, None, True, PRN_SYNAPTIC, "company"),
            rnd("2022-05-31", "Series B", 20000000, "Valor Equity Partners", None, PRN_SYNAPTIC, "company")]))
L.append(cls("tempo", status="private", rng="1b_plus", usd=5000000000, val_src="web_verified", val_cite=FORTUNE_TEMPO,
    asof="2025-10-17", extra={"valuation_range_source": "web_verified"}, city="San Francisco", focus="Crypto & Web3",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=FORTUNE_TEMPO, entry_date="2025-10",
    flags=["model_disputes_source"],
    note="Payments blockchain incubated by Stripe and Paradigm (CEO Matt Huang). The pre-filled 'acquired' joined a namesake bought by "
         "Daimler-Benz. $500M Series A at a $5B valuation led by Greenoaks and Thrive Capital; 'Sequoia, Ribbit Capital, and Ron Conway's "
         "SV Angel also participated' (Fortune, 2025-10-17). City aligned with the Thrive row.",
    rounds=[rnd("2025-10-17", "Series A", 500000000, "Greenoaks and Thrive Capital", True, FORTUNE_TEMPO, "press")]))
L.append(cls("top-group", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified", val_cite=PRN_TOP,
    asof="2025-07-03", extra={"valuation_range_source": "web_verified"}, country="AE", country_src="web_verified",
    country_cite=PRN_TOP, city="Dubai", focus="Crypto & Web3",
    stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=PRN_TOP, entry_date="2025-07",
    note="The Open Platform (TOP), the Dubai-based builder of Telegram's crypto wallet, founded by Andrew Rogozov. 'The equity round was "
         "led by Ribbit Capital ... with Pantera Capital also participating': a $28.5M Series A extension at a $1B valuation, the "
         "first unicorn in the TON ecosystem (the company's release, 2025-07-03). The mark sits exactly on the $1B band edge. Earlier "
         "seed money came in before, with no Ribbit role named, so the entry is read at the round Ribbit led (medium).",
    rounds=[rnd("2025-07-03", "Series A extension", 28500000, "Ribbit Capital", True, PRN_TOP, "company")]))
L.append(cls("vivid-money", status="private", rng="below_1b", country="DE", country_src="web_verified", country_cite=COVERAGER_VIVID,
    city="Berlin", focus="Fintech & Payments",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=COVERAGER_VIVID, entry_date="2020-11",
    flags=["model_disputes_source"],
    note="Berlin-based banking and investing app (the firm's own label: Germany; the pre-filled NL is its Dutch-registered holding). "
         "'Vivid Money has raised a $17.6 million Series A funding round led by Ribbit Capital' (Coverager, November 2020). Later "
         "rounds: EUR 60M (April 2021), $114M at an $886M valuation (February 2022), a EUR 100M Series C (2025, valuation not "
         "disclosed); no round at or above $1B found (news sweep 2026-09-28).",
    rounds=[rnd("2020-11", "Series A", 17600000, "Ribbit Capital", True, COVERAGER_VIVID, "press"),
            rnd("2022-02", None, 114000000, None, None, NEWS("vivid-money", "raises $114m at $886m"), "press")]))
L.append(cls("yoshi", status="private", rng="below_1b", country="US", country_src="web_verified", country_cite=IAPD_YOSHI,
    city="San Francisco", city_src="web_verified", focus="Fintech & Payments", stage="undetermined",
    flags=["model_disputes_source"],
    note="Automated personal-finance manager (yoshi.ai) run by Yoshi Advisory, an SEC-registered adviser (CRD 339574, Ferry Building, "
         "San Francisco); founder Ross Lipson. The pre-filled 'Monaco' joined another Yoshi. No round is public; no round at or above "
         "$1B found (news sweep 2026-09-28)."))
L.append(cls("zestmoney", status="defunct", rng="below_1b", country="IN", country_src="web_verified", country_cite=ENTRACKR_ZEST,
    city="Bangalore", focus="Fintech & Payments", stage="undetermined",
    note="Bengaluru-based buy-now-pay-later lender. Ribbit is named an existing backer in the $20M Series B led by Quona Capital "
         "(Entrackr, April 2019) and held 16.6% by 2021; the firm listed ZestMoney by January 2017 (archived Our Bets page), before "
         "the $6.5M Series A PayU led (announced February 2017), so Ribbit's round is not named. The company shut down in December "
         "2023 (" + NEWS("zestmoney", "ZestMoney to shut operations") + ").",
    rounds=[rnd("2017-02", "Series A", 6500000, "PayU", None, INC42_ZEST, "press"),
            rnd("2018-08", "Series A extension", 13400000, "Xiaomi", None, ENTRACKR_ZEST, "press"),
            rnd("2019-04", "Series B", 20000000, "Quona Capital", True, ENTRACKR_ZEST, "press")]))
jl.write("batch-005", L)
