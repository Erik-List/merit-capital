"""PRO-99 Kleiner Perkins, judge j05: the two batch-9 rows held back for their momentum-slice news checks
(superblocks, truv), recorded once nq.py returned (2026-09-30)."""
import judge_lib as jl
from judge_lib import cls, rnd


def PX(slug):
    m = [p["url"] for p in jl._POSTS if p["slug"] == slug]
    assert len(m) == 1, (slug, m)
    return m[0]


TC_SB = "https://techcrunch.com/2022/08/11/superblocks-secures-37m-to-help-companies-build-and-maintain-internal-apps/"

L = [
    cls("superblocks", status="private", rng="below_1b", country="US", stage="Series A", stage_src="first_party",
        stage_cite=PX("superblocks-series-a"), stage_conf="medium", entry_date="2021", focus="DevTools & APIs",
        flags=["city_unknown"],
        extra={"valuation_range_source": "web_verified", "valuation_citation": TC_SB},
        rounds=[rnd("2022-08-11", "Series A (part of $37M raised with Greenoaks, Spark and Meritech)", 37000000,
                    "Kleiner Perkins", True, PX("superblocks-series-a"), "firm"),
                rnd("2025-05-27", "$23M round", 23000000, None, None, None, "press")],
        note="Internal and AI app development platform. The firm's post says it led the Series A (announced "
             "2022-08-11, TechCrunch: $37M in total with Greenoaks, Spark and Meritech); the firm's listing year 2021 "
             "is read as that round's close year, and no source read shows an earlier Kleiner Perkins check. "
             "Momentum-slice check (nq.py, 2026-09-30): a $23M round in May 2025 and no priced round near $1B, so "
             "below_1b. No source read settles whether the office is in San Francisco or New York."),
    cls("truv", status="acquired", rng="below_1b", country="US", stage="Series A", stage_src="first_party",
        stage_cite=PX("truv-series-a"), stage_conf="medium", entry_date="2022-03", focus="Fintech & Payments",
        flags=["city_unknown"],
        rounds=[rnd("2022-03-03", "Series A", 25000000, "Kleiner Perkins", True, PX("truv-series-a"), "firm")],
        note="Income and employment verification (formerly Citadel API). The firm's post says it led the $25M Series "
             "A (March 2022; Business Insider headline the same day); the firm's listing year 2021 reads as the "
             "close year and no earlier Kleiner Perkins round is recorded. Momentum-slice check (nq.py, 2026-09-30): "
             "no $1B round; Checkr acquired Truv in August 2026 (Dealroom headline; truv.com now reads 'Truv is "
             "joining Checkr'), so acquired. No source read places its office."),
]

jl.write("j05c", L)
