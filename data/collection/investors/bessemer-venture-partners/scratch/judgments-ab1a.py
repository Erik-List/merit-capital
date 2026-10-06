"""A/B pass, judge ab1 (PRO-80): private rows at $1B or more, first half (abridge to jasper).

Pass A re-pins every mark that rested on the unicorn list to the round's own report (read on 2026-10-06); pass B
searched Google News (nq.py) for a newer round, a sale, a down round or a shutdown. Only the keys that change.

Run once: NQ_TAG=ab1 python3 judgments-ab1a.py
"""
import json

import judge_lib as jl
from judge_lib import cls, rnd, NEWS, POST

WV = "web_verified"
X = {"valuation_range_source": WV}
_CL = json.loads((jl.INV / "companies" / "classification.json").read_text())
_CL = _CL.get("bessemer-venture-partners", _CL)


def R(slug):
    """The funding rounds already on the row (record replaces the list, so a line carries the whole list)."""
    return [dict(x) for x in (_CL.get(slug) or {}).get("funding_rounds") or []]


L = []

# ---- abridge: the unicorn list's $2.75B was the February 2025 round; the Series E of June 2025 is the mark
TC_ABR = NEWS("abridge", "In just 4 months")
r = R("abridge") + [rnd("2025-06-24", "Series E", 300_000_000, "Andreessen Horowitz", None, TC_ABR)]
L.append(cls("abridge", rng="1b_plus", usd=5_300_000_000, val_src=WV, val_cite=TC_ABR, asof="2025-06-24", extra=X,
             flags=["cite_pending"], rounds=r,
             note="A/B 2026-10-06: the mark moves from the unicorn list's $2.75B to the $300M Series E of 2025-06-24 at "
                  "$5.3B (TechCrunch, read; led by Andreessen Horowitz), and Eli Lilly's equity investment of June 2026 "
                  "disclosed no valuation (Endpoints headline). A second try at the entry found only the combined seed "
                  "and Series A report of 2020, so the stage stays undetermined with cite_pending."))

# ---- axonius
TC_AX = "https://techcrunch.com/2024/03/05/axonius-a-specialist-in-cyber-asset-managment-secures-200m-at-a-flat-2-6b-valuation/"
POST_AX = POST("lessons-from-axonius")
L.append(cls("axonius", rng="1b_plus", usd=2_600_000_000, val_src=WV, val_cite=TC_AX, asof="2024-03-05", extra=X,
             stage="Series A", stage_src="first_party", stage_cite=POST_AX, stage_conf="high", flags=["stale"],
             rounds=[rnd("2019-02", "Series A", None, None, True, POST_AX, "firm"),
                     rnd("2021", "round at a $1.2B valuation", 100_000_000, None, None, TC_AX),
                     rnd("2022-03", "Series E", 200_000_000, "Accel", None, TC_AX),
                     rnd("2024-03-05", "Series E extension", 200_000_000, "Lightspeed and Accel", None, TC_AX)],
             note="A/B 2026-10-06: the mark moves from the unicorn list's $1.2B (2021) to the $200M Series E extension "
                  "of 2024-03-05 at a flat $2.6B (TechCrunch, read), older than 24 months, so stale; the January 2026 "
                  "report of sale talks with Cisco at $2B was denied (CTech and Techzine headlines) and is no priced "
                  "event. The Series A entry now cites the firm's own post instead of the Form D band."))

# ---- bigid
SW_BIG = NEWS("bigid", "BigID Raises $60 Million at $1 Billion")
POST_BIG = POST("bessemer-series-c-investment-bigid")
L.append(cls("bigid", rng="1b_plus", usd=1_000_000_000, val_src=WV, val_cite=SW_BIG, asof="2024-03-18", extra=X,
             stage="Growth", stage_src="first_party", stage_cite=POST_BIG, stage_conf="high", flags=["stale"],
             rounds=[rnd("2019-09-05", "Series C", 50_000_000, "Bessemer Venture Partners", True, POST_BIG, "firm"),
                     rnd("2020-12-16", "round at a $1B valuation", 70_000_000, None, None, None),
                     rnd("2021-04-22", "Advent investment at a $1.25B valuation", 30_000_000, "Advent International", None, None),
                     rnd("2024-03-18", "growth round", 60_000_000, "Riverwood Capital", None, SW_BIG)],
             note="A/B 2026-10-06: the last priced round is the $60M growth round of March 2024 led by Riverwood, "
                  "'valued at more than $1 billion' (SecurityWeek, read), which replaces the unicorn list's $1.25B (the "
                  "Advent round of April 2021) and matches the Tiger Global row; older than 24 months, so stale. A "
                  "fifth of the staff was cut in May 2026 (CTech headline); no lower priced event found."))

