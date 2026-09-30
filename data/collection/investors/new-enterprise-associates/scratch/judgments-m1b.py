"""PRO-100 NEA, judge m1, second half of queue/m1.json (38 rows): the Form D name-match clusters from Richard
Whitney's last row to Sara Nayeem. Run: NQ_TAG=m1 python3 judgments-m1b.py"""
import json

import judge_lib as jl

B = {r["slug"]: r for r in json.loads((jl.INV / "companies/base.json").read_text())}


def FD(slug, i=0):
    """The row's own Form D link (base.json formd_links)."""
    return [x.strip() for x in B[slug]["formd_links"].split(";") if x.strip()][i]


V, C = jl.verdict, jl.cls
rnd = jl.rnd
L = []
UNC = "no NEA listing, NEA vehicle filing or press source names an NEA fund in the company"

# ---------------------------------------------------------------- Richard Whitney (last row)
L += [V("sparkcharge-inc", "not_member", "Homonym: the Richard Whitney on SparkCharge's 2020 Form D is one of its own "
        "executive officers (Somerville, Massachusetts), an operator job, not NEA's venture advisor; " + UNC + ".",
        ec="formd_adjudicated", conf="high")]

# ---------------------------------------------------------------- Sheel Tyle (NEA 2013-17, then Amplo)
TP = "https://techpoint.africa/2015/06/25/andela-announces-series-a-funding-round"
L += [V("andela-inc", "not_member", "Tyle has sat on Andela's board since 2014, but the June 2015 Series A (led by "
        "Spark Capital with Omidyar Network and LearnCapital) and the seed backers the company named (Steve Case, "
        "Omidyar, Founder Collective, Rothenberg, LearnCapital, Melo7, Chris Hughes) do not include NEA, and the "
        "firm has never listed Andela; a personal seat (D2).", ec="formd_adjudicated", conf="medium", cite=TP),
      V("freightwalla-inc", "not_member", "Tyle's Freightwalla seat (2019) postdates his NEA years (to 2017; he then "
        "founded Amplo); " + UNC + ".", ec="formd_adjudicated", conf="high"),
      V("locale-hospitality-inc", "not_member", "Tyle's Locale seat (2020) postdates his NEA years (to 2017; he then "
        "founded Amplo); " + UNC + ".", ec="formd_adjudicated", conf="high")]

# ---------------------------------------------------------------- Sujay Jaswa (NEA principal 2008-10, then
# Dropbox, then WndrCo co-founder)
AUR = jl.FTS("Aura Consolidated", "DRS")
L += [V("aura-group-inc", "not_member", "Jaswa was at NEA from 2008 to 2010 (Aura's own 2026 registration statement "
        "says so); his 2023 Aura seat is WndrCo's, and " + UNC + ".",
        ec="formd_adjudicated", conf="high", cite=AUR),
      V("point-wild-holdings-inc", "not_member", "Jaswa's 2026 Point Wild (formerly Pango, Aura Group) seat sits "
        "beside Jeffrey Katzenberg of WndrCo, fifteen years after his NEA years (2008-10); " + UNC + ".",
        ec="formd_adjudicated", conf="high"),
      V("wndrco-llc", "not_member", "WndrCo, LLC is Jaswa's and Katzenberg's own holding and investment company "
        "(membership units, Beverly Hills, 2017), fund-shaped (D5) and formed seven years after Jaswa left NEA.",
        ec="formd_adjudicated", conf="high")]

