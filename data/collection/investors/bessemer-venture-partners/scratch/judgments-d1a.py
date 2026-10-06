"""PRO-80 Bessemer Venture Partners, delta judge d1, file a (access-international to knology, 22 rows).

Rows the rebuild added: companies from the firm's own 1999 to 2007 site (membership seeded on the listing) and
recall additions (verdict line plus classification line). Every URL below was printed by a tool run in this
session and read on 2026-10-06 (Light Reading through its own site search, SEC documents through secget.py,
news items through nq.py and judge_lib.NEWS); recall citations are read off the base row's own note.

Run once: NQ_TAG=d1 python3 judgments-d1a.py
"""
import json
import re

import judge_lib as jl
from judge_lib import cls, verdict, rnd, ARCH, FTS, W

WV = "web_verified"
_BASE = {r["slug"]: r for r in json.loads((jl.INV / "companies" / "base.json").read_text())}


def RC(slug):
    """The citation carried by the row's own 'recall addition:' note (the last URL in brackets)."""
    urls = re.findall(r"\((https?://[^)\s]+)\)", _BASE[slug].get("notes") or "")
    if not urls:
        raise SystemExit(f"RC({slug!r}): no citation in the row's note")
    return urls[-1]


LR = "https://www.lightreading.com"
LR_AZANDA_B = LR + "/business-management/azanda-collects-19m"
LR_AZANDA_ACQ = LR + "/business-management/cortina-acquires-azanda"
LR_CEYBA_SHUT = LR + "/cable-technology/ceyba-shuts-down"
LR_SOLINET_93 = LR + "/business-management/solinet-closes-93m-round"
LR_COR_HIDE = LR + "/cable-technology/coriolis-comes-out-of-hiding"
LR_COR_20 = LR + "/cable-technology/coriolis-closes-20m-second-round"
LR_COR_SHUT = LR + "/cable-technology/coriolis-shuts-down"
LR_ISHONI_PHILIPS = LR + "/network-technology/royal-philips-bankrolls-ishoni"
LR_K2_29 = LR + "/network-technology/k2-reaches-round-2-peak-29m"
LR_K2_ACQ = LR + "/semiconductors/emcore-acquires-k2"
TC_FUR = "https://techcrunch.com/2026/10/06/furientis-lands-25m-from-benchmark-to-mass-produce-low-cost-missile-interceptors/"
KNOLOGY_CIRC = FTS("KNOLOGY", "DEFA14A")
FORTUNE_FUR = RC("furientis")
GROW_6K = RC("grow-mobile")

FIRST_LISTED = "No round named; {y} is the first year the firm listed it, not an investment year."
FIRM_YEAR = "No round named; {y} is the firm's own investment year."

L = []

# ---- Access International
L.append(cls("access-international", status="unknown", rng="below_1b", stage="undetermined", entry_date="2002",
             country="US", focus="Fintech & Payments", flags=["city_unknown"], rounds=[],
             note="Access International Financial Services, securities processing software for brokers. Level 8 "
                  "Systems took its stock for consulting work in 2000 and 2001 and sold that interest on 2001-10-01, "
                  "and the company's contract suit against Level 8 in the District of Colorado settled in February "
                  "2003 (Level 8 10-K for 2002); nothing later was found, so its fate is not established. "
                  + FIRST_LISTED.format(y=2002)))

# ---- AP Engines
L.append(cls("ap-engines", status="unknown", rng="below_1b", stage="undetermined", entry_date="2000",
             country="US", focus="Data Infrastructure", flags=["city_unknown"], rounds=[],
             note="Billing mediation software for IP services over broadband networks. K2 Digital's annual report "
                  "names AP Engines, Inc. among its five largest clients of 2000; EDGAR full text, Light Reading and "
                  "Google News (searched 2026-10-06) show nothing later, so its fate is not established. "
                  + FIRM_YEAR.format(y=2000)))

