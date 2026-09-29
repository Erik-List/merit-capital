"""PRO-75 GV grind, judge j8: queue batch 8 (45 member rows, makani .. nava-therapeutics).
Pattern copied from judgments-pilot.py. Every URL below is either printed by a helper (SITE, POST, W, NEWS, FTS) or a
page this judge read (TechCrunch search API, the company's own site, SEC filings listed by EDGAR, stockanalysis.com)."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, verdict, rnd, POST, SITE, ARCH, W, NEWS, FTS = (jl.cls, jl.verdict, jl.rnd, jl.POST, jl.SITE, jl.ARCH, jl.W,
                                                      jl.NEWS, jl.FTS)
L = []
ASOF = "2026-09-28"


def post_exact(slug):
    """The firm's own post whose slug is exactly `slug` (POST() matches substrings)."""
    m = [p["url"] for p in jl._POSTS if p.get("slug") == slug]
    if len(m) != 1:
        raise SystemExit(f"post_exact({slug!r}) matched {len(m)}")
    return m[0]


# ---- pages read by this judge (TechCrunch search API / tag pages, company sites, EDGAR, stockanalysis)
MBQ_SEED = "https://techcrunch.com/2014/11/19/managed-by-q-the-platform-for-office-management-closes-1-65m-seed-round/"
MBQ_A = "https://techcrunch.com/2015/06/18/managed-by-q-sweeps-up-15m-led-by-rre-ventures-expands-to-san-francisco/"
MBQ_B = "https://techcrunch.com/2016/04/01/managed-by-q-the-digital-office-administrator-raises-25-million/"
MATTER_A = "https://techcrunch.com/2021/10/06/matter-raises-7-million-series-a-to-build-a-better-reading-app/"
MATTER_2026 = "https://techcrunch.com/2026/08/14/read-it-later-app-pocket-is-shutting-down-here-are-the-best-alternatives/"
MAZE_S1 = "https://www.sec.gov/Archives/edgar/data/1842295/000119312525002851/d769642ds1.htm"
SA_MAZE = "https://stockanalysis.com/stocks/maze/market-cap/"
MEDALLION_C = "https://medallion.co/news/medallion-raises-35-million-in-series-c"
MEDALLION_2025 = "https://www.medallion.co/news/medallion-raises-43-million-to-expand-ai-infrastructure-and-launch-credalliance"
MEDIUM_A = "https://techcrunch.com/2014/01/28/blogging-platform-medium-reportedly-closes-25m-round-led-by-greylock/"
MELTANO_B = "https://techcrunch.com/2022/06/08/gitlab-spinoff-meltano-raises-another-8-2m-for-its-open-source-dataops-platform/"
MELTANO_ARCH = "https://meltano.com/blog/looking-for-arch"
MERIDA_A = ("https://meridabio.com/news/merida-biosciences-launches-with-121m-to-create-therapeutics-for-multiple-"
            "autoimmune-and-allergic-diseases/")
MERIDA_LILLY = ("https://meridabio.com/news/lilly-to-acquire-merida-biosciences-to-advance-treatments-for-serious-"
                "autoimmune-and-allergic-diseases/")
MESSAGEME_A = ("https://techcrunch.com/2013/05/16/messageme-raises-a-10m-series-a-led-by-greylock-as-it-gears-up-for-"
               "money-and-premium-services-in-its-rich-messaging-app/")
METABIOTA_A = ("https://techcrunch.com/2015/05/20/metabiota-pulls-in-30-million-in-funding-to-help-predict-the-global-"
               "spread-of-disease/")
METSERA_S1 = "https://www.sec.gov/Archives/edgar/data/2040807/000119312525004504/d900229ds1.htm"
SPARE5_A = "https://techcrunch.com/2015/08/25/spare5-raises-10m-series-a-round-for-its-mobile-mechanical-turk-service/"
MILK_SEED = "https://techcrunch.com/2011/11/07/google-ventures-takes-a-sip-of-milk-invests-in-kevin-roses-new-startup/"
MILK_HIRE = "https://techcrunch.com/2012/03/15/winning-a-bidding-war-with-facebook-google-picks-up-the-entire-milk-team/"
EXPECT_SEED = ("https://techcrunch.com/2012/10/04/disrupt-battlefield-finalist-expect-labs-locks-up-2-4m-in-funding-"
               "for-its-real-time-conversation-analyzer/")
EXPECT_2013 = ("https://techcrunch.com/2013/07/22/expect-labs-nabs-idg-and-liberty-global-as-strategic-investors-says-"
               "ipad-app-launch-is-in-the-works/")
MINDMELD_CISCO = "https://techcrunch.com/2017/05/11/cisco-acquires-conversational-ai-startup-mindmeld-for-125-million/"
MIRVIE_B = ("https://www.mirvie.com/mirvie-media-releases/mirvie-raises-60-million-funding-round-to-shape-the-future-"
            "of-pregnancy-health")
MITRO_SEED = "https://techcrunch.com/2013/09/05/mitro-passwords/"
MITRO_TW = "https://techcrunch.com/2014/07/31/twitter-mitro/"
MODSY_SEED = "https://techcrunch.com/2015/10/29/modsy-brings-the-virtual-when-designing-reality/"
MODSY_A = "https://techcrunch.com/2016/02/02/modsy-raises-8m-series-a-as-it-gears-for-public-launch/"
MODSY_B = "https://techcrunch.com/2017/12/07/3d-home-design-startup-modsy-raises-23-million-in-series-b-funding/"
MODSY_SHUT = "https://techcrunch.com/2022/07/17/modsy-quietly-shut-down-while-some-customers-were-still-awaiting-refunds/"
MODULAR_SEED = ("https://techcrunch.com/2022/06/30/modular-closes-30m-seed-round-to-simplify-the-process-of-"
                "developing-ai-systems/")
MODULAR_100 = "https://techcrunch.com/2023/08/24/modular-raises-100m-for-ai-dev-tools/"
MODULAR_GC = "https://www.generalcatalyst.com/stories/our-investment-in-modular"
MODULAR_TERMS = "https://www.modular.com/legal/terms"
MOHAWK_FD = "https://www.sec.gov/Archives/edgar/data/1614019/000161401917000001/primary_doc.xml"
MOHAWK_FD14 = "https://www.sec.gov/Archives/edgar/data/1614019/000161401914000001/primary_doc.xml"
MOHAWK_S1 = "https://www.sec.gov/Archives/edgar/data/1757715/000119312519144273/d639806ds1.htm"
SA_ATER = "https://stockanalysis.com/stocks/ater/market-cap/"
GLUE_S1 = "https://www.sec.gov/Archives/edgar/data/1826457/000119312521182268/d47776ds1.htm"
SA_GLUE = "https://stockanalysis.com/stocks/glue/market-cap/"
MONZO_I = "https://techcrunch.com/2024/05/08/uk-challenger-bank-monzo-nabs-another-190m-at-5-2b-valuation/"
MONZO_SEC = "https://techcrunch.com/2024/10/11/uk-neobank-monzo-hits-5-9b-valuation-with-secondary-market-sale/"
MOONHUB_SEED = ("https://techcrunch.com/2023/02/07/moonhub-wants-to-transform-the-way-companies-find-job-candidates-"
                "using-ai/")
