"""A/B pass ab1a, part 1 (PRO-99 Kleiner Perkins; COLLECTION.md s7, s8 duty 1, verify rule 4), 2026-09-30.

The private $1B+ rows ambience .. fin of queue/ab1.json. Pass A re-pins marks resting on the unicorn list or a
weak page to the round's own announcement; pass B attacks each row for a newer round, a closed sale or a collapse
(Google News under NQ_TAG=ab1a: scratchpad/ab1a/q*.out, news-extra-ab1a.json; the publisher pages read with
scratchpad/ab1a/grab.py). Membership: cognition is the firm's own round (Series E); built and cultureamp are
partner-carried (R7). Run as NQ_TAG=ab1a python3 judgments-ab1a1.py.
"""
import importlib.util
from pathlib import Path

import judge_lib as jl
from judge_lib import POST, W, cls, rnd, verdict

_s = importlib.util.spec_from_file_location("ab1a_common", Path(__file__).resolve().parent / "scratchpad/ab1a/common.py")
C = importlib.util.module_from_spec(_s)
_s.loader.exec_module(C)
WV, VRS, AB, N, RC, SIB, ROUNDS, CP, READ, keep = C.WV, C.VRS, C.AB, C.N, C.RC, C.SIB, C.ROUNDS, C.CP, C.READ, C.keep

L = []

# ---- ambience: defended
L.append(keep("ambience", "mark defended, the $243M Series C at $1.25B of 2025-07-29 (MedCity News); Google News shows no later priced round."))

# ---- angellist: defended, stale
L.append(keep("angellist", "no priced round since the $100M Series B at $4.1B of March 2022 (Google News), so the mark stands, stale."))

# ---- anthropic: re-pin from the unicorn list to the company's own Series H announcement
L.append(cls("anthropic", rng="100b_plus", usd=965000000000, val_src=WV, val_cite=SIB("greylock", "anthropic"),
             asof="2026-05-28", extra=VRS, flags=CP("anthropic"),
             note=AB + "the mark is re-pinned from the unicorn list to Anthropic's own announcement of the $65B Series H at $965B post-money (2026-05-28), as the sibling books cite it; no later priced round. Stage citation attempted (Google News, the company's name beside Kleiner Perkins): no source names the round the firm entered in 2025."))

# ---- applied-compute: re-pin to the round's own notice
L.append(cls("applied-compute", rng="1b_plus", usd=1300000000, val_src=WV,
             val_cite=N("applied-compute", "Watkins Represents Applied Compute"), asof="2026-04-15", extra=VRS,
             note=AB + "the mark is re-pinned from TechCrunch's unicorn list to the round's own notice: $80M at a $1.3B post-money valuation led by Kleiner Perkins (Latham & Watkins, the company's counsel, 2026-04-15). Talks at about $3B were reported in August 2026 (The Information) and no closing is reported, so the April mark stands."))

# ---- applied-intuition: defended
L.append(keep("applied-intuition", "mark defended, the $600M Series F and tender at $15B of 2025-06-17 (the company's release); Google News shows no later priced round. The a16z row still carries the 2020 $1.25B."))

# ---- assured: defended; stage still open
L.append(keep("assured", "mark defended, Bloomberg's report of the round at about $1B (2025-03-04); no later priced round found for assured.com (the 2025-26 Assured raises in the news are the New York credentialing company, a namesake). Stage citation attempted: no source names the series of the round Kleiner Perkins backed.",
              flags=CP("assured")))

# ---- avoca: re-pin to the company's own release
L.append(cls("avoca", rng="1b_plus", usd=1000000000, val_src=WV,
             val_cite=N("avoca", "Power America's Services Economy With AI"), asof="2026-04-27", extra=VRS,
             note=AB + "the mark is re-pinned from TechCrunch's unicorn list to the company's own release (PR Newswire, 2026-04-27): more than $125M at a $1B valuation, the Series B led by Meritech and General Catalyst and the Series A led by Kleiner Perkins; the figure sits on the band edge. No later round found. The General Catalyst and Y Combinator rows still read below_1b."))

