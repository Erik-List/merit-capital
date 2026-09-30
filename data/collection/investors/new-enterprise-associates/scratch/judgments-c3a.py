"""PRO-100 NEA, judge c3, queue batch 5 (listed members, classification)."""
import json
from pathlib import Path

import judge_lib as jl

cls, rnd, SITE, POST, W, NEWS, ARCH = jl.cls, jl.rnd, jl.SITE, jl.POST, jl.W, jl.NEWS, jl.ARCH
SIBS = json.loads((Path(__file__).resolve().parent / "siblings.json").read_text())


def FTSU(reg, suffix):
    """A full-text-hit URL on disk: the filing of registrant `reg` whose URL ends with `suffix` (exactly one)."""
    m = sorted({f["url"] for r in jl._FTS if reg.lower() in r["registrant"].lower()
                for f in r.get("filings", []) if f["url"].endswith(suffix)})
    if len(m) != 1:
        raise SystemExit(f"FTSU({reg!r}, {suffix!r}) matched {m}")
    return m[0]


def SIBCITE(slug, investor):
    """The valuation citation a sibling book carries for the same company (rule 10 alignment)."""
    m = [x["val_cite"] for x in SIBS.get(slug, []) if x["investor"] == investor and x.get("val_cite")]
    if len(m) != 1:
        raise SystemExit(f"SIBCITE({slug!r}, {investor!r}) matched {m}")
    return m[0]


SA = "https://stockanalysis.com/stocks/{}/market-cap/"
WV = {"valuation_range_source": "web_verified"}
UNJOIN = {"valuation_source": None, "valuation_range_source": None, "valuation_asof": None}
LEFT = "Graduation left for the graduation pass."

L = []

# chg-healthcare
L.append(cls("chg-healthcare", status="acquired", rng="below_1b", stage="undetermined", entry_date="1998",
             country="US", city="Midvale", focus="Healthcare & Bio",
             note="Healthcare staffing company; the firm's exit line says acquired by J.W. Childs (2006, after the withdrawn IPO whose "
                  "registration rights agreement names NEA VIII). The 1998 round NEA entered is not named in any record found."))

# china-gtel-limited
L.append(cls("china-gtel-limited", status="unknown", rng="below_1b", stage="undetermined", entry_date="2006",
             country="CN", country_src="web_verified", country_cite=SITE("china-gtel-limited"),
             focus="Media, Gaming & Advertising", flags=["city_unknown"],
             note="Chinese wireless search provider the firm still lists as private from a 2006 investment; no press or filing "
                  "traces the company, so its state, city and round stay open."))

# china-health-citic
L.append(cls("china-health-citic", status="acquired", rng="below_1b", stage="undetermined", entry_date="2008",
             country="CN", country_src="web_verified", country_cite=SITE("china-health-citic"),
             focus="Healthcare & Bio", flags=["city_unknown"],
             note="Pharmaceutical and medical supply distributor serving China's healthcare services industry; the firm's exit "
                  "line says acquired by Shanghai Pharmaceuticals. City and the 2008 round are not on record."))

# chromacode
L.append(cls("chromacode", status="private", rng="below_1b", city="Carlsbad", focus="Healthcare & Bio",
             note="PCR multiplexing diagnostics company in Carlsbad (its Form D address), still private per the firm's listing; "
                  "no mark near $1B."))

# cirrus-logic
L.append(cls("cirrus-logic", rng="1b_plus", usd=6.02e9, val_src="web_verified", val_cite=SA.format("crus"),
             asof="2026-09-30", stage="undetermined", entry_date="1990", city="Austin", focus="Industrial & Robotics",
             extra=WV,
             note="Mixed-signal chip maker in Austin; market cap $6.02B on 2026-09-30 (stockanalysis), in line with the IVP "
                  "book's $6.01B. The firm dates its first investment to 1990, after the 1989 Nasdaq listing, and names no round."))

# cista
L.append(cls("cista", status="private", rng="below_1b", stage="undetermined", entry_date="2018", country="US",
             focus="Industrial & Robotics", flags=["city_unknown"],
             note="CMOS image sensor startup (Cista Design Inc.) the firm lists as private from a 2018 investment by its Asia "
                  "team; no press or filing places it in a city or names the round."))

