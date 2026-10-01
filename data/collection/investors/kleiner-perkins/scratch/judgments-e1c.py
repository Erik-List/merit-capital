#!/usr/bin/env python3
"""Delta pass, tag e1, batch 1, third block (PRO-99): recall additions kibu-com .. replaytv (14 rows).
Run: NQ_TAG=e1 python3 judgments-e1c.py

Every SEC URL was read through secget.py; press URLs were read with WebFetch or a direct fetch of the page. One
exception is stated on its row: the Nashville Post article behind medibuy is paywalled, and its funding sentence was
read only through the web search's rendering of the page.
"""
import judge_lib as jl
from judge_lib import cls, rnd, verdict, W, FTS

L = []
ASOF = "2026-09-30"

TC_LENDUP_2012 = ("https://techcrunch.com/2012/10/10/lendup-raises-cash-from-kleiner-perkins-andreessen-horowitz-"
                  "google-ventures-and-others-to-disrupt-payday-loans/")
TC_LENDUP_2013 = ("https://techcrunch.com/2013/11/12/lendup-raises-14m-from-google-ventures-data-collective-to-"
                  "disrupt-payday-lending/")
TC_LENDUP_2016 = "https://techcrunch.com/2016/01/22/the-loan-dolphin/"
PULSE_LMARENA = "https://pulse2.com/lmarena-100-million-seed-funding-raised-for-ai-focused-open-community-platform/"
TC_LMARENA = "https://techcrunch.com/2026/01/06/lmarena-lands-1-7b-valuation-four-months-after-launching-its-product/"
NASHPOST_MEDIBUY = ("https://www.nashvillepost.com/medibuy-moves-some-personnel-here-from-san-diego/"
                    "article_bfa8a7ec-b107-57e1-9a2f-bdf6c998cef8.html")
UTORONTO_NANOLEAF = ("https://www.utoronto.ca/news/asia-richest-philanthropist-major-silicon-valley-firm-invest-"
                     "alumni-nanoleaf-light-bulb")
AMD_13D = "https://www.sec.gov/Archives/edgar/data/909183/0000898430-95-002665.txt"
TC_NFTFI = ("https://techcrunch.com/2021/11/16/south-africas-nftfi-raises-5m-so-people-can-use-their-nfts-as-"
            "collateral-for-loans/")
TECHCABAL_NFTFI = "https://techcabal.com/2024/07/16/seychelles-south-africa-blockchain-funding/"
TECHMONITOR_OBLIX = "https://techmonitor.ai/technology/oblix_bags_106m_in_vc_netscape_and_novell_on_board"
OURA_RRA = "https://www.sec.gov/Archives/edgar/data/2133022/000119312526355689/filename3.htm"
AE_8K = "https://www.sec.gov/Archives/edgar/data/927003/000095013405023696/d31435e8vk.htm"
REPLAY_S1 = "https://www.sec.gov/Archives/edgar/data/1103772/000101287000000232/0001012870-00-000232.txt"
W_KIBU = W("Kibu.com")
W_MINISTOR = W("MiniStor")
W_NANOLEAF = W("Nanoleaf")
W_PICABOO = W("Picaboo")
W_PLEXUS = W("Plexus Computers")

# ---------------------------------------------------------------- kibu-com
L.append(verdict("kibu-com", "member",
                 "Wikipedia, Kibu.com: 'In February 2000, Kibu.com received an investment of US$22 million from "
                 "high-profile figures in Silicon Valley, such as Netscape co-founder Jim Clark, former @Home "
                 "Network chairman Tom Jermoluk, the venture capital firm Kleiner Perkins Caufield & Byers, and "
                 "CNET chairman Shelby Bonnie.' One source, naming the firm in the round.",
                 ec="web", conf="medium", cite=W_KIBU))
L.append(cls("kibu-com", status="defunct", rng="below_1b", country="US", stage="undetermined", entry_date="2000-02",
             focus="Media, Gaming & Advertising", flags=["city_unknown"],
             rounds=[rnd("2000-02", "unnamed", 22000000, None, True, W_KIBU, "press")],
             note="Website for teenage girls, created 1999. The $22M of February 2000 is its only known round and "
                  "is not named, so the stage stays undetermined. 'On October 2, 2000, Kibu.com shut down, laying "
                  "off all of its 65 staff members' (Wikipedia): defunct. No source read places its office."))

