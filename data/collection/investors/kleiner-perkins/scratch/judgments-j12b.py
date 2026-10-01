"""Judge j12, batch 24 (PRO-99 Kleiner Perkins)."""
import judge_lib as jl
from judge_lib import verdict, cls, rnd

L = []
NM = "formd_adjudicated"


def nm(slug, basis, conf="high", ec=NM, cite=None):
    L.append(verdict(slug, "not_member", basis, ec=ec, conf=conf, cite=cite))


# ---------------------------------------------------------------- name matches ruled out
KNAUF = ("Noah Knauf became a Kleiner Perkins investing partner in 2016 (the firm's own people page) after Warburg "
         "Pincus, and from 2018-09 is a Bond partner (D2)")
nm("photothera-inc",
   f"Name match only: {KNAUF}; his 2009 PhotoThera seat predates his KP years and no Kleiner Perkins listing, vehicle "
   "filing or press names the firm. D5 seat dating.")
nm("regionalcare-hospital-partners-holdings-inc",
   f"Name match only: {KNAUF}; his 2009-2013 RegionalCare seats predate his KP years (a Warburg Pincus hospital "
   "platform) and nothing names a Kleiner Perkins fund. D5 seat dating.")
nm("sbt-holdings-inc",
   f"Name match only: {KNAUF}; SBT Holdings is the Keystone Dental holding company, whose 2012 Form D seats him with "
   "Warburg Pincus colleagues at 450 Lexington Avenue, before his KP years. D5 seat dating.")
nm("silk-road-medical-inc",
   f"Name match only: {KNAUF}; his 2011-2015 Silk Road Medical seats predate his KP years and no Kleiner Perkins "
   "listing, vehicle filing or press names the firm. D5 seat dating.")
nm("specialists-on-call-inc",
   f"Name match only: {KNAUF}; his 2014-2015 Specialists On Call seats predate his KP years and nothing names a "
   "Kleiner Perkins fund. D5 seat dating.")
nm("sterigenics-nordion-topco-parent-llc",
   f"Name match only: {KNAUF}; the 2015 Sterigenics-Nordion topco (a buyout holding company) predates his KP years, "
   "and a control holding company is not a venture position (D4). D5 seat dating.")
nm("relativity-space-inc",
   f"Bond, not Kleiner Perkins: {KNAUF}; his 2019-2021 Relativity Space seats date after the September 2018 "
   "separation and locate Bond, and no Kleiner Perkins listing or fund filing names the firm (D2).")
nm("sugar-bowl-corp",
   "Not a venture position: Sugar Bowl Corp is the Sugar Bowl ski resort company in Norden, California; Noah Knauf (a Bond partner from 2018-09) is one of thirteen directors. D2, D3.")
for slug, yrs in (("plethora-corp", "2018-2021"), ("quantiply-corp", "2017-2018"), ("rammer-technologies-inc", "2021"),
                  ("rapiddeploy-inc", "2019-2023"), ("splice-machine-inc", "2019")):
    nm(slug, f"Name match only: Ray Lane founded GreatPoint Ventures in March 2015 after becoming a Kleiner Perkins "
             f"partner emeritus in April 2013 (Beyond Meat S-1 biography); his {yrs} seats locate GreatPoint, and no "
             "Kleiner Perkins listing, vehicle filing or press names the firm. D5 seat dating.")
nm("redaptive-inc",
   "Name match only: Michael Linse left Kleiner Perkins to found Linse Capital; his 2018-2021 Redaptive seats locate "
   "Linse Capital, and the S-1 names Kleiner Perkins only in a director's biography (R1), not as a holder.")
nm("scoutrfp-inc",
   "Name match only: Matt Murphy moved to Menlo Ventures in 2018; his 2019 Scout RFP seat locates Menlo (whose book "
   "holds Scout RFP), and nothing names a Kleiner Perkins fund. D5 seat dating.")
