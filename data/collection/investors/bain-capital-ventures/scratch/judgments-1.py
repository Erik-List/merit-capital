"""PRO-162 grind, batch-001 (6sense .. cofactr). Evidence: scratch/evidence-pack.json (the live CMS row,
the 2002-2022 archive rows, the firm's own posts), scratch/news-sweep.json + news-extra.json (Google News
headlines, decoded through judge_lib.NEWS), sources/edgar/fts-hits.json (IPO filings naming BCV funds),
Wikipedia sentences from the insource sweep, and articles fetched 2026-09-27 where quoted.
Seed graduations that need the absence test are left open for the graduation pass."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd, POST, SITE, W, NEWS = jl.cls, jl.verdict, jl.rnd, jl.POST, jl.SITE, jl.W, jl.NEWS
AS = "2026-09-27"
L = []
SEC = "https://www.sec.gov/Archives/edgar/data/"


def site_stage(slug):
    """first_party stage from the firm's own listing (decisions.md R2, medium)."""
    return dict(stage_src="first_party", stage_conf="medium", stage_cite=SITE(slug))


# ---------------------------------------------------------------- membership + classification
L.append(cls("6sense", city="San Francisco", stage="undetermined", focus="SaaS",
    usd=5200000000, val_src="web_verified", asof="2022-01-20",
    val_cite=NEWS("6sense", "Series E Round"), extra={"valuation_range_source": "web_verified"},
    flags=["stale", "model_disputes_source"],
    note="B2B revenue platform. BCV's own listing gives 2015 (Ajay Agarwal) and 'Early', an anchor that names no round; "
         "no source ties BCV to a named 2015 round, so the stage is undetermined. Mark: the $200M Series E of Jan 2022 at $5.2B "
         "(PR Newswire), fresher than the prefilled $2.1B Series D (2021); no later priced round, stale beyond 24 months."))

L.append(cls("ability-network-inovalon", status="acquired", rng="below_1b", city="Minneapolis", focus="Healthcare & Bio",
    note="Healthcare IT network (Minneapolis). Acquired by Inovalon in 2018 (the firm's listing: 'ABILITY Network (Inovalon)', Acquired). "
         "BCV's 2011 entry (Jeff Crisan on the Form D) is prefilled from the filings."))

L.append(cls("ableto", status="acquired", rng="below_1b", city="New York", focus="Healthcare & Bio",
    stage="Growth", **site_stage("ableto"), entry_date="2018-06",
    note="Virtual behavioral-health provider. Acquired by UnitedHealth's Optum in 2020 for about $470M (CNBC, "
         + NEWS("ableto", "advanced talks") + "). BCV entered in 2018 (Yumin Choi's Form D, 2018-06-06); the firm's listing tags the entry Growth; "
         "AbleTo had raised since 2008, so the 2018 round was a later-stage one."))

L.append(cls("accelecare", status="acquired", rng="below_1b", city="Bellevue", focus="Healthcare & Bio",
    note="Wound-care centre operator (Bellevue, WA per the firm's 2010 listing; the 2013 Form D gives Denver). Acquired by Healogics "
         "(the firm's archived listing: 'Acquired by Healogics')."))

L.append(cls("acorns", city="Irvine", stage="undetermined", focus="Fintech & Payments",
    usd=1900000000, val_src="web_verified", asof="2022-03-09",
    val_cite=NEWS("acorns", "1.9 billion valuation"), extra={"valuation_range_source": "web_verified"},
    flags=["stale", "model_disputes_source"],
    note="Micro-investing app (Irvine). BCV's listing gives 2017 and 'Early' (an anchor); no source names the round BCV entered. "
         "Mark: the $300M private round of March 2022 at $1.9B after the scrapped SPAC (CNBC), replacing the prefilled $2.2B SPAC "
         "valuation that never closed; stale beyond 24 months."))

