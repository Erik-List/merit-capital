"""PRO-162 grind, batch-011 (smallstep .. veza). Evidence as in judgments-1.py, plus Google News (nq.py, NQ_TAG=b11,
news-extra-b11.json), Wikipedia extracts cached under scratch/wiki/ (USinternetworking, Tennis Channel, Tealium), the
firm's 2006 past-portfolio page (sources/wayback/raw-old/2006-ind-all-past.html, descriptions quoted below) and pages
read 2026-09-27 where a line quotes them (WebSearch, 12 calls; WebFetch of press pages and company sites).

Three verdicts: USinternetworking (a 100% acquisition out of Chapter 11 by a Bain Capital Partners affiliate, control),
Swift Prepaid Solutions (bought outright in 2017 by Syncapay, a holding company BCV and co-investors launched; control,
medium, open for Erik) and The Lifelike Company (a 1996 Bain Capital investment, the heritage book, R1).
Momentum-slice checks (COLLECTION.md s6) ran on Google News on 2026-09-27 and are recorded in each note."""
import csv
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd, POST, SITE, W, NEWS, CCPAGE = jl.cls, jl.verdict, jl.rnd, jl.POST, jl.SITE, jl.W, jl.NEWS, jl.CCPAGE
L = []
HISTORY = ("https://web.archive.org/web/20060615151520/http://www.baincapitalventures.com:80/"
           "portfolio/index.asp?viewType=All&Section=3,0,0")
TAG = "[bain_capital_heritage] "
MC = "Momentum check (Google News, 2026-09-27): "


def site_stage(slug):
    return dict(stage_src="first_party", stage_conf="medium", stage_cite=SITE(slug))


def SIB(inv, slug, field):
    """A citation read off a sibling investor's published row (base.csv), never typed."""
    p = jl.ROOT / "data" / "collection" / "investors" / inv / "companies" / "base.csv"
    for r in csv.DictReader(open(p)):
        if r["slug"] == slug and r.get(field):
            return r[field]
    raise SystemExit(f"SIB({inv!r}, {slug!r}, {field!r}) not found")


def control(slug, why, cite, conf="high"):
    L.append(verdict(slug, "not_member",
        why + " A control acquisition is not a venture round (COLLECTION.md s1 T3 control positions; decisions.md D4): the firm "
        "with its co-investor group took 50% or more.", ec="site_listing", conf=conf, cite=cite) | {"exclusion": "control_position"})


L.append(cls("smallstep", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="Security", stage="Seed", **site_stage("smallstep"), entry_date="2020",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=SIB("accel", "smallstep", "graduation_citation"),
    note="Certificate management toolchain (San Francisco, aligned with Accel). BCV's listing: 2020, tagged Seed and Early (Enrique "
         "Salem); 'our participation in a $26 million combined Series A and seed round' (the firm's post, 2022-04-28). TechCrunch "
         "names the two legs: 'a $7 million seed led by Accel with help from Boldstart and a $19 million Series A led StepStone Group', "
         "so the seed entry graduated at the named Series A. Medium: the post does not say which leg BCV joined first.",
    rounds=[rnd("2022-04", "Series A", 19000000, "StepStone Group", None, SIB("accel", "smallstep", "graduation_citation"), "press")]))
L.append(cls("solcoa", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="Alameda",
    focus="Industrial & Robotics", stage="Seed", **site_stage("solcoa"), entry_date="2026-09", grad="censored",
    note="Rare earth metal production (Alameda, CA, where its 10-tonne line runs, per the company's site; the Solcoa One plant is "
         "being built in Nevada). BCV's listing: 2026, Seed (Alysaa Co, Kevin Zhang). 'Solcoa Announces $75M to Scale America's First "
         "New Metalmaking Process in 80 Years' (Business Wire, 2026-09-24, " + NEWS("solcoa", "Solcoa Announces $75M") + "): $45M of "
         "equity led by BCV and $30M of J.P. Morgan debt. Inside 24 months, so censored. No valuation was published."))
