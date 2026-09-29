"""PRO-75 GV grind, queue batch 10 (judge j10): 45 member rows, pager to ramp.
Each row researched from the firm's own posts and listings first, then S-1 tables, then press and Wikipedia.
Run: NQ_TAG=j10 python3 judgments-j10.py   (J10_DRY=1 writes the file without recording)."""
import importlib.util
import os
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, verdict, rnd, POST, CASE, SITE, ARCH, W, NEWS, FTS = (jl.cls, jl.verdict, jl.rnd, jl.POST, jl.CASE, jl.SITE,
                                                            jl.ARCH, jl.W, jl.NEWS, jl.FTS)
L = []
VW = {"valuation_range_source": "web_verified"}
GRAD_LEFT = "Graduation left for the graduation pass."

# ---------------------------------------------------------------- public rows, S-1 evidence
PBLS_CAP = "https://stockanalysis.com/stocks/pbls/market-cap/"
PBLS_S1 = FTS("Parabilis", "S-1")
FOG_B = NEWS("parabilis-medicines", "FogPharma Secures $66 Million")
L.append(cls("parabilis-medicines", status="public", rng="1b_plus", usd=4020000000, val_src="web_verified",
             val_cite=PBLS_CAP, asof="2026-09-28", extra=VW, city="Cambridge",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=FOG_B, entry_date="2018-05-16",
             flags=["stage_disputes_band"], focus="Healthcare & Bio",
             note="Parabilis Medicines (formerly FogPharma), Cambridge MA, helicon peptide cancer drugs; listed on Nasdaq "
                  "(PBLS) in June 2026. Market cap $4.02B as of 2026-09-28 (stockanalysis.com), fresher than the General "
                  "Catalyst row's $3.85B of 2026-09-25; same band. Entry: GV joined as a new investor in the $66M Series B "
                  "led by 6 Dimensions Capital (FogPharma's release, 2018-05-16), with Krishna Yeshwant joining the board. "
                  "The Form D band had dated the entry to the December 2020 Series C filing, a later round; the stage "
                  "(Growth) is unchanged, the entry date and source are corrected. The S-1 shows GV 2017, L.P. in the "
                  "Series E and GV 2019, L.P. in the Series F.",
             rounds=[rnd("2018-05-16", "Series B", 66000000, "6 Dimensions Capital", True, FOG_B, "company"),
                     rnd("2024-02", "Series E", 145000000, None, True, PBLS_S1, "filing"),
                     rnd("2026-01", "Series F", 305200000, None, True, PBLS_S1, "filing")]))

PRME_S1 = FTS("Prime Medicine", "S-1")
L.append(cls("prime-medicine", country="US", city="Cambridge", focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=PRME_S1, entry_date="2019-09",
             note="Prime Medicine, Cambridge MA, prime editing (Broad Institute, David Liu). Its S-1 (2022-09-23) lists GV "
                  "2019, L.P. buying 33,333,331 Series A preferred shares ($33.3M) in the Series A sold in closings of "
                  "September 2019, November 2020 and April 2021, and GV 2021, L.P. buying $24.0M of the $200M Series B; "
                  "the company had no round before the Series A (inception September 2019). Entry date is the Series A's "
                  "first closing. Market cap $511.47M on 2026-09-28 (stockanalysis.com), below $1B like the float on file.",
             rounds=[rnd("2019-09", "Series A", 115800000, None, True, PRME_S1, "filing"),
                     rnd("2021", "Series B", 200000000, None, True, PRME_S1, "filing")]))

# ---------------------------------------------------------------- Form D stage already known: status, city, band
L.append(cls("patientping", status="acquired", rng="below_1b", city="Boston", city_src="formd_address",
             focus="Healthcare & Bio",
             note="PatientPing, Boston, care-coordination notifications. Acquired by Appriss Health in 2021 (the firm's "
                  "exit line; press reported about $500M). Form D addresses (2015, 2016) are in Boston. The Form D band's "
                  "Series A entry (2015, Krishna Yeshwant as director) stands; a16z and Leerink led the $31.6M Series B in "
                  "December 2016."))

L.append(cls("pelage-pharmaceuticals", status="private", rng="below_1b", city="Los Angeles", city_src="formd_address",
             focus="Healthcare & Bio",
             note="Pelage Pharmaceuticals, Los Angeles (Form D address, Westwood), regenerative treatment for hair loss. "
                  "GV led the $16.75M Series A (February 2024) and the $14M Series A-1 (August 2024); a $120M Series B "
                  "followed in October 2025 with no valuation disclosed, so the row reads below $1B. The Form D band's "
                  "Series A entry agrees."))

L.append(cls("push-security", status="private", rng="below_1b", city="London", focus="Security",
             note="Push Security, London, identity and SaaS security. The firm's own post (2023-04-03) says GV led the $15M "
                  "Series A, which agrees with the Form D band; Redpoint led a $30M Series B in April 2025. No valuation "
                  "disclosed; below $1B."))

L.append(cls("quartet", status="acquired", rng="below_1b", city="New York", city_src="formd_address",
             focus="Healthcare & Bio",
             note="Quartet Health, New York, behavioral health care coordination. NeuroFlow acquired Quartet in January 2025 "
                  "after Quartet divested its telehealth assets (the firm's exit line 'Acquired by NueroFlow, 2025'; "
                  "Behavioral Health Business, 2025-01-30). Form D addresses are in New York."))