# ---------------------------------------------------------------- lendup
L.append(verdict("lendup", "member",
                 "TechCrunch, 2012-10-10: LendUp 'is launching today with funding from an impressive group of VC "
                 "firms and angels including Y Combinator, Kleiner Perkins, Yuri Milner's Startfund, Andreessen "
                 "Horowitz, Google Ventures ...'; the Los Angeles Times and Wikipedia also list Kleiner Perkins "
                 "among its backers.",
                 ec="web", conf="high", cite=TC_LENDUP_2012))
L.append(cls("lendup", status="defunct", rng="below_1b", city="San Francisco", stage="Seed", stage_src="model",
             stage_cite=TC_LENDUP_2012, stage_conf="medium", entry_date="2012-10-10", focus="Fintech & Payments",
             grad="graduated", grad_src="web_verified", grad_cite=TC_LENDUP_2016, grad_conf="high",
             rounds=[rnd("2012-10-10", "unnamed (launch funding)", None, None, True, TC_LENDUP_2012, "press"),
                     rnd("2013-11-12", "unnamed ($14M)", 14000000, "Google Ventures", None, TC_LENDUP_2013, "press"),
                     rnd("2016-01-22", "Series B ($50M equity, $100M debt)", 50000000, None, None, TC_LENDUP_2016,
                         "press")],
             note="Online lender to low-credit borrowers, San Francisco; it stopped lending in January 2022 under a "
                  "CFPB order (Wikipedia), defunct as in the a16z, GV and Y Combinator rows. Kleiner Perkins is "
                  "named in the launch funding of October 2012, which TechCrunch does not name; read as the seed "
                  "at medium confidence, as in the GV row (about $4M by the later totals). S2A: graduated; "
                  "TechCrunch (2016-01-22) calls the next equity round a Series B ('$50 million for equity'), "
                  "which does not name Kleiner Perkins."))

# ---------------------------------------------------------------- lmarena
L.append(verdict("lmarena", "member",
                 "Pulse 2.0, 2025-05-26, on the $100M seed: 'led by a16z and UC Investments (University of "
                 "California) with participation from Lightspeed, Laude Ventures, Felicis, Kleiner Perkins and The "
                 "House Fund'; TechCrunch (2026-01-06) names Kleiner Perkins again in the Series A.",
                 ec="web", conf="high", cite=PULSE_LMARENA))
L.append(cls("lmarena", status="private", rng="1b_plus", usd=1700000000, val_src="web_verified",
             val_cite=TC_LMARENA, asof="2026-01", val_conf="high", extra={"valuation_range_source": "web_verified"},
             country="US", city="San Francisco", stage="Seed", stage_src="web_verified", stage_cite=PULSE_LMARENA,
             stage_conf="high", entry_date="2025-05", focus="AI & Applied AI",
             grad="graduated", grad_src="web_verified", grad_cite=TC_LMARENA, grad_conf="high",
             rounds=[rnd("2025-05", "Seed", 100000000, "a16z, UC Investments", True, PULSE_LMARENA, "press"),
                     rnd("2026-01-06", "Series A", 150000000, "Felicis, UC Investments", True, TC_LMARENA, "press")],
             note="AI model evaluation platform out of UC Berkeley, renamed Arena in January 2026; status, mark, "
                  "country and city aligned with the a16z, Felicis and Lightspeed rows (their Arena). Kleiner "
                  "Perkins joined the $100M seed of May 2025. Momentum check 2026-09-30: the mark is the $150M "
                  "Series A 'at a post-money valuation of $1.7 billion' (TechCrunch, 2026-01-06). S2A: graduated, "
                  "that Series A, in which Kleiner Perkins took part."))

# ---------------------------------------------------------------- medibuy
L.append(verdict("medibuy", "member",
                 "Nashville Post, 2001-10-04, as rendered by the web search (the article body is paywalled and was "
                 "not read directly): 'Medibuy received $40 million in July 1999 from several high-profile "
                 "institutional investors, including Kleiner, Perkins, Caufield & Byers, Sequoia Capital, Oak "
                 "Investment Partners and Stanford University', with $77M more five months later. It matches the "
                 "biography in a 2016 8-K ('over $100 million in venture funding from Kleiner-Perkins, Sequoia, Oak "
                 "Investments'). R1 corroboration by press, at medium confidence for the indirect read.",
                 ec="web", conf="medium", cite=NASHPOST_MEDIBUY))
