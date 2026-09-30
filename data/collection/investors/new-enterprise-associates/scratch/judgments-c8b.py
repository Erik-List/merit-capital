"""PRO-100 NEA, judge c8, queue batch 16 (playdom .. reneo-pharmaceuticals): listed members, classification only."""
import judge_lib as jl
from judge_lib import cls, rnd, SITE, ARCH, POST, W, FTS, NEWS

WV = {"valuation_range_source": "web_verified"}
CHECKED = "2026-09-30"


def cap(tk):
    return f"https://stockanalysis.com/stocks/{tk}/market-cap/"


def momentum(url):
    return {"valuation_range_source": "web_verified", "valuation_citation": url, "valuation_asof": CHECKED}


L = []

# ---- playdom (dispute: the known Pre-Seed reads an $851K 2010 Form D)
PD = "https://techcrunch.com/2009/11/11/exclusive-playdom-raises-a-huge-round-at-a-huge-valuation/"
L.append(cls("playdom", rng="below_1b", stage="Series A", stage_src="web_verified", stage_cite=PD, stage_conf="medium",
             entry_date="2009-11-11", city="Palo Alto", focus="Media, Gaming & Advertising", flags=["stage_disputes_band"],
             rounds=[rnd("2009-11-11", "Series A (first outside round)", 43000000,
                         lead="NEA; Lightspeed; Norwest; Rick Thompson", firm_in_round=True, source=PD,
                         source_type="press")],
             note="TechCrunch (2009-11-11): Playdom's first outside round, $43M from NEA, Rick Thompson, Lightspeed and "
                  "Norwest; the company had been self-funded, so NEA entered at the first institutional round (Series A, "
                  "as in the Lightspeed row). The known Pre-Seed read an $851K 2010 Form D and the firm's Growth label "
                  "describes the size, not the round. Disney bought Playdom in 2010. City aligned with the Lightspeed row."))

# ---- playvs
PV = POST("playvs")
L.append(cls("playvs", status="private", rng="below_1b", stage="Series A", stage_src="first_party", stage_cite=PV,
             stage_conf="high", entry_date="2018-06-03", country="US", city="Santa Monica",
             focus="Media, Gaming & Advertising",
             rounds=[rnd("2018-06-03", "Series A", None, lead="NEA", firm_in_round=True, source=PV, source_type="firm")],
             note="High school esports platform in Santa Monica (as in the Battery and Coatue rows). The firm's own post of "
                  "2018-06-03 announces NEA's Series A investment, and the firm dates its first investment 2018."))

# ---- pluribus-networks
L.append(cls("pluribus-networks", status="acquired", rng="below_1b", city="Santa Clara", focus="Data Infrastructure",
             note="Software-defined networking company acquired by Arista Networks in 2022 (the firm's exit line). Santa "
                  "Clara as in the Menlo row; its 2012 Form D gave Palo Alto."))

# ---- plusmo
PLU = NEWS("plusmo", "Krishna Vedati")
L.append(cls("plusmo", status="acquired", rng="below_1b", stage="undetermined", entry_date="2007", country="US",
             focus="Consumer & Marketplaces", flags=["city_unknown"],
             note="Mobile widget platform; its co-founder's biography (MediaNews4U, 2022-06-28) says AT&T acquired it in "
                  "2009, matching the firm's exit line, so acquired rather than the Felicis row's defunct (that row should "
                  "align). No source read placed its office. The record does not name NEA's 2007 round."))

# ---- pocket (collisions: the Accel and YC "Pocket" rows are other companies)
L.append(cls("pocket", status="acquired", rng="below_1b", stage="undetermined", entry_date="2014", country="US",
             city="San Francisco", focus="Consumer & Marketplaces",
             note="Pocket (formerly Read It Later), acquired by Mozilla on 2017-02-27 (Wikipedia). The record does not name "
                  "NEA's 2014 round. The Accel row (private, Industrial & Robotics) and the YC row are different companies "
                  "named Pocket."))