L.append(cls("acv", status="public", country="US", country_src="model_knowledge", city="Buffalo", focus="Consumer & Marketplaces",
    stage="Growth", stage_src="model", stage_conf="medium", flags=["cite_pending"],
    note="Wholesale used-car auction marketplace (Buffalo), IPO March 2021 (NASDAQ: ACVA). BCV's funds are Bain Capital Venture Fund 2019 "
         "and BCV 2019-MD Primary (ACV's investors' rights agreement, S-1 exhibit 10.1, "
         + SEC + "1637873/000119312521060598/d34258dex101.htm), so BCV entered after the February 2018 $31M Series C, which Bessemer, Tribeca, "
         "SoftBank NY and Armory Square led without BCV (" + NEWS("acv", "Series C funding") + "): a Growth entry. Market cap to be pinned in the A/B pass."))

L.append(cls("adready-cpxi", status="acquired", rng="below_1b", city="Seattle", focus="Media, Gaming & Advertising",
    stage="undetermined",
    note="Display-ad platform (Seattle), later part of CPXi / Digital Remedy (the firm's listing: Acquired). BCV's 2007 listing year "
         "predates the first Form D the filings tie to Ajay Agarwal (2010-04, $5.3M), so the band is withheld and no source names BCV's 2007 round."))

L.append(cls("airbase", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="Fintech & Payments", stage="Seed", **site_stage("airbase"), entry_date="2017",
    grad="graduated", grad_src="first_party", grad_cite=POST("show-me-the-receipts"), grad_conf="high",
    note="Spend-management platform (San Francisco), acquired by Paylocity in 2024. BCV's listing: 2017, Seed; the firm then led the "
         "2020 Series A ('Bain Capital Ventures led the Series A funding round in Airbase', its own post), which graduates the seed.",
    rounds=[rnd("2020-05", "Series A", None, "Bain Capital Ventures", True, POST("show-me-the-receipts"), "firm"),
            rnd("2021-06", "Series B", 60000000, "Menlo Ventures", True, POST("ahead-of-projections"), "firm")]))

L.append(cls("airside", city="Herndon", rng="below_1b", focus="Security",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=POST("digitizing-identity"), entry_date="2017",
    grad="graduated", grad_src="first_party", grad_cite=POST("digitizing-identity"), grad_conf="high",
    note="Digital identity app (Herndon, VA). 'We had recently invested at the seed stage in a company called Airside' and BCV then "
         "led the $13M Series B (the firm's post, 2020-11-11). Acquired by Onfido in 2023 ("
         + NEWS("airside", "acquired by London") + "); the prefilled status stands.",
    rounds=[rnd("2020-11", "Series B", 13000000, "Bain Capital Ventures", True, POST("digitizing-identity"), "firm")]))

L.append(cls("aleph", status="private", rng="below_1b", city="New York", focus="Fintech & Payments",
    stage="Series A", stage_src="formd_band", stage_conf="medium", entry_date="2023-09",
    extra={"entry_stage_citation": SEC + "1999166/000199916623000001/0001999166-23-000001-index.htm"},
    note="AI-native FP&A software (New York). BCV entered with the round Christina Melas-Kyriazi's Form D records (2023-09-21), part of the "
         "$16.7M seed-and-Series-A Aleph announced on leaving stealth (businesswire 2023-10-24); a $29M Series B followed in 2025 (GlobeNewswire). "
         "The filing band reads Series A; the company was incorporated in 2020, so the band was withheld and is taken here with the "
         "announcement's Series A.",
    rounds=[rnd("2023-10", "Seed and Series A", 16700000, None, True, NEWS("aleph", "Emerges from Stealth with $16.7M to Build"), "press"),
            rnd("2025-09", "Series B", 29000000, None, None, NEWS("aleph", "Secures $29 Million Series B"), "press")]))

L.append(cls("alloy", status="private", rng="below_1b", country="US", country_src="web_verified",
    country_cite=NEWS("alloy", "Alloy Automation raises $20M"), city="San Francisco", focus="DevTools & APIs",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=POST("automating-the-ecommerce"), entry_date="2021-02",
    grad="graduated", grad_src="web_verified", grad_cite=NEWS("alloy", "Alloy Automation raises $20M"), grad_conf="high",
    flags=["model_disputes_source"],
    note="Alloy Automation, e-commerce integration and automation (San Francisco), not the Alloy of the identity-fraud sibling rows. "
         "'Bain Capital Ventures led a $5 million seed financing for Alloy' (the firm's post, 2021-02-02); the $20M Series A followed in "
         "February 2022 (TechCrunch). Wikidata's AU belongs to another Alloy.",
    rounds=[rnd("2021-02", "Seed", 5000000, "Bain Capital Ventures", True, POST("automating-the-ecommerce"), "firm"),
            rnd("2022-02", "Series A", 20000000, None, None, NEWS("alloy", "Alloy Automation raises $20M"), "press")]))