# ---------------------------------------------------------------- Ching-Ho Fung (NEA venture partner 2008-10,
# venture advisor 2013; co-founder of Parature and TravelBank)
TB = jl.SITE("travelbank")
L += [V("interfolio-inc", "not_member", "Ching-Ho Fung (NEA venture partner, later advisor) is a director on "
        "Interfolio's $1M 2013 raise beside its founder; " + UNC + ", so the name match stands uncorroborated.",
        ec="formd_adjudicated", conf="medium"),
      V("parature-inc", "not_member", "Fung co-founded Parature with Duke Chung and sits as a founder-director; the "
        "outside directors on the 2010 Form D are Sierra Ventures' Vispi Daver and Accel's Rich Wong, and " + UNC
        + ".", ec="formd_adjudicated", conf="medium"),
      V("travelator-inc", "member", "Travelator, Inc. (80 South Park Street, San Francisco; CEO Duke Chung, founded "
        "2015) is TravelBank, which the firm lists with a 2015 first investment and Patrick Kerins on the deal team; "
        "Kerins sits on this 2017 Series A Form D beside co-founder Fung. Duplicate of travelbank.",
        ec="site_listing", conf="high", cite=TB),
      C("travelator-inc", status="acquired", rng="below_1b", city="San Francisco", focus="Fintech & Payments",
        flags=["identity_conflated"],
        note="Same company as the travelbank row (TravelBank's legal name). Acquired by U.S. Bancorp per the firm's "
             "exit line.")]

# ---------------------------------------------------------------- Colin Bryant (NEA operating partner 2014-20,
# partner 2021-23; the live team page lists him as Former)
COL = ("Colin Bryant's {x} seat postdates his NEA years (on the team pages to 2023, now listed as Former); " + UNC
       + ".")
L += [V("sierra-space-corp", "not_member", COL.format(x="March 2026 Sierra Space"), ec="formd_adjudicated",
        conf="medium"),
      V("sunday-app-inc-pbc", "not_member", COL.format(x="October 2025 Sunday"), ec="formd_adjudicated",
        conf="medium"),
      V("tendril-holdings-llc", "not_member", COL.format(x="March 2025 Tendril Holdings (Uplight)"),
        ec="formd_adjudicated", conf="medium")]

# ---------------------------------------------------------------- Patrick Chung (NEA general partner 2008-14)
PU = jl.SITE("pulse")
L += [V("alphonso-labs-inc", "member", "Alphonso Labs is Pulse (founders Akshay Kothari and Ankit Gupta, Palo "
        "Alto), which the firm lists with a 2011 first investment; Patrick Chung (NEA) joined the board on this "
        "June 2011 Series A. Duplicate of pulse.", ec="site_listing", conf="high", cite=PU),
      C("alphonso-labs-inc", status="acquired", rng="below_1b", city="Palo Alto", focus="Consumer & Marketplaces",
        flags=["identity_conflated"],
        note="Same company as the pulse row (Pulse's legal name). Acquired by LinkedIn (2013)."),
      V("sim-ops-studios-inc", "not_member", "Homonym: the Patrick Chung on Sim Ops Studios' 2009 Form D gives his "
        "address as SK Telecom Ventures, Menlo Park, not NEA; " + UNC + ".", ec="formd_adjudicated", conf="high")]

# ---------------------------------------------------------------- Chen Wang (no NEA roster person; ChenLi Wang
# was an NEA associate 2009-10)
L += [V("bactana-corp", "not_member", "Homonym: the Chen Wang on Bactana's Form D lives in Auckland, New Zealand; "
        "NEA's roster has no Chen Wang (ChenLi Wang was an associate in 2009-10), and " + UNC + ".",
        ec="formd_adjudicated", conf="high"),
      V("silego-technology-inc", "not_member", "Homonym: the Chen Wang on Silego's 2010 Form D is one of its own "
        "executive officers, an operator job; " + UNC + ".", ec="formd_adjudicated", conf="high")]

# ---------------------------------------------------------------- Jordan Shapiro (NEA analyst/associate 2018-19)
L += [V("chuma-holdings-inc", "not_member", "Homonym: the Jordan Shapiro on Chuma Holdings' 2014 Form D is its own "
        "executive officer (a Nevada cannabis company), four years before NEA's analyst joined; " + UNC + ".",
        ec="formd_adjudicated", conf="high"),
      V("metropolitan-energy-corp", "not_member", "Homonym: the Jordan Shapiro on Metropolitan Energy's 2018 Form D "
        "is its own chief executive (Vancouver); " + UNC + ".", ec="formd_adjudicated", conf="high")]

