"""PRO-162 grind, batch-004 (netdata .. sigfig). Evidence as in judgments-1.py; web checks 2026-09-27
for Noteable and Ribbon (WebSearch, results cited per line). ShiftLeft is Qwiet AI under its old name
and merges at the rebuild (identity-merges.json), so it is not classified here."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd, POST, SITE, W, NEWS, CCPAGE = jl.cls, jl.verdict, jl.rnd, jl.POST, jl.SITE, jl.W, jl.NEWS, jl.CCPAGE
L = []


def site_stage(slug):
    return dict(stage_src="first_party", stage_conf="medium", stage_cite=SITE(slug))


L.append(cls("netdata", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="Data Infrastructure", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=W("Netdata"), entry_date="2019-09",
    flags=["stage_disputes_band"],
    note="Open-source infrastructure monitoring (San Francisco). 'In September 2019, Netdata announced a $17 million Series A funding round "
         "led by Bain Capital Ventures' (Wikipedia), extended to $31M in 2020; the documented round overrides the listing's Seed tag."))
L.append(cls("nightfall-shoreline-labs", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="Security", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=POST("cloud-native-data-loss"), entry_date="2018",
    grad="graduated", grad_src="first_party", grad_conf="high", grad_cite=POST("cloud-native-data-loss"),
    note="Cloud data-loss prevention (San Francisco). 'Our partnership with Nightfall started when we co-led its seed round last year' and BCV "
         "co-led the $20.3M Series A (the firm's post, 2019-11-07); a $40M Series B followed in 2022.",
    rounds=[rnd("2019-11", "Series A", 20300000, "Bain Capital Ventures and Venrock", True, POST("cloud-native-data-loss"), "firm")]))
L.append(cls("noteable", status="defunct", rng="below_1b", city="Cupertino", focus="Data Infrastructure",
    note="Collaborative data notebooks (Cupertino). Announced its shutdown in December 2023 ('Noteable.io is shutting down', "
         "https://news.ycombinator.com/item?id=38659315). Entry from the filings (2020 seed, Aaref Hilaly). Graduation left for the "
         "graduation pass."))
L.append(cls("novus-sei-investments", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="New York",
    focus="Fintech & Payments", stage="undetermined",
    note="Portfolio analytics for asset owners (New York). Acquired by SEI (the firm's listing). BCV's 2013 round is not named."))
L.append(cls("nubisio-tracxn", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", flags=["city_unknown"],
    focus="Data Infrastructure", stage="undetermined",
    note="Cloud storage gateway ('bottomless storage'); the firm lists it as acquired. BCV's 2012 round is not named; no source places the company."))
L.append(cls("observeit-proofpoint", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Boston",
    focus="Security", stage="undetermined",
    note="Insider-threat management (Boston). Acquired by Proofpoint in 2019. BCV's 2013 round is not named."))
L.append(cls("onera-acquired-by-lyniate-in-2021", status="acquired", rng="below_1b", country="US", country_src="model_knowledge",
    city="Burlingame", focus="SaaS", stage="undetermined",
    note="Retail inventory data (Burlingame). Acquired by Lyniate in 2021 (the firm's listing). BCV's 2014 round is not named."))
L.append(cls("openfin", status="private", rng="below_1b", city="New York", focus="Fintech & Payments", stage="undetermined",
    note="Desktop operating layer for finance (New York); a $35M Series D led by Bank of America in 2023. BCV entered in 2014 (Matt Harris) "
         "in a company incorporated in 2010; the band is withheld and the round is not named."))
L.append(cls("optimizely-episerver", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="SaaS", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=W("Optimizely"), entry_date="2013",
    note="Experimentation platform (San Francisco). BCV joined the 2013 round Benchmark led ('with participation from Bain Capital Ventures', "
         "Wikipedia), Optimizely's first large institutional round after its seed. Acquired by Episerver in 2020."))
L.append(cls("orum", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="New York",
    focus="Fintech & Payments", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=POST("taking-on-a-70"), entry_date="2020-08",
    grad="graduated", grad_src="first_party", grad_conf="high", grad_cite=POST("taking-on-a-70"),
    note="Real-time money movement (New York). 'BCV first invested in Orum's $5.2 million seed round in August 2020, then led its $21 million "
         "Series A in April 2021' (the firm's post). Stripe acquired Orum in July 2025 (" + NEWS("orum", "Stripe Acquires Orum for Undisclosed") + ").",
    rounds=[rnd("2020-08", "Seed", 5200000, None, True, POST("taking-on-a-70"), "firm"),
            rnd("2021-04", "Series A", 21000000, "Bain Capital Ventures", True, POST("taking-on-a-70"), "firm")]))
L.append(cls("oyster-com-tripadvisor", status="acquired", rng="below_1b", city="New York", focus="Consumer & Marketplaces",
    note="Hotel reviews (New York). Acquired by TripAdvisor (the firm's listing). Graduation left for the graduation pass."))
L.append(cls("passport-arrive", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Charlotte",
    focus="SaaS", stage="Growth", **site_stage("passport-arrive"), entry_date="2017",
    note="Parking and mobility payments (Charlotte). BCV's listing: 2017, Growth (Matt Harris). Now part of Arrive (the firm lists "
         "'Passport (Arrive)', Acquired)."))
L.append(cls("persado", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="New York",
    focus="AI & Applied AI", stage="undetermined",
    note="AI marketing language (New York); a $15M round in early 2013 and a $30M Goldman-led round in 2016. BCV's listing gives 2012 "
         "(Scott Friend); the round is not named."))
L.append(cls("playbook", status="private", rng="below_1b", city="San Francisco", focus="SaaS",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("playbook", "Raises $18M Series A Led by Bain"),
    entry_date="2022-04",
    note="Creative file management (San Francisco). 'Playbook Raises $18M Series A Led by Bain Capital Ventures' (PR Web, 2022-04-19)."))
L.append(cls("pleo", city="Copenhagen", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=POST("bcv-co-leads-150m"),
    entry_date="2021-07",
    note="Spend management (Copenhagen). 'BCV Co-Leads $150M Series C Round In Pleo' (the firm's post, 2021-07-06); 'BCV first invested in "
         "Pleo's Series C'. The prefilled $4.7B is the December 2021 extension."))
L.append(cls("precision-therapeutics", status="acquired", rng="below_1b", city="Pittsburgh", focus="Healthcare & Bio",
    note="Cancer drug-response testing (Pittsburgh); combined into Predictive Oncology. BCV's 2010 round from the filings."))
L.append(cls("prisma-sd-wan-palo-alto-networks", status="acquired", rng="below_1b", country="US", country_src="model_knowledge",
    city="San Jose", focus="Data Infrastructure", stage="undetermined",
    note="Cloud-delivered SD-WAN (CloudGenix, San Jose). Palo Alto Networks bought it in 2020 and sells it as Prisma SD-WAN. BCV's round "
         "(by 2015, Enrique Salem) is not named."))
L.append(cls("quanterix", city="Billerica", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2007",
    note="Ultrasensitive biomarker detection (Billerica, MA). BCV listed it from 2007 (Bain Capital Venture Fund 2005, a pre-IPO holder per its "
         "2017 S-1), at the company's 2007-2008 first institutional round beside ARCH and Flagship. IPO December 2017."))
L.append(cls("rapid7", city="Boston", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2008-09",
    flags=["stage_disputes_band", "cite_pending"],
    note="Security analytics (Boston). 'In September 2008, Rapid7 received its first institutional funding, a $7 million investment from Bain "
         "Capital Ventures' (Wikipedia; Ben Holzman on the board since August 2008, its S-1): the first institutional round of a bootstrapped "
         "company, read as its Series A. The Form D band read a 2010 filing as Seed. IPO July 2015 (NASDAQ: RPD)."))
L.append(cls("rave-mobile-safety", city="Framingham", rng="below_1b", stage="undetermined",
    note="Public-safety communications (Framingham, MA). 'Early investors included Bain Capital Ventures, Sigma Partners, and RRE Ventures' "
         "(Wikipedia); Motorola Solutions acquired Rave in 2022. The round is not named."))
L.append(cls("recharge", status="private", rng="1b_plus", country="US", country_src="model_knowledge", city="Santa Monica",
    focus="Fintech & Payments", usd=2100000000, val_src="web_verified", asof="2021-05",
    val_cite=NEWS("recharge", "Reaches $2.1bn Valuation"), extra={"valuation_range_source": "web_verified"},
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("recharge", "$277 Million in Growth Capital"),
    entry_date="2021-05", flags=["stale"],
    note="Subscription payments for e-commerce (Santa Monica). 'ReCharge Announces $277 Million in Growth Capital from Summit Partners, ICONIQ "
         "Growth and Bain Capital Ventures' (businesswire, 2021-05-06), at $2.1B; stale beyond 24 months."))
L.append(cls("red-balloon-security", status="private", rng="below_1b", city="New York", focus="Security",
    note="Embedded-device security (New York). BCV led the $21.9M Series A (the firm's post, 2018-04-03), the round the filings give."))
L.append(cls("redis", city="Mountain View", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=W("Redis (company)"),
    entry_date="2013", usd=2000000000, val_src="web_verified", asof="2021-04-07",
    val_cite=NEWS("redis", "valued at over $2 billion"), extra={"valuation_range_source": "web_verified"},
    flags=["stale", "model_disputes_source"],
    note="In-memory database (Mountain View). '$9 million in series A funding led by Bain Capital Ventures and Carmel Ventures' after an angel "
         "seed (Wikipedia; the firm lists 2012). Mark: the April 2021 round at over $2B (Reuters), fresher than the prefilled $1B; stale."))
L.append(cls("regulatory-datacorp", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="New York",
    focus="Fintech & Payments", stage="undetermined",
    note="Risk and compliance screening (RDC, New York). Acquired by Moody's in 2020 (the firm lists it as acquired). BCV's 2007 round is not named."))
L.append(cls("relay-financial", status="private", rng="below_1b", city="Toronto", focus="Fintech & Payments",
    stage="Seed", **site_stage("relay-financial"), entry_date="2020",
    grad="graduated", grad_src="first_party", grad_conf="high", grad_cite=POST("running-with-business-owners"),
    note="Small-business banking (Toronto). BCV's listing: 2020, 'Seed, Early'; BCV then led the $15M Series A ('BCV is leading a $15M Series A "
         "for Relay Financial', the firm's post, 2021-05-13), which graduates it; a $50M round followed in 2026.",
    rounds=[rnd("2021-05", "Series A", 15000000, "Bain Capital Ventures", True, POST("running-with-business-owners"), "firm")]))
L.append(cls("remedy-partners", status="acquired", rng="below_1b", city="Darien", focus="Healthcare & Bio",
    note="Bundled-payment programmes (Darien, CT). Combined into Signify Health in 2019 (Signify's filings name BCV's funds)."))
L.append(cls("rent-the-runway", city="New York"))
L.append(cls("rentomojo", status="private", rng="below_1b", country="IN", country_src="web_verified",
    country_cite=NEWS("rentomojo", "raises $10 mn from Bain Capital"), city="Bangalore", focus="Consumer & Marketplaces",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("rentomojo", "as Series B funding"), entry_date="2017-07",
    note="Furniture and appliance rental (Bangalore). BCV's 2017 entry was the $10M Series B (YourStory, VCCircle 2017-07-19). SEBI cleared its "
         "IPO in July 2026; still private."))
L.append(cls("reonomy-altus-group", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="New York",
    focus="SaaS", stage="undetermined",
    note="Commercial real-estate data (New York). Acquired by Altus Group in 2021 (the firm's listing). BCV's 2014 round is not named."))
L.append(cls("reprise", status="private", rng="below_1b", city="Boston", focus="SaaS",
    note="Product demo platform (Boston); $62M Series B from ICONIQ in 2021. Entry from the filings (Ajay Agarwal, 2020)."))
L.append(cls("reserv", status="private", rng="below_1b", city="New York", focus="Fintech & Payments",
    stage="Seed", **site_stage("reserv"), entry_date="2022", flags=["stage_disputes_band"],
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("reserv", "raises $125m Series C led by KKR"),
    note="AI claims administration (New York). BCV's listing: 2022, Seed (Matt Harris); the 2023 filing is the Series A ('after raising their "
         "series A', the firm's post); a $125M Series C followed in 2026.",
    rounds=[rnd("2026-05", "Series C", 125000000, "KKR", None, NEWS("reserv", "raises $125m Series C led by KKR"), "press")]))
L.append(cls("ribbon", status="acquired", rng="below_1b", city="New York", focus="Fintech & Payments",
    note="Cash-offer home buying (Ribbon Home, New York); $330M financing in 2019. Paused in late 2024; Hurst Lending bought its brand, "
         "technology and assets in 2025 (https://ribbonhome.com/post/is-ribbon-home-still-operating/): an asset sale, so acquired "
         "(COLLECTION.md s6). Sibling Greylock reads defunct."))
L.append(cls("roofstock", status="private", rng="1b_plus", city="Oakland", focus="Fintech & Payments",
    usd=1900000000, val_src="web_verified", asof="2022-03-10", val_cite=NEWS("roofstock", "raises USD240M at USD1.9B"),
    extra={"valuation_range_source": "web_verified"}, flags=["stale"],
    note="Single-family rental marketplace (Oakland). Mark: the $240M round of March 2022 at $1.9B; layoffs followed in 2022-23 without a "
         "priced down round; stale. Graduation left for the graduation pass."))
L.append(cls("rubrik", city="Palo Alto", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=POST("how-the-importance-of-data"),
    entry_date="2019-01",
    note="Data security (Palo Alto). 'We are excited to announce our participation in Rubrik's $261 million Series E financing' (the firm's "
         "post, 2019); IPO April 2024 (NYSE: RBRK)."))
L.append(cls("sansoro-health", status="acquired", rng="below_1b", city="Minneapolis", focus="Healthcare & Bio", stage="undetermined",
    note="Healthcare integration APIs (Minneapolis). Merged with Datica in June 2019 (Fierce Healthcare). BCV's 2017 round (Yumin Choi) sits in "
         "a company incorporated in 2014; the band is withheld and the round is not named."))
L.append(cls("scalearc-ignitetech", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Santa Clara",
    focus="Data Infrastructure", stage="undetermined",
    note="Database load balancing (Santa Clara). Acquired by IgniteTech (the firm's listing). BCV's 2015 round is not named."))
L.append(cls("scalebase", status="acquired", rng="below_1b", city="Boston", focus="Data Infrastructure", stage="undetermined",
    note="Distributed MySQL (Boston); the firm lists it as acquired. BCV's 2012 round is not named."))
L.append(cls("scorebig-ticketnetwork", status="acquired", rng="below_1b", city="Los Angeles", focus="Consumer & Marketplaces",
    note="Discounted event tickets (Los Angeles). Acquired by TicketNetwork (the firm's listing). Graduation left for the graduation pass."))
L.append(cls("semantic-machines-microsoft", status="acquired", rng="below_1b", city="Berkeley", focus="AI & Applied AI",
    note="Conversational AI (Berkeley and Boston). Microsoft acquired it in May 2018. Entry from the filings (Scott Friend, 2015)."))
L.append(cls("sendgrid-acquired-by-twilio-in-2018", status="acquired", rng="below_1b", city="Denver", focus="DevTools & APIs",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=W("SendGrid"), entry_date="2014", flags=["stage_disputes_band"],
    note="Email API (Denver). 'The series C round was led by a new investor Bain Capital Ventures' (Wikipedia, 2014). IPO 2017; Twilio "
         "acquired it in 2019. The Form D band read a later filing as Seed."))
L.append(cls("sevone-turbonomic", status="acquired", rng="below_1b", city="Wilmington", focus="Data Infrastructure",
    note="Network performance monitoring (Wilmington, DE). Acquired by Turbonomic (the firm's listing), itself bought by IBM."))
L.append(cls("shieldx-fortinet", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="San Jose",
    focus="Security", stage="undetermined",
    note="Cloud security (San Jose). Its assets went to Fortinet in 2020 (the firm lists 'ShieldX (Fortinet)'). BCV's round (by 2015) is not named."))
L.append(cls("shipbob", status="private", rng="below_1b", city="Chicago", focus="Consumer & Marketplaces", stage="undetermined",
    note="E-commerce fulfilment (Chicago). BCV led the $200M Series E of June 2021 'valuing the ecommerce logistics platform well over $1 "
         "billion' (PR Newswire): no figure was published, so no mark can be recorded and the row stays below_1b (COLLECTION.md s6 Rule A: a "
         "1b_plus band needs a citable figure; sibling Menlo reads the same). BCV's listing gives 2017; the 2017 round is not named."))
L.append(cls("sigfig", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="Fintech & Payments", stage="undetermined",
    note="Wealth-management software for banks (San Francisco); a $40M round with big banks in 2016 and a General Atlantic-led Series E in 2025. "
         "BCV's listing gives 2013; the round is not named."))

if __name__ == "__main__":
    jl.write("batch-004", L)
