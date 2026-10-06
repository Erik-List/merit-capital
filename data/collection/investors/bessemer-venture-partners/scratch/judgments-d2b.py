import judge_lib as jl
from judge_lib import cls, rnd, verdict, ARCH

L = []


def A(*a, **k):
    L.append(cls(*a, **k))


B1 = "below_1b"
U = "undetermined"
LR = "https://www.lightreading.com"
FIRST_LISTED = "Entry date is the first year the firm listed it ({y}), an upper bound and not an investment year; no round named."

# citations: printed by a tool in this session and read, or SEC URLs built from accessions EDGAR printed
MANG_SEED = LR + "/business-management/reeves-seeds-mangrove-systems"
MANG_20 = LR + "/business-management/mangrove-systems-gets-20m"
NANO_1 = LR + "/cable-technology/nanoopto-thinks-small"
SAND_2 = LR + "/business-management/sandbridge-draws-22-5m"
STAR_3 = LR + "/business-management/stargen-generates-15m"
TELE = "https://www.lightwaveonline.com/business/article/16660481/telephotonics-inc-opens-wafer-fabrication-facility"
RBJ = "https://rbj.net/2001/05/11/new-name-marks-transformation-of-software-firm"
DIVINE = "https://www.sec.gov/Archives/edgar/data/1097516/000095013101500496/d10k405.txt"

A("mangrove-systems", status="acquired", rng=B1, stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=MANG_SEED,
  entry_date="2002-06", grad="graduated", grad_src="web_verified", grad_cite=MANG_20, grad_conf="high",
  country="US", city="Wallingford", city_src="web_verified", focus="Data Infrastructure",
  rounds=[rnd("2002-06", "Seed", 3100000, None, True, MANG_SEED, "press"),
          rnd("2003-04-15", "Later round", 20000000, None, True, MANG_20, "press")],
  note="Light Reading (2002-06-24): $3.1M in seed money from the founders and Bessemer, a month after the company opened in Wallingford, "
       "Connecticut. On 2003-04-15 it announced over $20M from Bessemer, Highland, Columbia Capital and Silicon Valley Bank, a later priced round "
       "well over twice the seed, which graduates the row. Carrier Access bought its product assets for about $8M and hired 30 of its staff on "
       "2007-03-05 (Carrier Access's 8-K), so acquired.")

A("metratech", status="acquired", rng=B1, stage=U, entry_date="1998", country="US", city="Waltham", city_src="formd_address", focus="SaaS",
  rounds=[],
  note="Billing software company. Ericsson announced the purchase on 2014-07-29 and reported it among the acquisitions made in the third quarter "
       "of 2014 (its 6-K). Waltham is the address on the company's own Form D of 2012; Ericsson's announcement says Boston. Entry year is the "
       "firm's own (1998); no round named.")

A("morphics-technology", status="acquired", rng=B1, stage=U, entry_date="2002", country="US", city="Campbell", city_src="web_verified",
  focus="Industrial & Robotics", rounds=[],
  note="Reconfigurable signal processing chips for 3G handsets (Campbell, California). Infineon agreed in March 2003 to buy its assets and "
       "completed the purchase of the net assets in April 2003 (Infineon's 6-K), so acquired. " + FIRST_LISTED.format(y=2002))

A("nanoopto", status="acquired", rng=B1, stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=NANO_1,
  entry_date="2001-10", country="US", city="Somerset", city_src="formd_address", focus="Industrial & Robotics",
  rounds=[rnd("2001-10", "Series A-1", 16000000, "Bessemer Venture Partners; Morgenthaler Ventures; New Enterprise Associates", True, NANO_1, "press")],
  note="Light Reading (2001-12-03): a $16M first round from Bessemer, Morgenthaler and NEA. A co-investor's SEC filings carry the same purchase "
       "as Series A-1 preferred bought in October 2001 and name Bessemer beside it, so the round is read as the Series A. API Nanotronics bought "
       "the company's assets in July 2007 (its proxy statement), so acquired; Somerset, New Jersey.")

A("newview-technologies", status="unknown", rng=B1, stage=U, entry_date="1998", country="US", city="New York", focus="SaaS",
  flags=["identity_conflated"], rounds=[],
  note="The firm's own text says NewView Technologies is the former e-STEEL Corporation, so this row and e-steel are one company (New York, "
       "from memory). A general counsel's biography shows it still privately held in February 2003; no source read says what became of it. "
       "Entry year is the firm's own on the e-Steel listing (1998); no round named.")