# ---------------------------------------------------------------- Rohini Chakravarthy (NEA partner 2008-14)
L += [V("editring-inc", "not_member", "Rohini Chakravarthy (NEA partner) is a director on EditRing's $1.2M 2010 "
        "raise beside its Stanford founders; " + UNC + " (Google News finds no coverage), so the name match stands "
        "uncorroborated.", ec="formd_adjudicated", conf="medium"),
      V("pervasive-inc", "not_member", "Chakravarthy is listed at her home address, beside Walden's Lip-Bu Tan, on "
        "Pervasive's 2010 Form D; " + UNC + ", so the name match stands uncorroborated.", ec="formd_adjudicated",
        conf="medium")]

# ---------------------------------------------------------------- Ali Behbahani (NEA general partner)
FL = FD("firstlight-bio-inc")
BPD = jl.NEWS("launchpad-therapeutics-inc", "Black Diamond spins out")
L += [V("firstlight-bio-inc", "member", "Behbahani, an in-tenure NEA general partner, is director of record on "
        "FirstLight Bio's April 2022 Form D with his address given as 'c/o New Enterprise Associates 18, L.P.': the "
        "seat is NEA 18's. FirstLight Bio is an operating New York biotech.", ec="formd_adjudicated",
        conf="medium", cite=FL),
      C("firstlight-bio-inc", status="private", rng="below_1b", city="New York", focus="Healthcare & Bio",
        note="Last known state is private after its $25.4M 2022 round; no exit or shutdown found (Google News, "
             "2026-09-30)."),
      V("launchpad-therapeutics-inc", "member", "BioPharma Dive (December 2022) reports Versant Ventures and New "
        "Enterprise Associates putting $30 million into Launchpad Therapeutics, Black Diamond's spinout; "
        "Behbahani (NEA) is its director of record.", ec="web", conf="high", cite=BPD),
      C("launchpad-therapeutics-inc", status="private", rng="below_1b", city="Cambridge", focus="Healthcare & Bio",
        stage="undetermined", entry_date="2022-12", flags=["stage_disputes_band"],
        rounds=[rnd("2022-12", "launch financing (unnamed)", 30000000, None, True, BPD, "press")],
        note="NEA's entry is the company's launch financing, which no source names; a launch round is not a "
             "Series B, so the band's Growth is disputed and the stage is undetermined.")]

# ---------------------------------------------------------------- Ryan Drant (NEA general partner to 2013)
L += [V("oceana-therapeutics-inc", "member", "Drant, an in-tenure NEA general partner, is director of record on "
        "Oceana Therapeutics' 2009 Form D 'c/o New Enterprise Associates' beside Quaker BioVentures and Domain "
        "Partners: the seat is NEA's. Oceana is an operating specialty pharma company.", ec="formd_adjudicated",
        conf="medium", cite=FD("oceana-therapeutics-inc")),
      C("oceana-therapeutics-inc", status="acquired", rng="below_1b", country="US", city="Edison",
        focus="Healthcare & Bio", note="Acquired by Salix Pharmaceuticals (2011)."),
      V("viacor-inc", "member", "Drant and Coy Blevins are directors of record on Viacor's 2009 Form D at 1119 St. "
        "Paul Street, Baltimore, NEA's office address: the seats are NEA's. Viacor is an operating mitral-valve "
        "device company in Wilmington, Massachusetts.", ec="formd_adjudicated", conf="medium",
        cite=FD("viacor-inc")),
      C("viacor-inc", status="unknown", rng="below_1b", city="Wilmington", focus="Healthcare & Bio",
        note="No later record of the company after its 2010 Form D (Google News, 2026-09-30); status unknown. The "
             "prefilled Series A band rests on the first electronic Form D of a company incorporated around 2000.")]

# ---------------------------------------------------------------- Liza Landsman (NEA 2018-23)
SQ = jl.FTS("Squarespace", "S-1")
L += [V("squarespace-inc", "not_member", "Squarespace's S-1 (2021) names NEA only in Landsman's biography (director "
        "since December 2018) and lists no NEA fund among its holders; an independent director's seat (D2).",
        ec="formd_adjudicated", conf="high", cite=SQ)]
