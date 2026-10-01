#!/usr/bin/env python3
"""Delta pass, tag e1, batch 1, first block (PRO-99): recall additions q-entertainment .. evant (15 rows).
Run: NQ_TAG=e1 python3 judgments-e1a.py

Skipped (JUDGE-BRIEF run notes, a duplicate awaiting the merge): entremed-inc.
Google News answered an error on 2026-09-30, so no headline was decoded. Every SEC URL below was read through
secget.py (or the EDGAR full-text index); every press URL was read with WebFetch or printed by a publisher's own
search (TechCrunch, Crunchbase News, TechJuice, BetaKit WordPress search), unless the note says otherwise.
"""
import judge_lib as jl
from judge_lib import cls, rnd, verdict, W

L = []
ASOF = "2026-09-30"

# ---- URLs read in this pass
SEEC_PR = "https://www.sec.gov/Archives/edgar/data/925524/000095012803000076/j9836201exv99w1.txt"
ASIG_VOTE = "https://www.sec.gov/Archives/edgar/data/1843121/000110465922104204/tm2226813d1_ex10-2.htm"
TFN_ATLANTIC = "https://techfundingnews.com/founded-by-rohinhood-alumni-atlantic-money-takes-on-wise-paypal-picks-4-5m/"
GB_ATLANTIC = "https://growthbusiness.co.uk/deals-of-the-week-july-18-to-july-22-a-growth-business-round-up-20194/"
FINOVATE_ATLANTIC = "https://finovate.com/deel-acquires-atlantic-money-for-undisclosed-sum/"
NETMANAGE_10K = "https://www.sec.gov/Archives/edgar/data/909793/000119312505057729/d10k.htm"
SHAPR_CAD = "https://www.shapr3d.com/history-of-cad/miscellaneous-companies"
CRYOCOR_IRA = "https://www.sec.gov/Archives/edgar/data/1125294/000119312505070157/dex42.htm"
CRYOCOR_S1 = "https://www.sec.gov/Archives/edgar/data/1125294/000119312505070157/ds1.htm"
AMS_MERGER = "https://www.sec.gov/Archives/edgar/data/1114200/000095013402015687/c73602exv2w1.txt"
CVIE_13D = "https://www.sec.gov/Archives/edgar/data/946486/000143774918022825/ivbh20181227_sc13d.htm"
WINT_8K = "https://www.sec.gov/Archives/edgar/data/946486/000143774918022544/wint20181221_8k.htm"
TC_DAISIE = "https://techcrunch.com/2019/05/20/maisie-williams-talent-discovery-startup-daisie-raises-2-5-million-hits-100k-members/"
TC_DBANK = "https://techcrunch.com/2022/07/27/sequoia-kleiner-perkins-nubank-invest-in-pakistan-fintech-dbank/"
TC_MASSDROP_A = "https://techcrunch.com/2014/09/24/massdrop-series-a/"
TC_MASSDROP_B = "https://techcrunch.com/2015/08/13/massdrop-series-b/"
MANH_MERGER = "https://www.sec.gov/Archives/edgar/data/1056696/000095014405008854/g96995exv2w1.txt"
W_EESTOR = W("EEStor")
W_DROP = W("Drop (company)")

# ---------------------------------------------------------------- q-entertainment (listed; KPCB China)
L.append(cls("q-entertainment", status="defunct", rng="below_1b", city="Tokyo", stage="undetermined", rounds=[],
             focus="Media, Gaming & Advertising", flags=["kpcb_china"],
             note="Tokyo game studio of Tetsuya Mizuguchi (Lumines, Child of Eden), on the firm's China listing from "
                  "2010 and its company pages under Teams China and Digital (X1, flagged kpcb_china). Wikipedia: it "
                  "'was a Japanese video game developer'; Mizuguchi left in 2013 'as the parent company went defunct' "
                  "and its last title shipped in 2012, so defunct. No source names the KPCB China round."))