nm("star-therapeutics-llc",
   "Name match only: Beth Seidenberg's 2025 Star Therapeutics seat locates Westlake Village BioPartners (from 2018, "
   "D5); no Kleiner Perkins listing, vehicle filing or press names the firm.")
nm("quorum-information-technologies-inc",
   "Homonym: the Mark Allen on this Calgary issuer's $178K Form D is its executive officer; nothing ties it to the "
   "firm's former operating partner or to a Kleiner Perkins fund.")
nm("rto-energy-trading-llc",
   "Homonym: the Mark Allen on this Vienna, Virginia energy trading LLC's Form D filings is its executive officer; "
   "nothing names a Kleiner Perkins fund.")
nm("solicore-inc",
   "Name match only: a Mark Allen (home address in Fremont) sits on Solicore's 2009 Form D beside DFJ and Rho "
   "partners; no Kleiner Perkins listing, vehicle filing or press names the firm in Solicore.")
nm("remmie-inc",
   "Homonym: Jane Zhang is an executive officer of this Bothell, Washington issuer raising $100K, not the KPCB China "
   "associate; nothing names a Kleiner Perkins fund.")
nm("rrtc-inc",
   "Homonym: the director is David H. Wells on RRTC (Richard Riman's New Jersey company); nothing ties him to the firm "
   "or names a Kleiner Perkins fund.")
nm("sionix-corp",
   "Homonym: the David Wells on Sionix's 2011 Form D filings is its executive officer (a listed Los Angeles water "
   "treatment company); nothing names a Kleiner Perkins fund.")
nm("tabacaleraysidron-inc",
   "Homonym: the David Wells on this issuer's 2015 Form D is its executive officer; nothing names a Kleiner Perkins "
   "fund.")
nm("stageconnect-inc",
   "Homonym: the Matthew Murphy on this Nashua, New Hampshire issuer's small Form D filings is its executive officer; "
   "nothing names a Kleiner Perkins fund.")
nm("solera-health-inc",
   "Name match only: Lawrence Leisure (a Jiff co-founder) is a director on Solera Health's 2018 Form D; no Kleiner "
   "Perkins listing, vehicle filing or press names the firm in Solera.")
nm("sociable-labs-inc",
   "Personal angel check: Russell Siegelman (home address on the filing) is listed among Sociable Labs' angels; its "
   "rounds were led by Javelin (Series A) and Battery Ventures (Series B, TechCrunch 2011-10-26), and no source names "
   "a Kleiner Perkins fund (D3).")
nm("s-labs-holdings-llc",
   "Personal angel check: S Labs Holdings shares Sociable Labs' address, CEO and board (Nisan Gabbay, Javelin, Battery); "
   "Russell Siegelman sits from his home address and no source names a Kleiner Perkins fund (D3).")
nm("prealize-health-inc",
   "Personal check: Prealize (formerly Cardinal Analytx) says its $22M Series B was led by John Doerr personally, who "
   "joined the board (MedCity News, 2019-05-27); no source names a Kleiner Perkins fund in any round (D3).",
   conf="medium")
nm("ridwell-inc",
   "Name match only: Ryan Panchadsaram (the firm's advisor to the chairman) is a director on Ridwell's December 2025 "
   "$15M Form D, but no press, company or firm source names Kleiner Perkins in a Ridwell round; only vendor databases "
   "list it, which cannot corroborate (Rule A).", conf="medium")

# ---------------------------------------------------------------- vehicle filings that are T3 public-market positions
nm("platinum-software-corp",
   "Public-market position (T3/D4): KPCB VII's Schedule 13D (first filed 1994-09-22, amended 1999-03-10) covers Series "
   "C preferred bought from Platinum Software after its 1992 listing; no pre-IPO Kleiner Perkins round is on record.",
   conf="medium", ec="fund_filing",
   cite="https://www.sec.gov/Archives/edgar/data/891178/000104746999009198/0001047469-99-009198-index.htm")