# ---------------------------------------------------------------- firm's own post decides the stage
QAI_POST = POST("q-ai-joins-apple")
QAI_TC = NEWS("q-ai", "as the AI race heats up")
QAI_GLOBES = NEWS("q-ai", "Behind the $2b Apple acquisition")
L.append(cls("q-ai", status="acquired", rng="below_1b", focus="AI & Applied AI", country="IL",
             country_src="web_verified", country_cite=QAI_TC, city="Tel Aviv",
             stage="Seed", stage_src="first_party", stage_conf="high", stage_cite=QAI_POST, entry_date="2022",
             grad="graduated", grad_src="first_party", grad_conf="high", grad_cite=QAI_POST,
             note="Q.ai, Israeli audio and silent-speech AI company (founders Aviad Maizels, Yonatan Wexler, Avi Barliya) "
                  "that worked in stealth. The firm's own post (2026-01-29): GV co-led Q's inception seed in 2022 with "
                  "Aleph and followed on in the Series A in 2023; Globes adds that Kleiner Perkins and Spark co-led that "
                  "Series A and places its early demos in Tel Aviv. Apple acquired Q.ai in January 2026 (TechCrunch, "
                  "2026-01-29; reported near $2B).",
             rounds=[rnd("2022", "Seed", None, "GV and Aleph", True, QAI_POST, "firm"),
                     rnd("2023", "Series A", None, "Kleiner Perkins and Spark", True, QAI_GLOBES, "press")]))

# ---------------------------------------------------------------- Wikipedia and press
PLAID_W = W("Plaid Inc.")
L.append(cls("plaid", rng="1b_plus", usd=8000000000, val_src="web_verified", val_cite=PLAID_W, asof="2026-02",
             extra=VW, city="San Francisco", focus="Fintech & Payments",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=PLAID_W, entry_date="2013",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=PLAID_W,
             flags=["model_disputes_source"],
             note="Plaid, San Francisco, bank-data APIs. Google Ventures was in the $2.8M seed of late 2013 with Spark "
                  "Capital and NEA (Wikipedia); NEA put in $12.5M in 2014 and Plaid announced a $250M Series C on "
                  "2018-12-11, a named later round. Valuation: the unicorn-list $13.4B is the April 2021 Series D; "
                  "the April 2025 round priced Plaid at $6.1B and a February 2026 employee share sale at $8B "
                  "(Wikipedia). Aligned to $8B (2026-02) as the Coatue, Ribbit and Spark rows carry; band 1b_plus.",
             rounds=[rnd("2013", "Seed", 2800000, None, True, PLAID_W, "press"),
                     rnd("2014", "unnamed", 12500000, "New Enterprise Associates", None, PLAID_W, "press"),
                     rnd("2018-12-11", "Series C", 250000000, "Mary Meeker", None, PLAID_W, "press"),
                     rnd("2021-04-07", "Series D", 425000000, None, None, PLAID_W, "press"),
                     rnd("2025", "unnamed", 575000000, "Franklin Templeton, Fidelity, BlackRock", None, PLAID_W, "press"),
                     rnd("2026-02", "employee share sale", None, None, None, PLAID_W, "press")]))

PER_W = W("Periscope (service)")
L.append(cls("periscope", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="Media, Gaming & Advertising", flags=["model_disputes_source"],
             stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=PER_W, entry_date="2014-04",
             note="Periscope, San Francisco live-video app (founded February 2014 as Bounty). Its only round was $1.5M in "
                  "April 2014 from Founder Collective, Maveron, Google Ventures, Menlo Ventures, Bessemer and others "
                  "(Wikipedia); Menlo's own page labels that round Seed. Twitter bought it in January 2015 before launch "
                  "and shut the app in March 2021. The Wikidata GR country was a one-word-name join; the company was "
                  "American. " + GRAD_LEFT,
             rounds=[rnd("2014-04", "Seed", 1500000, None, True, PER_W, "press")]))

PIN_W = W("Pindrop Security")
L.append(cls("pindrop", status="private", rng="below_1b", city="Atlanta", focus="Security",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=PIN_W, entry_date="2016",
             note="Pindrop, Atlanta, voice fraud detection and authentication. Wikipedia: Google Capital led the $75M Series "
                  "C in 2016 with Andreessen Horowitz, GV and others (both Google units in one round); GV was not named "
                  "in the 2013 Series A (a16z, Citi Ventures) or the February 2015 Series B (IVP). The firm's /ai list "
                  "shows GV re-investing in November 2018 (the $90M round). No priced round at $1B or more on record; "
                  "below $1B as the a16z, Felicis and IVP rows carry.",
             rounds=[rnd("2013-06", "Series A", 11000000, "Andreessen Horowitz and Citi Ventures", False, PIN_W, "press"),
                     rnd("2015-02", "Series B", 35000000, "Institutional Venture Partners", False, PIN_W, "press"),
                     rnd("2016", "Series C", 75000000, "Google Capital", True, PIN_W, "press"),
                     rnd("2018-11", "re-investment", None, None, True, SITE("pindrop"), "firm")]))

PEER_B = NEWS("peerspace", "GV leads $16 million")
L.append(cls("peerspace", status="private", rng="below_1b", city="San Francisco", focus="Consumer & Marketplaces",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=PEER_B, entry_date="2018-07-18",
             note="Peerspace, San Francisco marketplace for renting venues and meeting spaces. GV led the $16M Series B "
                  "(VentureBeat, 2018-07-18) with Foundation Capital and Red Bridge Partners; Peerspace had raised about "
                  "$19M before, and the firm's listing first carries it in 2018. Still operating (new venue product, "
                  "September 2026); no valuation disclosed.",
             rounds=[rnd("2018-07-18", "Series B", 16000000, "GV", True, PEER_B, "press")]))

