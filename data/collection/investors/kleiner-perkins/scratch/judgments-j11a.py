"""PRO-99 Kleiner Perkins, judge j11, batch 21."""
import judge_lib as jl
from judge_lib import verdict, cls, rnd

FA = "formd_adjudicated"
L = []


def nm(slug, basis, conf="high"):
    L.append(verdict(slug, "not_member", basis, ec=FA, conf=conf))


# ---- S-1 prospectuses read for this batch (EDGAR, the companies' own registration statements)
S1_ACTIVE = "https://www.sec.gov/Archives/edgar/data/1088147/0001032210-99-000922.txt"
S1_BRIO = "https://www.sec.gov/Archives/edgar/data/1056294/0001012870-98-000596.txt"
S1_CONCENTRIC = "https://www.sec.gov/Archives/edgar/data/1007304/0000950109-97-004177.txt"
S1_CORSAIR = "https://www.sec.gov/Archives/edgar/data/1028285/0000898430-97-002431.txt"
S1_CORVIS = "https://www.sec.gov/Archives/edgar/data/1060490/000092838500001395/0000928385-00-001395.txt"
FIERCE_ARSENAL = "https://www.fiercebiotech.com/biotech/arsenalbio-joins-next-gen-cell-therapy-field-85m-a-round"
PR_CAMEO = "https://www.prnewswire.com/news-releases/cameo-closes-50-million-series-b-round-led-by-kleiner-perkins-300874358.html"
BEAM_PR = "https://www.biospace.com/beam-dental-raises-22-5-million-series-c-led-by-kleiner-perkins-to-reimagine-dental-insurance-for-small-and-medium-sized-businesses"
HARVEY_155 = "https://www.harvey.ai/blog/harvey-raises-dollar550m-at-a-dollar155b-valuation-to-help-legal-teams-own-their-intelligence"
BLUEOAK_AUCTION = "https://resource-recycling.com/e-scrap/2019/03/07/blueoak-equipment-on-the-auction-block/"
DUP = ["identity_conflated", "duplicate"]

# ================= not_member: Form D name matches without corroboration, dated seats, homonyms
nm("act-on-software-inc", "Form D name match only: Mamoon Hamid sat on the board in 2010-2011, years before he joined Kleiner "
   "Perkins in 2017 (he was then at US Venture Partners); no firm listing, KP vehicle or press names the firm in a round "
   "(D5 seat dating).")
nm("activ-surgical-inc", "Form D name match on a homonym: the David Wells on the 2018-2019 filings is an executive officer and "
   "director of the company, and the roster's David Wells appears at the firm only in 2012-2013; nothing names Kleiner "
   "Perkins in a round, and missing corroboration is not_member.")
nm("actym-therapeutics-inc", "Form D name match only: James Huang's 2020 seat falls after he left KPCB China to run his own "
   "firm (Panacea Venture); no firm listing, KP or KPCB China vehicle or press names the firm in a round (D5, X1).",
   conf="medium")
nm("adflow-health-networks-inc", "Form D name match on a homonym: the Michael Abbott on the 2011 filing is the company's "
   "executive officer; the firm's Mike Abbott joined Kleiner Perkins from Twitter in 2012; nothing names the firm in a round.")
nm("alethea-group-inc", "Form D name match only: Ted Schlein's 2022 seat is his Ballistic Ventures seat (D5: Ballistic from "
   "2022); no firm listing, KP vehicle or press names Kleiner Perkins in a round.")
nm("alexanders-steakhouse-inc", "Form D name match only: a restaurant company whose 2018 filing lists a Wen Hsieh as director; "
   "nothing shows it is the firm's partner acting for a fund, and no listing, KP vehicle or press names Kleiner Perkins in a "
   "round (missing corroboration).")
nm("alpha-design-ai-inc", "Form D name match only: Wen Hsieh sits on the board in 2026 at the company's Goleta address, when "
   "the firm's site lists him as an Advisor (and he co-founded Matter Venture Partners in 2022); an advisor's seat counts "
   "only where a firm fund held the position (D5), and no listing, KP vehicle or press names Kleiner Perkins in a round.",
   conf="medium")
