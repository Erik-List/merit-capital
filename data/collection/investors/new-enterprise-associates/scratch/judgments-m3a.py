"""PRO-100 NEA, judge m3, first half (38 rows): Form D name-match rows, judged cluster-first.
Run: NQ_TAG=m3 python3 judgments-m3a.py"""
import judge_lib as jl

verdict, cls, rnd = jl.verdict, jl.cls, jl.rnd
FD = "formd_adjudicated"
L = []


def out(slug, basis, conf="high", cite=None, ec=FD):
    L.append(verdict(slug, "not_member", basis, ec=ec, conf=conf, cite=cite))


# ---------------- Ralph Snyderman: NEA venture partner January 2006 to November 2009 ----------------
CAREDX = jl.FTS("CareDx", "DRS")
SNY = ("Ralph Snyderman was an NEA venture partner from January 2006 to November 2009 (CareDx's registration statement, "
       "which names NEA only in his biography)")
out("caredx-inc", f"{SNY}; his 2016 CareDx board seat comes after those years, the registration statement lists no NEA fund "
    "among holders, and no NEA listing, post or filing names CareDx (T4, D4).", cite=CAREDX)
out("xdx-inc", f"{SNY}; XDx (CareDx's earlier name) lists him as a director on 2010-2011 filings, after those years, beside "
    "Kleiner Perkins' Brook Byers, and CareDx's registration statement lists no NEA fund among holders (T4, D4).", cite=CAREDX)
out("crescendo-bioscience-inc", f"{SNY}; his Crescendo Bioscience seat on the 2011-2013 filings comes after those years, beside "
    "Kleiner Perkins' Brook Byers, and no NEA listing, post or filing names Crescendo (T4, D4).", cite=CAREDX)
out("essential-health-solutions-inc", f"{SNY}; his 2016-2018 seat on this Raleigh company comes years after, and no NEA listing, "
    "post or filing names it (T4, D4).", cite=CAREDX)
out("proventys-inc", f"{SNY}; his seat on Proventys' June 2010 filing (Newton, MA) comes after those years, and no NEA listing, "
    "post or filing names Proventys (T4, D4).", cite=CAREDX)
out("sengenix-inc", f"{SNY}; his 2014-2017 seat on this Durham, NC company comes years after, and no NEA listing, post or filing "
    "names SenGenix (T4, D4).", cite=CAREDX)
out("veritas-collaborative-holdings-llc", f"{SNY}; his 2016-2020 seat on Veritas Collaborative (Durham, NC) gives his own Duke "
    "University address and comes years after, and no NEA listing, post or filing names it (T4, D4).", cite=CAREDX)
out("zealcare-inc", f"{SNY}; on ZealCare's 2021-2025 filings he is an executive officer and director of a Cary, NC startup, "
    "an operator role long after his NEA years, and no NEA surface names ZealCare (T4).", cite=CAREDX)

# ---------------- Michael Li: NEA healthcare associate from 2021 ----------------
LI = ("NEA's Michael Li joined the healthcare team as an associate in 2021 (the firm's team pages 2021-2023, a principal on the "
      "live team)")
for s, what in [
    ("ambiq-micro-inc", "Ambiq Micro's 2017-2020 filings (an Austin chip company, beside Ker Zhang and Huang Lee)"),
    ("consensus-orthopedics-inc", "Consensus Orthopedics' 2014 filings (El Dorado Hills, CA)"),
    ("flexterra-inc", "Flexterra's 2017-2020 filings (Skokie, IL, beside Frank Ge)"),
    ("polyera-corp", "Polyera's 2012-2016 filings (Skokie, IL, beside Frank Ge)"),
    ("qd-vision-inc", "QD Vision's 2015 filing (Lexington, MA)"),
    ("waffle-labs-inc", "Waffle Labs' filings from its December 2018 founding round (New York)"),
    ("wibotic-inc", "WiBotic's filings from 2018 (Seattle, beside Pingrong Yu)"),
]:
    out(s, f"{LI}; the Michael Li on {what} holds a hardware and consumer seat taken before he joined, a namesake from another "
        "investor group, and no NEA listing, post or filing names the company (T4 homonym).")

# ---------------- Paul Walker: NEA healthcare partner, Menlo Park ----------------
PW = "NEA's Paul Walker is a healthcare (biotech) partner in Menlo Park (the firm's team pages from 2008)"
out("gfi-software-s-a", f"{PW}; the Paul Walker on GFI Software's 2011-2015 filings is a director of a Luxembourg software "
    "holding company beside Insight Venture Partners' Jeff Horing and Michael Triplett, a namesake, and no NEA listing, post or "
    "filing names GFI (T4 homonym).")