PAN_BI = NEWS("pangea", "CrowdStrike Buys Pangea for")
L.append(cls("pangea", status="acquired", rng="below_1b", country="US", city="Palo Alto", focus="Security",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=PAN_BI, entry_date="2022-08",
             note="Pangea, Silicon Valley security APIs and AI guardrails, founded 2021. BankInfoSecurity (2025-09-18): it "
                  "raised $51M in all, most recently a $26M Series B in November 2022 led by GV; the firm's /ai list dates "
                  "GV's first investment to August 2022, the entry date. CrowdStrike agreed to buy Pangea for about $260M "
                  "in September 2025; the firm's exit line reads 'Acquired by CrowdStrike, 2026'.",
             rounds=[rnd("2022-11", "Series B", 26000000, "GV", True, PAN_BI, "press")]))

PAN_SEED = NEWS("panorama-education", "Zuckerberg makes his first ed tech")
PAN_C = NEWS("panorama-education", "Series C Funding Led by General Atlantic")
L.append(cls("panorama-education", status="private", rng="below_1b", country="US", city="Boston", focus="SaaS",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=PAN_SEED, entry_date="2013-10",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=PAN_C,
             note="Panorama Education, Boston (founded in Cambridge MA), survey and analytics software for schools. "
                  "Boston.com (2013-10-21): $4M seed co-led by Startup:Education and SoftTech VC with Google Ventures, "
                  "A-Grade Investments and Yale. General Atlantic led a $60M Series C on 2021-09-02, a named later round. "
                  "No priced round at $1B or more; below $1B as the a16z, General Catalyst and Spark rows carry.",
             rounds=[rnd("2013-10-21", "Seed", 4000000, "Startup:Education and SoftTech VC", True, PAN_SEED, "press"),
                     rnd("2021-09-02", "Series C", 60000000, "General Atlantic", None, PAN_C, "press")]))

PARS_C = NEWS("parsable", "Parsable secures $40M")
PARS_ACQ = NEWS("parsable", "CAI Software, LLC Acquires Parsable")
L.append(cls("parsable", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="Industrial & Robotics", stage="undetermined",
             note="Parsable, San Francisco connected-worker software for factories. CAI Software (an STG company) acquired "
                  "it on 2024-09-25 (newswire.com release). GV's entry round is not on record: the $40M Series C of May "
                  "2018 (Future Fund lead, with B37, Lightspeed, Airbus Ventures, Aramco Ventures; TechCrunch) names no "
                  "GV, and the firm's listing first carries Parsable in 2019.",
             rounds=[rnd("2018-05-16", "Series C", 40000000, "Future Fund", False, PARS_C, "press")]))

# ---------------------------------------------------------------- momentum-slice helper (COLLECTION.md s6): a below_1b
# private row in a hot sector records its dated check with the latest round's citation.
CHECK = "2026-09-28"


def MOM(url):
    return {"valuation_range_source": "web_verified", "valuation_citation": url, "valuation_asof": CHECK}


POD_A = NEWS("podium", "Podium Receives $32 Million Series A")
POD_D = "https://www.pymnts.com/news/investment-tracker/2021/podium-closes-201m-series-d-funding-deal/"
POD_B = "https://www.ivp.com/content/podium-broadcasting-greatness/"
L.append(cls("podium", rng="1b_plus", usd=3000000000, val_src="web_verified", val_cite=POD_D, asof="2021-11",
             extra=VW, flags=["stale", "model_disputes_source"], city="Lehi", focus="SaaS",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=POD_A, entry_date="2017-05-11",
             note="Podium, Lehi UT, messaging, reviews and payments software for local businesses. Summit Partners' "
                  "release (2017-05-11): $32M Series A led by Accel with Summit Partners, GV and previous investor Y "
                  "Combinator, so GV entered at the Series A; IVP's post on its $60M Series B (2018-06-07) names GV "
                  "among the existing investors. Valuation: the unicorn-list $1.5B is the 2020 mark; the $201M Series D "
                  "of November 2021 priced Podium at $3B (PYMNTS), as the Accel, IVP and Y Combinator rows carry; no "
                  "priced round since, so stale.",
             rounds=[rnd("2017-05-11", "Series A", 32000000, "Accel", True, POD_A, "firm"),
                     rnd("2018-06-07", "Series B", 60000000, "IVP", True, POD_B, "firm"),
                     rnd("2021-11-15", "Series D", 201000000, "YC Continuity", None, POD_D, "press")]))

PH_STORY = "https://posthog.com/handbook/story"
L.append(cls("posthog", status="private", rng="1b_plus", usd=1400000000, val_src="web_verified", val_cite=PH_STORY,
             asof="2025-10", extra=VW, country="US", city="San Francisco", focus="DevTools & APIs",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=PH_STORY, entry_date="2020-12",
             note="PostHog, open-source product analytics for engineers. The company's own history page: $3.025M seed "
                  "(April 2020, YC Continuity and 1984 Ventures), then a $9M Series A in December 2020 led by GV (the "
                  "firm's post of 2020-12-17 says the same), a $15M Series B led by YC (June 2021), a $70M Series D led "
                  "by Stripe at about $920M with GV participating (June 2025) and a $75M Series E led by Peak XV at about "
                  "$1.4B (announced 2025-09-30). Momentum check 2026-09-28 (Google News on valuation and raises): no "
                  "later priced round; $1.4B as the Y Combinator row carries.",
             rounds=[rnd("2020-04", "Seed", 3025000, "YC Continuity and 1984 Ventures", False, PH_STORY, "company"),
                     rnd("2020-12", "Series A", 9000000, "GV", True, PH_STORY, "company"),
                     rnd("2021-06", "Series B", 15000000, "Y Combinator", None, PH_STORY, "company"),
                     rnd("2025-06", "Series D", 70000000, "Stripe", True, PH_STORY, "company"),
                     rnd("2025-10", "Series E", 75000000, "Peak XV", None, PH_STORY, "company")]))

