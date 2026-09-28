#!/usr/bin/env python3
"""Batch 4 of the Sutter Hill Ventures grind (PRO-77): 45 rows, edify-corporation to lynk.

Run: NQ_TAG=b4 python3 judgments-4.py
Citations come from helpers (ARCH, W, NEWS), from files on disk (fts-hits.json,
cc-manifest.json), or are URLs a tool printed in this session (tc.py for
TechCrunch, WebSearch, curl -w for the stockanalysis and SEC pages).
"""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, ARCH, W, NEWS

N = 4
L = []
INV = Path(__file__).resolve().parents[1]


def FTS(registrant, url_part):
    """An SEC URL read from the on-disk EDGAR full-text sweep (sources/edgar/fts-hits.json)."""
    d = json.loads((INV / "sources/edgar/fts-hits.json").read_text())
    hits = [f["url"] for r in d["registrants"] if registrant.lower() in r["registrant"].lower()
            for f in r["filings"] if url_part in f["url"]]
    hits = list(dict.fromkeys(hits))
    if len(hits) != 1:
        raise SystemExit(f"FTS({registrant!r}, {url_part!r}) matched {len(hits)}")
    return hits[0]


def CC(key):
    """A Common Crawl capture URL of a firm page, read from sources/wayback/cc-manifest.json."""
    m = json.loads((INV / "sources/wayback/cc-manifest.json").read_text())
    return m[key]["capture_url"]


# ---- citations
TEAM2014 = CC("CC-MAIN-2014-10/20140310182239-team.html")   # Anderson, Baker, Bird, Coxe, Speiser, White bios
WYTHES = CC("CC-MAIN-2012/20120204073812-team_wythes.html.html")
INFN_IRA = FTS("INFINERA", "dex1010.htm")                    # 2005 A&R investors' rights agreement, S-1 exhibit
ELOY_10K = FTS("ELOYALTY", "c60662e10-k.txt")                # 2001 10-K exhibit list
ELOY_FORM10 = "https://www.sec.gov/Archives/edgar/data/1094348/0000950137-99-003924.txt"  # Form 10, 1999-11-05
SA_GRAL = "https://stockanalysis.com/stocks/gral/market-cap/"
SA_IONS = "https://stockanalysis.com/stocks/ions/market-cap/"
SA_IDXX = "https://stockanalysis.com/stocks/idxx/market-cap/"
TC_FDB = ("https://techcrunch.com/2013/11/12/foundationdb-raises-17m-for-database-similar-to-next-"
          "generation-google-technology-used-to-run-adwords/")
TC_FDB_APPLE = "https://techcrunch.com/2015/03/24/apple-acquires-durable-database-company-foundationdb/"
TC_FARECAST = "https://techcrunch.com/2007/01/30/farecast-takes-12-million-more/"
TC_FARECAST_MSFT = "https://techcrunch.com/2008/04/17/microsoft-acquires-farecast-for-115m/"
TC_FM_A = "https://techcrunch.com/2011/05/11/former-ebay-oracle-execs-raise-11-million-for-gift-network-freemonee/"
TC_FM_B = "https://techcrunch.com/2012/08/07/consumer-gift-network-freemonee-raises-34-million-series-b/"
TC_KADOINK_END = "https://techcrunch.com/2009/06/04/beware-the-venture-debt-kadoink-shuts-down-for-good/"
TC_INSTART_B = ("https://techcrunch.com/2013/04/16/instart-logic-raises-17m-from-andreessen-horowitz-greylock-"
                "to-improve-web-and-mobile-app-performance/")
TC_INSTART_C = "https://techcrunch.com/2014/05/13/instart-logic-bags-26m-in-series-c-funding-to-disrupt-cdns/"
TC_FEEDBURNER = "https://techcrunch.com/2007/05/23/100-million-payday-for-feedburner-this-deal-is-confirmed/"
PEHUB_FEEDBURNER = "https://www.pehub.com/2005/04/pe-week-wire-thursday-april-7/"
VF_LUCY = ("https://www.vfc.com/investors/news-events-presentations/press-releases/detail/404/"
           "vf-completes-acquisition-of-lucyr-womens-activewear-brand")
GRAIL_PR = NEWS("grail", "Illumina Forms New Company")
LR_KADOINK = NEWS("kadoink", "Kadoink Raises")

UND = "SHV's entry round is not on record, so the stage reads undetermined."