out("logicnow-s-a", f"{PW}; LogicNow (GFI Software's 2015 spin-off, Luxembourg) carries the same board with Insight Venture "
    "Partners' Jeff Horing, a namesake director, and no NEA listing, post or filing names LogicNow (T4 homonym).")
out("med-access-inc", f"{PW}; the Paul Walker on Med Access' 2009 filing is its executive officer and promoter in Kelowna, "
    "British Columbia, on a $10,000 offering, an operator namesake (T4 homonym).")
out("spectral-medical-inc", f"{PW}; the Paul Walker on Spectral Medical's 2016 and 2022 filings is the Toronto company's own "
    "chief executive and director (a TSX-listed company), an operator namesake, and no NEA surface names Spectral (T4 homonym; X1).")
out("unqork-inc", f"{PW}; Unqork named Goldman Sachs alumnus Paul Walker to its board in August 2019 (PR Newswire), the "
    "director on its 2019-2020 filings, a namesake, and no NEA listing, post or filing names Unqork (T4 homonym).",
    cite=jl.NEWS("unqork-inc", "Goldman Sachs Alum Paul Walker"))
out("valstro-holdings-llc", f"{PW}; the Paul Walker on Valstro's 2025 filing is a director of a New York trading-workflow "
    "software company, a technology namesake, and no NEA listing, post or filing names Valstro (T4 homonym).")

# ---------------- Joshua Makower: venture partner from 2008, general partner from 2015, special partner from 2022 ----------------
CETERIX_MEMBER = False
if CETERIX_MEMBER:
    pass
else:
    out("ceterix-orthopaedics-inc", "Josh Makower, then an NEA venture partner (team pages 2008-2015), is a director on Ceterix's "
        "2013-2014 filings and the firm's 2015 release lists Ceterix among his directorships, but NEA's own list never carried "
        "Ceterix in any era and no round release, filing or post we could read names an NEA fund in it; a venture partner's seat "
        "counts only where an NEA fund held the position (D4). Vendor profiles list NEA, which is a lead for the A/B pass, not "
        "evidence (Rule A).", conf="medium", cite=jl.POST("nea-names-josh-makower"))
out("coravin-llc", "Josh Makower co-founded Coravin (the firm's own 2015 release calls it his co-founded consumer products company) "
    "and sits on its board as a founder; its rounds came from Quadrille Capital and Windham Venture Partners (Decanter, 2015), "
    "and no NEA listing, post or filing names NEA money in Coravin (T4 personal seat, D4).",
    cite=jl.NEWS("coravin-llc", "secures another"))

L.append(verdict("exploramed-nc7-inc", "member",
    "Same company as the listed member 'willow': ExploraMed NC7, Inc. is Willow's legal name (the Mountain View breast-pump company "
    "Makower's ExploraMed incubated, directors Makower and Croce), which NEA lists with a 2014 first investment. Recorded as a "
    "member so the row is not left unjudged; identity-merges.json should fold it into 'willow'.",
    ec="site_listing", conf="high", cite=jl.SITE("willow")))
L.append(cls("exploramed-nc7-inc", status="private", rng="below_1b", city="Mountain View", focus="Healthcare & Bio",
    note="Willow (wearable breast pump), still private; no priced round near $1B on record. The 2020 filing gives 1975 W El Camino "
         "Real, Mountain View."))

L.append(verdict("nc8-inc", "member",
    "Same company as the listed member 'revelle-aesthetics': EDGAR records NC8, Inc. (CIK 1819592) as Revelle Aesthetics' former "
    "name, which NEA lists with a 2020 first investment, and the firm's 2021 release names an NEA partner as NC8's board observer. "
    "Recorded as a member so the row is not left unjudged; identity-merges.json should fold it into 'revelle-aesthetics'.",
    ec="site_listing", conf="high", cite=jl.SITE("revelle-aesthetics")))
L.append(cls("nc8-inc", status="acquired", rng="below_1b", stage="undetermined", entry_date="2020", city="Mountain View",
    focus="Healthcare & Bio", rounds=[],
    note="Revelle Aesthetics (cellulite treatment, Mountain View), acquired by Tiger Aesthetics Medical per the firm's own exit "
         "line. The 2020 filing ($25M sold of $50M) is the first on record and names no round, so the entry stays undetermined."))