# ---- Azanda Network Devices
L.append(cls("azanda-network-devices", status="acquired", rng="below_1b", stage="Series A", stage_src=WV,
             stage_cite=LR_AZANDA_B, stage_conf="high", entry_date="2000", country="US", city="Sunnyvale",
             city_src=WV, focus="Industrial & Robotics",
             rounds=[rnd("2000", "Series A", 10000000, None, True, LR_AZANDA_B, "company"),
                     rnd("2002-03-11", "Series B", 19000000,
                         "Bessemer Venture Partners; Highland Capital Partners; Commonwealth Capital Ventures",
                         True, LR_AZANDA_B, "company")],
             note="Traffic management chips for optical networks, Sunnyvale. The company's release of 2002-03-11 says "
                  "'Series A investors Bessemer Venture Partners, Highland Capital Partners, and Commonwealth Capital "
                  "Ventures co-led' the $19M Series B and that it 'raised $10 million from its first round of funding "
                  "in 2000', so the entry is the 2000 Series A. Acq. by Cortina Systems, 2005 (Light Reading, "
                  "2005-02-02)."))

# ---- Bokee
L.append(cls("bokee", status="private", rng="below_1b", stage="undetermined", entry_date="2005", country="CN",
             country_src=WV, country_cite=ARCH("bokee"), city="Beijing", focus="Media, Gaming & Advertising",
             rounds=[rnd("2005", "unnamed venture funding", None, None, None,
                         W("Fang Xingdong"), "press")],
             note="Chinese blog host Bokee (bokee.com, formerly BlogChina), Beijing. Wikipedia (Fang Xingdong) says it "
                  "'received some funding from venture capital firms in 2005' without naming the round, and the firm "
                  "first listed it in January 2006, so the stage is undetermined and the date is that funding year. "
                  "bokee.com still serves a site (read 2026-10-06, its newest notice dated 2020), so it reads private."))

# ---- Ceyba (formerly Solinet Systems)
L.append(cls("ceyba", status="defunct", rng="below_1b", stage="undetermined", entry_date="2000", country="CA",
             country_src=WV, country_cite=LR_SOLINET_93, city="Ottawa", city_src=WV, focus="Data Infrastructure",
             rounds=[rnd(None, "first round (no series named)", 15000000, None, True, LR_SOLINET_93, "company"),
                     rnd("2001-05-31", "second round", 93000000, "U.S. Venture Partners", True, LR_SOLINET_93,
                         "company")],
             note="Long-haul optical systems maker, Ottawa (formerly Solinet Systems). Bessemer's Rob Soni was "
                  "already a director when the $93M second round closed on 2001-05-31 with $108M raised in all "
                  "(company release), so the entry is the unnamed first round of about $15M; the date is the year "
                  "the company started, inferred, since that round is undated. Closed in August 2003 (Light "
                  "Reading, 2003-08-05)."))

# ---- Collabria
L.append(cls("collabria", status="unknown", rng="below_1b", stage="undetermined", entry_date="1998", country="US",
             focus="SaaS", flags=["city_unknown"], rounds=[],
             note="Web-based print procurement software for the printing industry. Internet Capital Group held 8% at "
                  "the end of 2000 and reported no stake at 2001-06-30, and its chief financial officer left in June "
                  "2001 (FiberMark proxy, 2002); no source read says whether it was sold or closed, so its fate is "
                  "not established. " + FIRM_YEAR.format(y=1998)))

# ---- Coriolis Networks
L.append(cls("coriolis-networks", status="defunct", rng="below_1b", stage="undetermined", entry_date="2000",
             country="US", city="Boxborough", city_src=WV, focus="Data Infrastructure",
             rounds=[rnd(None, "first round (no series named)", 8500000, None, True, LR_COR_HIDE, "company"),
                     rnd("2000-08-22", "second round", 20000000, None, True, LR_COR_20, "company")],
             note="Metro optical equipment maker, Boxborough, Massachusetts. Its release of 2000-06-12 says it "
                  "'secured first-round funding from Bessemer Venture Partners, New Enterprise Associates and "
                  "Columbia Capital', which names no series, so the stage is undetermined; the date is the year of "
                  "that release, the round itself is undated (the company was founded in 1999). Closed on "
                  "2004-01-20 (Light Reading, 2004-01-21)."))