# clarifai
L.append(cls("clarifai", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified",
             stage_cite=W("Clarifai"), stage_conf="high", entry_date="2021-10", city="Washington",
             focus="AI & Applied AI",
             rounds=[rnd("2021-10", "Series C", 60_000_000, "New Enterprise Associates", True, W("Clarifai"), "press")],
             note="NEA led the $60M Series C of October 2021 (Wikipedia), its first round in the company; the firm's exit line "
                  "and the GV, Lux, Menlo and USV books record the sale to Nebius."))

# clarify
L.append(cls("clarify", status="acquired", rng="below_1b", stage="undetermined", entry_date="1992", city="San Jose",
             focus="SaaS",
             note="Customer service software company, Nasdaq CLFY, acquired by Nortel in 2000 (the firm's exit line; IVP and Menlo "
                  "agree). The Spark book's Clarify is Clarify Health, a different company."))

# clarvista-medical
L.append(cls("clarvista-medical", status="acquired", rng="below_1b", stage="undetermined", entry_date="2012",
             city="Aliso Viejo", city_src="formd_address", focus="Healthcare & Bio",
             note="Ophthalmic device company (formerly Prospex Medical IV) in Aliso Viejo; the firm's exit line says acquired by "
                  "the University of Colorado Anschutz Medical Campus. Entry year is the firm's own 2012; the 2015 Form D is a later round."))

# clearmetal
L.append(cls("clearmetal", status="acquired", rng="below_1b", stage="Seed", stage_src="first_party",
             stage_cite=SITE("clearmetal"), stage_conf="medium", entry_date="2015", city="San Francisco",
             focus="SaaS",
             note="Predictive logistics software; the firm's card reads Seed in 2015. project44 acquired it in May 2021 "
                  f"(FinSMEs, {NEWS('clearmetal', 'project44 Acquires ClearMetal')}). {LEFT}"))

# clearmotion
L.append(cls("clearmotion", status="private", rng="below_1b", city="Billerica", focus="Industrial & Robotics",
             note="Active suspension and digital chassis company in Billerica, Massachusetts (Form D address), still private; "
                  "no priced mark at or above $1B on record."))

# cleave-biosciences
L.append(cls("cleave-biosciences", status="private", rng="below_1b", stage="undetermined", entry_date="2013",
             country="US", city="Burlingame", focus="Healthcare & Bio",
             note="Oncology small-molecule company, now Cleave Therapeutics, still listed private by the firm; the 2016 $37M round "
                  "Celgene backed is later than NEA's 2013 entry, whose round is not named."))

# clementia
_CLEM_F1 = FTSU("Clementia", "c88073_f1.htm")
L.append(cls("clementia", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified",
             stage_cite=_CLEM_F1, stage_conf="high", entry_date="2015-06",
             country="CA", country_src="web_verified", country_cite=FTSU("Clementia", "c88073_ex4-2.htm"),
             city="Montreal", focus="Healthcare & Bio",
             rounds=[rnd("2015-06", "Class B preferred", 59_999_141, None, True, _CLEM_F1, "filing")],
             note="The F-1 shows NEA 15 buying $20.0M of the June 2015 Class B preferred and no NEA entity in the Class A; "
                  "Montreal company acquired by Ipsen in 2019."))

# cleo
L.append(cls("cleo", status="acquired", rng="below_1b", stage="Growth", stage_src="first_party",
             stage_cite=POST("cleo-series-b"), stage_conf="high", entry_date="2019-03", city="San Francisco",
             focus="Healthcare & Bio", flags=["stage_disputes_band"],
             rounds=[rnd("2019-03-20", "Series B", 27_500_000, "New Enterprise Associates", True, POST("cleo-series-b"), "firm")],
             note="The firm's post of 2019-03-20 announces NEA leading the $27.5M Series B after first meeting the CEO, so the "
                  "entry is the B, not the 2016 filing the band read. Wellthy acquired Cleo in September 2026 "
                  f"({NEWS('cleo', 'Wellthy acquires Cleo in bid')}); the Balderton, EQT and Greylock Cleo is Cleo AI, a different company."))

# cleversafe
L.append(cls("cleversafe", status="acquired", rng="below_1b", city="Chicago", focus="Data Infrastructure",
             note="Object storage company in Chicago acquired by IBM in 2015 (the firm's exit line)."))