L.append(cls("stacklok", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="Seattle",
    focus="Security", stage="undetermined", entry_date="2024",
    note="Software supply chain and MCP security (Seattle; the firm's listing). BCV's listing: 2024, Early (Enrique Salem), which "
         "never mints a stage (R2). The only announced round is the $17.5M seed of May 2023 (TechCrunch) that Accel's row carries; "
         "BCV came in after it and its round is not named. " + MC + "no later priced round and no $1B+ figure found."))
L.append(cls("stamped", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="New York",
    focus="Consumer & Marketplaces", stage="Seed", stage_src="model", stage_conf="medium", entry_date="2011",
    note="Recommendation app from ex-Googlers (New York). 'The company is backed by Bain Capital and Google Ventures' at its November "
         "2011 launch (https://techcrunch.com/2011/11/21/stamped-approval/); the firm's page on it was captured 2011-10-02. The launch "
         "financing of a company founded in 2011, before a later strategic round of celebrity investors, read as its seed. Yahoo "
         "acquired it in October 2012 (the firm's listing). Graduation left for the graduation pass."))
L.append(cls("storageos", status="acquired", rng="below_1b", country="GB", country_src="web_verified",
    country_cite="https://www.uktech.news/news/investment-news/storageos-secures-8m-series-a-20180503", city="London",
    focus="Data Infrastructure", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.prweb.com/releases/2017/06/prweb14468271.htm", entry_date="2017-06",
    grad="graduated", grad_src="web_verified", grad_conf="high",
    grad_cite="https://www.uktech.news/news/investment-news/storageos-secures-8m-series-a-20180503",
    note="Cloud-native storage for containers (London; renamed Ondat in 2021). 'StorageOS today announced a $2 million seed round led "
         "by Bain Capital Ventures' (PRWeb, 2017-06-29), then 'StorageOS has raised $8m in Series A funding led by Bain Capital "
         "Ventures' (UKTN, 2018-05-03). Akamai bought Ondat in 2023 (" + NEWS("storageos", "cloud storage provider Ondat") + ").",
    rounds=[rnd("2018-05", "Series A", 8000000, "Bain Capital Ventures", True,
                "https://www.uktech.news/news/investment-news/storageos-secures-8m-series-a-20180503", "press")]))
L.append(cls("straiker", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="Mountain View",
    focus="Security", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("straiker", "from Lightspeed and Bain"),
    entry_date="2025-03", grad="graduated", grad_src="web_verified", grad_conf="high",
    grad_cite=NEWS("straiker", "Raises $64M Series A to Secure"),
    note="Security for AI agents and applications (Mountain View, the Series A dateline). 'Straiker raises $21m from Lightspeed and "
         "Bain' (FinTech Global, 2025-03-28), the launch round Lightspeed's row reads as the seed; BCV's listing gives 2024. The $64M "
         "Series A of 2026-06-29 was led by Marathon Management Partners, Citi Ventures, Illuminate Financial and Workday Ventures 'with "
         "continued participation from Bain Capital Ventures and Lightspeed' (PR Newswire). " + MC + "no valuation was published "
         "for the Series A; no $1B+ figure found.",
    rounds=[rnd("2026-06", "Series A", 64000000, "Marathon Management Partners, Citi Ventures, Illuminate Financial, Workday Ventures",
                True, NEWS("straiker", "Raises $64M Series A to Secure"), "press")]))
L.append(cls("strategic-mapping", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Santa Clara",
    focus="Data Infrastructure", stage="undetermined",
    note="Strategic Mapping Inc., maker of the Atlas GIS desktop mapping software and demographic databases (Santa Clara, CA). The "
         "firm's 2006 past-portfolio page: 'Develops and sells mapping software for personal computers', Acquired. Claritas bought "
         "it in 1996 (a vendor deal record, not read), which would put Bain Capital's position before any venture vehicle (D2, R1); "
         "left as a member for Erik's heritage review because no source read dates the investment."))
L.append(cls("structify", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="New York",
    focus="Data Infrastructure", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=POST("structify-makes"),
    entry_date="2025-04", grad="censored",
    note="AI-built structured datasets through an API (New York, aligned with 8VC). 'We're thrilled to lead Structify's seed' (the "
         "firm's post, 2025-04-30); 'Structify launches with $4.1M' (VentureBeat). Inside 24 months, so censored. " + MC + "only "
         "the 2025 seed; no later round and no $1B+ figure found."))