nm("seec-inc",
   "Public-market position (T3/D4): in January 2003 KPCB bought about 1.2 million common shares of Nasdaq-listed SEEC "
   "for about $1.3M (SEEC press release, 8-K), alongside SEEC's purchase of assets of Asera, the firm's own portfolio "
   "company and the investment to record.", conf="high", ec="fund_filing", cite=jl.FTS("SEEC", "8-K"))

# ---------------------------------------------------------------- Atara's program companies (members)
ATARA = jl.FTS("Atara", "DRS")
for slug, nm_ in (("pinta-biotherapeutics-inc", "Pinta Biotherapeutics"),
                  ("santa-maria-biotherapeutics-inc", "Santa Maria Biotherapeutics")):
    L.append(verdict(slug, "member",
                     f"Atara Biotherapeutics' 2014 registration statement: {nm_} was one of three program companies "
                     "incorporated August 2012 whose Series A was bought by entities affiliated with Kleiner Perkins "
                     "Caufield & Byers ($5M), named as promoters; its stockholders were recapitalized into Atara on "
                     "2014-03-31. Same investment as atara-biotherapeutics.",
                     ec="fund_filing", conf="high", cite=ATARA))
    L.append(cls(slug, status="acquired", rng="below_1b",
                 stage="Series A", stage_src="web_verified", stage_cite=ATARA, stage_conf="high", entry_date="2012-10",
                 city="Brisbane", city_src="formd_address", focus="Healthcare & Bio",
                 rounds=[rnd("2012-10", "Series A (Oct 2012 to Mar 2013, $20.1M across Nina, Pinta and Santa Maria)",
                             20087750, None, True, ATARA, "filing")],
                 note=f"One of Atara's three program companies (Nina, Pinta, Santa Maria); KPCB entities bought $5M of "
                      "the Series A sold October 2012 to March 2013, so the entry date is 2012-10, not the 2013-11 "
                      "Form D close. Stockholders were recapitalized into Atara on 2014-03-31 (acquired, merged into "
                      "Atara). Should merge into atara-biotherapeutics."))

# ---------------------------------------------------------------- duplicates of listed companies (members)
RIP = jl.POST("kleiner-perkins-welcomes-rippling")
L.append(verdict("people-center-inc", "member",
                 "People Center, Inc. is Rippling (San Francisco; its 2019 and 2020 Form D filings), which the firm "
                 "lists and whose Series A it led ('Welcome Rippling', 2019-04-03); Mamoon Hamid is the director on "
                 "the filings. Duplicate of base row rippling.", ec="site_listing", conf="high",
                 cite=jl.SITE("rippling")))
RIP_VAL = "https://www.cnbc.com/2025/05/09/rippling-valued-at-16point8-billion-in-450-million-funding-round.html"
L.append(cls("people-center-inc", status="private", rng="10b_plus", usd=16800000000, val_src="web_verified",
             val_cite=RIP_VAL, asof="2025-05-09", extra={"valuation_range_source": "web_verified"},
             stage="Series A", stage_src="first_party", stage_cite=RIP, stage_conf="high", entry_date="2019-03-19",
             city="San Francisco", city_src="model_knowledge", focus="SaaS", flags=["stage_disputes_band"],
             rounds=[rnd("2019-03-19", "Series A ($45M; Kleiner Perkins wrote $25M)", 44999958, "Kleiner Perkins",
                         True, RIP, "firm"),
                     rnd("2025-05-09", "Series G ($450M at $16.8B)", 450000000, None, None, RIP_VAL, "press")],
             note="Rippling: the firm's posts say it led the Series A (its $25M check), dated by the round's Form D "
                  "(first sale 2019-03-19), not the Growth the band read off the $45M size. Mark: $16.8B Series G "
                  "(CNBC, 2025-05-09), aligned with coatue, lightspeed and sequoia. Duplicate of rippling."))

