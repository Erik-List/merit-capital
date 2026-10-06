"""PRO-80 Bessemer, judge j04, file d: batch 8 rows okera .. parallels (22 rows)."""
import json
import os

os.environ.setdefault("NQ_TAG", "j04")
import judge_lib as jl
from judge_lib import cls, verdict, rnd, POST, SITE, ARCH, W, NEWS

_SIB = json.loads((jl.INV / "scratch" / "siblings.json").read_text())


def SIB(slug, investor):
    m = [x for x in _SIB.get(slug, []) if x["investor"] == investor and x.get("val_cite")]
    if len(m) != 1:
        raise SystemExit(f"SIB({slug!r}, {investor!r}) matched {len(m)}")
    return m[0]["val_cite"]


# found with WebSearch and read with WebFetch on 2026-10-01
ONQ_SERIES_A = "https://www.biospace.com/cancer-diagnostics-company-b-on-q-ity-b-raises-21m-in-series-a-funding-for-the-development-of-technologies-to-personalize-cancer-therapy"

ola_tfs = NEWS("ola", "Ola acquires TaxiForSure in $200-mn deal")
olx_tc = NEWS("olx", "Craigslist Competitor OLX Raises $13.5M")
oms_2014 = NEWS("omsignal", "Smart' Shirt Maker OMSignal Raises $10 Million")
oms_2016 = NEWS("omsignal", "OMsignal announces $13 million")
onaroll_acq = NEWS("onaroll", "Array Acquires Onaroll")
onx_2018 = NEWS("onxmaps", "onX Closes $20.3 Million Growth Equity")
onyx_globes = NEWS("onyx-security", "Israeli AI security co Onyx Security raises $113m")
oper_a = NEWS("oper", "Oper Credits lands")
optibus_val = SIB("optibus", "insight-partners")
od_c = NEWS("optimal-dynamics", "Optimal Dynamics Raises $40M Series C to Scale the Decision Layer of Logistics - Newswire")
oto_a = NEWS("otonomo", "connected car startup Otonomo raises $12 million")
oto_merge = NEWS("otonomo", "Successful Closing of Merger With Otonomo")
ppay_b = NEWS("papaya-pay", "Papaya raises $50M Series B")
para_seed = NEWS("paraglide", "Seed Investment co-led by Bessemer Venture Partners and DN Capital")
okera_acq = NEWS("okera", "Databricks acquires AI-centric data governance platform Okera")