# ---- Determina (fka Araksha)
L.append(cls("determina", status="acquired", rng="below_1b", stage="undetermined", entry_date="2004", country="US",
             city="Redwood City", focus="Security", rounds=[],
             note="Memory firewall security software, Redwood City; first listed by the firm in April 2004 under its "
                  "earlier name Araksha. VMware's 10-Q for the quarter ended 2007-09-30 says it 'acquired Determina, "
                  "Inc.' in that quarter: acq. by VMware, 2007. " + FIRST_LISTED.format(y=2004)))

# ---- e-Steel (the same company as newview-technologies)
L.append(cls("e-steel", status="unknown", rng="below_1b", stage="undetermined", entry_date="1998", country="US",
             city="New York", focus="Consumer & Marketplaces", flags=["identity_conflated"], rounds=[],
             note="Online steel marketplace e-STEEL, New York, renamed NewView Technologies in 2001: the firm's own "
                  "2002 listing reads 'NewView Technologies (formerly e-STEEL Corporation)', so this row and "
                  "newview-technologies are one company. It was still a privately held software company in February "
                  "2003 (a former officer's biography in a Citizens Communications 10-K) and nothing later was "
                  "found, so its fate is not established; the Greylock book's two rows read acquired and defunct "
                  "from memory. " + FIRM_YEAR.format(y=1998)))

# ---- Elemental Security
L.append(cls("elemental-security", status="private", rng="below_1b", stage="undetermined", entry_date="2004",
             country="US", city="San Mateo", focus="Security", rounds=[],
             note="Security policy compliance software co-founded by Dan Farmer, San Mateo (city from memory). Its "
                  "site still serves as Elemental Cyber Security, Inc. (read 2026-10-06, copyright 2021), fresher "
                  "than the Sequoia book's uncited defunct reading, so it reads private. "
                  + FIRST_LISTED.format(y=2004)))

# ---- ePIT Systems
L.append(cls("epit-systems", status="unknown", rng="below_1b", stage="undetermined", entry_date="2000",
             country="US", focus="Fintech & Payments", flags=["city_unknown"], rounds=[],
             note="Exchange platform software for online markets. Its former president and chief executive Timothy "
                  "Campbell took over Industri-Matematik from January 2003 (that company's release of 2002-12-19); "
                  "no source read says what became of ePIT, so its fate is not established. "
                  + FIRM_YEAR.format(y=2000)))

# ---- Exemplary (Exemplary Software)
L.append(cls("exemplary", status="unknown", rng="below_1b", stage="undetermined", entry_date="1998", country="US",
             focus="SaaS", flags=["city_unknown"], rounds=[],
             note="Tools and templates that extend ERP applications (Exemplary Software). Business Objects' proxies "
                  "of 2002 and 2003 still list a director's seat at Exemplary Software and the firm listed it until "
                  "2005; nothing later was found, so its fate is not established. " + FIRM_YEAR.format(y=1998)))

# ---- Extraprise
L.append(cls("extraprise", status="unknown", rng="below_1b", stage="undetermined", entry_date="1997", country="US",
             city="Boston", focus="SaaS", rounds=[],
             note="CRM consulting, systems integration and training services (The Extraprise Group), Boston (city "
                  "from memory). The firm listed it until 2005; its domain now serves an unrelated gambling page "
                  "(read 2026-10-06) and no source read reports a sale or a closure, so its fate is not "
                  "established. " + FIRM_YEAR.format(y=1997)))

