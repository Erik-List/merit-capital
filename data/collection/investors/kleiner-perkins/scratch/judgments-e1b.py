#!/usr/bin/env python3
"""Delta pass, tag e1, batch 1, second block (PRO-99): recall additions evervault .. keplar (15 rows).
Run: NQ_TAG=e1 python3 judgments-e1b.py

Every SEC URL was read through secget.py (the 1999 prospectuses as the complete submission text of the accession the
EDGAR company index printed); press URLs were read with WebFetch or a direct fetch of the page.
"""
import judge_lib as jl
from judge_lib import cls, rnd, verdict, W, FTS, POST

L = []
ASOF = "2026-09-30"

TC_EVERVAULT = ("https://techcrunch.com/2019/10/16/evervault-raises-3-2m-from-sequoia-kleiner-for-an-api-to-build-"
                "apps-with-privacy-baked-in/")
SR_EVERVAULT_A = "https://www.siliconrepublic.com/start-ups/shane-curran-evervault-series-a-funding"
SR_EVERVAULT_B = "https://www.siliconrepublic.com/start-ups/evervault-data-security-funding-ireland-series-b"
FM_S1A = "https://www.sec.gov/Archives/edgar/data/949968/0000950128-99-001169.txt"
FM_PROXY = "https://www.sec.gov/Archives/edgar/data/949968/000095012801500080/j8828101def14a.txt"
SFGATE_GEOCAST = "https://www.sfgate.com/business/article/Geocast-Reveals-Its-Secret-Technology-System-2903480.php"
KP_NETSCAPE = "https://www.kleinerperkins.com/perspectives/netscape/"
CARSDIRECT_IRA = "https://www.sec.gov/Archives/edgar/data/1080131/000104746907005760/a2178793zex-4_3.htm"
HIMAX_6K = "https://www.sec.gov/Archives/edgar/data/1342338/000117184313002856/newsrelease.htm"
HIPPO_S1 = FTS("Hippo", "S-1")
HG_S1 = "https://www.sec.gov/Archives/edgar/data/1100408/0001032210-99-001757.txt"
WSTM_RRA = "https://www.sec.gov/Archives/edgar/data/1095266/000095011602002035/ex4-8.txt"
CARDIUM_APA = FTS("Cardium", "8-K")
MEDIX_PR = "https://www.sec.gov/Archives/edgar/data/890784/000094930301500017/exhibit99-1.htm"
BETAKIT_JETTI = "https://betakit.com/jetti-resources-raises-642000-for-cleantech-mining-project/"
CBN_UNICORNS = "https://news.crunchbase.com/venture/unicorn-board-new-companies-list-october-2022-fintch-web3/"
TC_KEPLAR = ("https://techcrunch.com/2025/09/17/kleiner-perkins-backed-voice-ai-startup-keplar-aims-to-replace-"
             "traditional-market-research/")
KP_AOL = POST("aol")
W_ROYSTON = W("Ivor Royston")
W_IMAGIC = W("Imagic")
W_HIMAX = W("Himax")

# ---------------------------------------------------------------- evervault
L.append(verdict("evervault", "member",
                 "TechCrunch, 2019-10-16: Evervault 'has raised $3.2 million in seed funding ... Led by Sequoia, the "
                 "round also includes Kleiner Perkins, Frontline, SV Angel'; Silicon Republic names Kleiner Perkins "
                 "again in the 2020 Series A and the 2026 Series B.",
                 ec="web", conf="high", cite=TC_EVERVAULT))
L.append(cls("evervault", status="private", rng="below_1b", country="IE", country_src="web_verified",
             country_cite=TC_EVERVAULT, city="Dublin", stage="Seed", stage_src="web_verified",
             stage_cite=TC_EVERVAULT, stage_conf="high", entry_date="2019-10", focus="Security",
             grad="graduated", grad_src="web_verified", grad_cite=SR_EVERVAULT_A, grad_conf="high",
             rounds=[rnd("2019-10-16", "Seed", 3200000, "Sequoia", True, TC_EVERVAULT, "press"),
                     rnd("2020-05-21", "Series A", 16000000, "Index Ventures", True, SR_EVERVAULT_A, "press"),
                     rnd("2026-03-06", "Series B", 25000000, "Ribbit Capital", True, SR_EVERVAULT_B, "press")],
             note="Encryption infrastructure for developers, Dublin (TechCrunch: 'founded by a 19-year-old in "
                  "Dublin, Ireland'), aligned with the Sequoia and Ribbit rows. Kleiner Perkins joined the $3.2M "
                  "seed of October 2019. The latest round is the $25M Series B of March 2026 (Silicon Republic, "
                  "total raised $46M), so no $1B+ mark. S2A: graduated, the $16M Series A of May 2020 led by Index "
                  "with 'Previous investors Sequoia Capital, Kleiner Perkins and Frontline' (Silicon Republic)."))

