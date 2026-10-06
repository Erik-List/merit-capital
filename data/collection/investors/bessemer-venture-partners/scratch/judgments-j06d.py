"""PRO-80 Bessemer, judge j06, file d: batch 12, second half (turbineone to vayyar), plus the focus the sisense
line of file a left out. Run as NQ_TAG=j06 python3 judgments-j06d.py."""
import json

import judge_lib as jl
from judge_lib import ARCH, NEWS, POST, SITE, W, cls, rnd

SIBS = json.loads((jl.INV / "scratch" / "siblings.json").read_text())
BVP = "Bessemer Venture Partners"
CHECK = "Momentum check 2026-10-01 (Google News): "


def SIB(slug, investor):
    m = [x for x in SIBS.get(slug, []) if x["investor"] == investor and x.get("val_cite")]
    if len(m) != 1:
        raise SystemExit(f"SIB({slug!r}, {investor!r}) matched {len(m)}")
    return m[0]["val_cite"]


L = []

L.append(cls("sisense", focus="Data Infrastructure"))

T1 = POST("turbineone-on-a-mission")
L.append(cls("turbineone", status="private", rng="below_1b",
             stage="Series A", stage_src="first_party", stage_cite=T1, stage_conf="high", entry_date="2024-03-27",
             country="US", city="Chantilly", city_src="web_verified", focus="AI & Applied AI",
             rounds=[rnd("2024-03-27", "Series A", 15000000, BVP, True, T1, "firm"),
                     rnd("2025-05-14", "Series B", 36000000, None, None,
                         NEWS("turbineone", "Raises $36M Series B"), "press")],
             note="The firm's own post announces it leading the $15M Series A. The company said in May 2026 it was "
                  "moving its headquarters from San Francisco to Chantilly, Virginia (San Francisco Business Times). " +
                  CHECK + "a $36M Series B in May 2025, no $1B priced round."))

TUR = NEWS("turneo", "seed funding - businesscloud")
L.append(cls("turneo", status="private", rng="below_1b",
             stage="Seed", stage_src="web_verified", stage_cite=TUR, stage_conf="high", entry_date="2024-09-18",
             country="GB", country_src="web_verified", country_cite=TUR, city="London",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2024-09-18", "Seed", 2000000, BVP, True, TUR, "press")],
             note="BusinessCloud, 2024-09-18: London-based Turneo closed a GBP 1.7M (about $2M) seed round led by "
                  "Bessemer with Underline Ventures. No later round found. Graduation left for the graduation pass."))

TQ_A = NEWS("turquoise-health", "Investing in Turquoise Health")
L.append(cls("turquoise-health", status="private", rng="below_1b",
             stage="Seed", stage_src="model", stage_conf="low", entry_date="2021",
             grad="graduated", grad_src="web_verified", grad_cite=TQ_A, grad_conf="high",
             country="US", city="San Diego", focus="Healthcare & Bio", flags=["stage_uncited"],
             rounds=[rnd("2021", "Seed", 5000000, "Andreessen Horowitz", True, None, "press"),
                     rnd("2022-05-11", "Series A", 20000000, "Andreessen Horowitz", None, TQ_A, "press"),
                     rnd("2026-03-17", "Series C", 40000000, None, None,
                         NEWS("turquoise-health", "Announces $40 Million Series C"), "press")],
             note="Bessemer joined the 2021 seed round led by Andreessen Horowitz (named from knowledge; no page in "
                  "hand, hence stage_uncited). The later round is cited: a16z's own post of 2022-05-11 announces it "
                  "leading the Series A ($20M per MobiHealthNews), and a $40M Series C followed in March 2026 with no "
                  "$1B mark."))

TW_MEMO = POST("memos/twilio")
L.append(cls("twilio", stage="Seed", stage_src="first_party", stage_cite=TW_MEMO, stage_conf="high",
             entry_date="2009-11", grad="graduated", grad_src="web_verified", grad_cite=W("Twilio"), grad_conf="high",
             city="San Francisco", focus="DevTools & APIs",
             rounds=[rnd("2009-03", "Seed", 800000, "Founders Fund and Mitch Kapor", False, TW_MEMO, "firm"),
                     rnd("2009-11-06", "Seed extension", 125000, None, True, TW_MEMO, "firm"),
                     rnd("2009-12-18", "Series A", 3700000, "Union Square Ventures", None, W("Twilio"), "press"),
                     rnd("2010", "Series B", 12000000, BVP, True, W("Twilio"), "press")],
             note="The firm's own memo of 2009-11-06 (Twilio Seed Investment, $125,000) recommends joining an "
                  "extension to the $800,000 seed round, so the entry is the 2009 seed and the 2015 Form D date is "
                  "replaced. Union Square Ventures then led the $3.7M Series A and Bessemer the $12M Series B "
                  "(Wikipedia)."))