L.append(cls("medibuy", status="acquired", rng="below_1b", country="US", city="San Diego", stage="undetermined",
             entry_date="1999-07", focus="Healthcare & Bio",
             rounds=[rnd("1999-07", "unnamed ($40M)", 40000000, None, True, NASHPOST_MEDIBUY, "press"),
                     rnd("1999-12", "unnamed ($77M)", 77000000, None, None, NASHPOST_MEDIBUY, "press")],
             note="Online marketplace for medical supplies, San Diego, founded 1999 (Nashville Post preview, read "
                  "directly: 'a San Diego, Calif.-based virtual marketplace'; it bought HCA's empactHealth.com in "
                  "2000). The July 1999 round with Kleiner Perkins is not named, and the sentence naming it was "
                  "read through the search engine only (see the verdict). Global Healthcare Exchange absorbed "
                  "Medibuy at the end of 2002 by the judge's knowledge (no page read), so acquired."))

# ---------------------------------------------------------------- ministor-peripherals
L.append(verdict("ministor-peripherals", "member",
                 "Wikipedia, MiniStor: 'MiniStor received seed funding from multiple investors, including Kleiner "
                 "Perkins Caufield & Byers, amounting to $4.2 million by the time of its incorporation' (founded "
                 "May 1991). Before EDGAR's full text, one source.",
                 ec="web", conf="medium", cite=W_MINISTOR))
L.append(cls("ministor-peripherals", status="defunct", rng="below_1b", country="US", city="San Jose", stage="Seed",
             stage_src="web_verified", stage_cite=W_MINISTOR, stage_conf="medium", entry_date="1991",
             focus="Industrial & Robotics",
             grad="graduated", grad_src="web_verified", grad_cite=W_MINISTOR, grad_conf="medium",
             rounds=[rnd("1991", "seed funding", 4200000, None, True, W_MINISTOR, "press"),
                     rnd("1993", "capital from Hitachi (amount not given)", None, "Hitachi", None, W_MINISTOR, "press"),
                     rnd("1994-08", "IPO", None, None, None, W_MINISTOR, "press")],
             note="Maker of 1.8-inch PC Card hard drives, San Jose, 1991 to 1995. The firm was in the $4.2M seed. "
                  "It 'filed its initial public offering in August 1994' and was a public company before 'filing "
                  "Chapter 11 bankruptcy in April 1995 with plans to liquidate its assets' (Wikipedia): defunct. "
                  "S2A: graduated; the Hitachi money of late 1993 and the 1994 IPO are later priced financings, "
                  "their amounts not given in the article, so medium confidence."))

# ---------------------------------------------------------------- nanoleaf
L.append(verdict("nanoleaf", "member",
                 "University of Toronto News, 2014-03-28: Nanoleaf's funding came from 'Li Ka Shing's investment "
                 "group, Horizons Ventures' and 'a Silicon Valley venture capital group called Kleiner Perkins' "
                 "(the founder's words); Wikipedia's Nanoleaf article says the same.",
                 ec="web", conf="high", cite=UTORONTO_NANOLEAF))
L.append(cls("nanoleaf", status="private", rng="below_1b", country="CA", country_src="web_verified",
             country_cite=W_NANOLEAF, city="Toronto", stage="undetermined", entry_date="2014", focus="Consumer & Marketplaces",
             rounds=[rnd("2014-03", "unnamed (first institutional money, reported 2014-03-28)", None, None, True,
                         UTORONTO_NANOLEAF, "press")],
             note="Smart lighting maker founded 2012 by three University of Toronto graduates; the CA claim is "
                  "confirmed, 'Nanoleaf opened their Headquarters in Toronto, Canada, in January 2015' (Wikipedia), "
                  "after a start in Shenzhen. The round Kleiner Perkins and Horizons funded after the Kickstarter "
                  "campaign is not named or sized in any source read. Still selling products in 2026."))

# ---------------------------------------------------------------- nexgen
L.append(verdict("nexgen", "member",
                 "AMD's Schedule 13D on NexGen, 1995-12-19: 'The stockholders of NexGen which have executed Voting "
                 "Agreements are Kleiner Perkins Caufield & Byers IV, Olivetti Holdings, ... Compaq Computer "
                 "Corporation', KPCB IV with 1,360,869 shares. A fund from 1986 holding the company it backed "
                 "before the 1995 IPO (Wikipedia: 'funded by Compaq, ASCII and Kleiner Perkins').",
                 ec="fund_filing", conf="high", cite=AMD_13D))