# ---------------------------------------------------------------- freemarkets (T3)
L.append(verdict("freemarkets", "not_member",
                 "T3 and D4: the fund's shares were bought in the IPO itself. The December 1999 prospectus reserves "
                 "'up to 350,000 shares for Kleiner Perkins Caufield & Byers IX L.P., an entity affiliated with one "
                 "of our directors' at the offering price and names no Kleiner Perkins purchase of preferred stock; "
                 "John Doerr's own 350,000 shares came from director options granted 1999-10-28 (a person). The "
                 "2001 proxy's 283,323 and 8,759 shares for KPCB IX-A and IX-B are that allocation. No private "
                 "round by a fund is on record.",
                 ec="fund_filing", conf="medium", cite=FM_S1A))

# ---------------------------------------------------------------- geocast-network-systems
L.append(verdict("geocast-network-systems", "member",
                 "San Francisco Chronicle (SFGate), 1999-10-07: 'Geocast Network created a buzz in Silicon Valley "
                 "after it received funding in December 1998 from three major venture capital firms -- Kleiner "
                 "Perkins Caulfield & Byers, The Mayfield Fund and Institutional Venture Partners.' R1 corroborated "
                 "by press naming the firm in the round.",
                 ec="web", conf="high", cite=SFGATE_GEOCAST))
L.append(cls("geocast-network-systems", status="defunct", rng="below_1b", country="US", city="Menlo Park",
             stage="undetermined", entry_date="1998-12", focus="Media, Gaming & Advertising",
             rounds=[rnd("1998-12", "unnamed (first venture funding)", None, None, True, SFGATE_GEOCAST, "press"),
                     rnd("1999-10", "strategic investment (up to $10M)", 10000000, "Hearst-Argyle Television", None,
                         SFGATE_GEOCAST, "press")],
             note="Datacasting over digital TV spectrum to PCs, Menlo Park. The December 1998 funding from Kleiner "
                  "Perkins, Mayfield and IVP is not named and its size was not disclosed (SFGate), so the stage "
                  "stays undetermined. The company closed in 2001 by the judge's knowledge (no shutdown page read), "
                  "so defunct."))

# ---------------------------------------------------------------- go-corporation
L.append(verdict("go-corporation", "member",
                 "The firm's own Netscape case study: 'Mike Homer, with whom Kleiner Perkins had worked at GO Corp. "
                 "(a former KP portfolio company), was hired to head marketing.' The firm names GO as its portfolio "
                 "company in its own words (section 1), which also corroborates the bio line under R1.",
                 ec="web", conf="high", cite=KP_NETSCAPE))
L.append(cls("go-corporation", status="acquired", rng="below_1b", country="US", city="Foster City",
             stage="undetermined", rounds=[], focus="Industrial & Robotics",
             note="Pen computing pioneer (the PenPoint operating system), founded 1987, Foster City; its hardware "
                  "spin-out is the row eo-computer. Wikipedia: AT&T acquired GO in January 1994, having bought EO "
                  "in 1993, and then ended the line, so acquired. No source read names the round the firm entered."))

# ---------------------------------------------------------------- greenlight-com
L.append(verdict("greenlight-com", "member",
                 "CarsDirect's Fifth Amended and Restated Investor Rights Agreement of 2001-02-06 recites the "
                 "'Agreement of Merger and Plan of Reorganization ... among the Company, CD Merger Sub, Inc., "
                 "Greenlight.com, Inc. KPCB Holdings, Inc., Asbury-Everest Holdings L.L.C. and Joel Manby, as "
                 "securityholder agent', under which those purchasers receive Series E preferred: KPCB Holdings, "
                 "the funds' nominee, was a Greenlight.com securityholder. R5: Greenlight.com is the row; the "
                 "CarsDirect stock is sale consideration.",
                 ec="fund_filing", conf="high", cite=CARSDIRECT_IRA))
