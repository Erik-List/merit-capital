"""Judge j12, batch 23 (PRO-99 Kleiner Perkins). homestore-com-inc is on the skip list (duplicate of move-com)."""
import judge_lib as jl
from judge_lib import verdict, cls, rnd

L = []
NM = "formd_adjudicated"


def nm(slug, basis, conf="high"):
    L.append(verdict(slug, "not_member", basis, ec=NM, conf=conf))


# ---------------------------------------------------------------- name matches ruled out
KNAUF = ("Noah Knauf became a Kleiner Perkins investing partner in 2016 (the firm's own people page) after Warburg "
         "Pincus, and from 2018-09 is a Bond partner (D2)")
nm("home-dialysis-plus-ltd",
   f"Name match only: {KNAUF}; his 2011 director seat predates his KP years and no Kleiner Perkins listing, vehicle "
   "filing or press names the firm in Home Dialysis Plus (Outset Medical, CIK 1484612). D5 seat dating.")
nm("jhp-group-holdings-inc",
   f"Name match only: {KNAUF}; the 2013 seat at JHP Group Holdings (JHP Pharmaceuticals, a Warburg Pincus holding) "
   "predates his KP years and nothing names a Kleiner Perkins fund. D5 seat dating.")
nm("outset-medical-inc",
   f"Name match only: {KNAUF}; the 2015 seat at Outset Medical (formerly Home Dialysis Plus, same CIK 1484612) "
   "predates his KP years and no Kleiner Perkins listing, vehicle filing or press names the firm. D5 seat dating.")
nm("human-longevity-inc",
   "Name match only: James Huang left KPCB China to found Panacea Venture in 2018; his 2024 director seat at Human "
   "Longevity locates Panacea, and no Kleiner Perkins listing, vehicle filing or press names the firm. D5 seat dating.")
nm("myrtelle-inc",
   "Name match only: James Huang ran Panacea Venture from 2018; his 2022 director seat at Myrtelle locates Panacea, "
   "and no Kleiner Perkins listing, vehicle filing or press names the firm. D5 seat dating.")
nm("hypori-inc-de",
   "Name match only: Ray Lane founded GreatPoint Ventures in 2015 after becoming a Kleiner Perkins partner emeritus; "
   "his 2021-2025 Hypori seats locate GreatPoint, and no Kleiner Perkins listing, vehicle filing or press names the "
   "firm. D5 seat dating.")
nm("kinetica-db-inc",
   "Name match only: Ray Lane's 2016-2020 Kinetica seats date from his GreatPoint Ventures years (founded 2015), and "
   "no Kleiner Perkins listing, vehicle filing or press names the firm in Kinetica. D5 seat dating.")
nm("integrated-plasmonics-corp",
   "Name match only: Mamoon Hamid joined Kleiner Perkins in 2017 (the firm's people page); his 2012 director seat at "
   "Integrated Plasmonics dates from his Social+Capital years, and nothing names a Kleiner Perkins fund. D5 seat dating.")
nm("infiniblaze-inc",
   "Name match only: Joel Serface appears on the firm's 2008-09 team page only; he is an executive officer of "
   "Infiniblaze in 2022 on a $25K raise, and nothing names a Kleiner Perkins fund.")
nm("inhometherapy-inc",
   "Homonym: the Matthew Murphy on this King of Prussia home-therapy company's Form D is an executive officer; the "
   "firm's Matt Murphy was an investor (at Menlo Ventures from 2018), and nothing names Kleiner Perkins.")
nm("nautilus-biotechnology-inc",
   "Homonym: the Matthew Murphy on Nautilus's 2021 Form D is an executive officer of the issuer, not the firm's "
   "former partner (at Menlo Ventures from 2018); no Kleiner Perkins listing or filing names the firm in Nautilus.")
nm("peiky-corp",
   "Homonym: a Toronto issuer raising $60K to $110K with a director named Matthew Murphy; nothing ties it to the "
   "firm's former partner or to a Kleiner Perkins fund.")
nm("olf-cayman-holdings-gp-llc",
   "Fund-shaped entity: a Cayman holdings GP LLC reporting $0 sold, with a Matthew Murphy as executive officer; a "
   "general partner vehicle is not an operating company (D6/T5) and nothing names a Kleiner Perkins fund.")
nm("icon-medical-corp",
   "Name match only: a Mark Allen sits on Icon Medical's 2012 Series C Form D (Atlanta); no Kleiner Perkins listing, "
   "vehicle filing or press names the firm in Icon Medical, so the match is uncorroborated.")
