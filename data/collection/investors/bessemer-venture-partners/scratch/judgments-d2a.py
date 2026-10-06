import json

import judge_lib as jl
from judge_lib import cls, rnd, verdict, NEWS

L = []


def A(*a, **k):
    L.append(cls(*a, **k))


B1 = "below_1b"
U = "undetermined"
LR = "https://www.lightreading.com"
FIRST_LISTED = "Entry date is the first year the firm listed it ({y}), an upper bound and not an investment year; no round named."

# citations: read from disk, printed by a tool in this session, or SEC URLs built from accessions EDGAR printed
HIST = json.loads((jl.INV / "sources/site/history-narrative.json").read_text())["capture_url"]
HARM = NEWS("harmoni", "Harmoni Raises $10 Million Series A Led by Bessemer")
COLOR = NEWS("colorchip", "sale talks break down")
CRES_A = LR + "/cable-technology/crescent-closes-financing"
CRES_B = LR + "/business-management/crescent-raises-37m-more"
ELLA = LR + "/business-management/is-ellacoya-on-the-comeback-trail-"
LWM = LR + "/network-technology/-75m-goes-to-lightwave-microsystems"
ESS_S1 = "https://www.sec.gov/Archives/edgar/data/1084465/0000912057-00-017232.txt"
FURN_S1 = "https://www.sec.gov/Archives/edgar/data/1103648/0000912057-00-002618.txt"
MEVC = "https://www.sec.gov/Archives/edgar/data/1099941/000095011703000243/a34277.txt"
GMS_PROXY = "https://www.sec.gov/Archives/edgar/data/898807/0000893877-98-000337.txt"
GMS_8K = "https://www.sec.gov/Archives/edgar/data/898807/0000893877-97-000678.txt"

A("accordus", status="unknown", rng=B1, stage=U, entry_date="2002", country="US", city="San Francisco", city_src="formd_address",
  focus="SaaS", rounds=[],
  note="Agreement and workflow software for the health care products industry; its paper Form D of February 2003 gives a San Francisco address. "
       "No source read says what became of it after 2003, so the status is unknown. " + FIRST_LISTED.format(y=2002))

A("ardais", status="unknown", rng=B1, stage=U, entry_date="2002", country="US", city="Lexington", city_src="formd_address",
  focus="Healthcare & Bio", rounds=[],
  note="Supplier of human biological materials for drug research (fka Cellstore), Lexington, Massachusetts per its Form D filings of 2004. "
       "A later prospectus names its chief executive of 2002 to 2003, and no source read says whether it was sold or closed. " + FIRST_LISTED.format(y=2002))

A("beachfire", status="unknown", rng=B1, stage=U, entry_date="2002", country="US", focus="SaaS", flags=["city_unknown"], rounds=[],
  note="Online collaboration software (fka eSprocket). A 2005 proxy statement names its chief executive for 2000 to 2002; nothing later was found, "
       "so its fate and its city are not established. " + FIRST_LISTED.format(y=2002))

A("capitalthinking", status="unknown", rng=B1, stage=U, entry_date="2000", country="US", city="New York", city_src="formd_address",
  focus="Fintech & Payments", rounds=[],
  note="Software for commercial real estate finance, New York (its Form D filings run to June 2003). No source read says what became of it. "
       "Entry year is the firm's own (2000); no round named.")

A("circline", status="unknown", rng=B1, stage=U, entry_date="1999", country="US", focus="Consumer & Marketplaces", flags=["city_unknown"], rounds=[],
  note="Online broker of fine art and antiques. A retailer's proxy statement shows it still operating between November 2001 and December 2002; "
       "nothing later was found, and no source read places its head office. Entry year is the firm's own (1999); no round named.")

A("colorchip", status="private", rng=B1, stage=U, entry_date="2006", country="IL", country_src="web_verified", country_cite=COLOR,
  city="Yokneam", city_src="web_verified", focus="Industrial & Robotics",
  rounds=[rnd("2017-04", "Later round", None, None, None, COLOR, "press")],
  note="Optical components maker in Yokneam, Israel. Globes (2018-12-24) reports that talks to sell it to a Chinese buyer broke down and half the "
       "staff was laid off; it still announced products in 2019, so private is the last known state. " + FIRST_LISTED.format(y=2006))

A("crescent-networks", status="acquired", rng=B1, stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=CRES_A,
  entry_date="2000-01", country="US", city="Lowell", city_src="web_verified", focus="Data Infrastructure",
  rounds=[rnd("2000-01-31", "First round", 13000000, "Bessemer Venture Partners; St. Paul Venture Capital; Venrock Associates", True, CRES_A, "press"),
          rnd("2000-10-03", "Series B", 37000000, "JAFCO Ventures", True, CRES_B, "press")],
  note="Light Reading (2000-01-31): a first round of over $13M led by Bessemer, St. Paul and Venrock. The next round (2000-10-03, $37M) is named "
       "Series B and brings the total to just over $50M, so the first round is read as the Series A. The company went under in early 2003 and Marconi "
       "bought its intellectual property and assets that December (Light Reading 2004-08-31; Marconi's 10-K), so acquired with Marconi as successor.")