# ---- poggled
L.append(cls("poggled", status="unknown", rng="below_1b", city="Chicago", city_src="formd_address",
             focus="Consumer & Marketplaces",
             note="Chicago nightlife deals startup (2011 Form D with NEA's Thomas Grossi a director); listed by the firm "
                  "only on its 2013 page, and a news search found nothing on its later fate. Graduation left for the "
                  "graduation pass."))

# ---- polyserve
L.append(cls("polyserve", status="acquired", rng="below_1b", stage="undetermined", entry_date="2000", country="US",
             city="Beaverton", focus="Data Infrastructure",
             note="Clustered file and database software from the Portland area, acquired by Hewlett-Packard in 2007. City "
                  "aligned with the Greylock row. The record does not name NEA's 2000 round."))

# ---- popai
POP = NEWS("popai", "Popai Health Raises $11M")
L.append(cls("popai", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_cite=POP,
             stage_conf="high", entry_date="2025-11-03", grad="censored", country="US", city="New York",
             city_src="web_verified", focus="Healthcare & Bio",
             rounds=[rnd("2025-11-03", "Seed", 11000000, lead="Team8", firm_in_round=True, source=POP,
                         source_type="company")],
             note="Voice AI for patient conversations, headquartered in New York with R&D in Tel Aviv. Team8 led the $11M "
                  "seed with NEA (PR Newswire, 2025-11-03); the firm labels it Seed. Entry inside the 24-month window, "
                  "so censored."))

# ---- portauthority
L.append(cls("portauthority", status="acquired", rng="below_1b", stage="undetermined", entry_date="2006",
             country="US", city="San Carlos", focus="Security",
             note="Data-leak prevention vendor acquired by Websense in 2007 (the firm's exit line). Country and city "
                  "aligned with the Greylock row; the Sequoia row carries IL, where its R&D sat. The record does not name "
                  "NEA's 2006 round."))

# ---- pponext
L.append(cls("pponext", status="acquired", rng="below_1b", stage="undetermined", entry_date="1999", country="US",
             focus="Healthcare & Bio", flags=["city_unknown"],
             note="PPO network services company; the firm's exit line records its acquisition by Concentra. A news search "
                  "found nothing that places its office. The record does not name NEA's 1999 round."))

# ---- predictive-biosciences
L.append(cls("predictive-biosciences", status="defunct", rng="below_1b", stage="undetermined", entry_date="2008",
             city="Lexington", city_src="formd_address", focus="Healthcare & Bio",
             note="Cancer diagnostics company in Lexington, Massachusetts; no activity after 2012 and its own domain now "
                  "redirects to an unrelated patent site (the firm's company link), read as a shutdown (medium "
                  "confidence). The 2010 Form D is a later round; the record does not name NEA's 2008 entry."))

# ---- prime-financial-technologies
L.append(cls("prime-financial-technologies", status="private", rng="below_1b", stage="undetermined", entry_date="2021",
             country="US", focus="Fintech & Payments", flags=["city_unknown"],
             note="SMB lending platform for community banks, Scott Sandell on the board; the firm lists it private. Momentum "
                  "check 2026-09-30: two Google News searches found no round at all, so no $1B+ mark and no office; the "
                  "firm's 2021 year carries no round word."))

# ---- procket
L.append(cls("procket", status="acquired", rng="below_1b", stage="undetermined", entry_date="1999", country="US",
             city="Milpitas", focus="Data Infrastructure",
             note="Core router startup acquired by Cisco Systems in 2004 (the firm's exit line). The record does not name "
                  "NEA's 1999 round."))

# ---- progress-software
L.append(cls("progress-software", status="public", rng="1b_plus", usd=1650000000, val_src="web_verified",
             val_cite=cap("prgs"), asof="2026-09-30", stage="undetermined", city="Burlington",
             focus="DevTools & APIs", extra=WV,
             note="Nasdaq: PRGS; market cap $1.65B on 2026-09-30 (stockanalysis), fresher than the Sequoia row's $1.55B. "
                  "NEA's Arthur Marks had been a director since July 1987 (2001 proxy), before the 1991 IPO, so the firm's "
                  "1995 year is not the entry; no record names NEA's round, so the stage is undetermined."))