L.append(cls("sunday-robotics", status="private", rng="1b_plus", usd=1150000000, val_src="web_verified", asof="2026-03-12",
    val_cite=NEWS("sunday-robotics", "Sunday raises $165M Series B"), extra={"valuation_range_source": "web_verified"},
    country="US", country_src="model_knowledge", city="Mountain View", focus="Industrial & Robotics",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("sunday-robotics", "Sunday raises $165M Series B"),
    entry_date="2026-03",
    note="Household robots (Mountain View, aligned with Coatue). 'Sunday raised $165 million in a Series B round, boosting its "
         "valuation to $1.15 billion'; 'Coatue led the round, with participation from major investors including Bain Capital "
         "Ventures' (jawlah.co, 2026-03-12), the day of the firm's post 'Robots, Finally at Home' (" + POST("robots-finally-at-home")
         + "). A Series B entry reads Growth. Mark: $1.15B at the Series B, aligned with Coatue's row."))
L.append(cls("swish", status="private", rng="below_1b", country="IN", country_src="web_verified",
    country_cite=NEWS("swish", "Bengaluru food delivery startup Swish raises $38M"), city="Bangalore", focus="Consumer & Marketplaces",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("swish", "Hara Global, Bain Capital Ventures lead"),
    entry_date="2026-03",
    note="10-minute food delivery (Bengaluru; spelled Bangalore to align with Accel). 'Hara Global, Bain Capital Ventures lead Swish's "
         "Series B round' (VCCircle, 2026-03-24; $38M, TechCrunch), with the firm's post of 2026-03-23 (" + POST("swish-rewiring") +
         "). A Series B entry reads Growth. A $24M round led by Bertelsmann India followed in September 2026 at about $175M "
         "(Entrackr). The Y Combinator 'Swish' (San Francisco) is a different company."))
L.append(cls("t-r-a-d-e-inc", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Tampa",
    focus="SaaS", stage="undetermined",
    note="T.R.A.D.E., Inc. (Tampa, FL): 'Collector, distributor of info. Regarding import and export info. U.S.', Acquired (the "
         "firm's 2006 past-portfolio page; also on the 2003 list). No source read names the acquirer, the round or its date. The Y "
         "Combinator 'Trade' (Broken Arrow, OK) is a different company."))
L.append(cls("targetspot", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="New York",
    focus="Media, Gaming & Advertising", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=SIB("union-square-ventures", "targetspot", "entry_stage_citation"), entry_date="2008-03",
    note="Internet radio ad network (New York). USV's post of 2008-03-11: TargetSpot closed an '$8.6mm Series B round led by Bain "
         "Capital Ventures'; a Series B entry reads Growth. Merged with Radionomy in 2014, aligned with USV's row."))
L.append(cls("tealium", status="private", rng="below_1b", city="San Diego", focus="SaaS",
    stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.prnewswire.com/news-releases/tealium-announces-307-million-of-additional-growth-financing-300037016.html",
    entry_date="2015-02",
    note="Customer data platform (San Diego). '$30.7 million in Series D financing ... led by ... Georgian Partners, complemented by a "
         "major investment from Bain Capital Ventures' (PR Newswire, 2015-02-17); a Series D entry reads Growth. The 2019 Series F "
         "valued it at $850M (Wikipedia); no later priced figure read, so below_1b, aligned with Battery."))
L.append(cls("tecton-databricks", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="Data Infrastructure", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=POST("tecton-feature"),
    entry_date="2022-07",
    note="ML feature platform (San Francisco). 'We are thrilled to be working with ... the Tecton team by investing in their $100m "
         "Series C' (the firm's post, 2022-07-13). Databricks acquired it ('Tecton is Joining Databricks', 2025-08-22, "
         + NEWS("tecton-databricks", "Tecton is Joining Databricks") + "); the firm's listing reads Acquired."))
L.append(cls("terrafirma", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="Buda",
    focus="Industrial & Robotics", stage="Seed", **site_stage("terrafirma"), entry_date="2024",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("terrafirma", "Raises $115 Million Series A"),
    note="Semi-autonomous heavy construction machinery (Buda, TX, its new headquarters, " + NEWS("terrafirma", "taps Buda as new HQ")
         + "). BCV's listing: 2024, Seed (Ajay Agarwal). 'TerraFirma Raises $115 Million Series A' (citybiz, 2026-07-14). No "
         "valuation was published.",
    rounds=[rnd("2026-07", "Series A", 115000000, None, None, NEWS("terrafirma", "Raises $115 Million Series A"), "press")]))