PEC_C = NEWS("pecan-ai", "Pecan AI raises $66 million from Insight Partners, Google")
L.append(cls("pecan-ai", status="private", rng="below_1b", extra=MOM(PEC_C), country="IL", country_src="web_verified",
             country_cite=PEC_C, city="Ramat Gan", focus="AI & Applied AI",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=PEC_C, entry_date="2021-11",
             note="Pecan AI, Israeli predictive-analytics software. Calcalist (2022-02-02): $66M Series C led by Insight "
                  "Partners with GV as a new investor, after a $35M Series B led by GGV in May 2021; the firm's /ai list "
                  "dates GV's investment to November 2021 (the entry date). City aligned with the Insight Partners row. "
                  "Momentum check 2026-09-28 (Google News on raises and valuation): no round after the Series C, layoffs "
                  "in 2023 and 2024; no priced mark at or above $1B.",
             rounds=[rnd("2021-05", "Series B", 35000000, "GGV Capital", False, PEC_C, "press"),
                     rnd("2022-02-02", "Series C", 66000000, "Insight Partners", True, PEC_C, "press")]))

PIX_A = NEWS("pixie-labs", "Pixie Labs raises $9.15M Series A")
L.append(cls("pixie-labs", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="DevTools & APIs",
             stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=PIX_A, entry_date="2018-10",
             note="Pixie Labs, San Francisco, Kubernetes observability. TechCrunch and the company's release (2020-10-01): "
                  "$9.15M Series A led by Benchmark with participation from GV, announced as it left stealth; neither "
                  "names an earlier round. The firm's /ai list dates GV's only investment to October 2018, so the Series A "
                  "most likely closed in stealth then (entry date from the firm, D7); confidence medium because a 2018 seed "
                  "cannot be ruled out from these pages. New Relic acquired Pixie in December 2020.",
             rounds=[rnd("2020-10-01", "Series A", 9150000, "Benchmark", True, PIX_A, "press")]))

PHY_56 = NEWS("physna", "Physna tops $86M funding")
PHY_B = NEWS("physna", "Sequoia Leads $20M Series B in Physna")
L.append(cls("physna", status="private", rng="below_1b", extra=MOM(PHY_56), country="US", city="Cincinnati",
             focus="AI & Applied AI",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=PHY_56, entry_date="2021-07-02",
             note="Physna, Cincinnati, geometric deep-learning search for 3D models. Drive Capital led the 2019 Series A "
                  "and Sequoia the $20M Series B of January 2021 (the release names no GV); Develop3D (2021-07-02): a $56M "
                  "round led by Tiger Global with GV and Sequoia, taking the total to $86M, so GV entered after the Series "
                  "B. Shapeways took control of Thangs, the 3D community Physna's search powers, in December 2024; Physna "
                  "continues with its B2B and government products (Develop3D). Momentum check 2026-09-28 (Google News): "
                  "no round after July 2021; no priced mark at or above $1B.",
             rounds=[rnd("2021-01-29", "Series B", 20000000, "Sequoia Capital", False, PHY_B, "company"),
                     rnd("2021-07-02", "Series B", 56000000, "Tiger Global", True, PHY_56, "press")]))

PHO_SEED = NEWS("phoebe", "Phoebe Secures $17M Seed Funding")
L.append(cls("phoebe", status="private", rng="below_1b", extra=MOM(PHO_SEED), country="GB", country_src="web_verified",
             country_cite=PHO_SEED, city="London", focus="AI & Applied AI",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=PHO_SEED, entry_date="2025-08",
             grad="censored",
             note="Phoebe, London, AI agents that find and fix software failures. $17M seed led by GV and Cherry Ventures "
                  "(StartupHub.ai and tech.eu, 2025-08-20); the firm's /ai list dates GV's investment to August 2025. "
                  "Censored: the seed is under 24 months old. Momentum check 2026-09-28 (Google News): no round after "
                  "the seed; no priced mark at or above $1B.",
             rounds=[rnd("2025-08-20", "Seed", 17000000, "GV and Cherry Ventures", True, PHO_SEED, "press")]))

POL_TC = NEWS("polar-signals", "Polar Signals wants to help companies cut cloud costs")
POL_ACQ = NEWS("polar-signals", "Dash0 Acquires Berlin Tech Company")
L.append(cls("polar-signals", status="acquired", rng="below_1b", country="DE", country_src="web_verified",
             country_cite=POL_ACQ, city="Berlin", focus="DevTools & APIs",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=POL_TC, entry_date="2021",
             note="Polar Signals, Berlin, continuous profiling for cloud software. TechCrunch (2024-03-12): the seed opened "
                  "in 2021 with $4M from GV and Lightspeed, and a further $6.8M came in 2024 from GV, Spark and "
                  "Lightspeed ($10.8M in all); the company is incorporated in the US but run from Berlin, where its "
                  "founder and CEO is based. Dash0 acquired it in August 2026 (Business Insider: 'Dash0 Acquires Berlin "
                  "Tech Company'; the firm's exit line 'Acquired by Dash0, 2026'); fresher than the Spark and "
                  "Lightspeed rows, which still read private. " + GRAD_LEFT,
             rounds=[rnd("2021", "Seed", 4000000, None, True, POL_TC, "press"),
                     rnd("2024-03-12", "unnamed", 6800000, None, True, POL_TC, "press")]))

