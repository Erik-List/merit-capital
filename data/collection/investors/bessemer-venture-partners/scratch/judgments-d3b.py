"""PRO-80 Bessemer, delta judge d3, file b: rows natpal to youngworld-stores-group (18 rows: 5 recall verdicts, one
not_member) and the seven older rows that lacked a country."""
import json
import re

import judge_lib as jl

N = jl.NEWS
_BASE = jl._base()
_CL = json.loads((jl.INV / "companies/classification.json").read_text())
_CL = _CL.get("bessemer-venture-partners", _CL)
WV = {"valuation_range_source": "web_verified"}


def RC(slug):
    """The citation URL carried by the row's own 'recall addition:' note (read from disk, never typed)."""
    m = re.findall(r"\((https?://[^)\s]+)\)", _BASE[slug].get("notes") or "")
    if not m:
        raise SystemExit(f"RC({slug!r}): no URL in the row's note")
    return m[-1]


def PRIOR(extra=None):
    """A country inferred from the firm's US desk: low confidence, flagged."""
    d = {"hq_country_confidence": "low"}
    d.update(extra or {})
    return d


def first_year(y, cap=True):
    s = f"The firm's {y} page gives no investment year, so the entry date is the first year the firm listed it (a capture year)"
    return s if cap else s[0].lower() + s[1:]


# Light Reading pages, each found through the publisher's own search and read 2026-10-06
LR = "https://www.lightreading.com"
PELAGO_R1 = LR + "/business-management/-17m-round-1-for-pelago-networks"
PELAGO_B = LR + "/business-management/pelago-grabs-32m"
WATERCOVE = LR + "/cable-technology/alcatel-swallows-watercove"
# other pages read 2026-10-06
YODLE = _CL["yodle"]                                            # the row natpal duplicates
CHANNELLIFE = N("orderwork", "Evernex buys")
RAIN_REL = RC("rain")
BLOCK_RAIN_B = N("rain", "raises $58 million from Samsung")
WIKI_RAIN = jl.W("Rain (platform)")
IIFL_RICO = "https://www.indiainfoline.com/company/rico-auto-industries-ltd/summary"            # WebSearch result, read
ENTRACKR_SHOPDECK = N("shopdeck", "WMall founders return")
INC42_SHOPDECK = N("shopdeck", "ShopDeck Bags")
YF_STAYTERRA = N("stayterra", "StayTerra Builds Out")
TRITON_S1 = "https://www.sec.gov/Archives/edgar/data/1050250/0000950144-00-008672.txt"          # S-1/A of 2000-07-12, read through secget
GLOBES_HYPERROLL = "https://en.globes.co.il/en/article-1000501576"                              # WebSearch result, read
VOICEBOT = N("life-bot", "Matchbox.io Has Acquired")
OFFBEAT = RC("off-beat")