# ---------------------------------------------------------------- asera
L.append(verdict("asera", "member",
                 "SEEC's own release of January 2003 (8-K exhibit): on buying Asera's assets it made an agreement "
                 "'with Asera's bridge lenders, who include Kleiner Perkins Caufield & Byers', whose debts were "
                 "converted into SEEC equity or paid; KPCB IX entities then filed the 13D on SEEC, and Vinod Khosla "
                 "sat on Asera's board (Juniper's 2001 proxy). The firm's money was in Asera (R1 corroborated by a "
                 "company source; R5: Asera is the row, SEEC is sale consideration and a public purchase).",
                 ec="web", conf="medium", cite=SEEC_PR))
L.append(cls("asera", status="acquired", rng="below_1b", country="US", city="Belmont", stage="undetermined",
             focus="SaaS",
             rounds=[rnd("2003-01", "bridge loans outstanding at the asset sale", None, None, True, SEEC_PR, "company")],
             note="E-business application software, Belmont, California, started by Vinod Khosla at Kleiner Perkins. "
                  "SEEC bought its assets in January 2003 (SEEC's release), an asset sale that ended the company, so "
                  "acquired with SEEC as successor. The firm's equity rounds are not named in any source read; only "
                  "its bridge loans are on record."))

# ---------------------------------------------------------------- asia-innovations-group (KPCB China Fund II)
L.append(verdict("asia-innovations-group", "member",
                 "The Company Shareholder Voting Agreement of 2022-09-30 for the Magnum Opus merger is signed by "
                 "'KPCB CHINA FUND II, L.P. By: /s/ Susan Biglieri', 2750 Sand Hill Road, as a shareholder of Asia "
                 "Innovations Group Limited: a KPCB China fund position, IN under X1's provisional reading.",
                 ec="fund_filing", conf="high", cite=ASIG_VOTE))
L.append(cls("asia-innovations-group", status="private", rng="below_1b", country="SG", country_src="web_verified",
             country_cite=ASIG_VOTE, city="Singapore", stage="undetermined", rounds=[],
             focus="Media, Gaming & Advertising", flags=["kpcb_china"],
             note="Live social apps (Uplive), a Cayman company run from Singapore (its founders sign the 2022 voting "
                  "agreement from a Singapore address). The 2022 merger with the SPAC Magnum Opus was terminated in "
                  "2023, so its reported $2.5B value never priced a closed deal and the row stays below $1B. The "
                  "round KPCB China Fund II entered is not named in the filing."))

# ---------------------------------------------------------------- atlantic-money
L.append(verdict("atlantic-money", "member",
                 "Tech Funding News, 2022-03-09, on the $4.5M seed: 'The round led by Amplo and Ribbit Capital "
                 "alongside participation from Kleiner Perkins, Index Ventures, Harry Stebbings' 20VC, Elefund'; "
                 "Growth Business (2022-07-22) repeats Kleiner Perkins in the initial seed.",
                 ec="web", conf="high", cite=TFN_ATLANTIC))
L.append(cls("atlantic-money", status="acquired", rng="below_1b", country="GB", country_src="web_verified",
             country_cite=FINOVATE_ATLANTIC, city="London", stage="Seed", stage_src="web_verified",
             stage_cite=TFN_ATLANTIC, stage_conf="high", entry_date="2022-03", focus="Fintech & Payments",
             grad="not_graduated", grad_src="web_verified", grad_cite=FINOVATE_ATLANTIC, grad_conf="high",
             grad_asof=ASOF,
             surfaces=[
                 "firm: the firm's own posts and listings for Atlantic Money -> no post names the company and it is "
                 "not on the live list",
                 "techcrunch: TechCrunch's own search for Atlantic Money -> 30 results, none naming the company",
                 "crunchbase_news: Crunchbase News's own search for Atlantic Money -> 30 results, none naming the company",
                 "growthbusiness: Growth Business deals round-up of 2022-07-22 -> a $3M seed extension led by Amplo, "
                 "the last money found",
                 "finovate: Finovate, 2024-12-02 -> 'Deel has acquired U.K.-based international funds transfer "
                 "company Atlantic Money'; no round after the seed",
                 "wikipedia: the Atlantic Money article -> seed funding of $7.5M over two phases in 2022, no later round",
                 "sibling:20vc: its row for Atlantic Money -> S2A not_graduated (web_verified)",
                 "sibling:ribbit-capital: its row for Atlantic Money -> S2A not_graduated (web_verified)"],
             rounds=[rnd("2022-03", "Seed", 4500000, "Amplo, Ribbit Capital", True, TFN_ATLANTIC, "press"),
                     rnd("2022-07", "Seed extension", 3000000, "Amplo", None, GB_ATLANTIC, "press"),
                     rnd("2024-12", "acquisition by Deel", None, "Deel", None, FINOVATE_ATLANTIC, "press")],
             note="Fixed-fee international money transfers, London, founded by Robinhood alumni. Kleiner Perkins "
                  "joined the $4.5M seed of March 2022 (Tech Funding News). Deel bought it (Finovate, 2024-12-02), "
                  "aligned with the 20VC and Ribbit rows. S2A: not graduated; the seed and its July 2022 extension "
                  "were the last rounds before the sale."))