lines = [
    cls("okera", status="acquired", rng="below_1b",
        stage="Series A", stage_src="model", stage_conf="medium", entry_date="2017-11-13",
        country="US", city="San Francisco", focus="Data Infrastructure",
        rounds=[rnd("2017-11-13", "Series A", 12000000, "Bessemer Venture Partners", True, None, "press"),
                rnd("2023-05-03", "acquisition by Databricks", None, None, None, okera_acq, "press")],
        note="Okera, data access governance, San Francisco; acq. by Databricks, May 2023 (TechCrunch). Bessemer led the $12M "
             "Series A that followed Felicis's seed, announced in 2018 (named from knowledge; the Felicis book cites the "
             "TechCrunch report of the $12M); the firm's archive dates its investment to 2017-11-13."),

    verdict("ola", "not_member",
            "Sale consideration: Bessemer backed TaxiForSure (a separate row, 2014), which Ola bought in March 2015 in a "
            "$200M cash-and-stock deal; the firm's listing gives Ola the TaxiForSure year (2014) and names no deal partner, "
            "and no Bessemer round in Ola was found. Stock received for a portfolio company is not membership "
            "(Erik 2026-09-22)",
            ec="web", conf="medium", cite=ola_tfs),

    cls("olx", status="acquired", rng="below_1b",
        stage="Series A", stage_src="web_verified", stage_cite=olx_tc, stage_conf="high", entry_date="2006-09-19",
        country="US", city="New York", focus="Consumer & Marketplaces",
        rounds=[rnd("2006-09", "Series A", 10000000, None, True, olx_tc, "press"),
                rnd("2008-04-11", "Series B", 13500000, None, True, olx_tc, "press")],
        note="OLX, online classifieds for markets outside the US, run from New York and Buenos Aires (New York as in the "
             "General Catalyst book); bought by Naspers, 2010. TechCrunch (2008-04-11): the Series B came 'from General "
             "Catalyst, Bessemer Venture Partners, Founders Fund, and DN Capital', after 'a previously undisclosed Series A "
             "round of $10M in September 2006 with the same VCs'; the firm's archive dates its investment to 2006-09-19."),

    cls("omgpop", status="acquired", rng="below_1b", city="New York", focus="Media, Gaming & Advertising",
        stage="undetermined", entry_date="2009-03-05",
        rounds=[rnd("2010-11-12", "Series B-1 (Form D)", 10600000, None, True, jl.FORMD_CITE("omgpop", 0), "filing")],
        note="OMGPOP (formerly iminlikewithyou), social games, New York; acq. by Zynga, March 2012. The firm's archive dates "
             "its investment to March 2009, between the $1.5M round of 2008 and the Series B-1 of late 2010 that the Spark "
             "book records; no source read names the 2009 round, so undetermined, and the 2010 Form D date is replaced by "
             "the firm's own."),

    cls("omsignal", status="acquired", rng="below_1b", city="Montreal", focus="Consumer & Marketplaces",
        stage="Series A", stage_src="model", stage_conf="medium",
        rounds=[rnd("2014-06-24", "Series A", 10000000, "Bessemer Venture Partners", True, oms_2014, "press"),
                rnd("2016-09-19", "unnamed", 10000000, "Relay Ventures", True, oms_2016, "press")],
        note="OMsignal, biometric smart clothing, Montreal. Bessemer led the $10M Series A of June 2014 (the WSJ headline "
             "gives the amount; the round name is from knowledge) and joined the 2016 round led by Relay (BetaKit). "
             "omsignal.com redirected to Hexoskin's store on 2026-10-01: read as an asset sale to Hexoskin's maker, no "
             "announcement found."),

    cls("on-q-ity", status="defunct", rng="below_1b", city="Waltham", focus="Healthcare & Bio",
        stage="Series A", stage_src="web_verified", stage_cite=ONQ_SERIES_A, stage_conf="high", entry_date="2009-10-22",
        rounds=[rnd("2009-11-03", "Series A", 21000000, "Mohr Davidow Ventures", True, ONQ_SERIES_A, "company"),
                rnd("2012-02-14", "unnamed (Form D)", 6533458, None, True, jl.FORMD_CITE("on-q-ity", 0), "filing")],
        note="On-Q-ity, cancer diagnostics, Waltham. Its launch release (2009-11-03): 'closed a $21 million series A "
             "financing. The funding was led by MDV-Mohr Davidow Ventures and included Bessemer Venture Partners'; the "
             "firm's archive dates its investment to 2009-10-22, which replaces the 2012 Form D date. The board wound the "
             "company down in November 2012 and sold the remaining patents (Atlas Venture's Bruce Booth, LifeSciVC, April "
             "2013): defunct."),

    cls("onaroll", status="acquired", rng="below_1b",
        stage="undetermined", entry_date="2021",
        country="US", city="New York", focus="SaaS", rounds=[],
        note="Onaroll, rewards and engagement for shift workers, New York; acq. by Array, announced 2025-10-28 (citybiz), as "
             "the Coatue book reads it (the Lux row still reads private). The firm's year is 2021; no source read names "
             "the round."),

    cls("onxmaps", status="private", rng="below_1b",
        stage="Growth", stage_src="web_verified", stage_cite=onx_2018, stage_conf="high", entry_date="2018-02-15",
        country="US", city="Missoula", focus="Consumer & Marketplaces",
        rounds=[rnd("2018-02-15", "growth equity round", 20300000, "Summit Partners", True, onx_2018, "press")],
        note="onX, mapping apps for hunters and outdoor recreation, Missoula. Summit Partners' release (2018-02-15): a $20.3M "
             "growth equity investment led by Summit; 'Additional investors include Bessemer Venture Partners'. Summit led "
             "a further $87M in 2024 with no valuation disclosed."),

    cls("onyx-security", status="private", rng="below_1b",
        stage="Growth", stage_src="first_party", stage_cite=POST("onyx-security-defining-cybersecurity"),
        stage_conf="high", entry_date="2026-07-30",
        country="IL", country_src="web_verified", country_cite=onyx_globes, city="Tel Aviv", focus="Security",
        rounds=[rnd("2026-07-29", "Series B", 113000000, "Bessemer Venture Partners", True,
                    POST("onyx-security-defining-cybersecurity"), "firm")],
        note="Onyx Security, control plane for enterprise AI agents, Tel Aviv as in the TCV book (Globes: 'Israeli AI "
             "security co'; a New York office as well). The firm's own post: 'Bessemer Venture Partners leads Onyx's $113M "
             "Series B', four months after the company left stealth with $40M of seed and Series A money in which Bessemer "
             "is not named. No valuation disclosed."),

    cls("oper", status="private", rng="below_1b",
        stage="Series A", stage_src="web_verified", stage_cite=oper_a, stage_conf="medium", entry_date="2022-07-12",
        country="BE", country_src="web_verified", country_cite=oper_a, city="Antwerp", focus="Fintech & Payments",
        rounds=[rnd("2022-07-12", "Series A", None, "Bessemer Venture Partners and ABN AMRO Ventures", True, oper_a,
                    "press")],
        note="Oper Credits, mortgage software for lenders, Antwerp ('Belgian-Swiss' in Tech.eu). Tech.eu (2022-07-12): EUR 11 "
             "million 'in Series A funding ... led by Bessemer Venture Partners and ABN Amro Ventures with existing "
             "shareholders, including Techstars, Pitchdrive and Verve Ventures'. The firm's listing year is 2020, two years "
             "earlier and unexplained by any source read; reported as an open point."),

    cls("optibus", status="private", rng="1b_plus", usd=1300000000, val_src="web_verified", val_cite=optibus_val,
        asof="2022-05-16", flags=["stale"],
        stage="Growth", stage_src="first_party", stage_cite=POST("the-future-of-smart-cities-begins"), stage_conf="high",
        entry_date="2021-03-10",
        country="IL", country_src="web_verified", country_cite=SITE("optibus"), city="Tel Aviv", focus="SaaS",
        rounds=[rnd("2021-03-10", "Series C", 107000000, "Bessemer Venture Partners", True,
                    POST("the-future-of-smart-cities-begins"), "firm"),
                rnd("2022-05-16", "Series D", 100000000, None, None, optibus_val, "company")],
        note="Optibus, planning and scheduling software for public transport, Tel Aviv (the firm lists it under its Israel "
             "office). The firm's own post: 'Bessemer Venture Partners leads Optibus' $107 million Series C' (2021-03-10). "
             "The Series D of May 2022 brought 'its valuation to $1.3 billion' (the company's release, as the Insight book "
             "cites); no later priced round found, stale."),

    cls("optimal-dynamics", status="private", rng="below_1b", city="New York", focus="AI & Applied AI",
        stage="Series A", stage_src="model", stage_conf="medium", entry_date="2021-04-09",
        flags=["stage_disputes_band"],
        rounds=[rnd("2020-05-01", "seed", 4395000, None, False, jl.FORMD_CITE("optimal-dynamics", 2), "filing"),
                rnd("2021-04-09", "Series A", 17357347, "Bessemer Venture Partners", True,
                    jl.FORMD_CITE("optimal-dynamics", 1), "filing"),
                rnd("2022-03-25", "Series B", 33000003, "Koch Disruptive Technologies", True,
                    jl.FORMD_CITE("optimal-dynamics", 0), "filing"),
                rnd("2025-05-12", "Series C", 40000000, "Koch Disruptive Technologies", True, od_c, "company")],
        note="Optimal Dynamics, decision automation for trucking, New York. Bessemer led the Series A of spring 2021 (named "
             "from knowledge; the April 2021 Form D of $17.4M is that round, the firm's listing year is 2021 and its "
             "December 2021 research post already calls it 'Our company'). The Growth band was anchored on the 2022 filing "
             "that first names Mike Droesch and is disputed. Momentum check 2026-10-01: Series C of $40M in 2025, no priced "
             "round at $1B or more."),

    cls("oshi-health", status="private", rng="below_1b",
        stage="Series A", stage_src="model", stage_conf="medium", entry_date="2021",
        country="US", city="New York", focus="Healthcare & Bio",
        rounds=[rnd("2021-10", "Series A", 23000000, None, True, None, "press"),
                rnd("2024-10-16", "Series C", 60000000, None, None,
                    NEWS("oshi-health", "Virtual Gastrointestinal Company Raises $60 Million (Series C)"), "press")],
        note="Oshi Health, virtual gastrointestinal care, New York. Bessemer joined at the $23M Series A of October 2021 "
             "with Flare Capital and Frist Cressey (named from knowledge; no page naming the round was read), the firm's "
             "listing year. Later rounds: $30M in 2023 and a $60M Series C in 2024, no valuation disclosed."),

    cls("otonomo", status="acquired", rng="below_1b",
        stage="Series A", stage_src="web_verified", stage_cite=oto_a, stage_conf="high", entry_date="2015-12-14",
        country="IL", country_src="web_verified", country_cite=oto_a, city="Herzliya", focus="Data Infrastructure",
        rounds=[rnd("2016-11-01", "Series A", 12000000, "Bessemer Venture Partners and StageOne Ventures", True, oto_a,
                    "press"),
                rnd("2023-10-19", "merger into Urgently", None, None, None, oto_merge, "company")],
        note="Otonomo, automotive data platform, Herzliya (VentureBeat: established in Tel Aviv in 2015; the Wikidata IL is "
             "confirmed). 'Otonomo has closed a $12 million series A round, led by Bessemer Venture Partners and Stageone "
             "Ventures' (VentureBeat, 2016-11-01); the entry date is the firm's own investment date. Listed through a SPAC "
             "in 2021, then merged into Urgently, closed 2023-10-19 (Urgently's release): acquired."),

    cls("ovascience", status="acquired", rng="below_1b", city="Waltham", focus="Healthcare & Bio",
        stage="Series A", stage_src="first_party", stage_cite=POST("our-deep-health-seed-program"), stage_conf="high",
        entry_date="2011-07-14", flags=["stage_disputes_band", "model_disputes_source"],
        rounds=[rnd("2011-07-14", "Series A", 6000000, "Longwood Fund and Bessemer Venture Partners", True,
                    W("OvaScience"), "press"),
                rnd("2012-03-29", "Series B", 37238097, None, True, W("OvaScience"), "press")],
        note="OvaScience, fertility treatments, Waltham. The firm's own post: 'We led the Series A of ... OvaScience'; "
             "Wikipedia gives a $6M Series A from Longwood and Bessemer before the $37M Series B of early 2012, and the "
             "firm's archive dates its investment to July 2011, so the Growth band (the 2012 filing) is disputed. OvaScience "
             "merged into Millendo Therapeutics in a 2018 reverse merger and the registrant is now Tempest Therapeutics, so "
             "the prefilled public status and float belong to the successor: acquired, as in the General Catalyst book."),

    cls("p-com", rng="below_1b", country="US", city="Campbell", focus="Data Infrastructure",
        stage="undetermined", entry_date="1992", rounds=[],
        note="P-Com, microwave radio links for carriers, Campbell CA; IPO 1995, later Wave Wireless, whose product lines were "
             "sold off in 2006 and 2007 (Wikipedia). The firm's list gives 1992 and 1993; no source names the round."),

    cls("pagerduty", city="San Francisco", focus="DevTools & APIs",
        stage="Growth", stage_src="first_party", stage_cite=POST("memos/pagerduty"), stage_conf="high",
        entry_date="2014-07-29",
        rounds=[rnd("2014-07-29", "Series B", 27200000, "Bessemer Venture Partners", True, POST("memos/pagerduty"),
                    "firm")],
        note="PagerDuty, incident management, San Francisco (NYSE: PD). The firm's own memo of July 2014: 'we signed a term "
             "sheet to lead the company's Series B with an investment of $19.6m out of a $27.2m round'; its archive dates "
             "the investment to 2014-07-29, which replaces the 2017 Form D date. The stage agrees with the band."),

    cls("pana", status="acquired", rng="below_1b", city="Denver", focus="SaaS",
        stage="Series A", stage_src="first_party", stage_cite=POST("bessemer-series-a-investment-pana"), stage_conf="high",
        rounds=[rnd("2019-03-15", "Series A", 10000000, "Bessemer Venture Partners", True,
                    POST("bessemer-series-a-investment-pana"), "firm")],
        note="Pana, corporate guest travel platform, Denver; acq. by Coupa, 2021 (the firm's listing). The firm's own post: "
             "'Bessemer's $10 million series A financing in Pana' (2019-04-23), the round the March 2019 Form D records. "
             "The Y Combinator row named Pana is a different company."),

    cls("papaya-global", country="US", city="New York", focus="Fintech & Payments",
        flags=["model_disputes_source"],
        stage="Series A", stage_src="web_verified", stage_cite=W("Papaya Global"), stage_conf="high",
        entry_date="2019-11",
        rounds=[rnd("2019-11", "Series A", 45000000, "Insight Partners and Bessemer Venture Partners", True,
                    W("Papaya Global"), "press"),
                rnd("2021-09", "Series D", 250000000, "Insight Partners and Tiger Global", None,
                    SIB("papaya-global", "ivp"), "company")],
        note="Papaya Global, global payroll and workforce payments, founded in Israel and 'headquartered in New York City' "
             "(Wikipedia; the IVP and Tiger books agree, the Insight row reads Tel Aviv); the prefilled country string was "
             "not a code. Wikipedia: 'In November 2019, the company raised $45 million in a Series A funding round led by "
             "Insight Partners and Bessemer Venture Partners'."),

    cls("papaya-pay", status="private", rng="below_1b",
        stage="Growth", stage_src="web_verified", stage_cite=ppay_b, stage_conf="high", entry_date="2021-12-15",
        country="US", city="Los Angeles", focus="Fintech & Payments",
        rounds=[rnd("2021-12-15", "Series B", 50000000, "Bessemer Venture Partners", True, ppay_b, "press")],
        note="Papaya, mobile bill payment app, Los Angeles. 'Papaya ... announced raising a $50 million Series B funding "
             "round led by Bessemer Venture Partners' (HousingWire's FinLedger, 2021-12-15); Sequoia led the Series A of "
             "2018. Momentum check 2026-10-01 (Google News): no later priced round found."),

    cls("paraglide", status="private", rng="below_1b",
        stage="Seed", stage_src="web_verified", stage_cite=para_seed, stage_conf="high", entry_date="2026-01-27",
        grad="censored",
        country="GB", country_src="web_verified", country_cite=W("Paraglide (company)"), city="London",
        focus="AI & Applied AI",
        rounds=[rnd("2026-01-27", "Seed", 5000000, "Bessemer Venture Partners and DN Capital", True, para_seed, "press")],
        note="Paraglide, AI agents for accounts receivable; 'headquartered in London, United Kingdom, with its technology "
             "team based in Malmo, Sweden' (Wikipedia). 'Paraglide secures GBP 3.6 million Seed Investment co-led by "
             "Bessemer Venture Partners and DN Capital' (UK Tech News, 2026-01-27; Wikipedia dates the raise to summer "
             "2025). Inside the 24-month window: censored. Momentum check 2026-10-01: nothing beyond the seed."),

    cls("parallels", status="acquired", rng="below_1b", city="Bellevue", focus="Data Infrastructure",
        stage="undetermined", entry_date="2005-06-03", rounds=[],
        note="Parallels (formerly SWsoft), virtualisation and hosting automation software, Bellevue as in the Insight book; "
             "acq. by Corel, December 2018 (Wikipedia). The firm's archive dates its investment to June 2005, made with "
             "Insight and Intel Capital; the round is not named on record."),
]

jl.write("j04d", lines)