lines = [
    jl.cls("natpal", status="acquired", rng="below_1b",
           stage=YODLE["entry_stage"], stage_src=YODLE["entry_stage_source"], stage_cite=YODLE["entry_stage_citation"],
           stage_conf="medium", entry_date=YODLE["entry_date"], country="US", city="New York",
           focus="Media, Gaming & Advertising", flags=["identity_conflated"], rounds=YODLE["funding_rounds"],
           note="NatPal is the earlier name of Yodle: the firm's later listings read 'Yodle (fka NatPal)'. This row duplicates the row yodle and is classified as that row is: New York, the Series A of November 2006 per Yodle's S-1 (the firm's own investment date 2006-10-04), acq. by Web.com, 2016."),
    jl.cls("nextmedium", status="acquired", rng="below_1b", stage="undetermined", entry_date="2006",
           country="US", city="Los Angeles", focus="Media, Gaming & Advertising", rounds=[],
           note="Marketplace and measurement technology for product placement; Los Angeles, from knowledge. Veritone's S-1 (2017): 'In July 2014, we acquired ROIM, Inc. ... and NextMedium, LLC ... through a series of transactions between entities where common control existed' (the Brand Affinity Technologies group), so the business ended up inside Veritone; when it left its venture holders was not found (successor entity, read acquired). "
                + first_year("2006") + "; no round named."),

    jl.verdict("off-beat", "member",
               "Bar and Bench (2026-05-07): 'OffBeat Studios Private Limited, dba OFF/BEAT, has concluded a Series Seed funding round led by Bessemer Venture Partners (BVP) and Reed India.' CIOL (2026-04-09) reports the same Rs 100 crore seed led by Bessemer.",
               ec="web", conf="high", cite=OFFBEAT),
    jl.cls("off-beat", status="private", rng="below_1b",
           stage="Seed", stage_src="web_verified", stage_cite=OFFBEAT, stage_conf="high", entry_date="2026-04-07",
           grad="censored", country="IN", country_src="web_verified", country_cite=OFFBEAT,
           focus="Media, Gaming & Advertising", flags=["city_unknown"],
           rounds=[jl.rnd("2026-04-07", "Seed", 10_751_748, "Bessemer Venture Partners and Reed India", True, OFFBEAT, "press")],
           note="Technology and AI venture for India's creator and content economy, started by boAt co-founder Aman Gupta (OffBeat Studios Private Limited). The Series Seed of April 2026 led by Bessemer and Reed India is the entry: INR 1.00B @ ECB 2026-04-07 (INR/EUR 107.4895, EUR/USD 1.1557) = $10.8M. Censored: the entry is inside the last 24 months. None of the reports read names the company's city."),

    jl.cls("orderwork", status="acquired", rng="below_1b", stage="undetermined", entry_date="2006",
           country="GB", country_src="web_verified", country_cite=CHANNELLIFE, focus="Consumer & Marketplaces",
           flags=["city_unknown"], rounds=[],
           note="Web-based network of local suppliers for on-site IT work, UK. ChannelLife (2026-06-30): 'Evernex has acquired UK-based Empowered and OrderWork', sister companies 'headquartered in Bedfordshire' (acq. by Evernex, 2026; who held OrderWork between the firm's listing and that sale was not read). The report gives the county and not the town, so the city is left open. "
                + first_year("2006") + "; no round named."),
    jl.cls("pelago-networks", status="defunct", rng="below_1b",
           stage="Series A", stage_src="web_verified", stage_cite=PELAGO_B, stage_conf="high", entry_date="2000",
           country="US", city="Marlborough", city_src="web_verified", focus="Data Infrastructure",
           rounds=[jl.rnd("2000-06", "Series A", 17_000_000, None, True, PELAGO_R1, "press"),
                   jl.rnd("2002-04-01", "Series B", 32_000_000, "Advent International", True, PELAGO_B, "press")],
           note="Enhanced voice services equipment for local carriers, Marlborough, Massachusetts. Light Reading (2002-04-01) reports the $32M Series B with Bessemer among the existing investors and says it 'follows Pelago's initial $17 million Series A venture financing in June 2000'; its report of 2000-12-06 names Bessemer, Charles River Ventures and Columbia Capital in that first round, the firm's own investment year. Light Reading (2003-05-05): Pelago 'had its stuff auctioned off a few days ago', sold for parts with no buyer of the business, so it reads defunct."),
    jl.cls("pre-solutions", status="acquired", rng="below_1b", stage="undetermined", entry_date="2004",
           country="US", focus="Fintech & Payments", flags=["city_unknown"], rounds=[],
           note="Prepaid debit cards for the unbanked, listed by the firm from 2004 as ITC Financial Services. CT Communications' 10-K for 2006: 'In December 2004, ITC Financial merged with PRE Solutions to form PRE Holdings, Inc. ... In June 2006, InComm purchased PRE Holdings, Inc.' (acq. by InComm, 2006, as the firm's listing says). "
                + first_year("2004") + "; no round named, and no source read places the company's city."),
    jl.cls("project-austin", status="unknown", rng="below_1b", stage="undetermined", entry_date="2000",
           country="US", focus="SaaS", flags=["city_unknown", "country_prior"], extra=PRIOR(), rounds=[],
           note="Listed by the firm in 2000 only as 'Project Austin, Inc.' (David Cowan), software that 'enables suppliers to maximize their revenues while reducing their costs'; the name reads like a working title and Wikipedia, Google News and EDGAR full text carry no trace of it, so the status reads unknown. The country is inferred from the firm's US desk of 2000; "
                + first_year("2000", cap=False) + ". No round named."),

    jl.verdict("rain", "member",
               "The company's own release (2026-01-09): the $250M Series C was 'led by ICONIQ, with participation from Sapphire Ventures, Dragonfly, Bessemer Venture Partners, Galaxy Ventures, FirstMark, Lightspeed, Norwest, and Endeavor Catalyst'.",
               ec="web", conf="high", cite=RAIN_REL),
    jl.cls("rain", status="private", rng="1b_plus", usd=1_950_000_000, val_src="web_verified", val_cite=RAIN_REL,
           asof="2026-01-09", val_conf="high",
           stage="Growth", stage_src="web_verified", stage_cite=RAIN_REL, stage_conf="high", entry_date="2026-01-09",
           city="New York", city_src="web_verified", focus="Fintech & Payments", extra=WV,
           rounds=[jl.rnd("2022", "Seed", 6_000_000, "Lightspeed Venture Partners", False, WIKI_RAIN, "press"),
                   jl.rnd("2025-03", "Series A", 24_500_000, "Norwest Venture Partners", False, WIKI_RAIN, "press"),
                   jl.rnd("2025-08-28", "Series B", 58_000_000, "Sapphire Ventures", False, BLOCK_RAIN_B, "press"),
                   jl.rnd("2026-01-09", "Series C", 250_000_000, "ICONIQ", True, RAIN_REL, "company")],
           note="Stablecoin-funded card issuing and payments infrastructure, New York (the release's dateline and Wikipedia; the ICONIQ row agrees, the Lightspeed row reads Los Angeles). The company's release names Bessemer in the $250M Series C of January 2026, which 'values Rain at $1.95 billion', the mark the ICONIQ and Lightspeed rows carry. The investor lists of the 2022 seed and the March 2025 Series A (Wikipedia) and of the August 2025 Series B (The Block) do not name Bessemer, so the Series C is the entry."),

    jl.verdict("rico-auto-industries", "not_member",
               "Purchase of a company that was already listed, with no Bessemer round before the listing (COLLECTION.md s1 T3, decisions.md R3): the firm's own 2005 to 2007 text reads 'Rico (BSE:RICOAUTO) designs and manufactures auto components ... The company is based in India' and first carried it in July 2005, while IIFL's company history has Rico Auto Industries, incorporated in 1983, coming out with a public issue of equity shares in 1993. The BVP India stake of 2005 went into a company listed for a decade.",
               ec="web", conf="high", cite=IIFL_RICO),

    jl.cls("sandial", status="unknown", rng="below_1b", stage="undetermined", entry_date="2003",
           country="US", city="Portsmouth", focus="Data Infrastructure", rounds=[],
           note="Storage network switch maker (Sandial Systems); Portsmouth, New Hampshire, from knowledge. A123 Systems' prospectus has its finance chief there from August 2002 to August 2004, and a venture lender's filings carry a loan to it through 2004; nothing read says what became of it, so the status reads unknown. "
                + first_year("2003") + "; no round named."),

    jl.verdict("shopdeck", "member",
               "The firm's own post of 2026-03-05 names ShopDeck among the companies where its vice president Aparna Chaganty sits as board observer; Entrackr (2024-08-07) has Bessemer putting Rs 35.24 crore into the Series B1 of ShopDeck's parent, and Inc42 (2024-11-27) reports the $8M Series B as led by Bessemer.",
               ec="web", conf="high", cite=RC("shopdeck")),
    jl.cls("shopdeck", status="private", rng="below_1b",
           stage="Growth", stage_src="web_verified", stage_cite=ENTRACKR_SHOPDECK, stage_conf="high", entry_date="2024-08",
           country="IN", country_src="web_verified", country_cite=INC42_SHOPDECK, city="Bangalore", city_src="web_verified",
           focus="SaaS",
           rounds=[jl.rnd("2024-08", "Series B1", 7_850_000, "Bessemer Venture Partners", True, ENTRACKR_SHOPDECK, "press")],
           note="Storefront and growth software for direct-to-consumer sellers (Blitzscale Technology, formerly WMall), Bengaluru (Inc42). Entrackr (2024-08-07) read the filings: a Series B1 of Rs 65.2 crore (about $7.85M) with Bessemer contributing Rs 35.24 crore beside Chiratae, Elevation, VH Capital and Reed India, at about $50M post-money; the round was announced on 2024-11-27 as an $8M Series B led by Bessemer. Bessemer's first round, so the entry reads Growth."),

    jl.cls("solant", status="acquired", rng="below_1b", stage="undetermined", entry_date="1999",
           country="US", city="Boulder", city_src="web_verified", focus="SaaS", rounds=[],
           note="Electronic billing and customer care software, formerly Novazen, 'a Boulder, Colorado-based vendor' (PlanetCAD proxy, 2001). Direct Insite's 10-K for 2000 speaks of 'Solant, Inc which was acquired by Avolent, Inc.', and a HyperSpace Communications prospectus dates an executive's move to Avolent January 2001, 'after Avolent's acquisition of Solant' (acq. by Avolent, 2001). The entry year 1999 is the firm's own; no round named."),

    jl.verdict("stayterra", "member",
               "The firm's own post of 2026-01-28 names StayTerra among the companies whose board meetings its vice president Sam Bondy attends, and the company's releases describe it as backed by Garnett Station Partners and Bessemer Venture Partners (2026-09-24). decisions.md R7: on both bvp.com and the Forge grid, IN as a minority growth investment beside the existing sponsor.",
               ec="web", conf="medium", cite=RC("stayterra")),
    jl.cls("stayterra", status="private", rng="below_1b",
           stage="Growth", stage_src="model", stage_conf="medium", entry_date="2025-07",
           country="US", city="New York", city_src="web_verified", focus="Consumer & Marketplaces",
           rounds=[jl.rnd("2025-07", "growth investment", None, None, True, None, "press")],
           note="Group of regional vacation rental management brands launched by Garnett Station Partners; its releases are datelined New York and name Garnett Station and Bessemer as its investors (Yahoo Finance, 2026-09-24). The entry is the growth investment of July 2025 beside the existing sponsor (decisions.md R7; the FinSMEs report of 2025-07-18 would not open in this pass, so the round is named from the run's record at medium confidence). No later priced round found."),

    jl.cls("thinq-learning-solutions", status="acquired", rng="below_1b", stage="undetermined", entry_date="1999",
           country="US", city="Baltimore", city_src="web_verified", focus="SaaS", rounds=[],
           note="Enterprise learning management software, listed by the firm in 2000 as TrainingNet.com. Saba's release of 2005-03-24: 'it has signed a definitive agreement to acquire THINQ Learning Solutions, Inc, a privately-held Baltimore-based provider of enterprise learning management solutions' (acq. by Saba, 2005, as the firm's listing says). The entry year 1999 is the firm's own; no round named."),

    jl.verdict("triton-network-systems", "member",
               "Triton's 10-K/A of April 2001 lists 'Entities affiliated with Bessemer Venture Partners' at 1,947,489 shares (5.5%), among them Bessemer Venture Partners IV L.P. and Bessec Ventures IV L.P.; its S-1/A of July 2000 shows those entities buying 1,177,500 series A, 470,000 series B and 300,000 series C preferred shares before the listing, a venture holding from the first round.",
               ec="web", conf="high", cite=RC("triton-network-systems")),
    jl.cls("triton-network-systems", status="defunct", rng="below_1b",
           stage="Series A", stage_src="web_verified", stage_cite=TRITON_S1, stage_conf="high", entry_date="1997-11",
           country="US", city="Orlando", city_src="web_verified", focus="Data Infrastructure",
           rounds=[jl.rnd("1997-11", "Series A", 14_400_000, None, True, TRITON_S1, "filing"),
                   jl.rnd("1998-05", "Series B", 32_769_845, None, True, TRITON_S1, "filing"),
                   jl.rnd("1999-10", "Series C", 50_525_000, None, True, TRITON_S1, "filing")],
           note="Broadband wireless equipment maker, Orlando, Florida, listed in July 2000. Its S-1/A: 'In November 1997, we sold an aggregate 7,200,000 shares of our series A preferred stock at a price of $2.00 per share', of which the Bessemer entities bought 1,177,500, then shares of the series B (1998 to 1999) and C (1999). The stockholders' meeting of 2001-10-29 was called to approve a Plan of Complete Liquidation and Dissolution (DEF 14A), so it reads defunct."),

    jl.cls("virtual-growth", status="acquired", rng="below_1b", stage="undetermined", entry_date="1999",
           country="US", city="New York", focus="SaaS", rounds=[],
           note="Outsourced accounting for small businesses over the Internet; New York, from knowledge. Administaff's 10-Q for the first quarter of 2002: it 'purchased substantially all of the assets of Virtual Growth, Inc. through bankruptcy proceedings for a total cost of $1.4 million', mainly its software and hardware (an asset sale out of insolvency: acq. by Administaff, 2002). The entry year 1999 is the firm's own; no round named."),
    jl.cls("watercove-networks", status="acquired", rng="below_1b", stage="undetermined", entry_date="2002",
           country="US", city="Chelmsford", city_src="web_verified", focus="Data Infrastructure", rounds=[],
           note="Packet data gateways (GGSN) for wireless carriers, Chelmsford, Massachusetts (its 2003 release dateline). Light Reading (2004-01-30): 'Alcatel has agreed to purchase' WaterCove, after $70M of venture funding from Charles River Ventures, Sprout Group, Orange Ventures and Bessemer, price undisclosed (acq. by Alcatel, 2004). "
                + first_year("2002") + "; no round named."),
    jl.cls("youngworld-stores-group", status="unknown", rng="below_1b", stage="undetermined", entry_date="2003",
           country="US", focus="Consumer & Marketplaces", flags=["city_unknown"], rounds=[],
           note="Chain of children's and young adults' clothing stores, listed by the firm in 2003 and 2004 (J. Edmund Colloton). A 2004 prospectus still names it as a privately held company with a US director (John Berylson), and EDGAR full text finds its stores in US commercial mortgage trust filings of 2001 to 2004; nothing read says what became of it, so the status reads unknown. "
                + first_year("2003") + "; no round named, and the head office was not found."),

    # ---- the seven older rows that lacked a country
    jl.cls("access-360-media", country="US", clear=["country_unknown"],
           note="Country answered: a US in-store television network for young shoppers (fka Access Retail Entertainment); its chief executive from October 2006 was Lon Otremba, per the proxies of two US companies on whose boards he sat, and MIT Technology Review (2008-04-11) describes its screens in stores. The city (New York is recalled) was not confirmed by a source read."),
    jl.cls("ba-systems", country="US", focus="Data Infrastructure", flags=["country_prior"], clear=["country_unknown"],
           extra=PRIOR(),
           note="Country answered by inference: the firm's 2006 page files it under semiconductors and components ('developing innovative enterprise networking solutions', Rob Chandra, site ba-sys.com) and marks its Indian companies as based in India, which it does not do here; no source read identifies the company, so US is the firm's desk, flagged. Focus moved from SaaS to the firm's own description."),
    jl.cls("datadistillr", country="US", clear=["country_unknown"],
           note="Country answered: a US start-up, built around the Apache Drill project by Charles Givre (from knowledge; the 2021 trade item already on the row ties it to Drill). Its site no longer answers (2026-10-06), which is noted and not read as a closure; city not established."),
    jl.cls("domain", country="US", flags=["country_prior"], clear=["country_unknown"], extra=PRIOR(),
           note="Country answered by inference only: the company still cannot be named (the 2008 history page's one use of the word is the Domain Name System, not a portfolio company), and the firm's desk in 1986 was the United States, so US is that desk, flagged. The row stays unresolved."),
    jl.cls("first-index", rng="below_1b", country="US", city="Whippany", city_src="web_verified",
           focus="Consumer & Marketplaces", clear=["identity_unresolved", "country_unknown", "city_unknown"],
           note="Identified: Aviation Week (2001-12-18) has 'First Index USA of Whippany, N.J.' launching e-sourcing software to help buyers find suppliers of custom-made products, and American Machinist (2002-01-01) calls it 'a business-to-business e-marketplace for custom-manufactured industrial components' with 7,000 active buyers, which is the company the firm describes. Named, so the band reads below $1B; nothing read says what became of it (status stays unknown) or names the round."),
    jl.cls("hyperroll", country="US", city="Mountain View", city_src="web_verified",
           clear=["country_unknown", "city_unknown"],
           note="Country answered: Globes (2009-09-30), on Oracle's purchase: 'It has its corporate headquarters in Mountain View, California, and its development center in Omer', with Greylock, Sequoia and Bessemer as the main shareholders. US and Mountain View on that report; the Sequoia row agrees on the country, the Greylock row (Kfar Saba, Israel) does not."),
    jl.cls("life-bot", status="acquired", country="GB", country_src="web_verified", country_cite=VOICEBOT,
           city="London", city_src="web_verified", clear=["city_unknown"],
           note="Country answered: Voicebot.ai (2019-11-19) calls the founders' company Opearlo 'London-based', established by Jess Williams and Oscar Merry in 2016 and at first operating under the name Life Bot. The same report has Matchbox.io acquiring all ten of its Alexa skills while the founders moved on, a sale of the whole product line, so the status reads acquired (skills acq. by Matchbox.io, 2019)."),
]

jl.write("d3b", lines)
