"""PRO-80 Bessemer Venture Partners, delta judge d1, file b (m4-financial to zingage, 22 rows).

Rows the rebuild added: companies from the firm's own 1999 to 2007 site (membership seeded on the listing) and
recall additions (verdict line plus classification line). Every URL below was printed by a tool run in this
session and read on 2026-10-06 (Light Reading through its own site search, SEC documents through secget.py,
news items through nq.py and judge_lib.NEWS, two pages found by web search); recall citations are read off the
base row's own note.

Run once: NQ_TAG=d1 python3 judgments-d1b.py
"""
import json
import re

import judge_lib as jl
from judge_lib import cls, verdict, rnd, ARCH, NEWS, W

WV = "web_verified"
_BASE = {r["slug"]: r for r in json.loads((jl.INV / "companies" / "base.json").read_text())}


def RC(slug):
    """The citation carried by the row's own 'recall addition:' note (the last URL in brackets)."""
    urls = re.findall(r"\((https?://[^)\s]+)\)", _BASE[slug].get("notes") or "")
    if not urls:
        raise SystemExit(f"RC({slug!r}): no citation in the row's note")
    return urls[-1]


LR = "https://www.lightreading.com"
LR_MEGISTO_SOLD = LR + "/cable-technology/megisto-sells-up"
LR_OMM_END = LR + "/cable-technology/omm-the-end-is-near"
LR_ORESIS_65 = LR + "/business-management/oresis-scores-65m-round-3"
LR_ORESIS_SHUT = LR + "/cable-technology/headcount-long-holidays"
LR_REEF_7 = LR + "/business-management/reefedge-reels-in-7m"
OMM_S1 = "https://www.sec.gov/Archives/edgar/data/1100338/000109581100005310/f65428a3s-1a.txt"
TC_PERC = NEWS("perceptron", "Ex-Meta scientists want to bring")
PERC_SITE = "https://perceptron.inc/about"
TECHEU = RC("sifflet")
PRN_SIFFLET = "https://www.prnewswire.com/news-releases/sifflet-confirms-momentum-with-18m-in-funding-302486300.html"
HIT_ZINGAGE = NEWS("zingage", "Healthcare IT Today")

FIRST_LISTED = "No round named; {y} is the first year the firm listed it, not an investment year."
FIRM_YEAR = "No round named; {y} is the firm's own investment year."

L = []

# ---- M4 Financial
L.append(cls("m4-financial", status="unknown", rng="below_1b", stage="undetermined", entry_date="2000",
             focus="Fintech & Payments", flags=["city_unknown", "country_unknown"], rounds=[],
             note="An eFinance application service provider for B2B exchanges on the firm's 2000 listing. EDGAR full "
                  "text and Google News (searched 2026-10-06) show no company of this name and business, so its "
                  "location and fate are not established. " + FIRM_YEAR.format(y=2000)))

# ---- Megisto Systems
L.append(cls("megisto-systems", status="acquired", rng="below_1b", stage="undetermined", entry_date="2002",
             country="US", city="Germantown", city_src=WV, focus="Data Infrastructure", rounds=[],
             note="Mobile data services platform, Germantown, Maryland, with about $60 million of venture funding. In "
                  "July 2005 its chief executive said it had concluded 'selling its product and all its customers to "
                  "another company', reported as Interactive Technology Holdings of Hong Kong for about $1 million "
                  "(Light Reading, 2005-07-01), so it reads acquired on an asset sale. "
                  + FIRST_LISTED.format(y=2002)))

# ---- Mindspring
L.append(cls("mindspring", status="acquired", rng="below_1b", stage="undetermined", entry_date="1995", country="US",
             city="Atlanta", focus="Data Infrastructure", rounds=[],
             note="Internet service provider, Atlanta; merged into EarthLink on 2000-02-04 (Wikipedia). MindSpring's "
                  "1996 registration statement shows its preferred stock going only to ITC Holding (59.1% in 1995) "
                  "and never names Bessemer, so the firm's position may have been held through ITC Holding, itself a "
                  "row; it stays a member on the firm's own listing. " + FIRM_YEAR.format(y=1995)))