# ---------------------------------------------------------------- broadband-office (R1, not corroborated)
L.append(verdict("broadband-office", "not_member",
                 "R1: the only sources are biographies in other companies' filings ('an internet start-up funded by "
                 "Kleiner-Perkins Caulfield & Byer, Microsoft and Sun', NetManage 10-K; 'a Kleiner Perkins Caufield "
                 "& Byers start-up', Borland 8-K; 'consultant to Kleiner, Perkins, Caufield and Byers/Broadband "
                 "Office', Avaya 10-K) and Vinod Khosla's board seat (Juniper's 2001 proxy). No fund on a filing, "
                 "no listing and no press or company source naming Kleiner Perkins in a round was found, so the "
                 "candidate is not added.",
                 ec="web", conf="medium", cite=NETMANAGE_10K))

# ---------------------------------------------------------------- cimlinc
L.append(verdict("cimlinc", "member",
                 "The History of CAD (Shapr3D's edition of Weisberg's book): Cadlinc, renamed Cimlinc in November "
                 "1985, 'In four rounds of funding ... raised $24 million in venture capital from a number of "
                 "investment firms including Kleiner, Perkins, Caufield and Byers and The Hillman Group'; the "
                 "founder's own account in a 2016 offering memorandum agrees ('raised $26 million in funding from "
                 "venture capital firms such as Kleiner Perkins Caufield & Byers', John Doerr on the board for ten "
                 "years). R1 corroborated by a press source naming the firm in the rounds.",
                 ec="web", conf="medium", cite=SHAPR_CAD))
L.append(cls("cimlinc", status="acquired", rng="below_1b", country="US", city="Itasca", stage="undetermined",
             focus="Industrial & Robotics",
             rounds=[rnd("1981", "four venture rounds from the 1981 founding (entry round not named)", 24000000, None,
                         True, SHAPR_CAD, "press")],
             note="CAD/CAM workstations and manufacturing software, founded April 1981 as Cadlinc in Elk Grove, "
                  "Illinois, later consolidated in Itasca. The firm was in its four venture rounds, but no source "
                  "says which it entered. The History of CAD has the AMT division sold to SofTech in late 1997 and "
                  "the rest gone by 2001; the founder says it 'was sold to Boeing'. The business left by sale of "
                  "its parts, so acquired, with that conflict noted."))

# ---------------------------------------------------------------- columbia-care-l-l-c (homonym)
L.append(verdict("columbia-care-l-l-c", "not_member",
                 "Homonym: the Michael Abbott named Executive Officer on Columbia Care's 2014 Form D is the "
                 "cannabis company's own co-founder and executive chairman, a former Goldman Sachs banker in New "
                 "York, not Mike Abbott the Kleiner Perkins partner (formerly Twitter's engineering head). Nothing "
                 "ties a Kleiner Perkins fund to Columbia Care.",
                 ec="formd_adjudicated", conf="high"))