L.append(verdict("stryder-corp", "member",
                 "Stryder Corp. is Handshake (CEO Garrett Lord, co-founder Ben Christensen), which the firm lists "
                 "(invested 2016) and whose $10.5M Series A it led (firm case study); Eric Feng then Mamoon Hamid sit "
                 "as directors on its Form D filings. Duplicate of base row handshake.", ec="site_listing",
                 conf="high", cite=jl.SITE("handshake")))
HS_VAL = "https://www.prnewswire.com/news-releases/no-network-required-handshake-raises-200m-to-help-gen-z-launch-careers-301463445.html"
L.append(cls("stryder-corp", status="private", rng="1b_plus", usd=3500000000, val_src="web_verified",
             val_cite=HS_VAL, asof="2022-01", extra={"valuation_range_source": "web_verified"},
             city="San Francisco", city_src="model_knowledge", focus="Consumer & Marketplaces", flags=["stale"],
             note="Handshake: $200M Series F at $3.5B (January 2022), no later priced round found, so stale; aligned "
                  "with coatue, lightspeed, spark-capital and eqt-ventures. The firm led the $10.5M Series A (2016), "
                  "matching the band. Duplicate of handshake."))

TURO = jl.FTS("Turo", "DRS")
TURO_VAL = "https://finance.yahoo.com/news/turo-becomes-techs-newest-unicorn-with-250m-iac-investment-194729985.html"
L.append(verdict("relayrides-inc", "member",
                 "RelayRides, Inc. is Turo (CIK 1514587, the issuer of Turo's later Form D filings and S-1), which the "
                 "firm lists (invested 2015); Brook Porter, then a Kleiner Perkins partner, was elected to the board by "
                 "the Series C holders in August 2015 (Turo registration statement). Duplicate of base row turo.",
                 ec="site_listing", conf="high", cite=jl.SITE("turo")))
L.append(cls("relayrides-inc", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified",
             val_cite=TURO_VAL, asof="2019-07", extra={"valuation_range_source": "web_verified"},
             stage="Growth", stage_src="web_verified", stage_cite=TURO, stage_conf="medium", entry_date="2015-08-18",
             city="San Francisco", city_src="model_knowledge", focus="Consumer & Marketplaces", flags=["stale"],
             rounds=[rnd("2015-08-18", "Series C ($44.7M)", 46600000, None, True, TURO, "filing"),
                     rnd("2019-07", "Series E ($250M, IAC)", 250000000, "IAC", None, TURO_VAL, "press")],
             note="Turo (RelayRides until 2015): Brook Porter, a Kleiner Perkins partner, joined the board in August "
                  "2015 as the Series C holders' director, matching the firm's 2015 since-year and the round's Form D "
                  "(first sale 2015-08-18), so the entry reads Growth. Mark: IAC's Series E at over $1B (2019-07), "
                  "stale; IPO withdrawn, still private. Aligned with gv. Duplicate of turo, whose 'defunct' status "
                  "is a bad Wikidata join."))

BYND = jl.POST("beyond-meat-the-future-of-protein")
L.append(verdict("savage-river-inc", "member",
                 "Savage River, Inc. is Beyond Meat (CIK 1655210, the S-1 registrant), which the firm lists (invested "
                 "2011) and whose S-1 names entities affiliated with Kleiner Perkins Caufield & Byers as a 16.1% holder. "
                 "Duplicate of base row beyond-meat.", ec="site_listing", conf="high", cite=jl.SITE("beyond-meat")))
L.append(cls("savage-river-inc", stage="Series A", stage_src="first_party", stage_cite=BYND, stage_conf="medium",
             entry_date="2011", city="El Segundo", city_src="formd_address", focus="Consumer & Marketplaces",
             rounds=[rnd("2011", "first financing round (Series A preferred, the first series)", None,
                         "Kleiner Perkins", True, BYND, "firm")],
             note="Beyond Meat: the firm's 2019 post says Kleiner Perkins was the only institutional investor in the "
                  "company's first financing round in 2011; the S-1's first preferred series is Series A, so the "
                  "entry reads Series A (medium). Ray Lane's 2015-2017 Form D seats are follow-ons. Duplicate of "
                  "beyond-meat."))