L.append(cls("nexgen", rng="below_1b", country="US", city="Milpitas", stage="undetermined", rounds=[],
             focus="Industrial & Robotics", flags=["model_disputes_source"],
             note="x86 microprocessor designer, Milpitas, California, founded 1986 and bought by AMD (the merger "
                  "closed 1996-01-16). The pre-filled LU and the acquirer 'NeXgen Patners' are a wrong join on "
                  "the name. Wikipedia has the first money from Compaq and Olivetti, 'joined in a later round by "
                  "venture capital firm Kleiner Perkins'; the round and its year are not on record."))

# ---------------------------------------------------------------- nftfi
L.append(verdict("nftfi", "member",
                 "TechCrunch, 2021-11-16: NFTfi 'has raised a seed round of $5 million ... Early-stage crypto fund "
                 "1kx led the round, with Ashton Kutcher's Sound Ventures, Maven 11, Scalar Capital, Kleiner Perkins "
                 "and others participating'.",
                 ec="web", conf="high", cite=TC_NFTFI))
L.append(cls("nftfi", status="private", rng="below_1b", country="ZA", country_src="web_verified",
             country_cite=TC_NFTFI, stage="Seed", stage_src="web_verified", stage_cite=TC_NFTFI, stage_conf="high",
             entry_date="2021-11", focus="Crypto & Web3", flags=["city_unknown"],
             grad="graduated", grad_src="web_verified", grad_cite=TECHCABAL_NFTFI, grad_conf="medium",
             rounds=[rnd("2021-11-16", "Seed", 5000000, "1kx", True, TC_NFTFI, "press"),
                     rnd("2023", "unnamed ($18M, per the CV VC Africa Blockchain report)", 18000000, None, None,
                         TECHCABAL_NFTFI, "press")],
             note="Peer-to-peer loans against NFTs; founded in South Africa, where most of the team lives, and "
                  "incorporated in the British Virgin Islands (TechCrunch); no source read gives a city. Kleiner "
                  "Perkins joined the $5M seed of November 2021. S2A: graduated, medium confidence; TechCabal "
                  "(2024-07-16), citing the CV VC Africa Blockchain report on 2023 funding: 'In South Africa, "
                  "Momint raised $2.7 million, while NFTfi secured $18 million', an unnamed later round above "
                  "twice the seed. The round's own announcement was not found and should be cited by a later pass."))

# ---------------------------------------------------------------- oblix
L.append(verdict("oblix", "member",
                 "Tech Monitor (Computergram), 1998-12-10: Oblix 'has completed its second round of venture "
                 "funding, bagging $10.6m', led by Patricof & Co Ventures, with 'follow-on capital from original "
                 "investors Kleiner Perkins Caufield & Byers and The Java Fund' (the KPCB Java Fund). R1 "
                 "corroborated by press naming the firm in the rounds.",
                 ec="web", conf="high", cite=TECHMONITOR_OBLIX))
L.append(cls("oblix", status="acquired", rng="below_1b", country="US", city="Cupertino", stage="undetermined",
             focus="Security", flags=["model_disputes_source"],
             rounds=[rnd(None, "first round (original investors Kleiner Perkins and the Java Fund; date and name "
                               "not on record)", None, None, True, TECHMONITOR_OBLIX, "press"),
                     rnd("1998-12", "second round", 10600000, "Patricof & Co Ventures", True, TECHMONITOR_OBLIX,
                         "press")],
             note="Identity and access management software; 'the Mountain View, California-based software "
                  "company' in 1998 (Tech Monitor), in Cupertino when Oracle bought it in 2005. The pre-filled GB "
                  "is a wrong join on the one-word name. Kleiner Perkins was an original investor, in the first "
                  "round before December 1998, which no source read names or dates."))

# ---------------------------------------------------------------- oura (sale consideration)
L.append(verdict("oura", "not_member",
                 "Sale consideration (Erik 2026-09-22; R5): KPCB Holdings signs Oura's Registration Rights Agreement "
                 "of 2026-03-31 as a stockholder, but no source names Kleiner Perkins in an Oura round (Wikipedia's "
                 "investor lists for every round omit it). Its stock traces to Proxy, the firm's 2019 Series A "
                 "company, which Oura bought in an all-equity deal in 2023 (the row proxy). The Oura director with "
                 "a Kleiner Perkins past, Wen Hsieh, joined in November 2025 from his own firm.",
                 ec="fund_filing", conf="medium", cite=OURA_RRA))

# ---------------------------------------------------------------- picaboo
L.append(verdict("picaboo", "member",
                 "Wikipedia, Picaboo (photo books, Palo Alto, founded 2002): 'Series-A funding was secured from "
                 "Kleiner Perkins and Softbank.' One source, naming the firm in the round.",
                 ec="web", conf="medium", cite=W_PICABOO))
