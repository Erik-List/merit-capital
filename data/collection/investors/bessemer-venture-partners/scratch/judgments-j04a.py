"""PRO-80 Bessemer, judge j04, file a: batch 7 rows leena-ai .. manychat (23 rows)."""
import json
import os

os.environ.setdefault("NQ_TAG", "j04")
import judge_lib as jl
from judge_lib import cls, verdict, rnd, POST, SITE, ARCH, W, NEWS

_SIB = json.loads((jl.INV / "scratch" / "siblings.json").read_text())
_FTS = json.loads((jl.INV / "sources/edgar/fts-hits.json").read_text())["registrants"]


def SIB(slug, investor):
    """The valuation citation a sibling book carries for the same company (read from scratch/siblings.json)."""
    m = [x for x in _SIB.get(slug, []) if x["investor"] == investor and x.get("val_cite")]
    if len(m) != 1:
        raise SystemExit(f"SIB({slug!r}, {investor!r}) matched {len(m)}")
    return m[0]["val_cite"]


def FTSURL(sub):
    """The one full-text-hit document URL containing `sub` (read from sources/edgar/fts-hits.json)."""
    m = {f["url"] for r in _FTS for f in r.get("filings", []) if sub in f["url"]}
    if len(m) != 1:
        raise SystemExit(f"FTSURL({sub!r}) matched {len(m)}")
    return m.pop()


# URLs found with WebSearch and read with WebFetch on 2026-10-01
LIVEAUCTIONEERS_PR = "https://www.prnewswire.com/news-releases/liveauctioneers-announces-476m-round-of-funding-led-by-bessemer-venture-partners-283179111.html"

leena_b = NEWS("leena-ai", "Announces $30M Series B round led by Bessemer")
legit_a = NEWS("legit-security", "raises $26.5 million Series A")
legora_val = SIB("legora", "bain-capital-ventures")
lithic_b = NEWS("lithic", "Series B Funding Round Led By Bessemer")
litify_ctl = NEWS("litify", "Acquires Majority Stake in Litify as Legal Tech")
livspace_val = NEWS("livspace", "at $1.2 billion valuation")
loveseat_a = NEWS("loveseat", "Loveseat Lands $7M")
luma_a = NEWS("lumachain", "Raises US$19.5M in Series A Funding Led by Bessemer")
mambu_val = SIB("mambu", "tcv")
mambu_2019 = NEWS("mambu", "Scores $34 Million in Funding")
manychat_2025 = NEWS("manychat", "Manychat Raises $140M Led by Summit Partners")
manychat_tc = NEWS("manychat", "Manychat taps $140M")
lp_c = NEWS("luxury-presence", "Luxury Presence Raises $22M Series C")
lp_b1 = NEWS("luxury-presence", "raises $19.2M")

