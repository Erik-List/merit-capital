#!/usr/bin/env python3
"""PRO-167 Tiger Global, verify-gap fix d (2026-09-29): valuation band for the other 14 of the 29 rows in
needs-value.json (productboard .. spinny), on the same rules as fix c. Non-USD marks convert with
scripts/fx-convert.py at the ECB rate of the figure's date.
Run: NQ_TAG=fx python3 fixd.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl  # noqa: E402
from judge_lib import cls  # noqa: E402
from fxlib import SRC, BURL, V, MARK  # noqa: E402

L = []
STALE = ("stale",)

# ---------------------------------------------------------------- Productboard
L.append(cls("productboard", flags=STALE, **V("productboard", "sequoia-capital"),
             note="Verify fix 2026-09-29: the $125M Series D co-led by Tiger at $1.725B (February 2022, the company's "
                  "post as the Sequoia row cites, written $1.72B); stale. Layoffs through January 2024 (Business "
                  "Insider) and no later priced round found (Bing News, 2026-09-29)."))

# ---------------------------------------------------------------- Qonto
L.append(cls("qonto", flags=STALE,
             **MARK(BURL("qonto", "French fintech Qonto nears $5 billion valuation", "finance.yahoo.com"),
                    4_987_840_000, "2022-01-11"),
             note="Verify fix 2026-09-29: the EUR 486M Series D co-led by Tiger and TCV valued Qonto at EUR 4.4B "
                  "(Reuters via Yahoo, 2022-01-11): EUR 4.40B @ ECB 2022-01-11 (EUR/USD 1.1336) = $4.99B, stale. The "
                  "FT reported talks on a share sale at EUR 5B in November 2024; no completed sale with a price was "
                  "found (Bing News, 2026-09-29). Insight's row reads $5.0B, same band."))

# ---------------------------------------------------------------- Quora: the 2024 round at $500M
L.append(cls("quora", flags=STALE, **MARK(SRC("quora-tc"), 500_000_000, "2024-01-09"),
             note="Verify fix 2026-09-29: Quora raised $75M from a16z in January 2024 and 'Quora's latest raise values "
                  "the company at just $500 million, a steep decline from its previous raise' (TechCrunch via Yahoo, "
                  "2024-01-09): below_1b at $500M, stale. This is fresher than the Benchmark row's $1.8B of 2017; the "
                  "a16z row, whose own note records the round at about $500M, carries no band. Both should follow."))

# ---------------------------------------------------------------- Rapyd
L.append(cls("rapyd", **V("rapyd", "coatue"),
             note="Verify fix 2026-09-29: the $500M round of March 2025 at $4.5B (Calcalist, as the Coatue and General "
                  "Catalyst rows cite), a down round from the 2021 peak; not stale. The Spark row's $15B (2022) is "
                  "older and should follow."))

# ---------------------------------------------------------------- Razorpay
L.append(cls("razorpay-inc", flags=STALE, **V("razorpay-inc", "lightspeed"),
             note="Verify fix 2026-09-29: the $375M Series F at $7.5B (December 2021, TechCrunch as the Lightspeed and "
                  "Y Combinator rows cite); stale. 2026 reports of an IPO at a $5-6B target are not a priced event "
                  "(Bing News, 2026-09-29)."))

# ---------------------------------------------------------------- Redis
L.append(cls("redis", flags=STALE,
             **MARK(BURL("redis", "Redis Labs surpasses $2B valuation", "zdnet"), 2_000_000_000, "2021-04-07"),
             note="Verify fix 2026-09-29: Tiger led the $110M Series G, which took the valuation to more than $2B "
                  "(ZDNet, 2021-04-07), written as $2.0B; stale. The April 2024 sale of $200-300M of shares by Tiger "
                  "and Viola at over $2B (Calcalist) was a secondary, so it stays in the note. No later priced round "
                  "found (Bing News, 2026-09-29)."))

# ---------------------------------------------------------------- Relativity Space
L.append(cls("relativity-space", flags=STALE, **V("relativity-space", "y-combinator"),
             note="Verify fix 2026-09-29: the last priced primary is the $650M Series E at $4.2B (June 2021, CNBC as "
                  "the Y Combinator row cites); stale. Eric Schmidt bought a controlling stake and became CEO in 2025 "
                  "at a price not disclosed (Bing News, 2026-09-29), so no figure replaces the 2021 mark; whether that "
                  "deal is collapse evidence is Erik's call."))

# ---------------------------------------------------------------- Revolut
L.append(cls("revolut", **V("revolut", "coatue"),
             note="Verify fix 2026-09-29: Revolut confirmed a $115B valuation in its July 2026 secondary share sale "
                  "(Bloomberg, as the Coatue, Balderton, Point Nine and Ribbit rows cite), a company-run sale at a "
                  "stated price: 100b_plus, not stale. The a16z and Greylock rows still carry the $75B sale of 2025."))

# ---------------------------------------------------------------- SafetyCulture
L.append(cls("safetyculture", flags=STALE, **MARK(SRC("safetyculture-afr"), 1_663_503_254, "2024-09-09"),
             note="Verify fix 2026-09-29: the A$165M round led by Airtree revalued SafetyCulture at A$2.5B, down from "
                  "A$2.7B (AFR, 2024-09-09): AUD 2.50B @ ECB 2024-09-09 (AUD/EUR 1.6596, EUR/USD 1.1043) = $1.66B, "
                  "1b_plus; 20 days past the 24-month line, so stale. No later priced round found (Bing News, "
                  "2026-09-29)."))

# ---------------------------------------------------------------- ShareChat
L.append(cls("sharechat", flags=STALE, **V("sharechat", "lightspeed"),
             note="Verify fix 2026-09-29: the last priced round was in mid-2022 at $4.9B; the April 2024 $49M "
                  "convertible round carried no stated valuation, and TechCrunch's source put its conversion below "
                  "$2B, the $2.0B the Lightspeed row carries (2024-04). Aligned, stale. No later priced round found "
                  "(Bing News, 2026-09-29)."))

# ---------------------------------------------------------------- slice: the September 2026 down round
L.append(cls("slice", **MARK(BURL("slice", "at lower valuation of $450 million", "moneycontrol"), 450_000_000,
                             "2026-09-03"),
             note="Verify fix 2026-09-29: slice Small Finance Bank raised $100M from Neo Wealth, Kado Global and Moore "
                  "Strategic Ventures 'at lower valuation of $450 million' (Moneycontrol, 2026-09-03; the Economic "
                  "Times reports $470M), a correction of nearly 70%: below_1b at $450M, not stale. Insight's 'Slice' "
                  "is Slice Global Equity, another company."))

# ---------------------------------------------------------------- Snyk
L.append(cls("snyk", flags=STALE, **V("snyk", "gv"),
             note="Verify fix 2026-09-29: the $196.5M Series G at $7.4B (December 2022, Snyk's release as the GV row "
                  "cites); stale. Business Insider (2026-08-28) reports the internal value of employee shares fell to "
                  "$1.16 a share from over $10 at the peak; an internal price, not a priced round or tender, so it "
                  "stays in the note and the collapse reading is Erik's."))

# ---------------------------------------------------------------- Spendesk
L.append(cls("spendesk", flags=STALE, **MARK(SRC("spendesk-tc"), 1_140_300_000, "2022-01-17"),
             note="Verify fix 2026-09-29: Tiger's EUR 100M ($114M) extension of the Series C gave Spendesk 'a valuation "
                  "of more than $1.14 billion (more than EUR 1 billion)' (TechCrunch, 2022-01-17): EUR 1.00B @ ECB "
                  "2022-01-17 (EUR/USD 1.1403) = $1.14B, 1b_plus, stale. No later priced round found (Google News and "
                  "Bing News, 2026-09-29)."))

# ---------------------------------------------------------------- Spinny
L.append(cls("spinny", **V("spinny", "accel"),
             note="Verify fix 2026-09-29: the Series G of about $160M, primary and secondary, at about $1.8B post-money "
                  "(TechCrunch, 2025-12-13; Accel had wired $44M per Indian filings), the Accel row's mark; not stale. "
                  "Spinny filed confidentially for an Indian IPO in September 2026 (Reuters)."))

if __name__ == "__main__":
    jl.write("fix-d", L)