RAMP_E2 = NEWS("ramp", "Ramp Raises $500 Million at $22.5 Billion")
RAMP_W = W("Ramp (company)")
L.append(cls("ramp", rng="10b_plus", usd=44000000000, val_src="web_verified", val_cite=RAMP_W, asof="2026-06",
             extra=VW, flags=["model_disputes_source"], city="New York", focus="Fintech & Payments",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=RAMP_E2, entry_date="2025-07-30",
             note="Ramp, New York, corporate cards and finance automation. Ramp's release (2025-07-30): $500M at a $22.5B "
                  "valuation led by ICONIQ, with GV among the new investors (Latham names the round Series E-2); the "
                  "firm's /ai list dates GV's first investment to July 2025. Valuation: the unicorn-list $32B is November "
                  "2025; in June 2026 Ramp raised $750M at $44B (Wikipedia), as most sibling rows carry. Momentum check "
                  "2026-09-28 (Google News on the valuation): September 2026 reports of talks at $60B are not a priced "
                  "round, so $44B stands.",
             rounds=[rnd("2025-07-30", "Series E-2", 500000000, "ICONIQ", True, RAMP_E2, "company"),
                     rnd("2026-06", "Series F", 750000000, "ICONIQ Growth, GIC, Ontario Teachers'", None, RAMP_W, "press")]))

QUAD_TC = "https://techcrunch.com/2024/04/02/quadratic-is-reimagining-the-spreadsheet-with-a-focus-on-data/"
L.append(cls("quadratic", status="private", rng="below_1b", extra=MOM(QUAD_TC), country="US", city="Boulder",
             city_src="web_verified", focus="SaaS",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=QUAD_TC, entry_date="2023-08",
             note="Quadratic, Boulder CO, a spreadsheet with Python, SQL and AI for data work. TechCrunch and the "
                  "company's own post (2024-04-02): $5.6M seed led by GV with Catapult Ventures, Betaworks and The Fund "
                  "Rockies; the firm's /ai list dates GV's investment to August 2023 (the entry date). Check 2026-09-28 "
                  "(Google News and one web search): no later round reported; no priced mark at or above $1B. " + GRAD_LEFT,
             rounds=[rnd("2023-08", "Seed", 5600000, "GV", True, QUAD_TC, "press")]))

PRU_SEED = NEWS("prudentia-sciences", "Wilson Sonsini Advises Prudentia Sciences")
PRU_A = NEWS("prudentia-sciences", "Prudentia Sciences: $20 Million Series A")
L.append(cls("prudentia-sciences", status="private", rng="below_1b", country="US", focus="Healthcare & Bio",
             flags=["city_unknown"],
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=PRU_SEED, entry_date="2024-10",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=PRU_A,
             note="Prudentia Sciences, AI diligence software for life-sciences dealmaking. Wilson Sonsini (2025-01-09): "
                  "Google Ventures led the $7M financing with Iaso Ventures and Virtue as the company left stealth; Pulse "
                  "2.0 calls it the 2024 seed. The firm's /ai list dates GV's investment to October 2024. McKesson "
                  "Ventures led the $20M Series A with GV following (Pulse 2.0, 2026-01-08), a named later round. No "
                  "source read places the company in a city.",
             rounds=[rnd("2024-10", "Seed", 7000000, "GV", True, PRU_SEED, "press"),
                     rnd("2026-01-06", "Series A", 20000000, "McKesson Ventures", True, PRU_A, "press")]))

PRE_A = NEWS("pretzel-therapeutics", "Mitochondrial drugs, with a twist")
L.append(cls("pretzel-therapeutics", status="private", rng="below_1b", country="US", city="Waltham",
             focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=PRE_A, entry_date="2022-09-12",
             note="Pretzel Therapeutics, Waltham MA (research site in Gothenburg), mitochondrial medicines. BioPharma Dive "
                  "(2022-09-12): launched with a $72.5M Series A, ARCH and Mubadala Capital putting in $15M each, with "
                  "GV, Invus and Angelini Ventures in the round. No later priced round seen; below $1B.",
             rounds=[rnd("2022-09-12", "Series A", 72500000, "ARCH Venture Partners and Mubadala Capital", True, PRE_A,
                         "press")]))

PER_A = NEWS("perceive-bio", "Perceive Pharma Attracts $15M Series A")
L.append(cls("perceive-bio", status="private", rng="below_1b", country="US", city="South San Francisco",
             city_src="web_verified", focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=PER_A, entry_date="2025-02-18",
             note="Perceive Bio (perceivebio.com, 6000 Shoreline Drive, South San Francisco), neuroprotective eye "
                  "therapies. PR Newswire (2025-02-18): Perceive Pharma, spun out of Perceive Biotherapeutics, raised a "
                  "$15M Series A led by Deerfield with J&J Innovation, Braidwell, GV, the Retinal Degeneration Fund and "
                  "Catalio. The firm's listing was created nine days later with both GV partners; confidence medium only "
                  "because the listing's name and site are the parent brand's.",
             rounds=[rnd("2025-02-18", "Series A", 15000000, "Deerfield Management", True, PER_A, "company")]))