# ======================================================================
# Membership: the firm's own "Investment Partnerships" category (D6)
# ======================================================================
L.append(verdict(
    "golden-gate-capital", "not_member",
    "D6 (T5, the LP-stake class): the firm filed Golden Gate Capital under its own 'Investment Partnerships' "
    "category (2008 to 2017 listings) and described it as a private equity firm; its 2014 team page says Len "
    "Baker is responsible for SHV's investment in Golden Gate Capital, 'a private equity firm in San Francisco "
    "that Sutter Hill helped found in 2000'. The position is an interest in a fund manager and its "
    "partnerships, not venture equity in an operating company.",
    ec="site_listing", conf="high", cite=ARCH("golden-gate-capital")))

L.append(verdict(
    "helion-venture-partners", "not_member",
    "D6 (T5, the LP-stake class): listed 2008 to 2016 under the firm's own 'Investment Partnerships' category "
    "and described there as 'a stage independent, India-focused venture fund'. A fund interest, not an "
    "operating company.",
    ec="site_listing", conf="high", cite=ARCH("helion-venture-partners")))

L.append(verdict(
    "indus-international", "not_member",
    "Judged on the evidence, the row is out. Its only record is one 2008 page titled 'Indus' "
    "(shv.com/investment/indus.html), filed under the firm's own 'Investment Partnerships' category (D6), "
    "whose text describes Indus International's January 2007 combination with MDSI into Ventyx. That "
    "category's text does not identify the position: the same 2008 category pairs 'Biovest', which the 1999 "
    "table lists as 'Biovest Partners, medical investment partnership, Distributed', with the unrelated "
    "Biovest International's company description. Read either way, no venture position exists: as a "
    "partnership interest (an investment firm such as Indus Capital Partners, founded 2000, fits the "
    "category) it is the LP-stake class (T5); as Indus International it was a listed company from its 1997 "
    "formation until the 2006 to 2007 buyout that merged it into Ventyx, so any SHV purchase was a "
    "public-market or buyout position (T3), and no SEC filing in the 2001 to 2024 full-text sweep ties SHV "
    "to it. Worth Erik's look beside D6.",
    ec="site_listing", conf="medium", cite=ARCH("indus-international")))

# ======================================================================
# Public rows
# ======================================================================
L.append(cls(
    "grail",
    usd=5_920_000_000, rng="1b_plus", val_src="web_verified", val_cite=SA_GRAL, asof="2026-09-28",
    val_conf="high", extra={"valuation_range_source": "web_verified"},
    stage="Series A", stage_src="web_verified", stage_cite=GRAIL_PR, stage_conf="high",
    entry_date="2016-01-10",
    rounds=[rnd("2016-01-10", "Series A", 100_000_000, "Illumina and ARCH Venture Partners", True,
                GRAIL_PR, "company"),
            rnd("2017-02-28", "Series B", 914_024_940, None, None,
                "Form D 0001699031-17-000001 (first sale 2017-02-28; $1.21B sold by the 2018-01 amendment)",
                "filing"),
            rnd("2018-05-16", "Series C", 300_000_000, None, None, "Form D 0000950103-18-006536", "filing")],
    country="US", city="Menlo Park", city_src="formd_address", focus="Healthcare & Bio",
    note="Blood-based multi-cancer early detection, Menlo Park (Form D address and Wikipedia). Illumina formed "
         "GRAIL in January 2016 with an over-$100M Series A 'from Illumina and ARCH Venture Partners, with "
         "participating investments from Bezos Expeditions, Bill Gates and Sutter Hill Ventures' (GRAIL's own "
         "release, 2016-01-10); Jeff Bird signed the 2020 investors' rights agreement for SHV. Illumina bought "
         "GRAIL in 2021 and spun it off in June 2024 (Nasdaq: GRAL), so the row reads public. Market cap $5.92B "
         "on 2026-09-28 (stockanalysis) replaces the prefilled $1.9B float of 2025-06-30; the band stays "
         "1b_plus. The later rounds' figures are Form D amounts, SHV's part in them not on record."))

L.append(cls(
    "isis", status="public",
    usd=7_570_000_000, rng="1b_plus", val_src="web_verified", val_cite=SA_IONS, asof="2026-09-28",
    val_conf="high", extra={"valuation_range_source": "web_verified"},
    stage="undetermined",
    country="US", city="Carlsbad", city_src="web_verified", focus="Healthcare & Bio",
    note="Isis Pharmaceuticals (antisense drugs), founded 1989, renamed Ionis Pharmaceuticals in 2015, "
         "Carlsbad, California (Wikipedia). The firm lists it 1999 ('Public company') to 2016. Nasdaq: IONS, "
         "market cap $7.57B on 2026-09-28 (stockanalysis). " + UND + " The 1991 IPO prospectus predates EDGAR."))