MOONHUB_END = "https://techcrunch.com/2025/06/02/salesforce-buys-moonhub-a-startup-building-ai-tools-for-hiring/"
MOTHER_2026 = ("https://www.alleywatch.com/2026/05/degen-mother-tech-ai-creative-app-prompt-free-ai-content-meme-"
               "generator-creator-economy-platform-kelsey-falter/")
KT_2013 = "https://techcrunch.com/2013/12/11/keeptruckin/"
KT_A = ("https://techcrunch.com/2015/10/29/keeptruckin-raises-8m-led-by-index-ventures-to-bring-logging-miles-for-"
        "truckers-into-the-21st-century/")
MPARTICLE_SEEDX = "https://techcrunch.com/2014/10/09/mparticle-seed-funding/"
MPARTICLE_A = "https://techcrunch.com/2016/01/13/mparticle-series-a/"
N3_A = "https://techcrunch.com/2013/06/05/n3twork/"
NAMO_SEED = "https://techcrunch.com/2013/03/18/namo-media-seed-round/"
NANIT_TC = "https://techcrunch.com/2021/02/22/nanit-raises-another-25m-for-its-ai-powered-baby-monitor/"
LEAVE = "Graduation left for the graduation pass."

# ---------------------------------------------------------------- makani
L.append(cls("makani", status="acquired", rng="below_1b", country="US", city="Alameda", city_src="web_verified",
    focus="Climate & Energy", stage="undetermined", rounds=[],
    note="Airborne wind turbines (Makani Technologies, 'an Alameda, California-based company', Wikipedia). It 'received "
         "funding as part of Google.org's Renewable Energy cheaper than Coal (RE<C) initiative'; Google acquired it in May "
         "2013 and folded it into Google X, and Alphabet shut it down in February 2020 (Wikipedia, " + W("Makani (company)")
         + "). The firm's listing carries it from its 2016 capture only, with the exit line 'Acquired by Google, 2013'. No "
         "source read names a GV round, so the stage is undetermined. Membership question for the report: the only funder "
         "on record is Google.org, not a GV vehicle (decisions D2)."))

# ---------------------------------------------------------------- managed-by-q
L.append(cls("managed-by-q", status="acquired", rng="below_1b", country="US", city="New York", focus="SaaS",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=MBQ_B, entry_date="2016-04",
    rounds=[rnd("2014-11-19", "Seed", 1650000, None, False, MBQ_SEED, "press"),
            rnd("2015-06-18", "Series A", 15000000, "RRE Ventures", False, MBQ_A, "press"),
            rnd("2016-04-01", "Series B", 25000000, "GV and Kapor", True, MBQ_B, "press")],
    note="Office management platform and services marketplace (New York). 'Managed By Q is today announcing the raise of a "
         "$25 million Series B round from GV and Kapor' (TechCrunch, 2016-04-01); the $1.65M seed (Homebrew, RRE) and the "
         "$15M RRE-led Series A named no GV, so the Series B is the entry, Growth. WeWork acquired it in April 2019 and sold "
         "it to Eden in March 2020 (Wikipedia, " + W("Managed by Q") + ")."))

# ---------------------------------------------------------------- matter
L.append(cls("matter", status="private", rng="below_1b", country="US", city="San Francisco",
    focus="Media, Gaming & Advertising", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=MATTER_A, entry_date="2021-10", flags=["model_disputes_source"],
    rounds=[rnd(None, "Seed", 2000000, None, False, MATTER_A, "press"),
            rnd("2021-10-06", "Series A", 7000000, "GV", True, MATTER_A, "press")],
    note="Read-it-later and reading app (getmatter.app; founders Ben Springwater and Robert Mackenzie, ex-Nextdoor). GV led "
         "the $7M Series A (TechCrunch, 2021-10-06); the earlier $2M seed came from Patrick Collison, Lachy Groom and the "
         "Hartzes, no GV. Still operating: TechCrunch lists 'a GV-backed company' Matter first among Pocket alternatives "
         "(2026-08-14, " + MATTER_2026 + "). The prefilled GB country is a one-word Wikidata join; the company is US "
         "(city aligned with sibling Y Combinator's row). Sibling a16z's Matter (Berlin, crypto) is a different company "
         "(Matter Labs), a name collision."))

# ---------------------------------------------------------------- maze-therapeutics
L.append(cls("maze-therapeutics", rng="1b_plus", usd=1490000000, val_src="web_verified", val_cite=SA_MAZE, asof=ASOF,
    country="US", city="South San Francisco", city_src="web_verified", focus="Healthcare & Bio",
    stage="Series A", stage_src="model", stage_conf="medium", stage_cite=NEWS("maze-therapeutics", "debuts with $191M"),
    entry_date="2019-02", flags=["model_disputes_source"],
    extra={"valuation_range_source": "web_verified"},
    rounds=[rnd("2019-02-28", "Launch financing (Series A)", 191000000, None, True,
                NEWS("maze-therapeutics", "debuts with $191M"), "press"),
            rnd("2021-12", "Series C", 120600000, None, None, MAZE_S1, "filing"),
            rnd("2024-11", "Series D and D-1", 75000000, None, True, MAZE_S1, "filing")],
    note="Genetics-driven medicines (South San Francisco, the S-1's principal office). GV is named in the $191M launch "
         "financing 'from ARCH Venture Partners, GV, Foresite Capital, Casdin Capital, Alexandria ... in addition to Third "
         "Rock' (Fierce Biotech, 2019-02-28); the round is unnamed there, and the S-1 shows Series A as the first preferred "
         "series (Third Rock bought 55M of its 105M shares), so the entry reads Series A at medium confidence. GV 2019 and "
         "GV 2023 hold over 5% and GV 2023 bought notes and Series D-1 (S-1, " + MAZE_S1 + "). Mark: market cap $1.49B as of "
         "2026-09-28 (stockanalysis.com), replacing the prefilled $443.9M float; sibling a16z's row still carries that "
         "2025-06-30 figure and should move with this fresher cap."))

# ---------------------------------------------------------------- mechanical-orchard
L.append(cls("mechanical-orchard", status="private", rng="below_1b", city="San Francisco", city_src="formd_address",
    focus="DevTools & APIs",
    note="AI-assisted mainframe application modernization (San Francisco; Form D address 1 Post St., and TechCrunch's "
         "'San Francisco-based'). The firm's own post: 'we convinced them to let us lead their $50M Series B' ("
         + POST("mechanical-orchard") + "), consistent with the prefilled Growth band; TechCrunch reports the $50M Series B "
         "led by GV, total raised $74M (" + NEWS("mechanical-orchard", "scores $50M") + "). Momentum check (AI and dev "
         "tools, first seen 2024; Google News, 2026-09-28): no later priced round and no $1B+ valuation found."))