# clio
_CLIO = SIBCITE("clio", "tcv")
L.append(cls("clio", rng="1b_plus", usd=5.0e9, val_src="web_verified", val_cite=_CLIO, asof="2025-11",
             stage="Growth", stage_src="first_party", stage_cite=SITE("clio"), stage_conf="medium", entry_date="2024",
             country="CA", country_src="web_verified", country_cite=_CLIO, city="Burnaby", focus="SaaS",
             clear=["unicorn_name_match"], extra=WV,
             note="Legal practice software in Burnaby, British Columbia; the firm's card reads Growth in 2024. Marked at the $5B "
                  "Series G of November 2025 (Clio's release), as in the TCV and Point Nine books; the Wikidata country CA is confirmed."))

# clockwork
L.append(cls("clockwork", status="private", rng="below_1b", stage="Series A", stage_src="web_verified",
             stage_cite=NEWS("clockwork", "Clockwork Raises $21M Series A Led by NEA"), stage_conf="high",
             entry_date="2022-03", country="US", city="Palo Alto", focus="Data Infrastructure",
             flags=["model_disputes_source"],
             rounds=[rnd("2022-03-16", "Series A", 21_000_000, "New Enterprise Associates", True,
                         NEWS("clockwork", "Clockwork Raises $21M Series A Led by NEA"), "company"),
                     rnd("2025-09-10", "funding", 20_500_000, None, None,
                         NEWS("clockwork", "Clockwork raises $20.5M to synchronize"), "press")],
             extra={**WV, "valuation_asof": "2026-09-30",
                    "valuation_citation": NEWS("clockwork", "Clockwork raises $20.5M to synchronize")},
             note="Clock synchronization software (clockwork.io, formerly Tick Tock Networks); NEA led the $21M Series A announced "
                  "2022-03-16. The Wikidata country DK is a wrong join on the one-word name. Momentum check 2026-09-30 (Google News): "
                  "latest round $20.5M in September 2025, no priced mark at or above $1B; the a16z Clockwork Labs is a different company."))

# cloudflare
_NET = "https://www.vcnewsdaily.com/cloudflare/venture-capital-funding/stndvkjrsv"  # found by WebSearch, read with WebFetch
L.append(cls("cloudflare", rng="100b_plus", usd=125.27e9, val_src="web_verified", val_cite=SA.format("net"),
             asof="2026-09-30", stage="Growth", stage_src="web_verified", stage_cite=_NET, stage_conf="medium",
             entry_date="2010", city="San Francisco", focus="Security", extra=WV,
             rounds=[rnd("2011-07-12", "Series B", 20_000_000, "New Enterprise Associates", True, _NET, "press")],
             note="NEA led the $20M Series B with Venrock and Pelion as the existing holders (VC News Daily, announced 2011-07-12; the "
                  "firm dates it 2010, though the S-1 seats Sandell from November 2009). Market cap $125.27B on 2026-09-30 "
                  "(stockanalysis), fresher than the USV book's $99.31B of 2026-09-04."))

# clovis-oncology
_CLOVIS = FTSU("Clovis", "d82988sv1.htm")
L.append(cls("clovis-oncology", rng="below_1b", stage="Series A", stage_src="web_verified", stage_cite=_CLOVIS,
             stage_conf="high", entry_date="2009-05-15", city="Boulder", focus="Healthcare & Bio",
             rounds=[rnd("2009-05-15", "Series A-1 preferred", None, None, True, _CLOVIS, "filing")],
             note="The S-1's related-party table shows NEA buying Series A-1 preferred on 2009-05-15 at the company's founding. "
                  "Clovis filed Chapter 11 in December 2022 and sold its drug assets, so it reads acquired."))

# coda
L.append(cls("coda", status="acquired", rng="below_1b", stage="undetermined", entry_date="2015", city="Mountain View",
             focus="SaaS",
             note="Document editor coda.io, acquired by Grammarly in December 2024 as in the General Catalyst and Greylock books; "
                  "NEA's 2015 round is not named. The Insight book's Coda is Coda Payments of Singapore, a different company."))

# code-biotherapeutics
L.append(cls("code-biotherapeutics", status="private", rng="below_1b", city="Hatfield", focus="Healthcare & Bio",
             note="Non-viral gene therapy company in Hatfield, Pennsylvania (Form D address), still private per the firm's listing."))

