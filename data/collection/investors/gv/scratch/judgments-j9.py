"""PRO-75 grind, judge j9: queue batch 9 (44 member rows, nChroma Bio to PACT Pharma).
Pattern copied from judgments-pilot.py. Every citation below was printed by a tool run in this session (nq.py through
NEWS(), wikifetch.py through W(), the firm's own CMS helpers, EDGAR full-text hits, TechCrunch's own search, a company
page fetched with curl, stockanalysis.com) and read before use. Rows with no source tying GV to a named round read
`undetermined` and keep the rounds that were found. Checks dated 2026-09-28."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, verdict, rnd, POST, SITE, ARCH, W, NEWS, FTS, CASE = (jl.cls, jl.verdict, jl.rnd, jl.POST, jl.SITE, jl.ARCH,
                                                            jl.W, jl.NEWS, jl.FTS, jl.CASE)
L = []
CHECK = "2026-09-28"
WV = {"valuation_range_source": "web_verified"}
# an acquired row that still carries the float layer's source keys: the float no longer describes the company
NO_FLOAT = {"valuation_source": None, "valuation_range_source": None, "valuation_asof": None,
            "valuation_confidence": None}
AI = jl.AI_LISTING


def mcap(t):
    return f"https://stockanalysis.com/stocks/{t}/market-cap/"


# ---------------------------------------------------------------- nChroma Bio (Chroma Medicine + Nvelop)
CHROMA_B = NEWS("nchroma-bio", "Chroma Medicine Secures $135M")
CHROMA_LAUNCH = NEWS("nchroma-bio", "A startup emerges with $125M")
NCHROMA_MERGE = NEWS("nchroma-bio", "Chroma, Nvelop merge")
L.append(cls("nchroma-bio", status="private", rng="below_1b", country="US", city="Boston", city_src="web_verified",
             focus="Healthcare & Bio", stage="Growth", stage_src="web_verified", stage_conf="medium",
             stage_cite=CHROMA_B, entry_date="2023-03-01",
             note="Epigenetic editing, formed in December 2024 when Chroma Medicine and Nvelop Therapeutics merged into "
                  "nChroma Bio with a $75M financing from 19 firms led by Cormorant, Arch, Atlas and Newpath; BioPharma "
                  "Dive names GV among the investors the two companies already had in common. The company's own site "
                  "gives 201 Brookline Avenue, Boston. Entry read through the predecessor: GV led Chroma Medicine's "
                  "$135M Series B (the company's release of 2023-03-01, Cambridge MA dateline), and its list of existing "
                  "investors does not include GV, so the Series B was the firm's first money in the business; Chroma "
                  "had launched in November 2021 with $125M seeded by Atlas and Newpath. The base also carries "
                  "chroma-medicine (batch 15) and nvelop-therapeutics (batch 17), the two predecessors of this company. "
                  "No priced valuation disclosed.",
             rounds=[rnd("2021-11-17", "Launch financing (Chroma Medicine)", 125000000, "Atlas Venture and Newpath "
                         "Partners", None, CHROMA_LAUNCH, "press"),
                     rnd("2023-03-01", "Series B (Chroma Medicine)", 135000000, "GV", True, CHROMA_B, "company"),
                     rnd("2024-12-11", "Merger financing (nChroma Bio)", 75000000, "Cormorant, Arch, Atlas and Newpath",
                         True, NCHROMA_MERGE, "press")]))

# ---------------------------------------------------------------- Nebex
NEBEX = NEWS("nebex", "Nebex Raises $30M to Connect")
L.append(cls("nebex", status="private", rng="below_1b", country="US", city="New York", city_src="web_verified",
             focus="Fintech & Payments", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=NEBEX,
             entry_date="2026-06-29", grad="censored", extra={**WV, "valuation_citation": NEBEX},
             note="Exchange and market infrastructure for the space economy, covered as a New York startup (AlleyWatch; "
                  "the Business Journals' New York deals list). GV and Eniac Ventures led the $30M seed (AlleyWatch, "
                  "2026-07-02); the firm's own post of 2026-06-29 says GV is leading the seed. Entry inside the 24-month "
                  "window, so censored. Momentum slice check 2026-09-28: Google News shows only the $30M seed and a "
                  "EUR 100M French initiative (not a financing); no priced round at or near $1B.",
             rounds=[rnd("2026-06-29", "Seed", 30000000, "GV and Eniac Ventures", True, NEBEX, "press")]))

# ---------------------------------------------------------------- Nectar Social
NECTAR_SEED = NEWS("nectar-social", "Nectar Social Raises $10.6M")
NECTAR_A = NEWS("nectar-social", "raises $30M Series A led by Menlo")
L.append(cls("nectar-social", status="private", rng="below_1b", country="US", city="Seattle", city_src="web_verified",
             focus="AI & Applied AI", stage="Seed", stage_src="web_verified", stage_conf="medium",
             stage_cite=NECTAR_SEED, entry_date="2025-06-05",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NECTAR_A,
             extra={**WV, "valuation_citation": NECTAR_A},
             note="Agentic social-commerce and marketing platform (renamed Nectar Agent in June 2026). The company's "
                  "release (Seattle dateline, 2025-06-05): True Ventures and GV co-led a combined pre-seed and seed of "
                  "$10.6M; the firm's own /ai list dates its investment January 2025. Seed with medium confidence "
                  "because the round was billed as pre-seed and seed together. Menlo Ventures led the $30M Series A in "
                  "May 2026 with GV and True following (TechCrunch), so the row graduated; aligned with the Menlo row "
                  "on Seattle and the band. Momentum slice check 2026-09-28: the Series A is the latest priced round, "
                  "no valuation disclosed, nothing at or near $1B.",
             rounds=[rnd("2025-06-05", "Pre-seed and seed (combined)", 10600000, "True Ventures and GV", True,
                         NECTAR_SEED, "company"),
                     rnd("2026-05-16", "Series A", 30000000, "Menlo Ventures", True, NECTAR_A, "press")]))

# ---------------------------------------------------------------- Neo.Tax
NEOTAX_A = NEWS("neo-tax", "The 50 hottest FinTech funding rounds last week")
L.append(cls("neo-tax", status="private", rng="below_1b", country="US", city="Mountain View",
             focus="Fintech & Payments", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=NEOTAX_A, entry_date="2022-02", extra={**WV, "valuation_citation": NEOTAX_A},
             note="AI automation of the R&D tax credit; still operating (its site, and a 2025 Thomson Reuters "
                  "ONESOURCE partnership, not an acquisition). FinTech Global (2022-02-11): Infinity Ventures led the "
                  "$10M Series A with Google Ventures, Acrew and Fin VC as new investors beside returning Uncork, "
                  "Floodgate, Liquid 2 and Lux; the firm's own /ai list dates the investment November 2021. City "
                  "aligned with the Lux row (Mountain View). Momentum slice check 2026-09-28: Google News shows no "
                  "later round and no priced mark at or near $1B.",
             rounds=[rnd("2022-02", "Series A", 10000000, "Infinity Ventures", True, NEOTAX_A, "press")]))

# ---------------------------------------------------------------- Neo4j
NEO4J_F = NEWS("neo4j", "Neo4j Announces $325 Million Series F")
NEO4J_2B = NEWS("neo4j", "Swedish company accelerates toward IPO")
NEO4J_TC = NEWS("neo4j", "Database startup Neo4j embraces AI")
L.append(cls("neo4j", status="private", rng="1b_plus", usd=2000000000, val_src="web_verified", val_cite=NEO4J_2B,
             asof="2024-11-28", val_conf="high", country="US", city="San Mateo", city_src="web_verified",
             focus="Data Infrastructure", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=NEO4J_F, entry_date="2021-06-17", extra=WV,
             note="Graph database (San Mateo dateline; founded in Malmo). The company's release of 2021-06-17: Eurazeo "
                  "led the $325M Series F with participation from GV, at a valuation over $2B, and the firm's own post "
                  "that day welcomes Neo4j to the portfolio, so the Series F was the entry. Mark: in November 2024 "
                  "Noteus Partners invested $50M, which the company said reaffirms its $2B valuation (ArcticStartup, "
                  "2024-11-28; TechCrunch that week wrote $2.2B). Same $2B figure as the Creandum row, dated fresher, "
                  "so not stale. Momentum slice check 2026-09-28: no later priced round found.",
             rounds=[rnd("2021-06-17", "Series F", 325000000, "Eurazeo", True, NEO4J_F, "company"),
                     rnd("2024-11-19", "Growth investment (unnamed)", 50000000, "Noteus Partners", None, NEO4J_TC,
                         "press")]))

# ---------------------------------------------------------------- Nest
NEST_W = W("Google Nest")
NEST_2013 = NEWS("nest", "Hits $800 Million Valuation")
L.append(cls("nest", status="acquired", rng="below_1b", country="US", country_src="web_verified", country_cite=NEST_W,
             city="Palo Alto", focus="Consumer & Marketplaces", stage="undetermined",
             flags=["model_disputes_source"],
             note="Nest Labs, the learning thermostat (Palo Alto). Country disputes the prefilled DE, a Wikidata join on "
                  "the one-word name: Wikipedia places the company's own headquarters in Palo Alto. Google agreed to "
                  "buy Nest for $3.2B in cash in January 2014 (Wikipedia; the firm's own exit line 'Acquired by Google, "
                  "2014'). The firm's archived listing carries Nest from the 2012 capture (Bill Maris and David Krane "
                  "named in 2014-2015). No source read names the round GV entered: Wikipedia names Shasta and Kleiner "
                  "as early investors, and the January 2013 round (reported at an $800M valuation) is known only from a "
                  "headline; stage undetermined.",
             rounds=[rnd("2013-01-30", "Unnamed round ($800M valuation reported)", None, None, None, NEST_2013,
                         "press")]))

# ---------------------------------------------------------------- Neuralink
NEURA_C = NEWS("neuralink", "raises $205 million Series C funding that includes")
NEURA_E = NEWS("neuralink", "Braintech Funding Booms As Musk")
L.append(cls("neuralink", rng="1b_plus", usd=9000000000, val_src="web_verified", val_cite=NEURA_E, asof="2025-06-02",
             val_conf="high", city="Fremont", city_src="web_verified", focus="Healthcare & Bio",
             stage="undetermined", entry_date="2019-05", clear=["unicorn_name_match"], extra=WV,
             note="Brain-computer interfaces, Fremont (Crunchbase News; Wikipedia gives Fremont as headquarters since "
                  "2022). Mark re-pinned from the unicorn list to the round itself: the $650M Series E announced "
                  "2025-06-02 reportedly valued Neuralink at $9B (Crunchbase News), the same mark as the Thrive, "
                  "Lightspeed rows. Secondary-market talk of $42B (July 2026) is a secondary estimate, not a mark. "
                  "Entry: the firm's own /ai list says Invested May 2019 and Re-invested July 2021; the July 2021 round "
                  "is the $205M Series C led by Vy Capital with GV participating (9to5Google). No source names the 2019 "
                  "round GV entered, so the stage is undetermined; the entry date is the firm's own month (decisions "
                  "D7).",
             rounds=[rnd("2019-05", "Unnamed (the firm's first investment)", None, None, True, AI, "firm"),
                     rnd("2021-07-29", "Series C", 205000000, "Vy Capital", True, NEURA_C, "press"),
                     rnd("2025-06-02", "Series E", 650000000, None, None, NEURA_E, "press")]))

# ---------------------------------------------------------------- Nextbit
L.append(cls("nextbit", status="acquired", rng="below_1b", city="San Francisco", focus="Consumer & Marketplaces",
             note="Nextbit, maker of the Robin smartphone (San Francisco). Acquired by Razer in 2017 (the firm's own exit "
                  "line 'Acquired by Razer, 2017'; the Accel row reads the same). Entry stays the Form D band's Series "
                  "A of December 2013, which the Accel row also records as the Series A."))

# ---------------------------------------------------------------- Nextdoor
NEXTDOOR_W = W("Nextdoor")
L.append(cls("nextdoor", rng="below_1b", usd=936170000, val_src="web_verified", val_cite=mcap("nxdr"), asof=CHECK,
             val_conf="high", city="San Francisco", focus="Consumer & Marketplaces", stage="undetermined", extra=WV,
             note="Nextdoor Holdings (NYSE: NXDR), San Francisco. Market cap $936.17M as of 2026-09-28 "
                  "(stockanalysis.com), which replaces the SEC float as the canonical public mark and matches the "
                  "Coatue, Insight and IVP rows' $0.97B of 2026-09-25 in band. The firm's archived listing carries "
                  "Nextdoor from the 2013 capture (Kevin Rose named in 2014, David Krane since). Wikipedia records an "
                  "$18.6M raise in July 2012, a $75M round at $1.5B in December 2017 and $123M at $2.1B in May 2019, "
                  "but no source read ties GV to a round, so the stage is undetermined.",
             rounds=[rnd("2012-07", "Unnamed", 18600000, None, None, NEXTDOOR_W, "press"),
                     rnd("2017-12", "Unnamed ($1.5B valuation)", 75000000, None, None, NEXTDOOR_W, "press"),
                     rnd("2019-05", "Unnamed ($2.1B valuation)", 123000000, None, None, NEXTDOOR_W, "press")]))

# ---------------------------------------------------------------- Ngmoco
NGMOCO_W = W("Ngmoco")
NGMOCO_C = NEWS("ngmoco", "Completes $25M Funding Round")
L.append(cls("ngmoco", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="Media, Gaming & Advertising", stage="undetermined",
             note="ngmoco, iPhone games publisher (San Francisco). DeNA announced its acquisition for $400M in October "
                  "2010 (Wikipedia; the firm's own exit line 'Acquired by DeNA, 2010'). Kleiner Perkins' iFund and "
                  "Norwest financed the first two rounds (Wikipedia); the Series C that closed at the end of 2009 was "
                  "led by Institutional Venture Partners with Kleiner, Norwest and Maples (Game Developer) and names no "
                  "Google Ventures. No source read ties GV to a round; stage undetermined, as on the IVP row.",
             rounds=[rnd("2009-12", "Series C", 25000000, "Institutional Venture Partners", False, NGMOCO_C, "press")]))

# ---------------------------------------------------------------- Nimble
NIMBLE_SEED = "https://techcrunch.com/2012/01/23/nimble-goes-after-salesforce/"
NIMBLE_SEED_NEWS = ("https://techcrunch.com/2012/01/04/google-ventures-mark-cuban-and-others-invest-1m-in-social-crm-"
                    "startup-nimble/")
NIMBLE_A = "https://techcrunch.com/2017/03/02/nimble-lands-9-million-series-a-to-simplify-contact-management-in-the-cloud/"
L.append(cls("nimble", status="private", rng="below_1b", country="US", city="Santa Monica", focus="SaaS",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=NIMBLE_SEED, entry_date="2012-01",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NIMBLE_A,
             note="Nimble, the social CRM founded by Jon Ferrara (Santa Monica); still operating (2025 product "
                  "releases). TechCrunch (2012-01-04) reported $1M from Mark Cuban, Google Ventures and others, and "
                  "TechCrunch (2012-01-23) calls it 'a $1 million seed round from Mark Cuban, Google Ventures, and "
                  "others'. Imagen Capital Partners led a $9M Series A in March 2017 (TechCrunch), so the row "
                  "graduated. The sibling rows named Nimble (Felicis and First Round, a healthcare company; Y "
                  "Combinator, a Miami consumer company) are different companies and are not aligned.",
             rounds=[rnd("2012-01-04", "Seed", 1000000, None, True, NIMBLE_SEED_NEWS, "press"),
                     rnd("2017-03-02", "Series A", 9000000, "Imagen Capital Partners", None, NIMBLE_A, "press")]))

# ---------------------------------------------------------------- Nimbus Therapeutics
NIMBUS = NEWS("nimbus-therapeutics", "Fresh off $4B deal")
L.append(cls("nimbus-therapeutics", status="private", rng="below_1b", country="US", city="Boston",
             focus="Healthcare & Bio", stage="Growth", stage_src="model", stage_conf="medium", stage_cite=NIMBUS,
             entry_date="2023-09-06",
             note="Structure-based drug discovery, Boston; sold its TYK2 program to Takeda for $4B upfront. BioPharma "
                  "Dive (2023-09-06): the $210M financing was led by new investor GV, with existing backers including "
                  "Atlas Venture and SR One. The round is unnamed, but it is GV's first money in a company founded in "
                  "2009 with years of venture backing, so it reads Growth (model, medium). No valuation disclosed; the "
                  "Takeda payment was an asset sale, not a company mark. Operating: a 2026 Eli Lilly obesity pact "
                  "(Boston Business Journal).",
             rounds=[rnd("2023-09-06", "Unnamed", 210000000, "GV", True, NIMBUS, "press")]))

# ---------------------------------------------------------------- NoRedInk
NRI_A = ("https://techcrunch.com/2013/08/26/with-funding-from-top-flight-investors-fast-growing-noredink-is-on-a-"
         "mission-to-rid-the-world-of-bad-grammar/")
NRI_B = "https://techcrunch.com/2021/08/24/noredink-raises-50-million-series-b-to-help-students-become-better-writers/"
L.append(cls("noredink", status="private", rng="below_1b", country="US", city="San Francisco",
             city_src="web_verified", focus="SaaS", stage="Series A", stage_src="web_verified", stage_conf="medium",
             stage_cite=NRI_A, entry_date="2013",
             note="Writing curriculum platform sold to schools, San Francisco (TechCrunch 2021). TechCrunch "
                  "(2013-08-26) reports NoRedInk 'closing a $2 million round of series A financing' from Google "
                  "Ventures, Social+Capital, Learn Capital, Kapor, NewSchools and CRV; Wikipedia dates the same $2M to "
                  "January 2013, so the entry date is the year. Medium confidence: TechCrunch's 2021 Series B story "
                  "($50M, Susquehanna Growth Equity) places the Series A 'nearly six years' earlier, so the company may "
                  "have renumbered a later round as its A.",
             rounds=[rnd("2013", "Series A", 2000000, None, True, NRI_A, "press"),
                     rnd("2021-08-24", "Series B", 50000000, "Susquehanna Growth Equity", None, NRI_B, "press")]))

# ---------------------------------------------------------------- Nothing
NOTHING_A = NEWS("nothing", "London-based Nothing secures £10.8M")
NOTHING_C = NEWS("nothing", "Nothing closes $200M Series C led by Tiger Global")
L.append(cls("nothing", status="private", rng="1b_plus", usd=1300000000, val_src="web_verified", val_cite=NOTHING_C,
             asof="2025-09-15", val_conf="high", country="GB", country_src="web_verified", country_cite=NOTHING_A,
             city="London", focus="Consumer & Marketplaces", stage="Series A", stage_src="web_verified",
             stage_conf="high", stage_cite=NOTHING_A, entry_date="2021-02", flags=["model_disputes_source"], extra=WV,
             note="Consumer electronics (phones, audio), London. Country disputes the prefilled FR, a Wikidata join on "
                  "the one-word name: UKTN calls it London-based Nothing. GV led the $15M Series A in February 2021 "
                  "(UKTN), after a $7M seed from angels in December 2020; the firm's own case study gives 'First "
                  "Round: Series A'. Tiger Global led the $200M Series C in September 2025 at a $1.3B valuation with GV "
                  "among existing backers (TechCrunch), the same mark as the EQT Ventures row.",
             rounds=[rnd("2020-12", "Seed", 7000000, None, False, NOTHING_A, "press"),
                     rnd("2021-02-09", "Series A", 15000000, "GV", True, NOTHING_A, "press"),
                     rnd("2025-09-15", "Series C", 200000000, "Tiger Global", True, NOTHING_C, "press")]))

# ---------------------------------------------------------------- nPlan
NPLAN_GV = NEWS("nplan", "GV leads $18.5m round for nPlan")
NPLAN_B = NEWS("nplan", "nPlan secures £11.9 million Series B")
L.append(cls("nplan", status="private", rng="below_1b", country="GB", country_src="web_verified",
             country_cite=NPLAN_B, city="London", focus="AI & Applied AI", stage="Series A", stage_src="model",
             stage_conf="medium", stage_cite=NPLAN_GV, entry_date="2021-03-23",
             note="AI forecasting of construction project schedules; London (UK Tech News; the company's site gives "
                  "Second Home Spitalfields). GV led an $18.5M round announced 2021-03-23 (Venture Capital Journal; the "
                  "firm's own /ai list dates the investment November 2020). The round is not named in what could be "
                  "read, but the company's next round, in October 2025, is its Series B ($16M, led by CapHorn, Chevron "
                  "Technology Ventures and Suffolk Technologies, with GV continuing), so the GV-led round reads as the "
                  "Series A (model, medium). No valuation disclosed.",
             rounds=[rnd("2021-03-23", "Unnamed (the Series A by sequence)", 18500000, "GV", True, NPLAN_GV, "press"),
                     rnd("2025-10-17", "Series B", 16000000, "CapHorn, Chevron Technology Ventures and Suffolk "
                         "Technologies", True, NPLAN_B, "press")]))

# ---------------------------------------------------------------- Nym Health
NYM_A = NEWS("nym-health", "Nym Health raises $16.5 million round A")
NYM_B = NEWS("nym-health", "Medtech startup Nym Health raises $25 million")
L.append(cls("nym-health", status="private", rng="below_1b", country="US", city="New York", focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=NYM_A, entry_date="2020-10-14",
             note="Autonomous medical coding for hospitals; R&D in Tel Aviv and US operations, New York as on the "
                  "Lightspeed row (Globes in 2020 called it Tel Aviv-based). Calcalist (2020-10-14): GV led the $16.5M "
                  "Series A, after a $6M seed in June 2019 (Lightspeed's entry); Addition led the $25M Series B in July "
                  "2021 with GV among existing investors.",
             rounds=[rnd("2019-06", "Seed", 6000000, None, None, NYM_A, "press"),
                     rnd("2020-10-14", "Series A", 16500000, "GV", True, NYM_A, "press"),
                     rnd("2021-07-27", "Series B", 25000000, "Addition", True, NYM_B, "press")]))

# ---------------------------------------------------------------- Oasis Health Partners
OASIS = NEWS("oasis-health-partners", "Seasoned Healthcare Executives Launch Oasis")
L.append(cls("oasis-health-partners", status="private", rng="below_1b", country="US", city="Myrtle Beach",
             city_src="web_verified", focus="Healthcare & Bio", stage="undetermined", entry_date="2023-01-09",
             note="Value-based primary care company, Myrtle Beach SC (the launch release's dateline). The release of "
                  "2023-01-09 says it is backed by Triple Aim Partners and GV but gives no amount or round name, and no "
                  "later financing was found; stage undetermined, the entry dated by the launch release. Operating: "
                  "it bought Premier Health in March 2026 and added PreferCare in 2025.",
             rounds=[rnd("2023-01-09", "Launch financing (amount and round not disclosed)", None, None, True, OASIS,
                         "company")]))

# ---------------------------------------------------------------- Oblenio Bio
OBLENIO_B = NEWS("oblenio-bio", "Oblenio Bio Raises $62M to Advance New Therapies")
OBLENIO_A = NEWS("oblenio-bio", "VC Aditum Bio hatches")
L.append(cls("oblenio-bio", status="private", rng="below_1b", country="US", city="Cambridge", city_src="web_verified",
             focus="Healthcare & Bio", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=OBLENIO_B, entry_date="2026-06-25",
             note="Tri-specific T-cell engager for autoimmune disease, Cambridge MA. Pfizer Ventures led the $62M Series "
                  "B (citybiz, 2026-06-25) with Deep Track Capital and GV as new investors and Aditum Bio, the Series A "
                  "investor that launched the company in November 2024 (Fierce Biotech). GV's entry is the Series B.",
             rounds=[rnd("2024-11-07", "Series A (launch)", None, "Aditum Bio", False, OBLENIO_A, "press"),
                     rnd("2026-06-25", "Series B", 62000000, "Pfizer Ventures", True, OBLENIO_B, "press")]))

# ---------------------------------------------------------------- Obsidian Security
OBS_2019 = NEWS("obsidian-security", "Status Update: Former CEO of Taco Bell")
OBS_D = NEWS("obsidian-security", "Raises $85 Million Series D at $1.1 Billion")
L.append(cls("obsidian-security", status="private", rng="1b_plus", usd=1100000000, val_src="web_verified",
             val_cite=OBS_D, asof="2026-08-04", val_conf="high", country="US", city="Newport Beach",
             city_src="web_verified", focus="Security", stage="Growth", stage_src="web_verified", stage_conf="medium",
             stage_cite=OBS_2019, entry_date="2019-03", extra=WV,
             note="SaaS and AI-agent security, Newport Beach. Orange County Register (2019-03-04): Wing Venture Capital "
                  "led a $20M round with participation from GV and 'Series A investor Greylock', so GV entered at the "
                  "round after the Series A (Growth; medium because the round is not named in the text). Crescent "
                  "Cove led the $85M Series D at a $1.1B post-money valuation in August 2026, with Greylock, Menlo, "
                  "Norwest, IVP, Wing and GV returning (Unite.AI). The Greylock, IVP and Menlo rows still read "
                  "below_1b; this row holds the fresher cited mark.",
             rounds=[rnd("2019-03-04", "Unnamed (after the Series A)", 20000000, "Wing Venture Capital", True,
                         OBS_2019, "press"),
                     rnd("2022-04", "Series C", 90000000, "Menlo Ventures, Norwest Venture Partners and IVP", None,
                         OBS_D, "press"),
                     rnd("2026-08-04", "Series D", 85000000, "Crescent Cove Advisors", True, OBS_D, "press")]))

# ---------------------------------------------------------------- Obsidian Therapeutics
OBX_2017 = NEWS("obsidian-therapeutics", "These Fifty Synthetic Biology Companies")
OBX_B = NEWS("obsidian-therapeutics", "Obsidian bags $115M")
OBX_C = NEWS("obsidian-therapeutics", "Obsidian Therapeutics lands $160M Series C")
OBX_MERGE = NEWS("obsidian-therapeutics", "Completes Galera Merger and $350 Million Financing")
L.append(cls("obsidian-therapeutics", status="public", rng="below_1b", usd=825900000, val_src="web_verified",
             val_cite=mcap("obx"), asof=CHECK, val_conf="high", country="US", city="Cambridge",
             city_src="web_verified", focus="Healthcare & Bio", stage="undetermined", extra=WV,
             note="Engineered TIL cell therapy, Cambridge MA (its S-1 of 2026-08-28 gives 1030 Massachusetts Avenue). "
                  "Public since the reverse merger with Galera Therapeutics closed on 2026-08-03 with a $350M private "
                  "placement; Nasdaq: OBX from 2026-08-04 (citybiz). Market cap $825.9M as of 2026-09-28 "
                  "(stockanalysis.com). The firm's archived listing carries it from the 2018 capture, but no source "
                  "read names the round GV entered: the 2017 venture round is only named in a SynBioBeta list, the $115M "
                  "Series B of 2021 was led by TCG Crossover with new investors, and the S-1 lists no GV holding among "
                  "5% holders; stage undetermined.",
             rounds=[rnd("2017", "Unnamed venture round", None, None, None, OBX_2017, "press"),
                     rnd("2021-09-09", "Series B", 115000000, "TCG Crossover", None, OBX_B, "press"),
                     rnd("2024-04-03", "Series C", 160000000, None, None, OBX_C, "press"),
                     rnd("2026-08-03", "Private placement at the Galera reverse merger", 350000000, None, None,
                         OBX_MERGE, "press")]))

# ---------------------------------------------------------------- Odyssey
ODY_SEED = NEWS("odyssey", "Can these two self-driving car vets")
ODY_B_AIRSTREET = NEWS("odyssey", "Odyssey raises $310M Series B for world models")
ODY_B = NEWS("odyssey", "World Models Startup Odyssey Raises $310M in Series B Funding, Valued")
L.append(cls("odyssey", rng="1b_plus", usd=1450000000, val_src="web_verified", val_cite=ODY_B, asof="2026-06-18",
             val_conf="high", country="US", country_src="web_verified", country_cite=ODY_SEED, city="Palo Alto",
             focus="AI & Applied AI", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=ODY_SEED,
             entry_date="2024-07-08", grad="graduated", grad_src="web_verified", grad_conf="high",
             grad_cite=ODY_B_AIRSTREET, flags=["model_disputes_source"], clear=["unicorn_name_match"], extra=WV,
             note="Odyssey (odyssey.systems), generative world models founded by Oliver Cameron and Jeff Hawke. Country "
                  "disputes the prefilled GB, a Wikidata join on the one-word name: Fortune (2024) calls it a San "
                  "Francisco-based startup; city aligned with the EQT Ventures and Point Nine rows (Palo Alto). It "
                  "emerged in July 2024 with $9M in seed funding from GV, with DCVC and Air Street participating "
                  "(Fortune, 2024-07-08). Natural Capital led the $310M Series B at a $1.45B valuation in June 2026 "
                  "with GV participating (AI Insider; Air Street), so the row graduated and the unicorn-list mark is "
                  "re-pinned to the round. The a16z, General Catalyst and USV rows named Odyssey are different "
                  "companies and are not aligned.",
             rounds=[rnd("2024-07-08", "Seed", 9000000, "GV", True, ODY_SEED, "press"),
                     rnd("2026-06-17", "Series B", 310000000, "Natural Capital", True, ODY_B, "press")]))

# ---------------------------------------------------------------- OMass Therapeutics
OMASS_B = ("https://www.omass.com/2022/04/28/omass-therapeutics-raises-100-million-in-series-b-financing-to-progress-"
           "drug-pipeline-in-immunology-and-rare-diseases/")
OMASS_NEWS = "https://www.omass.com/news"
L.append(cls("omass-therapeutics", status="private", rng="below_1b", country="GB", country_src="web_verified",
             country_cite=OMASS_B, city="Oxford", focus="Healthcare & Bio", stage="Growth", stage_src="web_verified",
             stage_conf="high", stage_cite=OMASS_B, entry_date="2022-04-28",
             note="Small-molecule drug discovery using native mass spectrometry, Oxford. The company's release "
                  "(Oxford, 2022-04-28): its $100M (GBP 75.5M) Series B was led by new investors GV, Northpond "
                  "Ventures and Sanofi Ventures, with Syncona, Oxford Science Enterprises and Oxford University "
                  "following, so GV entered at the Series B. Earlier: a GBP 14M Series A (November 2018) and a GBP "
                  "27.5M extended Series A (February 2020); a Series B extension in May 2023 (the company's news page). "
                  "No valuation disclosed; a Genentech collaboration in 2025.",
             rounds=[rnd("2018-11-20", "Series A (GBP 14M)", None, None, None, OMASS_NEWS, "company"),
                     rnd("2020-02-17", "Extended Series A (GBP 27.5M)", None, None, None, OMASS_NEWS, "company"),
                     rnd("2022-04-28", "Series B", 100000000, "GV, Northpond Ventures and Sanofi Ventures", True,
                         OMASS_B, "company"),
                     rnd("2023-05-15", "Series B extension", None, None, None, OMASS_NEWS, "company")]))

# ---------------------------------------------------------------- Omeat
OMEAT_TC = NEWS("omeat", "Omeat emerges from stealth with beefy")
OMEAT_AGF = NEWS("omeat", "Omeat emerges from stealth armed with $40m")
OMEAT_2026 = NEWS("omeat", "Omeat Becomes Evergreen")
L.append(cls("omeat", status="private", rng="below_1b", country="US", city="Los Angeles", city_src="web_verified",
             focus="Climate & Energy", stage="Series A", stage_src="web_verified", stage_conf="medium",
             stage_cite=OMEAT_TC, entry_date="2022",
             note="Cultivated beef grown with plasma-derived media, Los Angeles; renamed Evergreen in February 2026 "
                  "with a further $6M open round. It came out of stealth in June 2023: AgFunderNews reports a $3.5M "
                  "seed in 2021 and a $36.5M Series A in 2022, and TechCrunch says the '$40 million of Series A capital "
                  "in 2022' came from investors including Google Ventures. The firm's archived listing starts in 2023, "
                  "so the Series A is the entry the record supports (medium: AgFunder's investor list spans both "
                  "rounds). No valuation disclosed.",
             rounds=[rnd("2021", "Seed", 3500000, None, None, OMEAT_AGF, "press"),
                     rnd("2022", "Series A", 36500000, None, True, OMEAT_TC, "press"),
                     rnd("2026-02", "Open round after the rename to Evergreen", 6000000, None, None, OMEAT_2026,
                         "press")]))

# ---------------------------------------------------------------- Omni Analytics
OMNI_SEED_A = NEWS("omni-analytics", "RJMetrics alum Chris Merrick")
OMNI_B = NEWS("omni-analytics", "Omni raises $69M to design tools")
OMNI_C = NEWS("omni-analytics", "Omni raises $120M round for its AI analytics")
L.append(cls("omni-analytics", status="private", rng="1b_plus", usd=1500000000, val_src="web_verified",
             val_cite=OMNI_C, asof="2026-04-23", val_conf="high", country="US", city="San Francisco",
             city_src="web_verified", focus="Data Infrastructure", stage="Seed", stage_src="model",
             stage_conf="medium", stage_cite=OMNI_SEED_A, entry_date="2022-04",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=OMNI_SEED_A, extra=WV,
             note="Omni Analytics Inc. (exploreomni.com, now omni.co), business-intelligence platform, San Francisco. "
                  "The firm's /ai list carries the same company as 'Omni' (row omni): Invested April 2022, Re-invested "
                  "August 2022 and March 2025. Founded in early 2022, Omni closed exactly two rounds that year, a seed "
                  "led by First Round Capital and a Series A led by Redpoint (Technical.ly), announced together in "
                  "August 2022 at $26.9M; GV's April investment reads as the seed and its August one as the Series A "
                  "(model, medium: no page names GV in the seed). The named Series A graduates the row. ICONIQ led the "
                  "$69M Series B in March 2025 at $650M (TechCrunch) and the $120M Series C at a $1.5B valuation in "
                  "April 2026 with GV and Redpoint (SiliconANGLE). The First Round and Redpoint rows still read "
                  "below_1b; this row holds the fresher mark. Momentum slice check 2026-09-28: the Series C is the "
                  "latest priced round.",
             rounds=[rnd("2022", "Seed", None, "First Round Capital", None, OMNI_SEED_A, "press"),
                     rnd("2022", "Series A", None, "Redpoint Ventures", None, OMNI_SEED_A, "press"),
                     rnd("2025-03-13", "Series B", 69000000, "ICONIQ Growth", True, OMNI_B, "press"),
                     rnd("2026-04-23", "Series C", 120000000, "ICONIQ", True, OMNI_C, "press")]))

# ---------------------------------------------------------------- OnDeck
ONDECK_S1 = "https://www.sec.gov/Archives/edgar/data/1420811/000119312514405349/d772825ds1.htm"
L.append(cls("ondeck", rng="below_1b", country="US", city="New York", focus="Fintech & Payments",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=ONDECK_S1, entry_date="2013-04",
             clear=["stale"], extra=NO_FLOAT,
             note="On Deck Capital, small-business lending, New York (1400 Broadway, the S-1 cover). Its S-1 (2014-11-10) "
                  "says 'Google Ventures invested in our Series D Preferred Stock financing in April 2013' (Google "
                  "Ventures 2013, L.P. bought $13.0M of Series D beside IVP's $32.0M) and GV added $4.0M in the "
                  "Series E that Tiger Global led in February 2014. Listed on NYSE in December 2014 (the firm's exit "
                  "line 'NYSE: ONDK'); acquired by Enova in 2020, as on the IVP row, so the old float keys are cleared.",
             rounds=[rnd("2013-04", "Series D", None, None, True, ONDECK_S1, "filing"),
                     rnd("2014-02", "Series E", None, "Tiger Global", True, ONDECK_S1, "filing")]))

# ---------------------------------------------------------------- One Medical
ONEMED_FD13 = "https://www.sec.gov/Archives/edgar/data/1404123/000140412313000004/0001404123-13-000004-index.htm"
ONEMED_S1 = "https://www.sec.gov/Archives/edgar/data/1404123/000119312520001429/d806726ds1.htm"
ONEMED_Q1 = NEWS("one-medical", "Torrid Pace Continues for Healthcare IT Funding in Q1 2013")
ONEMED_CARLYLE = NEWS("one-medical", "One Medical gets up to $350M infusion")
L.append(cls("one-medical", status="acquired", rng="below_1b", city="San Francisco", focus="Healthcare & Bio",
             stage="Growth", stage_src="model", stage_conf="medium", stage_cite=ONEMED_FD13,
             flags=["stage_disputes_band"],
             note="One Medical (1Life Healthcare), primary care, San Francisco. IPO in January 2020 (NASDAQ: ONEM, the "
                  "firm's exit line); now owned by Amazon (Amazon One Medical in 2025 and 2026 coverage). Stage disputes the "
                  "Form D band's Series A: the "
                  "company was founded in 2007 and had filed Form Ds in 2009, 2010 and 2011 before the 2013 filing "
                  "($29,999,996) on which GV's Krishna Yeshwant first appears as a director; Mercom lists One Medical "
                  "among Q1 2013's $30M raises; and the S-1 capital table (" + ONEMED_S1 + ") shows Series A to E "
                  "before a Series F with a $30.0M liquidation preference, which matches that filing. GV 2013, L.P. "
                  "held 5.9% at the IPO. So GV entered at the Series F (Growth, model, medium).",
             rounds=[rnd("2013-03-06", "Series F (by the S-1 capital table)", 29999996, None, True, ONEMED_FD13,
                         "filing"),
                     rnd("2018-08-23", "Carlyle investment (up to $350M)", None, "The Carlyle Group", None,
                         ONEMED_CARLYLE, "press")]))

# ---------------------------------------------------------------- oneNav
ONENAV_B = NEWS("onenav", "oneNav Raises $21M For More Accurate")
ONENAV_FD23 = "https://www.sec.gov/Archives/edgar/data/1973867/000197386723000001/0001973867-23-000001-index.htm"
L.append(cls("onenav", status="private", rng="below_1b", city="Palo Alto", city_src="web_verified",
             focus="Industrial & Robotics", stage="undetermined", entry_date="2019-11",
             note="L5 GNSS receiver chips, Palo Alto (Crunchbase News); still shipping and field-testing in 2025 (GPS "
                  "World). GV led the $21M Series B in May 2021 (Crunchbase News: founded 2019, $33M raised in total). "
                  "The firm's own /ai list says Invested November 2019, Re-invested April 2021 and March 2023; the 2023 "
                  "investment is the $16.1M Form D with Karim Faris as a director, which had set the entry date the "
                  "row carried. The entry date is corrected to the firm's own November 2019 (decisions D7). No source "
                  "names the 2019 round; stage undetermined.",
             rounds=[rnd("2019-11", "Unnamed (the firm's first investment)", None, None, True, AI, "firm"),
                     rnd("2021-05-20", "Series B", 21000000, "GV", True, ONENAV_B, "press"),
                     rnd("2023-03-08", "Unnamed (Form D)", 16142870, None, True, ONENAV_FD23, "filing")]))

# ---------------------------------------------------------------- Openbay
OPENBAY_SEED = "https://techcrunch.com/2013/10/28/openbay/"
OPENBAY_A = NEWS("openbay", "Secures Series A Financing - PR Newswire")
OPENBAY_2023 = NEWS("openbay", "Openbay Deepens its Coverage with AAMCO")
L.append(cls("openbay", status="private", rng="below_1b", city="Cambridge", city_src="web_verified",
             focus="Consumer & Marketplaces", stage="Seed", stage_src="model", stage_conf="medium",
             stage_cite=OPENBAY_SEED, entry_date="2013-10-28",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=OPENBAY_A,
             note="Online marketplace for auto repair, Cambridge MA; operating in 2023 (AAMCO partnership). At launch "
                  "TechCrunch (2013-10-28) listed its investors as Google Ventures, a16z seed, Boston Seed Capital and "
                  "Stage 1 Ventures, quoting GV's Rich Miner; the launch financing is unnamed but precedes the $8M "
                  "Series A of June 2018 (the company's release), so it reads Seed (model, medium; the a16z row records "
                  "the same seed). The named Series A graduates the row.",
             rounds=[rnd("2013-10-28", "Launch financing (unnamed)", None, None, True, OPENBAY_SEED, "press"),
                     rnd("2018-06-25", "Series A", 8000000, None, None, OPENBAY_A, "company")]))

# ---------------------------------------------------------------- Opendoor
OPENDOOR_E = NEWS("opendoor", "Opendoor Announces $325 Million in Series E")
L.append(cls("opendoor", status="public", rng="1b_plus", usd=2360000000, val_src="web_verified", val_cite=mcap("open"),
             asof=CHECK, val_conf="high", city="Tempe", city_src="web_verified", focus="Consumer & Marketplaces",
             stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=OPENDOOR_E,
             entry_date="2016-11", extra=WV,
             note="Opendoor Technologies (NASDAQ: OPEN), home buying and selling; based in Tempe, Arizona "
                  "(stockanalysis.com profile). Market cap $2.36B as of 2026-09-28 (stockanalysis.com), fresher than "
                  "the sibling marks ($3.97B, $3.06B, $2.5B), same band. The company's Series E release (2018-06-18) "
                  "says the $210M Series D of November 2016 included Google Ventures, the earliest round naming the "
                  "firm, so GV entered at the Series D or before it at a later-stage round (Growth, medium).",
             rounds=[rnd("2016-11", "Series D", 210000000, None, True, OPENDOOR_E, "press"),
                     rnd("2018-06-18", "Series E", 325000000, "General Atlantic, Access Technology Ventures and Lennar",
                         None, OPENDOOR_E, "press")]))

# ---------------------------------------------------------------- OpenEvidence
OE_B = NEWS("openevidence", "Announces $210 Million Round at $3.5 Billion")
OE_D = NEWS("openevidence", "OpenEvidence hits $12B valuation")
OE_MIAMI = NEWS("openevidence", "recently moved to Miami")
OE_15 = NEWS("openevidence", "was valued at $15 billion in a new funding round")
L.append(cls("openevidence", rng="10b_plus", usd=12000000000, val_src="web_verified", val_cite=OE_D,
             asof="2026-01-21", val_conf="high", city="Miami", city_src="web_verified", focus="Healthcare & Bio",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=OE_B, entry_date="2025-07-15",
             clear=["unicorn_name_match"], extra=WV,
             note="AI medical search for clinicians. Founded in Cambridge MA, moved to Miami by October 2025 (Refresh "
                  "Miami, citing the Boston Globe, Florida records and the CEO), and called Miami-based in September "
                  "2026; the a16z, Menlo, Sequoia and Thrive rows still read Cambridge. The company's release of "
                  "2025-07-15: Google Ventures and Kleiner Perkins co-led the $210M Series B at $3.5B, Sequoia having "
                  "led the Series A earlier in 2025; the firm's /ai list dates its entry July 2025. GV then led the $200M "
                  "round of October 2025 at $6B, and Thrive and DST co-led the $250M Series D at $12B (TechCrunch, "
                  "2026-01-21), the mark kept here. Business Insider reported on 2026-09-24, from people familiar, a "
                  "$250M round led by a16z and hospital systems at $15B, not confirmed by the company; left for the "
                  "alignment pass, same band.",
             rounds=[rnd("2025", "Series A", None, "Sequoia Capital", None, OE_B, "company"),
                     rnd("2025-07-15", "Series B", 210000000, "GV and Kleiner Perkins", True, OE_B, "company"),
                     rnd("2025-10", "Round of October 2025", 200000000, "GV", True, OE_D, "press"),
                     rnd("2026-01-21", "Series D", 250000000, "Thrive Capital and DST", None, OE_D, "press"),
                     rnd("2026-09-24", "Unnamed (reported)", 250000000, "Andreessen Horowitz and hospital systems", None,
                         OE_15, "press")]))

# ---------------------------------------------------------------- Optimizely
OPT_2012 = "https://techcrunch.com/2012/05/30/optimizely-funding/"
OPT_A = "https://techcrunch.com/2013/04/10/optimizely-series-a/"
OPT_W = W("Optimizely")
L.append(cls("optimizely", status="acquired", rng="below_1b", city="San Francisco", focus="SaaS",
             stage="Seed", stage_src="model", stage_conf="medium", stage_cite=OPT_2012, entry_date="2012-05-30",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=OPT_A,
             note="A/B testing and experimentation software, San Francisco; acquired by Episerver in October 2020, which "
                  "then took the Optimizely name (Wikipedia). After a $1.2M angel round in 2010, Optimizely raised "
                  "'its first venture round' from Battery Ventures, Google Ventures and InterWest in May 2012, amount "
                  "undisclosed (TechCrunch); it had raised $3.2M in total when Benchmark led the $28M Series A in April "
                  "2013 with Google Ventures among existing investors (TechCrunch). The 2012 round is unnamed but sits "
                  "before the named Series A at about $2M, so it reads Seed (model, medium), and the Series A "
                  "graduates the row.",
             rounds=[rnd("2010-11", "Angel round", 1200000, None, False, OPT_W, "press"),
                     rnd("2012-05-30", "First venture round (amount undisclosed)", None, None, True, OPT_2012, "press"),
                     rnd("2013-04-10", "Series A", 28000000, "Benchmark", True, OPT_A, "press"),
                     rnd("2014-05", "Series B", 57000000, None, None, OPT_W, "press")]))

# ---------------------------------------------------------------- Optiwatt
L.append(cls("optiwatt", status="private", rng="below_1b", country="US", city="San Francisco",
             city_src="web_verified", focus="Climate & Energy", stage="undetermined",
             note="EV smart-charging app, now an energy-management platform for utilities; its own site gives San "
                  "Francisco and shows it operating in 2026. The firm's archived listing carries it from 2022 (Andy "
                  "Wheeler). Google News, TechCrunch's search and the company site name no round with GV or any "
                  "amount; stage undetermined, rounds list empty.",
             rounds=[]))

# ---------------------------------------------------------------- Oration
L.append(cls("oration", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="Healthcare & Bio", stage="undetermined",
             note="OrationRx, prescription price shopping (San Francisco, as on the a16z row). Status from the firm's own "
                  "exit line 'Acquired by PokitDok, 2017' on its live and archived listing; no press about the deal "
                  "was found (Google News and TechCrunch's search are empty), and the a16z row reads unknown. No "
                  "source read names GV's round; stage undetermined, rounds list empty.",
             rounds=[]))

# ---------------------------------------------------------------- Orbital Insight
ORB_A = NEWS("orbital-insight", "Orbital Insight Raises $9 Million for AI")
ORB_B = NEWS("orbital-insight", "Orbital Insight raises $20 million to wring")
ORB_W = W("Orbital Insight")
L.append(cls("orbital-insight", status="acquired", rng="below_1b", country="US", city="Palo Alto",
             city_src="web_verified", focus="Data Infrastructure", stage="Series A", stage_src="web_verified",
             stage_conf="high", stage_cite=ORB_A, entry_date="2015-03-16",
             note="Geospatial analytics from satellite imagery, Palo Alto (Wikipedia); bought by Privateer Space in "
                  "2024 (Wikipedia; the firm's exit line). SpaceNews (2015-03-16): Sequoia led the $8.7M Series A with "
                  "Bloomberg Beta, Google Ventures, citizen.vc and Lux participating, after $1.5M of Sequoia seed; GV "
                  "then led the $15M Series B in June 2016 (SpaceNews). Wikipedia's line that GV invested in 2016 "
                  "describes the Series B; the firm's archived listing already carried the company in April 2015.",
             rounds=[rnd("2014", "Seed", 1500000, "Sequoia Capital", False, ORB_A, "press"),
                     rnd("2015-03-16", "Series A", 8700000, "Sequoia Capital", True, ORB_A, "press"),
                     rnd("2016-06-27", "Series B", 15000000, "GV", True, ORB_B, "press"),
                     rnd("2017-05", "Series C", 50000000, "Sequoia Capital", None, ORB_W, "press")]))

# ---------------------------------------------------------------- Oscar
OSCAR_W = W("Oscar Health")
L.append(cls("oscar", rng="1b_plus", usd=9140000000, val_src="web_verified", val_cite=mcap("oscr"), asof=CHECK,
             val_conf="high", country="US", country_src="web_verified", country_cite=OSCAR_W, city="New York",
             focus="Healthcare & Bio", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=OSCAR_W, entry_date="2015-09", flags=["model_disputes_source"], extra=WV,
             note="Oscar Health (NYSE: OSCR), health insurer, New York (Wikipedia; the S-1 cover gives 75 Varick "
                  "Street). Country disputes the prefilled BE, a Wikidata join on the one-word name; the Khosla row "
                  "carries the same BE. Market cap $9.14B as of 2026-09-28 (stockanalysis.com), replacing the "
                  "2025-06-30 float and matching the General Catalyst row's $9.13B. Entry: Wikipedia records the 2015 "
                  "Series B ($145M) and then, in September 2015, 'a funding round with Google Ventures and Google "
                  "Capital, valuing the company at $1.75 billion', a later round, so Growth; Google Ventures 2014, L.P. "
                  "is a holder in the S-1.",
             rounds=[rnd("2015", "Series B", 145000000, None, None, OSCAR_W, "press"),
                     rnd("2015-09", "Unnamed (Google Ventures and Google Capital, $1.75B valuation)", None, None, True,
                         OSCAR_W, "press")]))

# ---------------------------------------------------------------- Osmo
OSMO_A = NEWS("osmo", "AI-powered fragrance company Osmo raises $70 million in Series B")
OSMO_WIRED = NEWS("osmo", "This Startup Is Using AI to Unearth New Smells")
OSMO_B = NEWS("osmo", "Osmo raises $70M and reports record patent")
L.append(cls("osmo", status="private", rng="below_1b", city="New York", focus="AI & Applied AI",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=OSMO_A, entry_date="2022-06",
             extra={**WV, "valuation_citation": OSMO_B},
             note="Digital olfaction, a Google Research spinout. Glossy (2026-02-04): Osmo launched in 2023 'with $60 "
                  "million in Series A funding led by Lux Capital and Google Ventures' (WIRED, 2023-01-24, calls it the "
                  "initial round); the firm's own /ai list dates the investment June 2022, used as the entry date. Two "
                  "Sigma Ventures led the $70M Series B in February 2026 (Premium Beauty News), no valuation "
                  "disclosed. WIRED placed the company in Cambridge MA in 2023; city aligned with the Lux row (New "
                  "York). Momentum slice check 2026-09-28: no priced round at or near $1B. The Accel row (Osmo, the "
                  "children's learning toy) and the Bain Capital Ventures row (Osmo, an AI video studio) are different "
                  "companies and are not aligned.",
             rounds=[rnd("2023-01-24", "Series A", 60000000, "Lux Capital and GV", True, OSMO_WIRED, "press"),
                     rnd("2026-02-04", "Series B", 70000000, "Two Sigma Ventures", None, OSMO_B, "press")]))

# ---------------------------------------------------------------- Oula Health
OULA_B = NEWS("oula-health", "Oula Secures $28M in Series B")
L.append(cls("oula-health", status="private", rng="below_1b", country="US", city="New York", focus="Healthcare & Bio",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=OULA_B, entry_date="2024-02-20",
             note="Midwifery-led maternity care clinics, founded in Brooklyn (New York, as on the 8VC row); still "
                  "opening clinics in 2026. Femtech Insider (2024-02-20): Revolution Ventures and Maverick Ventures "
                  "co-led the $28M Series B 'with contributions from GV and' earlier investors Female Founders Fund, "
                  "8VC, Alumni Ventures and Great Oaks, so GV entered at the Series B (the firm's listing starts in "
                  "2024).",
             rounds=[rnd("2024-02-20", "Series B", 28000000, "Revolution Ventures and Maverick Ventures", True, OULA_B,
                         "press")]))

# ---------------------------------------------------------------- Outdoor Voices
OV_C = NEWS("outdoor-voices", "Outdoor Voices raises $34 million in latest round")
OV_2026 = NEWS("outdoor-voices", "Outdoor Voices to Move Into China")
L.append(cls("outdoor-voices", status="acquired", rng="below_1b", city="Austin", city_src="web_verified",
             focus="Consumer & Marketplaces", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=OV_C, entry_date="2018-03-13",
             note="Activewear brand, Austin. CNBC (2018-03-13): a $34M Series C led by GV, earlier rounds having been "
                  "led by General Catalyst and Forerunner; Retail Dive calls GV a new addition. After the stores "
                  "closed in 2024 the brand was sold to Consortium Brand Partners, which WWD names as the brand owner "
                  "in June 2026; acquired, as on the General Catalyst row.",
             rounds=[rnd("2018-03-13", "Series C", 34000000, "GV", True, OV_C, "press")]))

# ---------------------------------------------------------------- Outlier
OUTLIER_B = NEWS("outlier", "Outlier.org Raises to $30M")
OUTLIER_ACQ = NEWS("outlier", "Savvas Learning Acquires Outlier.org")
L.append(cls("outlier", rng="below_1b", city="New York", focus="Consumer & Marketplaces", stage="Growth",
             stage_src="web_verified", stage_conf="high", stage_cite=OUTLIER_B, entry_date="2021-04",
             extra={"valuation_source": None, "valuation_confidence": None},
             note="Outlier.org, online college courses founded by MasterClass co-founder Aaron Rasmussen, New York "
                  "(AlleyWatch interview). AlleyWatch (April 2021): a $30M Series B led by GV with Unusual Ventures and "
                  "existing investors GSV and Harrison Metal, so GV entered at the Series B. Acquired by Savvas Learning "
                  "in February 2024 (EdWeek Market Brief). The First Round row named Outlier is a different company "
                  "(the business-data monitor Cisco bought) and is not aligned.",
             rounds=[rnd("2021-04", "Series B", 30000000, "GV", True, OUTLIER_B, "press")]))

# ---------------------------------------------------------------- Overture Life
OVT = NEWS("overture", "Overture Life Raises $20.6M to Scale IVF")
OVT_DALLAS = NEWS("overture", "Opens First U.S. Clinical Lab and Operations Hub in Dallas")
L.append(cls("overture", status="private", rng="below_1b", country="US", city="Dallas", city_src="web_verified",
             focus="Healthcare & Bio", stage="undetermined",
             note="Overture Life, IVF lab automation, founded in Madrid with offices in the US, UK and Spain (the firm's "
                  "own listing). In October 2025 it opened its first US clinical lab and operations hub in Dallas, "
                  "which its release calls its IVF robotics headquarters; city from that. The Felicis row reads Madrid "
                  "and the Khosla row (overture-life) New York from a 2017 Form D. Overwater Ventures led a $20.6M "
                  "strategic round in April 2025 with GV and Khosla participating, bringing total funding to $57M "
                  "(Femtech Insider). The firm's listing starts in 2021; no source names the round GV entered; stage "
                  "undetermined.",
             rounds=[rnd("2025-04-24", "Strategic round", 20600000, "Overwater Ventures", True, OVT, "press")]))

# ---------------------------------------------------------------- Overview
OVERVIEW_A = NEWS("overview", "Overview Lands $10 Million Series A")
L.append(cls("overview", status="private", rng="below_1b", country="US", city="San Francisco",
             city_src="web_verified", focus="AI & Applied AI", stage="Series A", stage_src="web_verified",
             stage_conf="high", stage_cite=OVERVIEW_A, entry_date="2022-02-17",
             extra={**WV, "valuation_citation": OVERVIEW_A},
             note="Overview.ai, AI visual inspection for manufacturing, founded by former Tesla engineers (Y "
                  "Combinator W19, the YC row). The company's release (San Francisco, 2022-02-17): Blumberg Capital "
                  "led the $10M Series A with new investors GV and Momenta; the firm's /ai list dates the investment "
                  "December 2021. Momentum slice check 2026-09-28: Google News shows no later round and no priced mark "
                  "at or near $1B.",
             rounds=[rnd("2022-02-17", "Series A", 10000000, "Blumberg Capital", True, OVERVIEW_A, "company")]))

# ---------------------------------------------------------------- Owkin
OWKIN_W = W("Owkin")
OWKIN_A1 = NEWS("owkin", "OWKIN Closes $11 Million Series A")
OWKIN_A2 = NEWS("owkin", "Owkin Raises $25M to Enhance")
OWKIN_A3 = NEWS("owkin", "Owkin closes Series A with $70 million")
L.append(cls("owkin", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified", val_cite=OWKIN_W,
             asof="2021-11", val_conf="medium", country="FR", country_src="web_verified", country_cite=OWKIN_W,
             city="Paris", focus="Healthcare & Bio", stage="Series A", stage_src="web_verified", stage_conf="medium",
             stage_cite=OWKIN_A3, entry_date="2018-05", flags=["stale"], extra=WV,
             note="AI for drug discovery and diagnostics, founded in Paris in 2016 (Wikipedia); offices in Paris, New "
                  "York and Geneva (its site, parent Owkin, Inc.). Otium Capital led the $11M Series A in January 2018 "
                  "(Cathay's release); the firm's /ai list dates GV's first investment May 2018, and ActuIA (July 2020) "
                  "lists GV among Owkin's Series A investors when the extended Series A closed at $70M; AlleyWatch "
                  "(May 2020) names GV an existing investor in the $25M extension. So GV entered in the Series A "
                  "(medium: the tranche is dated only by the firm's list). Mark: Owkin became a unicorn, valued at "
                  "more than $1B, through Sanofi's $180M equity investment in November 2021 (Wikipedia); $1B is that "
                  "floor, older than 24 months, so stale.",
             rounds=[rnd("2018-01-16", "Series A", 11000000, "Otium Capital", False, OWKIN_A1, "company"),
                     rnd("2018-05", "Series A tranche (the firm's first investment)", None, None, True, AI, "firm"),
                     rnd("2020-05", "Series A extension", 25000000, None, True, OWKIN_A2, "press"),
                     rnd("2020-07-01", "Series A close ($70M in total)", None, None, True, OWKIN_A3, "press"),
                     rnd("2021-11", "Sanofi strategic equity investment", 180000000, "Sanofi", None, OWKIN_W,
                         "press")]))

# ---------------------------------------------------------------- Packagd
PACKAGD_A = "https://techcrunch.com/2017/06/08/packagd-kpcb-forerunner-gv/"
PACKAGD_ACQ = NEWS("packagd", "Facebook quietly bought a startup")
L.append(cls("packagd", status="acquired", rng="below_1b", country="US", focus="Consumer & Marketplaces",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=PACKAGD_A,
             entry_date="2017-06-08", flags=["city_unknown"],
             note="Shoppable unboxing-video apps (Unboxed), incubated at Kleiner Perkins, which put up the first $1.5M; "
                  "TechCrunch (2017-06-08): a $6M Series A led by Forerunner Ventures and GV, with GV's M.G. Siegler "
                  "quoted. Facebook acquired Packagd in 2019 (Marketing Dive, citing Bloomberg; the firm's exit line "
                  "'Acquired in 2019'). Best Buy calls it a Silicon Valley startup; no source read gives the city.",
             rounds=[rnd("2017-06-08", "Series A", 6000000, "Forerunner Ventures and GV", True, PACKAGD_A, "press")]))

# ---------------------------------------------------------------- PACT Pharma
PACT_C = NEWS("pact-pharma", "Pact Pharma to lay off nearly 100")
PACT_2022 = NEWS("pact-pharma", "PACT unveils teased business venture")
L.append(cls("pact-pharma", status="unknown", rng="below_1b", country="US", city="South San Francisco",
             focus="Healthcare & Bio", stage="undetermined",
             note="Personalized neoantigen T-cell therapy, South San Francisco. Vida Ventures led the $75M Series C in "
                  "January 2020, and BioPharma Dive (2022-07-19) names GV among its earlier backers; in 2022 it laid off "
                  "94 people, ended its phase 1 program and sold its South San Francisco facility and some assets to "
                  "AmplifyBio (Fierce Biotech, 2022-10-03), planning a new trial in 2023. Nothing later was found and "
                  "its website returns 404 (checked 2026-09-28), while the firm's live list still carries it with no "
                  "exit line; no source read gives its fate, so unknown. No source names the round GV entered; stage "
                  "undetermined.",
             rounds=[rnd("2020-01", "Series C", 75000000, "Vida Ventures", None, PACT_C, "press")]))

jl.write("j9", L)