L.append(cls(
    "idexx-laboratories-inc", status="public",
    usd=41_680_000_000, rng="10b_plus", val_src="web_verified", val_cite=SA_IDXX, asof="2026-09-28",
    val_conf="high", extra={"valuation_range_source": "web_verified"},
    stage="undetermined",
    country="US", country_src="web_verified", country_cite=W("IDEXX Laboratories"),
    city="Westbrook", city_src="web_verified", focus="Healthcare & Bio", flags=("model_disputes_source",),
    note="Veterinary diagnostics, incorporated 1983, headquartered in Westbrook, Maine (Wikipedia). The "
         "prefilled Wikidata country NL is its EMEA office in Hoofddorp, not the headquarters, so the country "
         "is disputed to US with the citation. The firm lists it in the 1999 table ('Public company') and "
         "2008 to 2016. Nasdaq: IDXX, market cap $41.68B on 2026-09-28 (stockanalysis). " + UND))

# ======================================================================
# Rows whose entry round is on record
# ======================================================================
L.append(cls(
    "foundation-db", status="acquired", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=TC_FDB, stage_conf="high", entry_date="2013-10-29",
    rounds=[rnd(None, "Seed (founders and angels)", None, None, None, TC_FDB, "press"),
            rnd("2013-10-29", "Series A", 17_000_000, "Sutter Hill Ventures", True, TC_FDB, "press")],
    country="US", city="Vienna", city_src="formd_address", focus="Data Infrastructure",
    note="Distributed ACID database, Vienna, Virginia. 'The Series A round was led by Sutter Hill Ventures' "
         "($17M, TechCrunch 2013-11-12); its Form D (0001591582-13-000001) gives first sale 2013-10-29 and "
         "lists Sam Pullara of SHV as director. The round followed a seed from the founders and angels in "
         "which SHV is not named. Apple bought FoundationDB in March 2015 (TechCrunch 2015-03-24)."))

L.append(cls(
    "farecast-com", status="acquired", rng="below_1b",
    stage="Growth", stage_src="web_verified", stage_cite=TC_FARECAST, stage_conf="high", entry_date="2007-01-30",
    rounds=[rnd(None, "first and second rounds", 8_500_000, None, False, TC_FARECAST, "press"),
            rnd("2007-01-30", "third round", 12_100_000, "Sutter Hill Ventures", True, TC_FARECAST, "press")],
    country="US", city="Seattle", city_src="web_verified", focus="Consumer & Marketplaces",
    note="Airfare prediction site, Seattle. SHV came in as a new investor in the third round, $12.1M announced "
         "2007-01-30, with new backers PAR Capital, Pinnacle Ventures and Erik Blachford and returning "
         "Greylock, Madrona and WRF Capital ($20.6M over three rounds, TechCrunch); a third priced round "
         "reads Growth. Microsoft bought Farecast in April 2008 for a reported $115M (TechCrunch); Jim "
         "White's team bio lists it as acquired by Microsoft."))

L.append(cls(
    "feedburner", status="acquired", rng="below_1b",
    stage="Growth", stage_src="web_verified", stage_cite=PEHUB_FEEDBURNER, stage_conf="medium",
    entry_date="2005-04",
    rounds=[rnd("2004", "Series A", 1_000_000, "Portage Venture Partners", False, TC_FEEDBURNER, "press"),
            rnd("2005-04", "Series B (second round, first close)", 7_000_000, "Mobius Venture Capital", True,
                PEHUB_FEEDBURNER, "press"),
            rnd("2005", "Series B (total, second close 2006 with Union Square Ventures)", 9_000_000,
                "Mobius Venture Capital", True, TC_FEEDBURNER, "press")],
    country="US", city="Chicago", focus="Media, Gaming & Advertising",
    note="RSS feed management and feed advertising for publishers, Chicago. SHV joined the second round: $7M "
         "reported by PE Week Wire on 2005-04-07, led by Mobius Venture Capital and 'joined by Sutter Hill "
         "Ventures and return backers Portage Venture Partners and Draper Fisher Jurvetson'. TechCrunch names "
         "it the $9M Series B (closed mid 2005, second close in 2006) after Portage's $1M Series A of 2004, so "
         "the entry reads Growth. The PE Hub page is behind a sign-in; its wording was read from the search "
         "result, hence medium confidence. Google bought FeedBurner in June 2007 (about $100M). Sibling "
         "union-square-ventures agrees (acquired, Chicago; USV's 2006 entry is the second close of the same "
         "Series B)."))