L.append(cls("ankorstore", city="Paris", focus="Consumer & Marketplaces",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=POST("the-future-of-retail-is-local"), entry_date="2021-05",
    note="European wholesale marketplace (Paris). 'BCV first invested in Ankorstore in May 2021, co-leading the company's $102M Series B' "
         "(the firm's post). The prefilled mark is the January 2022 Series C at about $2B (" + NEWS("ankorstore", "$2 billion valuation") + ")."))

L.append(cls("apixio-centene", status="acquired", rng="below_1b", city="San Mateo", focus="Healthcare & Bio",
    stage="undetermined",
    note="Healthcare AI analytics (San Mateo). Centene closed its purchase in December 2020 (" + NEWS("apixio-centene", "Centene closes") + "). "
         "BCV entered with the 2013-11 round Jared Kesselheim's Form D records ($2.5M), in a company incorporated in 2009 that had raised before, "
         "so the band is withheld and the round is not named in any source read."))

L.append(cls("appassure-software-dell", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Reston",
    focus="Data Infrastructure", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=W("AppAssure"),
    entry_date="2008",
    note="Backup and recovery software (Reston, VA). 'In 2008, AppAssure Software received a Series A investment by Bain Capital Ventures' "
         "(Wikipedia). Acquired by Dell in February 2012 (the firm's archived page)."))

L.append(cls("appneta-broadcom-software", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Boston",
    focus="Data Infrastructure", stage="undetermined",
    note="Network performance monitoring (Boston; formerly Apparent Networks, Vancouver). Acquired by Broadcom (the firm's listing). "
         "BCV invested in 2007; no source names the round."))

L.append(cls("appriss-inc", status="acquired", rng="below_1b", city="Louisville", focus="SaaS", stage="undetermined",
    note="Data and analytics for government and retail (Louisville). The firm's 2010 archive files it under 'Expansion/Growth Buyout' "
         "and 'Acquired by Insight Venture Partners'; Clearlake and Insight later backed it. No source says whether BCV's 2007 position "
         "was a minority or a control stake, so it is kept as a member and the round is undetermined; raised for review."))

L.append(cls("archive", status="private", rng="below_1b", country="US", country_src="web_verified",
    country_cite=NEWS("archive", "Resale tech company Archive raises $15M"), city="San Francisco", focus="Consumer & Marketplaces",
    stage="Pre-Seed", stage_src="web_verified", stage_conf="high", stage_cite=POST("why-we-invested-in-archive"),
    entry_date="2021", flags=["model_disputes_source", "stage_disputes_band"],
    note="Branded resale platform (San Francisco). 'BCV first invested in Archive in their pre-seed round' and co-led the seed "
         "(the firm's post, 2022-01-26), so the entry is Pre-Seed, not the listing's Seed (decisions.md R2 names this case). "
         "Series A $15M (2022) and $30M (2025) followed; the company operates. Wikidata's 'acquired' and ZA belong to another 'Archive'.",
    clear=[]))

L.append(cls("argyle", city="New York", rng="below_1b", focus="Fintech & Payments",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=POST("bcv-leads-20-million-series-a-in-argyle"),
    entry_date="2019", status="private",
    grad="graduated", grad_src="first_party", grad_cite=POST("bcv-leads-20-million-series-a-in-argyle"), grad_conf="high",
    flags=["stage_disputes_band", "model_disputes_source"],
    note="Payroll-connectivity API (New York). BCV joined the 2019 seed ('our prior participation in Argyle's seed round last year') and "
         "led the $20M Series A in 2020 (the firm's post); a $30M Series C followed in 2024. The Form D band (Growth, 2022) reads a later "
         "filing; Wikidata's 'defunct' belongs to another Argyle.",
    rounds=[rnd("2019", "Seed", None, None, True, POST("bcv-leads-20-million-series-a-in-argyle"), "firm"),
            rnd("2020-10", "Series A", 20000000, "Bain Capital Ventures", True, POST("bcv-leads-20-million-series-a-in-argyle"), "firm"),
            rnd("2024-03", "Series C", 30000000, None, None, NEWS("argyle", "Series C Funding"), "press")]))