# ---- Fotomat (recall addition, pre-spin-out)
L.append(verdict("fotomat", "member",
                 "The firm's own history page (bvp.com/port/onepage.asp, Common Crawl capture of 2008-11-20): 'Pete "
                 "Bancroft joined Bessemer in 1967 to lead the venture practice. Some of his signature deals were "
                 "Measurex, Fotomat, and Interdata.' A deal of the venture group before the 1981 spin-out, stated on "
                 "the firm's own site (decisions.md R2, X1).",
                 ec="web", conf="high", cite=RC("fotomat")))
L.append(cls("fotomat", rng="below_1b", stage="undetermined", city="San Diego", focus="Consumer & Marketplaces",
             flags=["pre_spinout"], rounds=[],
             note="Drive-up photo finishing kiosks, founded in San Diego with the first kiosk in 1965; public in "
                  "1971 and acq. by Konishiroku (Konica), 1986 (Wikipedia). The firm's history page names it a "
                  "signature deal of Pete Bancroft, who joined in 1967; no source read dates the investment or "
                  "names the round, so the stage is undetermined and the entry undated."))

# ---- Furientis (recall addition)
L.append(verdict("furientis", "member",
                 "Fortune (2026-05-14) on the company's $5 million pre-seed: 'Silent Ventures led the round with "
                 "participation from Bessemer Venture Partners, SV Angel, Vanderbilt University, Channel 39 "
                 "Ventures, and the founders of companies including Anduril and Armada.'",
                 ec="web", conf="high", cite=FORTUNE_FUR))
L.append(cls("furientis", status="private", rng="below_1b", stage="Pre-Seed", stage_src=WV, stage_cite=FORTUNE_FUR,
             stage_conf="high", entry_date="2026-05", country="US", city="Los Angeles", city_src=WV,
             focus="Industrial & Robotics",
             rounds=[rnd("2026-05-14", "Pre-Seed", 5000000, "Silent Ventures", True, FORTUNE_FUR, "press"),
                     rnd("2026-10-06", "Seed", 25000000, "Benchmark", None, TC_FUR, "press")],
             note="Maker of low-cost interceptor missiles, Los Angeles. Fortune (2026-05-14) reports the $5 million "
                  "pre-seed led by Silent Ventures with Bessemer participating, the entry. TechCrunch (2026-10-06) "
                  "reports a $25 million seed led by Benchmark at a $125 million valuation 'according to a person "
                  "familiar with the company', the newest round found (Google News, 2026-10-06), far below $1B."))

# ---- Gloss.com
L.append(cls("gloss-com", status="acquired", rng="below_1b", stage="undetermined", entry_date="1999", country="US",
             city="San Francisco", focus="Consumer & Marketplaces", rounds=[],
             note="Online cosmetics retailer, San Francisco (city from memory). Estee Lauder's 10-K for fiscal 2001: "
                  "in fiscal 2000 'We also acquired Gloss.com, an Internet beauty site': acq. by Estee Lauder, 2000. "
                  + FIRM_YEAR.format(y=1999)))

# ---- Grow Mobile (recall addition)
L.append(verdict("grow-mobile", "member",
                 "Perion's release in its Form 6-K (2014-06-30): 'Grow Mobile is headquartered in San Francisco with "
                 "offices in New York and is venture-backed by Signia Venture Partners and Bessemer Venture "
                 "Partners.'",
                 ec="web", conf="high", cite=GROW_6K))
L.append(cls("grow-mobile", status="acquired", rng="below_1b", stage="undetermined", country="US",
             city="San Francisco", city_src=WV, focus="Media, Gaming & Advertising", rounds=[],
             note="Mobile app advertising platform, San Francisco, 'founded less than two years ago' in June 2014. "
                  "Acq. by Perion Network, 2014 (definitive agreement announced 2014-06-30, Perion's 6-K). The record "
                  "read names Bessemer only as a backer, with no round and no date (Google News searched "
                  "2026-10-06), so the stage is undetermined and the entry undated."))