A("diogenes", status="acquired", rng=B1, stage=U, entry_date="2001", country="US", city="Denver", city_src="web_verified",
  focus="Data Infrastructure", rounds=[],
  note="TriZetto acquired all shares of Diogenes, Inc. on 2004-04-26 (its 10-Q), a privately held Denver company whose Internet transaction "
       "messaging software matches the firm's description; the firm's listing and Rob Stavis's board seat both end in 2004. A Form D of 2002 gives "
       "an earlier address in Iselin, New Jersey. Entry by 2001: a proxy of December 2001 already lists the Stavis seat; no round named.")

A("eality-com", status="defunct", rng=B1, stage=U, entry_date="1999", country="US", focus="SaaS", flags=["city_unknown"], rounds=[],
  note="Application service provider (eAlity, Inc., doing business as Vita Systems). A SuccessFactors filing records that its lender Comdisco "
       "foreclosed on its assets, which Success Acquisition Corporation then bought from the lender; read as defunct, the foreclosure date is not "
       "stated. Entry year is the firm's own (1999); no round named.")

A("ellacoya-networks", status="acquired", rng=B1, stage=U, entry_date="2002", country="US", city="Merrimack", city_src="formd_address",
  focus="Data Infrastructure",
  rounds=[rnd("2003-01-13", "Fourth round", 14000000, "Atlas Venture; Flagship Ventures", True, ELLA, "press")],
  note="Arbor Networks acquired Ellacoya in January 2008 (Wikipedia, Arbor Networks). Light Reading (2003-01-13) names Bessemer among the investors "
       "from the earlier rounds ($111M in three rounds) taking part in the $14M recapitalisation, but no source says which round it entered. "
       + FIRST_LISTED.format(y=2002))

A("essential-com", status="defunct", rng=B1, stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=ESS_S1,
  entry_date="1999-04", country="US", city="Burlington", city_src="web_verified", focus="Consumer & Marketplaces",
  rounds=[rnd("1999-03", "Series A", 2096410, None, True, ESS_S1, "filing"),
          rnd("1999-07", "Series B", 12094359, None, True, ESS_S1, "filing"),
          rnd("2000-02", "Series C", 75008747, None, True, ESS_S1, "filing")],
  note="The company's S-1 (2000-04-10): Bessemer Venture Partners IV and Bessec Ventures IV bought Series A preferred in the sale of March to June "
       "1999, and Rob Soni joined the board in April 1999. An investor's 10-Q for June 2001 says Essential.com has filed for bankruptcy; no sale "
       "was found, so defunct. Burlington, Massachusetts.")

A("exp-systems", status="defunct", rng=B1, stage=U, entry_date="1999", country="US", city="Menlo Park", city_src="web_verified", focus="SaaS",
  rounds=[rnd("2000-06-06", "Series C", None, None, None, MEVC, "filing")],
  note="EXP.com, later EXP Systems (Menlo Park). A fund that held it reports the disbursement of the company's assets to its preferred holders in "
       "fiscal 2002 and a last return of capital in 2003, so the company was wound down. Entry year is the firm's own (1999); the only round on "
       "record is the Series C of June 2000, after the firm's entry, so no round named.")

A("fempartners", status="unknown", rng=B1, stage=U, entry_date="2002", country="US", city="Houston", focus="Healthcare & Bio", rounds=[],
  note="Manager of obstetrics and gynecology practices (Houston, from memory). A director's biography in a 10-K of 2012 still calls it a privately "
       "held company; nothing later was found, so the status is unknown. " + FIRST_LISTED.format(y=2002))

A("framework-technologies", status="unknown", rng=B1, stage=U, entry_date="1996", country="US", city="Burlington", focus="SaaS", rounds=[],
  note="Project collaboration software (ActiveProject); Burlington, Massachusetts, from memory. No source read says what became of it after the "
       "firm's last listing in 2004. Entry year is the firm's own (1996); no round named.")

A("furniture-com", status="defunct", rng=B1, stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=FURN_S1,
  entry_date="1998-06-19", country="US", city="Framingham", city_src="web_verified", focus="Consumer & Marketplaces",
  rounds=[rnd("1998-06-19", "Series A", 3040000, None, True, FURN_S1, "filing"),
          rnd("1998-12-29", "Series B", 10000000, None, True, FURN_S1, "filing"),
          rnd("1999-06-25", "Series C", 35000000, None, True, FURN_S1, "filing")],
  note="The company's S-1 (2000-01-27): entities of Bessemer and Brand Equity Ventures bought the Class A common and Series A preferred on 19 and "
       "25 June 1998 (about $3.04M), and Bessemer bought every later series. The offering was withdrawn in June 2000 and another retailer's 10-QSB "
       "of May 2001 refers to the bankruptcy of furniture.com; no sale of the business was found, so defunct. Framingham, Massachusetts.")