L.append(cls("armis-security", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="Security", stage="Growth", stage_src="model", stage_conf="medium",
    note="IoT and asset security (founded in Israel; San Francisco HQ). BCV's listing gives 2018 (Enrique Salem): the $30M Series B of April "
         "2018 (Calcalist) or the $65M Series C of 2019, both Growth. Insight bought control at $1.1B in 2020; ServiceNow closed its "
         "$7.75B purchase in April 2026 (" + NEWS("armis-security", "ServiceNow completes $7.7B acquisition of Israel") + ")."))

L.append(cls("attentive", status="private", rng="1b_plus", city="New York", focus="SaaS",
    usd=2200000000, val_src="web_verified", asof="2020-09-23",
    val_cite=NEWS("attentive", "Raises $230 Million Series D"), extra={"valuation_range_source": "web_verified"},
    flags=["stale"],
    note="Mobile messaging for commerce (New York). BCV led the Series A (its own post, 2018-03-14), which the filings also give. "
         "Mark: the $230M Series D (September 2020, Coatue) at $2.2B, the last priced round read here; later rounds reported at "
         "$5B+ are to be pinned in the A/B pass (siblings: Atomico $5B 2021, Sequoia $2.7B 2025)."))

L.append(cls("attivo-networks-sentinelone", status="acquired", rng="below_1b", country="US", country_src="model_knowledge",
    city="Fremont", focus="Security", stage="undetermined",
    note="Identity and deception security (Fremont). SentinelOne agreed to buy it in March 2022 ("
         + NEWS("attivo-networks-sentinelone", "SentinelOne to Acquire Attivo") + "). BCV's listing gives 2014 (Enrique Salem); no source names the round."))

L.append(cls("augtera-networks", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Palo Alto",
    focus="AI & Applied AI", stage="Seed", **site_stage("augtera-networks"), entry_date="2016",
    note="Network AIOps (Palo Alto). Nvidia acquired it in 2025 (" + NEWS("augtera-networks", "Nvidia quietly acquires") + "). "
         "BCV's listing: 2016, Seed. Graduation left for the graduation pass."))

L.append(cls("autoleap", status="private", rng="below_1b", country="CA", country_src="web_verified",
    country_cite=NEWS("autoleap", "revs up growth"), city="Toronto", focus="SaaS",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=POST("the-engine-for-modern-auto-repair"), entry_date="2021-10",
    note="Auto-repair shop software (Toronto). 'Bain Capital Ventures is proud to have led AutoLeap's Series A' ($18M, 2021); "
         "a $30M Series B followed in 2023 (TechCrunch).",
    rounds=[rnd("2021-10", "Series A", 18000000, "Bain Capital Ventures", True, POST("the-engine-for-modern-auto-repair"), "firm"),
            rnd("2023-04", "Series B", 30000000, None, None, NEWS("autoleap", "now with $30M Series B"), "press")]))

L.append(cls("avidxchange", city="Charlotte", rng="below_1b",
    note="Accounts-payable automation (Charlotte). IPO October 2021; taken private by TPG in 2025, so acquired stands. "
         "BCV entered at the 2015 round the filings give (Matt Harris)."))

L.append(cls("awake-security-arista-networks", status="acquired", rng="below_1b", country="US", country_src="model_knowledge",
    city="Santa Clara", focus="Security", stage="undetermined",
    note="Network detection and response (Santa Clara). Acquired by Arista Networks in 2020 after a $36M Series C that April (FinTech Global). "
         "BCV's listing gives 2016 (Enrique Salem); no source names its entry round."))

L.append(cls("bettercloud", status="acquired", rng="below_1b", city="New York", focus="SaaS",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=W("BetterCloud"),
    note="SaaS operations management (New York). 'In April 2018, BetterCloud raised $60 million in a Series E funding led by Bain Capital "
         "Ventures' (Wikipedia). Vista Equity Partners bought a majority stake in June 2022 (" + NEWS("bettercloud", "Vista Equity Partners buys") + ")."))