nm("lasq-llc",
   "Homonym: the Mark Allen on this Wichita LLC's $300K Form D is an executive officer of the issuer; nothing ties it "
   "to the firm's former operating partner or to a Kleiner Perkins fund.")
nm("kansas-natural-remedies-llc",
   "Homonym: a Wichita retailer's $50K raise with a director named David Wells; nothing ties it to the firm or to a "
   "Kleiner Perkins fund.")
nm("netflix-inc",
   "Homonym: David Wells on Netflix's 2011 Form D is Netflix's own chief financial officer (executive officer); the "
   "company was public from 2002 and no Kleiner Perkins fund held it (T3).")
nm("omniboros-inc",
   "Homonym: the David Wells on this Washington DC issuer's Form D is its executive officer; nothing names a Kleiner "
   "Perkins fund.")
nm("owlet-baby-care-inc",
   "Homonym: the Mike Abbott on Owlet's 2018-2019 Form D filings is an executive officer of Owlet in Lehi, Utah, not "
   "the firm's former partner; no Kleiner Perkins listing or filing names the firm in Owlet.")
nm("lifemine-therapeutics-inc",
   "Homonym: Weiqing Zhou is an executive officer of LifeMine on its Form D filings, not the firm's KPCB China "
   "partner; no Kleiner Perkins listing or filing names the firm in LifeMine (GV's book holds it as its own).")
nm("master-silicon-carbide-industries-inc",
   "Homonym: the director is James Tie Li of East Brunswick, New Jersey, on a Lakeville CT issuer financed by Vision "
   "Opportunity; nothing ties him to the firm or names a Kleiner Perkins fund.")
nm("latigo-biotherapeutics-inc",
   "Name match only: Beth Seidenberg's 2025 Latigo seat locates Westlake Village BioPartners (from 2018, D5); the "
   "S-1 names Kleiner Perkins only in her biography (R1), not as a holder, and the firm does not list Latigo.")
nm("luminar-technologies-inc",
   "Name match only: Ben Kortlang was a G2VP partner from 2016 (Luminar S-1 biography); his 2019-2020 Luminar seats "
   "locate G2VP, the S-1 names no Kleiner Perkins fund as holder (R1), and the firm does not list Luminar.")
nm("noho-health-inc",
   "Name match only: Chi-Hua Chien left for Goodwater Capital in 2014 (D5); his 2017-2020 NoHo Health seats locate "
   "Goodwater, and nothing names a Kleiner Perkins fund.")
nm("owl-cameras-inc",
   "Name match only: Trae Vassallo ran Defy from 2015 (D5); her 2018 Owl Cameras seat locates Defy, and nothing names "
   "a Kleiner Perkins fund (Khosla's book holds Owl as its own).")
nm("jiff-inc",
   "Name match only: Lawrence (Larry) Leisure co-founded Jiff with James Currier and Stan Chudnovsky; its 2014 Series "
   "B was led by Venrock with Aberdare (Business Wire, 2014-09-23), and no source names a Kleiner Perkins fund.")
nm("lumiata-inc",
   "Name match only: Larry Leisure's 2014-2016 director seat at Lumiata is uncorroborated; no Kleiner Perkins "
   "listing, vehicle filing or press names the firm in Lumiata (Khosla's book holds it as its own).")
nm("lifeqode-inc",
   "Name match only: Larry Leisure is a director on LifeQode's two $250K 2015 filings; no Kleiner Perkins listing, "
   "vehicle filing or press names the firm.")
nm("octave-bioscience-inc",
   "Name match only: Brook Byers chairs Octave and its seed filing gives the KPCB office as a c/o address, but the "
   "rounds name Byers Capital (his family office, R4), BCBS Venture Partners, Section 32 and others, never a Kleiner "
   "Perkins fund, and the firm does not list Octave.", conf="medium")
nm("optimus-outcome-inc",
   "Name match only: Amol Deshpande is a director on a $135K 2016 raise by Optimus Outcome (renamed Opya, same CIK "
   "1670012), after he left to run Farmers Business Network; nothing names a Kleiner Perkins fund (D3 personal).")
nm("opya-inc",
   "Name match only: Opya is Optimus Outcome renamed (CIK 1670012); Amol Deshpande's 2021 director seat is outside "
   "his Kleiner Perkins years and nothing names a Kleiner Perkins fund (D3 personal).")
