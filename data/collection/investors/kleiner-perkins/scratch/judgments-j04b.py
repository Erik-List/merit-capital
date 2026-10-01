"""Judge j04, batch 8 (Kleiner Perkins PRO-99): classification of the listed members, one sale-consideration verdict."""
import judge_lib as jl
from judge_lib import cls, verdict, rnd, SITE, POST, W, FTS, FORMD_CITE

GP = "Graduation left for the graduation pass."
ASOF = "2026-09-30"
L = []

# ---- qumulo
w = W("Qumulo")
L.append(cls("qumulo", status="private", rng="1b_plus", usd=1200000000, val_src="web_verified", val_cite=w,
             asof="2020-07", stage="Growth", stage_src="web_verified", stage_cite=w, stage_conf="high",
             entry_date="2015-02", city="Seattle", focus="Data Infrastructure", flags=["stale"],
             extra={"valuation_range_source": "web_verified"},
             rounds=[rnd("2012-04", "Seed", 500000, "Valhalla Partners", False, w, "press"),
                     rnd("2012-11", "Series A", 24500000, "Highland Capital Partners", False, w, "press"),
                     rnd("2015-02", "Series B", 40000000, "Kleiner Perkins Caufield & Byers", True, w, "press"),
                     rnd("2016-06", "Series C", 32500000, None, True, w, "press"),
                     rnd("2020-07", "Series E", 125000000, None, None, w, "press")],
             note="Wikipedia (Seattle): KPCB led the $40M Series B of February 2015, the firm's entry (its since-year "
                  "2014 is the close year; the band's 2016 Form D is the Series C). The Series E of July 2020 ($125M) "
                  "valued it at over $1.2B, the last priced mark, now over 24 months old."))

# ---- rain
rp = "https://www.kleinerperkins.com/perspectives/rain/"
w = W("Rain (cryptocurrency exchange)")
L.append(cls("rain", status="private", rng="below_1b", stage="Growth", stage_src="first_party", stage_cite=rp,
             stage_conf="high", entry_date="2022-01", country="BH", country_src="web_verified", country_cite=w,
             city="Manama", focus="Crypto & Web3", flags=["model_disputes_source"],
             rounds=[rnd("2021", "Series A", 6000000, "Middle East Venture Partners", False, w, "press"),
                     rnd("2022-01", "Series B", 110000000, "Paradigm; Kleiner Perkins", True, rp, "firm")],
             note="Rain (rain.bh), the Bahrain-licensed crypto exchange (Rain Management W.L.L., Manama). The firm's "
                  "post of 2022-01-19 says it co-led the $110M Series B, after the $6M Series A of 2021 (Wikipedia). "
                  "The Wikidata US country is disputed. The Lightspeed and ICONIQ 'Rain' rows ($1.95B, 2026) are the "
                  "US stablecoin-card company rain.xyz, a different company. No priced round at $1B on record for "
                  "this Rain."))

# ---- rambus
L.append(cls("rambus", stage="undetermined", entry_date="1990", city="San Jose", focus="Industrial & Robotics",
             rounds=[],
             note="Rambus (memory interface IP, San Jose) was founded in 1990, the firm's since-year; Wikipedia names "
                  "KPCB among its early investors, but no record names the round."))

# ---- rapid-micro-biosystems
L.append(cls("rapid-micro-biosystems", city="Lowell",
             note="Rapid Micro Biosystems is headquartered in Lowell, Massachusetts (the firm's 2010 listing gave "
                  "Bedford, its earlier site)."))

# ---- rapt-therapeutics
rd = FTS("RAPT", "DRS")
L.append(cls("rapt-therapeutics", rng="below_1b", stage="Series A", stage_src="web_verified", stage_cite=rd,
             stage_conf="medium", entry_date="2015", city="South San Francisco", focus="Healthcare & Bio",
             rounds=[rnd("2015", "Series A", None, None, True, rd, "filing"),
                     rnd("2016-04", "Series B", 50000000, None, True, rd, "filing"),
                     rnd("2017-12", "Series C", 30000000, None, True, rd, "filing"),
                     rnd("2018-12", "Series C-2", None, None, True, rd, "filing")],
             note="RAPT (formerly FLX Bio, founded 2015, the firm's since-year). The 2019 draft S-1 shows KPCB Holdings "
                  "(for KPCB XV) holding 21,282,391 shares pre-IPO but buying only about 4.05M in the Series B, C and "
                  "C-2 of 2016-18, so the rest was bought in the 2015 Series A. The base also carries it as flx-bio. "
                  "Prefilled status acquired kept."))