PUP_C = "https://techcrunch.com/2011/11/29/cisco-google-ventures-vmware-put-8-5m-in-data-center-automation-startup-puppet-labs/"
L.append(cls("puppet-labs", status="acquired", rng="below_1b", country="US", city="Portland", focus="DevTools & APIs",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=PUP_C, entry_date="2011-11-29",
             note="Puppet Labs (later Puppet), Portland OR, infrastructure automation. TechCrunch (2011-11-29): $8.5M "
                  "Series C led by Cisco, Google Ventures and VMware, all new investors, with existing investors Kleiner "
                  "Perkins, True Ventures and Radar Partners. Perforce acquired Puppet in April 2022 (Wikipedia).",
             rounds=[rnd("2011-11-29", "Series C", 8500000, "Cisco, Google Ventures, VMware", True, PUP_C, "press"),
                     rnd("2018-06", "unnamed", 42000000, "Cisco", None, W("Puppet (software)"), "press")]))

PG_F = "https://fortune.com/2015/05/13/sequoia-plangrid-funding-blueprints/"
PG_B = "https://techcrunch.com/2015/11/18/plangrid-lands-40-million-investment-to-expand-product/"
L.append(cls("plangrid", status="acquired", rng="below_1b", city="San Francisco", focus="SaaS",
             stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=PG_F, entry_date="2012",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=PG_F,
             note="PlanGrid, San Francisco construction software (YC W12). Fortune (2015-05-13): while still in the "
                  "accelerator the startup raised 'a small initial funding round of $1.5 million' from Sam Altman, Paul "
                  "Buchheit, 500 Startups and Google Ventures, the seed TechCrunch reported in May 2012; then $18M led by "
                  "Sequoia (May 2015, Series A per Wikipedia), a later priced round far above the seed. Tenaya led a $40M "
                  "round in November 2015. Autodesk bought PlanGrid for $875M in December 2018.",
             rounds=[rnd("2012", "Seed", 1500000, None, True, PG_F, "press"),
                     rnd("2015-05-13", "Series A", 18000000, "Sequoia Capital", None, PG_F, "press"),
                     rnd("2015-11-18", "Series B", 40000000, "Tenaya Capital", False, PG_B, "press")]))

PLX_35 = NEWS("plexxi", "Plexxi Raises $35 Million")
PLX_GV = NEWS("plexxi", "GV invests in networking startup Plexxi")
L.append(cls("plexxi", status="acquired", rng="below_1b", country="US", city="Nashua", focus="Data Infrastructure",
             stage="Growth", stage_src="model", stage_conf="medium", stage_cite=PLX_GV, entry_date="2016-01",
             note="Plexxi, Nashua NH, data-center networking. Its release of 2015-09-14: a $35M round led by an unnamed "
                  "new investor with Lightspeed, Matrix and North Bridge, bringing the total to $83M; ZDNet's headline of "
                  "2016-01-20 reports GV investing in Plexxi. Either way GV came in after the company's earlier rounds "
                  "(total already $83M), so the entry is a later-stage round: Growth, confidence medium because no page "
                  "read names GV's round. HPE acquired Plexxi in 2018.",
             rounds=[rnd("2015-09-14", "unnamed", 35000000, "unnamed new investor", None, PLX_35, "company"),
                     rnd("2016-01-20", "unnamed", None, None, True, PLX_GV, "press")]))

POY_TC = "https://techcrunch.com/2014/10/29/former-google-wallet-head-launches-poynt-a-future-proofed-payment-terminal/"
POY_GN = "https://www.globenewswire.com/en/news-release/2014/10/29/955657/0/en/Poynt-Introduces-World-s-First-Smart-Payment-Terminal.html"
POY_B = "https://venturebeat.com/business/former-google-exec-raises-28m-to-start-shipping-his-smart-payment-terminals"
L.append(cls("poynt", status="acquired", rng="below_1b", country="US", city="Palo Alto", focus="Fintech & Payments",
             stage="undetermined",
             note="Poynt, Palo Alto, smart payment terminals (founder Osama Bedier, ex-Google Wallet). At launch "
                  "(2014-10-29) TechCrunch reported a Series A led by Matrix Partners with Webb Investment Network and "
                  "Nyca, size undisclosed, and the company's own release lists Google Ventures among its backers; neither "
                  "ties GV to a named round, and no earlier round is reported. Oak HC/FT led the $28M Series B "
                  "(2015-10-22, no GV named). GoDaddy acquired Poynt (announced December 2020, about $365M).",
             rounds=[rnd("2014-10-29", "Series A", None, "Matrix Partners", None, POY_TC, "press"),
                     rnd("2015-10-22", "Series B", 28000000, "Oak HC/FT", None, POY_B, "press")]))

L.append(cls("product-hunt", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="Consumer & Marketplaces", stage="undetermined",
             note="Product Hunt, San Francisco product-discovery community (YC S14). The firm listed it from September "
                  "2014 with Kevin Rose as partner. Its only priced round was the $6.1M Series A led by Andreessen "
                  "Horowitz in October 2014 (Wikipedia); the investor lists reported for it do not name Google Ventures, "
                  "so GV's round is not on record. AngelList acquired Product Hunt in 2016.",
             rounds=[rnd("2014-10", "Series A", 6100000, "Andreessen Horowitz", None, W("Product Hunt"), "press")]))

PEN_C = NEWS("pensando", "Pensando Emerges From Stealth")
L.append(cls("pensando", status="acquired", rng="below_1b", country="US", city="Milpitas", focus="Data Infrastructure",
             stage="undetermined",
             note="Pensando Systems, edge and cloud networking silicon and software. Its release (2019-10-16, datelined "
                  "San Jose): up to $145M Series C led by HPE and Lightspeed with Goldman Sachs and Equinix, after a $71M "
                  "Series A and a $62M Series B; GV is not named, and the firm's listing first carries Pensando in 2020, "
                  "so GV's round (an extension or a later round) is not on record. AMD acquired Pensando in 2022 (about "
                  "$1.9B). City aligned with the Lightspeed row.",
             rounds=[rnd("2019-10-16", "Series C", 145000000, "Hewlett Packard Enterprise and Lightspeed", False, PEN_C,
                         "company")]))