L.append(cls("the-corner-pharmacy", status="unknown", rng="below_1b", country="US", country_src="model_knowledge", city="St. Louis",
    focus="Healthcare & Bio", stage="undetermined",
    note="Pharmacy business in the St. Louis area (13537 Barrett Parkway, per the firm's 2010-2013 listings, James Nahirny). The firm "
         "dropped it after 2013 and no source read (Google News, a web search) gives the round or its fate."))
L.append(cls("the-receivables-exchange", status="acquired", rng="below_1b", country="US", country_src="model_knowledge",
    city="New Orleans", focus="Fintech & Payments", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.businesswire.com/news/home/20100127005105/en/Receivables-Exchange-Closes-17-Million-Series-Financing",
    entry_date="2010-01",
    note="Online marketplace for trade receivables (New Orleans). 'The Receivables Exchange Closes $17 Million Series C Financing from "
         "Bain Capital Ventures' (Business Wire, 2010-01-27), after Redpoint's 2009 Series B; a Series C entry reads Growth. The firm "
         "lists it as exited; status acquired aligned with Redpoint's row, though no source read names the buyer."))
L.append(cls("the-sentience-company", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="New York",
    focus="AI & Applied AI", stage="Seed", **site_stage("the-sentience-company"), entry_date="2026", grad="censored",
    note="Personal AI that acts like its user (Sentience; Williamsburg, New York City, per the company's careers page). BCV's listing: "
         "2026, Seed (Kevin Zhang); launched 2026-03-26 (" + NEWS("the-sentience-company", "Sentience Launches") + "). Inside 24 "
         "months, so censored. " + MC + "only the launch; no priced figure found."))
L.append(cls("the-tennis-channel", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Santa Monica",
    focus="Media, Gaming & Advertising", stage="undetermined",
    note="Cable network for tennis (Santa Monica). Founded 2001; the founding group 'rounded up additional investors, Bain Capital "
         "Ventures, J.P. Morgan Partners, Battery Ventures, Columbia Capital, Pete Sampras and Andre Agassi, who as a group invested "
         "about $100 million' (Wikipedia, Tennis Channel); launched May 2003. Sinclair bought it for $350M in 2016. The round BCV "
         "entered is not named."))
L.append(cls("the-yes", rng="below_1b", city="San Francisco", focus="Consumer & Marketplaces", stage="undetermined",
    note="AI fashion shopping app (San Francisco, the launch dateline). 'The Yes raised $30M in funding from ... Forerunner Ventures, "
         "... True Ventures and ... NEA, as well as Comcast Ventures and Bain Capital Ventures' (PR Newswire, 2020-05-20, "
         + NEWS("the-yes", "Reimagines The Future") + "); the $30M spans more than one round and none is named. Pinterest acquired "
         "it in 2022."))
L.append(cls("thor-technologies", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="New York",
    focus="Security", stage="undetermined",
    note="Identity provisioning software (New York): 'Enterprise software for security and user management', Acquired (the firm's 2006 "
         "past-portfolio page; on the 2003 list, Jeff Schwartz). Oracle bought it in 2005. The round BCV entered is not named."))
L.append(cls("thoropass", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="New York",
    focus="Security", stage="Growth", **site_stage("thoropass"), entry_date="2021",
    note="Compliance and audit platform (Laika, renamed Thoropass; New York). BCV's listing: 2021, Growth (Matt Harris); 'Laika bags "
         "$35m from J.P Morgan-led Series B', with 'participation from ... Bain Capital Ventures' (FinTech Global, 2021-11-08, "
         + NEWS("thoropass", "Laika bags $35m") + "). Business Insider named 'Bain Capital' in the $10M Series A of September 2020; "
         "under D7 the parent's name is not BCV, so the listing's 2021 Growth entry stands. " + MC + "no priced round at $1B or "
         "more found (a GetLatka revenue estimate only)."))