# code42
L.append(cls("code42", status="acquired", rng="below_1b", stage="Growth", stage_src="first_party", stage_cite=SITE("code42"),
             stage_conf="medium", entry_date="2015", city="Minneapolis", focus="Security",
             note="Data protection and insider risk company in Minneapolis; the firm's card reads Growth in 2015. Mimecast acquired "
                  f"it in July 2024 ({NEWS('code42', 'Mimecast Acquires Veteran Data Security Firm Code42')}), fresher than the Accel book's private."))

# coedition
L.append(cls("coedition", status="acquired", rng="below_1b", stage="Seed", stage_src="first_party",
             stage_cite=SITE("coedition"), stage_conf="medium", entry_date="2018", country="US", city="New York",
             focus="Consumer & Marketplaces",
             note="Plus-size multi-brand store launched in 2018 by former Gilt Groupe executives; the firm's card reads Seed in "
                  f"2018 and points its site to City Chic's CoEdition store, read as a sale of the business to City Chic. {LEFT}"))

# cogenesys
L.append(cls("cogenesys", status="acquired", rng="below_1b", stage="Growth", stage_src="first_party",
             stage_cite=SITE("cogenesys"), stage_conf="medium", entry_date="2006", country="US", city="Rockville",
             focus="Healthcare & Bio",
             note="Biotherapeutics spin-out of Human Genome Sciences; the firm's card reads Growth in 2006 and its exit line records "
                  "the sale to Teva (2008)."))

# cohere-networks / cohere-technologies (one company; the unicorn figure is Cohere of Toronto)
for _s in ("cohere-networks", "cohere-technologies"):
    L.append(cls(_s, rng="below_1b", city="Santa Clara", focus="Data Infrastructure",
                 flags=["model_disputes_source"], clear=["unicorn_name_match", "needs_web_value"], extra=UNJOIN,
                 note="Cohere Technologies, the OTFS wireless modulation company (formerly Cohere Networks), in Santa Clara; the "
                      "$6.8B figure was the unicorn list's Cohere, the Toronto AI company (a name collision), so it is removed. "
                      "cohere-networks and cohere-technologies are one company."))

# collective-health
_CHB = "https://www.prweb.com/releases/2015/03/prweb12592281.htm"  # found by WebSearch, read with WebFetch
L.append(cls("collective-health", status="private", rng="1b_plus", usd=1.5e9, val_src="web_verified",
             val_cite=SIBCITE("collective-health", "redpoint-ventures"), asof="2021-05-04",
             stage="Series A", stage_src="model", stage_conf="medium", entry_date="2014", city="San Francisco",
             focus="Healthcare & Bio", flags=["stale"], extra=WV,
             rounds=[rnd("2015-03-19", "Series B", 38_000_000, "Founders Fund; New Enterprise Associates", True, _CHB, "company"),
                     rnd("2015-10-19", "Series C", 81_000_000, None, True, POST("collective-health-turning"), "firm")],
             note="The firm dates its first investment to 2014, before the $38M Series B of March 2015 whose release says the "
                  "company's funding 'has been led by Founders Fund and NEA', so the entry is read as the 2014 Series A. Marked at "
                  "the $1.5B of the May 2021 $280M round, as in the GV and Redpoint books (stale)."))

# com21
L.append(cls("com21", status="acquired", rng="below_1b", stage="undetermined", entry_date="1994", country="US",
             city="Milpitas", focus="Data Infrastructure",
             note="Cable modem maker (Nasdaq CMTO) with NEA's Kramlich a director from May 1994; it filed Chapter 11 in 2003 and "
                  "sold its business to ARRIS, so it reads acquired out of insolvency. The 1994 round is not named."))

# comanche
L.append(cls("comanche", status="private", rng="below_1b", city="Concord", city_src="formd_address",
             focus="Healthcare & Bio",
             note="Comanche Biopharma, preeclampsia drug developer, still private; its Form D gives Concord, Massachusetts."))

# compass-labs-inc
L.append(cls("compass-labs-inc", status="unknown", rng="below_1b", grad="graduated", grad_src="formd",
             city="San Jose", city_src="formd_address", focus="SaaS",
             note="Compass Labs of San Jose, a real-time search and social data startup (not Compass Inc., the real estate firm in "
                  "the Atomico, IVP and Thrive books, whose unicorn record was a name match); it left the firm's list after 2014 and "
                  "its fate is not on record. Its Form D sequence graduates the $5M 2010 round with $12M in 2012."))