A("nte", status="unknown", rng=B1, stage=U, entry_date="1997", country="US", city="Downers Grove", city_src="formd_address",
  focus="Consumer & Marketplaces",
  rounds=[rnd("1999-10-29", "undetermined", None, None, None, DIVINE, "filing")],
  note="Freight capacity exchange (NTE, formerly The National Transportation Exchange), Downers Grove, Illinois per its Form D of May 2002. "
       "An officer's biography shows it operating into 2002; no source read says what became of it. Entry year is the firm's own (1997); the "
       "only financing on record is another investor's purchase of October 1999, so no round named.")

A("optigrab-com", status="acquired", rng=B1, stage=U, entry_date="2000", country="US", city="Cambridge", focus="Data Infrastructure",
  flags=["identity_conflated"], rounds=[],
  note="Endeca was founded in 1999 as Optigrab (Wikipedia), so this row and endeca are one company, and the answers follow that row: acquired "
       "by Oracle in 2011, Cambridge, Massachusetts. Entry year is the firm's own (2000; the endeca row carries the firm's date 2000-02-24); "
       "no round named.")

A("pacific-microsonics", status="acquired", rng=B1, stage=U, country="US", city="Berkeley", city_src="web_verified",
  focus="Media, Gaming & Advertising", rounds=[],
  note="Developer of the HDCD audio process (Berkeley, California); Microsoft acquired the company and its intellectual property in 2000 "
       "(Wikipedia, and the firm's own listing). The firm first listed it in 2004 as a past exit, so the listing year says nothing about the entry "
       "and no entry date is written; no round named.")

A("perfect-commerce", status="acquired", rng=B1, stage=U, entry_date="2000", country="US", city="Palo Alto", city_src="formd_address",
  focus="SaaS", rounds=[],
  note="Procurement software company founded by Marc Porat in 1998 (Palo Alto address on its Form D filings to 2006). It took over Commerce One "
       "in 2006 and was itself acquired by Proactis in July 2017 for $132.5M (Wikipedia, Commerce One). Entry year is the firm's own (2000); "
       "no round named.")

A("productopia", status="defunct", rng=B1, stage=U, entry_date="2000", country="US", city="San Francisco", city_src="web_verified",
  focus="Consumer & Marketplaces", rounds=[],
  note="Consumer product advice site (San Francisco). ABC News (2000-12-04) reports that it shut down in October 2000 after its funding was cut "
       "off, with about 60 staff laid off. Entry year is the firm's own (2000); no round named.")

A("qiva", status="acquired", rng=B1, stage=U, entry_date="2000", country="US", city="San Francisco", city_src="formd_address", focus="SaaS",
  rounds=[],
  note="Supply chain execution software (San Francisco, per Qiva Holdings' Form D filings of 2002). A former director's biography in a 10-K "
       "lists it as acquired by TradeBeam; the date was not found. Entry year is the firm's own (2000); no round named.")

A("revivio", rng=B1, stage=U, entry_date="2003", city="Lexington", city_src="formd_address", focus="Data Infrastructure", rounds=[],
  note="Continuous data protection company founded in 2001 (Lexington, Massachusetts); Symantec bought it on 2006-12-07 for $20M (Wikipedia). "
       "Entry date is the first year the firm listed it (2003); no round named.")

A("sandbridge-technologies", status="acquired", rng=B1, stage=U, entry_date="2002", country="US", city="White Plains", city_src="web_verified",
  focus="Industrial & Robotics",
  rounds=[rnd("2003-06-30", "Second round", 22500000, None, True, SAND_2, "press")],
  note="Baseband processor designer (fka NetDSP; White Plains, New York). EE Times (2010-11-03) carries an analyst's account that Qualcomm bought "
       "it for about $55M, mainly for its patents and without an announcement, so acquired. Bessemer was an existing investor at the $22.5M second "
       "round of June 2003 ($14M raised before it), but no source calls the first round a Series A. " + FIRST_LISTED.format(y=2002))

