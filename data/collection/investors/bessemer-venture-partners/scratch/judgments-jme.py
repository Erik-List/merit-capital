"""PRO-80 Bessemer, judge jm, file e: the remaining not_member rows (batches 21 to 25): Jeremy Levine and Steve Kraus
homonyms, two personal seats of Rob Stavis, and three rows that fall to a standing exclusion (sale consideration, the
control addendum). The last three are flagged for review in the judge's report.
"""
import judge_lib as jl

NM = "not_member"
lines = []


def nm(slug, basis, ec="formd_adjudicated", conf="high", cite=None):
    lines.append(jl.verdict(slug, NM, basis, ec=ec, conf=conf, cite=cite))


# ---- Jeremy Levine: partner since 2001; the name is shared by the founder of StarStreet and Underdog
JLV = (" The issuer is not on the firm's own list or on Jeremy Levine's deal-partner map, and no Bessemer fund appears in "
       "its rounds.")
nm("starstreet-inc", "Form D name match only, a homonym: the filings (2013 to 2017) name Jeremy Levine as an executive "
   "officer of StarStreet, its own founder, not the Bessemer partner." + JLV)
nm("underdog-sports-holdings-inc", "Form D name match only, a homonym: the 2025 filing names Jeremy Levine as an executive "
   "officer of Underdog, its own founder (the StarStreet founder), not the Bessemer partner." + JLV)
nm("firescope-inc", "Form D name match with no corroboration: a 'Jeremy Levine' sits on the board of this Huntington Beach "
   "IT-monitoring company through twelve small filings (2009 to 2012); nothing identifies him as the Bessemer partner, "
   "and a company the partner sat on for four years would be on the firm's list (decisions.md D6)." + JLV, conf="medium")
nm("psudo-inc", "Form D name match with no corroboration: a 'Jeremy Levine' is a director of this Hermosa Beach footwear "
   "company, which raised $150,000 through a placement agent in 2023; nothing identifies him as the Bessemer partner "
   "(decisions.md D6)." + JLV, conf="medium")

# ---- Steve Kraus: partner since 2008 (healthcare); a common name
nm("total-talent-network-inc", "Form D name match with no corroboration: a 'Steve Kraus' is a director of this Timonium, "
   "Maryland staffing company, which had sold $300,000 in 2024; nothing identifies him as the Bessemer healthcare "
   "partner, and the issuer is not on the firm's list or his deal-partner map (decisions.md D6).", conf="medium")
nm("future-health-acquisition-inc", "Form D name match only, a homonym: the 2011 filing names a 'Steven Kraus' as an "
   "executive officer of this Watertown, South Dakota company, an operator, not the Bessemer partner; the issuer is not "
   "on the firm's list or deal-partner map (decisions.md D6).")

# ---- Rob Stavis: two seats that are his own
nm("ikigai-alpha-inc", "Personal seat, not fund money (decisions.md D4): Ikigai Alpha is Loris.ai, the company Nancy Lublin "
   "spun out of Crisis Text Line; its $2M seed of February 2018 was led by Ann Miura-Ko with Kapor Capital, Omidyar "
   "Network, Homebrew and others, and names no Bessemer fund. Rob Stavis sat on the board in his own capacity; the "
   "company is not on the firm's list or his deal-partner map.", ec="web", conf="medium",
   cite=jl.NEWS("ikigai-alpha-inc", "Secures $2M"))
nm("assembly-osm-inc", "Personal investment, not fund money (decisions.md D4): Assembly OSM's $38M Series A of July 2022 "
   "was led by Fifth Wall Climate and Rob Stavis as an individual, and the announcement names no Bessemer fund; the "
   "company is not on the firm's list or his deal-partner map.", ec="web", conf="medium",
   cite="https://theconstructionbroadsheet.com/modular-firm-assembly-osm-draws-m-in-latest-funding-round-p965-174.htm")

# ---- sale consideration: the Gentle Dental stake was received for GMS Dental Group
nm("gentle-dental-service-corp", "Sale consideration (Erik 2026-09-22): the Bessemer vehicle on the filings (Bessemer "
   "Venture Partners GMS, then Bessemer Venture Partners IV) held stock issued on 4 November 1997, when the listed "
   "Gentle Dental Service Corporation merged the private GMS Dental Group into itself and issued about 4,548,200 shares "
   "for all of GMS's stock. The investment was GMS Dental Group (its holders, Sprout, Accel and Bessemer Venture Partners "
   "GMS, appear in the 1998 proxy), which is the row the base should carry; no Bessemer fund bought a round of Gentle Dental itself.", ec="fund_filing", conf="medium",
   cite="https://www.sec.gov/Archives/edgar/data/898807/0000893877-97-000678.txt")

# ---- control addendum (COLLECTION.md s1 Control positions; decisions.md D5)
nm("gfi-software-s-a", "Control position (COLLECTION.md control addendum, decisions.md D5): GFI Software S.A. is the "
   "Luxembourg holding company of TeamViewer and GFI (the firm lists it as LogicNow (GFI); the same SEC registrant as "
   "the base row logicnow). Its own F-1 says funds affiliated with Insight acquired control of the registrant in July "
   "2009, when it became the parent of TeamViewer; the Bessemer funds were co-investors in that buyout through "
   "TeamViewer Holdings beside Insight and Greenspring, and the firm's own BVP Forge post names TeamViewer among its companies that "
   "fit a growth buyout structure. A control acquisition by the co-investor group is not a venture round. The position is also the same "
   "investment as the listed rows teamviewer and logicnow.", ec="fund_filing", conf="medium",
   cite="https://www.sec.gov/Archives/edgar/data/1534271/000104746912009998/a2208946zf-1.htm")
nm("ws-holdco-pbc", "Control position (COLLECTION.md control addendum, decisions.md D5): WS Holdco is WiredScore (chief "
   "executive Arie Barendrecht on the filing; the firm lists it as WiredScore, base row wiredscore). Bessemer's first "
   "entry, in October 2017, was the purchase of a majority interest by an investor group led by Bessemer Venture "
   "Partners and Fifth Wall, which bought out Jared Kushner's stake; the trade press reported it as the group acquiring "
   "WiredScore. The issuer is a holding company incorporated in 2017 for that purchase. A transaction in which the firm and its "
   "co-investor group take control is not a venture round, and the 2018 Series A came after it.", ec="web", conf="medium",
   cite="https://www.venturecapitaljournal.com/bessemer-and-fifth-wall-led-investor-group-acquires-wiredscore/")

assert len(lines) == 11, len(lines)
jl.write("jme", lines)