# complexa
L.append(cls("complexa", status="unknown", rng="below_1b", city="Berwyn", focus="Healthcare & Bio",
             note="Nitro fatty acid drug developer in Berwyn, Pennsylvania (Form D address); the firm marks the position Historic "
                  "with no exit, and no later filing or press shows the company's state."))

# comprehensive-pharmacy-services
L.append(cls("comprehensive-pharmacy-services", status="acquired", rng="below_1b", stage="undetermined", entry_date="2019",
             country="US", city="Memphis", focus="Healthcare & Bio",
             note="Hospital pharmacy services company in Memphis the firm lists as acquired by UnitedHealth Group, with "
                  "Makhzoumi on its board; the 2019 transaction NEA entered through is not described in any record found."))

# concentric-medical
L.append(cls("concentric-medical", status="acquired", rng="below_1b", stage="undetermined", entry_date="1999",
             country="US", city="Mountain View", focus="Healthcare & Bio",
             note="Stroke thrombectomy device maker acquired by Stryker in 2011 (the firm's exit line); NEA VIII signed its 2007 "
                  "investors' rights agreement, but the 1999 round is not named."))

# conceptus
L.append(cls("conceptus", rng="below_1b", stage="undetermined", entry_date="1992", country="US", city="Mountain View",
             focus="Healthcare & Bio",
             note="Reproductive health device maker (Nasdaq CPTS) acquired by Bayer in 2013; the 1992 round is not named."))

# contra
_CT = "https://vcnewsdaily.com/contra/venture-capital-funding/gwwrsfvyfp"  # found by WebSearch, read with WebFetch
L.append(cls("contra", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_cite=_CT,
             stage_conf="high", entry_date="2021-11", country="US", focus="Consumer & Marketplaces",
             flags=["city_unknown"],
             rounds=[rnd("2021-11-03", "Series B", 30_000_000, "New Enterprise Associates", True, _CT, "press")],
             note="Independent-work platform; NEA led the $30M Series B of November 2021, with the Series A investors Unusual and "
                  "Cowboy following on (VC News Daily), matching the firm's post of 2021-11-02. No source read gives its city."))

# conviva
L.append(cls("conviva", status="private", rng="below_1b", stage="undetermined", entry_date="2006", city="Foster City",
             focus="SaaS",
             note="Streaming video analytics company in Foster City, still private; NEA first invested in 2006 (the firm's year, "
                  "earlier than the 2012 Form D) and joined the $44M 2013 round, but the entry round is not named."))

# corca
_CORCA = POST("investing-in-corca")
L.append(cls("corca", status="private", rng="below_1b", stage="Seed", stage_src="first_party", stage_cite=_CORCA,
             stage_conf="high", entry_date="2026-06", grad="censored", country="US", focus="DevTools & APIs",
             flags=["city_unknown"],
             rounds=[rnd("2026-06-10", "Seed", 7_800_000, "New Enterprise Associates; Nventures", True, _CORCA, "firm")],
             extra={**WV, "valuation_asof": "2026-09-30",
                    "valuation_citation": NEWS("corca", "Corca Research Raises $7.8M in Funding")},
             note="Math workspace software; the firm's post says NEA co-led the $7.8M seed with Nventures (announced 2026-06-10), "
                  "which a vendor calls a Series A. Momentum check 2026-09-30 (Google News): no later round or $1B mark; no source gives its city."))

# corvis
L.append(cls("corvis", status="acquired", rng="below_1b", stage="undetermined", entry_date="1998", country="US",
             city="Columbia", focus="Data Infrastructure",
             note="Optical networking company (Nasdaq CORV, later Broadwing Corporation) acquired by Level 3 in 2007; NEA VII held "
                  "4.6M shares at the IPO, the 1998 round is not named."))

# corxel
_CX = NEWS("corxel", "CORXEL Announces $287 million Series D1")
L.append(cls("corxel", status="private", rng="below_1b", stage="undetermined", entry_date="2024", country="US",
             city="Berkeley Heights", city_src="web_verified", focus="Healthcare & Bio",
             rounds=[rnd("2026-01-22", "Series D-1", 287_000_000, "RTW Investments", None, _CX, "company")],
             note="Cardiometabolic drug developer (oral GLP-1 CX11) in Berkeley Heights, New Jersey; the firm's card reads Seed in "
                  "2024, but the company had reached a $287M Series D-1 by January 2026 and no record names the round NEA bought."))