L.append(cls("percolata", status="unknown", rng="below_1b", country="US", city="Palo Alto", city_src="formd_address",
             focus="SaaS", stage="undetermined",
             note="Percolata, Palo Alto, in-store traffic analytics for retailers; on the firm's listing from 2015 "
                  "(partner Shanna Tellerman). Its Form D of 2017-01-18 (CIK 1696887) reports $9.57M sold of a $14.6M "
                  "equity offering from Palo Alto, with no GV partner among the directors. No source read gives its fate "
                  "after 2017 (Google News returns nothing), so status unknown, as the a16z row carries; GV's round is "
                  "not on record.",
             rounds=[]))

QUE_G = NEWS("quettra", "SimilarWeb buys US co Quettra")
L.append(cls("quettra", status="acquired", rng="below_1b", country="US", focus="SaaS", flags=["city_unknown"],
             stage="undetermined",
             note="Quettra, a Silicon Valley mobile-app analytics and targeting startup of ex-Google, eBay and Microsoft "
                  "staff; SimilarWeb bought it for about $10M (Globes, 2015-12-10). On the firm's listing from 2014 "
                  "(partner M.G. Siegler); no source read names its rounds or its city.",
             rounds=[]))

PREM_FD = "https://www.sec.gov/Archives/edgar/data/1653395/000165339515000001/0001653395-15-000001-index.htm"
PREM_E = NEWS("premise", "Premise Data Raises $85 Million")
L.append(cls("premise", status="private", rng="below_1b", city="San Francisco", city_src="formd_address",
             focus="Data Infrastructure", stage="undetermined", flags=["stage_disputes_band"],
             extra={"entry_stage_source": None, "entry_stage_confidence": None, "entry_stage_citation": None,
                    "entry_date": None},
             note="Premise Data, San Francisco, crowdsourced market and ground-truth data. The Form D band dated GV's entry "
                  "to the September 2015 filing (about $50M, Karim Faris a director), but the firm's own listing on "
                  "googleventures.com already carried Premise in May 2013, so that round was a follow-on and the entry "
                  "round is not on record: stage undetermined (disputes the band). WestCap led an $85M Series E in "
                  "January 2021 (release names no GV). No valuation disclosed; below $1B.",
             rounds=[rnd("2015-09-11", "unnamed", 49999996, None, True, PREM_FD, "filing"),
                     rnd("2021-01-13", "Series E", 85000000, "WestCap", None, PREM_E, "company")]))

POH_B = NEWS("peopleone-health", "GV, Glen Tullman back PeopleOne")
L.append(cls("peopleone-health", status="private", rng="below_1b", city="Pittsburgh", focus="Healthcare & Bio",
             note="PeopleOne Health, employer-sponsored primary-care clinics, Pittsburgh area (Form D address in Oakmont, "
                  "PA; press calls it Pittsburgh-based). GV and Glen Tullman backed its $32M Series B (MobiHealthNews, "
                  "2024-10-25), which agrees with the Form D band's Growth entry. In September 2025 it closed its "
                  "Pennsylvania clinics to focus on Florida, where it still operates (Boca Raton, December 2025).",
             rounds=[rnd("2024-10-25", "Series B", 32000000, None, True, POH_B, "press")]))

PART_W = W("Partiful")
L.append(cls("partiful", status="private", rng="below_1b", country="US", city="New York",
             focus="Consumer & Marketplaces",
             stage="Seed", stage_src="model", stage_conf="low", entry_date="2021", flags=["stage_uncited"],
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=PART_W,
             note="Partiful, New York, event invitations app. The firm's own case study gives 'Date Invested: 2021', a year "
                  "before the company's first named round, the $20M Series A of 2022 led by Andreessen Horowitz "
                  "(Wikipedia; Business Insider, 2022-11-07); GV therefore entered at the seed stage, but no page read "
                  "names that round, so the stage is uncited (confidence low). The Series A is the cited later round.",
             rounds=[rnd("2021", "seed-stage round", None, None, True, CASE("partiful"), "firm"),
                     rnd("2022", "Series A", 20000000, "Andreessen Horowitz", None, PART_W, "press")]))

# ---------------------------------------------------------------- stealth codenames: company cannot be named
for q in ("q1", "q2"):
    L.append(cls(q, status="private", rng="undetermined", stage="undetermined", grad="undetermined",
                 country="US", focus="Healthcare & Bio",
                 flags=["identity_unresolved", "city_unknown", "model_disputes_source"],
                 extra={"valuation_usd": None, "valuation_source": None, "valuation_range_source": None,
                        "valuation_asof": None, "valuation_confidence": None, "is_public": False,
                        "public_since": None},
                 note=f"'{q.upper()}' on the firm's portfolio (Life Sciences), created 2025-12-03 minutes apart from its "
                      "twin, with no website and venture partner Sridhar Ramaswamy (GV's entrepreneur in residence for new "
                      "medical companies): a stealth company under a codename, so the company cannot be named. The "
                      "pre-filled values were one-word-name joins and are removed: Q2 had taken Q2 Holdings' SEC float "
                      "(public since 2014, $5.8B) and Q1 a German Wikidata country. Listed as a current holding, so "
                      "private; country read as the US from the firm's life-sciences practice, not from a source."))