# ---------------------------------------------------------------- medallion
L.append(cls("medallion", status="private", rng="below_1b", country="US", country_src="web_verified",
    country_cite=MEDALLION_C, city="San Francisco", city_src="web_verified", focus="Healthcare & Bio",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=MEDALLION_C, entry_date="2022-06",
    flags=["model_disputes_source"],
    rounds=[rnd("2022-06-23", "Series C", 35000000, "Spark Capital and GV", True, MEDALLION_C, "company"),
            rnd("2025-08-18", "Unnamed", 43000000, "Acrew Capital", True, MEDALLION_2025, "company")],
    note="Clinician licensing, credentialing and payer enrollment platform (San Francisco dateline). 'The round was co-led "
         "by Spark Capital and new investor GV' in the $35M Series C (the company's release, 2022-06-23), so GV entered at "
         "the Series C, Growth. GV is among the insiders in the Acrew-led $43M round of August 2025 (total $130M). The "
         "prefilled SE country is a one-word Wikidata join (siblings Sequoia and Spark read San Francisco, US)."))

# ---------------------------------------------------------------- medium
L.append(cls("medium", status="private", rng="below_1b", city="San Francisco", focus="Media, Gaming & Advertising",
    stage="Series A", stage_src="model", stage_conf="medium", stage_cite=MEDIUM_A, entry_date="2014-01",
    rounds=[rnd("2014-01-28", "Series A", 25000000, "Greylock", True, MEDIUM_A, "press")],
    note="Ev Williams' publishing platform (San Francisco). Its first outside round, $25M led by Greylock with Google "
         "Ventures participating (TechCrunch, 2014-01-28), is unnamed in that article; sibling Greylock's own listing names "
         "it the Series A, so the entry reads Series A at medium confidence. Later rounds (the 2015-2016 growth rounds led "
         "by Spark) are after GV's entry. Aligned with siblings a16z, Greylock and Spark: private, below $1B."))

# ---------------------------------------------------------------- meltano
L.append(cls("meltano", status="acquired", rng="below_1b", country="US", focus="Data Infrastructure",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("meltano", "GitLab spins out"),
    entry_date="2021-06", flags=["city_unknown"],
    rounds=[rnd("2021-06-30", "Seed", 4200000, "GV", True, NEWS("meltano", "GitLab spins out"), "press"),
            rnd("2022-06-08", "Unnamed", 8200000, "Venrock", True, MELTANO_B, "press")],
    note="Open-source ELT (GitLab spin-out, remote-only per TechCrunch). A '$4.2 million seed funding round' led by GV "
         "(VentureBeat, 2021-06-30); Venrock led an unnamed $8.2M round in June 2022 with GV participating (TechCrunch), "
         "below twice the seed, so it does not graduate the row on its own. The company rebranded its cloud product as "
         "Arch; 'Arch has officially shut down' and 'Matatika has acquired the Meltano open source project' (meltano.com, "
         + MELTANO_ARCH + "), which now runs under the Meltano name from London: an asset sale, read acquired with "
         "Matatika as successor. No source places the company itself, hence city_unknown. " + LEAVE))

# ---------------------------------------------------------------- merida-biosciences
L.append(cls("merida-biosciences", status="private", rng="below_1b", country="US", city="Cambridge",
    city_src="web_verified", focus="Healthcare & Bio", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=MERIDA_A, entry_date="2025-04",
    rounds=[rnd("2022", "Seed", None, "Third Rock Ventures", False, MERIDA_A, "company"),
            rnd("2025-04-08", "Series A", 121000000, "Bain Capital Life Sciences, BVF Partners, Third Rock Ventures",
                True, MERIDA_A, "company")],
    note="Autoimmune and allergy therapeutics (Cambridge, MA). $121M Series A co-led by Bain Capital Life Sciences, BVF "
         "Partners and Third Rock, with 'GV and Perceptive Xontogeny' participating; 'Merida was seeded in 2022 by Third "
         "Rock Ventures' (the company's release, 2025-04-08). Lilly signed a definitive agreement on 2026-08-31 to acquire "
         "it for 'up to $2.875 billion in cash, inclusive of an upfront payment, and contingent milestone payments', "
         "expected to close in the fourth quarter of 2026 (" + MERIDA_LILLY + "): still private until closing. The upfront "
         "is undisclosed, so no citable figure reaches $1B and the row holds below $1B; flagged for review (it reads "
         "acquired at closing)."))

# ---------------------------------------------------------------- messageme
L.append(cls("messageme", status="acquired", rng="below_1b", country="US", city="San Francisco",
    focus="Consumer & Marketplaces", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=W("MessageMe"), entry_date="2013",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=MESSAGEME_A,
    rounds=[rnd("2013", "Seed", 1900000, None, True, W("MessageMe"), "press"),
            rnd("2013-05-16", "Series A", 10000000, "Greylock Partners", True, MESSAGEME_A, "press")],
    note="Mobile messaging app (San Francisco). 'It raised a $1.9 million seed round from First Round Capital, Google "
         "Ventures, SV Angel and Andreessen Horowitz' (Wikipedia); the seed was first reported with the $10M Series A led "
         "by Greylock, in which Google Ventures also took part (TechCrunch, 2013-05-16). Yahoo acquired it in October 2014 "
         "for $30M to $40M (Wikipedia). Aligned with siblings a16z, First Round and Greylock."))

# ---------------------------------------------------------------- mestag-therapeutics
MESTAG_40 = NEWS("mestag-therapeutics", "Mestag Therapeutics Announces $40 Million")
L.append(cls("mestag-therapeutics", status="private", rng="below_1b", country="GB", country_src="web_verified",
    country_cite=MESTAG_40, city="Cambridge", city_src="web_verified", focus="Healthcare & Bio",
    stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("mestag-therapeutics", "J&J, Google back"), entry_date="2021-08",
    rounds=[rnd("2021-04", "Seed", 11000000, None, False, NEWS("mestag-therapeutics", "launches with $11m"), "press"),
            rnd("2021-08-03", "Seed extension", 45000000, None, True,
                NEWS("mestag-therapeutics", "J&J, Google back"), "press"),
            rnd("2026-03-17", "Unnamed", 40000000, None, True, MESTAG_40, "company")],
    note="Fibroblast immunology for inflammation and cancer (Cambridge, UK, per its 2026 release). It launched with an $11M "
         "seed from SV Health and J&J Innovation (Cambridge Independent, 2021-04), then 'extended its seed round' to $45M "
         "to include Forbion 'alongside Google's GV, Northpond Ventures' (Fierce Biotech, 2021-08-03): GV entered in the "
         "seed extension. The March 2026 $40M financing (SV Health, J&J, Forbion, GV, Northpond) is unnamed and below twice "
         "the seed. " + LEAVE))

# ---------------------------------------------------------------- metabiota
L.append(cls("metabiota", city="San Francisco", city_src="web_verified", rng="below_1b", focus="Healthcare & Bio",
    stage="undetermined",
    rounds=[rnd("2015-05-20", "Series A", 30000000, "RSTP", False, METABIOTA_A, "press")],
    note="Epidemic risk analytics (San Francisco, Wikipedia and TechCrunch). The $30M Series A led by RSTP (TechCrunch, "
         "2015-05-20) names Capricorn Healthcare, WP Global Partners, Industry Ventures and Data Collective, not GV; "
         "Wikipedia says only that 'Google invested $1 million into the company' (" + W("Metabiota") + "), with no round "
         "or date. The firm lists it from 2015 (Krishna Yeshwant). GV's round is not named, so undetermined. Status as "
         "prefilled: Ginkgo Bioworks bought its epidemiological data assets in August 2022."))