# ---- built: partner-carried (R7)
L.append(verdict("built", "not_member",
                 "Partner-carried (R7; Erik 2026-09-17 partner-carried rule): the firm's own post announcing Ilya Fushman (2018) credits Built to the board seats he held at Index Ventures; Index led Built's $21M Series A of November 2017 with Nyca (National Mortgage News), the site's 2017 year, a year before he joined Kleiner Perkins. The Series B (Goldman Sachs, 2019), Series C (Addition, 2021) and Series D (TCV, 2021) name their investors and no Kleiner Perkins fund is among them; the row is on the live list only, never in the archive.",
                 ec="web", conf="high", cite=READ["kp-fushman"]))

# ---- chainguard: defended
L.append(keep("chainguard", "mark defended, $3.5B at the $356M Series D of April 2025; the '$800M raised' headline of July 2026 (Crypto Briefing) is the company's cumulative funding and restates the same $3.5B, so there is no newer priced round."))

# ---- cognition: the firm's own round, not sale consideration
COG = N("cognition", "Announcing our Series E")
L.append(verdict("cognition", "member",
                 "Listed on the firm's live site as a 2026 Growth investment, and Cognition's own Series E announcement (2026-09-08) names Kleiner Perkins among the investors in the round. The position is therefore the firm's own round and not only stock received for Windsurf, which Kleiner Perkins backed as Codeium and Cognition bought in July 2025 (sale consideration alone would not be membership, Erik 2026-09-22).",
                 ec="site_listing", conf="high", cite=COG))
L.append(cls("cognition", stage="Growth", stage_src=WV, stage_cite=COG, stage_conf="high", entry_date="2026-09-08",
             rounds=ROUNDS("cognition",
                           rnd("2026-09-08", "Series E", 2000000000, "Andreessen Horowitz; Accel; Founders Fund; General Catalyst; Avenir", True, COG, "company"),
                           drop=("Series E",)),
             note=AB + "membership check settled: Cognition's own Series E post (2026-09-08, over $2B at $48B, led by Andreessen Horowitz and Accel) lists Kleiner Perkins among the other investors in the round, and the firm's page (2026, Growth) was created three days later, so the entry is the Series E. Any Cognition stock the firm received for Windsurf in 2025 would be sale consideration and is not what the row rests on. Mark defended at $48B."))

# ---- cultureamp: partner-carried (R7)
L.append(verdict("cultureamp", "not_member",
                 "Partner-carried (R7; Erik 2026-09-17 partner-carried rule): the firm's own post announcing Ilya Fushman (2018) credits CultureAmp to the board seats he held at Index Ventures; Index led Culture Amp's $10M Series B of March 2016 and Fushman joined its board (Tech.eu, 2016-03-07), the site's 2016 year, two years before he joined Kleiner Perkins. The Series C (Sapphire, 2017), Series E (Sequoia China, 2019) and Series F (Sequoia China and TDM, 2021) name their investors and no Kleiner Perkins fund is among them; the row is on the live list only, never in the archive.",
                 ec="web", conf="high", cite=READ["kp-fushman"]))

# ---- cuspai: defended
L.append(keep("cuspai", "mark defended, the $450M Series B at $2.6B of 2026-07-20; nothing newer in Google News."))

# ---- databricks: re-pin to the round's own report, and cite the round the firm entered
TI = N("databricks", "Kleiner Perkins, Founders Fund, SoftBank")
DBX = SIB("iconiq-growth", "databricks")
L.append(cls("databricks", rng="100b_plus", usd=190000000000, val_src=WV, val_cite=DBX, asof="2026-08-13", extra=VRS,
             stage="Growth", stage_src=WV, stage_cite=TI, stage_conf="medium", entry_date="2024-12",
             rounds=ROUNDS("databricks",
                           rnd("2024-12", "Series J", 10000000000, "Thrive Capital", True, TI, "press"),
                           rnd("2026-08-13", "$5B round at $190B", 5000000000, None, None, DBX, "press"),
                           drop=("Series J",)),
             note=AB + "the mark is re-pinned from the unicorn list to CNBC's report of the closed $5B round at $190B (2026-08-13), as the sibling books cite it; the Battery row still reads $134B. Stage cited: The Information (2024-12-11) reported Kleiner Perkins among the new investors in the fundraising that became the $10B Series J, the firm's 2024 year, so the entry is Growth (medium: a report ahead of the close, and the company's release does not list every participant)."))