# ---- razorgator-inc
w = W("RazorGator")
L.append(cls("razorgator-inc", status="acquired", rng="below_1b", stage="undetermined", country="US",
             city="Los Angeles", city_src="formd_address", focus="Consumer & Marketplaces", rounds=[],
             note="RazorGator (secondary tickets, 11150 Santa Monica Blvd, Los Angeles per its 2009 Form D; the firm's "
                  "2008 listing gave Beverly Hills) was acquired by TickPick on 2018-05-01 (Wikipedia). Russ Siegelman "
                  "is the partner; the round the firm entered is not on record, and the $188K 2009 Form D is not it."))

# ---- rebellion-defense
ng = "https://www.nextgov.com/artificial-intelligence/2021/09/defense-tech-startup-led-former-government-leaders-reaches-1-billion-valuation/185507/"
L.append(cls("rebellion-defense", status="private", rng="1b_plus", usd=1150000000, val_src="web_verified",
             val_cite=ng, asof="2021-09-15", stage="undetermined", entry_date="2019", country="US",
             city="Washington", focus="Security", flags=["stale"], extra={"valuation_range_source": "web_verified"},
             rounds=[rnd("2021-09", "Series B", 150000000, "Insight Partners", None, ng, "press")],
             note="Rebellion Defense (defence software, Washington DC). Nextgov: a Series B of more than $150M in "
                  "September 2021 at $1.15B, the last priced mark (over 24 months old), aligned with Insight. The "
                  "firm's since-year is 2019, the company's first year; its 2019 round is not named on record."))

# ---- redback-networks: sale consideration
L.append(verdict("redback-networks", "not_member",
                 "Sale consideration (Erik 2026-09-22; decisions.md R5): the firm's position in Redback came from "
                 "Redback's 1999-2000 stock acquisition of Siara Systems, the Vinod Khosla company Kleiner Perkins "
                 "backed from 1998 (the since-year). Khosla joined Redback's board in March 2000 when the deal closed "
                 "(2001 proxy); Redback's own seed came from Sequoia. Siara Systems is its own row.",
                 ec="fund_filing", conf="medium", cite=FTS("REDBACK", "DEF")))

# ---- redbrick-health
w = W("RedBrick Health")
L.append(cls("redbrick-health", status="acquired", rng="below_1b", stage="undetermined", city="Minneapolis",
             focus="Healthcare & Bio",
             rounds=[rnd("2009", "venture funding (total $45M)", 45000000, None, True, w, "press")],
             note="RedBrick Health (employee health engagement, Minneapolis) raised $45M from Highland, Versant, "
                  "Fidelity and KPCB (Wikipedia) and was acquired by Virgin Pulse in 2019. The firm's listing starts in "
                  "2009; the band's 2010 Form D ($152,800, Beth Seidenberg) is not an entry round, and the entry is not "
                  "named on record."))

# ---- relateiq
L.append(cls("relateiq", status="acquired", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2014", city="Palo Alto", focus="SaaS",
             rounds=[rnd("2013-06", "Series B", 20000000, None, None,
                         "https://www.finsmes.com/2013/06/relateiq-closes-20m-series-financingrelateiq-closes-20m-series-financing.html", "press"),
                     rnd("2014", "Series C", None, None, None, "https://www.redpoint.com/companies/relateiq/", "firm")],
             note="RelateIQ (Palo Alto) was bought by Salesforce in July 2014 for about $390M. The firm's since-year "
                  "is 2014, after the June 2013 Series B; the only 2014 round is the Series C (Redpoint's own card), "
                  "so Growth; KP's participation in it is inferred."))

