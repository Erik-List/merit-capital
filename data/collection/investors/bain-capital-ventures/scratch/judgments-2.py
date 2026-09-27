"""PRO-162 grind, batch-002 (color-labs .. hazel-health). Evidence as in judgments-1.py. The Doc Halo /
Halo Communications / Halo Health rows are one company (Form D CIK 1704200 for both Doc Halo and Halo
Communications; the firm lists Halo Health (Symplr)); the merge lands at the scheduled rebuild, so only
the canonical row is classified here."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd, POST, SITE, W, NEWS = jl.cls, jl.verdict, jl.rnd, jl.POST, jl.SITE, jl.W, jl.NEWS
L = []
SEC = "https://www.sec.gov/Archives/edgar/data/"


def site_stage(slug):
    return dict(stage_src="first_party", stage_conf="medium", stage_cite=SITE(slug))


L.append(cls("color-labs-inc-apple", status="acquired", rng="below_1b", country="US", country_src="model_knowledge",
    city="Palo Alto", focus="Consumer & Marketplaces", stage="Series A", stage_src="model", stage_conf="medium",
    note="Color, the photo-sharing app (Palo Alto). BCV (Michael Krupka) invested in its $41M first round of 2011 alongside Sequoia and "
         "Silicon Valley Bank; Apple bought the company in 2012 (the firm lists 'Color Labs Inc. (Apple)', Acquired; the press called it an "
         "acquisition, so it reads acquired under the acqui-hire rule's last sentence)."))

L.append(cls("column-tax", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="New York",
    focus="Fintech & Payments", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=POST("income-tax-is-the-next"),
    entry_date="2021-11", grad="graduated", grad_src="web_verified", grad_conf="high",
    grad_cite=NEWS("column-tax", "Raises A $21.7 Million Series A"),
    note="Embedded tax filing (New York). 'BCV has led a $5.1M seed financing for Column Tax' (the firm's post, 2021-11-23); the $21.7M "
         "Series A followed in May 2022 (Forbes). Acquired by Aiwyn in 2025 (" + NEWS("column-tax", "Following Column Tax Acquisition") + ").",
    rounds=[rnd("2021-11", "Seed", 5100000, "Bain Capital Ventures", True, POST("income-tax-is-the-next"), "firm"),
            rnd("2022-05", "Series A", 21700000, None, None, NEWS("column-tax", "Raises A $21.7 Million Series A"), "press")]))

L.append(cls("concurrent", status="unknown", rng="below_1b", city="San Francisco", focus="Data Infrastructure",
    note="Concurrent, Inc. (San Francisco), the company behind the Cascading data framework; BCV entered with Salil Deshpande in 2014 "
         "(Form D). No trace of the company after the mid-2010s; state unknown."))

L.append(cls("corvus-travelers", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Boston",
    focus="Fintech & Payments", stage="Seed", **site_stage("corvus-travelers"), entry_date="2016",
    note="Cyber insurance (Boston). Acquired by Travelers in 2024 (the firm lists 'Corvus (Travelers)', Acquired). BCV's listing: 2016, "
         "Seed. Graduation left for the graduation pass."))

L.append(cls("cquotient", status="acquired", rng="below_1b", city="Cambridge", focus="SaaS",
    note="Retail predictive analytics (Cambridge, MA). Acquired by Demandware in October 2014 ("
         + NEWS("cquotient", "Demandware Acquires") + "). The filings give BCV's 2010 seed ($3M) and no later round before the sale."))

L.append(cls("crusoe-energy", status="private", rng="10b_plus", city="San Francisco", focus="AI & Applied AI",
    usd=30900000000, val_src="web_verified", asof="2026-09-18",
    val_cite=NEWS("crusoe-energy", "Crusoe Raises $3.9 Billion"), extra={"valuation_range_source": "web_verified"},
    stage="Seed", **site_stage("crusoe-energy"), entry_date="2019",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("crusoe-energy", "Raises $70M in Funding"),
    flags=["stage_disputes_band"],
    note="AI cloud and data centres (founded in Denver; San Francisco HQ). BCV's listing: 2019, Seed (the $4.5M seed of May 2019); the "
         "partner-anchored Form D (2019-11, Stefan Cohen) is the $70M Series A of December 2019, which graduates the seed, so the band's "
         "Series A is overruled. Mark: the $3.9B round of September 2026 at $30.9B (trendingtopics.eu); the $1.375B Series E of October "
         "2025 was at $10B+.",
    rounds=[rnd("2019-05", "Seed", 4500000, None, True, NEWS("crusoe-energy", "Raises $4.5M in Seed"), "press"),
            rnd("2019-12", "Series A", 70000000, None, True, NEWS("crusoe-energy", "Raises $70M in Funding"), "press"),
            rnd("2025-10", "Series E", 1375000000, None, None, NEWS("crusoe-energy", "Crusoe raises $1.375B at $10B"), "company"),
            rnd("2026-09", "Series F", 3900000000, None, None, NEWS("crusoe-energy", "Crusoe Raises $3.9 Billion"), "press")]))

L.append(cls("cube-js", status="private", rng="below_1b", city="San Francisco", focus="Data Infrastructure",
    stage="Seed", stage_src="model", stage_conf="medium", entry_date="2020-09",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("cube-js", "Raises $15.5 Million to Help"),
    flags=["model_disputes_source", "cite_pending"],
    note="Semantic layer for data (Cube Dev, San Francisco; Wikidata's DE is another Cube). BCV's listing: 2020 (Aaref Hilaly), 'Early'; the "
         "2020 round is the $6.2M seed TechCrunch reported in September 2020, which BCV led; the $15.5M Series A (July 2021) and a $25M round "
         "(2024) followed.",
    rounds=[rnd("2020-09", "Seed", 6200000, "Bain Capital Ventures", True, NEWS("cube-js", "Cube Dev raises $6.2M"), "press"),
            rnd("2021-07", "Series A", 15500000, None, None, NEWS("cube-js", "Raises $15.5 Million to Help"), "press")]))

L.append(cls("decagon", status="private", rng="1b_plus", city="San Francisco", focus="AI & Applied AI",
    usd=4500000000, val_src="web_verified", asof="2026-01-28",
    val_cite=NEWS("decagon", "Valuation Triples to $4.5 Billion as it Ushers"), extra={"valuation_range_source": "web_verified"},
    note="AI customer-support agents (San Francisco). BCV entered in 2024 (Aaref Hilaly; the firm's post 'Why We Backed Decagon AI'). "
         "Mark: the $250M Series D of January 2026 at $4.5B."))

L.append(cls("defi-solutions", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="Dallas",
    focus="Fintech & Payments", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("defi-solutions", "picks $55m Series C"), entry_date="2018-01",
    note="Loan origination software (Dallas). 'defi SOLUTIONS picks $55m Series C led by Bain Capital' (FinTech Global, 2018-01-22; the firm "
         "lists it with Matt Harris, Growth). Merged with Sagent Auto in 2019 under the defi SOLUTIONS name; operating."))

L.append(cls("dgraph", status="acquired", rng="below_1b", city="San Francisco", focus="Data Infrastructure",
    grad="graduated", grad_src="web_verified", grad_conf="medium",
    grad_cite=NEWS("dgraph", "growing graph database"), entry_date="2017-10-25", flags=["model_disputes_source"],
    note="Graph database (Dgraph Labs). BCV (Salil Deshpande) entered with the 2017 seed the filings give; Redpoint led an $11.5M Series A "
         "in 2018 (TechTarget, 2019, on the company's funding), which graduates it though no BCV-anchored Form D records it. Istari Digital "
         "acquired Dgraph in October 2025 (" + NEWS("dgraph", "Istari Digital Acquires Dgraph") + ")."))

L.append(cls("digital-currency-group", city="Stamford", focus="Crypto & Web3",
    stage="Seed", **site_stage("digital-currency-group"), entry_date="2014", flags=["stale"],
    note="Crypto holding company (Stamford, CT; Grayscale's parent). BCV's listing: 2014, Seed (Matt Harris; the 2015 formation round that "
         "also brought in Mastercard and others). The prefilled $10B is the November 2021 sale of about $700M of shares led by SoftBank "
         "(" + NEWS("digital-currency-group", "tops $10 billion valuation") + "); after Genesis's 2023 collapse no newer priced event is "
         "known, so it stands, stale. Graduation left for the graduation pass."))

L.append(cls("docker", status="private", rng="1b_plus", city="Palo Alto", focus="DevTools & APIs",
    usd=2100000000, val_src="web_verified", asof="2022-03-31",
    val_cite=NEWS("docker", "Raises $105M At $2.1B Valuation"), extra={"valuation_range_source": "web_verified"},
    flags=["stale"],
    note="Container tooling (Palo Alto). BCV led the $105M Series C at $2.1B (the firm's post, 2022-03-31); no later priced round; stale."))

L.append(cls("docusign", city="San Francisco",
    note="E-signature (San Francisco). 'Bain Capital Ventures, along with Bain Capital Public Equity, was fortunate to lead DocuSign's last "
         "two rounds of funding' (the firm's post, 2018-04-27): growth rounds of 2014-2015, as the filings give."))

L.append(cls("dynamics", status="private", rng="below_1b", city="Cheswick", focus="Fintech & Payments",
    note="Battery-powered interactive payment cards (Cheswick, PA); product and partnership news through 2018 (SoftBank collaboration). "
         "No sale or shutdown found; read as operating."))

L.append(cls("dynatrace", city="Waltham", status="acquired", rng="below_1b", stage="undetermined",
    extra={"valuation_usd": None}, flags=["model_disputes_source"],
    note="Application performance monitoring. BCV's position was in dynaTrace software (Waltham), which Compuware bought in July 2011 "
         "(the firm's archived page); today's NYSE-listed Dynatrace is the business spun out of Compuware in 2019, so the float belongs to a "
         "successor and the row reads acquired (COLLECTION.md s8 duty 4). BCV's 2010 round (the filings' $4M in a company incorporated in "
         "2006, band withheld) is not named."))

L.append(cls("earnup", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="Fintech & Payments", stage="undetermined",
    note="Consumer loan-payment platform (San Francisco); a $31M Series C closed in March 2022. BCV's listing: 2019, 'Early'; the round is not named."))

L.append(cls("ecosense", status="acquired", rng="below_1b", city="Los Angeles", focus="Climate & Energy", stage="undetermined",
    note="LED lighting (EcoSense Lighting); combined into Korrus in 2021. BCV entered in 2011 (Jeffrey Glass, John Connolly on the Form D) in "
         "a company incorporated in 2008; the band is withheld and the round is not named."))

L.append(verdict("edgar-online-otc-markets-group", "not_member",
    "EDGAR Online was listed on NASDAQ (EDGR) from 1999; BCV's 2010 investment was a private placement into the listed company (its 8-K of "
    "2010-01-29 files the investor rights agreement signed by Bain Capital Venture Integral Investors). A placement into a public company is "
    "not a venture round in a private company (COLLECTION.md s1 T3; decisions.md D4).",
    ec="site_listing", conf="high", cite=SITE("edgar-online-otc-markets-group")))

L.append(verdict("education-holdings-1-the-princeton-review", "not_member",
    "The Princeton Review was listed on NASDAQ (REVU) from its 2001 IPO (the firm's own archive: 'IPO on 6/19/01'); BCV's 2007 investment "
    "was preferred stock issued by the listed company (its 8-K of 2007-07-26 defines the 'Bain Fund'), later renamed Education Holdings 1. "
    "A placement into a public company is not a venture round (COLLECTION.md s1 T3; decisions.md D4).",
    ec="site_listing", conf="high", cite=SITE("education-holdings-1-the-princeton-review")))

L.append(cls("emburse", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="Fintech & Payments", stage="Seed", **site_stage("emburse"), entry_date="2016",
    note="The original Emburse, a corporate card startup (San Francisco), bought in 2019 by the Certify / Chrome River group, which took its "
         "name. BCV's listing: 2016, Seed (Matt Harris). Graduation left for the graduation pass."))

L.append(cls("enclarity", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Aliso Viejo",
    focus="Healthcare & Bio", stage="undetermined",
    note="Healthcare provider data (Aliso Viejo, CA). Acquired by LexisNexis (the firm's archived listing). The filings' 2009 round sits in a "
         "company incorporated in 2005, so the band is withheld; no source names BCV's round."))

L.append(cls("enservio", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Natick",
    focus="Fintech & Payments", stage="undetermined",
    note="Claims-contents software for insurers (Natick, MA). The firm listed it from 2006 (Midstage) and later as Exited; acquired by Solera. "
         "BCV's first round (2006) precedes the 2009 Form D and is not named."))

L.append(cls("evertrue", status="acquired", rng="below_1b", city="Boston", focus="SaaS",
    note="Donor CRM for education (Boston); the firm lists it as Acquired. Graduation left for the graduation pass."))

L.append(cls("evident-io-palo-alto-networks", status="acquired", rng="below_1b", city="Dublin", focus="Security", stage="undetermined",
    note="Cloud security compliance (Dublin, CA). Palo Alto Networks bought it in March 2018 ("
         + NEWS("evident-io-palo-alto-networks", "Palo Alto Networks buys Evident.io") + "). BCV's listing gives 2014; the first "
         "partner-anchored Form D (2016) is a later round in a company incorporated in 2013; the entry round is not named."))

L.append(cls("expertvoice", status="private", rng="below_1b", city="Salt Lake City", focus="Consumer & Marketplaces",
    note="Brand-to-expert product marketing (ExpertVoice, formerly Experticity; Salt Lake City). Operating."))

L.append(cls("felt", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="Oakland",
    focus="SaaS", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=POST("felt-thinking-in-maps"), entry_date="2021-08",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("felt", "$15 million chance"),
    note="Collaborative web mapping (Oakland). 'Felt is announcing its $4.5M seed round led by BCV' (the firm's post, 2021-08-10); the $15M "
         "Series A followed in May 2022 (TechCrunch).",
    rounds=[rnd("2021-08", "Seed", 4500000, "Bain Capital Ventures", True, POST("felt-thinking-in-maps"), "firm"),
            rnd("2022-05", "Series A", 15000000, None, None, NEWS("felt", "$15 million chance"), "press")]))

L.append(cls("fermat", status="private", rng="below_1b", city="San Francisco", focus="AI & Applied AI",
    note="AI commerce storefronts (FERMAT, San Francisco); $17M Series A in March 2024, the round the filings give."))

L.append(cls("finix", status="private", rng="below_1b", city="San Francisco", focus="Fintech & Payments",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=POST("the-rise-of-the-payment-facilitator"), entry_date="2019-07",
    note="Payments infrastructure for software platforms (San Francisco). 'We are thrilled to announce that we're leading a $17.5 million "
         "Series A in Finix' (the firm's post, 2019-07-16)."))

L.append(cls("finley-concord", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="Fintech & Payments", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("finley-concord", "$3 million seed fundraise led by Bain"), entry_date="2021-06",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("finley-concord", "closes $17M"),
    flags=["stage_disputes_band"],
    note="Debt-capital management software (San Francisco). 'Finley announces $3 million seed fundraise led by Bain Capital Ventures' "
         "(PR Newswire, 2021-06-14); the $17M Series A followed (TechCrunch, January 2023). Concord acquired Finley in March 2026 ("
         + NEWS("finley-concord", "Concord acquires Finley") + ").",
    rounds=[rnd("2021-06", "Seed", 3000000, "Bain Capital Ventures", True, NEWS("finley-concord", "$3 million seed fundraise led by Bain"), "press"),
            rnd("2023-01", "Series A", 17000000, None, None, NEWS("finley-concord", "closes $17M"), "press")]))

L.append(cls("flow-commerce-global-e", status="acquired", rng="below_1b", city="Hoboken", focus="SaaS",
    note="Cross-border e-commerce (Hoboken, NJ). Acquired by Global-e in 2021 (the firm's listing)."))

L.append(cls("flux", city="San Francisco", status="private", rng="below_1b", country="US", country_src="web_verified",
    country_cite=NEWS("flux", "Browser-based hardware design tool"), focus="Industrial & Robotics",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=POST("software-for-modern-hardware"), entry_date="2021-10",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("flux", "Flux Raised $27M in Series B"),
    extra={"valuation_usd": None}, flags=["model_disputes_source"],
    note="Flux.ai, browser-based electronics design (San Francisco). BCV's 'Seed Investment In Flux' (the firm's post, 2021-10-13; the $12M "
         "round TechCrunch reported); a Series B followed in 2026 (FinSMEs, and $37M per Fortune). The prefilled public CZ float belongs to "
         "an unrelated listed 'Flux'.",
    rounds=[rnd("2021-10", "Seed", 12000000, None, True, POST("software-for-modern-hardware"), "firm"),
            rnd("2026-02", "Series B", 27000000, None, None, NEWS("flux", "Flux Raised $27M in Series B"), "press")]))

L.append(cls("flywire", city="Boston",
    note="Education and B2B payments (Boston), IPO May 2021 (NASDAQ: FLYW); entry from the filings (Matt Harris, 2015)."))

L.append(cls("forescout-technologies-inc", city="San Jose", rng="below_1b",
    note="Network access control (San Jose). BCV's 2015 growth round (Enrique Salem on the Form D); IPO 2017; taken private by Advent in 2020."))

L.append(cls("fossa", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="Chicago",
    focus="DevTools & APIs", stage="Seed", **site_stage("fossa"), entry_date="2016",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("fossa", "Series A to help enterprise"),
    note="Open-source license and security management (FOSSA; the firm lists Chicago). BCV's listing: 2016, Seed; the $8.5M Series A followed "
         "in 2019 (TechCrunch) and a $23M Series B in 2020.",
    rounds=[rnd("2019-09", "Series A", 8500000, None, None, NEWS("fossa", "Series A to help enterprise"), "press")]))

L.append(cls("fourkites", status="private", rng="below_1b", city="Chicago", focus="SaaS",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=POST("we-like-ike"), entry_date="2016",
    flags=["stage_disputes_band"],
    note="Supply-chain visibility (Chicago). 'FourKites has grown more than twentyfold since we led the Series A just over two years ago' "
         "(the firm's post, 2019-02-05); BCV's listing gives 2016. The band's Growth reads the later 2019 filing."))

L.append(cls("frame", status="acquired", rng="below_1b", city="San Mateo", focus="SaaS",
    note="Cloud desktop delivery (Frame, formerly Mainframe2; San Mateo). 'Frame Secures $16M in New Funding from Bain Capital Ventures, "
         "Microsoft Ventures and In-Q-Tel' (2017); acquired by Nutanix in 2018."))

L.append(cls("gainsight-vista", status="acquired", rng="below_1b", city="San Francisco", focus="SaaS",
    stage="Growth", **site_stage("gainsight-vista"), flags=["stage_disputes_band"],
    note="Customer success software (founded 2009 as JBara). BCV's listing tags the 2013 entry Growth, the $9M Series B of November 2013; the "
         "Form D band read it as Series A for a company that had raised since 2011. Vista acquired Gainsight in 2020 ($1.1B)."))

L.append(cls("gather-ai", status="private", rng="below_1b", city="Pittsburgh", focus="Industrial & Robotics",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=POST("gather-ai-drone-vision"), entry_date="2024-03",
    flags=["stage_disputes_band"],
    note="Warehouse inventory drones (Pittsburgh). 'We led Gather AI's $17 million Series A-1' (the firm's post, 2024-03-27); the $40M Series B "
         "(February 2026) is the later filing the band read."))

L.append(cls("gocardless", status="acquired", rng="below_1b", country="GB", country_src="web_verified",
    country_cite=NEWS("gocardless", "nears Unicorn status"), city="London", focus="Fintech & Payments",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("gocardless", "nears Unicorn status"), entry_date="2020-12",
    note="Bank-payment collection (London). BCV led the $95M Series F of December 2020 (Finextra; the firm's post 2021-01-05). Mollie agreed "
         "to buy GoCardless in December 2025 and closed the purchase in September 2026 (" + NEWS("gocardless", "Mollie closes the purchase") + ")."))

L.append(cls("graniteshares", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="New York",
    focus="Fintech & Payments", stage="Seed", **site_stage("graniteshares"), entry_date="2014",
    note="ETF sponsor (New York), an operating asset manager rather than a fund. BCV's listing: 2014, Seed (Matt Harris). Graduation left for "
         "the graduation pass."))

L.append(cls("halcyon", status="private", rng="1b_plus", city="Austin", focus="Security",
    usd=1000000000, val_src="web_verified", asof="2024-11-25",
    val_cite=NEWS("halcyon", "raises $100M at $1B valuation"), extra={"valuation_range_source": "web_verified"},
    note="Anti-ransomware platform (Austin). BCV led the $40M Series B (the firm's post, 2023-12-19). Mark: the $100M Series C of November 2024 "
         "at $1B (Austin Business Journal)."))

L.append(cls("halo-health-symplr", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Cincinnati",
    focus="Healthcare & Bio", flags=["identity_conflated"],
    note="Clinical communication (Cincinnati): Doc Halo, renamed Halo Communications and then Halo Health, acquired by symplr in 2022 (the firm "
         "lists 'Halo Health (Symplr)'). The doc-halo and halo-communications rows are the same company (one Form D CIK, 1704200) and merge "
         "into this row at the rebuild; the entry round comes with them."))

L.append(cls("hazel-health", status="private", rng="below_1b", city="San Francisco", focus="Healthcare & Bio",
    stage="undetermined", flags=["stage_disputes_band"],
    note="School-based telehealth (San Francisco); $33M Series C (2020) and $51.5M Series C1 (2022). BCV's listing gives 2017, three years before "
         "the first partner-anchored filing the band read as Growth; the 2017 round is not named."))

if __name__ == "__main__":
    jl.write("batch-002", L)