# ---- MyKidsDoctor.com
L.append(cls("mykidsdoctor-com", status="unknown", rng="below_1b", stage="undetermined", entry_date="2000",
             country="US", focus="Healthcare & Bio", flags=["city_unknown"], rounds=[],
             note="Online tools for pediatricians and their patients on the firm's 2000 listing. EDGAR full text and "
                  "Google News (searched 2026-10-06) return nothing on the name, so its fate is not established. "
                  + FIRM_YEAR.format(y=2000)))

# ---- NewChannel
L.append(cls("newchannel", status="acquired", rng="below_1b", stage="undetermined", entry_date="1998", country="US",
             focus="SaaS", flags=["city_unknown"], rounds=[],
             note="Proactive online sales service for e-commerce sites, 'Silicon Valley based' (LivePerson). "
                  "LivePerson's 10-K for 2002 says that in July 2002 it 'acquired all of the existing customer "
                  "contracts of NewChannel, Inc. and associated rights' for an initial $600,000, an asset sale: acq. "
                  "by LivePerson, 2002. " + FIRM_YEAR.format(y=1998)))

# ---- Notara
L.append(cls("notara", status="unknown", rng="below_1b", stage="undetermined", entry_date="2000", country="US",
             focus="SaaS", flags=["city_unknown"], rounds=[],
             note="Web services for managing brand licensing and sponsorship. MediaBin's annual report of April 2002 "
                  "still names Notara as a competitor; nothing later was found, so its fate is not established. "
                  + FIRM_YEAR.format(y=2000)))

# ---- OMM
L.append(cls("omm", status="defunct", rng="below_1b", stage="Growth", stage_src=WV, stage_cite=OMM_S1,
             stage_conf="high", entry_date="1998", country="US", city="San Diego", city_src=WV,
             focus="Industrial & Robotics",
             rounds=[rnd("1998-10-16", "Series C preferred", 5085300, None, True, OMM_S1, "filing"),
                     rnd("1999-11-16", "Series D preferred", 22075000, None, True, OMM_S1, "filing"),
                     rnd("2000-05-31", "Series E preferred", 75000000, None, True, OMM_S1, "filing")],
             note="Optical MEMS switching components, San Diego. OMM's registration statement (amended 2000-12-15) "
                  "lists entities affiliated with Bessemer Venture Partners IV among the buyers of its Series C "
                  "preferred, sold in October and December 1998 for $5.1 million, their first purchase, and of the "
                  "Series D and E; the record calls the entry Series C, so it reads Growth. It announced on "
                  "2003-03-04 that it would shut down that week (Light Reading)."))

# ---- Oresis Communications
L.append(cls("oresis-communications", status="defunct", rng="below_1b", stage="undetermined", entry_date="2001",
             country="US", city="Beaverton", city_src=WV, focus="Data Infrastructure",
             rounds=[rnd("2001-03-05", "third round", 65000000, "UBS Capital Americas", True, LR_ORESIS_65,
                         "company")],
             note="Carrier voice and data switch maker, Beaverton, Oregon. The company's release of 2001-03-05 lists "
                  "Bessemer among the 'existing investors' in its third round, so the entry is an earlier round the "
                  "record read does not name or date; 2001 is the latest year it can be. It filed for bankruptcy in "
                  "early November 2002 and shut its doors that month (Light Reading, 2002-11-25)."))

# ---- Perceptron (recall addition)
L.append(verdict("perceptron", "member",
                 "The firm's own fund announcement (2026-09): 'Companies like Abridge, ChipAgents, fal, Noda, "
                 "Perceptron, Plenful, TurbineOne, and Wonderful reflect that enduring commitment' to early-stage "
                 "investing; its post of 2026-04-16 lists Perceptron in 'our portfolio', and TechCrunch (2026-08-26) "
                 "reports $21 million raised 'from Bessemer Venture Partners, Foundation Capital, and S32'.",
                 ec="web", conf="high", cite=RC("perceptron")))
