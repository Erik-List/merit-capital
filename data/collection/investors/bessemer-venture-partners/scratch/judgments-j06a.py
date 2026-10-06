"""PRO-80 Bessemer, judge j06, file a: batch 11 rows decided from the firm's own posts, the archive, S-1s and
Wikipedia (no news query needed). Run as NQ_TAG=j06 python3 judgments-j06a.py."""
import json

import judge_lib as jl
from judge_lib import ARCH, FTS, POST, SITE, W, cls, rnd, verdict

SIBS = json.loads((jl.INV / "scratch" / "siblings.json").read_text())
BVP = "Bessemer Venture Partners"


def SIB(slug, investor):
    """The valuation citation a sibling book already carries for the same company (read from siblings.json)."""
    m = [x for x in SIBS.get(slug, []) if x["investor"] == investor and x.get("val_cite")]
    if len(m) != 1:
        raise SystemExit(f"SIB({slug!r}, {investor!r}) matched {len(m)}")
    return m[0]["val_cite"]


GFI_F1 = FTS("GFI Software", "F-1")
assert GFI_F1.endswith("a2208946zf-1.htm") or "a2208946z" in GFI_F1, GFI_F1
GFI_F1 = "https://www.sec.gov/Archives/edgar/data/1534271/000104746912009998/a2208946zf-1.htm"
SIRT_S1 = FTS("Sirtris", "S-1")
STUB_DRS = FTS("StubHub Holdings, Inc.", "DRS")
TEAM8_FUND = jl.NEWS("team8", "Second Company Creation Vehicle")

L = []

L.append(cls("sirtris-pharmaceuticals", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=SIRT_S1, stage_conf="medium", entry_date="2006-03-14",
             country="US", city="Cambridge", focus="Healthcare & Bio",
             rounds=[rnd("2004-08-17", "Series A", 5000000, None, False, SIRT_S1, "filing"),
                     rnd("2004-11-16", "Series A-1", 13000000, None, False, SIRT_S1, "filing"),
                     rnd("2005-02-25", "Series B", 27000000, None, False, SIRT_S1, "filing"),
                     rnd("2006-03-14", "Series C", 22100000, None, True, SIRT_S1, "filing"),
                     rnd("2007-01-23", "Series C-1", 35900000, None, None, SIRT_S1, "filing")],
             note="IPO May 2007 (NASDAQ: SIRT), then acq. by GlaxoSmithKline, 2008. The S-1 dates the Series C first "
                  "closing to 2006-03-14, the firm's own investment date, and Steve Kraus joined the board in 2006; the "
                  "S-1 does not name the Bessemer funds among the 5% holders, hence medium confidence."))

L.append(cls("sisense", city="New York", city_src="formd_address",
             note="HQ New York (Form D address, Wikipedia), R&D in Israel; the Battery book carries New York, the "
                  "Insight book Ramat Gan."))

L.append(cls("skybox-imaging", status="acquired", rng="below_1b", entry_date="2010-09-09", city="Mountain View",
             focus="Industrial & Robotics",
             note="acq. by Google, 2014. The firm's own investment date is 2010-09-09, two years before the 2012 Form D "
                  "the band read; the 2010 round followed Khosla's first round, so the stage stays Growth. Same company "
                  "as the row terra-bella-fka-skybox-imaging."))

L.append(cls("skype", status="acquired", rng="below_1b", stage="undetermined", entry_date="2003-10-20",
             country="LU", country_src="web_verified", country_cite=W("Skype Technologies"), city="Luxembourg",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2003-10-20", "first institutional round", None, BVP, True, ARCH("skype"), "firm")],
             note="acq. by eBay, 2005, then by Microsoft, 2011. The firm's archived listing says Rob Stavis led the "
                  "company's first institutional round in 2003 and names no round word, so the stage stays "
                  "undetermined; a later pass could settle it from a source naming that 2003 round."))

L.append(cls("smarterdx", status="acquired", rng="below_1b",
             stage="Series A", stage_src="first_party", stage_cite=POST("from-residency-to-rocketship"),
             stage_conf="high", entry_date="2023", country="US", city="New York", focus="Healthcare & Bio",
             rounds=[rnd("2023", "Series A", None, None, True, POST("from-residency-to-rocketship"), "firm")],
             note="acq. by New Mountain Capital, 2025 (the firm's listing). The firm's own post dates the relationship "
                  "from its Series A investment; the entry year is the listing's partnered year."))

L.append(cls("snapdeal", stage="Growth", stage_src="web_verified", stage_cite=W("Snapdeal"), stage_conf="medium",
             entry_date="2011-07", country="IN", country_src="web_verified", country_cite=SITE("snapdeal"),
             city="New Delhi", focus="Consumer & Marketplaces",
             rounds=[rnd("2011-07", "second round", 45000000, None, True, W("Snapdeal"), "press"),
                     rnd("2014-02", "round led by eBay", 133000000, "eBay", True, W("Snapdeal"), "press")],
             note="India confirmed (the firm's listing calls it India's largest e-commerce marketplace; Wikipedia "
                  "places it in New Delhi). Bessemer entered in the July 2011 $45M round alongside existing investors, "
                  "the company's second round, which reads Growth."))