# ---- HotSocket
L.append(cls("hotsocket", status="unknown", rng="below_1b", stage="undetermined", entry_date="2000", country="US",
             focus="Media, Gaming & Advertising", flags=["city_unknown"], rounds=[],
             note="Direct marketing and web commerce service on the firm's 2000 listing. The only later trace is a "
                  "Zeta Global 10-K naming an executive's earlier work at the startup Hotsocket; no source read says "
                  "what became of it, so its fate is not established. " + FIRM_YEAR.format(y=2000)))

# ---- InformationView Solutions
L.append(cls("informationview-solutions", status="unknown", rng="below_1b", stage="undetermined", entry_date="1995",
             country="US", focus="Data Infrastructure", flags=["city_unknown"], rounds=[],
             note="Billing reconciliation software for telecommunications carriers. Its chairman's term ran from "
                  "April 1995 to June 2000 (Performance Technologies proxy, 2001) and nothing later was found, so "
                  "its fate is not established. " + FIRM_YEAR.format(y=1995)))

# ---- ishoni Networks
L.append(cls("ishoni-networks", status="unknown", rng="below_1b", stage="undetermined", entry_date="1999",
             country="US", city="Santa Clara", city_src=WV, focus="Industrial & Robotics",
             rounds=[rnd("2002-02-13", "equity investment for a 51 percent interest", 25000000,
                         "Royal Philips Electronics", None, LR_ISHONI_PHILIPS, "company")],
             note="Broadband gateway chips and software, Santa Clara. Philips bought a 51 percent interest for $25 "
                  "million in February 2002, and in August 2003 the company was still run independently and "
                  "rebuilding after losing its Bangalore unit (Light Reading); nothing later was found, so its fate "
                  "is not established. " + FIRM_YEAR.format(y=1999)))

# ---- K2 Optronics
L.append(cls("k2-optronics", status="acquired", rng="below_1b", stage="Growth", stage_src=WV, stage_cite=LR_K2_29,
             stage_conf="high", entry_date="2001-03", country="US", city="Sunnyvale", city_src=WV,
             focus="Industrial & Robotics",
             rounds=[rnd("2000", "first round (no series named)", None, None, False, LR_K2_29, "company"),
                     rnd("2001-03-14", "second round", 29000000, "Bessemer Venture Partners", True, LR_K2_29,
                         "company")],
             note="Transmission lasers for fiber-optic networks, Sunnyvale. The company's release of 2001-03-14 says "
                  "Bessemer 'headed' the $29 million second round and lists the 'first-round financing participants' "
                  "separately without it, so the entry is the second round, which reads Growth. Acq. by Emcore, 2006 "
                  "(merger closed 2006-01-12, Emcore's release)."))

# ---- Knology
L.append(cls("knology", rng="below_1b", stage="Growth", stage_src=WV, stage_cite=KNOLOGY_CIRC, stage_conf="medium",
             entry_date="2000-02-07", city="West Point", city_src=WV, focus="Data Infrastructure",
             rounds=[rnd("2000-02-07", "Series B preferred", 100600000, None, True, KNOLOGY_CIRC, "filing")],
             note="Cable, telephone and internet provider in the Southeast, West Point, Georgia. Knology's 2002 "
                  "offering circular lists Bessemer Venture Partners V and Bessec Ventures V among the 'Series B "
                  "Investors' and dates that private placement to 2000-02-07 ($4.75 a share, about $100.6M); both "
                  "funds signed the January 2001 amendment to the stockholders agreement of that date (8-K). The "
                  "entry is the Series B, which reads Growth. Acq. by WideOpenWest, 2012 (Wikipedia)."))

assert len({x["slug"] for x in L}) == 22, len({x["slug"] for x in L})
for x in L:
    for k in ("note", "basis"):
        assert "—" not in (x.get(k) or "") and "–" not in (x.get(k) or ""), x["slug"]

jl.write("d1a", L)