# ---- proof-of-learn
L.append(cls("proof-of-learn", status="private", rng="below_1b", stage="Seed", stage_src="first_party",
             stage_cite=ARCH("proof-of-learn"), stage_conf="medium", entry_date="2021", city="Pembroke",
             city_src="formd_address", focus="Crypto & Web3",
             note="Web3 learn-to-earn education platform founded by Sheila Marcelo, with NEA's Tony Florence a director "
                  "on its 2022 Form D. The firm's archived listing labels the 2021 entry Seed; it is off today's list. "
                  "Graduation left for the graduation pass."))

# ---- prosensa
L.append(cls("prosensa", status="acquired", rng="below_1b", city="Leiden", focus="Healthcare & Bio",
             note="Dutch RNA-modulation biotech (Nasdaq: RNA) acquired by BioMarin in January 2015."))

# ---- prospex-medical-iii-inc (D5 candidate)
L.append(cls("prospex-medical-iii-inc", status="unknown", rng="below_1b", city="White Bear Lake",
             city_src="formd_address", focus="Healthcare & Bio",
             note="A medical device incubator (the firm's own description), with NEA's Ali Behbahani and John Nehra on its "
                  "2011 Form D; D5 candidate, since an incubator is fund-shaped until an operating company is named. No "
                  "later filing or press. Graduation left for the graduation pass."))

# ---- prostor-systems-inc
L.append(cls("prostor-systems-inc", status="acquired", rng="below_1b", stage="undetermined", entry_date="2004",
             city="Boulder", focus="Data Infrastructure",
             note="RDX removable-disk storage company in Boulder; Imation bought the RDX line and Tandberg Data took the "
                  "company (the firm's exit lines). The 2010 Form D is a later round (the band was withheld against the "
                  "firm's 2004 year); the record does not name NEA's entry."))

# ---- proteostasis-therapeutics
PTI = FTS("PROTEOSTASIS", "S-1")
L.append(cls("proteostasis-therapeutics", stage="Series A", stage_src="web_verified", stage_cite=PTI,
             stage_conf="high", entry_date="2008-08-15", country="US", city="Boston", focus="Healthcare & Bio",
             rng="below_1b",
             rounds=[rnd("2008-08-15", "Series A", 1096111, lead="HealthCare Ventures", firm_in_round=True, source=PTI,
                         source_type="filing"),
                     rnd("2015-09-02", "Series B", 22000000, lead=None, firm_in_round=True, source=PTI,
                         source_type="filing")],
             note="The 2015 S-1's related-party tables show New Enterprise Associates 12 buying Series A preferred at $1.00 "
                  "from 2008-08-15 (HealthCare Ventures had opened the round in 2007) and Series B in 2015. Merged into "
                  "Yumanity in 2020."))

# ---- proxima-therapeutics
L.append(cls("proxima-therapeutics", status="acquired", rng="below_1b", stage="undetermined", entry_date="1998",
             country="US", city="Alpharetta", focus="Healthcare & Bio",
             note="MammoSite brachytherapy maker acquired by Cytyc in 2005 (the firm's exit line). The record does not name "
                  "NEA's 1998 round."))

# ---- psikick-inc (the same company as the everactive row: CIK 1562446)
L.append(cls("psikick-inc", status="private", rng="below_1b", stage="undetermined", entry_date="2014",
             city="Santa Clara", city_src="formd_address", focus="Industrial & Robotics",
             note="PsiKick renamed itself Everactive (the firm's Everactive page says fka Psikick) and files under the same "
                  "CIK 1562446, so this row and the everactive row are one company. Batteryless wireless sensors, Santa "
                  "Clara on its 2018 Form D. The record does not name NEA's 2014 round."))

# ---- psyadon-pharmaceuticals
L.append(cls("psyadon-pharmaceuticals", status="acquired", rng="below_1b", stage="undetermined", entry_date="2004",
             country="US", city="Germantown", focus="Healthcare & Bio",
             note="Ecopipam developer for Tourette syndrome; the firm's exit line records its acquisition by Emalex "
                  "Biosciences. The record does not name NEA's 2004 round."))