# ---------------------------------------------------------------- last rows
PAR_A = NEWS("paradigm-health", "US-based Paradigm closes $203 million Series A")
PAR_B = NEWS("paradigm-health", "Raises $78 Million Series B")
L.append(cls("paradigm-health", status="private", rng="below_1b", country="US", city="Columbus", city_src="web_verified",
             focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=PAR_A, entry_date="2023-01",
             note="Paradigm Health, clinical-trials platform that brings research into routine care. Jawlah (2023-01-30): "
                  "$203M Series A led by ARCH Venture Partners and General Catalyst, which incubated it, with Mubadala "
                  "Capital, F-Prime Capital, GV and Lux Capital; a $78M Series B followed in December 2025 with the "
                  "purchase of Flatiron Health's clinical-research business, no valuation disclosed. City: the company's "
                  "own site gives 175 S. 3rd St, Columbus OH, and the December 2025 press calls it a Columbus startup; "
                  "fresher than the New York the 2023 coverage and the General Catalyst row carry.",
             rounds=[rnd("2023-01", "Series A", 203000000, "ARCH Venture Partners and General Catalyst", True, PAR_A,
                         "press"),
                     rnd("2025-12-04", "Series B", 78000000, None, None, PAR_B, "company")]))

L.append(cls("pager", status="unknown", rng="below_1b", city="New York", focus="Consumer & Marketplaces",
             stage="undetermined",
             note="Pager (pager.xyz), a New York consumer app that turns screenshots into shareable, clickable pages; on "
                  "the firm's list since 2023 with M.G. Siegler. Not the New York health-navigation company Pager (Pager "
                  "Health) in the Lux Capital book. Homebrew's post title reports a $5.2M seed in November 2022 and search "
                  "summaries say GV led it, but no page read ties GV to a named round (the Homebrew post now returns 404; "
                  "WIRED and Medium refuse reading). Status unknown: the company site no longer resolves (checked "
                  "2026-09-28, the domain keeps only mail records) and no news since 2022, though the firm still lists it.",
             rounds=[rnd("2022-08-01", "Seed", None, None, None, "https://gen.xyz/blog/pagerxyz", "vendor")]))

PARSE_A = "https://techcrunch.com/2011/11/09/parse-the-heroku-for-mobile-raises-5-5-million-series-a/"
L.append(cls("parse", rng="below_1b", city="San Francisco", focus="DevTools & APIs", stage="undetermined",
             note="Parse, San Francisco mobile backend-as-a-service (YC S11); Facebook bought it in April 2013 (the "
                  "firm's exit line 'Acquired by Facebook, 2013') and shut the service in January 2017. TechCrunch "
                  "(2011-11-09): $1.5M earlier from Y Combinator and angels, then a $5.5M Series A led by Ignition "
                  "Partners; neither names Google Ventures, which listed Parse by May 2013, so GV's round is not on record.",
             rounds=[rnd("2011", "Seed", 1500000, None, None, PARSE_A, "press"),
                     rnd("2011-11-09", "Series A", 5500000, "Ignition Partners", None, PARSE_A, "press")]))

PAY_14 = NEWS("payrange", "PayRange announces $2.7M round")
PAY_15 = NEWS("payrange", "PayRange raises $12M to install")
PAY_RV = NEWS("payrange", "Private Equity Firm Ridgeview Buys PayRange")
L.append(cls("payrange", status="acquired", rng="below_1b", country="US", city="Portland", focus="Fintech & Payments",
             stage="undetermined",
             note="PayRange, Portland OR, mobile payments for vending machines and laundromats; on the firm's list from "
                  "September 2014 (Kevin Rose). Rounds on record: $2.7M in August 2014, $12M in June 2015 (GeekWire "
                  "headlines) and $70M in 2020; the articles could not be read, so GV's round is not established. "
                  "Private-equity firm Ridgeview Partners bought PayRange in September 2024 (Bloomberg headline; the "
                  "firm's exit line 'Acquired by Ridgeview Partners, 2024').",
             rounds=[rnd("2014-08-13", "unnamed", 2700000, None, None, PAY_14, "press"),
                     rnd("2015-06-25", "unnamed", 12000000, None, None, PAY_15, "press")]))

L.append(cls("periscope-data", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="Data Infrastructure", stage="undetermined",
             note="Periscope Data, San Francisco SQL analytics and visualization. Sisense acquired it in May 2019 "
                  "(Globes: about $100M; the founder later put it at $130M). On the firm's list from 2016; no source read "
                  "names its rounds or GV's round.",
             rounds=[]))

POCKET_TC = "https://techcrunch.com/2011/07/26/read-it-later-raises-2-5-million-wants-to-become-the-dropbox-of-content/"
L.append(cls("pocket", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="Consumer & Marketplaces", stage="undetermined",
             note="Pocket (Read It Later until 2012), San Francisco save-for-later app. TechCrunch (2011-07-26): a $2.5M "
                  "round, the company's first external funding, led by Foundation Capital with Baseline Ventures, Google "
                  "Ventures and Founder Collective; the article gives it no round name, so the stage is undetermined "
                  "though the round is known. A $5M round followed in 2012 (Wikipedia). Mozilla acquired Pocket in "
                  "February 2017 and shut the service on 2025-07-08. Not the Pocket rows in the Accel and Y Combinator "
                  "books, which are other companies.",
             rounds=[rnd("2011-07-26", "unnamed (first external funding)", 2500000, "Foundation Capital", True,
                         POCKET_TC, "press"),
                     rnd("2012", "unnamed", 5000000, None, None, W("Pocket (service)"), "press")]))

RECORD = os.environ.get("J10_DRY") != "1"
jl.write("j10", L, record=RECORD)