L.append(cls("bevspot", status="private", rng="below_1b", city="Boston", focus="SaaS",
    note="Inventory software for food and beverage (Boston); raised a $5.25M round in 2015 (Boston Globe). Operating; entry round from the filings."))

L.append(cls("billtrust", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Lawrenceville",
    focus="Fintech & Payments", stage="Growth", stage_src="model", stage_conf="medium",
    note="B2B invoicing and payments (Lawrenceville, NJ). BCV wrote 'the first outside check into Billtrust in 2012' (the firm's post): "
         "a growth-equity investment in a profitable company founded in 2001 (Matt Harris on the board since November 2012, per Justworks' "
         "S-1). Public via SPAC (BTRS) in 2021; taken private by EQT for $1.7B in 2022."))

L.append(cls("blip-tv", status="acquired", rng="below_1b", city="New York", focus="Media, Gaming & Advertising",
    stage="undetermined",
    note="Web video network (New York). 'Financed by Bain Capital Ventures, Canaan Partners, and Ambient Sound Investments' (Wikipedia); "
         "BCV entered in 2010 with the $10M round the NYT reported (2010-05). Maker Studios acquired Blip in 2013 and closed the site in 2015: "
         "a sale of the company, so acquired (COLLECTION.md s6)."))

L.append(cls("bloomreach", status="private", rng="1b_plus", country="US", country_src="model_knowledge", city="Mountain View",
    focus="SaaS", usd=2200000000, val_src="web_verified", asof="2022-02-23",
    val_cite=NEWS("bloomreach", "valued at $2.2B"), extra={"valuation_range_source": "web_verified"},
    stage="undetermined", flags=["stale"],
    note="Commerce personalisation (Mountain View). BCV invested in 2009 (Ajay Agarwal), the company's founding year; no source read names "
         "the round. Mark: the $175M Series F at $2.2B (February 2022); stale beyond 24 months."))

L.append(verdict("bluecoat-symantec", "not_member",
    "Blue Coat was bought from Thoma Bravo in Bain Capital's 2016 buyout, with BCIP Venture Associates among the buyout investors "
    "(Blue Coat's registration-rights agreement, DRS 2016-01-29): a control acquisition, not a venture round (COLLECTION.md s1 T3; decisions.md D4).",
    ec="site_listing", conf="high", cite="https://www.sec.gov/Archives/edgar/data/1662655/000095012316010893/0000950123-16-010893-index.htm")
    | {"exclusion": "control_position"})
L.append(cls("bluestem-brands", status="acquired", rng="below_1b", city="Eden Prairie", focus="Consumer & Marketplaces",
    note="Online retailer (Eden Prairie; formerly Fingerhut Direct Marketing). 'Bain Capital' in its 2011 S-1 means Bain Capital Venture Fund, L.P. "
         "and affiliates; the company was sold to Capmark Financial in 2014 and later to Chinese investors. Entry from the filings."))
L.append(verdict("bmc-software", "not_member",
    "BMC Software, a listed company, was taken private in 2013 by Bain Capital, Golden Gate, GIC and Insight: a control acquisition of a public "
    "company, not a venture round (COLLECTION.md s1 T3; decisions.md D4; config verify.not_members).",
    ec="site_listing", conf="high", cite=SITE("bmc-software")) | {"exclusion": "control_position"})
L.append(cls("booker", status="acquired", rng="below_1b", city="New York", focus="SaaS",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=W("Booker Software"), flags=["stage_disputes_band"],
    note="Salon and spa scheduling software (New York). 'On April 16, 2013, Booker secured $27.5 million in Series B financing led by Bain "
         "Capital Ventures' (Wikipedia). Acquired by Mindbody in 2018."))
L.append(cls("boston-heart-diagnostics-eurofins-scientific", status="acquired", rng="below_1b", city="Framingham",
    focus="Healthcare & Bio", stage="undetermined",
    note="Cardiovascular diagnostics lab (Framingham). Acquired by Eurofins Scientific (the firm's listing). BCV's listing gives 2010 and "
         "the first partner-anchored Form D is 2011 ($6.5M) in a company incorporated in 2007, so the band is withheld; the round is not named."))
L.append(cls("bti-systems-juniper", status="acquired", rng="below_1b", city="Ottawa", focus="Data Infrastructure",
    note="Packet-optical networking (Ottawa). Acquired by Juniper Networks in 2016."))