L.append(cls("tomo", status="private", rng="below_1b", country="US", country_src="model_knowledge", flags=["city_unknown"],
    focus="AI & Applied AI", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("tomo", "Led By Bain Capital Ventures"),
    entry_date="2026-06", grad="censored",
    note="Personal AI coach. 'Tomo Raises $5 Million Seed Round Led By Bain Capital Ventures' (Pulse 2.0, 2026-06-26), with Accel, "
         "Conviction and Pear VC. Inside 24 months, so censored. No source read places the company. " + MC + "only the $5M seed."))
L.append(cls("topography-health", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="Los Angeles",
    focus="Healthcare & Bio", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=POST("topography-health-ceo"),
    entry_date="2022-01",
    note="Clinical trials run by community physicians ('Hollywood Hills West-based', LA Business Journal, "
         + NEWS("topography-health", "Topography Health Raises $21.5M") + "). 'BCV led Topography's $21.5M Series A' (the firm's post); "
         "a16z led the 2020 seed. In May 2026 it sold its clinical research site operations to FOMAT and kept its technology platform "
         "('Topography is focused exclusively on scaling its technology platform', " + NEWS("topography-health", "Westcove Advises")
         + "), so it stays private."))
L.append(cls("trucksmarter", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="Fintech & Payments", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("trucksmarter", "TruckSmarter Shutting Down"), entry_date="2022-09",
    note="Load board, factoring and payments for truckers (founded 2021 in San Francisco). 'a $25 million Series B in 2022 led by Thrive "
         "Capital, with participation from Bain Capital Ventures, Founders Fund and Andreessen Horowitz' (FreightWaves); the firm's "
         "listing: 2022, Growth. 'TruckSmarter announced on Tuesday that it has been acquired and that its driver app, Dispatch, shuts "
         "down on Friday, September 4' (FreightWaves, 2026-09-02); the buyer is not named and FreightWaves suspects an acqui-hire; OTR "
         "Solutions bought the factoring and banking division in November 2025. Read acquired on the company's own announcement "
         "(COLLECTION.md s6, acqui-hire rule). Fresher than the a16z and Thrive rows, which still read private."))
L.append(cls("truemotion", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Boston",
    focus="Fintech & Payments", stage="Seed", stage_src="model", stage_conf="medium", entry_date="2014-01",
    grad="graduated", grad_src="web_verified", grad_conf="high",
    grad_cite="https://finance.yahoo.com/news/censio-announces-close-10-million-130300574.html?_guc_consent_skip=1553340304",
    note="Smartphone driving telematics for insurers (Censio, renamed TrueMotion; Boston). The firm's Censio page was captured "
         "2014-01-23, before 'a $10 million Series A round ... led by General Catalyst Partners and included funding from Bain Capital "
         "Ventures and Lakestar', which 'brings total equity capital raised to more than $13 million' (press release, 2015-10-06); "
         "BCV's entry is the pre-A round, read as the seed and dated no later than January 2014. Cambridge Mobile Telematics acquired "
         "TrueMotion in June 2021 (" + NEWS("truemotion", "Cambridge Mobile Telematics acquires TrueMotion") + ").",
    rounds=[rnd("2015-10", "Series A", 10000000, "General Catalyst Partners", True,
                "https://finance.yahoo.com/news/censio-announces-close-10-million-130300574.html?_guc_consent_skip=1553340304", "press")]))
L.append(cls("truvideo", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="Wellesley",
    focus="SaaS", stage="Seed", **site_stage("truvideo"), entry_date="2019",
    grad="graduated", grad_src="web_verified", grad_conf="medium", grad_cite=NEWS("truvideo", "TruVideo Secures $40 Million Growth"),
    note="Video and texting for auto dealers' service departments (Wellesley, MA, per the firm's listing and the 2024 release). BCV's "
         "listing: 2019, Seed. 'TruVideo Secures $40 Million Growth Investment from TZP Growth Equity' (PR Newswire, 2024-12-10): an "
         "unnamed later round far above the $12M step-up an unrecorded 2019-21 seed needs (COLLECTION.md s6), so graduated; medium "
         "because the release gives no round name.",
    rounds=[rnd("2024-12", "Growth equity", 40000000, "TZP Growth Equity", None,
                NEWS("truvideo", "TruVideo Secures $40 Million Growth"), "press")]))