L.append(cls("perceptron", status="private", rng="below_1b", stage="undetermined", country="US", city="Bellevue",
             city_src=WV, focus="AI & Applied AI",
             rounds=[rnd(None, "unnamed (total raised to date)", 21000000, None, True, TC_PERC, "press")],
             note="Perceptron AI, vision models for robots and machines, founded in November 2024 by two former Meta "
                  "researchers; its open roles are all in Bellevue, Washington (the company's site). TechCrunch "
                  "(2026-08-26): it 'previously raised $21 million from Bessemer Venture Partners, Foundation "
                  "Capital, and S32, according to Pitchbook', a vendor figure with no round named, so the stage is "
                  "undetermined and the entry undated. Checked 2026-10-06 for a priced round at $1B or more: none "
                  "found (Google News); TechCrunch says a further round was being closed."))

# ---- PrismTPO (recall addition)
L.append(verdict("prismtpo", "member",
                 "The firm's own post of 2026-01-20 promoting Sofia Guerra to partner speaks of 'the way she shows up "
                 "in the boardrooms of PrismTPO, Zingage, and Pivotal Health', her seats as a Bessemer investor; no "
                 "round announcement naming the firm was found, so confidence is medium.",
                 ec="web", conf="medium", cite=RC("prismtpo")))
L.append(cls("prismtpo", status="private", rng="below_1b", stage="undetermined", country="US",
             focus="Healthcare & Bio", flags=["city_unknown"], rounds=[],
             note="Prism TPO, a drug purchasing and pricing transparency platform for independent oncology practices "
                  "in the United States; its site carries 2026 press releases (prismtpo.com, read 2026-10-06), so it "
                  "reads private. Its own releases name only Obvious Ventures as a backer and no funding report was "
                  "found (Google News and one web search, 2026-10-06), so the round, the entry date and the head "
                  "office are not established."))

# ---- PurchasingCenter
L.append(cls("purchasingcenter", status="unknown", rng="below_1b", stage="undetermined", entry_date="1999",
             country="US", focus="Consumer & Marketplaces", flags=["city_unknown"], rounds=[],
             note="Online procurement marketplace for industrial supplies and services on the firm's 2000 listing. "
                  "EDGAR full text and Google News (searched 2026-10-06) return nothing on the name, so its fate is "
                  "not established. " + FIRM_YEAR.format(y=1999)))

# ---- ReefEdge
L.append(cls("reefedge", status="unknown", rng="below_1b", stage="undetermined", entry_date="2000", country="US",
             city="Fort Lee", city_src=WV, focus="Security",
             rounds=[rnd("2000", "initial round (no series named)", 6800000,
                         "Bessemer Venture Partners; Columbia Capital", True, LR_REEF_7, "company"),
                     rnd(None, "second round (no series named)", 15000000, "RRE Ventures", True, LR_REEF_7,
                         "company"),
                     rnd("2001-12-18", "third round (no series named)", 7000000, None, None, LR_REEF_7, "company")],
             note="Wireless LAN security systems, Fort Lee, New Jersey. The company's release of 2001-12-18 says 'the "
                  "initial round funding of $6.8 million in 2000 was led by Bessemer Ventures and Columbia Capital', "
                  "an entry at the first round, which the record does not name, so the stage is undetermined. It was "
                  "restructuring in November 2004 (Light Reading) and sold its technology patents to Symantec for "
                  "$800,000 in January 2005 (Symantec 10-K); no source read says whether the company closed, so its "
                  "fate is not established."))