# ---------------------------------------------------------------- cryocor
L.append(verdict("cryocor", "member",
                 "CryoCor's Amended and Restated Investors' Rights Agreement of 2003-06-04 (S-1 exhibit 4.2) is "
                 "signed by 'KLEINER PERKINS CAUFIELD & BYERS VIII', 'KPCB LIFE SCIENCES ZAIBATSU FUND II' and "
                 "'KPCB VIII FOUNDERS FUND', by Brook Byers, and lists them among the earlier investors (its Schedule A): Kleiner "
                 "Perkins funds held the private company before its 2005 IPO.",
                 ec="fund_filing", conf="medium", cite=CRYOCOR_IRA))
L.append(cls("cryocor", status="acquired", rng="below_1b", country="US", city="San Diego", stage="undetermined",
             focus="Healthcare & Bio",
             rounds=[rnd("2000-08-31", "Series A and common issued to CryoGen for the assets", None, None, None,
                         CRYOCOR_S1, "filing"),
                     rnd("2003-06-04", "Series D", None, None, None, CRYOCOR_IRA, "filing")],
             note="Cardiac cryoablation, San Diego. The S-1: incorporated 2000-08-15 and on 2000-08-31 'acquired "
                  "assets ... from CryoGen, Inc. in exchange for our issuance of Series A convertible preferred "
                  "stock and common stock to CryoGen', so the funds' position traces to their CryoGen holding (the "
                  "row cryogen) and no round they bought is on record. Boston Scientific bought CryoCor in 2008."))

# ---------------------------------------------------------------- cryogen
L.append(verdict("cryogen", "member",
                 "The 2002 merger agreement with American Medical Systems lists as a closing condition the "
                 "termination of 'The letter agreement regarding \"Management Rights\", dated as of January 27, "
                 "1997, between the Company and Kleiner Perkins Caufield & Byers VIII': the fund itself held "
                 "management rights in Cryogen, the letter a venture fund takes with its investment.",
                 ec="fund_filing", conf="high", cite=AMS_MERGER))
L.append(cls("cryogen", status="acquired", rng="below_1b", country="US", city="San Diego", stage="undetermined",
             entry_date="1997-01", focus="Healthcare & Bio",
             rounds=[rnd("1997-01-27", "unnamed (the purchase behind the management rights letter)", None, None,
                         True, AMS_MERGER, "filing")],
             note="Cryosurgery devices (Her Option), San Diego. KPCB VIII's management rights letter is dated "
                  "1997-01-27, read as the date of its investment; the round is not named. American Medical Systems "
                  "acquired Cryogen under the December 2002 merger agreement."))

# ---------------------------------------------------------------- cvie-therapeutics (KPCB China Fund II)
L.append(verdict("cvie-therapeutics", "member",
                 "Schedule 13D of 2018-12-31 on Windtree: the shares issued to CVie's former holders are held by "
                 "Ivy Blue Holdings, and 'KPCB China Fund II, L.P. is the 100% owner of Ivy Blue Holdings Limited'. "
                 "R5: the member is CVie, the private company the fund held; the Windtree stock is sale "
                 "consideration. A KPCB China fund position, IN under X1's provisional reading.",
                 ec="fund_filing", conf="high", cite=CVIE_13D))
L.append(cls("cvie-therapeutics", status="acquired", rng="below_1b", country="TW", country_src="web_verified",
             country_cite=WINT_8K, city="Taipei", stage="undetermined", rounds=[], focus="Healthcare & Bio",
             flags=["kpcb_china"],
             note="Cardiovascular drug developer; Windtree's 8-K calls the operating company 'CVie Therapeutics "
                  "Limited, a Taiwan corporation'. Windtree Therapeutics acquired it in the merger that closed "
                  "2018-12-21. The round KPCB China Fund II entered is not in the filings."))

# ---------------------------------------------------------------- daisie
L.append(verdict("daisie", "member",
                 "TechCrunch, 2019-05-20: Daisie 'recently closed on $2.5 million in seed funding. The round was led "
                 "by Founders Fund ... Other investors included 8VC, Kleiner Perkins, and ... Shrug Capital'.",
                 ec="web", conf="high", cite=TC_DAISIE))