nm("palo-alto-health-sciences-inc",
   "Personal and family money: Russell and Elizabeth Siegelman both sit on Palo Alto Health Sciences' Form D filings "
   "from 2013; no Kleiner Perkins listing, vehicle filing or press names a firm fund (D3, R4).")

# ---------------------------------------------------------------- Atara's program company (member)
ATARA = jl.FTS("Atara", "DRS")
L.append(verdict("nina-biotherapeutics-inc", "member",
                 "Atara Biotherapeutics' 2014 registration statement: Nina Biotherapeutics was one of three program "
                 "companies incorporated August 2012 whose Series A was bought by entities affiliated with Kleiner "
                 "Perkins Caufield & Byers ($5M), named as promoters; its stockholders were recapitalized into Atara "
                 "on 2014-03-31. Same investment as atara-biotherapeutics.",
                 ec="fund_filing", conf="high", cite=ATARA))
L.append(cls("nina-biotherapeutics-inc", status="acquired", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=ATARA, stage_conf="high",
             entry_date="2012-10", city="Brisbane", city_src="formd_address", focus="Healthcare & Bio",
             flags=["stage_disputes_band"],
             rounds=[rnd("2012-10", "Series A (Oct 2012 to Mar 2013, $20.1M across Nina, Pinta and Santa Maria)",
                         20087750, None, True, ATARA, "filing")],
             note="One of Atara's three program companies (Nina, Pinta, Santa Maria); KPCB entities bought $5M of the "
                  "Series A sold October 2012 to March 2013, and the stockholders were recapitalized into Atara on "
                  "2014-03-31, so the company reads acquired (merged into Atara). The 2013-11 Form D the band read "
                  "as a Seed is a later close. Should merge into atara-biotherapeutics."))

# ---------------------------------------------------------------- duplicates of listed companies (members)
L.append(verdict("mechio-inc", "member",
                 "Mechio Inc. is Motiv (CIK 1601149; founders Michael and Eric Strasser and Curt von Badinski), which "
                 "the firm listed 2017-2026; Randy Komisar and Wen Hsieh sit as directors on its 2015 Series A Form D. "
                 "Duplicate of base row motiv.", ec="site_listing", conf="high", cite=jl.ARCH("motiv")))
L.append(cls("mechio-inc", status="private", rng="below_1b",
             stage="Series A", stage_src="model", stage_conf="medium", entry_date="2015-09-01",
             city="San Francisco", city_src="formd_address", focus="Consumer & Marketplaces",
             rounds=[rnd("2014-03", "unnamed ($1.5M, Form D)", 1500000, None, False, None, "filing"),
                     rnd("2014-12", "unnamed ($2M, Form D)", 2000000, None, False, None, "filing"),
                     rnd("2015-09-01", "Series A Convertible Preferred ($8.7M sold of $9.3M)", 8665698, None, True,
                         "https://www.sec.gov/Archives/edgar/data/1601149/000160114915000002/0001601149-15-000002-index.htm",
                         "filing")],
             note="Motiv (smart ring). The 2015 Form D names the Series A Convertible Preferred and seats Randy Komisar "
                  "and Wen Hsieh; the two earlier filings carry no firm partner, so the entry reads Series A "
                  "(model, medium). The company's site (checked 2026-09-30) says it no longer sells direct and lists "
                  "retailers as of 2021; no sale or shutdown found. Duplicate of motiv."))

MH_VAL = "https://www.globenewswire.com/news-release/2021/02/11/2174026/0/en/Modern-Health-Gains-Unicorn-Status-After-74-Million-Series-D-at-1-17-Billion-Valuation.html"
MH_POST = jl.POST("welcome-modern-health")
for slug, prior_name in (("modern-healthcare-inc", "Modern Healthcare Inc."), ("modern-life-inc", "Modern Life Inc.")):
    L.append(verdict(slug, "member",
                     f"{prior_name} (CIK 1744840) is Modern Health, which the firm lists (invested 2019) and whose "
                     "Series A it led ('Welcome Modern Health', 2019-05-23); Mamoon Hamid is the director on the "
                     "round's Form D. Duplicate of base row modern-health.",
                     ec="site_listing", conf="high", cite=jl.SITE("modern-health")))
common = dict(status="private", rng="1b_plus", usd=1170000000, val_src="web_verified", val_cite=MH_VAL,
              asof="2021-02-11", city="San Francisco", city_src="model_knowledge",
              extra={"valuation_range_source": "web_verified"})
