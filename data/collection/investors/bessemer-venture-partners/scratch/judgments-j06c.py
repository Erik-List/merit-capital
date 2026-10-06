"""PRO-80 Bessemer, judge j06, file c: batch 12, first half (tensorzero to tsm).
Run as NQ_TAG=j06 python3 judgments-j06c.py."""
import json

import judge_lib as jl
from judge_lib import ARCH, FTS, NEWS, POST, SITE, W, cls, rnd, verdict

SIBS = json.loads((jl.INV / "scratch" / "siblings.json").read_text())
BVP = "Bessemer Venture Partners"
CHECK = "Momentum check 2026-10-01 (Google News): "


def SIB(slug, investor):
    m = [x for x in SIBS.get(slug, []) if x["investor"] == investor and x.get("val_cite")]
    if len(m) != 1:
        raise SystemExit(f"SIB({slug!r}, {investor!r}) matched {len(m)}")
    return m[0]["val_cite"]


GFI_F1 = "https://www.sec.gov/Archives/edgar/data/1534271/000104746912009998/a2208946zf-1.htm"
assert any(f["url"] == GFI_F1 for r in jl._FTS for f in r.get("filings", [])), "GFI F-1 not in fts-hits"
TRIP_S1 = "https://www.sec.gov/Archives/edgar/data/1107895/000095013010001225/ds1.htm"
assert any(f["url"] == TRIP_S1 for r in jl._FTS for f in r.get("filings", [])), "Tripwire S-1 not in fts-hits"

L = []

TZ = NEWS("tensorzero", "Raises $7.3M Seed Round")
L.append(cls("tensorzero", status="private", rng="below_1b",
             stage="Seed", stage_src="web_verified", stage_cite=TZ, stage_conf="high", entry_date="2024",
             grad="censored", country="US", city="New York", focus="DevTools & APIs",
             rounds=[rnd("2025-08-19", "Seed", 7300000, "FirstMark", True, TZ, "press")],
             note="citybiz, 2025-08-19: $7.3M seed led by FirstMark with Bessemer, Bedrock, DRW and Coalition; the "
                  "entry year is the listing's partnered year 2024, read at its last day, so the row is censored. " +
                  CHECK + "no round beyond the seed."))

L.append(cls("terra-bella-fka-skybox-imaging", status="acquired", rng="below_1b",
             stage="Growth", stage_src="model", stage_conf="medium", entry_date="2010",
             country="US", city="Mountain View", focus="Industrial & Robotics",
             rounds=[rnd("2010", "Series B", 18000000, BVP, True, None, "press"),
                     rnd("2012-04-10", "Series C", 70227931, None, True, None, "filing")],
             note="acq. by Google, 2014. Same company as the row skybox-imaging (renamed Terra Bella under Google): "
                  "Bessemer led the 2010 Series B, after Khosla's first round (named from knowledge), so the entry "
                  "reads Growth as on that row."))

TEC = POST("logistics-for-space-travel")
L.append(cls("the-exploration-company", status="private", rng="1b_plus", usd=2000000000, val_src="web_verified",
             val_cite=SIB("the-exploration-company", "atomico"), asof="2026-07-27",
             stage="Growth", stage_src="first_party", stage_cite=TEC, stage_conf="high", entry_date="2024-11-18",
             city="Munich", focus="Industrial & Robotics",
             rounds=[rnd("2024-11-18", "Series B", None, None, True, TEC, "firm")],
             note="The firm's own post announces its Europe team investing in the Series B (EUR 150M, November 2024). "
                  "Mark $2.0B at the July 2026 round, as the Atomico, Balderton and EQT books carry it."))

FUZE = W("Fuze (company)")
L.append(cls("thinking-phone-networks", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=FUZE, stage_conf="medium", entry_date="2012-09-27",
             city="Boston", focus="SaaS",
             rounds=[rnd("2010-01", "first venture round", 1200000, "Capstone Partners", False, FUZE, "press"),
                     rnd("2012-10", "second venture round", 16500000, "Advanced Technology Ventures and Bessemer",
                         True, FUZE, "press"),
                     rnd("2014-12", "later round", 56700000, "Technology Crossover Ventures", True, FUZE, "press")],
             note="acq. by 8x8, January 2022, as Fuze. Same company as the row fuze (renamed in 2016). Wikipedia: the "
                  "first venture capital was $1.2M from Capstone in 2010, and the $16.5M round of October 2012 led by "
                  "ATV and Bessemer followed it, so the entry is the second round and reads Growth. City as the "
                  "sibling books' Fuze rows."))