# ---- Ridgeway Systems and Software
L.append(cls("ridgeway-systems-and-software", status="acquired", rng="below_1b", stage="undetermined",
             entry_date="1998", country="GB", country_src=WV, country_cite=W("Tandberg"), city="Reading",
             focus="Data Infrastructure", rounds=[],
             note="Software for carrying video and voice calls over IP networks and through firewalls, Reading, "
                  "England (city from memory). Wikipedia (Tandberg): 'In 2004, Ridgeway Systems and Software, a "
                  "UK-based software house specializing in firewall and NAT traversal, was acquired': acq. by "
                  "Tandberg, 2004. " + FIRM_YEAR.format(y=1998)))

# ---- Santel Networks
L.append(cls("santel-networks", status="unknown", rng="below_1b", stage="undetermined", entry_date="2002",
             country="US", city="Newark", city_src=WV, focus="Industrial & Robotics", rounds=[],
             note="Fabless chip startup for signal enhancement in optical networks, Newark, California (company "
                  "release, 2002-03-13). Its last Light Reading item is from December 2002 and an officer's "
                  "biography ends his term there in 2003 (Tessera 8-K, 2008); nothing says whether it was sold or "
                  "closed, so its fate is not established. " + FIRST_LISTED.format(y=2002)))

# ---- Sifflet (recall addition)
L.append(verdict("sifflet", "member",
                 "Tech.eu (2023-03-21): 'The €12 million Series A round was led by EQT Ventures with existing "
                 "seed round investors Bessemer Venture Partners and Mangrove Capital participating.'",
                 ec="web", conf="high", cite=TECHEU))
L.append(cls("sifflet", status="private", rng="below_1b", stage="Seed", stage_src=WV, stage_cite=TECHEU,
             stage_conf="high", entry_date="2021-11", grad="graduated", grad_src=WV, grad_cite=TECHEU,
             grad_conf="high", country="FR", country_src=WV, country_cite=TECHEU, city="Paris", city_src=WV,
             focus="Data Infrastructure",
             rounds=[rnd("2021-11", "Seed", None, None, True, TECHEU, "press"),
                     rnd("2023-03-21", "Series A", 12931200, "EQT Ventures", True, TECHEU, "press"),
                     rnd("2025-06-19", "unnamed funding from existing shareholders", 18000000, None, None,
                         PRN_SIFFLET, "company")],
             note="Data observability platform, Paris. Tech.eu (2023-03-21): the startup 'raised undisclosed amounts "
                  "in a seed round' in November 2021, and the Series A was led by EQT Ventures 'with existing seed "
                  "round investors Bessemer Venture Partners and Mangrove Capital participating', so the entry is "
                  "the seed and it graduated (EUR 12.0M @ ECB 2023-03-21 (EUR/USD 1.0776) = $12.9M). Checked "
                  "2026-10-06 for a priced round at $1B or more: none found (Google News); the newest round is $18M "
                  "from existing shareholders in June 2025 (company release), which does not name Bessemer."))

# ---- Sparter
L.append(cls("sparter", status="defunct", rng="below_1b", stage="undetermined", entry_date="2007", country="US",
             focus="Consumer & Marketplaces", flags=["city_unknown"], rounds=[],
             note="Marketplace for virtual game currencies. TechCrunch (2007-06-12) calls it 'a stealth startup "
                  "founded by Bessemer Venture Partners', which names no round, so the stage is undetermined and "
                  "2007 is the first year the firm listed it; TechCrunch (2008-06-03) reports that it 'has "
                  "effectively shut down'. No source read places its office."))

# ---- Synergy Computer Graphics
L.append(cls("synergy-computer-graphics", status="acquired", rng="below_1b", stage="Seed", stage_src="first_party",
             stage_cite=ARCH("synergy-computer-graphics"), stage_conf="high", entry_date="1984", country="US",
             focus="Industrial & Robotics", flags=["city_unknown"],
             rounds=[rnd("1984", "Seed", None, None, True, ARCH("synergy-computer-graphics"), "firm")],
             note="Maker of color printers and plotters. The firm's own listing: 'BVP seeded Synergy, a manufacturer "
                  "of high-performance color printers and plotters, in 1984. Four years later, Nippon Steel bought "
                  "the operation', so a Seed entry in 1984 and acq. by Nippon Steel, 1988. Graduation left for the "
                  "graduation pass. No source read places its office."))