nm("aperia-technologies-inc", "Form D name match only: Kathleen Ligocki was a Kleiner Perkins operating partner around 2013; "
   "her 2023 seat is ten years later and nothing names the firm in a round (D5 seat dating).")
nm("arcadia-power-inc", "Form D name match only: Ben Kortlang's 2021-2024 seat is his G2 Venture Partners seat (the green "
   "growth team left Kleiner Perkins to form G2VP in 2017); nothing names Kleiner Perkins in a round (D5).")
nm("asaas-ltd", "D2 Bond: Daegwon Chae on the 2024 Form D is a Bond partner, and after September 2018 a Bond partner locates "
   "Bond, not Kleiner Perkins; nothing names a Kleiner Perkins or Digital Growth fund (decisions.md D2).")
nm("asapp-inc", "Form D name match only: John Doerr sits on the board from 2021, but no firm listing, KP vehicle filing or press "
   "source found names a Kleiner Perkins fund in an ASAPP round; the seat alone is person-level (D3, D5).", conf="medium")
nm("attensity-media-llc", "Form D name match only: Larry Leisure is listed as an executive officer and director of this Santa "
   "Monica LLC at the company's own address (2013), a personal operating role; no firm listing, KP vehicle or press names "
   "Kleiner Perkins in a round (missing corroboration).", conf="medium")
nm("auron-therapeutics-inc", "Form D name match only: Isaac Ciechanover's 2020 seat falls eight years after his Kleiner Perkins "
   "years (2010-2012); nothing names the firm in a round (D5 seat dating).")
nm("bcmh-inc", "Form D name match on a homonym: BCMH, Inc. is Bain Capital's holding company for Apex Tool Group (the 2013 Form D "
   "is filed c/o Bain Capital, Boston) and its David Wells is an officer of that group, not the firm's partner.")
nm("bfe-inc", "Form D name match only: Tina Ju sat on the board of this Guangzhou business-services company in 2011, inside her "
   "KPCB China years, but it is not on the firm's own China listing and no KP or KPCB China vehicle filing or press source "
   "names the firm in a round; missing corroboration is not_member (X1).", conf="medium")
nm("biointellisense-inc", "Form D name match only: Lawrence Leisure's 2020-2022 seat falls after his Kleiner Perkins operating "
   "partner years (by 2015 he was a manager of Chicago Pacific Founders' general partner); nothing names the firm in a round "
   "(D5 seat dating).")
nm("brestem-therapeutics-inc", "Form D name match only: the related person is Weili Zhou, not the roster's Wei Zhou, and no "
   "listing, KP or KPCB China vehicle or press names the firm in a round (missing corroboration).")
nm("bricksolve-inc", "Form D name match only: Aileen Lee's 2014-2016 seat is her Cowboy Ventures seat (D5: Cowboy from 2012); "
   "nothing names Kleiner Perkins in a round.")
nm("cardiomems-inc", "Form D name match on a homonym: the Mark Allen on the 2009-2010 filings is an executive officer of the "
   "company (its co-founder), not the firm's operating partner; nothing names Kleiner Perkins in a round.", conf="medium")
nm("catalyze-holdings-llc", "Form D name match only: Joel Serface is the company's executive officer in 2019, a decade after his "
   "Kleiner Perkins years (2008-2009); nothing names the firm in a round (D5 seat dating).")
nm("centrillion-biosciences-corp", "Form D name match on a homonym: Wei Zhou is Centrillion's own founder and executive officer "
   "(the Palo Alto biochip company), not the KPCB China partner; nothing names Kleiner Perkins or KPCB China in a round. "
   "Same registrant (CIK 1473835) as centrillion-technology-holdings-corp.")
nm("centrillion-technology-holdings-corp", "Form D name match on a homonym: Wei Zhou is Centrillion's own founder and executive "
   "officer, not the KPCB China partner; nothing names Kleiner Perkins or KPCB China in a round. Same registrant (CIK "
   "1473835) as centrillion-biosciences-corp.")