# ---- relayr
L.append(cls("relayr", status="acquired", rng="below_1b", city="Berlin", focus="Industrial & Robotics",
             flags=["city_country_conflict"],
             note="relayr (industrial IoT) was founded and headquartered in Berlin; the prefilled US country is its "
                  "Boston subsidiary's Form D address (One Boston Place). Acquired by Munich Re's HSB in 2018, the "
                  "acquirer the firm's page names; its old domain now redirects elsewhere. Country correction to DE "
                  "left for review."))

# ---- remind  (status filled below after the news check)
REMIND = dict(status="acquired", note_status="Serent-backed ParentSquare acquired Remind (Business Wire and "
              "eSchool News, December 2023; Google News check 2026-09-30), the acquirer the firm's page names; this is "
              "fresher than the private status in the First Round and YC books.")

# ---- renmatix
L.append(cls("renmatix", status="private", rng="below_1b", city="King of Prussia", city_src="formd_address",
             focus="Climate & Energy",
             note="Renmatix (cellulosic sugars, 660 Allendale Road, King of Prussia per its 2015 Form D), still private "
                  "on record with a 2020 raise. The firm's Greentech listing starts in 2012 and the band reads a 2015 "
                  "Form D. The base also carries it as sriya-innovations-inc, its former name."))

# ---- rent-the-runway
L.append(cls("rent-the-runway", city="New York",
             note="Rent the Runway is headquartered in Brooklyn, New York, as Bain Capital Ventures and TCV carry it."))

# ---- reputation-com and reputationdefender (one company)
w = W("Reputation.com")
for s, extra_note in (("reputation-com", "The base also carries it as reputationdefender (renamed January 2011)."),
                      ("reputationdefender", "The same company as reputation-com (ReputationDefender renamed "
                                             "Reputation.com in January 2011); the two rows should merge.")):
    L.append(cls(s, status="private", rng="below_1b", stage="undetermined", entry_date="2010", city="San Ramon",
                 city_src="web_verified", focus="SaaS", rounds=[],
                 note="Reputation (founded 2006 as ReputationDefender, renamed Reputation.com in 2011) is an online "
                      "reputation software company headquartered in San Ramon, California (Wikipedia), still "
                      "private. Ted Schlein is the director on its 2010 and 2011 Form Ds; the 2010 round the firm "
                      "entered is not named on record. " + extra_note))

# ---- retym
rt = POST("retym-the-infrastructure")
L.append(cls("retym", status="private", rng="below_1b", stage="Seed", stage_src="first_party", stage_cite=rt,
             stage_conf="high", entry_date="2021", city="Cupertino", city_src="formd_address",
             focus="Industrial & Robotics", flags=["stage_disputes_band"],
             rounds=[rnd("2021", "Seed", None, "Kleiner Perkins", True, rt, "firm"),
                     rnd("2023-05-17", "unnamed (Form D)", 59999959, None, True, FORMD_CITE("retym"), "filing")],
             note="The firm's post (2025-03-31): 'Having led Retym's Seed round in 2021, we're excited to deepen our "
                  "investment', matching the 2021 since-year; the band's 2023 Form D ($60M) is a later round. "
                  "Semiconductors for AI data centres (20380 Town Center Lane, Cupertino per the Form D). " + GP))

# ---- ring
L.append(cls("ring", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2016",
             country="US", city="Santa Monica", focus="Consumer & Marketplaces",
             rounds=[rnd("2014-12", "Series A", None, "True Ventures", False, None, "press"),
                     rnd("2015-08", "unnamed", 28000000, None, False, None, "press")],
             note="Ring (Santa Monica) was acquired by Amazon in 2018. The firm's since-year is 2016, after the "
                  "December 2014 Series A and the $28M 2015 round (First Round's note), so a later round: Growth, as "
                  "the site also labels it; KP's own round is not cited."))

# ---- rippling
rw = POST("kleiner-perkins-welcomes-rippling")
L.append(cls("rippling", stage="Series A", stage_src="first_party", stage_cite=rw, stage_conf="high",
             entry_date="2019-04", city="San Francisco", focus="SaaS",
             rounds=[rnd("2019-04-03", "Series A", 45000000, "Kleiner Perkins", True, rw, "firm")],
             note="The firm's post of 2019-04-03: 'We couldn't be more excited to lead Rippling's Series A'; its 2024 "
                  "case study repeats that KP started at the Series A (Mamoon Hamid, Ilya Fushman)."))