L.append(cls(
    "freemonee", status="defunct", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=TC_FM_A, stage_conf="high", entry_date="2010",
    rounds=[rnd("2010", "Series A", 11_000_000, None, True, TC_FM_A, "press"),
            rnd("2012-08-07", "Series B", 34_000_000, "Charles Ryan (UFG Asset Management)", True, TC_FM_B,
                "press")],
    country="US", city="San Francisco", focus="Fintech & Payments",
    note="Bank-card gift network. SHV was one of the five investors in the $11M Series A (Opus, Redpoint, SHV, "
         "Pinnacle, Contrarian Group; announced 2011-05-11, raised in 2010 per TechCrunch's 2012 report) and "
         "returned in the $34M Series B of August 2012. Status and city follow sibling redpoint-ventures "
         "(defunct, wound down after 2014, San Francisco); SHV's own listing ran 2012 to 2014 and no later "
         "event is on record. Jim White's team bio lists FreeMonee among his investments."))

L.append(cls(
    "kadoink", status="defunct", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=LR_KADOINK, stage_conf="high", entry_date="2008-01-14",
    rounds=[rnd("2008-01-14", "Series A", 7_000_000, "Sutter Hill Ventures", True, LR_KADOINK, "press")],
    country="US", city="San Francisco", city_src="web_verified", focus="Consumer & Marketplaces",
    note="Web telephony for group calls, group texts and audio sharing from the phone, San Francisco. "
         "'Kadoink announces $7M Series A funding with Sutter Hill Ventures' (2008-01-14); Andy Sheehan of SHV "
         "joined the board. Its venture lender Hercules seized the company in April 2009 and it shut down for "
         "good in June 2009 (TechCrunch), so the row reads defunct."))

L.append(cls(
    "infinera", rng="below_1b",
    stage="Growth", stage_src="web_verified", stage_cite=INFN_IRA, stage_conf="high", entry_date="2001",
    rounds=[rnd("2001", "Series A", 36_906_000, None, False, INFN_IRA, "filing"),
            rnd("2001", "Series B", 29_457_000, None, False, INFN_IRA, "filing"),
            rnd("2001", "Series C", 24_400_000, None, True, INFN_IRA, "filing")],
    city="San Jose", city_src="web_verified", focus="Data Infrastructure",
    note="Optical networking systems on its own photonic integrated circuits; headquarters San Jose since 2019 "
         "(Sunnyvale before). SHV entered at the Series C: the 2005 amended investors' rights agreement filed "
         "with the 2007 S-1 lists Sutter Hill Ventures, A California Limited Partnership and the Sutter Hill "
         "Entrepreneurs Funds (AI) and (QP) among the Series C holders (and again among D and E), but not "
         "among the Series A or B holders. The firm's own page says Infinera raised $88M in 2001, which the "
         "S-1's Series A to C liquidation preferences match (amounts in rounds). Series C reads Growth. Nokia "
         "bought Infinera (agreed June 2024, closed 2025). Siblings accel and benchmark agree (acquired, US)."))

L.append(cls(
    "eloyalty", rng="below_1b",
    stage="Growth", stage_src="web_verified", stage_cite=ELOY_FORM10, stage_conf="medium", entry_date="1999-08-13",
    rounds=[rnd("1999-08-13", "pre-spin-off private placement of common stock", None, None, True, ELOY_FORM10,
                "filing")],
    country="US", city="Chicago", focus="SaaS",
    note="eLoyalty, CRM consulting and systems spun off from Technology Solutions Company (TSC) in February "
         "2000; renamed Mattersight Corporation in May 2011 after selling its contact-center business; NICE "
         "bought Mattersight by tender offer in 2018 (Schedule 14D-9 of 2018-05-10, Form 15 of 2018-08-30), so "
         "the row reads acquired. Last headquarters Chicago (EDGAR business address). SHV's entry is the Common "
         "Stock Purchase and Sale Agreement of 1999-08-13 among TSC, eLoyalty, SHV and TCV (Exhibit 10.3 of "
         "eLoyalty's Form 10; also listed in its 2001 10-K): SHV bought 1,200,000 eLoyalty shares and 250,000 "
         "TSC shares before the spin-off and got a board nominee. A pre-listing placement at scale beside TCV "
         "reads Growth; the record names no series, hence medium confidence. The base carries this company "
         "twice: this row and 'mattersight' (the 2013 to 2017 listing)."))

