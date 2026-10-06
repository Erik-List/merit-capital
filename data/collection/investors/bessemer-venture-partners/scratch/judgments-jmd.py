"""PRO-80 Bessemer, judge jm, file d: more alumni seats outside the window, homonyms and single-row clusters
(batches 21 to 25). All not_member: none of these issuers is on the firm's own list (live or archived) or its
deal-partner map, and no source ties a Bessemer fund to any of them.
"""
import judge_lib as jl

NM = "not_member"
EC = "formd_adjudicated"
lines = []
TAIL = " The issuer is not on the firm's own list or deal-partner map and no Bessemer fund appears in its rounds."


def nm(slug, basis, conf="high", cite=None):
    lines.append(jl.verdict(slug, NM, basis + TAIL, ec=EC, conf=conf, cite=cite))


# ---- Philippe Botteri: team pages 2008 to 2010; Accel from 2011
PB = ("Seat outside the person's Bessemer window (decisions.md D6): Philippe Botteri is last on the firm's team page in "
      "2010 and joined Accel in 2011; this is an Accel seat (the Accel book carries the company). ")
nm("algolia-inc", PB + "His Algolia seat runs from the 2015 filing to 2021.")
nm("uipath-inc", PB + "His UiPath seat is on the 2020 and 2021 filings.")
nm("snyk-ltd", PB + "His Snyk seat is on the 2020 to 2022 filings.")
nm("chainalysis-inc", PB + "His Chainalysis seat is on the 2021 filings, which also name Sarah Tavel, last on the firm's "
   "team page in 2012 and at Benchmark by then.")

# ---- Sunil Nagaraj: team pages 2012 to 2017; founder before, Ubiquity Ventures after
nm("triangulate-inc", "The 2010 filing names Sunil Nagaraj as an executive officer of Triangulate, the company he founded "
   "before joining Bessemer (team pages 2012 to 2017): an operator job outside his window (decisions.md D6).")
SN = ("Seat outside the person's Bessemer window (decisions.md D6): Sunil Nagaraj is last on the firm's team page in 2017 "
      "and founded Ubiquity Ventures that year. ")
nm("parallel-domain-inc", SN + "The Parallel Domain filing is from 2018, a Ubiquity seat.")
nm("jargon-inc", SN + "The Jargon filing is from 2019, a Ubiquity seat.")

# ---- Trevor Oelschig: team pages 2009 to 2016 (site alumni 2016); then General Catalyst
TO = ("Seat outside the person's Bessemer window (decisions.md D6): Trevor Oelschig left Bessemer in 2016 (the site marks "
      "him an alumnus) for General Catalyst. ")
nm("isubscribed-inc", TO + "The iSubscribed filing is from 2018.")
nm("singular-labs-inc", TO + "The Singular Labs filing is from 2018 (the General Catalyst book carries the company).")
nm("wc-sacd-holdings-inc", TO + "The WC SACD Holdings filings are from 2019 and 2020, and the issuer is a holding company.")

# ---- Vishal Gupta: partner in the India office; a common name
VG = ("Form D name match only, a homonym (decisions.md D6 names Vishal Gupta as a common roster name): Bessemer's Vishal "
      "Gupta is a partner in the India office; the filing names an executive officer of the issuer, another person. ")
nm("california-gold-mining-inc", VG + "California Gold Mining is a Canadian junior miner (filings 2017 to 2020).")
nm("anchor-balloon-inc", VG + "Anchor Balloon files in 2020 and 2024 for rounds of about $1.5M.")
nm("metalite-resources-inc", VG + "Metalite Resources is a Canadian junior miner (filing 2023).")

# ---- Aviad Ariel: senior associate in the Israel office (team page 2012, joined 2011)
AA = ("Seat outside the person's Bessemer window (decisions.md D6): Aviad Ariel was a senior associate in the Herzliya "
      "office on the 2012 team page only and later invested from another firm. ")
nm("ownbackup-ltd", AA + "His OwnBackup seat is on the 2018 to 2021 filings.")
nm("unity-scm-inc", AA + "The Unity SCM filing is from 2023.")

# ---- Chris Gabrieli: Partner Emeritus (team pages to 2019), a life-sciences investor at the firm
CG = ("Form D name match with no corroboration: Chris Gabrieli is a Partner Emeritus whose Bessemer deals, the education "
      "ones included (Advantage Schools, Flat World Knowledge), are on the firm's own list and deal-partner map; this "
      "issuer is on neither, which reads as a seat of his own (decisions.md D4). ")
nm("acelero-inc", CG + "Acelero is a New York early-education operator (2009 filing, $1M).", conf="medium")
nm("ellevation-inc", CG + "Ellevation is a Boston education-software company (2018 and 2020 filings).", conf="medium")

