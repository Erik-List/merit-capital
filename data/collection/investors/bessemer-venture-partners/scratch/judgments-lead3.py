"""Lead overrides 3 (2026-10-06): rule 10 decisions taken by the lead after the cross-book triage."""
import judge_lib as jl
lines = [
    jl.cls("the-exploration-company", rng="1b_plus", usd=2000000000, val_src="web_verified",
           val_cite="https://thenextweb.com/news/exploration-company-300m-raise-spacex-rival", asof="2026-07-27",
           extra={"valuation_range_source": "web_verified"},
           note="Lead decision 2026-10-06 (rule 10): the band returns to 1b_plus at $2.0B, the price the Financial Times "
                "reported for the Series C while it was being raised (via The Next Web, 2026-07-27); the round closed on "
                "2026-09-08 at $450M with no valuation disclosed. The Atomico, Balderton and EQT Ventures books carry "
                "the same mark on the same report, at low confidence, on the reasoning that a $450M primary round "
                "cannot sit under a $1B valuation; this book follows them so the four read alike."),
]
jl.write("lead3", lines)