L.append(cls("modern-healthcare-inc", flags=["stale"], focus="Healthcare & Bio", **common,
             note="Modern Health: $74M Series D at $1.17B led by Founders Fund (GlobeNewswire, 2021-02-11); no later "
                  "priced round found, so the mark is stale. Aligned with battery-ventures and felicis. Duplicate of "
                  "modern-health (and of modern-life-inc, the same CIK)."))
L.append(cls("modern-life-inc", flags=["stale"], **common,
             stage="Series A", stage_src="first_party", stage_cite=MH_POST, stage_conf="high",
             entry_date="2019-02-04", focus="Healthcare & Bio",
             rounds=[rnd("2018-09", "unnamed ($2.5M, Form D; seed)", 2500000, None, False, None, "filing"),
                     rnd("2019-02-04", "Series A", 11673567, "Kleiner Perkins", True, MH_POST, "firm"),
                     rnd("2021-02-11", "Series D", 74000000, "Founders Fund", None, MH_VAL, "company")],
             note="Modern Health: the firm's post says it led the Series A, and its Form D (first sale 2019-02-04, "
                  "Mamoon Hamid director) dates it; $1.17B Series D (GlobeNewswire, 2021-02-11) is the last priced "
                  "mark, stale. Duplicate of modern-health; the thrive-capital 'Modern Life' is a different company "
                  "(New York insurance brokerage)."))

L.append(verdict("moffett-data-inc", "member",
                 "Moffett Data, Inc. is Ripcord (Hayward; CEO Alex Fielding), which the firm listed 2017-2026; Michael "
                 "Abbott is named 'Series A Director' on its 2016 Form D. Duplicate of base row ripcord.",
                 ec="site_listing", conf="high", cite=jl.ARCH("ripcord")))
RIP_FD = "https://www.sec.gov/Archives/edgar/data/1639508/000163950816000003/0001639508-16-000003-index.htm"
L.append(cls("moffett-data-inc", status="private", rng="below_1b",
             stage="Series A", stage_src="model", stage_conf="medium", entry_date="2016-05-16",
             city="Hayward", city_src="formd_address", focus="Industrial & Robotics",
             flags=["stage_disputes_band"],
             rounds=[rnd("2016-05-16", "Series A (first close, $7.0M; Mike Abbott named Series A director)", 6982025,
                         None, True, RIP_FD, "filing"),
                     rnd("2017-08", "Series B ($40M)", 40000000, None, None, None, "press"),
                     rnd("2017-12-20", "Series B extension (led by Google Ventures)", 25000000, "Google Ventures", None,
                         None, "press")],
             note="Ripcord (robotic document digitisation). Its only Form D names the firm's Mike Abbott as the "
                  "'Series A Director', so the entry reads Series A, not the band's Seed (model, medium). Still "
                  "operating per gv's row (2023 round, 2026 facility). Duplicate of ripcord."))

LOOM_POST = jl.POST("loom-putting-video-messages-to-work")
L.append(verdict("opentest-inc", "member",
                 "Opentest, Inc. is Loom (CIK 1761257, the same issuer as Loom's later Form D filings), which the firm "
                 "lists (invested 2018) and whose Series A it led; Ilya Fushman is the director on this 2018 Form D. "
                 "Duplicate of base row loom.", ec="site_listing", conf="high", cite=jl.SITE("loom")))
L.append(cls("opentest-inc", status="acquired", rng="below_1b",
             stage="Series A", stage_src="first_party", stage_cite=LOOM_POST, stage_conf="high",
             entry_date="2018-11-27", city="San Francisco", city_src="model_knowledge", focus="SaaS",
             rounds=[rnd("2018-11-27", "Series A (about $11M, announced February 2019)", 10700499, "Kleiner Perkins",
                         True, LOOM_POST, "firm")],
             note="Loom: the firm's post says it led Loom's Series A; the round's Form D gives first sale 2018-11-27. "
                  "Acquired by Atlassian (announced 2023-10-12, $975M). Aligned with the sibling books (acquired, San "
                  "Francisco, SaaS). Duplicate of loom."))