L.append(verdict("threattrack-security", "not_member",
                 "Spin-off of a control position (COLLECTION.md s1 control addendum, decisions.md D5): ThreatTrack "
                 "Security is the security business unit GFI Software spun off in March 2013, and the firm's listing "
                 "dates its investment 2013-03-31, the spin-off itself. Bessemer held GFI through the Insight-led "
                 "buyout group (GFI's F-1; see the teamviewer row), so this position arose from that control holding, "
                 "not from a venture round in ThreatTrack.",
                 ec="web", conf="medium", cite="https://www.securityweek.com/gfi-software-spins-security-business/"))

THU = NEWS("thunes", "completes Series C")
L.append(cls("thunes", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=THU, stage_conf="high", entry_date="2023-06-06",
             country="SG", country_src="web_verified", country_cite=W("Thunes"), city="Singapore",
             focus="Fintech & Payments",
             rounds=[rnd("2023-06-06", "Series C", 60000000, "Marshall Wace", True, THU, "press")],
             note="Singapore confirmed (Wikipedia: a Singapore-based company regulated by the MAS). Electronic "
                  "Payments International, 2023-06-06: over $60M Series C led by Marshall Wace, Bessemer among the "
                  "backers. " + CHECK + "no $1B priced round on record, as the Insight book."))

L.append(cls("tigo-energy", status="public", rng="below_1b", usd=66890000, val_src="web_verified",
             val_cite="https://stockanalysis.com/stocks/tygo/market-cap/", asof="2026-10-01",
             stage="Growth", stage_src="web_verified", stage_cite=W("Tigo Energy"), stage_conf="medium",
             city="Campbell", focus="Climate & Energy",
             rounds=[rnd("2011-11-21", "fourth round", 18000000, BVP, True, W("Tigo Energy"), "press")],
             note="Listed on Nasdaq (TYGO) since its 2023 merger with Roth CH Acquisition IV; market cap $66.9M on "
                  "2026-10-01 (stockanalysis). Wikipedia: the $18M round Bessemer led in December 2011 was the "
                  "company's fourth round of funding, which reads Growth (the Form D band, Series A, was withheld). "
                  "HQ Campbell, California (formerly Los Gatos)."))

L.append(cls("tile", status="acquired", rng="below_1b", stage="undetermined", entry_date="2013-10-09",
             city="San Mateo", focus="Consumer & Marketplaces",
             rounds=[rnd("2014", "Series A", 13000000, "GGV Capital", None, W("Tile (company)"), "press"),
                     rnd("2016-05-20", "later round", 18000000, None, True, jl.FORMD_CITE("tile", 0), "filing")],
             note="acq. by Life360 (agreed November 2021, closed January 2022). The firm's own investment date is "
                  "2013-10-09, before the 2014 Series A led by GGV, while Byron Deeter appears on the Form D of the "
                  "$18M round of May 2016; no page names the round Bessemer first bought, so the stage is "
                  "undetermined."))

L.append(cls("tilera", status="acquired", rng="below_1b", stage="undetermined", entry_date="2004-11-18",
             city="San Jose", focus="Industrial & Robotics",
             rounds=[rnd("2009-03-06", "later round", 11005000, None, True, jl.FORMD_CITE("tilera", 0), "filing")],
             note="acq. by EZchip Semiconductor, 2014 ($130M). The firm's own investment date is 2004-11-18, the "
                  "company's founding year (Devesh Garg of Bessemer was a co-founder); no source found names that "
                  "first round, so the stage is undetermined and the 2009 Form D date is replaced."))

TMRW = NEWS("tmrw-sports", "Latham")
L.append(cls("tmrw-sports", status="private", rng="below_1b", stage="undetermined", entry_date="2026",
             country="US", city="Winter Park", focus="Media, Gaming & Advertising",
             rounds=[rnd("2024-06-24", "Series A", None, "Dynasty Equity and Connect Ventures", False,
                         NEWS("tmrw-sports", "Valued at $500M in Series A"), "press"),
                     rnd("2026-03-30", "investor group for the NFL flag football league", None, None, True, TMRW,
                         "press")],
             note="Latham & Watkins, 2026-03-31: Bessemer is among the institutional investors in the professional "
                  "flag football league the NFL launched with TMRW Sports; the release names no round or amount, so "
                  "the stage is undetermined. The 2024 Series A valued TMRW near $500M; band and city as the NEA "
                  "book."))

