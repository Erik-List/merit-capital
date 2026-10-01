"""A/B pass ab1a, part 2 (PRO-99 Kleiner Perkins; COLLECTION.md s7, s8 duty 1, verify rule 4), 2026-09-30.

The private $1B+ rows flock-safety .. interos of queue/ab1.json (the first 37 slugs end at interos). Pass A re-pins
marks resting on the unicorn list, Wikipedia or a weak page to the round's own announcement; pass B attacks each row
for a newer round, a closed sale or a collapse (Google News under NQ_TAG=ab1a: scratchpad/ab1a/q*.out,
news-extra-ab1a.json; the publisher pages read with scratchpad/ab1a/grab.py). Membership: front is partner-carried
(R7). Run as NQ_TAG=ab1a python3 judgments-ab1a2.py.
"""
import importlib.util
from pathlib import Path

import judge_lib as jl
from judge_lib import W, cls, rnd, verdict

_s = importlib.util.spec_from_file_location("ab1a_common", Path(__file__).resolve().parent / "scratchpad/ab1a/common.py")
C = importlib.util.module_from_spec(_s)
_s.loader.exec_module(C)
WV, VRS, AB, N, RC, SIB, ROUNDS, CP, READ, keep = C.WV, C.VRS, C.AB, C.N, C.RC, C.SIB, C.ROUNDS, C.CP, C.READ, C.keep

L = []

# ---- flock-safety: a newer priced round
FLOCK = N("flock-safety", "Valued At $8.4 Billion In A New Round")
L.append(cls("flock-safety", rng="1b_plus", usd=8400000000, val_src=WV, val_cite=FLOCK, asof="2026-04-17", extra=VRS,
             flags=CP("flock-safety"),
             rounds=ROUNDS("flock-safety",
                           rnd("2026-04", "Unnamed round at $8.4B", None, None, None, FLOCK, "press")),
             note=AB + "a newer priced round replaces the $7.5B of March 2025: Flock Safety was valued at $8.4B in a round completed in the weeks before 2026-04-17 (Reuters relaying The Information). Semafor reported on 2026-09-23 that the company is evaluating a sale; no deal is signed, so the status stays private. The Coatue, Spark, Tiger Global and Y Combinator rows still read $7.5B. Stage citation attempted (Google News, the company's name beside Kleiner Perkins): no source names the firm's 2023 transaction."))

# ---- front: partner-carried (R7)
L.append(verdict("front", "not_member",
                 "Partner-carried (R7; Erik 2026-09-17 partner-carried rule): Mamoon Hamid backed Front at Social Capital, which funded its $10M Series A of May 2016 (Tech.eu, 2016-05-26), the site's 2016 year, a year before he joined Kleiner Perkins in 2017. The later rounds name their investors (Series B 2018, Sequoia with DFJ; Series C 2020, a group of executives with Sequoia, Initialized and Anthos; Series D 2022, Salesforce Ventures and Battery with Sequoia, Threshold and Uncork) and no Kleiner Perkins fund is among them; the row is on the live list only, never in the archive.",
                 ec="web", conf="medium", cite=READ["techeu-front"]))

# ---- fullstory: defended, stale
L.append(keep("fullstory", "no priced round since the $103M Series D at $1.8B of August 2021 (Google News), so the mark stands, stale."))

# ---- garner-health: re-pin to the company's own release
L.append(cls("garner-health", rng="1b_plus", usd=2740000000, val_src=WV,
             val_cite=N("garner-health", "Closes $100 Million Series E at a $2.74B Valuation to Continue"),
             asof="2026-05-28", extra=VRS,
             note=AB + "the mark is re-pinned from a secondary page to the company's own release of the $100M Series E at $2.74B (PR Newswire, 2026-05-28); nothing newer. The Sequoia and Thrive rows still read below_1b."))

# ---- glean: defended
L.append(keep("glean", "mark defended, the $150M Series F at $7.2B of 2025-06-10; Google News shows revenue reports in 2026 and no later priced round."))

# ---- granola: re-pin from the unicorn list to the round's own report
L.append(cls("granola", rng="1b_plus", usd=1500000000, val_src=WV, val_cite=RC("granola", "techcrunch.com/2026/03/25"),
             asof="2026-03-25", extra=VRS,
             note=AB + "the mark is re-pinned from the unicorn list to TechCrunch's report of the $125M Series C at $1.5B (2026-03-25), the round Kleiner Perkins entered; nothing newer."))