# ---- robinhood
rh = "https://robinhood.com/us/en/newsroom/robinhood-raises-363-million-to-expand-product-lineup/"
L.append(cls("robinhood", status="public", rng="100b_plus", usd=101150000000, val_src="web_verified",
             val_cite="https://stockanalysis.com/stocks/hood/market-cap/", asof=ASOF, stage="Growth",
             stage_src="web_verified", stage_cite=rh, stage_conf="high", entry_date="2018-05-10",
             city="Menlo Park", focus="Fintech & Payments", extra={"valuation_range_source": "web_verified"},
             rounds=[rnd("2018-05-10", "Series D", 363000000, "DST Global", True, rh, "company")],
             note="Robinhood's release of 2018-05-10: the $363M Series D led by DST Global 'with participation from "
                  "new investors Iconiq, Capital G, Sequoia Capital, and Kleiner Perkins', the firm's 2018 entry. "
                  "Nasdaq HOOD, market cap $101.15B on 2026-09-30 (StockAnalysis)."))

# ---- rpx-corporation
w = W("RPX Corporation")
L.append(cls("rpx-corporation", rng="below_1b", stage="Series A", stage_src="model", stage_cite=w,
             stage_conf="medium", entry_date="2008", country="US", city="San Francisco", focus="SaaS",
             rounds=[rnd("2008", "initial financing", None, None, True, w, "press")],
             note="RPX (defensive patent aggregation, San Francisco) was founded in 2008 and 'initially financed by "
                  "Kleiner Perkins Caufield & Byers, Charles River Ventures, and Index Ventures' (Wikipedia), the "
                  "firm's 2008 since-year: the first institutional round, read as Series A. Taken private by HGGC in "
                  "2018."))

# ---- rudderstack
ru = POST("rudderstack_seriesa")
L.append(cls("rudderstack", status="private", rng="below_1b", stage="Series A", stage_src="first_party",
             stage_cite=ru, stage_conf="high", entry_date="2021-06", country="US", city="San Francisco",
             focus="Data Infrastructure",
             rounds=[rnd("2021-06-10", "Series A", 21000000, "Kleiner Perkins", True, ru, "firm"),
                     rnd("2022-02-02", "Series B", 56000000, "Insight Partners", None, None, "press")],
             note="The firm's post of 2021-06-10: 'we are leading RudderStack's Series A' (founded 2019, seed from "
                  "S28). Momentum check 2026-09-30 (Google News): the $21M Series A (June 2021) and $56M Series B "
                  "(February 2022) are the last reported rounds; no priced round at $1B."))

# ---- sagimet-biosciences
L.append(cls("sagimet-biosciences", stage="undetermined", entry_date="2007", city="San Mateo",
             focus="Healthcare & Bio", rounds=[],
             note="Sagimet (formerly 3-V Biosciences, San Mateo). The firm's since-year is 2007; its draft S-1 names "
                  "KPCB among the backers but covers only recent rounds, so the entry round is not named. The "
                  "duplicate 3-v-biosciences row is skipped in this run."))

# ---- secureframe
sf = POST("secureframe-series-a")
L.append(cls("secureframe", status="private", rng="below_1b", stage="Series A", stage_src="first_party",
             stage_cite=sf, stage_conf="medium", entry_date="2021-03", country="US", city="San Francisco",
             focus="Security",
             rounds=[rnd("2021-03-18", "Series A", None, None, True, sf, "firm")],
             note="The firm's post of 2021-03-18 (URL 'secureframe-series-a') announces its partnership at "
                  "Secureframe's Series A, matching the 2021 since-year. Compliance automation, San Francisco; no "
                  "priced round at $1B known."))

# ---- segment
L.append(cls("segment", status="acquired", rng="below_1b", stage="undetermined", entry_date="2013", country="US",
             city="San Francisco", focus="SaaS", rounds=[],
             note="Segment (customer data platform, San Francisco) was bought by Twilio in 2020 for $3.2B. The firm's "
                  "since-year is 2013, between the NEA/General Catalyst seed and Accel's 2014-15 round (Headline's "
                  "note); the 2013 round is not named on record."))