# ---- pulse (dispute: the BG country is a one-word Wikidata join)
PULSE = "https://www.telecompaper.com/news/pulse-raises-usd-9-mln-in-funding--810265"
L.append(cls("pulse", rng="below_1b", stage="Series A", stage_src="web_verified", stage_cite=PULSE, stage_conf="high",
             entry_date="2011-06", country="US", city="San Francisco", focus="Media, Gaming & Advertising",
             flags=["model_disputes_source"],
             rounds=[rnd("2011-06", "Series A", 9000000, lead="NEA", firm_in_round=True, source=PULSE,
                         source_type="press")],
             note="Pulse news reader (Alphonso Labs): NEA, Greycroft and Lerer Ventures put $9M into its June 2011 Series A, "
                  "with NEA's Patrick Chung joining the board (Telecompaper); the firm dates its entry 2011. LinkedIn "
                  "bought it in 2013 for about $90M. Country US, not BG: the BG code is a Wikidata join on the word "
                  "Pulse (the Lightspeed and Redpoint rows carry the same error). City as in the Lightspeed row; Headline "
                  "has Palo Alto, where it started."))

# ---- pulumi
L.append(cls("pulumi", status="private", rng="below_1b", city="Seattle", city_src="formd_address",
             focus="DevTools & APIs",
             note="Infrastructure-as-code company in Seattle. No $1B+ priced round on record."))

# ---- pure-energies
PURE = NEWS("pure-energies", "NRG buys Toronto-based")
L.append(cls("pure-energies", status="acquired", rng="below_1b", stage="undetermined", entry_date="2012",
             country="CA", country_src="web_verified", country_cite=PURE, city="Toronto", focus="Climate & Energy",
             note="Residential solar installer bought by NRG Energy in October 2014; CBC's headline calls it Toronto-based. "
                  "The record does not name NEA's 2012 round."))

# ---- pyxis
L.append(cls("pyxis", status="acquired", rng="below_1b", stage="undetermined", entry_date="1988", country="US",
             city="San Diego", focus="Healthcare & Bio",
             note="Automated medication dispensing company (Nasdaq: PYXS) acquired by Cardinal Health in 1996; city as in "
                  "the Menlo and Sutter Hill rows. The record does not name NEA's round."))

# ---- qadium (the same company as the expanse row: CIK 1642992)
L.append(cls("qadium", status="acquired", rng="below_1b", stage="Series A", stage_src="model", stage_conf="medium",
             entry_date="2016", city="San Francisco", city_src="formd_address", focus="Security",
             rounds=[rnd("2016-06-05", "Unnamed", 20000000, lead=None, firm_in_round=True,
                         source=NEWS("qadium", "DARPA Darlings"), source_type="press"),
                     rnd("2017-08-31", "Series B", 40000000, lead=None, firm_in_round=None,
                         source=NEWS("qadium", "Ex-CIA Agent Raises"), source_type="press")],
             note="Qadium renamed itself Expanse (the firm's Expanse page says formerly Qadium) and files under the same CIK "
                  "1642992, so this row and the expanse row are one company; Palo Alto Networks bought it in 2020. NEA "
                  "(Scott Sandell a director on the 2016 Form D) entered at the $20M round of June 2016 (Forbes headline), "
                  "which the $40M Series B of 2017 makes the Series A; medium confidence."))

# ---- qpex-biopharma
QPEX = NEWS("qpex-biopharma", "Announces Closing of $33 Million")
L.append(cls("qpex-biopharma", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified",
             stage_cite=QPEX, stage_conf="high", entry_date="2018-10-22", country="US", city="San Diego",
             city_src="web_verified", focus="Healthcare & Bio",
             rounds=[rnd("2018-10-22", "Series A", 33000000, lead="NEA", firm_in_round=True, source=QPEX,
                         source_type="company")],
             note="NEA led Qpex's $33M Series A at its October 2018 launch (San Diego dateline). Shionogi acquired it in "
                  "2023 for about $140M upfront."))