L.append(cls("picaboo", status="acquired", rng="below_1b", city="Palo Alto", stage="Series A",
             stage_src="web_verified", stage_cite=W_PICABOO, stage_conf="medium", focus="Consumer & Marketplaces",
             rounds=[rnd(None, "Series A (year not given; between the 2002 founding and the 2005 launch)", None,
                         None, True, W_PICABOO, "press")],
             note="Photo book and yearbook maker founded in Palo Alto in 2002 (city aligned with the NEA row). "
                  "The firm's entry is the Series A with Softbank, which the article does not date, so no entry "
                  "date is given. Status is fresher than the NEA row's private: 'In 2025 Picaboo was purchased by "
                  "Entrouage Yearbooks and the company relocated its headquarters to Princeton, NJ' (Wikipedia)."))

# ---------------------------------------------------------------- plexus-computers
L.append(verdict("plexus-computers", "member",
                 "Wikipedia, Plexus Computers: after leaving Onyx in 1980 the founders 'secured over $18.5 million "
                 "in startup capital from 17 large investment firms', among them Kleiner Perkins, Hambrecht & Quist "
                 "and L.F. Rothschild. Before EDGAR, one source, naming the firm in the funding.",
                 ec="web", conf="medium", cite=W_PLEXUS))
L.append(cls("plexus-computers", status="acquired", rng="below_1b", country="US", city="San Jose",
             stage="undetermined", focus="Industrial & Robotics",
             rounds=[rnd("1980", "startup capital from 17 firms (rounds not separated)", 18500000, None, True,
                         W_PLEXUS, "press")],
             note="Unix minicomputer maker founded September 1980 in Santa Clara; status and city aligned with the "
                  "Battery Ventures row. The $18.5M of startup capital is not split into rounds, so the stage "
                  "stays undetermined. It filed Chapter 11 in 1989 and 'In July 1989, Recognition Equipment, Inc., "
                  "of Dallas, Texas, acquired Plexus for $5 million' (Wikipedia): a sale out of insolvency, "
                  "acquired."))

# ---------------------------------------------------------------- portera (R1, not corroborated)
L.append(verdict("portera", "not_member",
                 "R1: the sources are a biography in Advanced Energy's 2005 8-K ('Portera, a Kleiner-Perkins "
                 "company') and Ted Schlein's board seat at Portera Systems in Corio's proxies, which locate a "
                 "person. No fund on a filing, no listing and no press or company source naming Kleiner Perkins in "
                 "a Portera round was found (the one funding table found is a vendor's and does not name the "
                 "firm), so the candidate is not added.",
                 ec="web", conf="medium", cite=AE_8K))

# ---------------------------------------------------------------- replaytv
L.append(verdict("replaytv", "member",
                 "ReplayTV's S-1 of 2000-01-26, private placement transactions: 'Entities affiliated with KPCB "
                 "Holdings (William R. Hearst III)' bought 7,870,968 Series D and 133,333 Series E preferred "
                 "shares; 'All shares are held by KPCB Holdings Inc., as nominee.' The funds' nominee on the "
                 "company's own filing.",
                 ec="fund_filing", conf="high", cite=REPLAY_S1))
L.append(cls("replaytv", status="acquired", rng="below_1b", country="US", city="Mountain View", stage="Growth",
             stage_src="web_verified", stage_cite=REPLAY_S1, stage_conf="high", entry_date="1999-03-24",
             focus="Consumer & Marketplaces", flags=["model_disputes_source"],
             rounds=[rnd("1998-11", "Series C ($0.632)", 2000000, None, False, REPLAY_S1, "filing"),
                     rnd("1999-03-24", "Series D ($0.775)", 7900000, "KPCB Holdings", True, REPLAY_S1, "filing"),
                     rnd("1999-07-30", "Series E ($7.50)", 52249973, None, True, REPLAY_S1, "filing")],
             note="Digital video recorder maker, Mountain View (the S-1's office). KPCB Holdings took 7,870,968 of "
                  "the 10,193,544 Series D shares sold on 1999-03-24 for $7.9M, when its partner joined the board; "
                  "the record names the round Series D, after three small earlier series, so Growth. Status "
                  "disputes the pre-filled defunct: ReplayTV, Inc. was merged into SONICblue in 2001 (the merger "
                  "agreement is an exhibit to SONICblue's S-4 of 2001-04-20), so acquired; the brand's later "
                  "owners went bankrupt in 2015 (Wikipedia)."))

if __name__ == "__main__":
    jl.write("e1c", L)