TOAST = POST("memos/toast")
L.append(cls("toast", stage="Growth", stage_src="first_party", stage_cite=TOAST, stage_conf="high",
             city="Boston", focus="Fintech & Payments",
             rounds=[rnd("2015-12-23", "Series B (first institutional round)", 24000000, BVP, True, TOAST, "firm")],
             note="The firm's own investment memo of 2015-12-14, headed Toast Series B IR, recommends $17.5M in the "
                  "$24M first institutional round of the Boston based company; the firm's label for its entry round "
                  "is Series B, which reads Growth."))

L.append(cls("torch-dental", status="private", rng="below_1b", city="New York", focus="Healthcare & Bio",
             grad="graduated", grad_src="formd",
             note="Dental supply ordering platform, New York. The Form D sequence decides the graduation: a $2.5M seed "
                  "in November 2017, then $9.0M in July 2019 and $12.0M in March 2024. No $1B mark on record."))

TORQ_B = NEWS("torq", "Israeli no-code automation co Torq")
TORQ_SEED = POST("out-of-stealth-stackpulse")
L.append(cls("torq", status="private", rng="1b_plus", usd=1200000000, val_src="web_verified",
             val_cite=SIB("torq", "insight-partners"), asof="2026-01-11",
             stage="Seed", stage_src="first_party", stage_cite=TORQ_SEED, stage_conf="high", entry_date="2020",
             grad="graduated", grad_src="web_verified", grad_cite=TORQ_B, grad_conf="high",
             country="IL", country_src="web_verified", country_cite=TORQ_B, city="Tel Aviv", focus="Security",
             rounds=[rnd("2020", "Seed", None, BVP, True, TORQ_SEED, "firm"),
                     rnd("2021-01-19", "second round (two rounds, $28M in all)", None, None, True, TORQ_SEED, "firm"),
                     rnd("2021-12-08", "Series B", 50000000, "Insight Partners", True, TORQ_B, "press")],
             note="Same company as the row stackpulse: Globes (2021-12-08) calls Torq formerly Stackpulse, and the "
                  "firm's own post says it led StackPulse's seed round when the company was founded in 2020. The $50M "
                  "Series B led by Insight graduates the seed. Mark $1.2B (January 2026) and Tel Aviv as the Insight "
                  "book carries them."))

TOSS = NEWS("toss", "Closes $48M Series C")
L.append(cls("toss", status="private", rng="1b_plus", usd=7002897246, val_src="web_verified",
             val_cite=SIB("toss", "kleiner-perkins"), asof="2022-12-19", flags=["stale"],
             stage="Growth", stage_src="web_verified", stage_cite=TOSS, stage_conf="high", entry_date="2017-03-10",
             country="KR", country_src="web_verified", country_cite=TOSS, city="Seoul", focus="Fintech & Payments",
             rounds=[rnd("2017-03-10", "Series C", 48000000, "Goodwater Capital", True, TOSS, "press")],
             note="FinSMEs, 2017-03-10: Seoul-based Viva Republica closed a $48M Series C led by Goodwater with PayPal, "
                  "Bessemer, Altos and Partech. Mark as the Kleiner and Ribbit books: the December 2022 Series G "
                  "(older than 24 months, hence stale)."))

YNET = NEWS("traffix", "multiplies seed investment")
L.append(cls("traffix", status="acquired", rng="below_1b", stage="undetermined", entry_date="2011",
             country="IL", country_src="web_verified", country_cite=YNET, city="Hod HaSharon",
             focus="Data Infrastructure",
             rounds=[rnd("2011", "$7M round led by Bessemer", 7000000, BVP, True, YNET, "press")],
             note="acq. by F5 Networks, February 2012 (about $135M). Ynet: Bessemer led a $7 million financing round "
                  "three months before the sale and held 25%, after StageOne's seed; the round is not named, so the "
                  "stage is undetermined."))

L.append(cls("transave-inhalation-biopharmaceuticals", status="acquired", rng="below_1b",
             stage="Growth", stage_src="model", stage_conf="medium", entry_date="2007-12-14",
             city="Monmouth Junction", city_src="formd_address", focus="Healthcare & Bio",
             flags=["stage_disputes_band"],
             rounds=[rnd("2007-12", "Series D", 35000000, None, True, None, "press"),
                     rnd("2009-10-26", "later round", 12000000, None, True,
                         jl.FORMD_CITE("transave-inhalation-biopharmaceuticals", 0), "filing")],
             note="Merged into Insmed, December 2010 (acq. by Insmed, 2010); the row insmed is the stock received in "
                  "that sale. The firm's own investment date is 2007-12-14, the $35M Series D of a company founded in "
                  "1997 (named from knowledge), so the Series A band read off the 2009 Form D is disputed."))