WL = jl.SITE("the-well")
L += [V("wrii-corp", "member", "WRII Corp. (71 Fifth Avenue, New York; co-founders Kane Sarhan and Sarrah Hallock, "
        "CEO Rebecca Parekh) is THE WELL, which the firm lists with a 2020 first investment; Landsman (NEA) sits on "
        "this November 2020 round's board. Duplicate of the-well.", ec="site_listing", conf="high", cite=WL),
      C("wrii-corp", status="private", rng="below_1b", city="New York", focus="Consumer & Marketplaces",
        grad="graduated", grad_src="formd", flags=["identity_conflated"],
        note="Same company as the the-well row. The firm's first-invested year (2020) matches this Form D entry; "
             "the $20M round of August 2021 graduates it on the filings.")]

# ---------------------------------------------------------------- Sara Nayeem (NEA partner to 2020)
FB = jl.NEWS("vanqua-bio-inc", "Vanqua Bio snags")
L += [V("vanqua-bio-inc", "not_member", "Nayeem's August 2021 Vanqua seat comes after her last NEA listing (2020), "
        "and Fierce Biotech's report of that $85M Series B names Omega Funds as lead with founding investor OrbiMed, "
        "Surveyor, Avoro and Eli Lilly, not NEA; the firm has never listed Vanqua.", ec="formd_adjudicated",
        conf="medium", cite=FB)]

# ---------------------------------------------------------------- Frank Torti (NEA partner 2007-18)
ARB = jl.FTS("Arbutus", "DEF 14A")
L += [V("arbutus-biopharma-corp", "not_member", "Torti chairs Arbutus from November 2018 as Roivant's investment "
        "chair, after his NEA years (August 2007 to August 2018 per the proxy); Arbutus is a listed company with no "
        "NEA private round (X1).", ec="formd_adjudicated", conf="high", cite=ARB)]

# ---------------------------------------------------------------- Ron Bernal (NEA venture partner 2010-25)
DR = jl.SITE("drobo")
L += [V("data-robotics-inc", "member", "Data Robotics is Drobo (renamed 2010), which the firm lists with a 2008 "
        "first investment; membership rests on that listing, not on Bernal, who signs this 2009 Form D care of "
        "Sutter Hill Ventures. Duplicate of drobo.", ec="site_listing", conf="high", cite=DR),
      C("data-robotics-inc", status="defunct", rng="below_1b", country="US", city="San Jose",
        focus="Data Infrastructure", stage="undetermined", entry_date="2008", flags=["identity_conflated"],
        note="Same company as the drobo row. The firm's first-invested year is 2008 and no source names the round; "
             "status and city follow the Greylock and Sutter Hill rows.")]

# ---------------------------------------------------------------- Arjun Aggarwal (NEA associate 2017)
L += [V("evergreen-nephrology-llc", "not_member", "Aggarwal's 2022 Evergreen Nephrology seat, beside Rubicon "
        "Founders' Adam Boehler and Abe Sutton and Oak HC/FT's Annie Lamont, postdates his NEA associate year "
        "(2017); " + UNC + ".", ec="formd_adjudicated", conf="medium")]

# ---------------------------------------------------------------- Greg Papadopoulos (NEA venture partner)
TU = jl.SITE("turi")
WG = jl.W("GraphLab")
L += [V("graphlab-inc", "member", "GraphLab, Inc. is Turi (renamed Dato, then Turi), which the firm lists with a "
        "2013 first investment and Papadopoulos on its board; he signs this May 2013 Form D at NEA's Timonium "
        "address. Duplicate of turi.", ec="site_listing", conf="high", cite=TU),
      C("graphlab-inc", status="acquired", rng="below_1b", city="Seattle", focus="AI & Applied AI",
        stage="Series A", stage_src="web_verified", stage_cite=WG, stage_conf="high", entry_date="2013-05",
        flags=["identity_conflated", "stage_disputes_band"],
        rounds=[rnd("2013-05", "Series A", 6750000, None, True, WG, "press"),
                rnd(None, "Series B", 18500000, "Vulcan Capital", None, WG, "press")],
        note="Same company as the turi row. Wikipedia: the company 'raised a $6.75M Series A from Madrona Venture "
             "Group and New Enterprise Associates', so the band's Seed is disputed. Acquired by Apple (August 2016).")]