X9 = jl.NEWS("x9-inc", "Wallingford startup X9")
L.append(verdict("x9-inc", "member",
    "Tak Cheung, an NEA partner in 2022 (team pages), and Josh Makower are directors of record on X9's November 2022 seed filing; X9 "
    "resolves to the dialysis-needle company ExploraMed incubated (Hartford Business Journal, 2026). An in-tenure partner's seat is "
    "the adjudicated pattern, flagged for the A/B pass: the press names DaVita Venture Group as the main seed investor and does not "
    "name NEA.", ec=FD, conf="medium",
    cite="https://www.sec.gov/Archives/edgar/data/1956558/000195655822000001/0001956558-22-000001-index.htm"))
L.append(cls("x9-inc", status="private", rng="below_1b", grad="graduated", grad_src="web_verified", grad_cite=X9,
    grad_conf="medium", city="Wallingford", focus="Healthcare & Bio",
    rounds=[rnd("2022-11-18", "Seed", 5100000, "DaVita Venture Group", None, X9, "press"),
            rnd("2025-11-24", "Series B", 8568181, "DaVita Venture Group", None, X9, "press")],
    note="X9 (dialysis cannulation device) moved to Wallingford, CT; DaVita Venture Group led the seed and later a Series B, "
         "about $8.6M closed in late 2025 (Hartford Business Journal), a named later round, so the seed graduated."))

# ---------------- Anita Sands: NEA venture partner in 2022 only ----------------
NOW = jl.FTS("ServiceNow", "DEF 14A")
AS = ("Anita Sands was an NEA venture partner in 2022 only (ServiceNow's proxy statements; the firm's 2022 team page), and "
      "her board seats are independent directorships")
out("jumpcloud-inc", f"{AS}: JumpCloud's 2022 filings list her c/o the company among its directors, a personal seat, and no NEA "
    "listing, post or filing names JumpCloud (D4).", cite=NOW)
out("nu-holdings-ltd", f"{AS}: Nu Holdings' 2021 filings list her at her home address beside Sequoia's Doug Leone, before "
    "her NEA year, and no NEA listing, post or filing names Nu (D4).", cite=NOW)
out("reaper-topco-ltd", f"{AS}: Reaper Topco is an Apax-backed Jersey holding company (Apax's Jesus Molins on its board) and "
    "its 2022-2025 filings list her at her home address; a buyout holdco, not an NEA position (D3, D4).", cite=NOW)
out("rokt-inc", f"{AS}: her seat on Rokt's 2025 filing comes after her NEA year, and no NEA listing, post or filing names Rokt (D4).",
    cite=NOW)
out("servicenow-inc", f"{AS}: ServiceNow is a listed company whose board she joined as an independent director; its 2025 "
    "filing comes after her NEA year and no NEA fund held ServiceNow (D4, X1).", cite=NOW)

# ---------------- Jeong Seuk Kang: an operator, not NEA's associate Jeon Kang ----------------
JK = ("NEA's roster has no Jeong Seuk Kang (only Jeon Kang, a New York associate 2021-2023); the filer is a Boston biotech "
      "operator who co-founded MitoLab and March Therapeutics with Fahim Farzadfard")
out("mitolab-inc", f"{JK}, executive officer and director on MitoLab's 2020 filing, an operator seat (T4 homonym).")
out("march-therapeutics-inc", f"{JK}; he is executive officer on March Therapeutics' 2022 filing (the same EDGAR registrant as "
    "MitoLab), an operator seat (T4 homonym).")
out("dxlab-inc", f"{JK}; his 2020 DxLab seat sits beside Farzadfard, a founder's angel seat, and no NEA surface names DxLab "
    "(T4 homonym).")
out("parasol-technologies-inc", f"{JK}; his 2023 seat on Parasol Technologies (Redwood City, beside Joichi Ito) is a personal "
    "seat, and no NEA surface names Parasol (T4 homonym).")

# ---------------- Anthony Florence: a Pittsburgh operator, not NEA's Tony Florence ----------------
AF = ("The Anthony Florence on this filing is the executive officer and promoter of a Carnegie/Pittsburgh, PA company at 215 "
      "Park Road, an operator namesake of NEA's technology partner Tony Florence (Chevy Chase, later New York)")
out("advanced-technology-healthcare-solutions-inc", f"{AF}; no NEA surface names the company (T4 homonym).")
out("brainstage-inc", f"{AF}; he is the sole related person on Brainstage's 2015 filings and no NEA surface names it (T4 homonym).")
out("skinject-inc", f"{AF}; he is director and promoter of SkinJect (Pittsburgh) on its 2015-2019 filings and no NEA surface "
    "names it (T4 homonym).")

jl.write("m3a", L)
