"""PRO-82 grind, batch-010 (frontback .. lacoon). Same evidence and conventions as batch-001. funxional-therapeutics,
genebio, genmab, gensight, glycovaxyn and ingenium are life sciences desk rows (done). infection-control waits for the
pre-2008 archive pass. Label rows (stage left for the label pass): geckoboard, go-try-it-on, harmonic, innovative-silicon."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("gl", Path(__file__).with_name("gl.py"))
gl = importlib.util.module_from_spec(spec); spec.loader.exec_module(gl)
C, post, narch, sib, news, rnd, nqurl, verdict, arch = gl.C, gl.post, gl.narch, gl.sib, gl.news, gl.rnd, gl.nqurl, gl.verdict, gl.arch
L = []
WV = dict(stage_src="web_verified", stage_conf="high")
def sv(slug, inv):
    return dict(usd=int(float(sib(slug, inv, "usd"))), val_src="web_verified", val_cite=sib(slug, inv, "val_cite"), asof=sib(slug, inv, "asof"))

L.append(C("frontback", status="defunct", country="US", city="San Francisco", stage="Seed", stage_src="model", stage_conf="low", entry_date="2013", rng="below_1b",
    focus="Consumer & Marketplaces", flags=["stage_uncited"], note="Front-and-back camera photo app (founded in Brussels, moved to San Francisco); about $4M raised in 2013-2014 seed financing, Terrence Rohan the Index partner; shut down in 2015 (PetaPixel)",
    extra={"status_citation": news("Frontback", "Frontback Shutting Down")}))
L.append(C("futurelytics", status="unknown", country="CZ", city="Ostrava", stage="Seed", stage_src="model", stage_conf="low", entry_date="2014", rng="below_1b", focus="Data Infrastructure",
    flags=["stage_uncited"], note="Predictive customer analytics for online shops (Ostrava per the firm's 2014 page; a Seedcamp company); Index joined its 2014 seed, Jan Hammer the partner; no source read shows what became of it (aligned to Seedcamp's row)"))
u = post("garner-bringing")
L.append(C("garner-health", status="private", country="US", city="New York", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2026-05", rng="1b_plus",
    **sv("garner-health", "kleiner-perkins"), focus="Healthcare & Bio",
    note="Health benefit that steers employees to high-quality doctors (New York); 'We are thrilled to partner with Nick and the Garner team' (the firm's post, 2026-05-28), published with the $100M Series E at $2.74B (aligned to Kleiner Perkins' cited mark)",
    rounds=[rnd("2026-05-28", "Series E", 100000000, None, True, u, "firm")]))
L.append(C("geckoboard", status="private", country="GB", city="London", rng="below_1b", focus="SaaS",
    note="Business KPI dashboards (London); on the firm's 2012 list under its Seed stage filter, Robin Klein the partner"))
u = post("geophy-secures")
L.append(C("geophy", status="acquired", country="US", city="New York", stage="Growth", **WV, stage_cite=u, entry_date="2019-01", rng="below_1b", focus="AI & Applied AI",
    note="AI-driven commercial property valuation (founded in Delft, headquartered in New York); 'Index Ventures ... led the Series B round' ($33M; the firm's post, 2019-01-24), Jan Hammer on the board; acq. by Walker & Dunlop, 2022",
    rounds=[rnd("2019-01-24", "Series B", 33000000, "Index Ventures", True, u, "firm")]))
u = post("getharley-raises")
L.append(C("getharley", status="private", country="GB", city="London", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2023-06", rng="below_1b",
    focus="Healthcare & Bio", note="Online skincare consultations with clinicians and prescribed product plans (London); 'has raised $52 million in funding led by Index' (the firm's post, 2023-06-07), its Series B, with Headline and Visionaries Club",
    rounds=[rnd("2023-06-07", "Series B", 52000000, "Index Ventures", True, u, "firm")]))
u = narch("Glasses Direct Secures")
L.append(C("glasses-direct", status="acquired", country="GB", city="London", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2007", rng="below_1b",
    focus="Consumer & Marketplaces", note="Online prescription glasses retailer (MyOptique Group, London); 'its second round of funding ... from Acton and our existing investors Index and Highland' (the firm's own news item, 2009-04-22): the firm entered at the first round, the 2007 Series A; acq. by Essilor, 2016",
    rounds=[rnd("2009-04-22", "Series B", None, "Acton Capital", True, u, "firm")]))
u = nqurl('"Glow" endpoint security AI Index Ventures raises', "Glow emerges from stealth at $1.2B valuation")
L.append(C("glow", dispute=("country",), status="private", country="IL", city="Tel Aviv", stage="undetermined", rng="1b_plus", usd=1200000000, val_src="web_verified", val_cite=u, asof="2026-07-22",
    focus="Security", note="AI-native endpoint security (glow.io; an Israeli company per Calcalist); out of stealth on 2026-07-22 with $180M raised across its rounds at a $1.2B valuation (TechCrunch), Shardul Shah the Index partner; which of those rounds the firm entered is not on any surface read; not the Glow rows of a16z, Redpoint or Sequoia unless a cross-ruling says so; the pre-filled CH is a one-word name join",
    rounds=[]))
L.append(C("gluster", dispute=("country",), country="US", city="Sunnyvale", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2010", rng="below_1b", focus="Data Infrastructure",
    note="Open-source scale-out file storage (Sunnyvale; engineering in Bangalore); Index led the $8.5M Series B of 2010 after Nexus had funded the first round, Bernard Dalle on the board; acq. by Red Hat, 2011 ($136M; the firm's own news item); the pre-filled IN is the engineering base",
    extra={"status_citation": narch("Red Hat To Acquire Gluster")}))
L.append(C("go-try-it-on", status="acquired", country="US", city="New York", rng="below_1b", focus="Consumer & Marketplaces",
    note="Outfit-feedback social app (New York); on the firm's 2012 list under both its Seed and Early stage filters; acq. by Rent the Runway, 2013"))
u = post("granola-investing")
L.append(C("granola", country="GB", city="London", stage="Growth", **WV, stage_cite=u, entry_date="2026-03", focus="AI & Applied AI",
    note="AI notepad for meetings (London); 'We couldn't be more thrilled to lead their $125m Series C' (the firm's post, 2026-03-25), at $1.5B",
    rounds=[rnd("2026-03-25", "Series C", 125000000, "Index Ventures", True, u, "firm")]))
L.append(verdict("greenfield-online", "not_member", "sale consideration (decisions.md D6; Erik's ruling of 2026-09-22): the firm's position was Ciao (its own row), which Greenfield Online bought in April 2005 for cash and stock (Greenfield's 8-K of 2005-04-07 names the Index funds as sellers); the 2008-2013 lists carry the acquirer under its ticker NASDAQ:SRVY",
                 ec="site_listing", conf="medium", cite=arch("greenfield-online", "list_tag")))
L.append(C("grey-area", dispute=("country",), status="defunct", country="FI", city="Helsinki", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2011", rng="below_1b",
    focus="Media, Gaming & Advertising", note="Location-based mobile games, maker of Shadow Cities (Helsinki per the firm's page); Index led the $2.5M Series A of 2011 with London Venture Partners, Ben Holmes the partner; the game closed in 2013 and the studio wound down; the pre-filled FR is a name join"))
L.append(C("groupalia", dispute=("country",), status="unknown", country="ES", city="Barcelona", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2011", rng="below_1b",
    focus="Consumer & Marketplaces", note="Daily-deals site for Spain, Italy and Latin America (Barcelona); Index joined the large 2011 round with Insight and General Atlantic; on the firm's 2012-2013 lists; later history not established (aligned to Insight's row); the pre-filled IT is one of its markets"))
u = narch("GroupSpaces Raises Investment")
L.append(C("groupspaces", status="unknown", country="GB", city="London", stage="Seed", **WV, stage_cite=u, entry_date="2010-07", rng="below_1b", focus="SaaS",
    note="Membership management for clubs and societies (London; Oxford founders); 'Raises Investment From New Index Seed Fund' ($1.3M with angels; the firm's own news item, 2010-07-01); no later round and no outcome on any surface read",
    rounds=[rnd("2010-07-01", "Seed", 1300000, "Index Ventures", True, u, "firm")]))
L.append(C("grupo-xango", status="unknown", country="BR", stage="undetermined", rng="below_1b", focus="Consumer & Marketplaces", flags=["city_unknown", "country_prior"],
    note="On the firm's 2013 list only, under its Early stage filter; a Brazilian e-commerce group by its name; no round, city or outcome is on any surface read", rounds=[]))
L.append(C("gruppo-mutuionline", status="public", country="IT", city="Milan", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2000", rng="below_1b", focus="Fintech & Payments",
    flags=["needs_web_value"], note="Online mortgage and insurance broker and outsourcing group (Milan; now Moltiply Group, Euronext Milan: MOL, IPO June 2007); Index backed it at its founding round in 2000, Giuseppe Zocco the partner; the market cap is read in the A/B pass"))
L.append(C("happylatte", status="unknown", country="CN", city="Beijing", stage="Series A", stage_src="model", stage_conf="low", entry_date="2011", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Mobile games studio, maker of High Noon (Beijing); Index funded its 2011 round, Ben Holmes the partner; on the firm's 2014-2016 pages; no outcome on any surface read"))
u = post("solving-the-ai-reasoning-gap")
L.append(C("harmonic", dispute=("status", "rng", "usd"), status="private", country="US", city="Palo Alto", rng="1b_plus", **sv("harmonic", "kleiner-perkins"), focus="AI & Applied AI",
    note="AI for verified mathematical reasoning, co-founded by Vlad Tenev (Palo Alto); 'The company has raised $75 million from investors including Index Ventures' (the firm's post, 2024-09-23, the Series A led by Sequoia); marked 'backed at Seed' on the firm's list; $1.45B at the November 2025 round (aligned to Kleiner Perkins' cited mark); the pre-filled 'public' and $0.65B are Harmonic Inc. (NASDAQ: HLIT), another company"))
u = news("Hoop", "Hoop Announces $5M in Seed Funding Led by Index Ventures")
L.append(C("hoop", status="private", country="US", stage="Seed", **WV, stage_cite=u, entry_date="2024-06", rng="below_1b", focus="AI & Applied AI", flags=["city_unknown", "country_prior"],
    note="AI to-do list that fills itself from meetings and messages (hoop.app; founded by former Trello staff, a remote US team); 'Hoop Announces $5M in Seed Funding Led by Index Ventures' (Business Wire, 2024-06-05), Neil Rimer the partner",
    rounds=[rnd("2024-06-05", "Seed", 5000000, "Index Ventures", True, u, "press")]))
u = narch("Housetrip.com Announces")
L.append(C("housetrip", status="acquired", country="GB", city="London", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2011", rng="below_1b", focus="Consumer & Marketplaces",
    note="Holiday rental marketplace (London; founded in Lausanne); Index led the first venture round in 2011, then 'existing investors Balderton Capital and Index Ventures also participating' in the $40M Series C led by Accel (the firm's own news item, 2012-10-09); acq. by TripAdvisor, 2016 (PhocusWire)",
    extra={"status_citation": news("HouseTrip", "TripAdvisor buys vacation rental platform HouseTrip")}))
u = post("hyperline-makes-pricing")
L.append(C("hyperline", status="private", country="FR", city="Paris", stage="Seed", **WV, stage_cite=u, entry_date="2023-06", rng="below_1b", focus="Fintech & Payments",
    note="Usage-based pricing and billing software (Paris); 'Hyperline made its debut with EUR 4 million in seed funding' (the firm's post, 2023-06-20), then 'leading an additional $10m of seed funding' (2025-01-16); no Series A on any surface read yet",
    rounds=[rnd("2023-06-20", "Seed", None, "Index Ventures", True, u, "firm"), rnd("2025-01-16", "Seed", 10000000, "Index Ventures", True, post("hyperline-raises-an-additional"), "firm")]))
L.append(C("ideogram-ai", status="private", country="CA", city="Toronto", stage="Seed", stage_src="model", stage_conf="medium", entry_date="2023-08", rng="below_1b", focus="AI & Applied AI",
    note="Text-to-image generation with reliable typography (Toronto; ex-Google Brain founders); launched in August 2023 on $16.5M of seed financing led by a16z and Index (BetaKit), Mike Volpi the partner; $80M Series A led by a16z in February 2024"))
L.append(C("imbera-electronics", status="acquired", country="FI", city="Espoo", stage="undetermined", rng="below_1b", focus="Industrial & Robotics",
    note="Embedded-component packaging for electronics (Espoo); on the firm's 2009-2013 lists under its Early stage filter; folded into GE's embedded electronics business; the round is not on record", rounds=[]))
u = post("the-superlearner"); v = nqurl('"Ineffable Intelligence" seed Index Ventures', "Ineffable Intelligence lands historic $1.1 billion Seed round at $5.1 billion valuation")
L.append(C("ineffable", status="private", country="GB", city="London", stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=v, entry_date="2026-04", grad="censored",
    rng="1b_plus", usd=5100000000, val_src="web_verified", val_cite=v, asof="2026-04-27", focus="AI & Applied AI",
    note="Reinforcement-learning 'superlearner' lab founded by David Silver (Ineffable Intelligence, London); 'The Superlearner: Investing in David Silver and Ineffable Intelligence' (the firm's post, 2026-04-27), published with the $1.1B seed at $5.1B (EU-Startups); inside the 24-month window",
    rounds=[rnd("2026-04-27", "Seed", 1100000000, None, True, u, "firm")]))
u = post("inherent-designing")
L.append(C("inherent", status="private", country="GB", city="London", stage="Seed", **WV, stage_cite=u, entry_date="2026-05", grad="censored", rng="below_1b", focus="AI & Applied AI",
    flags=["country_prior"], note="AI agents for scientific discovery (Inherent Laboratories); 'We're proud to stand with them to lead their $50m seed round, alongside Radical Ventures' (the firm's post, 2026-05-31); inside the 24-month window; London is inferred from the firm's Europe tag and its London partners",
    rounds=[rnd("2026-05-31", "Seed", 50000000, "Index Ventures", True, u, "firm")]))
L.append(C("innovative-silicon", status="acquired", country="US", city="Santa Clara", rng="below_1b", focus="Industrial & Robotics",
    note="Zero-capacitor floating-body memory (Z-RAM) licensing (founded in Lausanne, later Santa Clara); on the firm's lists under both its Seed and Early stage filters, Neil Rimer the partner; its patents and team went to Micron in 2010-2011"))
u = post("proving-ai-in-the-real-world")
L.append(C("intelligence", status="private", country="US", city="San Francisco", stage="Seed", **WV, stage_cite=u, entry_date="2026-08", grad="censored", rng="below_1b", focus="AI & Applied AI",
    flags=["country_prior"], note="Design Arena, a human-preference benchmark for AI-generated design (intelligence.ai); 'welcome Grace, Kamryn, and the Intelligence team into the Index family as part of their $7.9M seed round' (the firm's post, 2026-08-03); inside the 24-month window; the city is inferred from the San Francisco partners",
    rounds=[rnd("2026-08-03", "Seed", 7900000, None, True, u, "firm")]))
L.append(C("interana", status="unknown", country="US", city="Redwood City", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2015-01", rng="below_1b", focus="Data Infrastructure",
    note="Behavioural analytics on event data (Redwood City; renamed Scuba Analytics in 2020); Index led the $20M Series B of January 2015, Mike Volpi on the board ('Gaining Insights: Interana ushers the era of data democratization', the firm's own item of 2015-01-21); status aligned to a16z's row"))
u = post("congratulations-to-izettle")
L.append(C("izettle", status="acquired", country="SE", city="Stockholm", stage="Series A", **WV, stage_cite=u, entry_date="2011", rng="below_1b", focus="Fintech & Payments",
    note="Card readers and payments for small merchants (Stockholm); 'Index Ventures led the Series A investment in iZettle in Summer 2011 and participated in many of the subsequent financings' (the firm's post, 2018-05-17); acq. by PayPal, 2018 ($2.2B)",
    rounds=[rnd("2011-10-19", "Series A", None, "Index Ventures", True, narch("iZettle Rings Up"), "firm")], extra={"status_citation": u}))
u = narch("Joost Closes $45 Million")
L.append(C("joost", status="defunct", country="NL", city="Amsterdam", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2007-05", rng="below_1b",
    focus="Media, Gaming & Advertising", note="Peer-to-peer internet TV from the Skype founders (Leiden and Amsterdam); 'Joost Closes $45 Million in Financing' (the firm's own news item, 2007-05-09), its one venture round, with Sequoia, CBS and Viacom, Danny Rimer the partner; assets sold to Adconion in 2009 and the service closed (aligned to Sequoia's row)",
    rounds=[rnd("2007-05-09", "Series A", 45000000, None, True, u, "firm")]))
L.append(C("jumbo", dispute=("country",), country="US", city="New York", stage="undetermined", rng="below_1b", focus="Security",
    note="Consumer privacy assistant app (Jumbo Privacy, New York); Shardul Shah the Index partner; which round the firm joined is not on any surface read; acq. by Coalition, 2023 (The Insurer); the pre-filled AR is a one-word name join",
    rounds=[], extra={"status_citation": nqurl('"Jumbo" privacy Coalition acquires', "Coalition acquires web privacy specialist Jumbo")}))
u = narch("Just-Eat Completes")
L.append(C("just-eat", status="acquired", country="GB", city="London", stage="Series A", **WV, stage_cite=u, entry_date="2009-07", rng="below_1b", focus="Consumer & Marketplaces",
    note="Online takeaway ordering (London; founded in Denmark); 'Just-Eat Completes GBP 10.5 Million Series A Funding ... its first institutional financing' (the firm's own news item, 2009-07-14), led by Index; LSE IPO April 2014; merged into Just Eat Takeaway.com in 2020 (aligned to Redpoint's row)",
    rounds=[rnd("2009-07-14", "Series A", None, "Index Ventures", True, u, "firm")]))
L.append(C("keynoir", status="acquired", country="GB", city="London", stage="undetermined", rng="below_1b", focus="Consumer & Marketplaces",
    note="Premium daily-deals site (London; launched 2010); on the firm's 2010-2013 lists, marked exited; acq. by Time Out, 2011; the round is not on record", rounds=[]))
u = post("our-investment-in-kindred")
L.append(C("kindred", status="private", country="US", city="San Francisco", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2026-02", rng="below_1b",
    focus="Consumer & Marketplaces", note="Members-only home-swapping network (San Francisco); 'A New Way to See the World: Our Investment in Kindred' (the firm's post, 2026-02-03), published with the $125M round (PhocusWire), three years after its $15M Series A; the same company as a16z's row, not the Kindred rows of First Round and GV",
    rounds=[rnd("2026-02-03", "Growth round", 125000000, None, True, u, "firm")]))
u = post("the-king-of-candy")
L.append(C("king", dispute=("country",), country="GB", city="London", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2005-09", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Casual and mobile games, maker of Candy Crush (King Digital Entertainment, London); Index and Apax bought in together in September 2005 (EUR 34M), the company's only venture round; NYSE IPO March 2014; 'King was acquired by Activision Blizzard in 2016 for $5.9 billion' (the firm's post, 2024-11-19)",
    extra={"status_citation": u}))
L.append(C("kvs", dispute=("status",), status="acquired", country="GB", city="Reading", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2000", rng="below_1b", focus="SaaS",
    note="Email archiving software, Enterprise Vault (KVault Software, Reading); spun out of Compaq in 2000 with venture funding that included Index; acq. by Veritas, 2004 ($225M), now Symantec per the firm's own tag; the pre-filled 'defunct' is a dissolved-entity record after that sale"))
L.append(C("lacoon", status="acquired", country="IL", city="Tel Aviv", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2013-10", rng="below_1b", focus="Security",
    note="Mobile threat defence for enterprises (Lacoon Mobile Security; Tel Aviv per the firm's page); Index led the $8M Series A of October 2013 (the firm's own item of 2013-10-24), Shardul Shah on the board; acq. by Check Point, 2015"))
gl.write("batch-010", L)