nm("china-new-energy-group-co", "Form D name match only: a 2009-2010 placement by a company already quoted over the counter, a "
   "public-market purchase with no earlier private round (T3, D4); no Kleiner Perkins or KPCB China fund is named and the "
   "related person James Tie Li is not shown to be the firm's James Li.", conf="medium")
nm("clarifai-inc", "Form D name match only: Matt Murphy's 2016 seat is his Menlo Ventures seat (Menlo led Clarifai's 2016 "
   "Series B, the Menlo sibling row); nothing names Kleiner Perkins in a round (D5 seat dating).")
nm("cloudon-inc", "Form D name match only: Mamoon Hamid's 2012 seat predates his Kleiner Perkins years (from 2017) by five years; "
   "nothing names the firm in a round (D5 seat dating).")
nm("columbia-care-inc", "Form D name match on a homonym: the Michael Abbott on the 2014-2022 filings is an executive officer of "
   "the cannabis operator, not the firm's Mike Abbott; nothing names Kleiner Perkins in a round.")
nm("constitution-medical-investors-inc", "Form D name match only: Noah Knauf's 2010-2012 seat predates his Kleiner Perkins "
   "years (he came from Warburg Pincus, per his biography in the Hippo S-1); nothing names the firm in a round (D5).",
   conf="medium")
nm("content-checked-holdings-inc", "Form D name match on a homonym: the David Wells on the 2015 filings is the company's "
   "executive officer; nothing names Kleiner Perkins in a round.")
nm("cpf-senior-alpha-llc", "Another manager's fund, not an operating company: a Chicago Pacific Founders vehicle (the Form D is "
   "filed c/o Chicago Pacific Founders GP) on which Lawrence Leisure is a manager of the general partner (D6).")

# ================= members held by KP vehicles' own filings (classification only)
L.append(cls("active-software-inc", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified",
             stage_cite=S1_ACTIVE, stage_conf="high", entry_date="1996-02-01", country="US", city="Santa Clara",
             focus="Data Infrastructure",
             rounds=[rnd("1995-10", "Seed (convertible note)", 250000, "Enterprise Partners", False, S1_ACTIVE, "filing"),
                     rnd("1996-02-01", "Series A", 4035075, None, True, S1_ACTIVE, "filing")],
             note="Enterprise application integration software; IPO August 1999, acquired by webMethods in 2000. The 1999 "
                  "S-1 shows Kleiner Perkins Caufield & Byers VII, the KPCB Java Fund and the Zaibatsu Fund II buying "
                  "2,250,000 of the 6,022,500 Series A shares sold in February 1996 (agreement dated 1996-02-01; Kevin "
                  "Compton a director from January 1996), after Enterprise Partners' October 1995 seed note."))
L.append(cls("brio-technology-inc", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified",
             stage_cite=S1_BRIO, stage_conf="high", entry_date="1995-03-21", country="US", city="Santa Clara",
             focus="Data Infrastructure",
             rounds=[rnd("1995-03-21", "Series A", 3849998, None, True, S1_BRIO, "filing")],
             note="Business-intelligence software. The 1998 S-1 shows Kleiner Perkins Caufield & Byers VII (with the "
                  "Zaibatsu Fund II) buying 2,269,780 of the 2,496,756 Series A shares sold under the agreement of "
                  "1995-03-21 (Floyd Kvamme and Bernard Lacroute directors from March 1995), then Series B and C. IPO "
                  "1998; acquired by Hyperion in 2003 (Wikipedia)."))
L.append(cls("cardiogenesis-corp", status="acquired", rng="below_1b", stage="undetermined", rounds=[], country="US",
             city="Sunnyvale", focus="Healthcare & Bio",
             note="Laser revascularization devices (Sunnyvale); Kleiner Perkins funds filed 13Gs 1997-1999 after the 1996 "
                  "IPO. Merged into Eclipse Surgical Technologies in 1999, which took the Cardiogenesis name. EDGAR holds "
                  "no IPO prospectus for it, so no source names the firm's round."))