A("sequation", status="unknown", rng=B1, stage=U, entry_date="2000", country="US", city="Vienna", city_src="formd_address", focus="Security",
  rounds=[],
  note="Security management software (fka HyperNOC), Vienna, Virginia per its Form D filings, the last in September 2005. No source read says "
       "what became of it. Entry year is the firm's own (2000); no round named.")

A("silicon-valley-solar", status="unknown", rng=B1, stage=U, entry_date="2007", country="US", city="Santa Clara", city_src="formd_address",
  focus="Climate & Energy", rounds=[],
  note="Maker of flat-plate concentrator solar modules, Santa Clara (its Form D of June 2007). The firm listed it only in 2007 and no source read "
       "says what became of it. Entry date is the year of that listing and filing (2007); no round named.")

A("stargen", status="acquired", rng=B1, stage=U, entry_date="2002", country="US", city="Marlborough", city_src="web_verified",
  focus="Industrial & Robotics",
  rounds=[rnd("1999-07", "Seed", 6000000, None, None, STAR_3, "press"),
          rnd("2000-07", "Series B", 20000000, None, None, STAR_3, "press"),
          rnd("2003-06-16", "Third round", 15000000, None, None, STAR_3, "press")],
  note="Fabless interconnect chip maker (Marlborough, Massachusetts); Dolphin Interconnect Solutions acquired it in early 2007, its holders taking "
       "about 22% of the combined company (Wikipedia). Light Reading (2003-06-16) lists a $6M seed (July 1999), a $20M Series B (July 2000) and a "
       "$15M third round whose investor list omits Bessemer; no source says which round the firm entered. " + FIRST_LISTED.format(y=2002))

A("telephotonics", status="unknown", rng=B1, stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=TELE,
  entry_date="2000", country="US", city="Wilmington", city_src="web_verified", focus="Industrial & Robotics",
  rounds=[rnd("2000", "Series A", 18000000, None, True, TELE, "press")],
  note="Lightwave (2001-02-14): founded in March 2000 in Wilmington, Massachusetts, with about $18M of Series A financing from Atlas Venture, "
       "Bessemer and Blue Chip; the round is undated between the founding and the article and is read as 2000. Its chief executive left in 2003, "
       "the year DuPont set up DuPont Photonics Technologies in the same town, but no page read states a purchase, so the status is unknown.")

A("trellix", status="acquired", rng=B1, stage=U, entry_date="2002", city="Concord", focus="SaaS", rounds=[],
  note="Web site publishing software company founded by Dan Bricklin in 1995 (Concord, Massachusetts, from memory); Interland bought it in 2003 "
       "(Wikipedia, Dan Bricklin). " + FIRST_LISTED.format(y=2002))

A("vibrant-solutions", status="acquired", rng=B1, stage=U, entry_date="1995", country="US", city="Fairfax", city_src="formd_address",
  focus="SaaS", flags=["identity_conflated"],
  rounds=[rnd("2000", "undetermined", 15000000, None, True, RBJ, "press")],
  note="EDGAR carries Vibrant Solutions as the renamed Information View Solutions Corp, so this row and informationview-solutions are one "
       "company (Fairfax, Virginia). The Rochester Business Journal (2001-05-11) names Columbia Capital and Bessemer as its backers, with $15M "
       "raised in summer 2000; TEOCO acquired it in 2006 (an industry profile of TEOCO). Entry year is the firm's own on the InformationView "
       "listing (1995); no round named.")

L.append(verdict("voyant-technologies", "not_member",
                 "Sale consideration (Erik 2026-09-22, decisions.md R6): the firm's own listing says Voyant acquired BVP's portfolio company Octave "
                 "Communications in 2002 and merged with Polycom the following year. The position in Voyant is what the firm received for Octave "
                 "Communications, which is its own row (octave-communications); no source read shows a Bessemer round in Voyant before that.",
                 ec="site_listing", conf="high", cite=ARCH("voyant-technologies")))

A("xcelerate", status="unknown", rng=B1, stage=U, entry_date="2000", country="US", city="Fort Lauderdale", focus="SaaS", rounds=[],
  note="E-business services firm. EDGAR carries an Xcelerate Corp in Fort Lauderdale, Florida with a Form D of March 2002, read as this company "
       "on the name, the era and memory; no source read ties Bessemer to it, so the city is low confidence. No source read says what became of "
       "it. Entry year is the firm's own (2000); no round named.")

jl.write("d2b", L)