# ---------------------------------------------------------------- metaview
L.append(cls("metaview", status="private", rng="below_1b", city="London", city_src="formd_address",
    focus="AI & Applied AI",
    note="AI note-taking and hiring platform (London; Form D address 2-20 Scrutton Street). The firm's own post announces "
         "'our lead investment in Metaview's $35 million Series B round' (" + POST("metaview-ai") + "), consistent with the "
         "prefilled Growth band (Tech.eu, " + NEWS("metaview", "raises $35M to replace hiring guesswork") + "). Momentum "
         "check (AI, first seen 2025; Google News, 2026-09-28): no later priced round found (it bought Reval in August "
         "2026), no $1B+ valuation."))

# ---------------------------------------------------------------- metsera
L.append(cls("metsera", country="US", city="New York", city_src="web_verified", rng="below_1b",
    focus="Healthcare & Bio", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=METSERA_S1,
    entry_date="2024-04",
    rounds=[rnd("2023-05", "Series Seed", 35000000, None, False, METSERA_S1, "filing"),
            rnd("2023-08", "Series A", 240000000, None, True, METSERA_S1, "filing"),
            rnd("2024-11", "Series B", 215000000, None, True, METSERA_S1, "filing")],
    note="Obesity medicines (New York; the S-1's principal office at 3 World Trade Center). The S-1's related-party table "
         "shows GV 2023, L.P. buying 7,333,332 Series A shares (Series A sold August 2023 to August 2024 at $3.00) and "
         "992,063 Series B shares, and no Series Seed. GV is named in the $290M launch financing led by ARCH (BioSpace, "
         "2024-04-18, " + NEWS("metsera", "Weight-Loss Drug Startup Metsera Launches") + "). Status as prefilled: Pfizer "
         "acquired it in November 2025 (the firm's exit line)."))

# ---------------------------------------------------------------- midi-health
MIDI_D = NEWS("midi-health", "Series D At Over $1 Billion")
L.append(cls("midi-health", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified", val_cite=MIDI_D,
    asof="2026-02", country="US", city="Palo Alto", city_src="web_verified", focus="Healthcare & Bio",
    stage="Series A", stage_src="first_party", stage_conf="high", stage_cite=POST("midi-womens-health"),
    entry_date="2023-09", extra={"valuation_range_source": "web_verified"},
    rounds=[rnd("2023-09-27", "Series A", 25000000, "GV", True, POST("midi-womens-health"), "firm"),
            rnd("2026-02", "Series D", 100000000, "Goodwater Capital", True, MIDI_D, "press")],
    note="Virtual menopause and midlife care clinic ('The Palo Alto-based company', Pulse 2.0). The firm's own post: 'GV is "
         "leading a $25M Series A' and welcomes the company to the portfolio (2023-09-27); Felicis's $14M seed of 2022 had "
         "no GV. Mark: the $100M Series D led by Goodwater 'values the women's telehealth company at over $1 billion', with "
         "GV continuing (Pulse 2.0, 2026-02); recorded at the $1B floor the sources state, at the band edge. Sibling "
         "Felicis's row reads below $1B and should move to this fresher priced round."))

# ---------------------------------------------------------------- mighty-ai
MIGHTY_14 = NEWS("mighty-ai", "Spare5 re-launches")
L.append(cls("mighty-ai", status="acquired", rng="below_1b", country="US", city="Seattle", city_src="web_verified",
    focus="AI & Applied AI", stage="Growth", stage_src="model", stage_conf="medium", stage_cite=MIGHTY_14,
    entry_date="2017-01",
    rounds=[rnd("2015-08-25", "Series A", 10000000, "Foundry Group, Madrona, NEA", False, SPARE5_A, "press"),
            rnd("2017-01-10", "Unnamed", 14000000, "Intel Capital", True, MIGHTY_14, "press")],
    note="AI training data (Spare5, renamed Mighty AI; 'Seattle startup', GeekWire). Spare5's $10M Series A was led by "
         "Foundry, Madrona and NEA with no GV (TechCrunch, 2015-08-25); the $14M round of January 2017 was 'led by Intel "
         "Capital ... and also included participation from Accenture and GV' (GeekWire, 2017-01-10). That round is unnamed "
         "but follows the named Series A, so GV's entry reads Growth at medium confidence. Uber acquired it in June 2019 "
         "(GeekWire; the firm's exit line)."))

# ---------------------------------------------------------------- milk
L.append(cls("milk", status="defunct", rng="below_1b", country="US", city="San Francisco",
    focus="Consumer & Marketplaces", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=MILK_SEED,
    entry_date="2011-11", flags=["model_disputes_source"],
    rounds=[rnd("2011-11-07", "Seed", 1700000, None, True, MILK_SEED, "press")],
    note="Kevin Rose's mobile app lab (Oink). Google Ventures joined the seed, which then totalled $1.7M (TechCrunch, "
         "2011-11-07). In March 2012 Google hired the team in 'an acqui-hire type deal'; 'Google is not picking up the Oink "
         "app itself or the technology' and 'The Oink app itself shut down' (TechCrunch, 2012-03-15, " + MILK_HIRE + "). "
         "Under the acqui-hire ruling (2026-09-20) the company's own fate decides: defunct, not acquired; the firm's exit "
         "line 'Acquired by Google, 2012' and sibling First Round's acquired row predate that ruling. The prefilled JP "
         "country is a one-word Wikidata join (also on First Round's row). " + LEAVE))

# ---------------------------------------------------------------- mill
MILL_PR = NEWS("mill", "Compass Group")
L.append(cls("mill", status="private", rng="below_1b", country="US", country_src="web_verified", country_cite=MILL_PR,
    city="San Bruno", city_src="web_verified", focus="Climate & Energy", stage="undetermined",
    flags=["model_disputes_source"], rounds=[],
    note="Food-waste recycler for homes and commercial kitchens (Mill Industries; 'headquartered in San Bruno, California', "
         "founded 2020 by Nest's Matt Rogers and Harry Tannenbaum, its release of 2026-04-27 announcing a Compass Group "
         "partnership). The prefilled defunct status and GB country are a one-word Wikidata join; the company operates "
         "(also Whole Foods deployment news, December 2025). It had 'raised about $100 million from investors like Google "
         "Ventures, Breakthrough Energy Ventures, Energy Impact Partners, Lowercarbon, and Prelude' (Business Insider, "
         "2023-01, " + NEWS("mill", "exclusive pitch deck food waste") + ") and discloses no round detail, so GV's round "
         "is undetermined."))

# ---------------------------------------------------------------- mimic
MIMIC_A = NEWS("mimic", "Ransomware defense company Mimic")
L.append(cls("mimic", status="private", rng="below_1b", country="US", city="Palo Alto", city_src="web_verified",
    focus="Security", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=MIMIC_A,
    entry_date="2025-02",
    rounds=[rnd("2025-02-27", "Series A", 50000000, "GV and Menlo Ventures", True, MIMIC_A, "company")],
    note="Ransomware defense ('Founded in 2023, Mimic is headquartered in Palo Alto, California'). 'Series A funding of $50 "
         "million led by GV (Google Ventures) and Menlo Ventures' (the company's release, 2025-02-27); the firm lists it "
         "from 2025 and no source puts GV in the Ballistic-led 2024 seed that sibling Menlo joined. The city follows the "
         "company's own release, where sibling Menlo's row reads San Francisco."))