# ---- canva
FORTUNE_CANVA = NEWS("canva", "billionaire founders are minting")
TC_CANVA = "https://techcrunch.com/2019/10/16/canva-now-valued-at-3-2-billion-launches-an-enterprise-product/"
L.append(cls("canva", rng="10b_plus", usd=42_000_000_000, val_src=WV, val_cite=FORTUNE_CANVA, asof="2025-08", extra=X,
             stage="Growth", stage_src=WV, stage_cite=TC_CANVA, stage_conf="high", entry_date="2019-10-16",
             rounds=[rnd("2019-10-16", "round at a $3.2B valuation", 85_000_000, None, True, TC_CANVA),
                     rnd("2025-08", "employee share sale at a $42B valuation", None, None, None, FORTUNE_CANVA)],
             note="A/B 2026-10-06: the mark is re-pinned to the employee share sale of August 2025 'valuing the company "
                  "at $42 billion' (Fortune, read), the last priced transaction; in August 2026 Blackbird and Airtree "
                  "marked it down to about US$34.9B and the yearly independent valuation for staff shares read US$31B "
                  "(Startup Daily, read), which are fund marks and not priced events, and the band holds either way. "
                  "TechCrunch (2019-10-16, read) names Bessemer among the investors at the $85M raise at $3.2B, so the "
                  "Growth entry is cited."))

# ---- choco
TC_CHOCO = "https://techcrunch.com/2019/10/28/choco-raises-33-5m-to-bring-restaurants-and-suppliers-a-modern-ingredient-ordering-platform/"
r = R("choco")
r[0].update({"date": "2019-10-28", "source": TC_CHOCO})
L.append(cls("choco", stage="Series A", stage_src=WV, stage_cite=TC_CHOCO, stage_conf="high", entry_date="2019-10-28",
             rounds=r,
             note="A/B 2026-10-06: TechCrunch (2019-10-28, read): 'closed a $33.5 million Series A led by Bessemer "
                  "Venture Partners', so the entry is cited; no priced round after the April 2022 Series B2 found "
                  "(Google News), the mark stays stale."))

# ---- clickhouse, cloudinary, drivenets, firebolt, jasper: attacked, nothing changes
L.append(cls("clickhouse", note="A/B 2026-10-06: no priced round after the January 2026 Series D found (Google News; "
             "TechCrunch headline of 2026-05-27 on $250M of annualized revenue and a path to a listing)."))
L.append(cls("cloudinary", note="A/B 2026-10-06: no priced event after Blackstone's purchase of February 2022 found "
             "(Google News)."))
L.append(cls("drivenets", note="A/B 2026-10-06: no priced event after the June 2026 Series D found (Google News); "
             "Reuters and Globes headlines of 2026-06-01 carry the same $410M and $8.5B."))
L.append(cls("firebolt", note="A/B 2026-10-06: no priced round after January 2022 found (Google News); the workforce "
             "cut of February 2026 (CTech headline) came with no financing."))
L.append(cls("jasper", note="A/B 2026-10-06: no priced round after October 2022 found (Google News)."))

# ---- discord
CNBC_DISCORD = "https://www.cnbc.com/2021/09/22/discord-doubles-valuation-to-15-billion-in-new-funding-round.html"
r = R("discord")
r[1] = rnd("2020-12", "round at over $7B", 100_000_000, "Bessemer Venture Partners and Greenoaks Capital", True, CNBC_DISCORD)
r[2].update({"date": "2021-09-22"})
L.append(cls("discord", rng="10b_plus", usd=15_000_000_000, val_src=WV, val_cite=CNBC_DISCORD, asof="2021-09-22", extra=X,
             stage="Growth", stage_src=WV, stage_cite=CNBC_DISCORD, stage_conf="medium", entry_date="2020-12",
             flags=["stale"], rounds=r,
             note="A/B 2026-10-06: CNBC (2021-09-22, read) cites both columns: the $500M round led by Dragoneer leaves "
                  "Discord 'valued at $15 billion', and 'in December 2020, Discord raised $100 million' in a round "
                  "'led by Bessemer Venture Partners and Greenoaks Capital'. The mark is older than 24 months, so stale; "
                  "the listing planned for 2026 has not priced (Google News, 2026-10-06), and the $8.5B figures in "
                  "circulation are forecasts, not a priced event."))

# ---- forter
TC_FORTER = "https://techcrunch.com/2021/05/25/forter-raises-300m-on-a-3b-valuation-for-a-platform-to-combat-e-commerce-fraud/"
r = R("forter") + [rnd("2021-05-25", "Series F", 300_000_000, "Tiger Global", True, TC_FORTER)]
L.append(cls("forter", rng="1b_plus", usd=3_000_000_000, val_src=WV, val_cite=TC_FORTER, asof="2021-05-25", extra=X,
             flags=["stale"], rounds=r,
             note="A/B 2026-10-06: the mark is re-pinned from the unicorn list to the $300M Series F of 2021-05-25, which "
                  "'values Forter at $3 billion' and names Bessemer among the existing investors (TechCrunch, read); "
                  "older than 24 months, so stale, and no later priced round found (Google News)."))

# ---- guild
PRN_GUILD = NEWS("guild", "Guild Raises $21 Million")
r = R("guild")
r[0].update({"date": "2017-09-06", "source": PRN_GUILD, "source_type": "company"})
L.append(cls("guild", stage="Growth", stage_src=WV, stage_cite=PRN_GUILD, stage_conf="high", entry_date="2017-09-06",
             rounds=r,
             note="A/B 2026-10-06: the company's release of 2017-09-06 (read): 'closed a $21 million Series B financing "
                  "round led by Bessemer Ventures', so the Growth entry is cited and dated instead of resting on the "
                  "2019 Form D; no priced round after June 2022 found (Google News), the mark stays stale."))

if __name__ == "__main__":
    jl.write("ab1a", L)