# ---- quadramed-corporation
L.append(cls("quadramed-corporation", status="acquired", rng="below_1b", stage="undetermined", country="US",
             city="Reston", focus="Healthcare & Bio",
             note="Healthcare information software company, listed in 1996 (NEA filed 13Gs in 1997-98) and taken private by "
                  "Francisco Partners in 2010. The record does not name NEA's entry round."))

# ---- qualified-health
QH = NEWS("qualified-health", "Raises $125M Series B to Meet")
L.append(cls("qualified-health", status="private", rng="below_1b", stage="Growth", stage_src="web_verified",
             stage_cite=QH, stage_conf="high", entry_date="2026-03-25", country="US", city="Palo Alto",
             city_src="web_verified", focus="Healthcare & Bio",
             rounds=[rnd("2025-01-08", "Seed", 30000000, lead=None, firm_in_round=None,
                         source=NEWS("qualified-health", "Launches with $30M Seed"), source_type="company"),
                     rnd("2026-03-25", "Series B", 125000000, lead="NEA", firm_in_round=True, source=QH,
                         source_type="company")],
             note="NEA led the $125M Series B of 2026-03-25 (PR Newswire, Palo Alto dateline), its first investment (the "
                  "firm dates it 2026). Valuation not disclosed. The Menlo row carries San Francisco; the company's own "
                  "release is the fresher source."))

# ---- quantum-bridge-communications
L.append(cls("quantum-bridge-communications", status="acquired", rng="below_1b", stage="undetermined",
             entry_date="1998", country="US", city="Andover", focus="Data Infrastructure",
             note="Optical access equipment maker acquired by Motorola in 2004 (the firm's exit line). The record does not "
                  "name NEA's 1998 round."))

# ---- quidsi-diapers-com
L.append(cls("quidsi-diapers-com", status="acquired", rng="below_1b", country="US", city="Jersey City",
             focus="Consumer & Marketplaces",
             note="Parent of Diapers.com, headquartered at Exchange Place in Jersey City (Wikipedia); acquired by Amazon in "
                  "2011."))

# ---- quotewell
QW = NEWS("quotewell", "Comes Out of Stealth")
QW2 = NEWS("quotewell", "Secures Additional $12 Million")
L.append(cls("quotewell", status="private", rng="below_1b", stage="Seed", stage_src="first_party",
             stage_cite=SITE("quotewell"), stage_conf="medium", entry_date="2022", grad="graduated",
             grad_src="web_verified", grad_cite=QW, grad_conf="medium", grad_asof=CHECKED, country="US",
             city="Austin", city_src="web_verified", focus="Fintech & Payments", extra=momentum(QW2),
             rounds=[rnd("2023-10-25", "Series A", 15000000, lead="NEA", firm_in_round=True, source=QW,
                         source_type="press"),
                     rnd("2025-10-08", "Unnamed", 12000000, lead="NEA", firm_in_round=True, source=QW2,
                         source_type="company")],
             note="Commercial insurance wholesale brokerage founded in 2021, Austin dateline. The firm labels its 2022 entry "
                  "Seed; NEA then led the $15M Series A announced as it left stealth on 2023-10-25 (Insurance Journal), a "
                  "later named round, and the $12M of October 2025 (total raised $32M, which leaves room for the earlier "
                  "seed). Momentum check 2026-09-30: no $1B+ priced round, valuation undisclosed."))

# ---- ra-pharmaceuticals
L.append(cls("ra-pharmaceuticals", rng="below_1b", city="Cambridge", focus="Healthcare & Bio",
             note="Ra Pharma (Nasdaq: RARX) was acquired by UCB in 2020, so no figure is carried."))

# ---- radiology-partners
RP = NEWS("radiology-partners", "NEA-Founded Radiology Startup")
L.append(cls("radiology-partners", status="private", rng="1b_plus", usd=4000000000, val_src="web_verified",
             val_cite=RP, asof="2019-07-18", city="El Segundo", focus="Healthcare & Bio",
             flags=["stale"], extra=WV,
             note="NEA-founded national radiology practice. WSJ headline of 2019-07-18: the NEA-founded startup hit a $4B "
                  "valuation (paywalled; the figure is in the headline). The $720M growth equity of February 2024 "
                  "disclosed no valuation, so the 2019 mark stands, stale. El Segundo (its 2017 Form D); its 2026 Form D "
                  "gives a Nashville address, which may mark a move."))