L.append(cls("cellpro-incorporated", status="defunct", rng="below_1b", stage="undetermined", rounds=[], country="US",
             city="Bothell", focus="Healthcare & Bio",
             note="Stem-cell selection devices (Bothell, WA), listed 1991; after losing the Baxter and Johns Hopkins patent "
                  "case it filed for Chapter 11 in 1998 with no going-concern sale found, so defunct (bankruptcy rule). "
                  "Its IPO predates EDGAR, so no source names the firm's round."))
L.append(cls("concentric-network-corp", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified",
             stage_cite=S1_CONCENTRIC, stage_conf="high", entry_date="1995-04-20", country="US", city="San Jose",
             focus="Data Infrastructure",
             rounds=[rnd("1995-04-20", "Series A", 10000000, None, True, S1_CONCENTRIC, "filing")],
             note="Internet access and network services. The 1997 S-1 records the Series A agreement of 1995-04-20 selling "
                  "Series A preferred and warrants for about $10.0M to GS Capital Partners, Kleiner Perkins Caufield & "
                  "Byers VII and the KPCB VII Founders Fund (Vinod Khosla a director from April 1995). IPO 1997; merged "
                  "into NEXTLINK in 2000 (later XO Communications)."))
L.append(cls("connective-therapeutics-inc", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
             country="US", city="Palo Alto", focus="Healthcare & Bio", flags=DUP,
             note="Connective Therapeutics renamed itself Connetics in 1996 and was acquired by Stiefel Laboratories in "
                  "2006: the same company as the connetics row (the firm's 2012 page), so the two rows should merge with "
                  "connetics canonical. Kleiner Perkins partner Alexander Barkas was its CEO in 1994 (Connetics proxy); "
                  "EDGAR holds no IPO prospectus naming the firm's round."))
L.append(cls("corsair-communications-inc", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified",
             stage_cite=S1_CORSAIR, stage_conf="high", entry_date="1994-12-08", country="US", city="Palo Alto",
             focus="SaaS",
             rounds=[rnd("1994-12-08", "Series A", 16240000, None, True, S1_CORSAIR, "filing")],
             note="Wireless carrier fraud-prevention and prepaid billing systems (Palo Alto). The 1997 S-1 shows Kleiner "
                  "Perkins Caufield & Byers VII and the Zaibatsu Fund II buying 1,333,334 of the 5,413,340 Series A shares "
                  "sold in December 1994 (closing set for 1994-12-08; Kevin Compton chairman from December 1994). IPO "
                  "1997; acquired by Lightbridge in 2001. Aligned with the TCV row."))
L.append(cls("corvis-corp", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified",
             stage_cite=S1_CORVIS, stage_conf="high", entry_date="1998-05-15", country="US", city="Columbia",
             focus="Data Infrastructure",
             rounds=[rnd("1997-07-17", "Series A", 2820000, None, False, S1_CORVIS, "filing"),
                     rnd("1998-05-06", "Series A", 100000, None, False, S1_CORVIS, "filing"),
                     rnd("1998-05-15", "Series B", 13532253, None, True, S1_CORVIS, "filing")],
             note="Optical networking (Columbia, MD). The 2000 S-1: Series A went to the founder David Huber for "
                  "intellectual property (1997) and a small 1998 purchase by Frank Bonsal; Vinod Khosla and affiliated "
                  "entities (Kleiner Perkins Caufield & Byers VIII and its founders fund, per the holder table) bought "
                  "2,325,582 Series B shares on 1998-05-15, the firm's entry, so it reads Growth by the round word. IPO "
                  "2000, renamed Broadwing, acquired by Level 3 in 2007."))

# ================= duplicates of listed rows (same company, another legal name): members, flagged for the merge
L.append(verdict("arsenal-biosciences-inc", "member",
                 "Same company as the arsenalbio row on the firm's own live list (since 2019): Arsenal Biosciences, Inc. is "
                 "ArsenalBio's legal name, Brook Byers sits on its board, and Fierce Biotech names Kleiner Perkins in the "
                 "$85M Series A (2019-10-17). Merge into arsenalbio.", ec="site_listing", cite=jl.SITE("arsenalbio")))
