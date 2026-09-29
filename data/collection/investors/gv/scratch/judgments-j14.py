"""PRO-75 grind, judge j14: queue batch 14 (45 member rows, TuneIn to Watch Club).

Every citation below is a URL a tool printed or a page read in this pass (TechCrunch's and Crunchbase News's own
WordPress search, Google News through nq.py, EDGAR's submissions API, the full-text hits via FTS(), the firm's own
posts via POST(), Wikipedia via wikifetch.py). Checked 2026-09-28."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, verdict, rnd, POST, SITE, ARCH, W, NEWS, FTS = (jl.cls, jl.verdict, jl.rnd, jl.POST, jl.SITE, jl.ARCH, jl.W,
                                                      jl.NEWS, jl.FTS)
L = []
TODAY = "2026-09-28"
VW = {"valuation_range_source": "web_verified"}
GRAD_LEFT = "Graduation left for the graduation pass."

# ---------------------------------------------------------------- TuneIn
TI_GUARDIAN = NEWS("tunein", "TuneIn raises $25m")
TI_DONE = NEWS("tunein", "Completion of TuneIn Acquisition")
L.append(cls("tunein", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="Media, Gaming & Advertising",
             stage="Growth", stage_src="model", stage_conf="medium", entry_date="2012-08",
             note="Internet radio and podcast streaming, San Francisco. Stingray Group closed its purchase of TuneIn "
                  "Holdings in December 2025 for up to $175M in cash (Stingray's release), so the row is acquired; the "
                  "three sibling books still read private and are staler. Entry: TuneIn's funding ran $6M from Sequoia "
                  "in 2010, $16M in August 2012 and $25M in May 2013 (Wikipedia and the Guardian, which puts the total "
                  "at $47M since the first round in 2010, exactly those three); the Guardian names Google Ventures among the previous investors in the May 2013 round IVP led, and "
                  "Wikipedia gives the 2010 round to Sequoia alone, so GV entered in the August 2012 round, the "
                  "company's second institutional round (a Series B, Growth). No source names GV in that round in "
                  "words, hence model at medium.",
             rounds=[rnd("2010", "unnamed ($6M)", 6000000, "Sequoia Capital", False, W("TuneIn"), "press"),
                     rnd("2012-08", "unnamed ($16M)", 16000000, None, None, W("TuneIn"), "press"),
                     rnd("2013-05-30", "unnamed ($25M)", 25000000, "Institutional Venture Partners", True, TI_GUARDIAN, "press"),
                     rnd("2017", "unnamed ($50M at $500M)", 50000000, None, None, W("TuneIn"), "press")]))

# ---------------------------------------------------------------- Turo (RelayRides)
TC_RR_2011_09 = "https://techcrunch.com/2011/09/21/relayrides-names-former-shopping-com-head-andre-haddad-as-ceo/"
TC_RR_2011_10 = "https://techcrunch.com/2011/10/26/carsharing-service-relayrides-raises-another-3-million-led-by-gm-ventures/"
TC_RR_2014 = "https://techcrunch.com/2014/06/24/relayrides-25m/"
TC_TURO_2015 = "https://techcrunch.com/2015/11/03/relayrides-rebrands-as-turo-and-raises-47-million-led-by-kleiner/"
TURO_UNICORN = NEWS("turo", "newest unicorn")
L.append(cls("turo", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified", val_cite=TURO_UNICORN,
             asof="2019-07", city="San Francisco", focus="Consumer & Marketplaces",
             stage="Series A", stage_src="model", stage_conf="medium", entry_date="2010-12",
             flags=("stale", "stage_disputes_band", "model_disputes_source"), extra=VW,
             note="Peer-to-peer car rental marketplace (RelayRides until 2015), San Francisco (the S-1's principal "
                  "office). Disputes the pre-filled status: 'defunct' came from a Wikidata join dated 1988, while Turo "
                  "operates, filed S-1 amendments through November 2024 and withdrew its IPO in February 2025 (EDGAR). "
                  "Mark: IAC's $250M Series E of July 2019 gave Turo 'a valuation of over $1 billion' (Yahoo Finance); "
                  "the figure is that stated floor, no later priced round is on record, and the mark is older than 24 "
                  "months, so stale. Disputes the Pre-Seed band: the band anchored on a 2009 filing (sold $672,500) "
                  "that carries no GV person, before GV's 2010 vehicle existed. GV 2010, L.P. holds Turo stock (the "
                  "S-1); TechCrunch (September 2011) names Google Ventures, August Capital and Shasta among the $10M "
                  "raised to date, and (October 2011) calls that financing the Series A, which GM Ventures' $3M "
                  "extension took to $13M; the Series A's first close is the Form D sold from 2010-12-14, the month "
                  "CNET called the company 'Google-backed'. The Series B ($25M, Canaan) followed in June 2014 with "
                  "Google Ventures named as a previous investor. Model at medium: no single page names GV in the "
                  "Series A in words.",
             rounds=[rnd("2010-12", "Series A (first close; $13M in all with GM Ventures' extension)", 13000000, None, True, TC_RR_2011_10, "press"),
                     rnd("2014-06-24", "Series B", 25000000, "Canaan Partners", True, TC_RR_2014, "press"),
                     rnd("2015-11-03", "Series C", 47000000, "Kleiner Perkins", None, TC_TURO_2015, "press"),
                     rnd("2019-07", "Series E", 250000000, "IAC", None, TURO_UNICORN, "press")]))

# ---------------------------------------------------------------- Twyla
L.append(cls("twyla", status="unknown", rng="below_1b", city="Austin", focus="Consumer & Marketplaces",
             note="Online marketplace for limited-edition contemporary art, Austin (the 2016 Form D address; David Krane "
                  "is a director on it). Fate not established: the last dated news is the January 2018 CEO change (PR "
                  "Newswire), and twyla.com shows only a 'pardon our dust' holding page. No source read gives a shutdown "
                  "or a sale, so unknown, aligned with IVP's row. The pre-filled Series A band (the $19.3M 2016 round) "
                  "stands."))

# ---------------------------------------------------------------- Uber
UBER_TC = "https://techcrunch.com/2013/08/22/google-ventures-puts-258m-into-uber-its-largest-deal-ever/"
UBER_CAP = "https://stockanalysis.com/stocks/uber/market-cap/"
L.append(cls("uber", status="public", rng="100b_plus", usd=139220000000, val_src="web_verified", val_cite=UBER_CAP,
             asof=TODAY, country="US", city="San Francisco", focus="Consumer & Marketplaces",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=UBER_TC, entry_date="2013-08",
             flags=("model_disputes_source",), extra=VW,
             note="Uber Technologies (NYSE: UBER), San Francisco. Disputes the pre-filled NL, a one-word Wikidata join to "
                  "Uber's Dutch holding entity; the operating headquarters is San Francisco (EDGAR business address, "
                  "1725 3rd Street). Market cap $139.22B as of 2026-09-28 (stockanalysis.com), fresher than the "
                  "siblings' September figures, same band. Entry: Google Ventures put $257.79M into Uber's August "
                  "2013 round, its largest deal then, at about $3.76B post-money (TechCrunch); the round's "
                  "shares were Series C-1 and C-2 and existing investor Benchmark added $15M (TechCrunch), after the "
                  "2011 Series A and B the Benchmark and Menlo rows cite, so Growth.",
             rounds=[rnd("2013-08-22", "Series C-1/C-2", 361200000, "Google Ventures", True, UBER_TC, "press")]))

# ---------------------------------------------------------------- UberSense
UBS_SEED = "https://techcrunch.com/2012/09/17/ubersense-1-1m/"
UBS_HUDL = NEWS("ubersense", "Hudl Acquires Ubersense")
L.append(cls("ubersense", status="acquired", rng="below_1b", country="US", city="Boston",
             focus="Consumer & Marketplaces",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=UBS_SEED, entry_date="2012-09",
             note="Video coaching app for athletes (Cambridge, Mass. in 2012, Boston at the sale). Ubersense announced a "
                  "$1.1M seed with Atlas Venture, Google Ventures and Boston Seed Capital in September 2012 "
                  "(TechCrunch). Hudl acquired it in September 2014; the team stayed in Boston, and it had raised "
                  "$2.5M in all from the same three investors (Re/code). " + GRAD_LEFT,
             rounds=[rnd("2012-09-17", "Seed", 1100000, None, True, UBS_SEED, "press")]))

# ---------------------------------------------------------------- Udacity
UDA_D = "https://techcrunch.com/2015/11/11/udacity-raises-105-million-series-d-bringing-valuation-to-1-billion/"
L.append(cls("udacity", status="acquired", rng="below_1b", city="Mountain View", focus="Consumer & Marketplaces",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=UDA_D, entry_date="2015-11",
             note="Online courses and nanodegrees, Mountain View. Accenture acquired it in May 2024 (Wikipedia; the "
                  "firm's own exit line agrees). Entry: Google Ventures joined the $105M Series D of November 2015 as a "
                  "new investor, in the Bertelsmann-led round that valued Udacity at $1B (TechCrunch); a16z, CRV and "
                  "Drive were the existing investors. Growth.",
             rounds=[rnd("2015-11-11", "Series D", 105000000, "Bertelsmann", True, UDA_D, "press")]))

# ---------------------------------------------------------------- UJET
UJET_B = NEWS("ujet", "raises $25M led by GV")
L.append(cls("ujet", status="private", rng="below_1b", country="US", city="San Francisco", focus="SaaS",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=UJET_B, entry_date="2018-02",
             note="Cloud contact-center software, San Francisco. GV led the $25M Series B of February 2018; the other "
                  "participants were returning investors Kleiner Perkins and DCM and new backer Citi Ventures "
                  "(TechCrunch), so GV was new at the B: Growth. Later rounds include a $76M Series D in September "
                  "2024 (Business Wire headline); no priced round at $1B or more is on record.",
             rounds=[rnd("2018-02-13", "Series B", 25000000, "GV", True, UJET_B, "press")]))

# ---------------------------------------------------------------- Typeface
TF_LAUNCH_CBN = "https://news.crunchbase.com/ai-robotics/venture-funding-ai-startup-typeface/"
TF_LAUNCH_TC = NEWS("typeface", "emerges from stealth with $65M to bring")
TF_B = NEWS("typeface", "raises $100M at a $1B valuation")
L.append(cls("typeface", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified", val_cite=TF_B,
             asof="2023-06-29", country="US", city="San Francisco", city_src="web_verified", focus="AI & Applied AI",
             stage="Series A", stage_src="model", stage_conf="medium", entry_date="2023-02",
             flags=("stale",), extra=VW,
             note="Generative AI for enterprise content, San Francisco ('a San Francisco-based generative AI startup', "
                  "Crunchbase News; Lightspeed's row says Palo Alto). Entry: GV's first 'Invested' month is February "
                  "2023 (the firm's /ai list), when Typeface emerged from stealth with $65M from Lightspeed, GV, M12 "
                  "and Menlo (TechCrunch, Crunchbase News); no page names that round, but the next one, $100M led by "
                  "Salesforce Ventures in June 2023 with GV participating, is named Series B, and the Lightspeed and "
                  "Menlo rows record their own firms' pages labelling the launch round Series A, so model at medium. Mark: the Series B valued "
                  "Typeface at $1B (TechCrunch, 2023-06-29), exactly the band edge, older than 24 months, so stale. "
                  "Momentum check 2026-09-28 (Google News on the name, twice): no later priced round and no "
                  "acquisition; the company still ships product in September 2026; the only newer valuation line is "
                  "a vendor estimate (GetLatka), which never bands.",
             rounds=[rnd("2023-02-27", "unnamed launch round ($65M)", 65000000, None, True, TF_LAUNCH_TC, "press"),
                     rnd("2023-06-29", "Series B", 100000000, "Salesforce Ventures", True, TF_B, "press")]))

# ---------------------------------------------------------------- Ultromics
ULT_B = NEWS("ultromics", "completes US$33 million Series B")
ULT_C = NEWS("ultromics", "Lands $55M Series C")
L.append(cls("ultromics", status="private", rng="below_1b", country="GB", country_src="web_verified",
             country_cite=ULT_C, city="Oxford", city_src="web_verified", focus="Healthcare & Bio",
             stage="Growth", stage_src="model", stage_conf="medium", entry_date="2021-08",
             note="AI echocardiography analysis for heart failure, Oxford (the Series C release is datelined Oxford, "
                  "England). Entry: GV's first 'Invested' month on its /ai list is August 2021, the month Ultromics "
                  "completed its $33M Series B (Cardiac Rhythm News headline; the article body is not readable to us), "
                  "and the July 2025 $55M Series C release names GV among the continuing investors. No page names GV "
                  "in the Series B in words, hence model at medium; Growth either way. No priced round at $1B or "
                  "more is on record.",
             rounds=[rnd("2021-08-19", "Series B", 33000000, None, True, ULT_B, "press"),
                     rnd("2025-07-31", "Series C", 55000000, "L&G, Allegis Capital, Lightrock", True, ULT_C, "company")]))

# ---------------------------------------------------------------- Unbabel
UNB_SEED_TC = "https://techcrunch.com/2014/07/18/unbabel-raises-1-5m-to-expand-translation-service-grow-customer-base/"
UNB_B_TC = "https://techcrunch.com/2018/01/11/unbabel/"
UNB_TP = NEWS("unbabel", "TransPerfect Solidifies Leadership")
UNB_INS = NEWS("unbabel", "declared insolvent after receiving")
L.append(cls("unbabel", status="acquired", rng="below_1b", city="San Francisco", focus="AI & Applied AI",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=W("Unbabel"), entry_date="2014-05",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=UNB_B_TC,
             note="AI-plus-human translation platform with headquarters in Lisbon and San Francisco (Wikipedia). "
                  "TransPerfect acquired it in August 2025 (TransPerfect's release; Wikipedia); the Portuguese entity "
                  "left behind was declared insolvent in June 2026 (Portugal Resident), after the sale, so the row "
                  "reads acquired. Entry: the $1.5M seed of May 2014 with Google Ventures among the investors "
                  "(Wikipedia; TechCrunch names Kevin Rose of Google Ventures, July 2014). Graduation: a $5M Series A "
                  "in October 2016 and a $23M Series B in January 2018 (TechCrunch). Country kept at the pre-filled US "
                  "with San Francisco as the city; Headline's row reads Lisbon and PT and YC's San Francisco and US, "
                  "so the two siblings already disagree and the dual headquarters is flagged for the A/B pass.",
             rounds=[rnd("2014-05", "Seed", 1500000, None, True, W("Unbabel"), "press"),
                     rnd("2016-10", "Series A", 5000000, None, None, UNB_B_TC, "press"),
                     rnd("2018-01-11", "Series B", 23000000, "Scale Venture Partners", None, UNB_B_TC, "press")]))

# ---------------------------------------------------------------- Universe
UNI_A = "https://techcrunch.com/2020/04/07/mobile-website-builder-universe-raises-10m-from-gv-as-it-ventures-into-commerce"
UNI_B = NEWS("universe", "Universe Raises $30M to Empower Creators")
L.append(cls("universe", status="private", rng="below_1b", country="US", city="New York", city_src="web_verified",
             focus="SaaS", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=UNI_A,
             entry_date="2020-04", flags=("model_disputes_source",),
             extra={"valuation_source": None, "valuation_asof": None, "valuation_range_source": None, "acquirer": None},
             note="Universe (univer.se), the no-code website builder for iPhone, Brooklyn (TechCrunch; the Series B "
                  "release is datelined Brooklyn), so New York. Disputes both pre-fills: the Wikidata join ('acquired "
                  "by Arcs', dated 2017, and CZ) is a different entity; this company raised a $30M Series B led by "
                  "Addition in December 2021, won a 2023 Apple Design Award, launched an AI designer in July 2023 "
                  "(TechCrunch) and its site still sells, so private. The GC and YC sibling rows carry the same stale "
                  "Wikidata status (acquired, defunct) and are flagged for alignment. Entry: GV's M.G. Siegler led the "
                  "$10M Series A of April 2020 and took a board seat (TechCrunch); the company had raised $7.2M before "
                  "from BoxGroup and General Catalyst. The December 2021 release names Google Ventures among the "
                  "existing investors. No priced round at $1B or more is on record.",
             rounds=[rnd("2020-04-07", "Series A", 10000000, "GV", True, UNI_A, "press"),
                     rnd("2021-12-06", "Series B", 30000000, "Addition", True, UNI_B, "company")]))

# ---------------------------------------------------------------- Upbound (Crossplane)
L.append(cls("upbound", status="private", rng="below_1b", city="Seattle", city_src="formd_address",
             focus="DevTools & APIs", flags=("model_disputes_source",),
             note="Upbound (upbound.io), the company behind the Crossplane cloud control plane, Seattle (its Form D "
                  "address). Disputes the pre-filled public status and the $1.41B float: the weak CIK join picked up "
                  "Upbound Group, Inc. (NASDAQ: UPBD, the former Rent-A-Center), a different company. This Upbound is "
                  "private and still ships product (August 2026 platform launch). The pre-filled Series A band (the "
                  "$9M 2018 round, Dave Munichiello a director) stands; the later $52M round of November 2021 carries "
                  "no disclosed valuation, and no priced round at $1B or more is on record.",
             extra={"valuation_usd": None, "valuation_source": None, "valuation_range_source": None,
                    "valuation_asof": None}))

# ---------------------------------------------------------------- Upstart
L.append(cls("upstart", country="US", city="Burlingame", city_src="web_verified", focus="Fintech & Payments",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=W("Upstart Holdings"),
             entry_date="2012-04",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=W("Upstart Holdings"),
             note="AI lending marketplace (NASDAQ: UPST). Its latest 10-Q (filed 2026-08-04) gives the principal "
                  "executive office as 220 Park Road, Burlingame; the First Round and Khosla rows still read San Mateo "
                  "and are staler. Entry: the $1.75M seed that came with the April 2012 launch, from First Round, "
                  "Kleiner Perkins, NEA, Google Ventures, Crunchfund and Mark Cuban (Wikipedia). Graduation: the $5.9M "
                  "Series A that followed (Wikipedia), a named later round, so graduated whatever the amounts.",
             rounds=[rnd("2012-04", "Seed", 1750000, None, True, W("Upstart Holdings"), "press"),
                     rnd(None, "Series A", 5900000, None, None, W("Upstart Holdings"), "press")]))

# ---------------------------------------------------------------- Upthere
UPT_2015 = "https://techcrunch.com/2015/10/29/whats-upthere/"
UPT_77 = "https://techcrunch.com/2016/07/27/upthere-puts-a-new-spin-on-personal-cloud-storage/"
UPT_WD = "https://techcrunch.com/2017/08/28/western-digital-acquires-cloud-services-company-upthere/"
L.append(cls("upthere", status="acquired", rng="below_1b", country="US", city="Palo Alto", city_src="web_verified",
             focus="Consumer & Marketplaces", stage="undetermined",
             note="Consumer cloud storage built by Apple and Oracle veterans, Palo Alto (TechCrunch, 2015). Western "
                  "Digital acquired it in August 2017 (TechCrunch). Stage undetermined: Upthere never disclosed the "
                  "size or number of its rounds (TechCrunch, 2015); it came out of beta in July 2016 with $77M raised "
                  "in all from KPCB and Western Digital (leads) with Floodgate, Elevation Partners, GV, NTT Docomo "
                  "Ventures and Square 1 Bank, and no page ties GV to a named round. The firm has listed it since "
                  "2013 (the year is an anchor from the archive, not an entry label).",
             rounds=[rnd("2016-07-27", "cumulative financing to date ($77M)", 77000000, "KPCB and Western Digital", True, UPT_77, "press")]))

# ---------------------------------------------------------------- Urban Engines
UE_TC = "https://techcrunch.com/2014/05/15/backed-by-google-ventures-and-eric-schmidt-urban-engines-wants-to-solve-urban-congestion-using-data-intelligence/"
L.append(cls("urban-engines", status="acquired", rng="below_1b", city="Los Altos", focus="SaaS",
             stage="undetermined", entry_date="2014",
             note="Urban mobility and location analytics, Los Altos (aligned with a16z's row). Google acquired it in "
                  "September 2016 (Wikipedia; the firm's own exit line). Stage undetermined: at its May 2014 launch "
                  "Urban Engines had raised an undisclosed amount from Google Ventures, Eric Schmidt, Ram Shriram, "
                  "a16z and SV Angel (TechCrunch), and Wikipedia says the round was led by Google Ventures, but no "
                  "source names it.",
             rounds=[rnd("2014-05-15", "unnamed (undisclosed amount)", None, "Google Ventures", True, UE_TC, "press")]))

# ---------------------------------------------------------------- Urban Machine
UM_SEED = "https://www.einpresswire.com/article/605438698/urban-machine-closes-5-6m-seed-round-to-build-a-greener-future"
L.append(cls("urban-machine", status="private", rng="below_1b", country="US", city="Oakland", city_src="web_verified",
             focus="Industrial & Robotics",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=UM_SEED, entry_date="2022-12",
             note="Robotics and AI that reclaim lumber from construction and demolition waste, Oakland (the seed "
                  "release is datelined Oakland, CA). Lowercarbon Capital and GV led the $5.6M seed, announced 9 "
                  "December 2022, with Union Labs and Catapult Ventures following on (the company's release). A 2025 "
                  "raise appears only on a data-vendor page, which cannot cite a round. " + GRAD_LEFT,
             rounds=[rnd("2022-12-09", "Seed", 5600000, "Lowercarbon Capital and GV", True, UM_SEED, "company")]))

# ---------------------------------------------------------------- Ursa Computing
URSA_SEED = "https://ursalabs.org/blog/ursa-computing/"
VD_TC = "https://techcrunch.com/2022/02/17/voltron-data-grabs-110m-to-build-startup-based-on-apache-arrow-project/"
L.append(cls("ursa-computing", status="acquired", rng="below_1b", country="US", focus="Data Infrastructure",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=URSA_SEED, entry_date="2020-10",
             flags=("city_unknown",),
             note="Wes McKinney's Apache Arrow company. Its own announcement (10 December 2020) says it raised $4.9M in "
                  "seed funding led by GV with Walden International, Nepenthe, Amplify Partners and RStudio; GV's /ai "
                  "list dates the investment October 2020. Ursa folded into Voltron Data in 2021 (Ursa Labs' site now "
                  "reads 'Ursa Labs is now Voltron Data Labs', and Voltron Data was launched by staff from Nvidia, "
                  "Ursa Computing and BlazingSQL, TechCrunch), so acquired by merger. No source read places Ursa "
                  "Computing in a city. " + GRAD_LEFT,
             rounds=[rnd("2020-12-10", "Seed", 4900000, "GV", True, URSA_SEED, "company")]))

# ---------------------------------------------------------------- URX
URX_SEED = "https://techcrunch.com/2013/10/16/urx-ads/"
URX_2014 = "https://techcrunch.com/2014/04/28/mobile-deep-linking-startup-urx-raises-12-million-launches-universal-link-service-called-omnilinks/"
L.append(cls("urx", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="Media, Gaming & Advertising",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=URX_SEED, entry_date="2013-10",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=URX_2014,
             note="Mobile deep-linking product ads, San Francisco (YC Summer 2012). Pinterest acquired it in 2016 (the "
                  "firm's own exit line). Entry: the $3.1M seed of October 2013 lists Google Ventures among the "
                  "investors (TechCrunch). Graduation: Accel led a $12M round in April 2014 at a $40M valuation with "
                  "Google Ventures following (TechCrunch); the round is unnamed, and $12M clears max(2 x $3.1M, $5M).",
             rounds=[rnd("2013-10-16", "Seed", 3100000, None, True, URX_SEED, "press"),
                     rnd("2014-04-28", "unnamed", 12000000, "Accel", True, URX_2014, "press")]))

# ---------------------------------------------------------------- Vaccitech (Barinthus Bio)
VAC_S1 = FTS("Vaccitech", "S-1")
VAC_8K = "https://www.sec.gov/Archives/edgar/data/1828185/000110465926106183/tm2625093d1_8k.htm"
VAC_10K = "https://www.sec.gov/Archives/edgar/data/1828185/000182818526000012/brns-20251231.htm"
L.append(cls("vaccitech", status="acquired", rng="below_1b", country="GB", country_src="web_verified",
             country_cite=VAC_S1, city="Germantown", city_src="web_verified", focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=VAC_S1, entry_date="2017-11",
             flags=("city_country_conflict", "model_disputes_source"),
             note="Oxford vaccine and T-cell immunotherapy spin-out (renamed Barinthus Biotherapeutics in 2023). "
                  "Disputes the pre-filled public status: Clywedog's holding company acquired all of Barinthus's shares "
                  "under a scheme of arrangement effective 9 September 2026, making it a wholly owned subsidiary (the "
                  "8-K), and the ADSs were delisted; the firm's exit line 'NASDAQ: VACC' is stale (decisions D8). "
                  "Entry: entities affiliated with GV (GV Europe 2014 and GV 2017) bought 5,516 Series A shares for "
                  "GBP 6.0M in the Series A that opened in November 2017 (the S-1's related-party table); the firm's "
                  "own post dates GV's investment to 2017. Country: GB confirmed at entry (the S-1 gives Oxford); the "
                  "principal executive office moved from Harwell, Oxfordshire to Germantown, Maryland by the FY2025 "
                  "10-K, so the last-known city is Germantown and the pair is flagged city_country_conflict for Erik.",
             rounds=[rnd("2017-11", "Series A", 33900000, None, True, VAC_S1, "filing"),
                     rnd("2021-03-15", "Series B", 125000000, None, None, VAC_S1, "filing")]))
# Vaccitech carries a sec_public_float source from the pre-fill; an acquired row keeps no mark.
L[-1].update({"valuation_source": None, "valuation_range_source": None, "valuation_asof": None})

# ---------------------------------------------------------------- Vareto
VAR_A = "https://techcrunch.com/2021/10/01/vareto-raises-24m-from-gv-menlo-and-all-star-angels-to-reinvent-financial-planning-for-enterprises/"
L.append(cls("vareto", status="private", rng="below_1b", country="US", city="Mountain View", city_src="web_verified",
             focus="SaaS",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=VAR_A, entry_date="2021",
             note="FP&A and strategic finance planning software. GV led the $20M Series A in 2021 after Menlo Ventures "
                  "led the $4.2M seed in the summer of 2020 (TechCrunch, 2021-10-01), so GV entered at the A. City: "
                  "TechCrunch calls it 'Mountain View-based'; Menlo's row reads San Francisco without a citation, so "
                  "the two books disagree and the city is flagged for the A/B pass. Status: operating and independent "
                  "(its own site, footer 2025; product releases through April 2024). Momentum check 2026-09-28 (Google "
                  "News on the name): no priced round at $1B or more; the newest items are 2022-2024 product and "
                  "hiring releases.",
             rounds=[rnd("2020", "Seed", 4200000, "Menlo Ventures", False, VAR_A, "press"),
                     rnd("2021", "Series A", 20000000, "GV", True, VAR_A, "press")]))

# ---------------------------------------------------------------- Veem (Align Commerce)
VEEM_TC = "https://techcrunch.com/2017/03/08/align-commerce-veem-24-million/"
L.append(cls("veem", status="private", rng="below_1b", country="US", city="San Francisco", focus="Fintech & Payments",
             stage="Growth", stage_src="model", stage_conf="medium", entry_date="2017-03",
             note="Cross-border B2B payments (Align Commerce until March 2017), San Francisco (Wikipedia). Entry: GV was "
                  "a new investor in the $24M round led by NAB Ventures that came with the rebrand in March 2017, which "
                  "took total funding past $40M (TechCrunch); the company had already raised more than $16M in earlier "
                  "rounds, so the $24M round was its Series B or later. No page names the round, hence model at "
                  "medium; Growth either way. A $31M raise followed in 2020 (Business Insider headline); no priced "
                  "round at $1B or more is on record.",
             rounds=[rnd("2017-03-08", "unnamed ($24M)", 24000000, "NAB Ventures", True, VEEM_TC, "press")]))

# ---------------------------------------------------------------- Ventus Therapeutics
VEN_A = NEWS("ventus-therapeutics", "Launches with $60 Million Series A")
L.append(cls("ventus-therapeutics", status="private", rng="below_1b", city="Waltham", city_src="web_verified",
             focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=VEN_A,
             flags=("stage_disputes_band",),
             note="Structural-immunology drug discovery (NLRP3 and innate immunity), Waltham, Mass. with research in "
                  "Montreal (the launch release's dateline). Disputes the Growth band: the band read the $60M 2020 "
                  "filing against the era's Series A ceiling, but the company names it: 'a $60 million Series A "
                  "financing led by founding investor Versant Ventures with participation by GV' (6 May 2020), with "
                  "GV's Brendan Bulik-Sullivan quoted and a director on the filing, so Series A. The pre-filled entry "
                  "date (2019-11-18, that Series A's first sale) stands. Later rounds: $100M Series B (April 2021), "
                  "$140M Series C led by SoftBank (February 2022), then a Novo Nordisk licensing deal; no sale and no "
                  "priced round at $1B or more is on record.",
             rounds=[rnd("2020-05-06", "Series A", 60000000, "Versant Ventures", True, VEN_A, "company")]))

# ---------------------------------------------------------------- Veo Robotics
VEO_A = NEWS("veo-robotics", "raises $12m in Series A round backed by Google")
VEO_SALE = NEWS("veo-robotics", "Symbotic acquires Veo Robotics for $8.7M")
L.append(cls("veo-robotics", status="acquired", rng="below_1b", country="US", city="Waltham",
             focus="Industrial & Robotics",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=VEO_A, entry_date="2017-09",
             note="3D sensing and safety software for industrial robots, Waltham. Symbotic bought it for $8.7M in "
                  "August 2024, taking most of its IP and staff (The Robot Report); the firm's exit line agrees. Entry: "
                  "GV's $12M Series A in 2017, with Lux Capital joining and GV's Andy Wheeler taking a board seat, "
                  "after a $1M seed from Siemens' venture arm (The Robot Report); GV's /ai list dates its first "
                  "investment September 2017 (the entry date, D7). A $29M Series B followed in 2023 (TechCrunch).",
             rounds=[rnd("2017-10-19", "Series A", 12000000, "GV", True, VEO_A, "press"),
                     rnd("2023-04-25", "Series B", 29000000, None, None, "https://techcrunch.com/2023/04/25/robotics-safety-firm-veo-raises-29-million-with-help-from-amazon/", "press")]))

# ---------------------------------------------------------------- Vera Therapeutics (formerly Trucode Gene Repair)
VERA_S1 = FTS("Vera Therapeutics", "S-1")
TRU_34 = NEWS("trucode", "Kleiner, GV drive gene editing startup")
L.append(cls("vera-therapeutics", country="US", city="Brisbane", city_src="web_verified", focus="Healthcare & Bio",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=VERA_S1, entry_date="2019-09",
             note="Immunology biotech (atacicept), NASDAQ: VERA; renamed from Trucode Gene Repair in April 2020 and from "
                  "CDF Therapeutics before that (the S-1). Current principal office 2000 Sierra Point Parkway, Brisbane "
                  "(EDGAR). Entry: the S-1's beneficial-ownership table shows GV 2017, L.P. holding only Series B "
                  "preferred and GV 2019, L.P. the Series C; Kleiner Perkins held the Series A and B. Trucode emerged "
                  "from stealth in September 2019 with $34M from Kleiner Perkins and GV (Fierce Biotech, BioSpace), "
                  "which dates the Series B GV bought. Growth. The base also carries this company as 'trucode' (the "
                  "firm listed TruCode in 2019-2021): one company, two rows.",
             rounds=[rnd("2019-09-10", "Series B (announced with $34M in total financing)", 34000000, None, True, TRU_34, "press"),
                     rnd("2020-10", "Series C", 80000000, "Abingworth", True, VERA_S1, "filing")]))

# ---------------------------------------------------------------- Verana Health
VERANA_C = NEWS("verana-health", "Verana Health raises $30 million Series C")
VERANA_E = NEWS("verana-health", "Secures $150M Series E")
L.append(cls("verana-health", status="private", rng="below_1b", country="US", city="San Francisco",
             focus="Healthcare & Bio",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=VERANA_C, entry_date="2018-07",
             note="Real-world clinical data from specialty-society registries, San Francisco. GV led the $30M Series C "
                  "of July 2018, with Biomatics Capital, GE Ventures, Lagunita Biosciences and Brook Byers named as the "
                  "existing investors (MedCity News), so GV entered at the C: Growth. By February 2020 the company "
                  "had raised $100M from GV, Bain Capital Ventures, Casdin and Define (TechCrunch), and GV joined the $150M Series E of January 2022 as an "
                  "existing investor (Verana's release). No priced round at $1B or more is on record.",
             rounds=[rnd("2018-07-31", "Series C", 30000000, "GV", True, VERANA_C, "press"),
                     rnd("2022-01-14", "Series E", 150000000, "Johnson & Johnson Innovation, Novo Growth", True, VERANA_E, "company")]))

# ---------------------------------------------------------------- Vercel
VERCEL_POST = POST("vercel-founder-guillermo-rauch")
L.append(cls("vercel", city="San Francisco", focus="DevTools & APIs",
             stage="Growth", stage_src="first_party", stage_conf="high", stage_cite=VERCEL_POST, entry_date="2020-12",
             note="Frontend cloud and the Next.js framework, San Francisco. Entry: GV's /ai list dates its first "
                  "investment December 2020, and the firm's own post of 16 December 2020 says Vercel had 'just "
                  "announced its Series B funding, led by GV', so the Series B was GV's entry: Growth. The pre-filled "
                  "$9.3B (the September 2025 Series F) stands.",
             rounds=[rnd("2020-12", "Series B", None, "GV", True, VERCEL_POST, "firm")]))

# ---------------------------------------------------------------- Verse (Verse Enterprises)
VERSE_A = "https://verse.inc/press/verse-inc-secures-20-5-million-series-a-funding-led-by-gv/"
VERSE_B = NEWS("verse-enterprises", "Verse Raises $54M and Launches")
L.append(cls("verse-enterprises", status="private", rng="below_1b", city="San Francisco", city_src="web_verified",
             focus="Climate & Energy",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=VERSE_A, entry_date="2024-05",
             flags=("stage_disputes_band",),
             note="Grid connection and power dispatch software for data centers and large energy buyers (verse.inc), "
                  "San Francisco. Disputes the Seed band: both Form Ds were filed together in 2024 with the same "
                  "directors, so the band's 2022 anchor is the seed Coatue led, not GV's. Verse's own release (22 May "
                  "2024): 'our $20.5M Series A funding round led by Google Ventures, with notable participation from "
                  "our lead seed round investor, Coatue', so GV entered at the Series A. Bessemer led the $54M Series "
                  "B in June 2026 with GV participating (GlobeNewswire); no valuation was disclosed. Coatue's book "
                  "carries the same company as 'verse' (private, below $1B, San Francisco), and this row agrees.",
             rounds=[rnd("2024-05-22", "Series A", 20500000, "GV", True, VERSE_A, "company"),
                     rnd("2026-06-18", "Series B", 54000000, "Bessemer Venture Partners", True, VERSE_B, "company")]))

# ---------------------------------------------------------------- Verve Therapeutics
VERVE_S1 = FTS("Verve Therapeutics", "S-1")
L.append(cls("verve-therapeutics", rng="below_1b", city="Boston", city_src="web_verified", focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=VERVE_S1, entry_date="2018-08",
             flags=("stage_disputes_band",),
             note="PCSK9 gene-editing medicines; acquired by Eli Lilly in 2025 (the pre-filled status; the firm's exit "
                  "line 'NASDAQ: VERV' is stale). Last principal office 201 Brookline Avenue, Boston (EDGAR). Disputes "
                  "the Growth band, which read the January 2021 Series B filing: the S-1's related-party tables show "
                  "GV 2017, L.P. buying $7.0M of the Series A in its first closing of August 2018 (then further "
                  "tranches in 2019 and 2020), and the firm's own post says 'GV led the $58.5M Series A'. GV 2019 "
                  "then bought Series A-2 (2020) and $5M of the $94M Series B (2021).",
             rounds=[rnd("2018-08", "Series A", 58500000, "GV", True, POST("verve-therapeutics-ipo"), "firm"),
                     rnd("2021-01", "Series B", 94000000, "Wellington Management and Casdin Capital", True, VERVE_S1, "filing")]))

# ---------------------------------------------------------------- Veza
VEZA_POST = POST("congratulations-veza")
VEZA_CLOSE = "https://www.crnasia.com/news/2026/cybersecurity/servicenow-s-veza-integration-fuels-identity-security-push-f"
L.append(cls("veza", status="acquired", rng="below_1b", country="US", city="Palo Alto", focus="Security",
             stage="Growth", stage_src="first_party", stage_conf="medium", stage_cite=VEZA_POST, entry_date="2021",
             note="Identity and authorization security, Palo Alto (aligned with the sibling rows). ServiceNow announced "
                  "the purchase in December 2025 and completed it on 2 March 2026 (CRN Asia), so acquired, aligned "
                  "with BCV's row (Accel's still reads private and is staler). Entry: the firm's own post says 'When GV "
                  "led Veza's Series B in 2021', and its April 2022 post calls GV 'an early investor'; no firm page "
                  "shows an earlier GV round, so the Series B is read as the entry: Growth, medium because the post "
                  "does not say 'first' in words.",
             rounds=[rnd("2021", "Series B", None, "GV", True, VEZA_POST, "firm")]))

# ---------------------------------------------------------------- Vicinitas Therapeutics
VIC_A = NEWS("vicinitas-therapeutics", "Investing in Vicinitas Therapeutics")
VIC_CBN = "https://news.crunchbase.com/venture/biggest-funding-rounds-vc-startups-cleerly-carmot/"
L.append(cls("vicinitas-therapeutics", status="private", rng="below_1b", country="US", city="South San Francisco",
             city_src="web_verified", focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=VIC_A, entry_date="2022-07",
             note="Protein stabilization (DUBTAC) spun out of Novartis and UC Berkeley, South San Francisco (Crunchbase "
                  "News). It launched in July 2022 with a $65M Series A co-led by a16z and Deerfield, with Droia, GV, "
                  "The Mark Foundation and the Berkeley Catalyst Fund participating (a16z's announcement), the "
                  "company's first financing, so GV entered at the A. No later priced round is on record.",
             rounds=[rnd("2022-07-28", "Series A", 65000000, "a16z and Deerfield", True, VIC_A, "firm")]))

# ---------------------------------------------------------------- VIDA
VIDA_SEED = "https://techcrunch.com/2014/11/12/vida-raises-1-3-million-for-socially-responsible-e-commerce/"
L.append(cls("vida", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="Consumer & Marketplaces",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=VIDA_SEED, entry_date="2014-11",
             note="Marketplace turning artists' designs into apparel and accessories (YC Summer 2017), San Francisco. "
                  "Cimpress acquired it in 2018 (the firm's own exit line; YC's row agrees). Entry: the $1.3M seed "
                  "disclosed in November 2014, with Google Ventures' M.G. Siegler and Dave Munichiello named as its "
                  "investors in VIDA (TechCrunch). " + GRAD_LEFT,
             rounds=[rnd("2014-11-12", "Seed", 1300000, None, True, VIDA_SEED, "press")]))

# ---------------------------------------------------------------- VigLink
L.append(cls("viglink", status="acquired", rng="below_1b", city="San Francisco", focus="Media, Gaming & Advertising",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=W("VigLink"),
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=W("VigLink"),
             flags=("stage_disputes_band",),
             note="Outbound-link monetization for publishers, San Francisco; merged into Sovrn in 2018 (the firm's exit "
                  "line; now Sovrn Commerce), so acquired. Disputes the Pre-Seed band: the record names the $800,000 "
                  "round of 2009 'seed funding from First Round Capital and Google Ventures' (Wikipedia; the Form D of "
                  "June 2009 sold exactly $800,000), so Seed; the pre-filled entry date stands. Graduation: a $5.4M "
                  "Series B led by Emergence Capital in March 2011 with Google Ventures and First Round following "
                  "(Wikipedia), a named later round. First Round's row still carries the Pre-Seed band on the same "
                  "round.",
             rounds=[rnd("2009-06", "Seed", 800000, None, True, W("VigLink"), "press"),
                     rnd("2011-03", "Series B", 5400000, "Emergence Capital", True, W("VigLink"), "press")]))

# ---------------------------------------------------------------- Vir Biotechnology
VIR_IRA = FTS("Vir Biotechnology", "S-1")
L.append(cls("vir-biotechnology", country="US", city="San Francisco", focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=VIR_IRA, entry_date="2017",
             note="Infectious-disease immunology biotech (NASDAQ: VIR), San Francisco (EDGAR business address). Entry: "
                  "GV 2017, L.P. signed Vir's Amended and Restated Investors' Rights Agreement dated 29 November 2017 "
                  "as an investor (the S-1 exhibit); the S-1 shows only Series A-1 and A-2 preferred outstanding then, "
                  "with the Series B issued in January 2019, so GV's position was bought in the Series A-1 financing "
                  "of 2016-2018. Series A, medium because the exhibit does not state the series GV bought.",
             rounds=[rnd("2017-11-29", "Series A-1 (GV an investor-rights party by this date)", None, None, True, VIR_IRA, "filing"),
                     rnd("2019-01", "Series B", 327600000, None, None, VIR_IRA, "filing")]))

# ---------------------------------------------------------------- Vitara Biomedical
VIT_B = NEWS("vitara-biomedical", "Vitara Biomedical Raises $50 Million in Additional Financing")
L.append(cls("vitara-biomedical", status="private", rng="below_1b", country="US", city="Philadelphia",
             city_src="web_verified", focus="Healthcare & Bio",
             stage="Growth", stage_src="model", stage_conf="medium", entry_date="2024-11",
             note="Extra-uterine support (EXTEND) for extremely premature infants, out of CHOP, Philadelphia (its own "
                  "site gives 2301 Chestnut Street). Sands Capital led the $50M Series B of November 2024 'with "
                  "participation from Google Ventures (GV), First Spark Ventures, Flerie and Khosla Ventures', and GV's "
                  "Cathy Friedman is a board observer (the company's release). The only earlier financing on record is "
                  "an unlabeled $25M round of August 2022 whose investors we could not read, and the firm first lists "
                  "Vitara in 2024; the Series B is read as GV's entry, model at medium because no page says GV was new. "
                  "Growth.",
             rounds=[rnd("2022-08-09", "unnamed ($25M)", 25000000, None, None, NEWS("vitara-biomedical", "raises $25M to advance its artificial womb"), "press"),
                     rnd("2024-11-19", "Series B", 50000000, "Sands Capital", True, VIT_B, "company")]))

# ---------------------------------------------------------------- Viz.ai
VIZ_A = NEWS("viz-ai", "AI healthcare co Viz.ai raises $21m")
VIZ_B = NEWS("viz-ai", "Viz.ai Raises $50M To Detect")
VIZ_D = "https://www.insightpartners.com/ideas/viz-ai-raises-100-million-in-series-d-funding-led-by-tiger-global-and-insight-partners-at-1-2-billion-valuation/"
L.append(cls("viz-ai", status="private", rng="1b_plus", usd=1200000000, val_src="web_verified", val_cite=VIZ_D,
             asof="2022-04-07", city="San Francisco", focus="Healthcare & Bio",
             stage="Series A", stage_src="model", stage_conf="medium", entry_date="2018-06",
             flags=("stale",), extra=VW,
             note="AI stroke detection and care coordination, San Francisco (with Tel Aviv R&D). Entry: GV's /ai list "
                  "dates its first investment June 2018; Kleiner Perkins led the $21M round announced in July 2018 "
                  "'with participation from Google's GV fund' after Innovation Endeavors' $7.5M round (Globes), and the "
                  "next round, $50M in October 2019, is named Series B with GV and Kleiner as existing investors "
                  "(NoCamels), so the $21M round was the Series A; no page names it, hence model at medium. Mark: the "
                  "$100M Series D of April 2022 at $1.2B, co-led by Tiger Global and Insight with GV following (Insight's "
                  "release), older than 24 months, so stale; aligned with Insight's row.",
             rounds=[rnd("2018-07-18", "unnamed ($21M)", 21000000, "Kleiner Perkins", True, VIZ_A, "press"),
                     rnd("2019-10-23", "Series B", 50000000, "Greenoaks", True, VIZ_B, "press"),
                     rnd("2022-04-07", "Series D", 100000000, "Tiger Global and Insight Partners", True, VIZ_D, "firm")]))

# ---------------------------------------------------------------- Vocode
VOC_SEED = NEWS("vocode", "Conversational AI Startup Raises $3.25 Million")
L.append(cls("vocode", status="acquired", rng="below_1b", country="US", city="San Francisco", focus="AI & Applied AI",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=VOC_SEED, entry_date="2023-04",
             note="Open-source voice AI framework for developers (YC Winter 2023), San Francisco (Business Insider). "
                  "Entry: the $3.25M seed from Y Combinator, Base10, GV, Gradient, Accel and Liquid2, closed in the "
                  "weeks after YC's demo day (Business Insider, February 2024); GV's /ai list dates the investment "
                  "April 2023. Status aligned with YC's row, whose directory lists Vocode as acquired; no source read "
                  "names an acquirer, and vocode.dev now redirects to the company's GitHub organization, last active "
                  "November 2024. Momentum check 2026-09-28 (Google News twice, one web search): no priced round at "
                  "$1B or more. " + GRAD_LEFT,
             rounds=[rnd("2023-04", "Seed", 3250000, None, True, VOC_SEED, "press")]))

# ---------------------------------------------------------------- Voicea (Voicera; legal name Rizio, Inc.)
VOI_A = "https://techcrunch.com/2018/03/07/voicera-lands-20-million-with-help-from-big-enterprise-investors/"
L.append(cls("voicea", status="acquired", rng="below_1b", country="US", city="Menlo Park", city_src="formd_address",
             focus="AI & Applied AI",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=VOI_A, entry_date="2018-03",
             note="AI meeting assistant (Voicera, legal name Rizio, Inc.); Cisco acquired it in 2019 (the firm's exit "
                  "line; Headline's row agrees). Entry: the $13.5M Series A of March 2018 led by e.ventures, with GV "
                  "among the enterprise investors (TechCrunch); GV's /ai list dates the investment March 2018. City: "
                  "Rizio's Form Ds of December 2017 and March 2018 give Menlo Park (earlier ones Los Altos); Headline's "
                  "row reads San Jose without a source, so the books disagree and the city is flagged for the A/B pass.",
             rounds=[rnd("2018-03-07", "Series A", 13500000, "e.ventures", True, VOI_A, "press")]))

# ---------------------------------------------------------------- Voltage (bitcoin infrastructure)
VOLT_SEED = NEWS("voltage", "Voltage Announces $6 Million Seed Round")
L.append(cls("voltage", status="private", rng="below_1b", country="US", city="Wichita", city_src="web_verified",
             focus="Crypto & Web3",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=VOLT_SEED, entry_date="2022-01",
             flags=("model_disputes_source",),
             note="Bitcoin and Lightning payment infrastructure (voltage.cloud). Disputes the pre-filled JP, a one-word "
                  "Wikidata join to a Japanese namesake: the seed release is datelined Wichita, Kansas. Entry: the $6M "
                  "seed of January 2022 led by Trammell Venture Partners with Craft Ventures, GV and others (the "
                  "company's release). Status: operating (a Lightning credit line launched February 2026). Momentum "
                  "check 2026-09-28 (Google News): no priced round at $1B or more; the '$2.5 billion' Voltage Park "
                  "headline is a different company. " + GRAD_LEFT,
             rounds=[rnd("2022-01-20", "Seed", 6000000, "Trammell Venture Partners", True, VOLT_SEED, "company")]))

# ---------------------------------------------------------------- Voltron Data
VD_CLOSE = "https://www.cs.cmu.edu/~pavlo/blog/2026/01/2025-databases-retrospective.html"
L.append(cls("voltron-data", status="defunct", rng="below_1b", country="US", city="Mountain View",
             focus="Data Infrastructure",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=VD_TC, entry_date="2022-02",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=VD_TC,
             note="GPU-accelerated Apache Arrow analytics (Theseus), Mountain View (aligned with Battery and Coatue). "
                  "Shut down: it announced its closure in late 2025 (Andy Pavlo's 2025 databases retrospective, CMU), "
                  "after halving its staff in 2024; defunct, aligned with Coatue's row (Battery and Lightspeed still "
                  "read private and are staler). Entry: GV was in the $22M seed led by BlackRock and Walden and in the "
                  "$88M Series A led by Walden Catalyst, announced together in February 2022 (TechCrunch); GV also "
                  "held Ursa Computing, whose team co-founded Voltron. Graduation: the named Series A.",
             rounds=[rnd("2022-02-17", "Seed", 22000000, "BlackRock and Walden", True, VD_TC, "press"),
                     rnd("2022-02-17", "Series A", 88000000, "Walden Catalyst", True, VD_TC, "press")]))

# ---------------------------------------------------------------- Vungle
VUN_SEED = "https://techcrunch.com/2012/05/02/vungle-hustles-its-way-into-2m-seed-round-from-all-star-investors-for-mobile-app-video-trailers/"
VUN_A = "https://techcrunch.com/2013/08/15/vungle-series-a/"
VUN_SALE = "https://techcrunch.com/2019/07/15/blackstone-is-acquiring-mobile-ad-company-vungle/"
L.append(cls("vungle", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="Media, Gaming & Advertising",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=VUN_SEED, entry_date="2012-05",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=VUN_A,
             note="In-app video advertising (AngelPad), San Francisco. Blackstone acquired it in July 2019 for a reported "
                  "$750M or more (TechCrunch). Entry: the $2M seed of May 2012 includes Google Ventures (TechCrunch). "
                  "Graduation: the $6.5M Series A led by Crosslink in August 2013 with Google Ventures participating "
                  "(TechCrunch); a $17M Series B followed in 2014.",
             rounds=[rnd("2012-05-02", "Seed", 2000000, None, True, VUN_SEED, "press"),
                     rnd("2013-08-15", "Series A", 6500000, "Crosslink Capital", True, VUN_A, "press")]))

# ---------------------------------------------------------------- Walker and Company
WAL_B = "https://techcrunch.com/2015/09/28/walker-company-brands-raises-24m-series-b-inks-bevel-deal-with-target/"
WAL_A = "https://techcrunch.com/2014/06/17/walker-co-6-9m-a16z/"
WAL_PG = "https://techcrunch.com/2018/12/12/procter-gamble-acquires-walker-company/"
L.append(cls("walker-and-company", status="acquired", rng="below_1b", country="US", city="Atlanta",
             city_src="web_verified", focus="Consumer & Marketplaces",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=WAL_B, entry_date="2015-09",
             note="Health and beauty products for people of color (Bevel). Procter & Gamble acquired it in December 2018 "
                  "and the team moved to Atlanta (TechCrunch), the last-known city. Entry: Google Ventures is named in "
                  "the $24M Series B of September 2015 led by IVP (TechCrunch); the $2.4M seed and the a16z-led $6.9M "
                  "Series A of June 2014 list no Google Ventures (TechCrunch), so GV entered at the B: Growth.",
             rounds=[rnd("2014-06-17", "Series A", 6900000, "Andreessen Horowitz", False, WAL_A, "press"),
                     rnd("2015-09-28", "Series B", 24000000, "Institutional Venture Partners", True, WAL_B, "press")]))

# ---------------------------------------------------------------- Waltz Health
WALTZ_FD = jl.FORMD_CITE("waltz-health", 0)   # the 2022-01-14 filing (Asset Blue Pharmacy Services, Inc.)
WALTZ_FD21 = jl.FORMD_CITE("waltz-health", 2)   # the 2021-08-24 filing
WALTZ_SALE = NEWS("waltz-health", "EVERSANA buys digital drug-price")
L.append(cls("waltz-health", status="acquired", rng="below_1b", city="Chicago", focus="Healthcare & Bio",
             stage="Series A", stage_src="formd_structural", stage_conf="medium", stage_cite=WALTZ_FD,
             entry_date="2022-01-14",
             note="AI-driven prescription drug marketplaces, Chicago. EVERSANA acquired it on 26 August 2025, with Waltz's "
                  "CEO Mark Thierer becoming EVERSANA's CEO (pharmaphorum, EVERSANA's own news site); the firm's exit "
                  "line agrees. Stage from the company's own Form D sequence (CIK 1880783, filing first as Asset Blue "
                  "Pharmacy Services, Inc.): a $3M equity round of August 2021 with only the founders as related "
                  "persons, then the $35M offering first sold 2022-01-14 with GV's Benjamin Robbins a director, filed "
                  "from Google's Cambridge office; one earlier filing and $35M under the 2022 Series A ceiling ($40M) "
                  "give Series A. It launched publicly with the $35M in April 2022. Replaces the pre-filled entry date "
                  "(2024-11-26, the later $20M filing); GV's 2022 post already lists Waltz among Ben Robbins's "
                  "investments.",
             rounds=[rnd("2021-08-24", "unnamed ($3M)", 3000000, None, False, WALTZ_FD21, "filing"),
                     rnd("2022-01-14", "unnamed ($35M offering)", 35000000, None, True, WALTZ_FD, "filing")]))

# ---------------------------------------------------------------- Wander (Days app)
WAN_SEED = "https://observer.com/2012/04/after-pitching-dinevore-for-a-year-founder-jeremy-fisher-snags-1-2-m-for-wander/"
WAN_SALE = "https://techcrunch.com/2014/02/11/yahoo-acquires-social-diary-company-wander-for-over-10m/"
L.append(cls("wander", status="acquired", rng="below_1b", city="New York", focus="Consumer & Marketplaces",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=WAN_SEED, entry_date="2012-04",
             note="Wander, the social diary app Days (TechStars NY 2012), New York. Yahoo acquired it in February 2014 for "
                  "a reported price above $10M and the team joined Yahoo's New York mobile group (TechCrunch). Entry: "
                  "the $1.2M seed of April 2012 from SV Angel, Google Ventures and others (the Observer); it was all "
                  "Wander ever raised (TechCrunch). Redpoint's 'wander' row is a different company (the vacation-home "
                  "network founded 2021): a name collision, not aligned. " + GRAD_LEFT,
             rounds=[rnd("2012-04-20", "Seed", 1200000, None, True, WAN_SEED, "press")]))

# ---------------------------------------------------------------- Warp (warp.dev)
WARP_TC = "https://techcrunch.com/2022/04/05/warp-raises-23m-to-build-a-better-terminal/"
WARP_POST = POST("warp-reinventing-command-line-terminal")
L.append(cls("warp", status="private", rng="below_1b", city="New York", city_src="formd_address",
             focus="DevTools & APIs",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=WARP_TC, entry_date="2020-06",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=WARP_TC,
             note="Warp (warp.dev), the Rust terminal turned agentic development environment, New York (the 2020 Form "
                  "D of Denver Technologies, Inc., Warp's legal name, gives 11 Prince Street, New York, with Erik "
                  "Nordlander a director). Entry: GV led the $6M seed (TechCrunch; the firm's own post: 'Shortly "
                  "thereafter, GV led Warp's seed financing'), first sold 2020-06-02 on that Form D. Graduation: the "
                  "$17M Series A led by Dylan Field, announced April 2022 (TechCrunch). Sequoia led a $50M Series B in "
                  "June 2023. Momentum check 2026-09-28 (Google News twice): no priced round at $1B or more. "
                  "Battery's and YC's 'warp' rows are a different company (the payroll startup): a name collision, not "
                  "aligned.",
             rounds=[rnd("2020-06-02", "Seed", 6000000, "GV", True, WARP_TC, "press"),
                     rnd("2022-04-05", "Series A", 17000000, "Dylan Field", None, WARP_TC, "press")]))

# ---------------------------------------------------------------- Watch Club
WC_TC = "https://techcrunch.com/2026/02/03/watch-club-microdrama-video-social-network/"
L.append(cls("watch-club", status="private", rng="below_1b", country="US", focus="Media, Gaming & Advertising",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=WC_TC, entry_date="2026-02",
             grad="censored", flags=("city_unknown",),
             note="Microdrama streaming app with a fan social network (watchclubtv.com; legal name Kino Technologies "
                  "Inc.), founded by a former Meta product manager. 'The idea alone was interesting enough to secure "
                  "seed funding led by GV' (TechCrunch, 3 February 2026). No source read places the company in a "
                  "city; US from its Inc. legal name. The entry is inside the 24-month window, so censored.",
             rounds=[rnd("2026-02-03", "Seed", None, "GV", True, WC_TC, "press")]))

jl.write("j14", L)