# ---- gusto: defended
L.append(keep("gusto", "mark defended, the employee tender at $9.3B of June 2025 (Fortune); no later priced event (TechCrunch reported $1B of revenue in May 2026, no round). The General Catalyst and Y Combinator rows still read the 2021 $9.5B."))

# ---- handshake: re-pin from Wikipedia to the company's own release
HS = SIB("coatue", "handshake")
L.append(cls("handshake", rng="1b_plus", usd=3500000000, val_src=WV, val_cite=HS, asof="2022-01-19", extra=VRS,
             flags=["stale"],
             rounds=ROUNDS("handshake",
                           rnd("2022-01-19", "Series F", 200000000, "Coatue Management; Valiant Peregrine Fund", True, HS, "company"),
                           drop=("Series F",)),
             note=AB + "the mark is re-pinned from Wikipedia to the company's own release of the $200M Series F at $3.5B (PR Newswire, 2022-01-19), which names Kleiner Perkins among the investors. No priced round since, although the AI data business has grown fast (The Information, April 2026), so the mark stands, stale."))

# ---- harmonic: defended
L.append(keep("harmonic", "mark defended, the $120M Series C at $1.45B of 2025-11-25; NVentures joined in January 2026 (SiliconANGLE) with no new price reported."))

# ---- harvey: re-pin from the unicorn list to the company's own post, and cite the round the firm entered
HV = SIB("gv", "harvey")
HW = W("Harvey (software)")
L.append(cls("harvey", rng="10b_plus", usd=15500000000, val_src=WV, val_cite=HV, asof="2026-09-09", extra=VRS,
             stage="Growth", stage_src=WV, stage_cite=HW, stage_conf="medium", entry_date="2023-12",
             flags=["stage_disputes_band"],
             rounds=ROUNDS("harvey",
                           rnd("2022-11", "Seed", 5000000, "OpenAI Startup Fund", None, HW, "press"),
                           rnd("2023-04", "$23M round", 23000000, "Sequoia Capital", None, HW, "press"),
                           rnd("2023-12", "Series B", 80000000, "Elad Gil; Kleiner Perkins", True, HW, "press"),
                           rnd("2024-07", "Series C", 100000000, "GV", True, HW, "press"),
                           rnd("2025-02", "Series D", 300000000, None, None, HW, "press"),
                           rnd("2025-06", "Series E", 300000000, "Kleiner Perkins; Coatue Management", True, HW, "press"),
                           rnd("2025-12", "Series F", 160000000, "Andreessen Horowitz", True, HW, "press"),
                           rnd("2026-03", "$200M round at $11B", 200000000, "GIC; Sequoia Capital", None, HW, "press"),
                           rnd("2026-09-09", "$550M round at $15.5B", 550000000, "Diffusion; Lightspeed Venture Partners", None, HV, "company")),
             note=AB + "the mark is re-pinned from the unicorn list to Harvey's own post of the $550M round at $15.5B (2026-09-09), aligned with the GV row; the a16z, Coatue and Sequoia rows still read $11B. Stage: the first round naming the firm is the $80M Series B of December 2023 led by Elad Gil and Kleiner Perkins (Wikipedia; the firm's own post of 2023-12-19 says it co-leads the Series B), while the April 2023 round the Form D band read was led by Sequoia with no Kleiner Perkins on record, so the entry is Growth."))

# ---- hippocratic-ai: defended
L.append(keep("hippocratic-ai", "mark defended, the $126M Series C at $3.5B of November 2025 (the company's release, Reuters); nothing newer."))

# ---- houzz: re-pin from the unicorn list to the round's own report, and cite the round the firm entered
NOC = N("houzz", "Gets $35M Cash Injection")
L.append(cls("houzz", rng="1b_plus", usd=4000000000, val_src=WV, val_cite=RC("houzz", "techcrunch.com/2017/06/24"),
             asof="2017-06", extra=VRS, flags=["stale"],
             stage="Growth", stage_src=WV, stage_cite=NOC, stage_conf="medium", entry_date="2013-01",
             rounds=ROUNDS("houzz",
                           rnd("2013-01-30", "$35M round (the third, Series C)", 35000000, "New Enterprise Associates; GGV Capital", True, NOC, "press")),
             note=AB + "the mark is re-pinned from the unicorn list to TechCrunch's report of the $400M round at $4B (June 2017); no priced round since (job cuts in 2019 and 2022, an IPO mandate in 2021), so it stands, stale. Stage: the first round naming the firm is the $35M round of January 2013, led by NEA and GGV with Sequoia, Kleiner Perkins Caufield & Byers and Comcast Ventures (NoCamels citing Bloomberg), which took the total raised to $48.6M after the 2010 and 2011 rounds, so it was the third round and the entry is Growth."))