L.append(cls("greenlight-com", status="acquired", rng="below_1b", country="US", city="San Mateo",
             stage="undetermined", rounds=[], focus="Consumer & Marketplaces",
             note="Online car buying service launched in 2000 with Asbury Automotive, San Mateo. CarsDirect.com "
                  "merged it in under the agreement of 2001-02-06 (the filing), so acquired. The filing does not "
                  "give the round KPCB Holdings bought."))

# ---------------------------------------------------------------- himax-display
L.append(verdict("himax-display", "member",
                 "Himax Technologies' release of 2013-07-22 (6-K): 'Google will join the core group of HDI "
                 "shareholders including KPCB Holdings, Inc., Khosla Ventures I, L.P. and Intel Capital "
                 "Corporation.' KPCB Holdings, the funds' nominee, held Himax Display, the private subsidiary.",
                 ec="fund_filing", conf="high", cite=HIMAX_6K))
L.append(cls("himax-display", status="private", rng="below_1b", country="TW", country_src="web_verified",
             country_cite=W_HIMAX, city="Tainan", stage="undetermined", focus="Industrial & Robotics",
             rounds=[rnd("2013-07-22", "preferred shares sold to Google (6.3%)", None, "Google", None, HIMAX_6K,
                         "company")],
             note="LCOS microdisplay maker, the subsidiary Himax Technologies (Tainan) held at 81.5% in 2013; "
                  "status, band, country and city aligned with the Khosla Ventures row. KPCB Holdings was already a "
                  "core shareholder when Google invested; the round it bought is not in the release."))

# ---------------------------------------------------------------- hippo-holdings-inc (D2, Bond)
L.append(verdict("hippo-holdings-inc", "not_member",
                 "D2: the Form D match is Noah Knauf, a Bond partner from September 2018; the filings date from "
                 "July 2019, when Bond led Hippo's Series D, and Hippo's 2021 S-1 describes him as having 'co-led "
                 "Kleiner Perkins' Digital Growth Fund team, which became BOND in 2019'. The seat locates Bond; no "
                 "KPCB Digital Growth Fund or other Kleiner Perkins vehicle appears in the filings.",
                 ec="formd_adjudicated", conf="high", cite=HIPPO_S1))

# ---------------------------------------------------------------- homegrocer
L.append(verdict("homegrocer", "member",
                 "HomeGrocer.com's S-1 of 1999-12-17, related party transactions: 'Kleiner Perkins Caufield & Byers "
                 "(4)' holds 1,300,000 common, 200,000 Series A, 8,285,714 Series B, 484,732 Series C and 3,448,274 "
                 "Series D shares, footnote 4 naming 'Kleiner Perkins Caufield & Byers VIII, L.P., KPCB VIII "
                 "Founders Fund, L.P. and KPCB Information Sciences Zaibatsu Fund II, L.P.'; Douglas Mackenzie a "
                 "director since September 1998. R1 corroborated by the funds on the company's own filing.",
                 ec="fund_filing", conf="high", cite=HG_S1))
L.append(cls("homegrocer", status="acquired", rng="below_1b", city="Kirkland", stage="Series A",
             stage_src="web_verified", stage_cite=HG_S1, stage_conf="medium", entry_date="1998",
             focus="Consumer & Marketplaces",
             rounds=[rnd("1998-07", "Series A (sold February to July 1998 at $0.50)", 4000000, None, True, HG_S1,
                         "filing"),
                     rnd("1998-09", "Series B ($0.35)", 5900000, None, True, HG_S1, "filing"),
                     rnd("1999-05", "Series C ($1.75)", 52400000, "Amazon.com", True, HG_S1, "filing"),
                     rnd("1999-11", "Series D ($5.80)", 106800000, None, True, HG_S1, "filing")],
             note="Online grocer, Kirkland, Washington (the S-1's office). The funds hold Series A preferred (sold "
                  "February to July 1998) and about half of the September 1998 Series B, when their partner joined "
                  "the board, so the entry is 1998 and the earliest series held is the Series A; medium confidence "
                  "because the filing does not date the funds' own Series A purchase, and the Series B two months "
                  "later was their main cheque. Webvan acquired HomeGrocer in 2000."))

# ---------------------------------------------------------------- hybritech
L.append(verdict("hybritech", "member",
                 "Wikipedia, Ivor Royston: 'Financier Brook Byers, of Kleiner Perkins Caufield & Byers ... His firm "
                 "provided the $300,000 start-up funding' for Hybritech, founded 1978. Before EDGAR, one source "
                 "family.",
                 ec="web", conf="medium", cite=W_ROYSTON))