# ---- raise
L.append(cls("raise", status="private", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2014", city="Chicago", focus="Fintech & Payments",
             rounds=[rnd("2013", "Unnamed", 18000000, lead="Bessemer", firm_in_round=False, source=W("Raise.com"),
                         source_type="press"),
                     rnd("2015", "Unnamed", 56000000, lead="NEA", firm_in_round=True, source=W("Raise.com"),
                         source_type="press")],
             note="Gift card marketplace in Chicago (Wikipedia; its 2016 Form D). Wikipedia: $18M from Bessemer at the 2013 "
                  "launch, then $56M from NEA, which the firm dates 2014 and archived as growth: a round after the "
                  "company's first institutional one, so Growth. It raised $63M in February 2025 with no valuation "
                  "disclosed."))

# ---- ravel
RAV = "https://venturebeat.com/entrepreneur/ravel-law-raises-8m-to-help-lawyers-gather-data-and-cut-costs-in-a-new-way-exclusive"
L.append(cls("ravel", status="acquired", rng="below_1b", stage="Seed", stage_src="model", stage_conf="low",
             entry_date="2012", grad="graduated", grad_src="web_verified", grad_cite=RAV, grad_conf="high",
             grad_asof=CHECKED, country="US", city="San Francisco", city_src="web_verified", focus="SaaS",
             flags=["stage_uncited"],
             rounds=[rnd("2012-07", "Seed", 1100000, lead=None, firm_in_round=None,
                         source="https://pitchbook.com/profiles/company/56304-19", source_type="vendor"),
                     rnd("2014-02-03", "Series A", 8100000, lead="NEA", firm_in_round=True, source=RAV,
                         source_type="press")],
             note="Legal research analytics, San Francisco (ABA Journal on the June 2017 LexisNexis acquisition). The firm "
                  "dates its first investment 2012, the year of the $1.1M seed (vendor record only, so the stage is "
                  "uncited); NEA then led the $8.1M Series A of 2014-02-03 (VentureBeat), which graduates the seed."))

# ---- recludix-pharma
REC = NEWS("recludix-pharma", "launches Recludix with $60M")
L.append(cls("recludix-pharma", status="private", rng="below_1b", stage="undetermined", entry_date="2019",
             country="US", city="San Diego", focus="Healthcare & Bio",
             rounds=[rnd("2021-11-15", "Series A", 60000000, lead=None, firm_in_round=True, source=REC,
                         source_type="press")],
             note="STAT inhibitor biotech; it came out of stealth in November 2021 with a $60M Series A from NEA, Westlake "
                  "Village BioPartners and Access Industries (Fierce Biotech). The firm dates its first investment 2019, "
                  "before that announcement, so the round NEA entered is not named. Sanofi licensed its STAT6 program in "
                  "2023."))

# ---- red-ridge-bio
RR = "https://redridgebio.com/"
L.append(cls("red-ridge-bio", status="private", rng="below_1b", stage="undetermined", entry_date="2023",
             country="CH", country_src="web_verified", country_cite=RR, city="Basel", city_src="web_verified",
             focus="Healthcare & Bio",
             note="Cancer and autoimmune biotech with its registered office, lab and offices in Basel and US offices in San "
                  "Francisco and Cambridge (its own site); Versant's Alex Mayweg chairs it and NEA's Ali Behbahani sits on "
                  "the board. Pierre Fabre joined its Series A in March 2025; the firm dates its own entry 2023 and the "
                  "record does not name that round."))

# ---- redbaby
L.append(cls("redbaby", status="acquired", rng="below_1b", stage="undetermined", entry_date="2006", country="CN",
             country_src="web_verified", country_cite=SITE("redbaby"), city="Beijing", focus="Consumer & Marketplaces",
             note="Chinese online baby-products retailer (the firm's own page: China's largest multi-channel direct "
                  "marketer), from NEA's China desk; Suning bought it in 2012, so the firm's private status is stale. The "
                  "record does not name NEA's 2006 round."))

