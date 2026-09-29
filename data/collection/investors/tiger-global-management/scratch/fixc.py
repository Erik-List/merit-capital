#!/usr/bin/env python3
"""PRO-167 Tiger Global, verify-gap fix c (2026-09-29): valuation band for 15 of the 29 rows in needs-value.json
(avant .. pristyn-care). Each private row takes its last priced round at a stated valuation with a citation
(flag `stale` when the as-of is before 2024-09-29); a row with no priced figure on record reads below_1b with the
check in the note (Rule A). Marks come from pages this pass read (BURL, SRC) or a sibling's cited mark (V).
Run: NQ_TAG=fx python3 fixc.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl  # noqa: E402
from judge_lib import cls  # noqa: E402
from fxlib import SRC, BURL, V, MARK, WV  # noqa: E402

L = []
STALE = ("stale",)

# ---------------------------------------------------------------- Avant
L.append(cls("avant", flags=STALE,
             **MARK(BURL("avant", "Once $659 million", "chicagobusiness"), 2_000_000_000, "2015-09"),
             note="Verify fix 2026-09-29: the $325M Series E of September 2015 was priced 'at a valuation close to $2 "
                  "billion' (Crain's Chicago Business, 2023-07-05), written as $2.0B: 1b_plus, stale. The same article "
                  "reports that the $659M of equity Avant raised is nearly gone; that is balance-sheet erosion, not a "
                  "priced round, tender or sale, so under COLLECTION.md 6 the 2015 mark stands and a collapse reading "
                  "is Erik's. No later equity round found (Bing News, 2026-09-29). The Ribbit row reads below_1b (it "
                  "found no stated figure), so the two books disagree on the band; the Sutter Hill 'Avant!' is "
                  "another company."))

# ---------------------------------------------------------------- Grafana Labs
L.append(cls("grafana-labs", flags=STALE, **MARK(SRC("grafana-sa-2024"), 6_000_000_000, "2024-08-21"),
             note="Verify fix 2026-09-29: the $270M primary and secondary transaction of August 2024 at $6B "
                  "(SiliconANGLE, 2024-08-21) is the last priced round with a stated valuation; stale by 39 days. The "
                  "$9B on the Coatue, Lightspeed and Sequoia rows is a February 2026 report of a round being "
                  "finalized (The Information; SiliconANGLE 'reportedly raising'); no closing was found (Google News "
                  "and Bing News, 2026-09-29), and COLLECTION.md 6 rules out pricing a row off a deal only reported. "
                  "Same band as the siblings."))

# ---------------------------------------------------------------- Mensa Brands
L.append(cls("mensa-brands", flags=STALE, **MARK(SRC("mensa-mc"), 1_000_000_000, "2021-11-16"),
             note="Verify fix 2026-09-29: the $135M Series B 'valued the six-month-old venture at over a billion "
                  "dollars' (Moneycontrol, 2021-11-16), written as $1.0B at the band edge: 1b_plus, stale. Since then "
                  "$40M of debt from EvolutionX (2023), a reverse flip to India (2024) and a rebrand as BRND.ME with "
                  "the sale of MensXP (2025); no priced equity round found (Google News, 2026-09-29)."))

# ---------------------------------------------------------------- Moglix
L.append(cls("moglix", flags=STALE,
             **MARK(BURL("moglix", "Moglix raises $250 million, at $2.6 billion valuation", "thehindubusinessline"),
                    2_600_000_000, "2022-01-27"),
             note="Verify fix 2026-09-29: Tiger and Alpha Wave led the $250M Series F at $2.6B (Business Line, "
                  "2022-01-27), the Accel row's mark; stale. No later priced round found (Bing News, 2026-09-29)."))

# ---------------------------------------------------------------- Moka: no figure on record
L.append(cls("moka", rng="below_1b",
             extra={**WV, "valuation_citation": BURL("moka", "Moka Completes US$100 Million in Series C", "prnewswire")},
             note="Verify fix 2026-09-29: no valuation on record. The $100M Series C of November 2021 led by Tiger (the "
                  "company's PR Newswire release; TechCrunch) states none, and no later priced round is reported "
                  "(Bing News, 2026-09-29, through the May 2026 'Moka AI' launch): below_1b under Rule A."))

# ---------------------------------------------------------------- MoonPay
L.append(cls("moonpay", flags=STALE, **V("moonpay", "coatue"),
             note="Verify fix 2026-09-29: the $555M first round at $3.4B led by Tiger and Coatue (November 2021, CNBC, "
                  "as the Coatue and Thrive rows cite); stale. Reports in December 2025 of an ICE investment at a "
                  "targeted $5B (MSN, ADVFN) found no closing with a stated price (Bing News, 2026-09-29), so the 2021 "
                  "mark stands."))

# ---------------------------------------------------------------- NoBroker
L.append(cls("nobroker", flags=STALE,
             **MARK(BURL("nobroker", "Indian realty platform NoBroker valued at $1 billion after new funding",
                         "hindustantimes"), 1_000_000_000, "2021-11-22"),
             note="Verify fix 2026-09-29: the $210M Series E led by General Atlantic and Tiger valued NoBroker at $1 "
                  "billion (Reuters via Hindustan Times, 2021-11-22), a figure at the $1B band edge: 1b_plus, stale. "
                  "Google joined the Series E in 2023 (Business Today) at no stated new price; no later priced round "
                  "found (Bing News, 2026-09-29)."))

# ---------------------------------------------------------------- NotCo
L.append(cls("notco", flags=STALE,
             **MARK(BURL("notco", "NotCo Announces $235M Series D Round", "streetinsider"), 1_500_000_000, "2021-07-26"),
             note="Verify fix 2026-09-29: the $235M Series D at $1.5B led by Tiger (the company's release via "
                  "StreetInsider, 2021-07-26), the General Catalyst row's figure; stale. The $70M extension of the "
                  "Series D in December 2022 reported no new valuation (Yahoo Finanzas)."))

# ---------------------------------------------------------------- Nuro
L.append(cls("nuro", **MARK(BURL("nuro", "Self-driving vehicle startup Nuro valued at $6 billion", "ca.finance.yahoo"),
                            6_000_000_000, "2025-08-21"),
             note="Verify fix 2026-09-29: the Series E closed at $203M and a $6B valuation with Uber and Nvidia joining "
                  "(Reuters via Yahoo, 2025-08-21); not stale. The Greylock row reads the same figure."))

# ---------------------------------------------------------------- OfBusiness
L.append(cls("ofbusiness", flags=STALE,
             **MARK(BURL("ofbusiness", "Valued at $5 billion, OfBusiness raises", "financialexpress"),
                    5_000_000_000, "2021-12-20"),
             note="Verify fix 2026-09-29: the $325M Series G led by Alpha Wave, Tiger and SoftBank valued OfBusiness at "
                  "about $5B (Financial Express, 2021-12-20); stale. What followed is talks or targets ($8-9B "
                  "secondary talks in 2022, a $6B target in 2023, an IPO at up to $9B in 2024) and an INR 100 crore "
                  "round from Cornerstone (April 2025) with no stated valuation; none is a priced mark (Bing News, "
                  "2026-09-29)."))

# ---------------------------------------------------------------- OpenSea
L.append(cls("opensea", flags=STALE, **V("opensea", "coatue"),
             note="Verify fix 2026-09-29: the last priced primary is the $300M Series C at $13.3B (January 2022, led by "
                  "Paradigm and Coatue; CNBC as the Coatue and Y Combinator rows cite); stale. Coatue marked its stake "
                  "down 90% (Cointelegraph, November 2023) and Tiger 94% (December 2023): fund fair-value marks, not "
                  "a priced round or tender, so the mark stands and a collapse reading is Erik's. No equity round "
                  "since (Bing News, 2026-09-29)."))

# ---------------------------------------------------------------- OutSystems
L.append(cls("outsystems", flags=STALE,
             **MARK(BURL("outsystems", "[Funding] OutSystems Raises $150 Million", "ciol"), 9_500_000_000, "2021-02-17"),
             note="Verify fix 2026-09-29: the $150M round co-led by Abdiel Capital and Tiger at $9.5B (CIOL, "
                  "2021-02-17); stale. No later priced round found (Bing News, 2026-09-29)."))

# ---------------------------------------------------------------- Papaya Global
L.append(cls("papaya-global", flags=STALE, **V("papaya-global", "ivp"),
             note="Verify fix 2026-09-29: the $250M Series D at $3.7B (September 2021, the company's release as the IVP "
                  "row cites); stale. Sale talks at $3.5-4.5B were reported in January 2026 (Crowdfund Insider); "
                  "nothing signed was found (Bing News, 2026-09-29), so no new mark."))

# ---------------------------------------------------------------- Patreon
L.append(cls("patreon", flags=STALE, **V("patreon", "coatue"),
             note="Verify fix 2026-09-29: the $155M Series F led by Tiger at $4B (April 2021, TechCrunch as the Coatue "
                  "and Thrive rows cite); stale. An internal memo put the valuation 70% lower in 2022 (Business "
                  "Insider), an internal figure, not a priced event, so it stays in the note."))

# ---------------------------------------------------------------- Pristyn Care
L.append(cls("pristyn-care", flags=STALE, **MARK(SRC("pristyn-fortune"), 1_400_000_000, "2021-12-15"),
             note="Verify fix 2026-09-29: the $96M Series E made Pristyn Care a unicorn 'valued at $1.4 billion' "
                  "(Fortune India, 2021-12-15): 1b_plus, stale. A $4M top-up in July 2025 was done at the Series E "
                  "share price, 'indicating the valuation remains unchanged' (Entrackr), with no new figure stated."))

if __name__ == "__main__":
    jl.write("fix-c", L)