TW1 = POST("building-the-governed-context-layer")
L.append(cls("twin1", status="private", rng="below_1b",
             stage="Seed", stage_src="first_party", stage_cite=TW1, stage_conf="high", entry_date="2025",
             grad="censored", country="US", city="Foster City", focus="AI & Applied AI",
             rounds=[rnd("2026-08-20", "Seed", 20000000, "Bessemer, Tribeca Venture Partners and Aramco Ventures",
                         True, TW1, "firm")],
             note="The firm's own post announces it co-leading the $20M seed (announced 2026-08-20; the listing's "
                  "partnered year is 2025), inside the censoring window either way. City from the firm's listing "
                  "(Foster City; the company's release is datelined San Mateo). " + CHECK + "no round beyond the "
                  "seed."))

TWITCH = POST("memos/twitch")
L.append(cls("twitch", status="acquired", rng="below_1b",
             stage="Growth", stage_src="first_party", stage_cite=TWITCH, stage_conf="high", entry_date="2012-09-11",
             country="US", city="San Francisco", focus="Media, Gaming & Advertising",
             rounds=[rnd("2012-09-11", "Series B", None, BVP, True, TWITCH, "firm")],
             note="acq. by Amazon, 2014 (about $970M). The firm's own memo of 2012-07-07 (Twitch Series B IR) "
                  "recommends $13M at $53M pre-money to lead the Series B of the Justin.tv entity; the firm's "
                  "investment date is 2012-09-11. Same company as the row justin-tv-inc."))

UALA = SIB("ual", "ribbit-capital")
L.append(cls("ual", status="private", rng="1b_plus", usd=3200000000, val_src="web_verified", val_cite=UALA,
             asof="2026-03-04", stage="undetermined", entry_date="2017",
             country="AR", country_src="web_verified", country_cite=UALA, city="Buenos Aires",
             focus="Fintech & Payments", flags=["model_disputes_source"], rounds=[],
             note="Identified as Ualá, the Argentine digital bank (the live listing: founded 2017, partnered 2017, "
                  "Brian Feinstein); the first archived listing carried the description of Uala, an Italian beauty "
                  "booking marketplace later merged into Treatwell, which looks like a wrong text join, and so does "
                  "the prefilled acquired status. Private at $3.2B after the March 2026 round, as the Ribbit book. No "
                  "citable page names the 2017 round Bessemer joined (an investor database shows a seed), so the "
                  "stage is undetermined; Erik may want to confirm the identification."))

L.append(cls("ultrasolar-technology", status="private", rng="below_1b", city="Santa Clara",
             city_src="formd_address", focus="Climate & Energy", grad="graduated", grad_src="formd",
             note="Solar cell efficiency technology, Santa Clara. Last seen raising $9.0M on a Form D in April 2021, "
                  "which also decides the graduation against the $4.3M seed of October 2011; nothing in the press "
                  "since, so private is the last known state."))

UNF = NEWS("unframe-ai", "Noname Security founder launches")
L.append(cls("unframe-ai", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=UNF, stage_conf="medium", entry_date="2025",
             country="US", city="Cupertino", focus="AI & Applied AI",
             rounds=[rnd("2024", "Seed", 20000000, None, None, UNF, "press"),
                     rnd("2025-04-03", "Series A", 30000000, BVP, True, UNF, "press"),
                     rnd("2026-05-19", "Series B", 50000000, None, None,
                         NEWS("unframe-ai", "Series B after surpassing"), "press")],
             note="Calcalist, 2025-04-03: a $30M Series A led by Bessemer with TLV Partners, Craft and others, on top "
                  "of a previously undisclosed $20M seed whose investors are not named; the listing's partnered year "
                  "is 2025, so the entry is read as the Series A (medium: Bessemer may also have been in the seed). " +
                  CHECK + "a $50M Series B in May 2026, no $1B priced round."))

L.append(cls("united-capital", status="acquired", rng="below_1b", stage="undetermined", entry_date="2009",
             country="US", city="Newport Beach", focus="Fintech & Payments",
             rounds=[rnd("2013-10-22", "$30M stake by a new investor", 30000000, None, False,
                         NEWS("united-capital", "Ex-KKR"), "press")],
             note="acq. by Goldman Sachs, 2019 ($750M). A wealth advisory platform; the firm's fintech post says it "
                  "invested in 2009 and names no round, and the news query found none, so the stage is undetermined."))