# ======================================================================
# Rows whose entry round is not on record
# ======================================================================
L.append(cls(
    "instart-logic", status="acquired", rng="below_1b", stage="undetermined",
    rounds=[rnd("2012-02", "Series A", 9_000_000, None, None, W("Instart Logic"), "press"),
            rnd("2013-04-16", "Series B", 17_000_000, "Tenaya Capital", True, TC_INSTART_B, "press"),
            rnd("2014-05-13", "Series C", 26_000_000, None, True, TC_INSTART_C, "press")],
    country="US", city="Palo Alto", focus="Data Infrastructure",
    note="Web and application delivery (a CDN replacement), Palo Alto. SHV is named in the $17M Series B of "
         "April 2013 (TechCrunch; Tenaya Capital led) and the $26M Series C of May 2014. The $9M Series A of "
         "February 2012 has no investor list on record and no report says SHV was new in the B, so the B is "
         "only a ceiling on SHV's entry and the stage reads undetermined (the Series A investors would settle "
         "it). Mike Speiser's team bio: responsible for the firm's investment in Instart Logic. Akamai "
         "acquired Instart's customers and select IP on 2020-02-27 (Wikipedia), which reads acquired. "
         "Sibling a16z agrees (acquired, Palo Alto)."))

L.append(cls(
    "edify-corporation", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="Santa Clara", focus="SaaS",
    note="Interactive voice response and customer self-service software, Santa Clara. The firm's 1999 table: "
         "'Public company' (IPO 1996); S1 Corporation (Security First Technologies) bought it in November "
         "1999, and Edify's Form 15 followed on 1999-11-12. Tench Coxe's team bio lists Edify among his "
         "investments. " + UND + " Edify's EDGAR record starts in May 1996, after its IPO prospectus. Sibling "
         "greylock agrees (acquired, Santa Clara). First Round Capital's 'Edify' (Santa Monica, a 2019 entry, "
         "bought by Avaya in 2024) is a different company."))

L.append(cls(
    "evernet", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Los Angeles", city_src="web_verified", focus="Data Infrastructure",
    note="EverNet Systems, a Los Angeles network systems-integration company. The firm's 1999 table: "
         "'Acquired by Control Data'; Control Data Systems completed the purchase in June 1993 for about $11M "
         "in cash and $11M in stock (UPI, 1993-06-07). " + UND))

L.append(cls(
    "forte-software", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Oakland", focus="DevTools & APIs",
    note="Forte Software, client/server and application-integration development tools, Oakland; IPO 1996. "
         "The firm's 1999 table: 'Acquired by Sun' (1999). " + UND + " Sibling greylock agrees (acquired, "
         "Oakland)."))

L.append(cls(
    "grain-communications-group", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Sarasota", city_src="web_verified", focus="Data Infrastructure",
    note="Wireless tower company founded by David Grain in 2006, Sarasota, Florida (100 N Washington Blvd, its "
         "business address). The firm's own listing, 2010 to 2016, says it 'has been acquired by the Grain "
         "Infrastructure Fund, L.P.', so the row reads acquired. Sibling general-catalyst reads it 'unknown' "
         "with no source; this row holds the fresher first-party evidence. " + UND))

L.append(cls(
    "grand-junction", status="acquired", rng="below_1b", stage="undetermined",
    country="US", country_src="model_knowledge", city="Fremont", focus="Data Infrastructure",
    flags=("model_disputes_source",),
    note="Grand Junction Networks, Fast Ethernet switching, Fremont, California. The firm's 1999 table and "
         "2010 listing: acquired by Cisco Systems (1995; Cisco's own history of the Catalyst 1900, which began "
         "as the Grand Junction FastSwitch). The prefilled Wikidata country GB is a wrong join on the name; "
         "the company was American. Tench Coxe's team bio lists Grand Junction among his investments. " + UND))

L.append(cls(
    "hybritech", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="San Diego", focus="Healthcare & Bio",
    note="Monoclonal antibody diagnostics, San Diego, founded 1978. The firm's 1999 table and 2013 listing: "
         "acquired by Eli Lilly (1986); Beckman later bought it from Lilly (Wikipedia, Beckman Coulter). David "
         "Anderson's team bio lists a Hybritech board seat. " + UND))