SRIYA_FD = "https://www.sec.gov/Archives/edgar/data/1421009/000142100912000002/0001421009-12-000002-index.htm"
L.append(verdict("sriya-innovations-inc", "member",
                 "Sriya Innovations is Renmatix (King of Prussia; CEO Mike Hamilton; CIK 1421009, the issuer of "
                 "Renmatix's later Form D filings), which the firm listed 2012-2025 with John Doerr as partner; John "
                 "Doerr and Ajit Nazre sit as directors on its 2011 Form D. Duplicate of base row renmatix.",
                 ec="site_listing", conf="high", cite=jl.ARCH("renmatix")))
L.append(cls("sriya-innovations-inc", status="private", rng="below_1b", stage="undetermined",
             city="King of Prussia", city_src="formd_address", focus="Climate & Energy",
             rounds=[rnd("2011-12-19", "unnamed ($50.1M sold, Form D)", 50124997, None, None, SRIYA_FD, "filing")],
             note="Renmatix (supercritical-water biomass sugars), incorporated 2007 as Sriya Innovations. The firm's "
                  "partners are directors by December 2011, but no source names the round Kleiner Perkins entered, so "
                  "the stage is undetermined. Last Form D 2020 ($48.6M); no sale or shutdown found. Duplicate of "
                  "renmatix."))

SINO_FD = "https://www.sec.gov/Archives/edgar/data/1480071/000148007112000001/0001480071-12-000001-index.htm"
L.append(verdict("sinoelectric-powertrain-corp", "member",
                 "SinoElectric Powertrain Corp is SinoEV, the EV powertrain supplier the firm's own archive listed "
                 "2012-2024 under Teams China and Greentech; Tina Ju (KPCB China) and a Leung sit as directors on its "
                 "2012 Form D. X1 provisional IN (kpcb_china). Duplicate of base row sinoev.",
                 ec="site_listing", conf="medium", cite=jl.ARCH("sinoev")))
L.append(cls("sinoelectric-powertrain-corp", status="unknown", rng="below_1b", stage="undetermined",
             country="US", country_src="formd_address", city="Sunnyvale", city_src="formd_address",
             focus="Climate & Energy", flags=["kpcb_china"],
             rounds=[rnd("2012-08-14", "unnamed ($6.0M sold, Form D; Cayman issuer)", 6000002, None, None, SINO_FD,
                         "filing")],
             note="SinoEV / SinoElectric Powertrain (EV powertrain supplier; Cayman company with a Sunnyvale office on "
                  "its Form D, operations likely in China). A KPCB China holding (X1, provisional). No source names "
                  "the entry round or the company's fate, so stage undetermined and status unknown. Duplicate of "
                  "sinoev."))

# ---------------------------------------------------------------- vehicle-filing members: classification only
PREV = "https://www.sec.gov/Archives/edgar/data/1047121/0001012870-97-002326.txt"
L.append(cls("preview-travel-inc", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=PREV, stage_conf="high", entry_date="1995-01",
             country="US", city="San Francisco", focus="Consumer & Marketplaces",
             rounds=[rnd("1995-01", "Series D Preferred ($4.20/share)", None, None, True, PREV, "filing"),
                     rnd("1996-06", "Series E Preferred", None, None, True, PREV, "filing")],
             note="Preview Travel's November 1997 IPO prospectus: in January 1995 AOL and the KPCB funds (KPCB VII and "
                  "affiliates) bought Series D Preferred, and Hearst and Mackenzie joined the board in February 1995, "
                  "so the entry reads Growth. Merged with Travelocity in 2000 (acquired)."))