# ---- huntress: re-pin from Wikipedia to the round's own report, and cite the round the firm entered
HU = N("huntress", "Huntress Captures $150M Series D")
HUW = W("Huntress (company)")
L.append(cls("huntress", rng="1b_plus", usd=1500000000, val_src=WV, val_cite=HU, asof="2024-06-18", extra=VRS,
             flags=["stale"],
             stage="Growth", stage_src=WV, stage_cite=HU, stage_conf="high",
             rounds=ROUNDS("huntress",
                           rnd("2020-02", "Series A", 18000000, "ForgePoint Capital", None, HUW, "press"),
                           rnd("2021-05", "Series B", 40000000, "JMI Equity", None, HUW, "press"),
                           rnd("2023-05", "Series C", 60000000, "Sapphire Ventures", None, HUW, "press"),
                           rnd("2024-06-18", "Series D", 150000000, "Kleiner Perkins; Meritech Capital; Sapphire Ventures", True, HU, "press")),
             note=AB + "the mark is re-pinned from Wikipedia to Crunchbase News's report of the $150M Series D at more than $1.5B (2024-06-18), led by Kleiner Perkins and Meritech with the existing investor Sapphire, which is also the round the firm entered (its own post of the same day says it co-leads the Series D): Growth, now cited. Axios reported in July 2026 that the company is eyeing a fresh raise; none has closed, so the mark stands, stale."))

# ---- imprint: defended
L.append(keep("imprint", "mark defended, the $150M Series D at $1.2B of 2025-12-17 (the company's release, Bloomberg); nothing newer."))

# ---- inmobi: re-pin from the unicorn list to a priced transaction
ET = N("inmobi", "company valued at around $1 billion")
MINT = N("inmobi", "True North picks up $50-60 mn stake in IPO-bound InMobi - Livemint")
L.append(cls("inmobi", rng="1b_plus", usd=1000000000, val_src=WV, val_cite=ET, asof="2025-12-04", extra=VRS,
             rounds=ROUNDS("inmobi",
                           rnd("2025-12-04", "Founders' buyback of 25-30% from SoftBank at about $1B", 250000000, None, False, ET, "press"),
                           rnd("2026-09-25", "Secondary sale of 2-3% to True North, price not disclosed", None, "True North", False, MINT, "press")),
             note=AB + "the mark is re-pinned from the unicorn list to a priced transaction: the founders bought back 25-30% from SoftBank for about $250M, valuing InMobi at around $1B (The Economic Times, 2025-12-04); the figure sits on the band edge. True North bought 2-3% for $50-60M in September 2026, mostly secondary, with the valuation not disclosed (Mint), and the IPO targets of $4B and up are bankers' targets, not a price, so neither moves the mark."))

# ---- instinct: defended
L.append(keep("instinct", "mark defended, the $1B Series C at $10B of 2026-09-28 (PYMNTS, TechCrunch), two days old."))

# ---- interos: cite the round the firm entered; the mark stands
IB = N("interos", "Interos Raises $17.5M Series B")
L.append(cls("interos", stage="Series A", stage_src=WV, stage_cite=IB, stage_conf="high",
             rounds=ROUNDS("interos",
                           rnd("2019-01-25", "Series A", 8350000, None, True, IB, "press"),
                           rnd("2020-03-12", "Series B", 17500000, "Venrock", True, IB, "press"),
                           rnd("2021-08-02", "Series C", 100000000, "NightDragon", True, RC("interos", "cooley.com"), "press"),
                           rnd("2024-10-24", "$40M investment, no price disclosed", 40000000, "Blue Owl Capital", None, None, "press"),
                           rnd("2026-01-07", "$20M round, no price disclosed", 20000000, None, None, N("interos", "raises $20M to expand"), "press")),
             note=AB + "stage cited: Crunchbase News (2020-03-12) says Kleiner Perkins joined the Venrock-led Series B and 'also invested in the company's $8.35 million Series A last year', the Form D of January 2019, so the Series A entry now rests on a named round. Mark: the $20M raise of January 2026 and the $40M Blue Owl investment of October 2024 disclosed no price, so the 2021 'more than $1B' stands, stale."))

jl.write("ab1a2", L)