L.append(cls("arsenal-biosciences-inc", status="private", rng="below_1b", stage="Series A", stage_src="web_verified",
             stage_cite=FIERCE_ARSENAL, stage_conf="medium", entry_date="2019-10-17", city="South San Francisco",
             focus="Healthcare & Bio", flags=DUP + ["stage_disputes_band"],
             rounds=[rnd("2019-10-17", "Series A", 85000000, None, True, FIERCE_ARSENAL, "press")],
             note="Programmable cell therapy (South San Francisco). Kleiner Perkins participated in the $85M Series A "
                  "(Fierce Biotech, 2019-10-17), the year the firm's list dates its entry; the pre-filled Growth band "
                  "reads the 2022 Series B filing ($220M, Sixth Street release 2022-09-06), a later round. $325M Series C "
                  "2024-09-04 at an undisclosed valuation: below_1b. Duplicate of arsenalbio."))

L.append(verdict("baron-app-inc", "member",
                 "Baron App, Inc. is Cameo (its Form D lists Steven Galanis and Martin Blencowe at Cameo's Chicago address, "
                 "with Ilya Fushman at 2750 Sand Hill Road); the firm's archived logo grid lists Cameo 2020-2026 and it "
                 "led the $50M Series B (PR Newswire, June 2019). Merge into cameo.", ec="site_listing",
                 cite=jl.ARCH("cameo")))
L.append(cls("baron-app-inc", status="private", rng="below_1b", city="Chicago", focus="Consumer & Marketplaces", flags=DUP,
             note="Cameo, personalised celebrity videos (Chicago). The March 2021 round valued it at $1B, then the mark "
                  "collapsed: Wikipedia records its own investors estimating $50M by 2023, and The Information reported a "
                  "2024 cramdown round at least 90% below the peak (2024-03-22), so below_1b, aligned with the Bain Capital "
                  "Ventures, GV, Headline, Lightspeed and Spark rows. The cameo row's pre-filled IT is a Wikidata homonym. "
                  "Duplicate of cameo."))

L.append(verdict("beam-technologies-inc", "member",
                 "Beam Technologies Inc. is Beam Dental (its Form D lists Alex Frommeyer at Beam's Columbus address with "
                 "Lucas Swisher on the board), on the firm's own live list since 2018; Kleiner Perkins led its $22.5M "
                 "Series C (the company's release, 2018-05-16). Merge into beam-dental.", ec="site_listing",
                 cite=jl.SITE("beam-dental")))
L.append(cls("beam-technologies-inc", status="private", rng="below_1b", stage="Growth", stage_src="web_verified",
             stage_cite=BEAM_PR, stage_conf="high", entry_date="2018-05-16", city="Columbus", focus="Fintech & Payments",
             flags=DUP + ["model_disputes_source"],
             rounds=[rnd("2018-05-16", "Series C", 22500000, "Kleiner Perkins", True, BEAM_PR, "company")],
             note="Dental and employee-benefits insurance (Columbus, OH). Kleiner Perkins led the $22.5M Series C "
                  "(release 2018-05-16), its entry per the firm's own 2018 year. The pre-filled acquired status belongs "
                  "to a homonym: the company kept filing Form Ds through 2025 ($24M in 2025), so private; no priced $1B "
                  "round found. The accel, spark-capital and y-combinator 'Beam' rows are other companies. Duplicate of "
                  "beam-dental."))

L.append(verdict("biomine-inc", "member",
                 "BioMine, Inc. (CIK 1530978) is BlueOak, the same registrant as the firm's archived blueoak row (kpcb.com "
                 "company page 2013-2018, partners Amol Deshpande and Brook Porter); its 2011 Form D lists Amol Deshpande "
                 "c/o KPCB Holdings, Inc., 2750 Sand Hill Road. Merge into blueoak.", ec="site_listing",
                 cite=jl.ARCH("blueoak")))