# ---- segway
w = W("Segway Inc.")
L.append(cls("segway", status="acquired", rng="below_1b", stage="undetermined", country="US", city="Bedford",
             focus="Consumer & Marketplaces", flags=["stage_disputes_band"], rounds=[],
             note="Segway (Bedford, New Hampshire) was founded in 1999; John Doerr invested in it (Wikipedia), long "
                  "before the band's $40,000 Form D of 2009, which cannot be the firm's entry. Sold to Summit in 2013 "
                  "and to Ninebot in 2015. The founding-era round is not named on record."))

# ---- servicemax
w = W("ServiceMax")
L.append(cls("servicemax", status="acquired", rng="below_1b", stage="Growth", stage_src="model",
             stage_conf="medium", entry_date="2014", city="Pleasanton", focus="SaaS", rounds=[],
             note="ServiceMax (field-service software, Pleasanton) was founded in 2007 and funded from 2008 "
                  "(Wikipedia); the firm entered in 2014 from the Green Growth Fund (archived page), a late round, so "
                  "Growth. GE bought it in 2016 and PTC in January 2023 (Wikipedia)."))

# ---- sessionm
L.append(cls("sessionm", status="acquired", rng="below_1b", stage="undetermined", entry_date="2011", country="US",
             city="Boston", focus="SaaS", rounds=[],
             note="SessionM (mobile engagement and loyalty, Boston) was acquired by Mastercard in 2019, the acquirer "
                  "the firm's page names. The firm entered in 2011 from the iFund (archived page, Matt Murphy); the "
                  "round is not named on record."))

# ---- shape-security
L.append(cls("shape-security", status="acquired", rng="below_1b", city="Mountain View", focus="Security",
             note="Shape Security was acquired by F5 in 2020 for about $1B, the acquirer the firm's page names; "
                  "Mountain View as in the GV book. " + GP))

# ---- shazam
w = W("Shazam (music app)")
L.append(cls("shazam", status="acquired", rng="below_1b", stage="Growth", stage_src="model", stage_cite=w,
             stage_conf="medium", entry_date="2009-10", city="London", focus="Media, Gaming & Advertising",
             rounds=[rnd("2009-10", "unnamed", None, "Kleiner Perkins Caufield & Byers", True, w, "press")],
             note="Wikipedia: Shazam's success 'led to a funding round from Kleiner Perkins Caufield & Byers in October "
                  "2009' (iFund), matching the firm's 2009 since-year; Shazam (founded 1999) had earlier venture "
                  "rounds, so Growth. The band's 2015 Form D is a later round. Apple bought Shazam in 2018."))

# ---- shopkick
w = W("Shopkick")
L.append(cls("shopkick", status="acquired", rng="below_1b", stage="Series A", stage_src="model", stage_conf="medium",
             entry_date="2009", city="Denver", city_src="web_verified", focus="Consumer & Marketplaces",
             rounds=[rnd("2009", "first round (Form D $5.02M)", 5020000, None, True, None, "filing"),
                     rnd("2010-06-30", "second round (Form D $19.4M)", 19449992, None, True, None, "filing")],
             note="Founded 2009 by Cyriac Roeding, a KP entrepreneur-in-residence; the firm's since-year 2009 is the "
                  "first ($5M, iFund) round, not the band's 2010 filing. Acquired by SK Planet in 2014 and by Trax in "
                  "2019; Wikipedia places it in Denver now (Greylock and Menlo carry Redwood City, its earlier base)."))

# ---- shyp
L.append(cls("shyp", rng="below_1b", city="San Francisco",
             note="Shyp (on-demand shipping, San Francisco) shut down in 2018."))

# ---- siluria-technologies
L.append(cls("siluria-technologies", status="acquired", rng="below_1b", city="San Francisco",
             focus="Climate & Energy",
             note="Siluria (natural gas to ethylene and fuels, San Francisco) was bought by McDermott in 2019 "
                  "(Wikipedia; Lux carries the same). " + GP))

# ---- silver-spring-networks
L.append(cls("silver-spring-networks", rng="below_1b", city="San Jose",
             note="Silver Spring Networks (smart-grid networking) was headquartered in San Jose when Itron bought it "
                  "in January 2018, as GV carries it."))