# ---- "Lin Li": not a person on the firm's roster as read (the roster has Lindsey Li and Li Sun)
LL = ("Form D name match only: no 'Lin Li' is on the firm's roster of team pages (the nearest names are Lindsey Li and "
      "Li Sun), so the match is a homonym at best. ")
nm("acea-therapeutics-inc", LL + "The filings name a director of a San Diego drug developer (2018 to 2019).")
nm("northann-corp", LL + "The 2023 filing names the issuer's own chief executive.")

# ---- single-row clusters
nm("euronet-worldwide-inc", "Form D name match only, a homonym: Bessemer's Andrew Schmitt is an investor on the team pages "
   "of 2021 to 2024; the Euronet director on the 2014 and 2015 filings is a long-serving independent director of the "
   "listed company, another person.")
nm("educerus-health-llc", "Form D name match only, a homonym (the brief's list): Bessemer's Andrew Walsh joined in 2013; "
   "the 2011 filing names an executive officer of the issuer, another person.")
nm("virtuous-software-inc", "Seat outside the person's Bessemer window (decisions.md D6): Aneesha Raghunathan is on the "
   "firm's team pages for 2015 to 2017 only; the Virtuous filing is from 2024, a later firm's seat.")
nm("hatsu-labs-inc", "Brandon Saw is on the firm's team page in 2017 only; the 2024 filing names him as an executive "
   "officer of Hatsu Labs, his own company, an operator job (decisions.md D4, D6).")
nm("aviation-spectrum-resources-holdings-inc", "Form D name match only, a homonym: the filing names a 'Darshan Patel' as "
   "director of an aviation-industry holding company raising $350 in 2022, not Bessemer's investor Darsh Patel.")
nm("opsclarity-inc", "Form D name match only, a homonym: Bessemer's Dhruv Jain joined in 2016; the 2014 filing names "
   "OpsClarity's own co-founder as an executive officer.")
nm("equity-international-services-llc", "Form D name match only, a homonym: Bessemer's Eric Kaplan is on the team pages "
   "from 2022; the 2014 filing names an executive officer of the issuer, another person.")
nm("ask-parable-inc", "Seat outside the person's Bessemer window (decisions.md D6): Hansae Catlett is last on the firm's "
   "team page in 2023; the Parable filing is from August 2025, a later firm's seat.")
nm("infield-inc", "Seat outside the person's Bessemer window (decisions.md D6): Lauri Moore joined Bessemer in 2024, and "
   "the firm's own announcement lists Infield among her Foundation Capital investments; the filing is from 2023.",
   cite=jl.POST("welcomes-lauri-moore"))
nm("stellaservice-inc", "Seat outside the person's Bessemer window (decisions.md D6): Lisa Wu is on the firm's team pages "
   "for 2008 to 2010 only; the StellaService filing is from 2019, a later firm's seat.")
nm("cedar-build-inc", "Seat outside the person's Bessemer window (decisions.md D6): Mary D'Onofrio left in 2025 (the site "
   "marks her an alumna); the Cedar Build filing is from March 2026, a later firm's seat.")
nm("generate-capital-pbc", "Matan Friedman is on the firm's team pages for 2008 to 2010 only; the 2017 to 2021 filings name "
   "him as an executive officer of Generate Capital, his own company, an operator job (decisions.md D4, D6).")
nm("layer2-financial-holdings-inc", "Seat outside the person's Bessemer window (decisions.md D6): Mike Giampapa is last on "
   "the firm's team page in 2022; the Layer2 Financial filing is from 2024, a later firm's seat.")
nm("parcel-biosciences-inc", "Seat outside the person's Bessemer window (decisions.md D6): Morgan Cheatham left in 2024 "
   "(the site marks him an alumnus); the Parcel Biosciences filing is from 2026, a later firm's seat.")
nm("law-pivot-inc", "Form D name match only, a homonym (the brief's list): Bessemer's Nitin Gupta joined in 2016; the 2010 "
   "and 2011 filings name LawPivot's own co-founder as an executive officer.")
nm("lifeguides-inc", "Phil Strazzulla is on the firm's team page in 2012 only; the 2015 filing names him as an executive "
   "officer of LifeGuides, his own company, an operator job (decisions.md D4, D6).")
nm("swoop-com-inc", "Ron Elwell was an operating partner on the firm's team lists of 2003 to 2010; the 2012 to 2020 filings "
   "name him as an executive officer of Swoop, the company he ran afterwards, an operator job (decisions.md D4, D6).")
nm("onecrew-software-inc", "Seat outside the person's Bessemer window (decisions.md D6): Sakib Dadi left in 2023 (the site "
   "marks him an alumnus); the OneCrew filing is from 2025, a later firm's seat.")
nm("airgarage-inc", "Seat outside the person's Bessemer window (decisions.md D6): Trevor Neff left in 2019 (the site marks "
   "him an alumnus); the AirGarage filing is from 2024, a later firm's seat.")

assert len(lines) == 38, len(lines)
jl.write("jmd", lines)