L.append(cls("hybritech", status="acquired", rng="below_1b", country="US", city="San Diego", stage="Seed",
             stage_src="model", stage_cite=W_ROYSTON, stage_conf="medium", entry_date="1978",
             focus="Healthcare & Bio",
             grad="graduated", grad_src="web_verified", grad_cite=W_ROYSTON, grad_conf="medium",
             rounds=[rnd("1978", "start-up funding", 300000, "Kleiner Perkins Caufield & Byers", True, W_ROYSTON,
                         "press"),
                     rnd("1981", "IPO", None, None, None, W_ROYSTON, "press")],
             note="Monoclonal antibody diagnostics, San Diego, founded 1978; acquired by Eli Lilly in 1986 for "
                  "$480M, aligned with the Sutter Hill row. The firm supplied the $300,000 of start-up money, read "
                  "as the seed (the article does not use the word). S2A: graduated; 'Hybritech went public in 1981' "
                  "(the same article), a later priced financing, its amount not given there."))

# ---------------------------------------------------------------- icarian
L.append(verdict("icarian", "member",
                 "Workstream's registration rights agreement for Icarian's former holders (10-K exhibit 4.8, 2002) "
                 "carries signature blocks for 'KPCB Java Fund', 'Kleiner Perkins Caufield & Byers VIII' and 'KPCB "
                 "VIII Founders Fund' among the investors: the funds held Icarian when Workstream bought it. R5: "
                 "Icarian is the row; the Workstream shares are sale consideration.",
                 ec="fund_filing", conf="high", cite=WSTM_RRA))
L.append(cls("icarian", status="acquired", rng="below_1b", country="US", city="Sunnyvale", stage="undetermined",
             rounds=[], focus="SaaS",
             note="Web-hosted recruiting software, Sunnyvale, California. Workstream announced the acquisition on "
                  "2002-05-23 (its release calls Icarian 'California-based'). The filings do not give the round "
                  "the Java Fund and KPCB VIII entered."))

# ---------------------------------------------------------------- imagic
L.append(verdict("imagic", "member",
                 "The firm's own AOL case study: 'Kleiner Perkins had invested in Imagic, a video game business "
                 "primed to go public until the market collapsed and the company failed.' Wikipedia's Imagic article "
                 "has the founders pitching Kleiner Perkins and Merrill Pickard for the first money.",
                 ec="web", conf="high", cite=KP_AOL))
L.append(cls("imagic", rng="below_1b", city="Los Gatos", stage="Seed", stage_src="web_verified",
             stage_cite=W_IMAGIC, stage_conf="medium", entry_date="1981", focus="Media, Gaming & Advertising",
             grad="graduated", grad_src="web_verified", grad_cite=W_IMAGIC, grad_conf="low",
             rounds=[rnd("1981", "seed capital", 2000000, None, True, W_IMAGIC, "press"),
                     rnd("1983", "stock sale after the failed IPO (date approximate)", 12000000, None, None,
                         W_IMAGIC, "press")],
             note="Video game publisher founded 1981 by Atari alumni, Los Gatos, California. Wikipedia: the "
                  "founders 'pitched venture capitalist Kleiner Perkins and Merrill Pickard, ultimately raising $2 "
                  "million in seed capital', so a Seed entry in 1981. S2A: graduated, low confidence; after the "
                  "IPO was pulled in December 1982 Imagic 'reportedly sold $12 million of its own company stock' "
                  "(the same article), an unnamed later round above twice the seed and above $5M."))

# ---------------------------------------------------------------- innercool-therapies
L.append(verdict("innercool-therapies", "member",
                 "Cardium's asset purchase agreement of March 2006 requires, among the lien releases at closing, "
                 "'the duly executed release by KPCB Holdings, Inc. in favor of Seller': the funds' nominee held a "
                 "secured claim on InnerCool's assets, a bridge financing by a fund. Joseph Lacob, a Kleiner "
                 "Perkins partner since 1987, was an INNERCOOL Therapies director (Corixa's 2003 proxy). R5: "
                 "InnerCool is the row; Cardium was ruled out as sale consideration.",
                 ec="fund_filing", conf="medium", cite=CARDIUM_APA))