# ---------------------------------------------------------------- mindmeld
L.append(cls("mindmeld", status="acquired", rng="below_1b", country="US", city="San Francisco",
    city_src="web_verified", focus="AI & Applied AI", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=EXPECT_SEED, entry_date="2012-10",
    rounds=[rnd("2012-10-04", "Seed", 2400000, None, True, EXPECT_SEED, "press"),
            rnd("2013-07-22", "Strategic (Intel, Samsung, Telefonica, IDG, Liberty Global)", None, None, None,
                EXPECT_2013, "press")],
    note="Expect Labs, renamed MindMeld, conversational AI ('The San Francisco startup'). It 'locked up a $2.4 million "
         "investment ... from KPG Ventures, Google Ventures, and Greylock Partners' (TechCrunch, 2012-10-04), a round "
         "TechCrunch later calls 'the startup's $2.4 million seed round' (2013-07-22); the 2013 strategic investments are "
         "undisclosed in size. Cisco bought it for $125M in May 2017 (TechCrunch, " + MINDMELD_CISCO + "). " + LEAVE))

# ---------------------------------------------------------------- mindsumo
MINDSUMO_MBO = NEWS("mindsumo", "MBO Partners")
L.append(cls("mindsumo", status="acquired", rng="below_1b", country="US", city="Durham", city_src="web_verified",
    focus="SaaS", stage="undetermined", rounds=[],
    note="Challenge-based student recruiting and open innovation platform ('based out of Durham, N.C.' at its sale). MBO "
         "Partners agreed to acquire MindSumo, Inc. on 2020-09-29 (" + MINDSUMO_MBO + "). The firm lists it from 2013 "
         "(Andy Wheeler); no source read names its funding rounds, so GV's round is undetermined."))

# ---------------------------------------------------------------- mirrortab
MIRRORTAB_SEED = NEWS("mirrortab", "Raises $8.5M Seed Round")
L.append(cls("mirrortab", status="private", rng="below_1b", country="US", city="San Francisco",
    city_src="web_verified", focus="Security", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=MIRRORTAB_SEED, entry_date="2025-02", grad="censored",
    rounds=[rnd("2025-02-18", "Seed", 8500000, "Valley Capital Partners", True, MIRRORTAB_SEED, "press")],
    note="Browser-side defense for web applications ('San Francisco startup'; MirrorTab Corp. files from San Francisco). "
         "'$8.5 million in seed funding led by Valley Capital Partners' with GV participating (SecurityWeek, 2025-02-18). "
         "Entry inside 24 months, so censored."))

# ---------------------------------------------------------------- mirvie
L.append(cls("mirvie", status="private", rng="below_1b", country="US", city="South San Francisco",
    city_src="web_verified", focus="Healthcare & Bio", stage="Growth", stage_src="model", stage_conf="medium",
    stage_cite=MIRVIE_B, entry_date="2022-05",
    rounds=[rnd("2022-05-17", "Series B", 60000000, "Decheng Capital", True, MIRVIE_B, "company")],
    note="RNA blood test for pregnancy complications ('based in South San Francisco'). The $60M Series B 'was led by Decheng "
         "Capital with additional funding from ... BlackRock, Foresite Capital, General Catalyst, GV, Khosla Ventures, and "
         "Mayfield' (the company's release, 2022-05-17); the release does not say which investors were new, and the firm's "
         "listing first carries Mirvie in 2022, so the entry reads the Series B, Growth, at medium confidence. Aligned "
         "with siblings General Catalyst and Khosla."))

# ---------------------------------------------------------------- mist-systems
L.append(cls("mist-systems", status="acquired", rng="below_1b", city="Cupertino", city_src="formd_address",
    focus="Data Infrastructure",
    note="AI-driven enterprise wireless networking (Cupertino; Form D address 1601 S. De Anza Blvd.). Juniper Networks "
         "bought it for $405M in 2019 (CRN headline; the firm's exit line). The prefilled Growth band dates GV's entry to "
         "the December 2017 filing, but the firm's listing already carries Mist in 2016, so that date is a ceiling; no "
         "source read names GV's first round."))

# ---------------------------------------------------------------- mitro
L.append(cls("mitro", status="acquired", rng="below_1b", country="US", city="New York", city_src="web_verified",
    focus="Security", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=MITRO_SEED,
    entry_date="2013",
    rounds=[rnd("2013", "Seed", 1200000, None, True, MITRO_SEED, "press")],
    note="Team password manager ('New York-based', TechCrunch). 'Backed by $1.2 million in seed funding from Google Ventures "
         "and Matrix Partners' (TechCrunch, 2013-09-05; Wikipedia agrees). Twitter acquired it and open-sourced the "
         "product in July 2014 (TechCrunch, " + MITRO_TW + "); the service shut down in October 2015. " + LEAVE))

# ---------------------------------------------------------------- mode
MODE_PR = NEWS("mode", "Mode Emerges from Stealth")
L.append(cls("mode", status="acquired", rng="below_1b", country="US", country_src="web_verified", country_cite=MODE_PR,
    city="San Francisco", city_src="web_verified", focus="Data Infrastructure", stage="Growth",
    stage_src="web_verified", stage_conf="high", stage_cite=MODE_PR, entry_date="2018-06",
    flags=["model_disputes_source"],
    rounds=[rnd("2017", "Series A", 8000000, "NEA", False, MODE_PR, "company"),
            rnd("2018-06-07", "Series B", 16000000, "GV", True, MODE_PR, "company")],
    note="Cloud private network for SD-WAN (Mode.net; SAN FRANCISCO dateline). The company's release: an '$8 million Series "
         "A led by NEA' closed the year before and a '$16 million Series B led by GV' (2018-06-07), so GV entered at the "
         "Series B, Growth. VMware acquired it in 2020 (the firm's exit line). The prefilled GB country is a one-word "
         "Wikidata join."))

# ---------------------------------------------------------------- modern-age
MODAGE = NEWS("modern-age", "Healthcare Brew")
L.append(cls("modern-age", status="defunct", rng="below_1b", country="US", city="New York", focus="Healthcare & Bio",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=MODAGE, entry_date="2021-10",
    rounds=[rnd("2021-10", "Series A", 27000000, "Oak HC/FT", True, MODAGE, "press")],
    note="Longevity and healthy-aging clinics (two New York City clinics). It raised '$27 million in a Series A fundraise in "
         "October 2021 led by Oak HC/FT, alongside GV' ($33M in all), and shut down in March 2024 'after failing to secure "
         "adequate outside capital' (Healthcare Brew, 2024-03-22)."))