L.append(cls(
    "i-pro", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="San Francisco", focus="Media, Gaming & Advertising",
    note="I/PRO (Internet Profiles Corporation), web audience measurement and traffic audits for publishers "
         "and advertisers, San Francisco. The firm's 1999 table: 'Acquired by CMGI'. " + UND))

L.append(cls(
    "ibalance", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="Boulder", city_src="web_verified", focus="Healthcare & Bio",
    note="iBalance Medical, a high tibial osteotomy implant system for knee malalignment, Boulder, Colorado. "
         "Arthrex bought it and took the iBalance HTO System worldwide (announced March 2012, Healio "
         "2012-03-31); Arthrex still sells the system. " + UND + " The company filed no electronic Form D."))

L.append(cls(
    "ideas", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Bloomington", focus="SaaS",
    note="IDeaS (Integrated Decisions and Systems), hotel revenue-management software founded 1989, "
         "Bloomington (Minneapolis area), Minnesota. 'IDeaS was acquired by data company SAS in 2008' (HOTELS "
         "magazine, 2026-09-04). The firm's 1999 table calls it 'Public company', which no other source "
         "supports. " + UND))

L.append(cls(
    "idun", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="San Diego", focus="Healthcare & Bio",
    note="Idun Pharmaceuticals, apoptosis (caspase inhibitor) drug developer, San Diego. The firm's 2013 to "
         "2016 listing gives only the name 'idun'; its team page identifies it: Jeff Bird 'was formerly a "
         "director at ... Idun Pharmaceuticals, (acquired by Pfizer in 2005)'. " + UND))

L.append(cls(
    "index-technology", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Cambridge", focus="DevTools & APIs",
    note="Index Technology, CASE tools, Cambridge, Massachusetts. The firm's 1999 table: 'Merged into "
         "Intersolv' (1991), which reads acquired. " + UND + " Sibling greylock agrees (acquired, Cambridge). "
         "Bain Capital Ventures' 'Index' (Sydney, a 2005 seed) and Y Combinator's 'Index' (San Francisco) are "
         "different companies."))

L.append(cls(
    "indicative-software-inc", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Fort Collins", city_src="web_verified", focus="Data Infrastructure",
    note="Indicative Software, business service management and IT monitoring software, Fort Collins, "
         "Colorado. The firm's 2008 page: 'acquired by Nimsoft'; Nimsoft bought it in April 2008 and set up an "
         "R&D base in Fort Collins (Wikipedia, Nimsoft). " + UND))

L.append(cls(
    "infomedics", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Woburn", city_src="web_verified", focus="Healthcare & Bio",
    note="InfoMedics, patient-experience data and interactive patient communications for pharmaceutical "
         "marketers, Woburn, Massachusetts. Physicians Interactive (later Aptus Health) bought it in late 2012 "
         "(Covington Associates, InfoMedics' M&A adviser). The firm lists it 1999 ('Private company') to "
         "2012. " + UND))

L.append(cls(
    "ingres", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Alameda", focus="Data Infrastructure",
    note="Ingres Corporation (founded 1980 as Relational Technology Inc.), relational database software, "
         "Alameda, California. The firm's 1999 table: 'Acquired by ASK'; ASK bought it in November 1990 "
         "(Wikipedia, Ingres). " + UND))

L.append(cls(
    "inquira", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="San Bruno", focus="SaaS",
    note="InQuira, natural-language self-service search and knowledge management for customer service, San "
         "Bruno, California. The firm's 2013 listing: 'acquired by Oracle in July, 2011'; Jim White's team "
         "bio lists it as acquired by Oracle. " + UND))

L.append(cls(
    "integrated-genetics", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Framingham", focus="Healthcare & Bio",
    note="Integrated Genetics, DNA probe diagnostics and cardiovascular therapeutics, Framingham, "
         "Massachusetts. The firm's 1999 table: 'Acquired by Genzyme' (1989, Wikipedia on Genzyme). David "
         "Anderson's team bio lists an Integrated Genetics board seat. " + UND))

L.append(cls(
    "interventional-technologies", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="San Diego", focus="Healthcare & Bio",
    note="InterVentional Technologies (IVT), cardiology catheters, San Diego. The firm's 2013 listing: 'IVT is "
         "now a part of Boston Scientific' (acquired 2001). " + UND))