L.append(cls("innercool-therapies", status="acquired", rng="below_1b", country="US", city="San Diego",
             stage="undetermined", rounds=[], focus="Healthcare & Bio",
             note="Endovascular temperature control systems, San Diego. Cardium Therapeutics bought substantially "
                  "all its assets in March 2006 for 2.5 million Cardium shares (Cardium's release), and Philips "
                  "bought the business from Cardium in 2009: acquired. The filings name KPCB Holdings as a secured "
                  "creditor and a partner on the board (Corixa's 2003 proxy) but no round."))

# ---------------------------------------------------------------- iscribe
L.append(verdict("iscribe", "member",
                 "The company's own paragraph in the joint release with Medix Resources (8-K exhibit, April 2001): "
                 "'Based in Redwood City, CA, iScribe is backed by six leading venture capital firms in healthcare "
                 "and e-commerce technology, Kleiner Perkins Caufield and Byers, Mayfield Fund, Skyline Ventures, "
                 "Galen Partners, Domain Associates and Gleacher Capital Partners.' A company source naming the "
                 "firm among its venture investors (R1).",
                 ec="web", conf="medium", cite=MEDIX_PR))
L.append(cls("iscribe", status="acquired", rng="below_1b", country="US", city="Redwood City", stage="undetermined",
             rounds=[], focus="Healthcare & Bio",
             note="Handheld electronic prescribing, Redwood City (its own release). AdvancePCS bought the business "
                  "later in 2001 by the judge's knowledge (no page read in this pass), so acquired. No source read "
                  "names the round the firm entered."))

# ---------------------------------------------------------------- jetti-resources
L.append(verdict("jetti-resources", "member",
                 "BetaKit, 2019-07-17: Jetti 'has raised more than $24 million CAD to date ... all of which was "
                 "from a Series A raised by US investors, in 2017. Disclosed investors in the startup include DNS "
                 "Capital, Kleiner Perkins, and Zoma Capital.'",
                 ec="web", conf="medium", cite=BETAKIT_JETTI))
L.append(cls("jetti-resources", status="private", rng="1b_plus", usd=2500000000, val_src="web_verified",
             val_cite=CBN_UNICORNS, asof="2022-10", val_conf="medium",
             extra={"valuation_range_source": "web_verified"}, flags=["stale"],
             country="US", city="Boulder", city_src="web_verified", stage="Series A", stage_src="web_verified",
             stage_cite=BETAKIT_JETTI, stage_conf="medium", entry_date="2017", focus="Industrial & Robotics",
             rounds=[rnd("2017", "Series A", 18700000, None, True, BETAKIT_JETTI, "press"),
                     rnd("2022-10", "Series D", 100000000, "T. Rowe Price", None, CBN_UNICORNS, "press")],
             note="Catalytic copper leaching technology, founded in Vancouver (BetaKit, 2019) and by 2022 'based in "
                  "Boulder, Colorado' (Crunchbase News). The firm is a disclosed investor in the 2017 Series A of "
                  "more than C$24M ($18.7M), the only round to 2019. Mark: the $100M Series D from T. Rowe Price "
                  "'that valued the company at $2.5 billion' (Crunchbase News unicorn board, 2022-11-09), older "
                  "than 24 months, so stale; no later priced round was found."))

# ---------------------------------------------------------------- keplar
L.append(verdict("keplar", "member",
                 "TechCrunch, 2025-09-17: 'the two-year-old company announced that it raised $3.4 million in seed "
                 "funding led by Kleiner Perkins, with participation from SV Angel, Common Metal, and South Park "
                 "Commons.'",
                 ec="web", conf="high", cite=TC_KEPLAR))
L.append(cls("keplar", status="private", rng="below_1b", country="US", city="San Francisco", stage="Seed",
             stage_src="web_verified", stage_cite=TC_KEPLAR, stage_conf="high", entry_date="2025-09-17",
             grad="censored", focus="AI & Applied AI",
             extra={"valuation_range_source": "web_verified", "valuation_citation": TC_KEPLAR,
                    "valuation_asof": ASOF},
             rounds=[rnd("2025-09-17", "Seed", 3400000, "Kleiner Perkins", True, TC_KEPLAR, "press")],
             note="Voice AI for market research interviews; San Francisco by the judge's knowledge (the article "
                  "gives no city). Kleiner Perkins led the $3.4M seed announced 2025-09-17; not yet on the firm's "
                  "live list. Momentum check 2026-09-30 (TechCrunch's own search): the seed report is the only "
                  "funding story, no $1B+ round. S2A: censored, the seed is inside the 24-month window."))

if __name__ == "__main__":
    jl.write("e1b", L)