# ---------------------------------------------------------------- modsy
L.append(cls("modsy", status="acquired", rng="below_1b", city="San Francisco", city_src="formd_address",
    focus="Consumer & Marketplaces", grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=MODSY_A,
    rounds=[rnd("2015", "Seed", 2750000, None, None, MODSY_SEED, "press"),
            rnd("2016-02-02", "Series A", 8000000, None, None, MODSY_A, "press"),
            rnd("2017-12-07", "Series B", 23000000, "Advance Venture Partners", None, MODSY_B, "press")],
    note="3D online interior design (Pencil & Pixel, Inc., San Francisco). The prefilled Seed rests on the March 2015 Form "
         "D; the $8M Series A of February 2016 (TechCrunch) is a named later round, so the row graduates, as the Form D "
         "layer also finds. Caveat for review: the band's anchor is founder Shanna Tellerman, a former Google Ventures "
         "partner filing as Modsy's own executive, not a GV seat, and the spring 2015 seed of $2.75M names 'Norwest Venture "
         "Partners, Metamorphic Ventures and others' (TechCrunch, 2015-10-29), not GV. Modsy ceased operations on 2022-07-06 "
         "and its assets went to Pencil, LLC through an assignment for the benefit of creditors, reportedly funded in part "
         "by Lennar's venture arm (TechCrunch, " + MODSY_SHUT + "); the firm's exit line reads 'Acquired by Lennar, 2023': "
         "an asset sale out of insolvency, read acquired."))

# ---------------------------------------------------------------- modular
BLUE_WATER = post_exact("blue-water-autonomy")
L.append(cls("modular", status="acquired", rng="below_1b", country="US", city="Los Altos", city_src="web_verified",
    focus="AI & Applied AI", stage="Series A", stage_src="first_party", stage_conf="medium", stage_cite=BLUE_WATER,
    entry_date="2022-02",
    rounds=[rnd("2022-06-30", "Seed (press) / Series A (GV)", 30000000, "GV", True, MODULAR_SEED, "press"),
            rnd("2023-08-24", "Series B", 100000000, "General Catalyst", True, MODULAR_100, "press")],
    note="AI inference platform and the Mojo language (Chris Lattner, Tim Davis; 'Modular Inc with offices located at 199 "
         "1st Street, Los Altos', " + MODULAR_TERMS + "). GV led the first round: 'we are leading the first round of "
         "funding for Modular' (the firm's post, 2022-06-30, " + POST("modular-ai") + "), and GV's Dave Munichiello later "
         "lists 'Chris Lattner (Modular)' among 'Founders whom I've backed at the Series A' (the firm's post, 2025-08-26). "
         "TechCrunch called that $30M round a seed, but General Catalyst calls the $100M round it led in 2023 'their $100M "
         "Series B financing' (" + MODULAR_GC + "), so the firm's own label holds: Series A, medium confidence. GV's /ai "
         "list dates its first investment 2022-02. Qualcomm completed its acquisition in July 2026 (the company's site and "
         "the firm's exit line); aligned with siblings General Catalyst and Greylock."))

# ---------------------------------------------------------------- mohawk
L.append(cls("mohawk", rng="below_1b", usd=10590000, val_src="web_verified", val_cite=SA_ATER, asof=ASOF,
    country="US", country_src="web_verified", country_cite=MOHAWK_S1, city="New York", city_src="web_verified",
    focus="Consumer & Marketplaces", stage="Growth", stage_src="model", stage_conf="medium", stage_cite=MOHAWK_FD,
    entry_date="2017-03", flags=["model_disputes_source"],
    extra={"valuation_range_source": "web_verified"},
    rounds=[rnd("2014-06-12", "Series A (first Form D)", 26349990, None, False, MOHAWK_FD14, "filing"),
            rnd("2017-03-06", "Series B (inferred from the S-1's series)", 7999998, None, True, MOHAWK_FD, "filing")],
    note="Data-driven consumer products (Mohawk Group Holdings, now Aterian, NASDAQ: ATER; New York, 37 East 18th Street, "
         "per the S-1). The company's Form D of March 2017 (first sale 2017-03-06, $8.0M) lists GV's David Munichiello as "
         "director, and the S-1 says he joined the board on March 6, 2017 (GV 2016 and GV 2017 then held 7.6%, "
         + MOHAWK_S1 + "). Its only earlier filing is the June 2014 round of $26.3M without GV, and the S-1 names the "
         "preferred series A, B, B-1 and C (C in April 2018), so the March 2017 entry reads Series B, Growth, at medium "
         "confidence. Mark: market cap $10.59M as of 2026-09-28 (stockanalysis.com), replacing the prefilled $13.4M; the "
         "firm's exit line 'NASDAQ: MWK' is the old ticker. The prefilled GB country is a one-word Wikidata join."))

# ---------------------------------------------------------------- mokn
MOKN_SW = NEWS("mokn", "Phish-Back Platform - SecurityWeek")
L.append(cls("mokn", status="private", rng="below_1b", country="FR", country_src="web_verified", country_cite=MOKN_SW,
    city="Paris", city_src="web_verified", focus="Security", stage="Series A", stage_src="first_party",
    stage_conf="high", stage_cite=POST("mokn"), entry_date="2026-05",
    rounds=[rnd("2025-10", "Seed", None, "Moonfire and OVNI Capital", False,
                NEWS("mokn", "raises $15M Series A to grow identity"), "press"),
            rnd("2026-05-28", "Series A", 15000000, "GV", True, POST("mokn"), "firm")],
    note="Identity-theft protection by decoy logins ('Paris-based MokN was founded in 2023', SecurityWeek). The firm's own "
         "post: 'We at GV are delighted to lead their Series A' (2026-05-28), GV's first French investment; $15M with "
         "Datadog, Moonfire and OVNI Capital (SecurityWeek). The earlier EUR 2.6M seed of October 2025 had Moonfire and "
         "OVNI (Tech.eu), not GV."))

# ---------------------------------------------------------------- monte-rosa-therapeutics
MR_C = NEWS("monte-rosa-therapeutics", "round - startupticker.ch")
L.append(cls("monte-rosa-therapeutics", rng="below_1b", usd=999020000, val_src="web_verified", val_cite=SA_GLUE,
    asof=ASOF, country="US", city="Boston", city_src="web_verified", focus="Healthcare & Bio",
    stage="Growth", stage_src="model", stage_conf="medium", stage_cite=MR_C, entry_date="2020-09",
    flags=["model_disputes_source"], extra={"valuation_range_source": "web_verified"},
    rounds=[rnd("2019", "Series A", 19250000, "Versant Ventures", False, GLUE_S1, "filing"),
            rnd("2020-04", "Series A-2", 12500000, "New Enterprise Associates", False, GLUE_S1, "filing"),
            rnd("2020-09", "Series B", 96000000, None, True, GLUE_S1, "filing"),
            rnd("2021-03", "Series C", 95000000, "Avoro Capital Advisors", True, MR_C, "press")],
    note="Molecular glue degraders (Boston principal office per the S-1; research in Basel). The S-1 shows the Series A "
         "(2019) bought entirely by Versant and the Series A-2 (April 2020) by NEA; the $96M Series B closed in September "
         "2020, and at the $95M Series C of March 2021 GV is listed among the 'additional existing investors' "
         "(Startupticker), with GV 2019 and GV 2021 signing the March 2021 investors' rights agreement. So GV entered at the "
         "Series B, Growth, medium confidence. Mark: market cap $999.02M as of 2026-09-28 (stockanalysis.com), replacing "
         "the prefilled $212M; within 5% of the $1B band edge."))