# coursera
_COUR = POST("charting-a-new-course")
L.append(cls("coursera", rng="1b_plus", usd=1.34e9, val_src="web_verified", val_cite=SA.format("cour"), asof="2026-09-30",
             stage="Series A", stage_src="first_party", stage_cite=_COUR, stage_conf="high", entry_date="2012-04",
             city="Mountain View", focus="Consumer & Marketplaces", flags=["stage_disputes_band"], extra=WV,
             rounds=[rnd("2012-04-18", "Series A", 16_000_000, None, True, _COUR, "firm")],
             note="Scott Sandell's post of 2012-04-18 announces the $16M Series A NEA backed with Kleiner Perkins, so the entry is "
                  "the A, not the 2015 filing the band read. Market cap $1.34B on 2026-09-30 (stockanalysis)."))

# courtyard
_CY = POST("courtyard-creating")
_CYA = NEWS("courtyard", "Collectibles platform Courtyard.io lands $30m Series A")
L.append(cls("courtyard", status="private", rng="below_1b", stage="Seed", stage_src="first_party", stage_cite=_CY,
             stage_conf="high", entry_date="2022-11", grad="graduated", grad_src="web_verified", grad_cite=_CYA,
             grad_conf="high", country="US", city="New York", city_src="web_verified", focus="Consumer & Marketplaces",
             flags=["model_disputes_source"],
             rounds=[rnd("2022-11-02", "Seed", 7_000_000, "New Enterprise Associates", True, _CY, "firm"),
                     rnd("2025-07-24", "Series A", 30_000_000, "Forerunner", None, _CYA, "press")],
             note="The firm's post of 2022-11-02 says NEA led the $7M seed; graduated with the $30M Series A Forerunner led in July "
                  "2025. Courtyard, Inc. gives a New York address on its site, so the Wikidata country GB is a wrong join."))

# cowboy-space
_CS = W("Cowboy Space Corporation")
L.append(cls("cowboy-space", status="private", rng="1b_plus", usd=2.0e9, val_src="web_verified",
             val_cite=SIBCITE("cowboy-space", "ivp"), asof="2026-05", stage="Series A", stage_src="web_verified",
             stage_cite=_CS, stage_conf="medium", entry_date="2025-04", country="US", city="San Carlos",
             focus="Industrial & Robotics", extra=WV,
             rounds=[rnd("2025-04", "Series A", 50_000_000, "Index Ventures; Interlagos", True, _CS, "press")],
             note="Formerly Aetherflux (base row aetherflux is the same company); NEA joined the $50M Series A of April 2025 "
                  "(Wikipedia). Marked at the $2B of the $275M Series B of May 2026, as in the IVP and Ribbit books."))

# crispr
L.append(cls("crispr", rng="1b_plus", usd=5.43e9, val_src="web_verified", val_cite=SA.format("crsp"), asof="2026-09-30",
             city="Zug", focus="Healthcare & Bio", extra=WV,
             note="CRISPR Therapeutics AG, domiciled and headquartered in Zug, Switzerland; market cap $5.43B on 2026-09-30 (stockanalysis)."))

# crowdbotics
_CB = NEWS("crowdbotics", "Crowdbotics raises $40M to help devs")
L.append(cls("crowdbotics", status="private", rng="below_1b", city="Berkeley", city_src="formd_address",
             focus="DevTools & APIs",
             rounds=[rnd("2023-01-25", "Series B", 40_000_000, None, True, _CB, "press")],
             extra={**WV, "valuation_asof": "2026-09-30", "valuation_citation": _CB},
             note="App-building platform in Berkeley (Form D address); NEA's Aaron Jacobson is a director on the Form D of its "
                  "$40M Series B of January 2023. Momentum check 2026-09-30 (Google News): no later priced round and no mark at or above $1B."))

# crowdmed
L.append(cls("crowdmed", status="defunct", rng="below_1b", stage="Seed", stage_src="web_verified",
             stage_cite=W("CrowdMed"), stage_conf="high", entry_date="2013", city="San Francisco",
             focus="Healthcare & Bio",
             note="Crowdsourced diagnosis site; Wikipedia names NEA among the investors in its $2.4M seed and the firm's card reads "
                  f"Seed in 2013. Defunct as in the a16z, General Catalyst, Khosla and YC books. {LEFT}"))

jl.write("c3a", L)