L.append(cls("social-tables", status="acquired", rng="below_1b", city="Washington", focus="SaaS",
             note="acq. by Cvent, 2018. The firm's own post confirms the band: Alex Ferrara led the 2014 Series A."))

L.append(cls("soluto", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=W("Soluto"), stage_conf="medium",
             city="Tel Aviv", focus="Consumer & Marketplaces", flags=["stage_disputes_band"],
             rounds=[rnd("2009", "second round", 6200000, BVP, True, W("Soluto"), "press"),
                     rnd("2011-06-07", "round led by Index Ventures", 10237529, "Index Ventures", None,
                         jl.FORMD_CITE("soluto", -1), "filing")],
             note="acq. by Asurion, 2013. The $6.2M round Bessemer led in 2009 was the company's second round of "
                  "financing (Wikipedia), after Giza and Proxima's first round, so the entry reads Growth and the "
                  "Form D band's Seed is disputed."))

L.append(cls("sorare", rng="1b_plus", usd=4300000000, val_src="web_verified", val_cite=SIB("sorare", "accel"),
             asof="2021-09-21", flags=["stale"],
             stage="Growth", stage_src="first_party", stage_cite=POST("sorare-building-top-nft"), stage_conf="high",
             entry_date="2021-09-21", country="FR", country_src="web_verified",
             country_cite=POST("sorare-building-top-nft"), city="Paris", focus="Media, Gaming & Advertising",
             rounds=[rnd("2021-09-21", "Series B", 680000000, "SoftBank", True, POST("sorare-building-top-nft"), "firm")],
             note="France confirmed: the firm's own post calls it a Paris-based startup and announces Bessemer's "
                  "participation in the $680M Series B, which valued the company at $4.3B (the mark the sibling books "
                  "carry; older than 24 months, hence stale)."))

L.append(cls("spire", stage="Growth", stage_src="web_verified", stage_cite=W("Spire Global"), stage_conf="medium",
             entry_date="2015-06-11", city="Vienna", focus="Industrial & Robotics",
             rounds=[rnd("2013-02", "Seed", 1500000, "Shasta Ventures", False, W("Spire Global"), "press"),
                     rnd("2014-07", "Series A", 25000000, "RRE Ventures", False, W("Spire Global"), "press"),
                     rnd("2015-06-30", "Series B", 40000000, "Promus Ventures", True, W("Spire Global"), "press")],
             note="Bessemer joined the June 2015 $40M round led by Promus Ventures, which followed the 2013 seed and "
                  "the 2014 Series A (Wikipedia calls it the Series B); the firm's own investment date is 2015-06-11. "
                  "HQ Vienna, Virginia."))

L.append(cls("storwize", status="acquired", rng="below_1b",
             stage="Growth", stage_src="model", stage_conf="medium", entry_date="2008-03-28",
             country="IL", country_src="web_verified", country_cite=ARCH("storwize"), city="Yokneam",
             focus="Data Infrastructure",
             rounds=[rnd("2008", "Series C", 25000000, None, True, None, "press")],
             note="acq. by IBM, 2010. Bessemer entered in the $25M Series C of early 2008, after Sequoia Israel and "
                  "Genesis backed the earlier rounds (named from knowledge, no page in hand); the firm's archived "
                  "listing files the company under Israel."))

L.append(cls("streambase", status="acquired", rng="below_1b",
             stage="Series A", stage_src="model", stage_conf="medium", entry_date="2003-07-24",
             city="Lexington", focus="Data Infrastructure",
             rounds=[rnd("2003", "Series A", None, None, True, None, "press"),
                     rnd("2010-04-20", "later round", 5500000, None, True, jl.FORMD_CITE("streambase", 0), "filing")],
             note="acq. by TIBCO Software, 2013. Bessemer and Accel funded the 2003 Series A of the company, then "
                  "called Grassy Brook (named from knowledge; the firm's own investment date is 2003-07-24, the "
                  "founding year). City as the Accel book."))

L.append(cls("stubhub", rng="1b_plus", usd=2110000000, val_src="web_verified", val_cite=SIB("viagogo", "atomico"),
             asof="2026-10-01", stage="undetermined", entry_date="2012", country="US", city="New York",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2019-11-24", "equity commitment for the StubHub acquisition", None, None, True, STUB_DRS,
                         "filing")],
             note="Market cap $2.11B on 2026-10-01 (stockanalysis, STUB). The firm entered Viagogo in 2012 and helped "
                  "finance its purchase of StubHub from eBay; neither the firm's posts nor the prospectus name the "
                  "2012 round, so the stage stays undetermined. Same company as the row viagogo."))