# ---------------------------------------------------------------- vehicle-filing members: classification only
IND = "https://www.sec.gov/Archives/edgar/data/1002536/0000927016-96-000615.txt"
L.append(cls("individual-inc", status="acquired", rng="below_1b", stage="undetermined",
             country="US", city="Burlington", focus="Media, Gaming & Advertising", rounds=[],
             note="Individual, Inc. (personalised business news). Its 1996 S-1 lists KPCB VI and its founders fund as "
                  "an 8.9% holder of common stock but names no series or date for the entry, so the stage is "
                  "undetermined. Merged with Desktop Data in 1998 to form NewsEdge (acquired)."))
L.append(cls("keravision-inc-ca", status="acquired", rng="below_1b", stage="undetermined",
             country="US", city="Fremont", focus="Healthcare & Bio", rounds=[],
             note="KeraVision (Intacs corneal implants), IPO 1995. The firm's 13G of 1997 shows the holding; no "
                  "EDGAR filing names the round it entered (the IPO predates electronic filing), so the stage is "
                  "undetermined. Filed for bankruptcy in 2001 and its Intacs business was sold to Addition "
                  "Technology (acquired, out of insolvency)."))
MSLO = jl.FTS("MARTHA STEWART", "10-K405")
L.append(cls("martha-stewart-living-omnimedia-inc", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=MSLO, stage_conf="high", entry_date="1999-07",
             country="US", city="New York", focus="Media, Gaming & Advertising",
             rounds=[rnd("1999-07", "private sale of a 5% equity interest in MSLO LLC with a warrant", None,
                         "Kleiner Perkins Caufield & Byers", True, MSLO, "filing")],
             note="The 2000 10-K: in July 1999 MSLO sold a five percent equity interest in MSLO LLC, with a warrant, "
                  "to an affiliate of KPCB, three months before the October 1999 IPO; a pre-IPO purchase in an "
                  "established company reads Growth. Acquired by Sequential Brands in 2015."))
NXT = "https://www.sec.gov/Archives/edgar/data/1081015/0000950149-99-000951.txt"
L.append(cls("nextcard-inc", status="defunct", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=NXT, stage_conf="high", entry_date="1998-11",
             country="US", city="San Francisco", focus="Fintech & Payments",
             rounds=[rnd("1996-12", "Series A ($0.44/share, Dec 1996 to Mar 1997)", None, None, False, NXT, "filing"),
                     rnd("1997-08", "Series B-1/B-2 ($0.56/share)", None, None, False, NXT, "filing"),
                     rnd("1998-05", "Series C-1/C-2 ($1.29/share)", None, None, False, NXT, "filing"),
                     rnd("1998-11", "Series D-1/D-2 ($2.67/share)", None, None, True, NXT, "filing")],
             note="NextCard's May 1999 IPO prospectus: Kleiner Perkins Caufield & Byers VIII bought 3,000,002 shares "
                  "of the Series D-1/D-2 preferred (November 1998) and none of the earlier series, so the entry reads "
                  "Growth. The bank was closed by regulators in 2002 and the company went into Chapter 11 and "
                  "liquidated (defunct)."))
ONS = "https://www.sec.gov/Archives/edgar/data/1026506/0000898430-97-001588.txt"
L.append(cls("onsale-inc", status="acquired", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=ONS, stage_conf="high", entry_date="1996-09",
             country="US", city="Menlo Park", focus="Consumer & Marketplaces",
             rounds=[rnd("1996-09", "Series A Preferred ($6.39/share, with Series B warrants)", None,
                         "Kleiner Perkins Caufield & Byers", True, ONS, "filing")],
             note="Onsale's April 1997 IPO prospectus: in September 1996 KPCB VIII and KPCB Information Sciences "
                  "Zaibatsu Fund II bought the Series A Preferred. Onsale merged with Egghead.com in 1999 (renamed "
                  "Egghead.com); that company went into Chapter 11 in 2001 and its name and assets were sold "
                  "(acquired, out of insolvency)."))
OYS = jl.FTS("Oyster Point", "3")
L.append(cls("oyster-point-pharma-inc", rng="below_1b", stage="undetermined",
             country="US", city="Princeton", focus="Healthcare & Bio",
             rounds=[rnd(None, "Series A Convertible Preferred (45,529 shares held at the 2019 IPO)", None, None, True,
                         OYS, "filing")],
             note="The KPCB XIV Form 3 at the October 2019 IPO shows 322,458 common shares and 45,529 Series A "
                  "preferred; the S-1 names no Kleiner Perkins fund and nothing dates or explains the larger common "
                  "holding, so the entry round is undetermined. Acquired by Viatris (January 2023)."))

jl.write("j12a", L)