lines = [
    cls("leena-ai", status="private", rng="below_1b",
        stage="Growth", stage_src="web_verified", stage_cite=leena_b, stage_conf="high", entry_date="2021-09-28",
        country="US", city="New York", focus="AI & Applied AI",
        rounds=[rnd("2021-09-28", "Series B", 30000000, "Bessemer Venture Partners", True, leena_b, "company")],
        note="Leena AI, HR assistant for enterprises. Bessemer led the $30M Series B of September 2021 (the company's release), "
             "its first round in the company; the firm's own post of the same day names no round. New York as in the Y Combinator book. "
             "Momentum check 2026-10-01 (Google News): no priced round at $1B or more."),

    cls("legit-security", status="private", rng="below_1b",
        stage="Series A", stage_src="web_verified", stage_cite=legit_a, stage_conf="high", entry_date="2022-02-10",
        country="IL", country_src="web_verified", country_cite=legit_a, city="Tel Aviv", focus="Security",
        rounds=[rnd("2022-02-10", "Series A", 26500000, "Bessemer Venture Partners and TCV", True, legit_a, "press"),
                rnd("2023-09-20", "Series B", 40000000, "CRV", None,
                    NEWS("legit-security", "Secures $40 Million Series B Investment Led by CRV"), "company")],
        note="Legit Security, software supply chain security. Bessemer and TCV led the $26.5M Series A announced in February 2022 "
             "(Calcalist, which calls it an Israeli startup); the seed came from Cyberstarts. The firm's listing year is 2021, the close. "
             "Tel Aviv as in the TCV book."),

    cls("legora", status="private", rng="1b_plus", usd=5550000000, val_src="web_verified", val_cite=legora_val,
        asof="2026-03-10",
        stage="Growth", stage_src="first_party", stage_cite=POST("building-legoras-collaborative"), stage_conf="high",
        entry_date="2025-10-30",
        country="SE", country_src="web_verified", country_cite=legora_val, city="Stockholm", focus="AI & Applied AI",
        rounds=[rnd("2025-10-30", "Series C", 150000000, "Bessemer Venture Partners", True,
                    POST("building-legoras-collaborative"), "firm"),
                rnd("2026-03-10", "Series D", 550000000, "Accel", None, legora_val, "press")],
        note="Legora, AI platform for lawyers, Stockholm (Crunchbase News: 'the Swedish company'); the Wikidata country is confirmed. "
             "Bessemer led the $150M Series C of October 2025 (the firm's post). The $550M Series D of March 2026 valued it at "
             "$5.55 billion (Crunchbase News), the mark the sibling books carry."),

    cls("lentra", status="private", rng="below_1b",
        stage="undetermined", entry_date="2019",
        country="IN", country_src="web_verified", country_cite=POST("lentra-s-60-million-series-b"), city="Pune",
        focus="Fintech & Payments",
        rounds=[rnd("2022-11-10", "Series B", 60000000, "Bessemer Venture Partners, SIG and Citi Ventures", True,
                    POST("lentra-s-60-million-series-b"), "firm")],
        note="Lentra, lending cloud for banks, Pune. The firm's Series B post of 2022 calls itself an early investor in "
             "'the India-based company' and its listing gives 2019, but no source read names the 2019 round, so the stage is "
             "undetermined. The 2022 Series B was reported at about $400M, below $1B."),

    cls("liazon", status="acquired", rng="below_1b",
        stage="undetermined", entry_date="2012-04-11",
        country="US", city="Buffalo", focus="Healthcare & Bio", rounds=[],
        note="Liazon, private benefits exchange, Buffalo; acq. by Towers Watson, 2013 (the firm's listing). The firm's own "
             "investment date is April 2012; no source found names that round (Google News, 2026-10-01)."),

    cls("life360", stage="undetermined", entry_date="2011-10-24",
        country="US", city="San Mateo", focus="Consumer & Marketplaces", rounds=[],
        note="Life360, family location app, San Mateo (ASX and Nasdaq listed). The firm's post says it first invested in 2011 "
             "and its archive dates the investment to October 2011, but neither names the round and no press source read does."),

    cls("lifelock", rng="below_1b", city="Tempe", focus="Security",
        stage="Series A", stage_src="first_party", stage_cite=POST("memos/lifelock"), stage_conf="high",
        entry_date="2006-11-20", flags=["stage_disputes_band"],
        rounds=[rnd("2006-11-20", "Series A", None, "Bessemer Venture Partners", True, POST("memos/lifelock"), "firm")],
        note="LifeLock, identity theft protection, Tempe; acq. by Symantec, 2017, after its 2012 IPO. The firm's own memo of "
             "September 2006 recommends leading the Series A, and its archive dates the investment to November 2006; the Form D "
             "band read a 2009 follow-on as the entry, which the memo disputes."),

    cls("linkedin", rng="below_1b", country="US", city="Sunnyvale", focus="Consumer & Marketplaces",
        stage="Growth", stage_src="first_party", stage_cite=POST("memos/linkedin"), stage_conf="high",
        entry_date="2006-12-29",
        rounds=[rnd("2006-12-29", "Series C", 12500000, "Bessemer Venture Partners", True, POST("memos/linkedin"), "firm")],
        note="LinkedIn; acq. by Microsoft, 2016, after its 2011 IPO. The firm's own memo of December 2006 recommends leading "
             "the Series C ('We will be the only Series C investor'), and its archive dates the investment to 2006-12-29."),

    cls("lithic", status="private", rng="below_1b",
        stage="Growth", stage_src="web_verified", stage_cite=lithic_b, stage_conf="medium", entry_date="2021-05-20",
        country="US", city="New York", focus="Fintech & Payments",
        rounds=[rnd("2021-05-20", "Series B", 43000000, "Bessemer Venture Partners", True, lithic_b, "press")],
        note="Lithic (formerly Privacy.com), card issuing platform, New York. Bessemer led the $43M Series B announced in May "
             "2021 (Crowdfund Insider); the firm's listing year is 2020, read as that round's close, and no earlier Bessemer "
             "round was found. The Series C of 2021 was reported at $800M, below $1B."),

    verdict("litify", "not_member",
            "Control position: Bessemer acquired a majority stake in Litify in February 2023 (the company's own release, "
            "'Bessemer Venture Partners Acquires Majority Stake in Litify'); a control acquisition is not a venture round "
            "(COLLECTION.md s1 control positions, decisions.md D5)",
            ec="web", conf="high", cite=litify_ctl),

    cls("liveauctioneers", status="acquired", rng="below_1b",
        stage="Growth", stage_src="first_party", stage_cite=POST("introducing-bvp-forge"), stage_conf="medium",
        entry_date="2014-10-03",
        country="US", city="New York", focus="Consumer & Marketplaces",
        rounds=[rnd("2014-11-19", "unnamed (first outside funding)", 47600000, "Bessemer Venture Partners", True,
                    LIVEAUCTIONEERS_PR, "company")],
        note="LiveAuctioneers, online auction marketplace, New York; acq. by Auction Technology Group, 2021 (Cove Hill bought a "
             "majority in 2019). Bessemer led its first outside funding, $47.6M, announced in November 2014; the firm's own "
             "Forge post lists it among companies that fit 'a growth buyout investment structure', read as Growth. The release "
             "does not say whether the stake was a majority, so the control question stays open for a ruling."),

    cls("livspace", status="private", rng="1b_plus", usd=1200000000, val_src="web_verified", val_cite=livspace_val,
        asof="2022-02-08", flags=["stale"],
        stage="Series A", stage_src="web_verified", stage_cite=W("Livspace"), stage_conf="medium", entry_date="2014-12",
        country="SG", country_src="web_verified", country_cite=W("Livspace"), city="Singapore",
        focus="Consumer & Marketplaces",
        rounds=[rnd("2014-12", "Series A", 4600000, None, True, W("Livspace"), "press"),
                rnd("2016-08", "Series B", 15000000, "Bessemer Venture Partners", True, W("Livspace"), "press"),
                rnd("2022-02-08", "Series F", 180000000, "KKR", None, livspace_val, "press")],
        note="Livspace, home interiors platform serving India and Southeast Asia, headquartered in Singapore (Wikipedia). "
             "Bessemer joined the $4.6M Series A of December 2014 with Helion and Jungle (Wikipedia). KKR's $180M Series F of "
             "February 2022 valued it at $1.2 billion (Economic Times); no later priced round found, stale."),

    verdict("logicnow", "not_member",
            "Sale consideration: the position in GFI Software (later LogicNow) dates from the 2010 merger of Bessemer's "
            "portfolio company TeamViewer into GFI, in the firm's own archived description ('In 2010 GFI merged with BVP "
            "portfolio company Teamviewer'); stock received for a portfolio company is not membership, TeamViewer is the row "
            "(Erik 2026-09-22)",
            ec="site_listing", conf="medium", cite=ARCH("logicnow")),

    cls("loveseat", status="defunct", rng="below_1b", city="Austin", focus="Consumer & Marketplaces",
        stage="Series A", stage_src="web_verified", stage_cite=loveseat_a, stage_conf="high",
        flags=["stage_disputes_band"],
        rounds=[rnd("2021-12-20", "Series A", 7000000, "Bessemer Venture Partners", True, loveseat_a, "press")],
        note="Loveseat, online auctions for returned and overstock furniture, Austin. Built In Austin (2022-03-16): '$7 million "
             "in a Series A financing round led by Bessemer Venture Partners', the round the December 2021 Form D records, so "
             "the Seed band is disputed. The firm dropped the row after 2024 and loveseat.com read 'Loveseat Store Coming "
             "Soon' on 2026-10-01: read as shut down, no notice found."),

    cls("lumachain", status="private", rng="below_1b",
        stage="Series A", stage_src="web_verified", stage_cite=luma_a, stage_conf="high", entry_date="2022-08-25",
        country="AU", country_src="web_verified", country_cite=luma_a, city="Sydney", focus="AI & Applied AI",
        rounds=[rnd("2022-08-25", "Series A", 19500000, "Bessemer Venture Partners", True, luma_a, "company")],
        note="Lumachain, computer vision for meat and food processing, Sydney (the release is datelined Denver and Sydney and "
             "announces a first US office in Denver). Bessemer led the $19.5M Series A of August 2022. Momentum check "
             "2026-10-01 (Google News): no priced round at $1B or more."),

    cls("lumere", status="acquired", rng="below_1b",
        stage="undetermined", entry_date="2012",
        country="US", city="Chicago", focus="Healthcare & Bio", rounds=[],
        note="Lumere (formerly Procured Health), clinical evidence software for hospitals, Chicago; acq. by Global Healthcare "
             "Exchange, 2020 (the firm's listing). The firm's year is 2012, the company's founding year; no source found names "
             "the round (Google News, 2026-10-01)."),

    cls("luxury-presence", status="private", rng="below_1b",
        stage="Growth", stage_src="model", stage_conf="medium", entry_date="2021",
        country="US", city="Austin", city_src="web_verified", focus="SaaS",
        rounds=[rnd("2021-11", "Series B", 25900000, "Bessemer Venture Partners", True, None, "press"),
                rnd("2023-08-25", "Series B1", 19200000, "Bessemer Venture Partners", True, lp_b1, "press"),
                rnd("2026-01-08", "Series C", 22000000, "Bessemer Venture Partners", True, lp_c, "press")],
        note="Luxury Presence, websites and marketing software for real estate agents, Austin (Crunchbase News, 2026). "
             "Crunchbase News counts the 2026 Series C as the third time Bessemer invested, after the Series B1 it led in 2023 "
             "(TechCrunch), which makes the Series B it led in 2021 the entry (named from knowledge, no page read). The "
             "listing's 2019 does not fit that count and is not used. No valuation disclosed."),

    cls("main-street-hub", status="acquired", rng="below_1b", city="Austin", focus="SaaS",
        stage="Growth", stage_src="model", stage_conf="medium",
        rounds=[rnd("2013-12-23", "Series B", 14000000, "Bessemer Venture Partners", True,
                    jl.FORMD_CITE("main-street-hub", 1), "filing")],
        note="Main Street Hub, social media and CRM service for local businesses, Austin; acq. by GoDaddy, 2018 ($125M). "
             "Bessemer led the $14M round closed in December 2013, reported at the time as the Series B after a $2.6M round "
             "of 2011 (named from knowledge; the Form D gives the amount and date)."),

    cls("maintainx", status="acquired", rng="below_1b", city="San Francisco", focus="SaaS",
        note="MaintainX, maintenance and work order software, San Francisco; acq. by Autodesk, closed 2026-08-03 (about $3.6B, "
             "Autodesk's 8-K as the Bain Capital Ventures book cites). The firm's post of 2025 says 'We first led MaintainX's "
             "Series B in 2021', which agrees with the Growth band."),

    cls("maker-communications", status="acquired", rng="below_1b",
        stage="Series A", stage_src="first_party", stage_cite=ARCH("maker-communications"), stage_conf="high",
        entry_date="1995",
        country="US", city="Framingham", focus="Industrial & Robotics",
        rounds=[rnd("1995", "Series A", None, "Bessemer Venture Partners", True, ARCH("maker-communications"), "firm")],
        note="Maker Communications, communications processors, Framingham; IPO 1999, acq. by Conexant, 2000. The firm's own "
             "archived description: 'BVP led the Series A round'; its list gives 1995 and 1996 as the investment year."),

    cls("mambu", rng="1b_plus", usd=5542390000, val_src="web_verified", val_cite=mambu_val, asof="2021-12-09",
        flags=["stale", "model_disputes_source"],
        stage="Growth", stage_src="model", stage_conf="medium", entry_date="2019-02",
        country="NL", country_src="web_verified", country_cite="https://en.wikipedia.org/wiki/Mambu", city="Amsterdam",
        focus="Fintech & Payments",
        rounds=[rnd("2019-02-20", "Series C", 34000000, "Bessemer Venture Partners", True, mambu_2019, "press"),
                rnd("2021-01-07", "Series D", None, "TCV", None, None, "press"),
                rnd("2021-12-09", "Series E", 266000000, "EQT Growth", None, mambu_val, "company")],
        note="Mambu, cloud banking platform, founded in Berlin and headquartered in Amsterdam (Wikipedia, as the TCV and "
             "Point Nine books read it; the Wikidata DE is the founding country). Bessemer led the EUR 30M round of February "
             "2019 (Finovate), the round before TCV's Series D and EQT's Series E, so a Series C (named from knowledge). "
             "EUR 4.90B @ ECB 2021-12-09 (EUR/USD 1.1311) = $5.54B, the Series E mark the sibling books carry, replacing "
             "the $2.1B of January 2021; stale."),

    cls("manta", status="acquired", rng="below_1b",
        stage="Series A", stage_src="first_party", stage_cite=POST("data-lineage-leader-manta"), stage_conf="high",
        entry_date="2020-10-06",
        country="US", city="Tampa", focus="Data Infrastructure",
        rounds=[rnd("2020-10-06", "Series A", 13000000, "Bessemer Venture Partners", True,
                    POST("data-lineage-leader-manta"), "firm")],
        note="Manta, data lineage software, founded in Prague and moved its headquarters to Tampa in 2022 (St. Pete Catalyst); "
             "acq. by IBM, 2023. The firm's own post: 'Bessemer Venture Partners leads Manta's $13 million Series A'."),

    cls("manychat", status="private", rng="below_1b",
        stage="Series A", stage_src="web_verified", stage_cite=manychat_2025, stage_conf="medium", entry_date="2019",
        country="US", city="San Francisco", focus="SaaS",
        rounds=[rnd("2019", "Series A", 18000000, "Bessemer Venture Partners", True, manychat_2025, "company"),
                rnd("2025-04-22", "growth round", 140000000, "Summit Partners", None, manychat_tc, "press")],
        note="Manychat, chat marketing automation. The company's 2025 release: 'its first institutional investment of $18 "
             "million in 2019 by Bessemer Venture Partners', which TechCrunch calls the $18 million Series A of 2019; the "
             "firm's listing year 2018 is read as the close. Summit led $140M in 2025 with no valuation disclosed. San "
             "Francisco from knowledge."),
]

jl.write("j04a", lines)
