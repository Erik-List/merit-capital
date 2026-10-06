"""PRO-80 Bessemer, second pass s21, file b: entry stages from cited rounds (press, filings, Wikipedia) and from
named rounds at medium confidence, plus statuses, cities and countries settled for the newer rows."""
import json
from pathlib import Path

import judge_lib as jl

A = jl.ARCH
PK = json.loads((Path(__file__).resolve().parent / "evidence-pack.json").read_text())
BVP = "Bessemer Venture Partners"

TC_YOTPO = "https://techcrunch.com/2016/06/14/yotpo-series-c/"
CS_VERODIN = jl.NEWS("verodin", "raises $21 million Series B")
TC_INFINIO = ("https://techcrunch.com/2013/02/12/virtual-storage-performance-company-infinio-raises-10m-from-"
              "highland-capital-and-bessemer-venture-partners/")
CEDU_F1 = "https://www.sec.gov/Archives/edgar/data/1411419/000119312507253192/df1.htm"
WEAV_S1 = "https://www.sec.gov/Archives/edgar/data/1609151/000162828021020169/weaves-1.htm"
UQ_ZOPA_JUN = "https://www.unquote.com/unquote/news/78756/uk-zopa-gains-additional-usd5m-backing-for-transatlantic-launch"
UQ_ZOPA_APR = "https://www.unquote.com/unquote/news/88392/germany-uk-wellington-partners-back-zopa-in-further-round"
VB_ZOPA = "https://venturebeat.com/technology/zopa-raises-129m-more-to-expand-online-lending-marketplace"
W_IID = jl.W("Internet Identity")
AW_WRAP = jl.NEWS("wrapbook", "Wrapbook Raises $20M to Simplify")
TC_SMULE = "https://techcrunch.com/2009/12/16/app-store-champ-smule-raises-another-8-million/"
TC_SMULE_B = "https://techcrunch.com/2009/02/12/innovative-iphone-developer-smule-raises-39-million/"
W_MIA = jl.W("MiaSolé")
TC_SIANO10 = "https://techcrunch.com/2010/01/11/siano-lands-23-5-million-for-mobile-tv-receiver-chips/"
TC_SIANO11 = "https://techcrunch.com/2011/05/24/siano-raises-another-20-million-for-mobile-tv-receiver-chips/"
TARA_S1 = "https://www.sec.gov/Archives/edgar/data/1359931/000104746914007662/a2221427zs-1.htm"
BG_ALC = jl.NEWS("alcresta-pharmaceuticals", "Newton firm raises")
MIT_WS = jl.NEWS("watershed", "Helping scientists run complex data analyses")
TC_WAY = "https://techcrunch.com/2010/09/01/verifone-acquires-way-systems-for-6-million-upfront-and-3-million-earn-out/"
VCC_AST = jl.NEWS("applied-solar-technologies", "raises $40M from Future Fund")
HIST_FG = PK["fg-wireless"]["history"]["capture_url"]