# ---- Tiburon Networks
L.append(cls("tiburon-networks", status="unknown", rng="below_1b", stage="undetermined", entry_date="2002",
             country="US", city="Andover", focus="Data Infrastructure", rounds=[],
             note="Optical networking startup in the Merrimack Valley of Massachusetts, Andover (city from memory; "
                  "CommonWealth magazine has it cutting staff from 120 to 80 after the crash). No source read reports a "
                  "sale or a closure, so its fate is not established; the Greylock book reads defunct (closed 2002) and "
                  "Petaluma from memory. " + FIRST_LISTED.format(y=2002)))

# ---- utMOST Technologies
L.append(cls("utmost-technologies", status="unknown", rng="below_1b", stage="undetermined", entry_date="2002",
             focus="Industrial & Robotics", flags=["city_unknown", "country_unknown"], rounds=[],
             note="Developer of ultra-high-speed silicon for optical applications (the firm's sentence calls it "
                  "Utmost Systems), listed in 2002 only. EDGAR full text, Light Reading and Google News (searched "
                  "2026-10-06) return nothing on the name, so its location and fate are not established. "
                  + FIRST_LISTED.format(y=2002)))

# ---- Voter.com
L.append(cls("voter-com", status="defunct", rng="below_1b", stage="undetermined", entry_date="2000", country="US",
             city="Boston", focus="Media, Gaming & Advertising", rounds=[],
             note="Political news and election website founded in November 1999, Boston (city from memory). "
                  "Washington Technology (2001-02-07): Voter.com 'conceded Feb. 5 it was time to close up shop for "
                  "good', so it reads defunct. " + FIRM_YEAR.format(y=2000)))

# ---- WorldChain
L.append(cls("worldchain", status="unknown", rng="below_1b", stage="undetermined", entry_date="2000", country="US",
             focus="SaaS", flags=["city_unknown"], rounds=[],
             note="Internet-based supply chain management services for manufacturers. Its chief executive served "
                  "from 2001 to 2004 (Del Monte 10-K) and Optum, Inc. owed WorldChain a promissory note dated "
                  "2004-05-12 (Click Commerce's merger agreement for Optum), which suggests a sale of the business "
                  "to Optum but does not state one, so its fate is not established. " + FIRM_YEAR.format(y=2000)))

# ---- Zingage (recall addition)
L.append(verdict("zingage", "member",
                 "The firm's own post of 2026-08-12 lists Zingage among the companies it has 'backed', and the "
                 "company's release (Healthcare IT Today, 2025-11-18) announces '$12.5 million in seed funding led "
                 "by Bessemer Venture Partners'.",
                 ec="web", conf="high", cite=RC("zingage")))
L.append(cls("zingage", status="private", rng="below_1b", stage="Seed", stage_src=WV, stage_cite=HIT_ZINGAGE,
             stage_conf="high", entry_date="2025-10-07", grad="censored", country="US", city="New York",
             city_src=WV, focus="Healthcare & Bio",
             rounds=[rnd("2025-10-07", "Seed", 12500000, "Bessemer Venture Partners", True, HIT_ZINGAGE, "company")],
             note="AI care delivery platform for home care agencies, 'Founded in 2023 and based in New York'. The "
                  "company's release (first announced 2025-10-07): '$12.5 million in seed funding led by Bessemer "
                  "Venture Partners, alongside TQ Ventures, South Park Commons, WndrCo, and executives from Ramp'. "
                  "An entry after 2024-10-01, so censored. Checked 2026-10-06 for a later round or a $1B mark: none "
                  "found (Google News)."))

assert len({x["slug"] for x in L}) == 22, len({x["slug"] for x in L})
for x in L:
    for k in ("note", "basis"):
        assert "—" not in (x.get(k) or "") and "–" not in (x.get(k) or ""), x["slug"]

jl.write("d1b", L)