# ---- simple-healthkit
gn = "https://www.globenewswire.com/news-release/2023/02/06/2602229/0/en/Simple-HealthKit-Raises-8M-to-Transform-Health-Diagnostics-and-Follow-Up-Care-Expands-Portfolio-to-Include-Solutions-for-Sexual-Health-Tripledemic.html"
L.append(cls("simple-healthkit", status="private", rng="below_1b", stage="Seed", stage_src="web_verified",
             stage_cite=gn, stage_conf="high", entry_date="2019", grad="graduated", grad_src="web_verified",
             grad_cite=gn, grad_conf="high", country="US", city="Fremont", city_src="web_verified",
             focus="Healthcare & Bio",
             rounds=[rnd("2019", "Seed", 4000000, None, True, gn, "company"),
                     rnd("2023-02-06", "Series A", 8000000, "Initialized Capital", True, gn, "company")],
             note="The company's release (Fremont, 2023-02-06): an $8M Series A led by Initialized Capital with "
                  "participation from seed investors Kleiner Perkins, Kapor Capital and Quest, total funding $12M. "
                  "The firm entered at the seed (since-year 2019); the named Series A graduates it."))

# ---- simplivity
L.append(cls("simplivity", status="acquired", rng="below_1b", city="Westborough", focus="Data Infrastructure",
             note="SimpliVity (hyperconverged infrastructure, Westborough MA) was acquired by HPE in 2017 for $650M, "
                  "which retires its earlier $1B+ private mark."))

# ---- slack
sp = POST("slack-its-where")
L.append(cls("slack", rng="below_1b", stage="Growth", stage_src="first_party", stage_cite=sp, stage_conf="high",
             entry_date="2014-10", country="US", city="San Francisco", focus="SaaS",
             rounds=[rnd("2014-04", "round led by Social Capital", None, "Social Capital", False, sp, "firm"),
                     rnd("2014-10", "round led by Kleiner Perkins (John Doerr)", None, "Kleiner Perkins", True, sp, "firm"),
                     rnd("2015-04", "round led by Index Ventures", None, "Index Ventures", None, sp, "firm")],
             note="The firm's post: after Mamoon Hamid's April 2014 round at Social Capital, 'That October ... John "
                  "led the next round for Kleiner Perkins', the firm's entry; Tiny Speck had raised earlier venture "
                  "rounds, so Growth. Salesforce bought Slack in 2021."))

# ---- smiledirectclub
w = W("SmileDirectClub")
L.append(cls("smiledirectclub", rng="below_1b", stage="Growth", stage_src="web_verified",
             stage_cite=w, stage_conf="high", entry_date="2018-10", city="Nashville", focus="Healthcare & Bio",
             rounds=[rnd("2018-10", "unnamed", 380000000, "Clayton, Dubilier & Rice; Kleiner Perkins", True, w, "press")],
             note="Wikipedia: CD&R and Kleiner Perkins led the $380M round of October 2018 at $3.2B, the firm's entry "
                  "(a late round). Chapter 11 in September 2023, operations ceased in December 2023, and its assets and "
                  "technology were later bought by SmileSet, a Nashville successor (Wikipedia): the prefilled acquired "
                  "stands under the asset-sale rule, against Spark's defunct."))

# ---- snap
w = W("Snap Inc.")
L.append(cls("snap", rng="1b_plus", usd=9130000000, val_src="web_verified",
             val_cite="https://stockanalysis.com/stocks/snap/market-cap/", asof=ASOF, stage="Growth",
             stage_src="web_verified", stage_cite=w, stage_conf="medium", entry_date="2014", country="US",
             city="Santa Monica", focus="Consumer & Marketplaces", extra={"valuation_range_source": "web_verified"},
             rounds=[rnd("2014", "Series D", 100000000, "KPCB", True, w, "press")],
             note="Wikipedia: in 2014 Snapchat raised Series D funding led by KPCB, the firm's 2014 entry, after the "
                  "Lightspeed, IVP and Coatue rounds, so Growth. Market cap $9.13B on 2026-09-30 (StockAnalysis), so "
                  "the prefilled 10b_plus float ($11.6B, 2025) moves to 1b_plus, as every sibling book carries."))