MJ = jl.SITE("mojo-vision")
L += [V("tectus-corp", "member", "Tectus Corp (Saratoga; co-founders Mike Wiemer and Drew Perkins, CEO Nikhil "
        "Balram) is Mojo Vision, which the firm lists with a 2016 first investment and Papadopoulos on its board. "
        "Duplicate of mojo-vision.", ec="site_listing", conf="high", cite=MJ),
      C("tectus-corp", status="private", rng="below_1b", city="Saratoga", focus="Industrial & Robotics",
        stage="undetermined", entry_date="2016", flags=["identity_conflated", "stage_disputes_band"],
        note="Same company as the mojo-vision row. The firm first invested in 2016, so this 2023 Form D is a "
             "follow-on, not the entry; the entry round is not named.")]

# ---------------------------------------------------------------- Amit Mukherjee (NEA partner 2017-20)
BR = jl.SITE("block-renovation")
L += [V("lyra-technologies-inc", "member", "Lyra Technologies (Brooklyn; founders Koda Wang and Tim Sherwin) is "
        "Block Renovation, which the firm lists with a 2018 first investment at Seed; Mukherjee (NEA partner) is its "
        "2019 director. Duplicate of block-renovation.", ec="site_listing", conf="high", cite=BR),
      C("lyra-technologies-inc", status="private", rng="below_1b", city="New York",
        focus="Consumer & Marketplaces", stage="Seed", stage_src="first_party", stage_cite=BR,
        stage_conf="medium", entry_date="2018", flags=["identity_conflated", "stage_disputes_band"],
        note="Same company as the block-renovation row. The firm's own label is Seed with a 2018 first investment, "
             "before this 2019 filing, so the band's Series A is disputed. Graduation left for the graduation pass.")]

# ---------------------------------------------------------------- Andrew Schoen (NEA partner)
SU = jl.SITE("super")
L += [V("nusantara-holdings-inc", "member", "Nusantara Holdings, Inc. (founder Steven Wongsoredjo, Indonesia) is "
        "Super, the Indonesian social commerce company the firm lists with a 2022 first investment and Schoen on "
        "its board. Duplicate of super.", ec="site_listing", conf="high", cite=SU),
      C("nusantara-holdings-inc", status="private", rng="below_1b", city="Surabaya",
        focus="Consumer & Marketplaces", flags=["identity_conflated"],
        note="Same company as the super row. Super was founded in Surabaya; the 2022 Form D gives a Tangerang "
             "Selatan office.")]

# ---------------------------------------------------------------- Yanev Suissa, Matt Sacks
L += [V("rescale-inc", "not_member", "Suissa was an NEA venture fellow in 2013; his 2018-20 Rescale seat postdates "
        "it, and " + UNC + ".", ec="formd_adjudicated", conf="medium"),
      V("sparkplug-applications-inc", "not_member", "Sacks was at NEA in 2017-18; his December 2022 SparkPlug seat, "
        "beside Jason Calacanis, postdates it, and " + UNC + ".", ec="formd_adjudicated", conf="medium")]

# ---------------------------------------------------------------- Jake Nunn and Ryan Drant
TV = jl.SITE("trivascular")
L += [V("tv2-holding-co", "member", "TV2 Holding Co (Santa Rosa; founder Michael Chobotov) is TriVascular, bought "
        "from Boston Scientific in March 2008 and renamed TriVascular Technologies in 2013; the firm lists it with a "
        "2008 first investment and NEA's Nunn and Drant sit on this board. Duplicate of trivascular.",
        ec="site_listing", conf="high", cite=TV),
      C("tv2-holding-co", rng="below_1b", city="Santa Rosa", focus="Healthcare & Bio", stage="undetermined",
        entry_date="2008", flags=["identity_conflated"],
        note="Same company as the trivascular row. NEA 12 and NEA Ventures 2008 held it from the March 2008 "
             "carve-out; the round is not named. Acquired by Endologix (2016).")]

jl.write("m1b", L)