# ---------------------------------------------------------------- monzo
L.append(cls("monzo", rng="1b_plus", usd=5900000000, val_src="web_verified", val_cite=MONZO_SEC, asof="2024-10",
    country="GB", country_src="web_verified", country_cite=W("Monzo"), city="London", city_src="web_verified",
    focus="Fintech & Payments", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=MONZO_I,
    entry_date="2024-03", flags=["model_disputes_source"], extra={"valuation_range_source": "web_verified"},
    rounds=[rnd("2024-03", "Series I (first tranche)", 430000000, "CapitalG", True, MONZO_I, "press"),
            rnd("2024-05-08", "Series I extension", 190000000, None, None, MONZO_I, "press"),
            rnd("2024-10-11", "Secondary sale", None, None, None, MONZO_SEC, "press")],
    note="UK digital bank ('a British online bank based in London', Wikipedia). 'The first tranche of the Series I round saw "
         "Alphabet's CapitalG and Google's GV make a rare co-investment' (TechCrunch, 2024-05-08), so GV entered at the "
         "March 2024 Series I, Growth, alongside CapitalG (external under D1; GV's own position is the firm's). Mark: the "
         "October 2024 company-run secondary sale at $5.9B (TechCrunch), replacing the prefilled $2.5B and aligned with "
         "siblings Accel, Coatue, General Catalyst, Ribbit and Thrive. Nubank's reported interest (September 2026) is talk, "
         "not a mark."))

# ---------------------------------------------------------------- moonhub
L.append(cls("moonhub", status="defunct", rng="below_1b", country="US", city="Menlo Park", city_src="web_verified",
    focus="AI & Applied AI", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=MOONHUB_SEED,
    entry_date="2022-06",
    rounds=[rnd("2023-02-07", "Seed", 4400000, "Khosla Ventures and GV", True, MOONHUB_SEED, "press"),
            rnd("2023-10", "Seed extension", 10000000, None, True, NEWS("moonhub", "3 times faster"), "press")],
    note="AI recruiting ('its entire Menlo Park, California-based team', TechCrunch). 'The $4.4 million seed round was led by "
         "Khosla Ventures and GV' (TechCrunch, 2023-02-07); GV's /ai list dates its first investment 2022-06, and the "
         "later money was more seed ('over $10 million in its seed round', Fortune, 2023-10). In June 2025 part of the team "
         "joined Salesforce, which said 'Moonhub has not, in fact, been acquired', and Moonhub shut down (TechCrunch, "
         + MOONHUB_END + "): under the acqui-hire ruling that reads defunct, not the firm's 'Acquired by Salesforce, "
         "2025'. " + LEAVE))

# ---------------------------------------------------------------- moonwalk-biosciences
MOONWALK = NEWS("moonwalk-biosciences", "Moonwalk Biosciences Launches")
L.append(cls("moonwalk-biosciences", status="private", rng="below_1b", country="US", city="South San Francisco",
    city_src="web_verified", focus="Healthcare & Bio", stage="undetermined", entry_date="2024-01",
    rounds=[rnd("2024-01-04", "Seed and Series A (combined)", 57000000, "Alpha Wave Ventures", True, MOONWALK, "company")],
    note="Precision epigenetic medicines (dateline South San Francisco and San Diego). 'The completion of $57 million in seed "
         "and Series A financing from Alpha Wave Ventures, ARCH Venture Partners, Future Ventures, GV, Khosla Ventures and "
         "YK Bioventures' (BioSpace, 2024-01-04) does not say which tranche GV bought, so the stage is undetermined. Sibling "
         "Khosla records a named $70M Series B in September 2026. Aligned with Khosla on status, band and city."))

# ---------------------------------------------------------------- mother-games
L.append(cls("mother-games", status="private", rng="below_1b", country="US", city="New York", city_src="web_verified",
    focus="AI & Applied AI", stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=MOTHER_2026,
    entry_date="2026-05", grad="censored",
    rounds=[rnd("2024-09", "Pre-seed", 5000000, None, False, NEWS("mother-games", "AlleyWatch"), "press"),
            rnd("2026-05", "Pre-seed/seed", 15000000, "GV", True, MOTHER_2026, "press")],
    note="Kelsey Falter's Brooklyn studio (mothergames.com lists 223 Bedford Ave, Brooklyn). Its $5M pre-seed of September "
         "2024 came from BoxGroup, Shine and Lerer Hippeau, no GV (AlleyWatch). In May 2026 the same founder's MOTHER.Tech, "
         "'Brooklyn-based', raised $15M 'pre-seed/seed' led by Google Ventures with Lerer Hippeau, Box Group and Shine "
         "(AlleyWatch, 2026-05), the year the firm first lists Mother Games; read as the same company and a Seed entry at "
         "medium confidence (it follows a pre-seed). Censored. Momentum check (AI, first seen 2026; 2026-09-28): the "
         "$15M round is the latest, no $1B+ valuation."))

# ---------------------------------------------------------------- motive
L.append(cls("motive", status="private", rng="1b_plus", usd=2850000000, val_src="web_verified",
    val_cite=W("Motive (company)"), asof="2022-05", city="San Francisco", city_src="formd_address", focus="SaaS",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=KT_2013, entry_date="2013",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=KT_A,
    flags=["stage_disputes_band", "stale"], extra={"valuation_range_source": "web_verified"},
    rounds=[rnd("2013", "Seed", 2300000, "Google Ventures", True, KT_2013, "press"),
            rnd("2015-10-29", "Series A", 8000000, "Index Ventures", None, KT_A, "press"),
            rnd("2022-05", "Series F", 150000000, "Insight Partners and Kleiner Perkins", True, W("Motive (company)"),
                "press")],
    note="KeepTruckin, renamed Motive, fleet management ('an eight-person, San Francisco-based startup' in 2013). It 'has "
         "raised $2.3 million from investors, including Google Ventures' (TechCrunch, 2013-12-11), 'an earlier round led by "
         "Google Ventures' before the $8M round led by Index (TechCrunch, 2015-10-29); Wikipedia names these the 2013 seed "
         "and the 2015 Series A. So GV entered at the seed, disputing the prefilled Growth band, which read a 2022 filing "
         "(the firm lists KeepTruckin from 2014). The Series A graduates the row. Mark: $2.85B after the 2022 Series F "
         "(Wikipedia), stale; the $1.3B General Catalyst growth financing of September 2026 disclosed no valuation and "
         "Motive withdrew its IPO filing (The Next Web, " + NEWS("motive", "The Next Web") + "). Aligned with siblings "
         "Insight and IVP; sibling Accel's acquired row for 'Motive' looks like a different company or an error."))

# ---------------------------------------------------------------- mparticle
L.append(cls("mparticle", status="acquired", rng="below_1b", country="US", city="New York",
    focus="Data Infrastructure", stage="undetermined",
    rounds=[rnd("2014-10-09", "Seed (additional)", 1500000, None, False, MPARTICLE_SEEDX, "press"),
            rnd("2016-01-13", "Series A", 15000000, "Social Capital", False, MPARTICLE_A, "press")],
    note="Customer data platform (New York, aligned with siblings Bain Capital Ventures and Battery). The firm lists it "
         "from 2013 (Wesley Chan). TechCrunch's reports of the $1.5M additional seed (2014, after $4.5M raised earlier) and "
         "the $15M Series A led by Social Capital (2016) do not name GV; AlleyWatch lists Google Ventures among its backers "
         "without a round. GV's round is undetermined. Rokt acquired it in a $300M transaction in January 2025 (AlleyWatch, "
         + NEWS("mparticle", "Rokt Acquires mParticle") + ")."))