L.append(cls(
    "ipin", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="San Francisco", city_src="web_verified", focus="Fintech & Payments",
    note="iPIN, a 1998 San Francisco start-up billing web micropayments to the buyer's internet-service "
         "account, backed by Accel, SHV and others ($14M from Accel, SHV and Comdisco, per Computerworld). "
         "Its service debuted in 1999 and 'was never widely adopted' (Wikipedia, Micropayment); no source "
         "gives the company's fate, so status reads unknown. The firm's 1999 table: 'Private company'. No "
         "source names the round SHV entered."))

L.append(cls(
    "ipsilon-networks", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Sunnyvale", focus="Data Infrastructure",
    note="Ipsilon Networks, IP switching, Sunnyvale. The firm's 1999 table: 'Acquired by Nokia' (1997). " + UND +
         " Sibling greylock agrees (acquired, Sunnyvale)."))

L.append(cls(
    "jp-kids", status="unknown", rng="below_1b", stage="undetermined",
    country="US", city="San Francisco", city_src="web_verified", focus="Media, Gaming & Advertising",
    note="JP Kids, a children's television and media company founded in 1996 by Jim Steyer (producer of The "
         "Famous Jett Jackson for the Disney Channel), San Francisco. The firm's 1999 table: 'Private "
         "company'. Steyer founded Common Sense Media in 2003, but no source gives JP Kids' own fate, so status "
         "reads unknown. " + UND))

L.append(cls(
    "kalypto-medical-inc", status="acquired", rng="below_1b", stage="undetermined",
    rounds=[rnd("2007-10-01", "Reg D offering (paper notice, as IASIS Medical)", None, None, None,
                "EDGAR REGDEX 9999999997-07-043025, amended 2008-04-29", "filing"),
            rnd("2009-11-20", "Form D offering", 8_375_000, None, None,
                "Form D 0001414237-09-000003 (Bill Younger, SHV, a director)", "filing")],
    country="US", city="Mendota Heights", city_src="formd_address", focus="Healthcare & Bio",
    note="Negative-pressure wound therapy, Mendota Heights, Minnesota (formerly IASIS Medical). The firm's "
         "2013 listing: 'acquired by Smith & Nephew, Inc. in May 2012'. Its first offering was a paper Reg D "
         "notice of 2007-10-01 and its first electronic Form D (first sale 2009-11-20, $8,375,000) lists SHV's "
         "Bill Younger as a director; no source names the round SHV entered, so the stage reads undetermined."))

L.append(cls(
    "lancet-medical", status="acquired", rng="below_1b", stage="undetermined",
    country="US", focus="Healthcare & Bio", flags=("city_unknown",),
    note="Lancet Medical, clinical laboratories. The firm's 1999 table: 'Acquired by Metpath' (MetPath, the US "
         "laboratory chain that later became part of Quest Diagnostics). No source places the company's city "
         "or dates the sale; country US is inferred from the acquirer and the firm's domestic book of that "
         "era. " + UND))

L.append(cls(
    "legato-systems", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Mountain View", focus="Data Infrastructure",
    note="Legato Systems, storage management software founded 1988, Mountain View; IPO 1995. The firm's own "
         "listing: 'acquired by EMC' (2003). Tench Coxe's team bio lists Legato among his investments. " + UND +
         " Sibling greylock agrees (acquired, Mountain View)."))

L.append(cls(
    "lifescan", city="Malvern", city_src="web_verified", rng="below_1b", stage="undetermined",
    focus="Healthcare & Bio",
    note="Blood glucose monitoring. The firm's 1999 table: 'Acquired by Johnson & Johnson' (1986). J&J sold "
         "LifeScan to Platinum Equity in 2018; it went through Chapter 11 and emerged on 2025-12-08 as "
         "LifeScan Enterprises LLC, headquartered in Malvern, Pennsylvania (Wikipedia), its last known "
         "headquarters (Milpitas, California in the J&J years). " + UND))

L.append(cls(
    "line-6", city="Calabasas", city_src="web_verified", rng="below_1b", stage="undetermined",
    focus="Consumer & Marketplaces",
    note="Digital modeling guitar amplifiers and effects, Calabasas, California; a Yamaha subsidiary since 2014 "
         "(Wikipedia). Len Baker of SHV sat on its board (team page). The firm's 1999 table: 'Private "
         "company'. " + UND + " Sibling redpoint-ventures agrees (acquired, Calabasas); focus follows the "
         "consumer-device rule, where Redpoint's row reads Industrial & Robotics."))