lines = [
    # ---- cited rounds naming Bessemer
    jl.cls("yotpo", stage="Growth", stage_src="web_verified", stage_cite=TC_YOTPO, stage_conf="high",
           rounds=[jl.rnd("2016-06-14", "Series C", amount_usd=22000000, lead=BVP, firm_in_round=True,
                          source=TC_YOTPO, source_type="press")],
           note="Second pass: TechCrunch (2016-06-14) reports '$22 million in Series C funding', with Bessemer "
                "Venture Partners leading 'along with participation from existing investors', so Bessemer entered "
                "at the Series C, Growth; the firm's own date is 2016-06-02."),
    jl.cls("verodin", stage="Growth", stage_src="web_verified", stage_cite=CS_VERODIN, stage_conf="high",
           city="McLean", city_src="web_verified",
           rounds=[jl.rnd("2018-07-17", "Series B", amount_usd=21000000, lead="TenEleven Ventures; " + BVP,
                          firm_in_round=True, source=CS_VERODIN, source_type="press")],
           note="Second pass: CyberScoop (2018-07-17) says the $21M Series B was led by TenEleven Ventures and "
                "Bessemer Venture Partners, so Growth; the firm's own close date 2018-06-22 is kept. The same "
                "article places the company in McLean, Virginia."),
    jl.cls("infinio-systems", stage="Series A", stage_src="web_verified", stage_cite=TC_INFINIO, stage_conf="high",
           rounds=[jl.rnd(None, "Seed", amount_usd=2000000, lead="Lightspeed Venture Partners",
                          firm_in_round=False, source=TC_INFINIO, source_type="press"),
                   jl.rnd("2013-02-12", "Series A", amount_usd=10000000, lead="Highland Capital Partners; " + BVP,
                          firm_in_round=True, source=TC_INFINIO, source_type="press")],
           note="Second pass: TechCrunch (2013-02-12) reports 'a $10 million Series A round from Highland Capital "
                "Partners and Bessemer Venture Partners' after a $2M seed from Lightspeed and Founder Collective, "
                "so the entry is the Series A (the firm dates its close 2012-08-22). Status still unknown: a "
                "Google News search on 2026-10-06 returned nothing about the company's fate."),
    jl.cls("chinaedu-com", status="acquired", stage="Growth", stage_src="web_verified", stage_cite=CEDU_F1,
           stage_conf="high", entry_date="2007-03-09",
           rounds=[jl.rnd("2005-07", "Series C", firm_in_round=False, source=CEDU_F1, source_type="filing"),
                   jl.rnd("2007-03-09", "Series D", amount_usd=7578737, firm_in_round=True, source=CEDU_F1,
                          source_type="filing")],
           note="Second pass: the November 2007 F-1 says 'In March 2007, we issued an aggregate of 1,968,503 Series "
                "D preferred shares' to investors 'including ... certain affiliated funds of Bessemer Venture "
                "Partners' and lists the Bessemer VI funds' purchases on 2007-03-09, so Growth. EDGAR shows a "
                "going-private transaction (Schedule 13E3, January to April 2014) and deregistration on "
                "2014-05-05, so acquired: taken private by a buyer group in April 2014."),
    jl.cls("weave", stage="Growth", stage_src="web_verified", stage_cite=WEAV_S1, stage_conf="medium",
           rounds=[jl.rnd("2017-08-11", "Series B-1", amount_usd=22008000, firm_in_round=True, source=WEAV_S1,
                          source_type="filing"),
                   jl.rnd("2018-11", "Series C", amount_usd=37500000, firm_in_round=True, source=WEAV_S1,
                          source_type="filing"),
                   jl.rnd("2019-10", "Series D", amount_usd=70000000, firm_in_round=True, source=WEAV_S1,
                          source_type="filing")],
           note="Second pass: the S-1 dates the Series B-1 stock purchase agreement 2017-08-11 and says Series B-1 "
                "shares were issued from then to 2018-05-10, the only preferred sold in that window; the firm's own "
                "date 2017-09-27 falls inside it, and the $3.31M the S-1 table shows is Bessemer's Series C "
                "purchase of November 2018. Entry read as the Series B-1, Growth, at medium confidence."),
    jl.cls("zopa", stage="Growth", stage_src="web_verified", stage_cite=UQ_ZOPA_JUN, stage_conf="medium",
           rounds=[jl.rnd("2006-04-03", "Second round", amount_usd=15000000, firm_in_round=True,
                          source=UQ_ZOPA_APR, source_type="press"),
                   jl.rnd("2006-06-22", "Addition to the second round", amount_usd=5000000, firm_in_round=None,
                          source=UQ_ZOPA_JUN, source_type="press"),
                   jl.rnd("2007-03-20", "Later round", amount_usd=12900000, lead=BVP, firm_in_round=True,
                          source=VB_ZOPA, source_type="press")],
           note="Second pass: unquote (2006-06-22) reports 'the $15m recently raised by Bessemer Venture Partners, "
                "Benchmark Capital and Wellington Partners', and its item of 2006-04-03 calls that $15m 'a second "
                "round of financing'; the firm's own date is 2006-02-15, a year after the launch round Balderton "
                "(then Benchmark Europe) lists as its Series A. Entry at the second round, Growth; medium because "
                "the April item muddles which investors were in the first round. VentureBeat (2007-03-20) calls "
                "Bessemer 'an existing investor' leading the next $12.9M."),
    jl.cls("internet-identity-iid", stage="Series A", stage_src="web_verified", stage_cite=W_IID,
           stage_conf="medium",
           rounds=[jl.rnd("2013", "First round of institutional funding", amount_usd=8000000, lead=BVP,
                          firm_in_round=True, source=W_IID, source_type="press")],
           note="Second pass: Wikipedia says 'In 2013, IID accepted its first round of institutional funding for $8 "
                "million from Bessemer Venture Partners', read as Series A; the firm's own date is 2013-10-25."),
    jl.cls("wrapbook", stage="Growth", stage_src="web_verified", stage_cite=AW_WRAP, stage_conf="high",
           rounds=[jl.rnd("2024-09-24", "Series B extension", amount_usd=20000000, lead=BVP, firm_in_round=True,
                          source=AW_WRAP, source_type="press")],
           note="Second pass: AlleyWatch (September 2024) quotes the company: 'We recently raised $20M in a Series B "
                "extension round led by Bessemer Venture Partners', at a $750M valuation, so Growth. A Google News "
                "search on 2026-10-06 shows no later priced round."),
    jl.cls("sonic-mule", stage="Seed", stage_src="web_verified", stage_cite=TC_SMULE, stage_conf="high",
           entry_date="2008-06-25", grad="graduated", grad_src="web_verified", grad_cite=TC_SMULE,
           grad_conf="high", city="Salt Lake City", city_src="web_verified",
           rounds=[jl.rnd("2008-06-25", "Seed", amount_usd=1600000, lead=BVP, firm_in_round=True, source=TC_SMULE,
                          source_type="press"),
                   jl.rnd("2009-02-12", "Series B", amount_usd=3900000, lead="Granite Ventures", firm_in_round=True,
                          source=TC_SMULE_B, source_type="press"),
                   jl.rnd("2009-12-16", "Later round", amount_usd=8000000, lead="Shasta Ventures",
                          firm_in_round=True, source=TC_SMULE, source_type="press")],
           note="Second pass: TechCrunch (2009-12-16) says 'Bessemer fueled Smule's $1.6 million seed round, and "
                "joined Granite Ventures and Maple Investments for their $3.9 million Series B', so the entry is "
                "the Seed and the named Series B of February 2009 graduates it. This row is the same company as "
                "the base row smule: the entry date 2008-06-25 is the firm's own date on that listing, and the "
                "city follows it (Salt Lake City, Wikipedia)."),

    # ---- named rounds at medium confidence
    jl.cls("miasol", stage="Growth", stage_src="model", stage_conf="medium",
           rounds=[jl.rnd("2004", "Initial raise", lead="VantagePoint Venture Partners", firm_in_round=False,
                          source=W_MIA, source_type="press"),
                   jl.rnd("2005-06", "Series B", amount_usd=16000000, lead="Kleiner Perkins Caufield & Byers",
                          firm_in_round=None, source=W_MIA, source_type="press"),
                   jl.rnd("2006-10", "Later round", amount_usd=35000000, firm_in_round=None, source=W_MIA,
                          source_type="press")],
           note="Second pass: Wikipedia lists an initial raise in 2004 led by VantagePoint, a $16M B round in June "
                "2005 led by Kleiner Perkins and $35M in October 2006. The firm's own year is 2005, the year of "
                "the B round and of no other, so the entry is read as the Series B, Growth, at medium confidence "
                "(Wikipedia does not name Bessemer). Hanergy bought the company in January 2013 (Wikipedia)."),
    jl.cls("siano-mobile-silicon", stage="Growth", stage_src="model", stage_conf="medium",
           rounds=[jl.rnd("2006-03-30", "Second round", firm_in_round=True, source=None, source_type="firm"),
                   jl.rnd("2010-01-11", "Later round", amount_usd=23500000, firm_in_round=True, source=TC_SIANO10,
                          source_type="press"),
                   jl.rnd("2011-05-24", "Later round", amount_usd=20000000, lead="Jerusalem Venture Partners",
                          firm_in_round=None, source=TC_SIANO11, source_type="press")],
           note="Second pass: TechCrunch says Siano was founded in late 2004 and names Bessemer among the investors "
                "of its $23.5M round of January 2010 beside the founding backers JVP, DFJ Tamir Fishman and Star. "
                "Bessemer's own date is 2006-03-30, the company's second round (recalled as a Series B that "
                "Bessemer led), so Growth from knowledge at medium confidence. Status still unknown: no news of a "
                "sale or closure found on 2026-10-06."),
    jl.cls("proteon-therapeutics", stage="Growth", stage_src="model", stage_conf="medium",
           rounds=[jl.rnd("2009-04", "Series B", firm_in_round=True, source=None, source_type="press"),
                   jl.rnd("2011-08-02", "Series C", amount_usd=15183371, firm_in_round=None, source=TARA_S1,
                          source_type="filing"),
                   jl.rnd("2014-05-13", "Series D", firm_in_round=None, source=TARA_S1, source_type="filing")],
           note="Second pass: the 2014 S-1 lists Series A, A-1, B, C (August 2011) and D (May 2014) preferred and a "
                "March 2009 option agreement with a large pharmaceutical company, but does not date the Series B "
                "or name its buyers. Bessemer's own date is 2009-04-17, recalled as the Series B that closed with "
                "the Novartis option, so Growth from knowledge at medium confidence. The S-1 gives Waltham as the "
                "2014 headquarters; the city stays with the successor Protara."),
    jl.cls("abacus", stage="Seed", stage_src="model", stage_conf="medium",
           rounds=[jl.rnd("2014-05", "Seed", firm_in_round=True, source=None, source_type="press")],
           note="Second pass: Abacus came out of Y Combinator's Winter 2014 batch (TechCrunch, 2014-02-18, New "
                "York) and the firm's own date is 2014-05-14, the seed round it joined with General Catalyst and Google "
                "Ventures two months after demo day, named from knowledge at medium confidence; no page read states it. "
                "TechCrunch dates the Certify acquisition to July 2018. The Menlo row named Abacus is a different "
                "company. Graduation left for the graduation pass."),
    jl.cls("verata-health", stage="Series A", stage_src="model", stage_conf="medium",
           city="Minneapolis", city_src="web_verified",
           rounds=[jl.rnd("2019", "Series A", amount_usd=12000000,
                          lead="BlueCross BlueShield Venture Partners; " + BVP, firm_in_round=True, source=None,
                          source_type="press")],
           note="Second pass: the firm's post says it invested in 2019; the round is the $12M Series A of September "
                "2019 that Bessemer co-led with BlueCross BlueShield Venture Partners, named from knowledge at "
                "medium confidence (Google News returned no report of it). The Star Tribune headline of 2020-12-06 "
                "reads 'Minneapolis-based Verata Health bought for $120M', so the city is corrected from San "
                "Francisco."),
    jl.cls("alcresta-pharmaceuticals", stage="Series A", stage_src="model", stage_conf="medium",
           rounds=[jl.rnd("2011-09-09", "Series A", amount_usd=10000000, firm_in_round=True, source=None,
                          source_type="firm"),
                   jl.rnd("2013-07-22", "Series B", amount_usd=10000000,
                          lead="Third Rock Ventures; Frazier Healthcare; " + BVP, firm_in_round=True,
                          source=BG_ALC, source_type="press")],
           note="Second pass: the Boston Globe (2013-07-22) reports a $10M Series B led by Third Rock, Frazier and "
                "Bessemer that 'brings Alcresta's total to $20 million' and places the company in Newton. "
                "Bessemer's own date is 2011-09-09, so its entry was the first $10M, the Series A that came before "
                "that Series B; the round name is from knowledge at medium confidence."),
    jl.cls("stayglad", stage="Series A", stage_src="model", stage_conf="medium", city="Bangalore",
           rounds=[jl.rnd("2015-10", "Series A", firm_in_round=True, source=None, source_type="press")],
           note="Second pass: the firm's own date is 2015-10-14, the round the press of the time reported as StayGlad's "
                "Series A from Bessemer, named from knowledge at medium confidence; Google News searches on "
                "2026-10-06 returned no report of the round. City (Bangalore) from memory."),

    # ---- statuses, cities and countries
    jl.cls("tribe", status="private", city="Toronto",
           note="Second pass: Tribe renamed itself Bettermode, so this row and the base row bettermode are one "
                "company; status and city aligned to that row (private, Toronto, BetaKit)."),
    jl.cls("vimo", status="private", city="Mountain View",
           note="Second pass: Vimo, Inc. trades as GetInsured, so this row and the base row getinsured are one "
                "company; status and city aligned to that row (private, Mountain View). The firm's history page "
                "says its operating partner Chini Krishnan founded Vimo in 2005, which names no round."),
    jl.cls("watershed", status="private", country="US", city="Cambridge", city_src="web_verified",
           flags=("model_disputes_source",), clear=("country_unknown", "city_unknown"),
           note="Second pass: MIT News (2025-10-14) profiles Watershed Bio (Watershed Informatics), founded in 2019 "
                "by Jonathan Wang and based in Kendall Square, Cambridge, Massachusetts, and its site watershed.bio "
                "was live on 2026-10-06, so private, United States, Cambridge. The Wikidata GB match is another "
                "company. No source read names the 2021 round."),
    jl.cls("way-systems", status="acquired", entry_date="2005", country="US", country_src="formd_address",
           city="Woburn", city_src="formd_address", clear=("country_unknown",),
           rounds=[jl.rnd("2002", "Seed", lead="Bill Melton", firm_in_round=False, source=TC_WAY,
                          source_type="press"),
                   jl.rnd("2008-10-02", "Later round (Form D)", amount_usd=3371923, firm_in_round=True, source=None,
                          source_type="filing")],
           note="Second pass: TechCrunch (2010-09-01) reports VeriFone bought the assets of WAY Systems for $6M "
                "plus an earn-out, after a 2002 seed from Bill Melton and $50M of equity from Bessemer and Austin "
                "Ventures between 2004 and 2009, so acquired by VeriFone, 2010. The entry date is the firm's own "
                "year 2005, not the 2008 Form D, which was a later round. EDGAR places the company in Woburn, "
                "Massachusetts. No source read names the 2005 round."),
    jl.cls("gotv", status="acquired", city="Sherman Oaks",
           note="Second pass: Wikipedia's Phunware article lists GoTV among the companies Phunware acquired, so "
                "acquired by Phunware (the year, 2011, is from memory). City (Sherman Oaks, California) from "
                "memory. No source read names the 2004 round."),
    jl.cls("fg-wireless", country="CN", country_src="web_verified", country_cite=HIST_FG,
           clear=("country_unknown",),
           note="Second pass: the firm's own 2008 history page names 'FG Wireless in China' among its wireless "
                "companies, so the country is China; the company is still not identified beyond that."),
    jl.cls("applied-solar-technologies", status="private", city="New Delhi", city_src="web_verified",
           rounds=[jl.rnd("2015-06-08", "Later round", amount_usd=40000000, lead="Future Fund", firm_in_round=True,
                          source=VCC_AST, source_type="press")],
           note="Second pass: VCCircle (2015-06-08) reports 'Delhi-based Applied Solar Technologies' raising $40M "
                "led by Australia's Future Fund with existing investors Bessemer, Capricorn and IFC, and trade "
                "press still profiled its co-founder in May 2024, so private, New Delhi. No source read names the "
                "2009 round."),
    jl.cls("remedinet", city="Bangalore",
           note="Second pass: city (Bangalore) from memory. The Economic Times (2014-07-23) reports a later round "
                "in which Rakesh Jhunjhunwala's RARE Enterprises joined the venture funds; no source read names "
                "Bessemer's March 2013 round."),
    jl.cls("sarvega", city="Oakbrook Terrace",
           note="Second pass: city corrected to Oakbrook Terrace, Illinois, where the Intel acquisition coverage "
                "placed the company (from memory). Wikipedia dates the Intel announcement 2005-08-17 and names no "
                "funding round."),
]

jl.write("s21b", lines)