# ---- regression-games
RG = NEWS("regression-games", "Just-launched esports startup")
L.append(cls("regression-games", status="private", rng="below_1b", stage="Seed", stage_src="web_verified",
             stage_cite=RG, stage_conf="high", entry_date="2022-08-17", country="US", city="Philadelphia",
             city_src="web_verified", focus="Media, Gaming & Advertising",
             rounds=[rnd("2022-08-17", "Seed", 4200000, lead="NEA", firm_in_round=True, source=RG, source_type="press")],
             note="AI agents for game testing, Philadelphia area. NEA led the $4.2M seed with a16z (Technical.ly, "
                  "2022-08-17); the firm labels it Seed. Graduation left for the graduation pass."))

# ---- regulus-therapeutics
L.append(cls("regulus-therapeutics", rng="below_1b", city="San Diego", focus="Healthcare & Bio",
             note="Regulus (Nasdaq: RGLS) was acquired by Novartis in 2025, so no figure is carried. X1 note: the firm "
                  "labels its 2017 entry Public/PIPES, years after the 2012 IPO."))

# ---- relievant-medsystems
L.append(cls("relievant-medsystems", status="acquired", rng="below_1b", stage="undetermined", entry_date="2012",
             city="Edina", city_src="formd_address", focus="Healthcare & Bio",
             note="Intracept basivertebral nerve ablation maker in Edina, acquired by Boston Scientific for $850M upfront, "
                  "closed November 2023 (Star Tribune; MassDevice). Edina also on its 2023 Form D. The 2015 Form D is a later round (the band was withheld against the "
                  "firm's 2012 year); the record does not name NEA's entry."))

# ---- reltio
REL_DONE = NEWS("reltio", "SAP Completes Acquisition of Reltio")
REL_A = NEWS("reltio", "Reltio Raises $10M Series A")
L.append(cls("reltio", status="acquired", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2016-07-15", city="Redwood City", focus="Data Infrastructure",
             rounds=[rnd("2015-03-16", "Series A", 10000000, lead=None, firm_in_round=False, source=REL_A,
                         source_type="company"),
                     rnd("2016-07-15", "Unnamed (Form D)", 22344210, lead=None, firm_in_round=True,
                         source=jl.FORMD_CITE("reltio", 1), source_type="filing"),
                     rnd("2021-11-05", "Unnamed", 120000000, lead=None, firm_in_round=None,
                         source="https://www.techtarget.com/data-technologies/news/252509158/Reltio-advances-master-data-management-with-120M-fund-raise",
                         source_type="press")],
             note="Master data management company in Redwood City. SAP announced its purchase on 2026-03-27 and completed "
                  "it on 2026-05-07 (SAP News Center), price undisclosed, so no figure; the $120M round of 2021 had valued "
                  "it at $1.7B. Reltio's Series A was the $10M of March 2015; NEA's first investment is the 2016 round "
                  "(Chetan Puttagunta a director on its Form D), a later round, so Growth."))

# ---- reneo-pharmaceuticals (the same issuer as onkure-therapeutics-inc: CIK 1637715)
RENEO = "https://www.sec.gov/Archives/edgar/data/1637715/000119312521087741/d63585ds1.htm"
L.append(cls("reneo-pharmaceuticals", stage="Series A", stage_src="web_verified", stage_cite=RENEO, stage_conf="high",
             entry_date="2015", country="US", city="Boulder", focus="Healthcare & Bio",
             note="Reneo's 2021 S-1 lists Series A convertible preferred bought by New Enterprise Associates 15 (plus Series "
                  "B), and the firm dates its first investment 2015, the Series A. In 2024 Reneo merged with OnKure and "
                  "took its name (Nasdaq: OKUR), now based in Boulder; the onkure-therapeutics-inc row is the same issuer "
                  "(CIK 1637715)."))


jl.write("c8b", L)