TB = POST("reimagining-indias-corporate-banking")
L.append(cls("transbnk", status="private", rng="below_1b",
             stage="Growth", stage_src="first_party", stage_cite=TB, stage_conf="high", entry_date="2025-08-27",
             country="IN", country_src="web_verified", country_cite=TB, city="Mumbai", focus="Fintech & Payments",
             rounds=[rnd("2025-08-27", "Series B", 25000000, BVP, True, TB, "firm")],
             note="The firm's own post announces it leading TransBnk's $25M Series B, its first investment in the "
                  "Mumbai company. " + CHECK + "no $1B priced round."))

L.append(cls("triana-biomedicines", status="private", rng="below_1b", city="Lexington", city_src="formd_address",
             focus="Healthcare & Bio",
             note="Molecular glue degrader biotech; the November 2025 Form D ($120M round, Andrew Hedin a director) "
                  "files from Lexington, Massachusetts, which is fresher than the Lightspeed book's Waltham. No $1B "
                  "mark on record."))

L.append(cls("tripwire", status="acquired", rng="below_1b", stage="undetermined", entry_date="2000-02-03",
             city="Portland", focus="Security",
             rounds=[rnd("2000-02-03", "round with Bessemer", None, None, True, TRIP_S1, "filing")],
             note="acq. by Thoma Bravo, 2011, then by Belden, 2014. The 2010 S-1 shows the Bessec Ventures V and "
                  "Bessemer Venture Partners V funds holding 10.06% and Series A to D preferred outstanding, without "
                  "saying which series the funds bought in 2000, so the stage is undetermined (as the IVP book); the "
                  "2009 Form D date is replaced by the firm's own."))

L.append(cls("trm-labs", status="private", rng="1b_plus", usd=2000000000, val_src="web_verified",
             val_cite=SIB("trm-labs", "tiger-global-management"), asof="2026-09-09",
             stage="Series A", stage_src="model", stage_conf="medium", entry_date="2021",
             country="US", city="San Francisco", focus="Fintech & Payments",
             rounds=[rnd("2021-06", "Series A", 14000000, BVP, True, None, "press"),
                     rnd("2026-02-04", "Series C", 70000000, "Blockchain Capital", None,
                         NEWS("trm-labs", "SiliconANGLE"), "press")],
             note="Bessemer led the $14M Series A of June 2021 (named from knowledge; the news query surfaced only "
                  "later rounds). Mark $2.0B at the September 2026 Series C expansion, as the Tiger Global book; the "
                  "YC book still carries the February 2026 $1B."))

TRUE = POST("truebill-the-real-deal")
L.append(cls("truebill", status="acquired", rng="below_1b",
             stage="Growth", stage_src="first_party", stage_cite=TRUE, stage_conf="high", entry_date="2020-11-12",
             country="US", city="Silver Spring", focus="Fintech & Payments",
             rounds=[rnd("2020-11-12", "Series B (reported as Series C)", 17000000, BVP, True, TRUE, "firm"),
                     rnd("2021-06-01", "Series D", 45000000, "Accel", True,
                         NEWS("truebill", "Raises $45M in Series D"), "press")],
             note="acq. by Rocket Companies, December 2021 ($1.275B). The firm's own post says it led the Series B a "
                  "little over a year earlier, the $17M round of November 2020 (the press called it a Series C). City "
                  "as the YC book; the Accel book carries Des Plaines."))

L.append(cls("tscan-therapeutics", city="Waltham", focus="Healthcare & Bio",
             note="HQ Waltham, Massachusetts, as the GV book."))

L.append(cls("tsm", status="private", rng="below_1b", stage="Series A", stage_src="model", stage_conf="medium",
             entry_date="2018", country="US", city="Los Angeles", focus="Media, Gaming & Advertising",
             rounds=[rnd("2018-07-24", "Series A", 37000000, BVP, True, NEWS("tsm", "Raises $37 Million"), "press")],
             note="Esports organisation (Swift, parent of Team SoloMid). Bessemer led the $37M Series A announced "
                  "2018-07-24 (Forbes carries the raise; the page is paywalled, so the round word and the lead are "
                  "named from knowledge). No $1B mark on record."))

assert len(L) == 23, len(L)
jl.write("j06c", L)