L.append(cls("sukino", status="private", rng="below_1b",
             stage="Growth", stage_src="first_party", stage_cite=POST("expanding-continuum-healthcare-in-india"),
             stage_conf="high", entry_date="2025", country="IN", country_src="web_verified",
             country_cite=POST("expanding-continuum-healthcare-in-india"), city="Bangalore", focus="Healthcare & Bio",
             rounds=[rnd("2026-01-13", "Series B", 31000000, BVP, True,
                         POST("expanding-continuum-healthcare-in-india"), "firm")],
             note="The firm's own post announces it leading the $31M Series B as a new backer (announced 2026-01-13; "
                  "the live listing's partnered year is 2025, the archive's 2020 is unexplained). Centers in "
                  "Bangalore, Kochi and Coimbatore."))

L.append(cls("summit-microelectronics", status="acquired", rng="below_1b", stage="undetermined", entry_date="1997",
             city="Sunnyvale", focus="Industrial & Robotics", rounds=[],
             note="acq. by Qualcomm, 2012. The firm's archived listing gives 1997 and 1998 as investment years and no "
                  "round; nothing found names the entry round, so the stage is undetermined (the 2011 Form D is a "
                  "late insider round, not the entry)."))

L.append(cls("supermaven", status="acquired", rng="below_1b",
             stage="Seed", stage_src="first_party", stage_cite=POST("introducing-supermaven"), stage_conf="high",
             entry_date="2024-09-16", country="US", city="San Francisco", focus="AI & Applied AI",
             rounds=[rnd("2024-09-16", "Seed", 12000000, BVP, True, POST("introducing-supermaven"), "firm")],
             note="acq. by Anysphere (Cursor), November 2024, two months after the $12M seed Bessemer led. "
                  "Graduation left for the graduation pass."))

L.append(cls("syndio", status="private", rng="below_1b",
             stage="Growth", stage_src="first_party", stage_cite=POST("syndio-is-solving"), stage_conf="high",
             city="Seattle", focus="SaaS",
             rounds=[rnd("2020-05-08", "earlier round", 7500000, None, False, None, "filing"),
                     rnd("2021-01-07", "Series B", 17000000, BVP, True, POST("syndio-is-solving"), "firm")],
             note="The firm's own post announces its Series B investment, the $17M round it led (Form D sale date "
                  "2020-12-28, announced 2021-01-07); a $50M round followed in 2021 with no $1B mark on record."))

L.append(cls("tackle-io", status="acquired", rng="below_1b",
             stage="Series A", stage_src="first_party", stage_cite=POST("backing-entrepreneurs-with-3-3b"),
             stage_conf="high", entry_date="2020", city="Boise", focus="SaaS", flags=["stage_disputes_band"],
             rounds=[rnd("2020-06-05", "Series A", 12946324, BVP, True, POST("backing-entrepreneurs-with-3-3b"), "firm")],
             note="acq. by AppDirect, December 2025 (the firm's listing). The firm's own post says Mike Droesch led "
                  "its Series A investment in Tackle.io; the Form D band read a 2017 filing that predates Bessemer "
                  "(partnered 2020), so the Pre-Seed label and its 2017 date are disputed."))

L.append(verdict("team8", "not_member",
                 "Fund-shaped entry (decisions.md D7): Team8 is a company-creation foundry that raises investment "
                 "vehicles from backers; Bessemer is named among the backers of its $85M second company-creation "
                 "vehicle. A position in the foundry is a position in a vehicle, not in an operating company; the "
                 "companies it built that Bessemer funds hold directly (Claroty) are their own rows.",
                 ec="web", conf="medium", cite=TEAM8_FUND))

L.append(verdict("teamviewer", "not_member",
                 "Control position (COLLECTION.md s1 control addendum, decisions.md D5): GFI Software's F-1 says "
                 "TeamViewer Holdings was formed in June 2009 at the direction of Insight funds and acquired a "
                 "controlling interest in TeamViewer, with Insight, Bessemer and Greenspring funds as its "
                 "shareholders; Bob Goodman joined the board in November 2009. The firm's 2009 investment was its "
                 "share of that buyout group, and its own BVP Forge post names TeamViewer as a growth buyout.",
                 ec="web", conf="high", cite=GFI_F1))

L.append(cls("teleport", status="private", rng="1b_plus", usd=1100000000, val_src="web_verified",
             val_cite=SIB("teleport", "insight-partners"), asof="2022-05-03",
             stage="Growth", stage_src="first_party", stage_cite=POST("investing-in-teleport"), stage_conf="high",
             entry_date="2022-05-03", country="US", city="Oakland", focus="Security",
             flags=["stale", "model_disputes_source"],
             rounds=[rnd("2022-05-03", "Series C", 110000000, BVP, True, POST("investing-in-teleport"), "firm")],
             note="The firm's own post announces Bessemer Growth leading the $110M Series C, which valued Teleport at "
                  "$1.1B (the company's own Series C post, as the Insight and Kleiner books; older than 24 months, "
                  "hence stale). The prefilled country AT is a wrong Wikidata join on the one-word name: the company "
                  "(fka Gravitational) is in Oakland, California."))

assert len(L) == 21, len(L)
jl.write("j06a", L)