# ---------------------------------------------------------------- multiverse
MV_B = NEWS("multiverse", "formerly WhiteHat, books")
MV_2026 = NEWS("multiverse", "Multiverse: $70 Million Raised At $2.1 Billion")
L.append(cls("multiverse", status="private", rng="1b_plus", usd=2100000000, val_src="web_verified", val_cite=MV_2026,
    asof="2026-05", country="GB", country_src="web_verified", country_cite=W("Multiverse (company)"), city="London",
    city_src="web_verified", focus="SaaS", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=MV_B, entry_date="2020-11", extra={"valuation_range_source": "web_verified"},
    rounds=[rnd("2019", "Series A", 16000000, "Index Ventures and Lightspeed", False, MV_B, "press"),
            rnd("2021-01-19", "Series B", 44000000, "General Catalyst", True, MV_B, "press"),
            rnd("2026-05-15", "Unnamed (primary)", 70000000, "Schroders Capital", None, MV_2026, "press")],
    note="Apprenticeship and AI upskilling platform ('Based in London', Wikipedia). GV joined the $44M Series B 'led by "
         "General Catalyst, with participation from Google Ventures' (Tech.eu, 2021-01-19); Index and Lightspeed had led the "
         "$16M Series A in 2019 without GV. GV's /ai list dates its first investment 2020-11. Mark: $70M primary round at a "
         "$2.1B valuation led by Schroders Capital (Pulse 2.0, 2026-05-15), aligned with sibling General Catalyst; siblings "
         "Lightspeed and Y Combinator still read below $1B."))

# ---------------------------------------------------------------- mylaurel
MYLAUREL = NEWS("mylaurel", "myLaurel Secures $12 Million")
L.append(cls("mylaurel", status="private", rng="below_1b", country="US", city="New York", city_src="web_verified",
    focus="Healthcare & Bio", stage="undetermined",
    rounds=[rnd("2025-06-03", "Unnamed", 12000000, "Deerfield Management and GV", True, MYLAUREL, "company")],
    note="Acute and transitional care at home ('Headquartered in New York'). The $12M initial closing of June 2025 came 'from "
         "existing investors' and 'is led by Deerfield Management and GV' (the company's release), and SteelSky Ventures "
         "led a further round in November 2025 joining 'previous investors Deerfield Management and Google Ventures'. GV "
         "was already an investor by June 2025 (the firm lists it from 2023), but no source read names its first round: "
         "undetermined."))

# ---------------------------------------------------------------- n3twork
N3_END = NEWS("n3twork", "secretive blockchain")
L.append(cls("n3twork", status="acquired", rng="below_1b", country="US", city="San Francisco",
    focus="Media, Gaming & Advertising", stage="Series A", stage_src="model", stage_conf="medium", stage_cite=N3_A,
    entry_date="2013-06",
    rounds=[rnd("2013-06-05", "Unnamed first round", 12000000, None, True, N3_A, "press")],
    note="Neil Young's content app turned mobile and blockchain games company. Its first round, $12M in June 2013, had "
         "'Kleiner Perkins ... Google Ventures and Mike Maples' Floodgate' (TechCrunch); unnamed there, it sits above the "
         "era's seed ceiling in the Series A band, so Series A at medium confidence. Forte bought it in January 2022 "
         "('N3twork, a blockchain company bought by Forte in 2022', Game Developer, " + N3_END + "; Business Wire's "
         "headline says Forte acquired N3TWORK's platform); a separate N3TWORK Studios later raised its own Series A."))

# ---------------------------------------------------------------- namo-media
L.append(cls("namo-media", status="acquired", rng="below_1b", city="San Francisco",
    focus="Media, Gaming & Advertising", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=NAMO_SEED, entry_date="2013-03",
    rounds=[rnd("2013-03-18", "Seed", 1900000, "Google Ventures", True, NAMO_SEED, "press")],
    note="Native mobile advertising (founded by ex-Googlers). A '$1.9 million seed round ... with Google Ventures leading' "
         "(TechCrunch, 2013-03-18). Twitter acquired it in June 2014 (Wikipedia, " + W("Namo Media") + "). Aligned with "
         "sibling a16z. " + LEAVE))

# ---------------------------------------------------------------- nanit
L.append(cls("nanit", status="private", rng="below_1b", city="New York", city_src="formd_address",
    focus="Consumer & Marketplaces", stage="Growth", stage_src="first_party", stage_conf="high",
    stage_cite=POST("nanit"), entry_date="2021-02", flags=["stage_disputes_band"],
    rounds=[rnd("2021-02-22", "Series C", 25000000, "GV", True, NANIT_TC, "press")],
    note="Smart baby monitor (UdiSense Inc., New York, Form D address 244 5th Ave). The firm's own post: 'I'm especially "
         "excited to lead Nanit's Series C announced today' (2021-02-22); TechCrunch: 'Series C round led by GV', bringing "
         "the total to $75M. A Series C entry is Growth, disputing the prefilled Series A band read off the 2021 filing."))

# ---------------------------------------------------------------- nava-benefits
NAVA_B = NEWS("nava-benefits", "Nava Benefits Raises $40 Million")
L.append(cls("nava-benefits", status="private", rng="below_1b", country="US", city="New York",
    city_src="web_verified", focus="Healthcare & Bio", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=NAVA_B, entry_date="2022-06",
    rounds=[rnd("2022-06-08", "Series B", 40000000, "Thrive Capital", True, NAVA_B, "company")],
    note="Employee benefits brokerage for small and mid-sized businesses (New York). '$40 million Series B funding round led "
         "by Thrive Capital ... New investors GV, K5 Ventures, and Homebrew also participated' (the company's release, "
         "2022-06-08), so GV entered at the Series B, Growth. A $30M round followed in October 2025 (FinTech Global "
         "headline). Aligned with sibling Thrive."))

# ---------------------------------------------------------------- nava-therapeutics
NAVA_TX = NEWS("nava-therapeutics", "Comes Out of Stealth")
L.append(cls("nava-therapeutics", status="private", rng="below_1b", country="US", city="Cambridge",
    city_src="web_verified", focus="Healthcare & Bio", stage="undetermined",
    rounds=[rnd(None, "Seed", 10000000, None, None, NAVA_TX, "press"),
            rnd("2024", "Series A", 79000000, None, None, NAVA_TX, "press")],
    note="Lipid nanoparticle delivery (Cambridge, MA team for discovery and manufacturing, a smaller Philadelphia team). It "
         "emerged in July 2026 with $89M: 'a $10 million seed round' and 'a previously undisclosed $79 million Series A in "
         "2024', from 'investors including GV, Andreessen Horowitz, Versant Ventures, F-Prime Capital, Readout Capital, and "
         "Alexandria' (BioBuzz). Which round GV joined is not stated, so undetermined (the Endpoints account is "
         "paywalled)."))

jl.write("j8", L)
