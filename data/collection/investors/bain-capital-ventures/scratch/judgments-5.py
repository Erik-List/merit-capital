"""PRO-162 grind, batch-005 (signifyd .. aboon). Evidence as in judgments-1.py, plus Wikipedia extracts cached under
scratch/wiki/ (wikifetch.py) and Google News (nq.py, news-extra.json). Three control positions surfaced from the
companies' own filings or histories: SolarWinds (S-1: investors led by BCV and Insight bought 67.8% in the December 2005
recapitalisation; Insight's run excluded the same deal), SurveyMonkey (Spectrum Equity and Bain Capital bought a
majority in 2009) and Zelis (the 2019 Zelis-RedCard combination under Parthenon and Bain Capital). SquareTrade's 2012
deal was reported as a $238M growth equity investment; whether it carried control is an open question for Erik."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd, POST, SITE, W, NEWS, CCPAGE = jl.cls, jl.verdict, jl.rnd, jl.POST, jl.SITE, jl.W, jl.NEWS, jl.CCPAGE
L = []


def site_stage(slug):
    return dict(stage_src="first_party", stage_conf="medium", stage_cite=SITE(slug))


def control(slug, why, cite, conf="high"):
    L.append(verdict(slug, "not_member",
        why + " A control acquisition is not a venture round (COLLECTION.md s1 T3 control positions; decisions.md D4): the firm "
        "with its co-investor group took 50% or more.", ec="site_listing", conf=conf, cite=cite) | {"exclusion": "control_position"})


L.append(cls("signifyd", status="private", rng="1b_plus", usd=1340000000, val_src="web_verified", asof="2021-04",
    val_cite=W("Signifyd"), extra={"valuation_range_source": "web_verified"}, country="US", country_src="model_knowledge",
    city="San Jose", focus="Security", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=W("Signifyd"),
    entry_date="2017", flags=["stale"],
    note="E-commerce fraud protection (San Jose). 'In 2017, it raised $56 million in Series C funding led by Bain Capital Ventures' "
         "(Wikipedia). Mark: the $205M Series E of April 2021 at $1.34B, aligned with a16z and Menlo; stale beyond 24 months."))
L.append(cls("skai-kenshoo", status="private", rng="below_1b", country="IL", country_src="web_verified",
    country_cite=NEWS("skai-kenshoo", "Marketing Companies in Israel"), city="Tel Aviv", focus="Media, Gaming & Advertising",
    stage="Growth", **site_stage("skai-kenshoo"), entry_date="2014",
    note="Omnichannel marketing platform (Kenshoo, renamed Skai in 2021; Tel Aviv, with offices in New York). BCV's listing: 2014, "
         "Growth. The round is not named."))
L.append(cls("smartrent", city="Scottsdale"))
L.append(cls("sneakpeeq", status="unknown", rng="below_1b", city="San Francisco", city_src="formd_address",
    note="Social shopping site (2011 Form D, Ajay Agarwal). The firm listed it in 2011-2013 only; no source read gives its fate. "
         "Graduation left for the graduation pass."))
L.append(cls("socure", city="Incline Village", stage="Growth", **site_stage("socure"), entry_date="2021",
    usd=5200000000, val_src="web_verified", asof="2026-08",
    val_cite="https://news.crunchbase.com/venture/socure-raises-acquires-agentic-ai-startup-fravity/",
    extra={"valuation_range_source": "web_verified"}, flags=["model_disputes_source"],
    note="Identity verification (Incline Village, NV; the firm's listing still says New York). BCV's listing: 2021, Growth (Merritt "
         "Hummer), the year of the $100M Series D and the $450M Series E at $4.5B. Mark: the August 2026 round at $5.2B, aligned with "
         "Accel, fresher than the prefilled 2021 figure."))
L.append(verdict("solarwinds", "not_member",
    "SolarWinds' S-1 (2008-03-21): 'In December 2005, investors led by Bain Capital Ventures and Insight Venture Partners acquired an "
    "aggregate of 67.8% of our outstanding capital stock from our original stockholders and we recapitalized our company', with $110M "
    "of new debt. A majority recapitalisation by the firm and its co-investor group (COLLECTION.md s1 T3 control positions; decisions.md "
    "D4). Insight's run excluded the same deal as a control position.",
    ec="site_listing", conf="high", cite="https://www.sec.gov/Archives/edgar/data/1428669/000119312508062588/ds1.htm")
    | {"exclusion": "control_position"})
L.append(cls("soona", status="private", rng="below_1b", city="Denver", focus="Consumer & Marketplaces",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=POST("bcv-leads-35m-investment-in-soona"), entry_date="2022-01",
    note="Virtual product photo and video shoots (Denver). 'BCV Leads $35M Investment In soona' ('we're so excited to lead the recent "
         "$35M Series B round', the firm's post, 2022-01-24); a Series B entry reads Growth. The 2023 filing is a later round."))
L.append(cls("squaretrade-allstate", status="acquired", rng="below_1b", country="US", country_src="model_knowledge",
    city="San Francisco", focus="Fintech & Payments", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("squaretrade-allstate", "snags $238 million growth equity"), entry_date="2012-01",
    note="Consumer electronics protection plans (San Francisco). 'SquareTrade announced today it has secured a $238 million growth equity "
         "investment lead by Bain Capital' (CNET, 2012-01-25), with Bain Capital Venture Fund 2009 beside Bain Capital Fund X (the 2012 "
         "securityholder agreement, Allstate's 8-K of 2016-11-28). Allstate bought it for $1.4B in January 2017 'from a group of "
         "shareholders, including Bain Capital Private Equity and Bain Capital Ventures'. OPEN for Erik: no source read states the "
         "2012 ownership; the merger agreement's 'Contingent Consideration attributable to the Bain Capital Transaction' reads like "
         "acquisition accounting, which would make it a control position (D4)."))
L.append(cls("stackdriver-google", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Boston",
    focus="DevTools & APIs", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2012",
    note="Cloud monitoring as a service (Boston). 'Founded in 2012 ... and secured US$5 million in funding from Bain Capital Ventures' "
         "(Wikipedia), the company's first institutional round, read as its Series A; Google acquired it in May 2014."))
L.append(cls("startree-cortexdata", status="private", rng="below_1b", city="Mountain View",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("startree-cortexdata", "StarTree Secures $24 Million"),
    entry_date="2021-05", flags=["stage_disputes_band"],
    note="Real-time analytics on Apache Pinot (Mountain View). 'StarTree Secures $24 Million Funding' (GlobeNewswire, 2021-05-05): the "
         "seed and Series A BCV led at launch; the 2022 filing the band read is the $47M Series B."))
L.append(cls("stream", status="acquired", rng="below_1b", country="US", country_src="web_verified",
    country_cite=CCPAGE("/portfolio/company/stream"), city="Richardson", stage="undetermined", entry_date="2001",
    flags=["model_disputes_source"],
    note="Stream International, technical-support outsourcing (Richardson, TX, in the firm's 2006 listing, 'Expansion/Growth Buyout'). "
         "'Stream was acquired by Solectron (NYSE: SLR) in October 2001' (the firm's 2012 page), so the entry predates that; the round "
         "is not named. The prefilled Italian country and 'defunct' came from a wrong Wikidata join, and the 2009 Form D joined to the "
         "row is Stream Global Services (Wellesley, MA; listed), a different company."))
control("surveymonkey",
    "SurveyMonkey: 'In 2009, Spectrum Equity and Bain Capital acquired a majority stake in the company' (Wikipedia); the vehicle was SM "
    "Holdco LLC, and Bain Capital Venture Fund 2007 signed the registration-rights agreement filed with SVMK's 2018 S-1.",
    W("SurveyMonkey"))
control("sm-holdco-llc",
    "SM Holdco LLC is the holding company of SurveyMonkey's 2009 recapitalisation (merges into 'surveymonkey'), which carried a majority "
    "stake bought by Spectrum Equity and Bain Capital (Wikipedia). This replaces the membership recorded for the merge.",
    W("SurveyMonkey"))
L.append(cls("symphony-commerce", status="acquired", rng="below_1b", city="San Francisco", focus="SaaS", stage="undetermined",
    note="Commerce-as-a-service for brands (San Francisco). The firm lists it as acquired. BCV's 2011 entry (Ajay Agarwal) sits in a "
         "company incorporated in 2010; the round is not named."))
L.append(cls("synapdx", status="unknown", rng="below_1b", city="Waltham",
    note="Autism blood test (Waltham, MA); a 2013 round with Google Ventures. BCV led its 2010 Series A filing (James Nahirny). The firm "
         "dropped it after 2013 and no source read gives its fate."))
L.append(cls("sysdig", city="San Francisco", stage="Seed", **site_stage("sysdig"), entry_date="2013",
    usd=2500000000, val_src="web_verified", asof="2021-12",
    val_cite="https://www.sysdig.com/press-releases/350m-series-g-financing-2-5b-valuation",
    extra={"valuation_range_source": "web_verified"}, flags=["stale", "model_disputes_source"],
    note="Cloud and container security (Draios, San Francisco). BCV's listing: 2013, Seed (Salil Deshpande, whose post names Sysdig among "
         "his open-source investments); Accel's Series A followed. Mark: the $350M Series G at $2.5B (December 2021), aligned with Accel "
         "and Insight, not the prefilled $1.18B; stale. Graduation left for the graduation pass (Draios' filings merge at the rebuild)."))
L.append(cls("taleo", city="Dublin", rng="below_1b", stage="undetermined", entry_date="1999-11",
    note="Talent management software (Recruitsoft, later Taleo; Dublin, CA). Bain Capital Venture Fund, L.P. held Recruitsoft from "
         "November 1999 (Taleo's S-1, 2004), the venture family's first vehicle (decisions.md D2). IPO 2005; Oracle bought it for $1.9B "
         "in 2012. The 1999 round is not named."))
L.append(cls("tapcommerce-twitter", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="New York",
    focus="Media, Gaming & Advertising", stage="undetermined",
    note="Mobile ad retargeting (New York). 'Twitter Confirms Acquisition Of Mobile Ad Retargeting Startup TapCommerce' (TechCrunch, "
         "2014-06-30, " + NEWS("tapcommerce-twitter", "Twitter Confirms Acquisition") + "). BCV's 2013 round is not named."))
L.append(cls("tellapart-acquired-by-twitter-in-2015", status="acquired", rng="below_1b", city="Burlingame",
    note="Ad personalisation for retailers (Burlingame). Twitter acquired it in 2015 (the firm's listing)."))
L.append(cls("tengion", city="Winston-Salem", rng="below_1b", stage="undetermined",
    note="Regenerative medicine (East Norriton, PA, then Winston-Salem, NC). Bain Capital Venture Fund 2005 signed its investor rights "
         "agreement (S-1, 2009); IPO April 2010. The round BCV entered is not named."))
L.append(cls("thefind-meta", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Mountain View",
    focus="Consumer & Marketplaces", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=W("TheFind.com"),
    entry_date="2007",
    note="Product search (Mountain View). 'In 2007, they received an additional $15 million in funding led by Bain Capital Ventures' "
         "(Wikipedia): a follow-on round after the 2006 launch financing, read as its Series B. Facebook acquired it in 2015."))
L.append(cls("thumbplay", status="acquired", rng="below_1b", city="New York", focus="Media, Gaming & Advertising", stage="undetermined",
    note="Mobile entertainment (New York). Clear Channel acquired it in 2011 (Wikipedia). BCV's 2009 filing (Ajay Agarwal) sits in a "
         "company founded in 2004 with earlier rounds; the band is withheld and the round is not named."))
L.append(cls("tidalscale", status="acquired", rng="below_1b", city="Santa Clara", focus="Data Infrastructure", stage="undetermined",
    entry_date="2014",
    note="Software-defined servers (Santa Clara). HPE acquired it in 2023 (" + NEWS("tidalscale", "HPE Adds One More") + "). BCV's "
         "listing gives 2014 (Enrique Salem); the 2018 filing the band read is a later round; the entry round is not named."))
L.append(cls("tokbox", status="acquired", rng="below_1b", city="San Francisco", focus="DevTools & APIs",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=W("TokBox"), entry_date="2008-07",
    note="Embedded video API (San Francisco). 'July: Series B funding from Bain Capital Ventures and Sequoia Capital' (Wikipedia, 2008); "
         "a Series B entry reads Growth. Telefonica acquired it in October 2012."))
L.append(cls("total-attorneys-internet-brands", status="acquired", rng="below_1b", country="US", country_src="model_knowledge",
    city="Chicago", focus="SaaS", stage="undetermined",
    note="Practice-management software and marketing for lawyers (Chicago). Acquired by Internet Brands (the firm's listing). BCV's 2012 "
         "round is not named."))
L.append(cls("tracelytics", status="acquired", rng="below_1b", city="Providence",
    note="Application performance tracing (Providence, RI). Acquired by AppNeta in 2012. Graduation left for the graduation pass."))
L.append(cls("travelclick-amadeus", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="New York",
    focus="SaaS", stage="undetermined", entry_date="2003",
    note="Hotel revenue software (New York; Schaumburg, IL in the firm's 2003 listing). Genstar sold it to Thoma Bravo for $930M in 2014 "
         "and Amadeus bought it in 2018. BCV held it by 2003; the round is not named."))
L.append(cls("trooly-airbnb", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Los Altos",
    focus="Security", stage="undetermined",
    note="Online trust and background screening (Los Altos). 'Airbnb to Buy a Startup That Does Background Checks' (Fortune, 2017-06-16, "
         + NEWS("trooly-airbnb", "Airbnb to Buy a Startup") + "). BCV's 2015 round is not named."))
L.append(cls("turbonomic-ibm", status="acquired", rng="below_1b", city="Boston", stage="Series A", stage_src="model", stage_conf="medium",
    entry_date="2009", flags=["stage_disputes_band"],
    note="Application resource management (VMTurbo, renamed Turbonomic; Boston). BCV backed it from its 2009 founding (the firm's listing; "
         "Ben Nye later became CEO), the company's first institutional round, read as its Series A; the 2019 filing the band read is a "
         "late round. IBM acquired it in June 2021 (Wikipedia)."))
L.append(cls("txvia-google", status="acquired", rng="below_1b", city="New York",
    note="Prepaid and payments processing platform (New York). Google acquired it in 2011 (the firm's listing)."))
L.append(cls("unstructured", status="private", rng="below_1b", city="San Francisco",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=POST("how-unstructured"), entry_date="2022",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("unstructured", "Seed and Series A Funding"),
    flags=["stage_disputes_band"],
    note="LLM data preprocessing (San Francisco). The firm 'partnered at the seed' (its post, 2023-07-27); the Series A followed "
         "('Unstructured Secures $25 Million in Seed and Series A Funding', businesswire, 2023-07-19), then a $40M Series B led by Menlo "
         "(2024). The 2023 filing the band read is the Series A.",
    rounds=[rnd("2023-07", "Series A", None, "Madrona", None, NEWS("unstructured", "Seed and Series A Funding"), "press")]))
L.append(verdict("us-lec", "not_member",
    "US LEC was listed on NASDAQ (CLEC) from 1998; Bain Capital's position was preferred stock in the listed company, held as a 10% owner "
    "(Bain Capital Investors, LLC's Form 4 of 2007-03-02, with Michael Krupka). A placement into a public company is not a venture round "
    "(COLLECTION.md s1 T3; decisions.md D4). PAETEC acquired US LEC in 2007.",
    ec="site_listing", conf="high", cite="https://www.sec.gov/Archives/edgar/data/1054290/000118143107016258/0001181431-07-016258-index.htm"))
L.append(cls("venminder-digital-comply", status="acquired", rng="below_1b", country="US", country_src="model_knowledge",
    city="Elizabethtown", focus="Fintech & Payments", stage="undetermined",
    note="Third-party risk management (Elizabethtown, KY). Ncontracts acquired it in September 2024 ("
         + NEWS("venminder-digital-comply", "Ncontracts Acquires Third Party") + "). BCV's round (listing: 2012) is not named."))
L.append(cls("vention", status="private", rng="below_1b", country="CA", country_src="web_verified", country_cite=W("Vention"),
    city="Montreal", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=POST("hot-off-the-assembly"),
    entry_date="2019-01",
    note="Machine design and automation platform (Montreal). 'Our $13 million Series A investment in Montreal-based Vention' (the firm's "
         "post, 2019-01-15; 'in 2018, when we led the A round'). The prefilled US country was wrong."))
L.append(cls("vetsource", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Portland",
    focus="Healthcare & Bio", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=POST("our-50-million"),
    entry_date="2018-06",
    note="Pharmacy and software for veterinary clinics (Portland, OR). 'We're excited to lead a $50 million investment in Vetsource' (the "
         "firm's post, 2018-06-05; FinSMEs calls it the Series D). Mars took a controlling stake in 2021 ("
         + NEWS("vetsource", "Mars to take controlling stake") + ")."))
L.append(cls("voiceops", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="AI & Applied AI", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=POST("better-coaching"),
    entry_date="2019-08",
    note="Voice analytics for sales coaching (San Francisco). 'We are excited to announce our Series A investment in VoiceOps' (the firm's "
         "post, 2019-08-27)."))
L.append(cls("vonage", city="Holmdel", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2005",
    note="Consumer VoIP (Holmdel, NJ). Bain Capital Venture Fund 2005 held convertible preferred before the May 2006 IPO (its S-1): a "
         "late private round in a company founded in 1998, read as Growth. Ericsson acquired it in 2022 for $6.2B."))
L.append(cls("wonolo", status="private", rng="below_1b", city="San Francisco",
    note="On-demand staffing marketplace (San Francisco); $138M in new funding in 2021. BCV entered at the 2018 Series C (Jamison Hill; "
         "'Wonolo Raises $32M Series C', Crunchbase News, 2018-11-19)."))
L.append(cls("world", status="private", rng="1b_plus", usd=1310000000, val_src="web_verified", asof="2026-08",
    val_cite="https://www.coingecko.com/en/coins/worldcoin", extra={"valuation_range_source": "web_verified"},
    country="US", country_src="model_knowledge", city="San Francisco", focus="Crypto & Web3",
    stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("world", "Raises $115M in Series C Round"), entry_date="2023-05", flags=["stage_disputes_band"],
    note="World (Worldcoin), the proof-of-personhood network of Tools for Humanity (San Francisco), on Bain Capital Crypto's list. BCV "
         "entered at the $115M Series C led by Blockchain Capital (May 2023) and bought WLD tokens again in May 2025. Mark: the WLD "
         "token capitalisation, aligned with a16z's row. The 2009 Form D joined to the row (Alex Evans, issuer 'World') is a namesake "
         "filed twelve years before he joined BCV, so its Seed band is withdrawn."))
L.append(cls("wrike", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="San Jose", focus="SaaS",
    stage="Series A", stage_src="model", stage_conf="medium", entry_date="2013-10",
    note="Work management (San Jose). 'In October, 2013, Wrike secured $10 million in investment funding from Bain Capital' (Wikipedia; "
         "'With $10M Bet From Bain Capital Ventures', Forbes), its first institutional round after a small angel seed, read as its Series "
         "A. Citrix bought it for $2.25B in 2021."))
L.append(cls("xplenty-xenon", status="acquired", rng="below_1b", country="IL", country_src="web_verified",
    country_cite=NEWS("xplenty-xenon", "Xenon Ventures Buys Israeli"), city="Tel Aviv", focus="Data Infrastructure", stage="undetermined",
    note="Cloud data integration (Tel Aviv). 'Xenon Ventures Buys Israeli Cloud Company Xplenty' (Calcalist, 2018-12-19). BCV's 2014 "
         "round is not named."))
control("zelis",
    "Zelis: BCV's listing (2019, Growth, Matt Harris) is the 2019 combination of Zelis and RedCard under Parthenon Capital and Bain "
    "Capital ('Zelis, RedCard merge to form health care payments optimization platform', ROI-NJ, 2019-08-02), a sponsor-controlled "
    "merger, not a round (config verify.not_members).",
    NEWS("zelis", "Zelis, RedCard merge"))
L.append(cls("zero-turnaround", status="acquired", rng="below_1b", city="Boston", city_src="formd_address",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=W("ZeroTurnaround"), entry_date="2011",
    flags=["stage_disputes_band"],
    note="Java developer tools (Tartu, Estonia; US office Boston). 'Seed funding of $0.38M in 2008/9 from Webmedia, and a Series A round "
         "in 2011 followed by further investment of $2.7M in January 2014, both led by Bain Capital Ventures' (Wikipedia); the 2013 filing "
         "the band read is the follow-on. Rogue Wave acquired it in 2017."))
L.append(cls("1-800-dentist", status="unknown", rng="below_1b", country="US", country_src="model_knowledge", city="Los Angeles",
    focus="Healthcare & Bio", stage="undetermined", entry_date="2011",
    note="Dental referral service (Futuredontics, Los Angeles). The firm listed it in 2011-2013 (Paul Zurlo, Weston Gaddy); still "
         "operating in 2013 (new CEO). No source read gives the round, the stake or its later fate."))
L.append(cls("4moms", status="acquired", rng="below_1b", city="Pittsburgh", focus="Consumer & Marketplaces", stage="undetermined",
    entry_date="2012",
    note="Robotic baby gear (Thorley Industries, Pittsburgh). UPPAbaby acquired it in July 2024 ("
         + NEWS("4moms", "UPPAbaby Expands") + "). BCV's 2012 round is not named."))
L.append(cls("aboon", status="private", rng="below_1b", country="US", country_src="model_knowledge", flags=["city_unknown"],
    focus="Fintech & Payments", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("aboon", "secures $17.5M seed"), entry_date="2025-10", grad="censored",
    note="401(k) platform for financial advisors. 'Aboon secures $17.5M seed funding' (InvestmentNews, 2025-10-16), with the firm's post "
         "the same day; inside 24 months, so censored. No source read places the company."))

if __name__ == "__main__":
    jl.write("batch-005", L)