L.append(cls("daisie", status="private", rng="below_1b", country="GB", country_src="web_verified",
             country_cite=TC_DAISIE, city="London", stage="Seed", stage_src="web_verified", stage_cite=TC_DAISIE,
             stage_conf="high", entry_date="2019-05", focus="Consumer & Marketplaces",
             grad="not_graduated", grad_src="absence_check", grad_asof=ASOF,
             surfaces=[
                 "firm: the firm's own posts and listings for Daisie -> no post names the company and it is not on "
                 "the live list",
                 "techcrunch: TechCrunch's own search for Daisie -> 30 results, none reporting a later round of the "
                 "company; the seed report of 2019-05-20 is its only funding story",
                 "crunchbase_news: Crunchbase News's own search for Daisie -> 1 result (2019-05-24), not about a "
                 "round of the company",
                 "pulse2: Pulse 2.0's own search for Daisie -> 2 results, neither naming the company"],
             rounds=[rnd("2019-05", "Seed", 2500000, "Founders Fund", True, TC_DAISIE, "press")],
             note="Maisie Williams' network for creators, London (TechCrunch puts its members and team there). "
                  "Kleiner Perkins joined the $2.5M seed of May 2019. Its site still answers (2026-09-30), so "
                  "private. S2A: not graduated; the absence test found no later round (surfaces listed)."))

# ---------------------------------------------------------------- dbank
L.append(verdict("dbank", "member",
                 "TechCrunch, 2022-07-27: Dbank 'has raised $17.6 million in a seed round, the largest in Pakistan, "
                 "co-led by Sequoia Capital Southeast Asia' and Kleiner Perkins, with Nubank, Askari Bank and Rayn.",
                 ec="web", conf="high", cite=TC_DBANK))
L.append(cls("dbank", status="unknown", rng="below_1b", country="PK", country_src="web_verified",
             country_cite=TC_DBANK, city="Islamabad", stage="Seed", stage_src="web_verified", stage_cite=TC_DBANK,
             stage_conf="high", entry_date="2022-07", focus="Fintech & Payments",
             grad="not_graduated", grad_src="absence_check", grad_asof=ASOF,
             surfaces=[
                 "firm: the firm's own posts and listings for Dbank -> no post names the company and it is not on "
                 "the live list",
                 "techcrunch: TechCrunch's own search for Dbank -> 2 results, the seed report of 2022-07-27 the only "
                 "one naming the company",
                 "crunchbase_news: Crunchbase News's own search for Dbank -> 18 results, none naming the company",
                 "techjuice: TechJuice's own search for Dbank (Pakistan) -> 22 results, the seed report of "
                 "2022-07-29 the only one naming the company"],
             rounds=[rnd("2022-07", "Seed", 17600000, "Sequoia Capital Southeast Asia, Kleiner Perkins", True,
                         TC_DBANK, "press")],
             note="Digital bank project, Islamabad (founded 2021). Kleiner Perkins co-led the $17.6M seed. Its state "
                  "could not be established from a page read in this pass: by the judge's recollection it wound "
                  "down in 2023 after Pakistan's five digital bank licences went to others, which a later pass "
                  "should cite; until then unknown. Momentum check 2026-09-30 (TechCrunch, Crunchbase News and "
                  "TechJuice searches): no round after the seed, no $1B+ round. S2A: not graduated; the absence "
                  "test found no later round (surfaces listed)."))

# ---------------------------------------------------------------- drop (Massdrop)
L.append(verdict("drop", "member",
                 "TechCrunch, 2014-09-24: Massdrop (renamed Drop in 2018) 'has raised $6.5 million in Series A "
                 "funding. The round was led by Mayfield Fund' with 'additional investment from previous backers "
                 "Kleiner Perkins Caufield & Byers, First Round Capital, and Cowboy Ventures'; Wikipedia's Drop "
                 "(company) article carries the same round.",
                 ec="web", conf="high", cite=TC_MASSDROP_A))