L.append(cls("turnkey", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="New York",
    focus="Crypto & Web3", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("turnkey", "Series B Led by Bain Capital Crypto"), entry_date="2025-06",
    note="Wallet and key infrastructure (New York, aligned with Sequoia), on Bain Capital Crypto's list (published 2025-06-09). "
         "'Turnkey Raises $30M Series B Led by Bain Capital Crypto' (2025-06-09); an equity round, and a Series B entry reads Growth. "
         + MC + "a $12.5M round in May 2026 (" + NEWS("turnkey", "raises $12.5 million") + ") with no valuation published; no "
         "$1B+ figure found."))
L.append(verdict("usinternetworking", "not_member",
    "USinternetworking (the row absorbs the 2006 listing 'Interpath / USInternetworking', Expansion/Growth Buyout): USi, listed on "
    "NASDAQ since its 1999 IPO, filed a prepackaged Chapter 11 in January 2002 under which 'USi Holdings, an investment affiliate of "
    "Bain Capital Partners, LLC, will invest up to $106 million in USi' and 'When completed, Bain will own all of the equity in USi' "
    "(USi's 8-K press release, 2002-01-07); it emerged in May 2002 merged with Interpath (Wikipedia). A 100% acquisition by a Bain "
    "Capital private-equity affiliate of a listed company is neither a venture round nor a BCV desk position (COLLECTION.md s1 T3 "
    "control positions; decisions.md D1, D4). AT&T bought it in 2006.",
    ec="site_listing", conf="high", cite="https://www.sec.gov/Archives/edgar/data/0001076732/000095013302000157/w56745ex99-1.htm")
    | {"exclusion": "control_position"})
L.append(cls("variational-research", status="private", rng="below_1b", country="KY", country_src="web_verified",
    country_cite=NEWS("variational-research", "Variational raises $50 million Series A"), flags=["city_unknown"],
    focus="Crypto & Web3", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("variational-research", "raises $10.3 million in seed"), entry_date="2021-12",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("variational-research", "Variational raises $50 million Series A"),
    note="Market maker, then a peer-to-peer derivatives protocol ('The Cayman Islands-based Variational', Fortune; no municipality "
         "given), on Bain Capital Crypto's list. 'Bain Capital Crypto and Peak XV Partners ... co-led' the $10.3M seed, which 'closed "
         "it in December' 2021 (The Block, 2024-10-23); an equity round. 'A $50 million Series A funding round led by Dragonfly "
         "Capital' with Bain Capital Crypto participating (Fortune, 2026-05-20). " + MC + "no valuation was published for the "
         "Series A; no $1B+ figure found.",
    rounds=[rnd("2026-05", "Series A", 50000000, "Dragonfly Capital", True,
                NEWS("variational-research", "Variational raises $50 million Series A"), "press")]))
L.append(cls("vauto", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Oak Brook",
    focus="SaaS", stage="undetermined", entry_date="2006",
    note="Used-vehicle inventory software for dealers (2221 Camden Court, Oak Brook, IL, per the firm's listing). 'vAuto was acquired "
         "by AutoTrader.com in September 2010' and BCV supported it 'since investing in 2006' (the firm's own case page, Michael "
         "Krupka). The 2006 round is not named."))
L.append(cls("verana-health", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="Healthcare & Bio", stage="Growth", stage_src="web_verified", stage_conf="medium",
    stage_cite=NEWS("verana-health", "Google Arm, Bain Lead"), entry_date="2020-02",
    note="Real-world clinical data from specialty registries (San Francisco). 'Google Arm, Bain Lead $100 Million Infusion for "
         "Health-Data Startup' (Bloomberg, 2020-02-05), the round before the $150M Series E of January 2022, so a Series D; BCV's "
         "listings from January 2020 (Growth, Yumin Choi) tie the 'Bain' of the headline to BCV (D7). Medium: the headline names the "
         "parent brand."))