UNITO = POST("unito-series-a")
L.append(cls("unito", status="private", rng="below_1b",
             stage="Series A", stage_src="first_party", stage_cite=UNITO, stage_conf="high", entry_date="2019",
             country="CA", country_src="web_verified", country_cite="https://unito.io/about/", city="Montreal",
             focus="SaaS",
             rounds=[rnd("2020-01-22", "Series A", 10500000, BVP, True, UNITO, "firm")],
             note="The firm's own post (Our Series A investment in Unito, 2020-01-22) announces it leading the $10.5M "
                  "Series A; the listing's partnered year is 2019. Montreal per the press quoted on the company's own "
                  "about page. No later round found."))

UNI = NEWS("uniuni", "secures additional $42.2 million")
L.append(cls("uniuni", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=UNI, stage_conf="high", entry_date="2024-11-15",
             country="CA", country_src="web_verified", country_cite=UNI, city="Richmond",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2024-11-15", "Series C2", 30000000, BVP, True, UNI, "press"),
                     rnd("2025-07-02", "Series D", 70000000, None, None,
                         NEWS("uniuni", "Series D round"), "press")],
             note="BetaKit, 2024-11-15: Richmond, BC-based UniUni raised a $30M Series C2 led by Bessemer, a new "
                  "investor (closed about a month earlier). A $70M Series D (2025) and an $85M round (2026) followed, "
                  "with no $1B mark reported."))

UNR = NEWS("unrivaled-basketball", "HEADLINED BY BESSEMER")
L.append(cls("unrivaled-basketball", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=UNR, stage_conf="high", entry_date="2025-09-08",
             country="US", city="Miami", focus="Media, Gaming & Advertising",
             rounds=[rnd("2024-12", "Series A", None, None, False, W("Unrivaled (basketball)"), "press"),
                     rnd("2025-09-08", "Series B", None, BVP, True, UNR, "press")],
             note="The league's own release, Miami, 2025-09-08: an oversubscribed Series B led by Bessemer, lifting the "
                  "valuation to $340M, after the 2024 seed and Series A."))

UPS = SIB("upside", "general-catalyst")
L.append(cls("upside", status="private", rng="1b_plus", usd=1500000000, val_src="web_verified", val_cite=UPS,
             asof="2022-04-26", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2020",
             country="US", city="Washington", focus="Consumer & Marketplaces",
             flags=["stale", "model_disputes_source"],
             rounds=[rnd("2020", "Series C", None, None, True, None, "press"),
                     rnd("2022-04-26", "Series D", 165000000, "General Catalyst", True, UPS, "press")],
             note="Upside (fka GetUpside), the cash-back app in Washington, DC, operates; the prefilled defunct is a "
                  "wrong name join (as the General Catalyst book found). SiliconANGLE, 2022-04-26: the $165M Series D "
                  "brought the valuation to $1.5B, with existing investor Bessemer participating (older than 24 "
                  "months, hence stale). Bessemer entered in 2020 at the round before it, the Series C (named from "
                  "knowledge), after the company's Series A and B."))

UPV = NEWS("upvest", "Bessemer-led round")
L.append(cls("upvest", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=UPV, stage_conf="high", entry_date="2022-06-16",
             country="DE", country_src="web_verified", country_cite=UPV, city="Berlin", focus="Fintech & Payments",
             rounds=[rnd("2022-06-16", "Series B", 42000000, BVP, True, UPV, "press"),
                     rnd("2024-12-11", "Series C", 105000000, None, None,
                         NEWS("upvest", "raises $105M"), "press")],
             note="Tech.eu, 2022-06-16: Berlin-based Upvest raised a $42M Series B led by Bessemer. " + CHECK +
                  "the EUR 100M Series C of December 2024 carried no $1B valuation, as the HV and Speedinvest books."))

UPW = NEWS("upwind", "more than doubles valuation")
UPW_B = POST("securing-the-next-generation-of-cloud")
L.append(cls("upwind", status="private", rng="1b_plus", usd=3800000000, val_src="web_verified", val_cite=UPW,
             asof="2026-09-02", stage="Growth", stage_src="first_party", stage_cite=UPW_B, stage_conf="high",
             entry_date="2026-01-26", country="IL", country_src="web_verified", country_cite=UPW, city="Tel Aviv",
             focus="Security",
             rounds=[rnd("2026-01-26", "Series B", 250000000, BVP, True, UPW_B, "firm"),
                     rnd("2026-09-02", "round led by Bessemer and TCV", 300000000, "Bessemer and TCV", True, UPW,
                         "press")],
             note="The firm's own post announces it leading the $250M Series B (January 2026, $1.5B). Calcalist, "
                  "2026-09-02: the Israeli cloud security company raised about $300M led by Bessemer and TCV at "
                  "roughly $3.8B. Country and city as the Greylock book, whose below_1b band is older than both "
                  "rounds and needs aligning."))