L.append(cls("drop", status="acquired", rng="below_1b", country="US", city="San Francisco", stage="Seed",
             stage_src="model", stage_cite=TC_MASSDROP_A, stage_conf="medium", entry_date="2014",
             focus="Consumer & Marketplaces", flags=["model_disputes_source"],
             grad="graduated", grad_src="web_verified", grad_cite=TC_MASSDROP_A, grad_conf="high",
             rounds=[rnd(None, "seed (about $1.5M by the totals; date not on record)", 1500000, None, True,
                         TC_MASSDROP_A, "press"),
                     rnd("2014-09-24", "Series A", 6500000, "Mayfield Fund", True, TC_MASSDROP_A, "press"),
                     rnd("2015-08-13", "Series B", 40000000, "August Capital", None, TC_MASSDROP_B, "press"),
                     rnd("2023-07-17", "acquisition by Corsair", None, "Corsair", None, W_DROP, "press")],
             note="This Drop is Massdrop, the San Francisco community commerce company (the recall note's 'Dublin' "
                  "and the pre-filled FR are wrong joins on the one-word name; the same company as the First Round "
                  "row). Kleiner Perkins was a 'previous backer' at the $6.5M Series A of September 2014, which took "
                  "the total to $8M, so it entered in the roughly $1.5M round before it, read as the seed; that "
                  "round's date is not on record (2014 at the latest, as in the First Round row). Corsair acquired "
                  "Drop on 2023-07-17 and closed the store in March 2026 (Wikipedia), fresher than the First Round "
                  "row's private. S2A: graduated, the $6.5M Series A of September 2014 (TechCrunch)."))

# ---------------------------------------------------------------- eestor
L.append(verdict("eestor", "member",
                 "Wikipedia, EEStor: 'In July 2005, Kleiner Perkins Caufield & Byers invested $3 million in EEStor', "
                 "and on 2013-12-30 ZENN completed 'the purchase of Series A preferred shares of EEStor (includes "
                 "Kleiner Perkins Caufield & Byers shares ...)'; the ZENN Motor Company article agrees ('KPCB "
                 "invested $3 million in EEStor in 2005 for approximately 20% ownership').",
                 ec="web", conf="medium", cite=W_EESTOR))
L.append(cls("eestor", status="acquired", rng="below_1b", country="US", city="Cedar Park", stage="Series A",
             stage_src="web_verified", stage_cite=W_EESTOR, stage_conf="medium", entry_date="2005-07",
             focus="Climate & Energy",
             rounds=[rnd("2005-07", "Series A", 3000000, "Kleiner Perkins Caufield & Byers", True, W_EESTOR, "press"),
                     rnd("2007-04", "ZENN Motor Company investment (3.8%)", 2500000, "ZENN Motor Company", None,
                         W_EESTOR, "press"),
                     rnd("2009-07", "ZENN Motor Company investment (to 10.7%)", 5000000, "ZENN Motor Company", None,
                         W_EESTOR, "press")],
             note="Ceramic ultracapacitor developer, Cedar Park, Texas. The firm put $3M in during July 2005 and "
                  "the shares ZENN later bought from it were Series A preferred, so a Series A entry (one source "
                  "family, Wikipedia and the ZENN disclosure it quotes). ZENN took control through the December "
                  "2013 purchase and held 71% by 2015, then took the EEStor name itself: acquired."))

# ---------------------------------------------------------------- evant (R2, not corroborated)
L.append(verdict("evant", "not_member",
                 "R2 and R1: the 2005 merger agreement names 'Ted Schlein, as Shareholder Representative', care of "
                 "Kleiner Perkins, and Corio's proxies list his board seats at Nonstop Solutions and Evant, all of "
                 "which locate the person. No fund is named in any filing read, the firm never listed the company, "
                 "and the only source putting Kleiner Perkins in a round (the June 2004 Series C) is a vendor page, "
                 "which cannot cite. Not added without that corroboration.",
                 ec="web", conf="medium", cite=MANH_MERGER))

if __name__ == "__main__":
    jl.write("e1a", L)