L.append(cls(
    "linear-technology-corporation", status="acquired", rng="below_1b", stage="undetermined",
    rounds=[rnd("1981", "start-up funding (the firm's words; no series named)", None, None, True, TEAM2014, "firm")],
    country="US", city="Milpitas", city_src="web_verified", focus="Industrial & Robotics",
    note="Analog integrated circuits, founded 1981, Milpitas (Wikipedia). The firm listed it 2010 to 2016; its "
         "team pages say David Anderson was 'responsible for the firm's start-up funding of ... Linear "
         "Technology' and that Paul Wythes led the investment. 'Start-up funding' names no series (it straddles "
         "Seed and Series A), so the stage reads undetermined. Analog Devices bought Linear Technology in March "
         "2017. The company is not in the firm's 1999 table, although decisions D7's example list says it is. "
         "Sibling sequoia-capital ('Linear Technology') agrees (acquired, Milpitas); the accel and "
         "sequoia-capital rows named 'Linear' (San Francisco software, $1.25B) are a different company."))

L.append(cls(
    "liquid-software", status="unknown", rng="below_1b", stage="undetermined",
    country="US", focus="DevTools & APIs", flags=("city_unknown",),
    note="Liquid Software, integration software, listed only in the firm's 1999 table ('Private company'). "
         "Google News and TechCrunch searches found nothing more, so its fate and city are not on record and "
         "status reads unknown; country US is inferred from the firm's domestic book of that era. " + UND))

L.append(cls(
    "logic-modeling", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Beaverton", focus="Industrial & Robotics",
    note="Logic Modeling, simulation models of chips and hardware modeling systems for electronic design, "
         "Beaverton, Oregon. The firm's 1999 table: 'Acquired by Synopsys' (1994, EEJournal's EDA history). "
         + UND + " Sibling sequoia-capital agrees (acquired, US)."))

L.append(cls(
    "lsi-logic-corporation", country="US", city="San Jose", rng="below_1b", stage="undetermined",
    rounds=[rnd("1981", "start-up funding (the firm's words; no series named)", None, None, True, TEAM2014, "firm")],
    focus="Industrial & Robotics",
    note="ASIC and storage chips (LSI Corporation from 2007), San Jose at the end. Avago bought it for $6.6B in "
         "May 2014 (Wikipedia). The firm listed it 2010 to 2016, and David Anderson's team bio credits him with "
         "'the firm's start-up funding of ... LSI Logic'; Wikipedia's account of the initial $6M of 1981 names "
         "KPCB, IVP and Technical Development Capital without an exhaustive list. 'Start-up funding' names no "
         "series, so the stage reads undetermined. The company is not in the firm's 1999 table, although "
         "decisions D7's example list says it is. Sibling sequoia-capital agrees (acquired, San Jose)."))

L.append(cls(
    "lucy", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
    country="US", country_src="web_verified", country_cite=VF_LUCY, city="Portland", city_src="web_verified",
    focus="Consumer & Marketplaces", flags=("model_disputes_source",),
    note="Lucy (Lucy.com, then Lucy Activewear), women's activewear retailer founded 1999, Portland, Oregon. "
         "Backed by SHV, Maveron, Oak Investment Partners and Lone Pine; VF completed its purchase on "
         "2007-08-27 ('Portland, Oregon-based lucy', VF's release) and later folded the brand into The North "
         "Face. The prefilled Wikidata country BG is a wrong join on the name. No source found names the "
         "round SHV entered, so the stage reads undetermined. Felicis's 'Lucy' (a private seed-stage company) "
         "is a different company."))

L.append(cls(
    "lynk", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Atlanta", focus="Fintech & Payments",
    note="Lynk Systems, merchant card processing, ATM and EBT transaction services, founded 1991, Atlanta (the "
         "firm's own listing). The Royal Bank of Scotland agreed to buy it for $525M (Finextra, 2004-08-03) "
         "and the firm's 2013 listing says it was acquired by the Royal Bank of Scotland. Tench Coxe's team "
         "bio lists Lynk Systems among his investments. " + UND))


if __name__ == "__main__":
    seen = [x["slug"] for x in L]
    batch = [i["slug"] for i in json.loads((jl.Q / f"batch-{N:03d}.json").read_text())]
    missing = sorted(set(batch) - set(seen))
    extra = sorted(set(seen) - set(batch))
    if missing or extra:
        raise SystemExit(f"coverage: missing {missing}, extra {extra}")
    jl.write(f"batch-{N:03d}", L)