RAST = "https://www.sec.gov/Archives/edgar/data/753081/0000891618-96-001609.txt"
L.append(cls("raster-graphics-inc", status="acquired", rng="below_1b", stage="undetermined",
             country="US", city="San Jose", focus="Industrial & Robotics",
             rounds=[rnd("1995-02", "Series C Preferred ($2.50/share as converted; a follow-on)", None, None, True,
                         RAST, "filing")],
             note="Raster Graphics' 1996 IPO prospectus: KPCB IV holds 10.3% and Tom Caufield has been a director since "
                  "November 1988; KPCB IV bought into the February 1995 Series C, a follow-on. The round it first "
                  "entered is not named, so the stage is undetermined. Acquired by Gretag Imaging in 1999."))
L.append(cls("prism-solutions-inc", status="acquired", rng="below_1b", stage="undetermined",
             country="US", city="Sunnyvale", focus="Data Infrastructure", rounds=[],
             note="Prism Solutions (data warehouse software), IPO March 1996. The firm's 13G filings of 1997-1999 show "
                  "the holding; no EDGAR filing names the round it entered, so the stage is undetermined. Acquired by "
                  "Ardent Software in 1999."))
RES = "https://www.sec.gov/Archives/edgar/data/1026380/0001012870-00-004134.txt"
L.append(cls("resonate-inc", status="acquired", rng="below_1b", stage="undetermined",
             country="US", city="Sunnyvale", focus="Data Infrastructure",
             rounds=[rnd("1998-06", "Series C preferred ($3.034/share)", None, None, True, RES, "filing"),
                     rnd("1999-06", "Series D preferred ($4.81/share)", None, None, True, RES, "filing"),
                     rnd("2000-03", "Series E preferred (Sun Microsystems)", None, None, False, RES, "filing")],
             note="Resonate's August 2000 IPO prospectus: KPCB Java Fund and KPCB VIII bought Series C (1998) and "
                  "Series D (1999), but Russell Siegelman has been a director since April 1997, so the entry predates "
                  "the Series C and its round is not named; stage undetermined. Taken private by GTG Acquisition Corp "
                  "in 2003 (merger proxy). The y-combinator 'Resonate' is a different company."))
RHY = "https://www.sec.gov/Archives/edgar/data/1065869/0001047469-99-013684.txt"
L.append(cls("rhythms-net-connections-inc", status="acquired", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=RHY, stage_conf="high", entry_date="1997-07",
             country="US", city="Englewood", focus="Data Infrastructure",
             rounds=[rnd("1997-07-03", "Series A Preferred ($12.3M in three closings)", 12300000, None, True, RHY,
                         "filing")],
             note="Rhythms NetConnections' April 1999 S-1/A: the Series A purchase agreement of July 3, 1997 names "
                  "Kleiner Perkins Caufield & Byers among the Series A purchasers, and Kevin Compton joined the board "
                  "that month as KPCB's nominee. Filed Chapter 11 on 2001-08-02 and its network assets were sold to "
                  "WorldCom (acquired, out of insolvency)."))
SG = "https://www.sec.gov/Archives/edgar/data/1013170/0000950131-96-003553.txt"
L.append(cls("silicon-gaming-inc", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=SG, stage_conf="high", entry_date="1995-08",
             country="US", city="Palo Alto", focus="Media, Gaming & Advertising",
             rounds=[rnd("1995-08", "Series B Preferred ($2.5M by KPCB VII and related entities)", 2499999, None, True,
                         SG, "filing"),
                     rnd("1996-03", "Series C Preferred", 666670, None, True, SG, "filing")],
             note="Silicon Gaming's July 1996 IPO prospectus: KPCB VII and related entities bought Series B Preferred "
                  "in August 1995 (Series A went to Technology Partners by debt conversion), so the entry reads "
                  "Growth. Merged into International Game Technology after its 2001 restructuring (acquired); "
                  "aligned with benchmark."))

jl.write("j12b", L)