L.append(cls("biomine-inc", status="defunct", rng="below_1b", stage="undetermined", rounds=[], city="Palo Alto",
             city_src="formd_address", focus="Climate & Energy", flags=DUP,
             note="E-waste urban mining (BlueOak Resources, formerly BioMine; Palo Alto on its Form D). Its Osceola, "
                  "Arkansas refinery closed in 2018 and the equipment was auctioned in March 2019, not under a court order "
                  "(Resource Recycling, 2019-03-07, " + BLUEOAK_AUCTION + "), so defunct. The entry is judged on the "
                  "blueoak row. Duplicate of blueoak."))

L.append(verdict("borderx-lab-inc", "member",
                 "BorderX Lab Inc. is the borderx-labs row on the firm's archived logo grid (2018-2026), and the firm's "
                 "own post announces the $20M Series B it led (2018-05-08). Merge into borderx-labs.", ec="site_listing",
                 cite=jl.POST("borderx-lab-raises")))
L.append(cls("borderx-lab-inc", status="private", rng="below_1b", stage="Growth", stage_src="first_party",
             stage_cite=jl.POST("borderx-lab-raises"), stage_conf="medium", entry_date="2018-05-08", city="Sunnyvale",
             focus="Consumer & Marketplaces", flags=DUP,
             rounds=[rnd("2018-05-08", "Series B", 20000000, "Kleiner Perkins", True, jl.POST("borderx-lab-raises"), "firm")],
             note="Cross-border e-commerce (Sunnyvale, per the release). The firm's post announces the $20M Series B it "
                  "led; no earlier Kleiner Perkins round is on record (the company's only Form D is this round), so "
                  "Growth at medium. No priced $1B round found. Duplicate of borderx-labs."))

L.append(verdict("breathe-acquisition-corp", "not_member",
                 "Same investment as the breathe-technologies row, filed under another legal entity: Breathe Acquisition "
                 "Corp. is Breathe Technologies' 2017 recapitalisation vehicle (same Irvine address and CEO Lawrence "
                 "Mastrovich; breathe-technologies already carries this CIK's 2017 filings). Kept as its own row it would "
                 "double-count one investment (identity_conflated); membership rests on breathe-technologies.",
                 ec=FA, conf="high"))

L.append(verdict("counsel-ai-corp", "member",
                 "Counsel AI Corp is Harvey (the Form D lists Winston Weinberg and Gabriel Pereyra with Ilya Fushman on the "
                 "board, CIK 1974654 as on the harvey row), on the firm's own live list since 2023; the firm co-led the "
                 "Series B (its post of 2023-12-19). Merge into harvey.", ec="site_listing", cite=jl.SITE("harvey")))
L.append(cls("counsel-ai-corp", status="private", rng="10b_plus", usd=15500000000, val_src="web_verified",
             val_cite=HARVEY_155, asof="2026-09-09", stage="Growth", stage_src="first_party",
             stage_cite=jl.POST("harvey-ai"), stage_conf="medium", entry_date="2023-12", city="San Francisco",
             focus="AI & Applied AI", flags=DUP, extra={"valuation_range_source": "web_verified"},
             rounds=[rnd("2023-04", "round (unnamed)", 23000000, "Sequoia", False, jl.W("Harvey (software)"), "press"),
                     rnd("2023-12", "Series B", 80000000, "Elad Gil; Kleiner Perkins", True, jl.POST("harvey-ai"), "firm"),
                     rnd("2024-07", "Series C", 100000000, "GV", True, jl.W("Harvey (software)"), "press"),
                     rnd("2025-06", "Series E", 300000000, "Kleiner Perkins; Coatue", True, jl.W("Harvey (software)"), "press"),
                     rnd("2026-09-09", "unnamed", 550000000, "Diffusion; Lightspeed", None, HARVEY_155, "company")],
             note="Legal AI (San Francisco). The firm's post of 2023-12-19 says it co-led the Series B ($80M at $715M, "
                  "Wikipedia); Sequoia led the $23M April 2023 round without the firm (Wikipedia), so the entry is the B (Growth) and the "
                  "pre-filled Series A band on the harvey row reads the company's own first filing. Momentum check "
                  "2026-09-30: Harvey's post of 2026-09-09 announces $550M at a $15.5B valuation, aligned with the GV row. "
                  "Duplicate of harvey."))

jl.write("j11a", L)
