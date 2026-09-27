"""Batch 5 (pass 1), plus the two hidden CMS rows held back from batch 2 (Flutterwave,
Friendsurance). Hidden CMS docs are judged on corroboration, never on the doc alone
(config site_api _note); the seed step had counted them as site listings.

Form D name-match rows are judged cluster-first (COLLECTION.md s3): Matthew / Matt
Brown (at Headline from ~2022, before that The Chernin Group, Wag and Stripes Group,
per his CMS bio), Michael / Mike Kent (Azimo's founder, London, from ~2022), Jonathan
Becker (Berlin, from 2011), Jonathan Turner (e.ventures Growth 2015-2021, Mohr
Davidow before, Accel after), and the distinctive founders Schilling and Gieselmann.
Rows that are a known company's legal entity are merged in identity-merges.json and
carry no line (the one rebuild absorbs them): brainfights-inc, codefied-inc,
hound-technology-inc, blossom-bh-opco-inc, ixtens-inc, superintelligence."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, verdict, write, rnd, post_url  # noqa: E402

TAJ = "https://headline.com/founders/taj-kamranpour/"
CAMEO = "https://globalventuring.com/blog/2021/03/31/cameo-closes-100m/"
CLYDE = "https://www.pymnts.com/news/investment-tracker/2021/product-protection-startup-clyde-raises-41m-led-by-headline/"
CLYDE_ACQ = "https://www.globenewswire.com/news-release/2023/03/15/2627874/0/en/Cover-Genius-Acquires-Clyde-Deepening-Footprint-in-121B-Global-Warranty-Industry.html"
FAN_ACQ = "https://www.businesswire.com/news/home/20141103005311/en/Rovi-Acquires-Content-Discovery-and-Navigation-Innovator-Fanhattan"
FAN_BV = "https://variety.com/2014/digital/news/rovi-buys-fanhattan-to-pitch-startups-fan-tv-box-to-cable-operators-1201345937/"
THRIVE = "https://globalventuring.com/blog/2015/07/31/thrive-market-prospers-with-30m-series-a/"
FLW = "https://flutterwave.com/us/blog/flutterwave-closes-35m-series-b-co-led-by-greycroft-and-eventures"
FRIEND = "https://www.startbase.com/organization/friendsurance/"
TRELLIS = "https://headline.com/founders/nicole-clark-and-alon-shwartz/"
TRAWA = post_url("trawa", "trawa")
STOT2 = post_url("stotles", "Double Down")
MAT_BIO = "https://headline.com/team/matt-brown/"
BROWN = ("Matthew / Matt Brown cluster: Headline's Matt Brown joined from The Chernin Group (earlier Wag and Stripes Group, "
         "his CMS bio); the name is common, the firm lists none of these companies, and no Headline round was found.")
L = [
    # ---- site rows
    cls("stotles", status="private", country="GB", city="London", rng="below_1b", stage="Seed", stage_src="web_verified",
        stage_conf="high", stage_cite=TAJ, entry_date="2022-06",
        grad="graduated", grad_src="first_party", grad_cite=STOT2,
        note="The firm's founder story (2022-06-22): 'Stotles, whose Seed round we share today'; its 2025-05-29 post: 'We invested in Stotles' Seed round in 2022 ... co-leading their $13M Series A alongside Acton Capital'.",
        rounds=[rnd("2022-06-22", "Seed", None, None, True, TAJ, "firm"),
                rnd("2025-05-29", "Series A", 13000000, "Headline; Acton Capital", True, STOT2, "firm")]),
    cls("swile", status="private", country="FR", city="Montpellier", stage="Growth", stage_src="model", stage_conf="medium",
        note="Headline's growth fund entered in 2021 (the CMS: 'Growth 2021'), the year of Swile's $200M Series D led by SoftBank: a late entry, Growth by taxonomy."),
    cls("tabnine", status="private", country="IL", city="Tel Aviv", rng="below_1b",
        note="Tabnine (formerly Codota), Tel Aviv; the CMS location 'Middletown, DE' is a Delaware registered-agent address."),
    cls("tandem", status="unknown", country="DE", country_src="model_knowledge", rng="undetermined",
        stage="undetermined", grad="undetermined", flags=["identity_unresolved", "country_prior"],
        note="'Tandem' is a title-only CMS doc on Andreas Haug's team page, with no location, website or date. Tandem the Berlin language app lists no e.ventures money (Series A 2020 led by Brighteye; earlier Rubylight, Faber), and Tandem Bank and Tandem Diabetes do not fit; the company cannot be named. Country is the Berlin desk's, inferred."),
    cls("taxwire", status="private", country="US", city="New York", rng="below_1b", stage="Seed", stage_src="first_party",
        stage_conf="medium", stage_cite="https://iznipsfw.apicdn.sanity.io/v2021-10-21/data/query/production?query=%2A%5B_type%3D%3D%22company%22%20%26%26%20slug.current%3D%3D%22taxwire%22%5D",
        entry_date="2026", grad="censored",
        note="The firm's own CMS entry reads 'Seed 2026'; its post 'Our Investment in Taxwire' (2026-06-30) names no round."),
    cls("thread", status="private", country="US", city="New York", rng="below_1b",
        note="The firm's post 'Why We Invested in Thread' (2025-08-12) names no round; the entry round goes to the stage pass."),
    cls("trawa", status="private", country="DE", city="Berlin", rng="below_1b", stage="Series A", stage_src="web_verified",
        stage_conf="high", stage_cite=TRAWA, entry_date="2025-05",
        note="The firm's own post (2025-05-22): 'We're proud to lead trawa's €24M Series A, alongside existing investors Balderton, Speedinvest, AENU, and Magnetic' - Headline new in the round. EUR 24.0M @ ECB 2025-05-22 (EUR/USD 1.1309) = $27.1M.",
        rounds=[rnd("2025-05-22", "Series A", 27141600, "Headline", True, TRAWA, "firm")]),
    cls("trellis", status="private", country="US", city="Santa Monica", rng="below_1b", stage="Series A",
        stage_src="web_verified", stage_conf="high", stage_cite=TRELLIS, entry_date="2021-10",
        note="The firm's founder story: 'Headline led Trellis' Series A, announced October 2021.'",
        rounds=[rnd("2021-10", "Series A", None, "Headline", True, TRELLIS, "firm")]),
    cls("upheal", status="private", country="CZ", city="Prague", rng="below_1b"),
    cls("verse-medical", status="private", country="US", city="New York", rng="below_1b"),
    cls("viabill", status="private", country="DK", city="Copenhagen", rng="below_1b"),
    cls("vicampo", status="acquired", country="DE", city="Mainz", rng="below_1b",
        note="acq. by VIVA Wine Group, 2021 (the firm's CMS)."),
    cls("vizzia", status="private", country="FR", city="Paris", rng="below_1b"),
    cls("voicea", status="acquired", country="US", city="San Jose", rng="below_1b",
        note="acq. by Cisco, 2019. Legal name Rizio, Inc. (Form Ds 2016-2018 in Menlo Park, Schilling director; merged). e.ventures led Voicea's $14.5M Series A; the CMS dates the firm's entry 'Early 2016', before it: the entry round goes to the stage pass."),
    cls("vox-ai", status="private", country="NL", city="Amsterdam", rng="below_1b"),
    cls("vuze", status="unknown", country="US", city="Palo Alto", rng="below_1b",
        note="Vuze, Inc. (formerly Azureus, the BitTorrent client); Wikipedia: a later round 'led by NEA, with existing investors Redpoint Ventures, Greycroft Partners, BV Capital'; BV Capital's entry round and the company's later state are not established."),
    verdict("wawa", "not_member",
            "A hidden CMS doc titled only 'Wawa' (created 2026-08-18, referenced to the EU fund page) with no location, website or date. Hidden docs are judged on corroboration, never on the doc alone (config site_api note); several unrelated companies share the name (WaWa, Wawa Fertility, Wawa Technology) and none shows a Headline round; the Wikidata join to Wawa Inc., the Pennsylvania store chain, is wrong. Re-judge when a round is announced.",
            ec="site_listing", conf="medium"),
    cls("weavr", status="private", country="GB", city="London", rng="below_1b"),
    cls("yeahka", status="public", country="CN", city="Shenzhen", stage="Growth", stage_src="model", stage_conf="medium",
        note="HKEX 9923 since 2020. The CMS lists 'Early 2011' (the Asia desk, Infinity Ventures: decisions.md D2) and 'Growth 2014'; the home entry is the growth fund's 2014 check, a later round, Growth by taxonomy. Market cap goes to the valuation pass."),
    cls("zippia", status="private", country="US", rng="below_1b",
        note="Zippia, the careers site; a title-only CMS doc on Thomas Gieselmann's team page; city to the city pass."),
    cls("zive", status="acquired", country="DE", city="Hamburg", rng="below_1b",
        note="acq. by Docebo, 2026 (the firm's CMS)."),
    # ---- hidden CMS rows, corroborated
    verdict("thrive-market", "member",
            "Hidden CMS doc referenced to the Global Growth fund page, corroborated: e.ventures co-led Thrive Market's $30M Series A with Greycroft in July 2015 (Global Venturing 2015-07-31).",
            ec="web", conf="high", cite=THRIVE),
    cls("thrive-market", status="private", country="US", city="Los Angeles", rng="below_1b", stage="Series A",
        stage_src="web_verified", stage_conf="high", stage_cite=THRIVE, entry_date="2015-07",
        note="e.ventures co-led the $30M Series A with Greycroft (July 2015), with Powerplant Ventures, CAVU and Scripps Networks.",
        rounds=[rnd("2015-07", "Series A", 30000000, "Greycroft; e.ventures", True, THRIVE, "press")]),
    verdict("flutterwave", "member",
            "Hidden CMS doc referenced to the Global Growth fund page, corroborated: Flutterwave's own blog, 'Flutterwave Closes $35M Series B Co-Led By Greycroft and eVentures' (January 2020).",
            ec="web", conf="high", cite=FLW),
    cls("flutterwave", status="private", country="US", city="San Francisco", stage="Growth", stage_src="web_verified",
        stage_conf="high", stage_cite=FLW, entry_date="2020-01",
        note="Series B $35M co-led by Greycroft and e.ventures (2020-01-21), from the growth fund. Dual HQ San Francisco and Lagos (Wikipedia). Mark goes to the valuation pass.",
        rounds=[rnd("2020-01-21", "Series B", 35000000, "Greycroft; e.ventures", True, FLW, "company")]),
    verdict("friendsurance", "member",
            "Hidden CMS doc (no fund reference), corroborated: the company's own funder statement names e.ventures among the institutional investors that financed Friendsurance (Alecto GmbH, Berlin); medium because the statement is transcribed by a directory, not read on the company's page.",
            ec="web", conf="medium", cite=FRIEND),
    cls("friendsurance", status="private", country="DE", city="Berlin", rng="below_1b",
        note="Friendsurance (Alecto GmbH), Berlin insurtech; e.ventures among its early institutional investors; Horizons Ventures led the 2014 and 2016 rounds; Round2 Capital invested in July 2025. e.ventures' entry round goes to the stage pass."),
    # ---- Housecall Pro: city correction with the merge of its legal entity
    cls("housecall-pro", city="Denver",
        note="Codefied Inc. does business as Housecall Pro (Form Ds 2013-2022, Gieselmann director; merged). HQ Denver (the firm's CMS and the 2022 Form D, 4180 Wynkoop Street); founded in San Diego."),
    # ---- Form D name matches
    verdict("attlee-inc", "not_member",
            "Jonathan Turner as director of record on a 2009 Form D filed care of Mohr Davidow Ventures, 3000 Sand Hill Road: a seat at his prior firm, six years before his e.ventures tenure (seat dated at filing time, COLLECTION.md s1).",
            ec="formd_adjudicated", conf="high",
            cite="https://www.sec.gov/Archives/edgar/data/1456034/000145603409000002/0001456034-09-000002-index.htm"),
    verdict("baron-app-inc", "member",
            "Baron App, Inc. is Cameo. e.ventures led Cameo's $100M Series C in March 2021 and Jonathan Turner joined the board (Global Venturing 2021-03-31); his seat on the 2021-2024 Form Ds is the fund's. decisions.md D4 (the reverse): Accel's run reads this e.ventures-era seat the same way.",
            ec="web", conf="high", cite=CAMEO),
    cls("baron-app-inc", status="private", city="Chicago", rng="below_1b", stage="Growth", stage_src="web_verified",
        stage_conf="high", stage_cite=CAMEO, entry_date="2021-03",
        note="Cameo. e.ventures led the $100M Series C at just over $1B (March 2021). The 2021 mark collapsed (2023 down round reported near $100M; the Spark and Lightspeed rows carry it): below_1b.",
        rounds=[rnd("2021-03-31", "Series C", 100000000, "e.ventures", True, CAMEO, "press")]),
    verdict("capital-integration-systems-llc", "not_member", f"{BROWN} Here an executive officer of a New York financial LLC (2010-2022): an operator role, not a firm seat.",
            ec="formd_adjudicated", conf="high", cite=MAT_BIO),
    verdict("central-iowa-lithotripsy-inc", "not_member",
            "Michael Kent homonym: a West Des Moines lithotripsy practice (2011); Headline's Michael Kent is Azimo's London founder, at the firm from about 2022.",
            ec="formd_adjudicated", conf="high"),
    verdict("chimney-trail-co", "not_member", f"{BROWN} Here an executive officer of a Windsor, Colorado issuer (2022-2023).",
            ec="formd_adjudicated", conf="high", cite=MAT_BIO),
    verdict("clyde-technologies-inc", "member",
            "Clyde Technologies (Clyde, New York product protection): Headline led the $25M Series B in October 2021 (PYMNTS 'Product Protection Startup Clyde Raises $41M Led by Headline'); Schilling director on the 2021 Form D.",
            ec="web", conf="high", cite=CLYDE),
    cls("clyde-technologies-inc", status="acquired", city="New York", rng="below_1b", stage="Growth", stage_src="web_verified",
        stage_conf="high", stage_cite=CLYDE, entry_date="2021-10",
        note="Headline led the $25M Series B (plus $16M working capital), October 2021, with Vulcan, Spark Capital and Crosslink. acq. by Cover Genius (assets), March 2023 (GlobeNewswire 2023-03-15). The Spark book reads Spark as lead and the sale as 2024: cross-investor alignment item.",
        rounds=[rnd("2021-10-19", "Series B", 25000000, "Headline", True, CLYDE, "press")]),
    verdict("daily-secret-inc", "member",
            "Director of record (COLLECTION.md s1): Mathias Schilling, a founding partner with an exact distinctive name, is director on Daily Secret Inc.'s three Form Ds 2012-2014, in tenure, and the issuer resolves to Daily Secret, the New York city-guide newsletter. No announcement was found; medium, flagged for the A/B pass.",
            ec="formd_adjudicated", conf="medium",
            cite="https://www.sec.gov/Archives/edgar/data/1543994/000154399412000001/0001543994-12-000001-index.htm"),
    cls("daily-secret-inc", status="unknown", city="New York", rng="below_1b", flags=["formd_adjudicated", "unannounced_deal"],
        note="Daily Secret, a New York daily email of city secrets (dailysecret.com), 25 Broadway; Form Ds 2012 $1.85M, 2013 $2.27M, 2015 $2.75M; no trace of later activity found."),
    verdict("eaw-llc", "not_member", "Mike Kent homonym: director of a Cincinnati LLC (2024); Headline's Michael Kent is London-based.",
            ec="formd_adjudicated", conf="high"),
    verdict("emergent-properties-inc", "not_member", f"{BROWN} Here a 2013 New York director seat, a decade before his Headline tenure.",
            ec="formd_adjudicated", conf="high", cite=MAT_BIO),
    verdict("endur-apparel-ltd", "not_member",
            "Jonathan Becker homonym: director of an apparel company in Victoria, British Columbia (2021); Headline's Jonathan Becker is its Berlin partner.",
            ec="formd_adjudicated", conf="high"),
    verdict("etf-issuer-solutions-inc", "not_member", f"{BROWN} Here an executive officer (2013).",
            ec="formd_adjudicated", conf="high", cite=MAT_BIO),
    verdict("fanhattan-inc", "member",
            "Fanhattan (Fan TV, San Mateo): its investors included NEA, Redpoint Ventures, BV Capital and Greycroft (Variety, 2014); Schilling director on the 2014 Form D.",
            ec="web", conf="high", cite=FAN_BV),
    cls("fanhattan-inc", status="acquired", city="San Mateo", rng="below_1b",
        note="acq. by Rovi, November 2014, all cash (Business Wire 2014-11-03). BV Capital was an investor before the 2014 filing; the 2014 Form D ($18M) is a later round of a 2010 company (band withheld); the entry round goes to the stage pass. The Redpoint book dates the sale 2016: cross-investor alignment item."),
    verdict("global-water-farms-inc", "not_member", "Jonathan Becker homonym: an executive officer of a water company (2020).",
            ec="formd_adjudicated", conf="high"),
    verdict("glove-holdings-inc", "not_member", f"{BROWN} Here a 2011-2013 Woodland Hills director seat, before his Headline tenure.",
            ec="formd_adjudicated", conf="high", cite=MAT_BIO),
    verdict("goldin-parent-inc", "not_member",
            "Matthew Brown as director of Goldin (collectibles auctions, 2021): Headline's Matt Brown was then a Vice President at The Chernin Group, whose portfolio includes Collectors (his CMS bio); a prior-firm seat (T4).",
            ec="formd_adjudicated", conf="high", cite=MAT_BIO),
    verdict("itinerate-inc", "not_member", f"{BROWN} Here an executive officer of a Denver issuer (2019).",
            ec="formd_adjudicated", conf="high", cite=MAT_BIO),
]
if __name__ == "__main__":
    write("batch-005", L, record="--dry" not in sys.argv)