# ---- solexel (status filled below after the news check)
SOLEXEL = dict(status="unknown", note_status="No shutdown or sale is cited on record, so the state is unknown.")

# ---- somatix
L.append(cls("somatix", status="acquired", rng="below_1b", stage="undetermined", entry_date="1991", country="US",
             city="Alameda", focus="Healthcare & Bio", rounds=[],
             note="Somatix Therapy (gene therapy, Alameda) merged into Cell Genesys in 1997, the acquirer the firm's "
                  "page names; the firm's since-year is 1991 and the round is not on record."))

# ---- spacex
L.append(cls("spacex", status="public", rng="100b_plus", usd=2050000000000, val_src="web_verified",
             val_cite="https://stockanalysis.com/stocks/spcx/market-cap/", asof=ASOF, stage="Growth",
             stage_src="model", stage_conf="medium", entry_date="2023", city="Starbase", focus="Industrial & Robotics",
             extra={"valuation_range_source": "web_verified"},
             rounds=[rnd("2023", "tender and late primary rounds (about $150-180B)", None, None, None, None, "press")],
             note="The firm's since-year is 2023, when SpaceX sold shares only in tenders and late rounds at about "
                  "$150-180B, so Growth; the exact round is not cited. Public since the June 2026 IPO (SPCX), market "
                  "cap $2.05T on 2026-09-30 (StockAnalysis). Headquartered at Starbase, Texas."))

# ---- spatial-photonics-inc (status filled below after the news check)
SPATIAL = dict(status="unknown", note_status="The firm's archived page reads Acquired (2012-14) without an acquirer "
               "and Khosla's row reads defunct; no sale is cited, so the state is unknown.")

# ---- spinal-modulation
L.append(cls("spinal-modulation", status="acquired", rng="below_1b", city="Menlo Park", focus="Healthcare & Bio",
             note="Spinal Modulation (dorsal root ganglion stimulation, Menlo Park) was acquired by St. Jude Medical in "
                  "2015. The firm's since-year (2005) predates the band's 2011 Form D, so the entry is likely earlier."))

# ---- spinlaunch
L.append(cls("spinlaunch", status="private", rng="below_1b", city="Long Beach", city_src="web_verified",
             focus="Industrial & Robotics",
             note="SpinLaunch (kinetic space launch) is headquartered in Long Beach (Wikipedia), still private after "
                  "its 2025 raise; about $150M raised by 2022, no priced round at $1B known."))


def finish(remind, solexel, spatial):
    w = W("Remind")
    L.append(cls("remind", status=remind["status"], rng="below_1b", stage="Growth", stage_src="model",
                 stage_cite=w, stage_conf="medium", entry_date="2013", country="US", city="San Francisco",
                 focus="SaaS",
                 rounds=[rnd("2013-09-18", "Series A", 3500000, "Social+Capital", False,
                             "https://techcrunch.com/2013/09/18/now-in-30k-schools-remind101-lands-3-5m-from-socialcapital-yuri-milner-more-to-bring-texting-to-teachers/", "press")],
                 note="Remind (Remind101, San Francisco). The Series A was Social+Capital's $3.5M of September 2013 "
                      "(First Round's note); Kleiner Perkins came in next, with John Doerr joining the board in 2014 "
                      "(Wikipedia), a later round, so Growth. " + remind["note_status"]))
    L.append(cls("solexel", status=solexel["status"], rng="below_1b", city="Milpitas", focus="Climate & Energy",
                 note="Solexel (thin crystalline silicon solar cells, Milpitas). " + solexel["note_status"]))
    L.append(cls("spatial-photonics-inc", status=spatial["status"], rng="below_1b", stage="undetermined",
                 city="Sunnyvale", focus="Industrial & Robotics", rounds=[],
                 note="Spatial Photonics (projection microdisplays, Sunnyvale) was backed while Vinod Khosla was at the "
                      "firm (to 2004), long before the band's 2009 Form D; the round is not on record. "
                      + spatial["note_status"]))


if __name__ == "__main__":
    finish(REMIND, SOLEXEL, SPATIAL)
    jl.write("j04b", L)