# ---- dexterity: defended
L.append(keep("dexterity", "mark defended, the $95M round at $1.65B of March 2025; the $50M Form D of May 2026 disclosed no valuation and Google News shows no priced round since."))

# ---- dji: re-pin from the unicorn list to the round's own report, as the Accel row reads
VERGE = N("dji", "nabs $75 million")
CAIXIN = SIB("accel", "dji")
L.append(cls("dji", rng="10b_plus", usd=15000000000, val_src=WV, val_cite=CAIXIN, asof="2018-04", extra=VRS,
             flags=["stale"] + CP("dji"),
             rounds=ROUNDS("dji",
                           rnd("2015-05-06", "$75M round at about $8B", 75000000, "Accel", None, VERGE, "press"),
                           rnd("2015", "$500M round", 500000000, "New China Life Insurance; GIC; New Horizon Capital", None, W("DJI"), "press"),
                           rnd("2018-04", "$1B round by competitive bidding, at about $15B", 1000000000, None, None, CAIXIN, "press"),
                           drop=("Unnamed round",)),
             note=AB + "the mark is re-pinned from the unicorn list to the last priced round on record, the $1B raise of April 2018 run as a bidding process at about $15B (Caixin, 2018-04-18; Wikipedia records the raise as done), aligned with the Accel row and stale. The price is the one reported while the bidding ran; the last round priced at its close is Accel's $75M at about $8B (The Verge, 2015-05-06), which would read 1b_plus. Stage citation attempted (Google News, DJI beside Kleiner Perkins): no source names the firm's 2015 round."))

# ---- epic-games: re-pin from the unicorn list to the press report of Disney's priced investment
EPIC = SIB("iconiq-growth", "epic-games")
L.append(cls("epic-games", rng="10b_plus", usd=22500000000, val_src=WV, val_cite=EPIC, asof="2024-02-07", extra=VRS,
             flags=["stale"],
             rounds=ROUNDS("epic-games",
                           rnd("2024-02-07", "Disney strategic investment at $22.5B", 1500000000, "The Walt Disney Company", False, EPIC, "press")),
             note=AB + "the mark is re-pinned from the unicorn list to the priced event: Disney's $1.5B investment of February 2024 valued Epic at $22.5B, down from $31.5B in 2022 (Reuters relaying The Information, 2024-02-08), as the ICONIQ row cites it. No priced round since, and the mark is now older than 24 months: stale."))

# ---- etched: re-pin from the unicorn list to the company's own release
L.append(cls("etched", rng="10b_plus", usd=21000000000, val_src=WV, val_cite=RC("etched", "globenewswire.com"),
             asof="2026-08-18", extra=VRS,
             note=AB + "the mark is re-pinned from the unicorn list to the company's own release of the $700M round at $21B (2026-08-18), the round Kleiner Perkins entered; nothing newer. The Sequoia row still reads $10.3B (July 2026)."))

# ---- fal: defended
L.append(keep("fal", "mark defended, the $140M Series D at $4.5B of 2025-12-09 (the company's release); the higher valuation reported in talks in 2026 has not closed in any source found."))

# ---- farmers-business-network: defended, stale
L.append(keep("farmers-business-network", "no priced round since the $3.9B of November 2021: the 2023 Form D and the $50M raise of July 2025 disclosed no valuation, and no down-round or sale report was found (Google News), so the last primary stands, stale."))

# ---- fin: the closing date and the acquirer's own release
FIN = N("fin", "Salesforce Completes Acquisition of Fin - Salesforce")
L.append(cls("fin", extra={"valuation_citation": FIN, "valuation_asof": "2026-09-10"},
             note=AB + "attack confirmed and dated from the acquirer: Salesforce's own release says it completed the acquisition of Fin, formerly Intercom, on 2026-09-10, so the row is acquired (the ab2 pass recorded the flip from a 2026-09-14 report). The ICONIQ row still reads private at the signed $3.6B."))

jl.write("ab1a1", L)