L.append(cls("buywithme-gilt-groupe", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Boston",
    focus="Consumer & Marketplaces", stage="undetermined",
    note="Group-buying site (Boston). 'In 2010, BuyWithMe was funded with $36.5M by Matrix Partners, Bain Capital Ventures, and Pinnacle "
         "Ventures' (Wikipedia); acquired by Gilt City in November 2011 (the firm's archived page). The round names are not given."))
L.append(cls("celerion-h-i-g-capital", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Lincoln",
    focus="Healthcare & Bio", stage="undetermined",
    note="Early-stage clinical research (Lincoln, NE), formed in 2010 from MDS Pharma Services' early clinical business. The firm's archive files "
         "it under 'Expansion/Growth Buyout' and 'Acquired by MTS Health Investors'; whether BCV's 2010 position was control is not established, "
         "raised for review."))
L.append(cls("centivo", status="private", rng="below_1b", country="US", country_src="web_verified",
    country_cite=NEWS("centivo", "New Type of Health Plan"), city="Buffalo", focus="Healthcare & Bio",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("centivo", "New Type of Health Plan"), entry_date="2018-07",
    note="Employer health plans (the 2018 release is datelined New York; the firm lists Buffalo). 'Bain Capital Ventures led the financing round' "
         "of the $34M Series A (PR Newswire 2018-07-18); Series B $34M (2020) and $75M (2024) followed.",
    rounds=[rnd("2018-07", "Series A", 34000000, "Bain Capital Ventures", True, NEWS("centivo", "New Type of Health Plan"), "press")]))
L.append(cls("chrome-river-emburse", status="acquired", rng="below_1b", city="Los Angeles", focus="SaaS",
    note="Expense and invoice automation (Los Angeles). Merged into Emburse in 2019 (the firm's listing). Entry from the filings."))
L.append(cls("clari", city="Sunnyvale", status="acquired", rng="below_1b", flags=["model_disputes_source"],
    extra={"valuation_usd": None},
    note="Revenue platform (Sunnyvale). Merged with Vista's Salesloft in late 2025; the combined company operates as 'Clari + Salesloft' "
         "(" + NEWS("clari", "cuts dozens of jobs") + "), so Clari no longer stands alone: acquired, with the successor ambiguity noted "
         "(COLLECTION.md s6). Its standalone mark was $2.6B (Series F, January 2022). Sibling Sequoia still reads private $2.6B."))
L.append(cls("clockwise", status="defunct", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="SaaS", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=POST("the-end-of-meeting-hell"), entry_date="2020-06",
    note="Calendar automation (San Francisco). BCV led the $18M Series B (the firm's post, 2020-06-16). The product shut on 2026-03-27 after "
         "Salesforce hired the team without buying the company (the acqui-hire rule: defunct)."))
L.append(cls("cloudistics-fungible", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Reston",
    focus="Data Infrastructure", stage="undetermined",
    note="Private-cloud infrastructure (Reston, VA; the firm lists Washington, DC). Acquired by Fungible (the firm's listing). BCV's listing "
         "gives 2016 (Ben Nye); the round is not named."))
L.append(cls("clovr-media", status="unknown", rng="below_1b", city="Boston", focus="Media, Gaming & Advertising",
    note="Card-linked ad offers (Boston); raised $1.5M in 2010 (Reuters). No trace after the early 2010s; state unknown."))
L.append(cls("cofactr", status="private", rng="below_1b", city="New York", focus="Industrial & Robotics",
    stage="Seed", **site_stage("cofactr"), entry_date="2021", flags=["stage_disputes_band"],
    grad="graduated", grad_src="web_verified", grad_cite=NEWS("cofactr", "Raises $17M Series A"), grad_conf="high",
    note="Electronics supply-chain software (New York). BCV's listing: 2021, Seed (and its 2022 post on the investment); the first "
         "partner-anchored Form D (2023-09) is a later round, so the band's Series A is overruled. The $17M Series A (December 2024) graduates it.",
    rounds=[rnd("2024-12", "Series A", 17000000, None, None, NEWS("cofactr", "Raises $17M Series A"), "press")]))

if __name__ == "__main__":
    jl.write("batch-001", L)