L.append(cls("veza", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Palo Alto",
    focus="Security", stage="Seed", **site_stage("veza"), entry_date="2020",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("veza", "Series D at $808 Million"),
    note="Identity security (Palo Alto, aligned with Accel). BCV's listing: 2020, Seed (Enrique Salem), now tagged Acquired. Later "
         "named rounds include the $108M Series D at $808M (Business Wire, 2025-04-28). ServiceNow announced the purchase in December "
         "2025 and completed it in March 2026 ('following the completion of the acquisition in March this year', CRN Asia, "
         + NEWS("veza", "Veza integration") + "); fresher than Accel's row, which still reads private.",
    rounds=[rnd("2025-04", "Series D", 108000000, None, None, NEWS("veza", "Series D at $808 Million"), "press")]))
# ---- archive-only rows of the 2003-2014 listings
L.append(cls("solect", status="acquired", rng="below_1b", country="CA", country_src="web_verified",
    country_cite="https://www.theglobeandmail.com/report-on-business/us-firm-to-buy-solect-for-12-billion/article18421346/",
    city="Toronto", focus="SaaS", stage="undetermined",
    note="Read as Solect Technology Group, IP billing and customer care software: 'Amdocs Ltd. will buy Toronto-based Solect Technology "
         "Group Inc.' for about $1.2B in stock (The Globe and Mail, 2000-03-01), closed April 2000. The firm's 2003 list gives the "
         "name only, so the identification is by name; the article mentions a $33.5M venture round in January without naming its "
         "investors. The round BCV entered is not named."))
L.append(cls("soleil-securities", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="New York",
    focus="Fintech & Payments", stage="undetermined",
    note="Independent research broker-dealer (New York): 'Operates a sales and trading platform to collect revenue from asset managers "
         "for independent buy-side research' (the firm's 2006 page, Expansion/Growth Buyout, Jeff Schwartz). 'Soleil Securities was "
         "acquired by Ticonderoga Securities on May 2011' (the firm's listing). Vendor profiles record an $11M Series B led by BCV in "
         "March 2005 (a minority round, not a buyout); no press or filing read names it, so the stage stays open."))
L.append(cls("stoneacre-partners", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Wakefield",
    focus="Media, Gaming & Advertising", stage="undetermined",
    note="Coalition loyalty marketing and NASCAR-branded membership clubs (Wakefield, MA): the firm's 2006 page ('Early'), Acquired on "
         "its 2014 listing. No source read names the acquirer or the round."))
L.append(verdict("the-lifelike-company", "not_member",
    TAG + "Another desk (decisions.md D2, R1): The Lifelike Company (My Twinn dolls; Littleton, CO; 'Manufacturer and marketer of "
    "toy dolls and accessories', Acquired, on the firm's 2006 past-portfolio page). As chief executive of Bain Capital, 'Romney "
    "invested $2.1 million in 1996 for a stake in the company' (the Wall Street Journal's report, quoted by the Daily Republic, "
    "2012). A 1996 position of Bain Capital's generalist funds, made before any Bain Capital venture vehicle existed; the firm's own "
    "2006 page files such deals under 'Bain Capital's history of investing ... since 1984' (" + HISTORY + ").",
    ec="site_listing", conf="medium",
    cite="https://www.dailyrepublic.com/all-dr-news/opinion/state-national-columnists/romney-a-perfect-doll/"))
control("swift-prepaid-solutions",
    "Swift Prepaid Solutions (BCV's listing 2019-2022, Growth, Matt Harris): 'Syncapay, a new holding company focused on "
    "high-potential payments solutions has launched with the backing of Bain Capital Ventures, Silversmith Capital Partners, "
    "MissionOG, Nyca Partners' and 'Syncapay's first acquisition, Swift Prepaid Services, was made late last year' (PR Newswire, "
    "Dallas, 2018-05-02). BCV's money reached Swift through a holding company its investor group formed to buy the business "
    "outright; renamed daVinci Payments (2019) and merged into Onbe on Centerbridge's majority investment (2020). OPEN for Erik: the "
    "release does not state the group's share of Syncapay; if BCV held a minority stake in Syncapay, the row is a member under the "
    "holding company's name.",
    "https://www.prnewswire.com/news-releases/payments-industry-veterans-launch-syncapay-to-maximize-the-success-of-disruptor-"
    "payments-companies-300641028.html", conf="medium")

if __name__ == "__main__":
    jl.write("batch-011", L)