L.append(verdict("gms-dental-group", "member",
                 "Gentle Dental Service Corporation's 1998 proxy statement lists Bessemer Venture Partners GMS (83 Walnut Street, Wellesley Hills, "
                 "the firm's office) as holder of 393,530 shares, 5.04%. The company's 8-K of 1997-11-19 (" + GMS_8K + ") records that on 1997-11-04 "
                 "the privately held GMS Dental Group was merged into it and its holders took about 4,548,200 shares, so the venture position was "
                 "GMS Dental Group; the acquirer is out as sale consideration (decisions.md R6).",
                 ec="web", conf="high", cite=GMS_PROXY))
A("gms-dental-group", status="acquired", rng=B1, stage=U, country="US", city="Yorba Linda", focus="Healthcare & Bio", rounds=[],
  note="Dental practice management company (22 offices in California, Idaho and Hawaii), merged into the listed Gentle Dental Service Corporation "
       "on 1997-11-04. Its preferred ran to Series A, B-1 and C; the filings read do not say which series Bessemer bought or when, so the stage and "
       "the entry date stay open. The city is where the combined company put its head office at the merger (Yorba Linda), read as GMS's own.")

L.append(verdict("harmoni", "member",
                 "The company's own release (PR Newswire, 2026-09-09): Harmoni has raised $10 million in Series A funding led by Bessemer Venture "
                 "Partners. The citybiz page named in the recall note refused the fetch; it carries the same release.",
                 ec="web", conf="high", cite=HARM))
A("harmoni", status="private", rng=B1, stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=HARM,
  entry_date="2026-09-09", country="US", city="Akron", city_src="web_verified", focus="AI & Applied AI",
  rounds=[rnd("2026-09-09", "Series A", 10000000, "Bessemer Venture Partners", True, HARM, "company")],
  note="The company's release (2026-09-09, Akron, Ohio): $10M Series A led by Bessemer; founded in 2023, and no earlier round or investor is named, "
       "so the Series A is read as the firm's entry. Momentum check 2026-10-06 (Google News): the $10M round is the only financing reported, "
       "no $1B+ mark.")

A("incert-software", status="unknown", rng=B1, stage=U, entry_date="2002", country="US", city="Cambridge", focus="DevTools & APIs", rounds=[],
  note="Tools that make software applications more available and supportable (Cambridge, Massachusetts, from memory). A director's biography gives "
       "its chief executive for 1997 to 2000; no source read says what became of it after the firm's last listing in 2003. "
       + FIRST_LISTED.format(y=2002))

L.append(verdict("interdata", "member",
                 "The firm's own history page (bvp.com/port/onepage.asp, captured 2008-11-20, read from sources/site/history-narrative.json): "
                 "Pete Bancroft joined Bessemer in 1967 to lead the venture practice; some of his signature deals were Measurex, Fotomat, and "
                 "Interdata. A deal of the venture group before the 1981 spin-out, stated on the firm's own site (decisions.md R2, X1).",
                 ec="web", conf="high", cite=HIST))
A("interdata", status="acquired", rng=B1, stage=U, country="US", city="Oceanport", city_src="web_verified", focus="Data Infrastructure",
  flags=["pre_spinout"], rounds=[],
  note="Minicomputer maker founded in 1966 in Oceanport, New Jersey; Perkin-Elmer bought it in 1973 for $63.6M (Wikipedia). The firm's history "
       "page names it among Pete Bancroft's deals after he joined in 1967, so the entry falls between 1967 and 1973; no source read gives the year "
       "or the round, and no entry date is written. Deal of the venture group before the 1981 spin-out (X1, R2).")

A("isr-global-telecom", status="unknown", rng=B1, stage=U, entry_date="1997", country="US", focus="Data Infrastructure",
  flags=["city_unknown"], rounds=[],
  note="Software for managing wide-area communications networks. A finance chief's biography shows it still a venture-backed company making its "
       "own acquisitions until February 2003; no source read says what became of it or where it was based. Entry year is the firm's own (1997); "
       "no round named.")

A("kelson-physician-partners", status="unknown", rng=B1, stage=U, entry_date="2002", country="US", city="Hartford", city_src="formd_address",
  focus="Healthcare & Bio", rounds=[],
  note="Pediatric practice management and services company, Hartford, Connecticut (its Form D of June 2005). Its chief executive left in March "
       "2005 and no source read says what became of it. " + FIRST_LISTED.format(y=2002))

A("lightwave-microsystems", status="acquired", rng=B1, stage=U, entry_date="2002", country="US", city="San Jose", city_src="web_verified",
  focus="Industrial & Robotics",
  rounds=[rnd("2000-10-31", "Later round", 75000000, "Meritech Capital Partners", None, LWM, "press")],
  note="Planar optical circuit maker (San Jose). It ceased operations on 2002-09-27 (Light Reading) and NeoPhotonics acquired the company in "
       "March 2003 (NeoPhotonics' prospectus), so acquired. The $75M round of October 2000 does not name Bessemer among its new or returning "
       "investors, and no source says when or in which round the firm invested. " + FIRST_LISTED.format(y=2002))

jl.write("d2a", L)