URB = W("Urban Company")
L.append(cls("urban-company", status="public", rng="1b_plus", usd=2521163151, val_src="web_verified",
             val_cite=SIB("urban-company", "tiger-global-management"), asof="2026-10-01",
             stage="Growth", stage_src="web_verified", stage_cite=URB, stage_conf="high", entry_date="2015-11-18",
             country="IN", country_src="web_verified", country_cite=SITE("urban-company"), city="Gurugram",
             focus="Consumer & Marketplaces", flags=["model_disputes_source"],
             rounds=[rnd("2015", "Series A", 10000000, "SAIF Partners and Accel", False, URB, "press"),
                     rnd("2015-11-18", "Series B", 25000000, BVP, True, URB, "press")],
             note="Listed on the NSE since September 2025 (the firm's listing), so the prefilled acquired is wrong; "
                  "market cap INR 242.86B @ ECB 2026-10-01 (INR/EUR 108.832, EUR/USD 1.1298) = $2.52B "
                  "(stockanalysis). Wikipedia: the $25M Series B was led by Bessemer with SAIF and Accel returning; "
                  "the date is the firm's own archived investment date. Same company as the row urbanclap."))

L.append(cls("us-health-partners-llc", status="private", rng="below_1b", stage="undetermined", entry_date="2021",
             country="US", city="Rockville", city_src="web_verified", focus="Healthcare & Bio", rounds=[],
             note="A cardiovascular care network of partner practices based in Rockville, Maryland (its own site), "
                  "formed in 2021 with Bessemer; a private equity tracker lists it as a practice-management platform "
                  "backed by Silversmith Capital. No source names the financing or its terms, so the stage is "
                  "undetermined and the nature of the position (a venture round or a sponsor-style platform) is open "
                  "for a later pass."))

VAL = POST("meet-nadia")
L.append(cls("valence", status="private", rng="below_1b",
             stage="Growth", stage_src="first_party", stage_cite=VAL, stage_conf="high", entry_date="2025-09-25",
             country="US", city="New York", city_src="web_verified", focus="AI & Applied AI",
             rounds=[rnd("2022", "Series A", 25000000, "Insight Partners", False, None, "press"),
                     rnd("2025-09-25", "Series B", 50000000, BVP, True, VAL, "firm")],
             note="The firm's own post announces it leading the $50M Series B. The company's Series B release is "
                  "datelined New York (September 2025); the Insight book carries Toronto, where the company began. "
                  "The YC row named Valence is another company. " + CHECK + "no $1B priced round."))

VAPI = POST("our-investment-in-vapi")
L.append(cls("vapi", status="private", rng="below_1b",
             stage="Series A", stage_src="first_party", stage_cite=VAPI, stage_conf="high",
             city="San Francisco", focus="AI & Applied AI",
             rounds=[rnd("2024-12-13", "Series A", 20000000, BVP, True, VAPI, "firm"),
                     rnd("2026-05-12", "Series B", 50000000, "Peak XV", None,
                         NEWS("vapi", "hits $500M valuation after winning Amazon Ring over 40 rivals - techcrunch"),
                         "press")],
             note="The firm's own post announces it leading the $20M Series A (Form D sale date 2024-10-03). " + CHECK +
                  "the $50M Series B of May 2026 valued Vapi at $500M (TechCrunch), below the $1B band."))

L.append(cls("vasona-networks", status="acquired", rng="below_1b", city="San Jose", focus="Data Infrastructure",
             note="acq. by ZephyrTel, 2018. Mobile network traffic management software; last headquarters San Jose "
                  "(the 2011 and 2013 Form Ds file from Santa Clara)."))

L.append(cls("vayyar", status="private", rng="below_1b", stage="undetermined", entry_date="2012",
             country="IL", country_src="web_verified", country_cite=SITE("vayyar"), city="Yehud",
             focus="Industrial & Robotics",
             rounds=[rnd("2012-05", "Seed", None, None, None, W("Vayyar"), "press"),
                     rnd("2017-12-13", "Series C", 45000000, None, None, NEWS("vayyar", "Closes $45m Series C"), "press"),
                     rnd("2022-06-06", "Series E", 108000000, "Koch Disruptive Technologies", True,
                         NEWS("vayyar", "Series E at over $1 billion"), "press")],
             note="Israel confirmed (the firm's Israel list; city as the Battery book). The company closed its seed "
                  "round in May 2012, the firm's partnered year, but no page ties Bessemer to that round by name, so "
                  "the stage is undetermined. The 2022 Series E named existing investor Bessemer; its valuation was "
                  "an estimate (over $1B, not disclosed), so the band stays below_1b as in the Battery book."))

assert len(L) == 23, len(L)
jl.write("j06d", L)
