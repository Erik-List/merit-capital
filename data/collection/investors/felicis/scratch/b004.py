import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import classify

J = {
 "piazza": ("private", None, "below_1b", None, None, None),
 "picnichealth": ("private", "US", "below_1b", None, None, None),
 "pindrop": ("private", None, "below_1b", None, None, None),
 "plaid": (None, None, None, None, None, None),
 "planet": ("public", None, None, None, None, "NYSE: PL. Range deferred to the A/B pass for a cited market cap."),
 "pluralsight": ("acquired", None, "below_1b", None, None, "Taken private by Vista Equity Partners in 2021 ($3.5B); ownership passed to its lenders in a 2024 restructuring."),
 "poly": ("private", "US", "below_1b", None, None, None),
 "poolside": ("private", "US", None, None, None, None),
 "popmenu": ("private", "US", "below_1b", None, None, None),
 "predibase": ("acquired", "US", "below_1b", None, None, "acq. by Rubrik, 2025."),
 "prenuvo": ("private", None, "below_1b", None, None, None),
 "preql": ("private", "US", "below_1b", None, None, None),
 "proton": (None, None, "below_1b", None, None, None),
 "puzzle": ("private", "US", "below_1b", None, None, None),
 "radiant-nuclear": (None, None, None, None, None, None),
 "rapidfort": ("private", "US", "below_1b", None, None, "$8.5M seed, 2022."),
 "recursion": ("public", "US", None, None, None, "Nasdaq: RXRX. Range deferred to the A/B pass."),
 "revel": ("private", "US", "below_1b", None, None, None),
 "ricursive-intelligence": ("private", "US", "below_1b", None, None, None),
 "rigetti": ("public", "US", None, None, None, "Nasdaq: RGTI, public by SPAC in 2022. Range deferred to the A/B pass."),
 "ring": (None, "US", "below_1b", None, None, "acq. by Amazon, Feb 2018 (~$1B reported). Acquired rows carry a null figure."),
 "roadmunk": ("acquired", "CA", "below_1b", None, None, "acq. by Tempo Software, 2022."),
 "rovio": ("acquired", "FI", "below_1b", None, None, "acq. by Sega Sammy, 2023 (EUR 706M). Helsinki-based; the Angry Birds studio."),
 "runlayer": ("private", "US", "below_1b", None, None, "$11M seed Nov 2025; Felicis led the $30M Series A in 2026."),
 "sapho": ("acquired", "US", "below_1b", None, None, "acq. by Citrix, 2018."),
 "scopely": ("acquired", None, "below_1b", None, None, "acq. by Savvy Games Group, 2023 ($4.9B)."),
 "semgrep": ("private", "US", "below_1b", None, None, None),
 "sentilink": ("private", "US", "below_1b", None, None, None),
 "simular": ("private", "US", "below_1b", None, None, None),
 "skild-ai": (None, None, None, None, None, None),
 "skip-the-dishes": ("acquired", "CA", "below_1b", None, None, "acq. by Just Eat, 2016."),
 "sleuth": ("private", "US", "below_1b", None, None, None),
 "slingshot": ("private", None, "below_1b", None, None, None),
 "sona": ("private", None, "below_1b", None, None, None),
 "soundhound": ("public", None, None, None, None, "Nasdaq: SOUN. Range deferred to the A/B pass."),
 "sourcegraph": (None, None, None, None, None, None),
 "spekit": ("private", "US", "below_1b", None, None, None),
 "sphere": ("private", None, "below_1b", None, None, None),
 "stainless": ("private", "US", "below_1b", None, None, None),
 "standard-kernel": ("private", "US", "below_1b", None, None, None),
 "stream": (None, None, "below_1b", None, None, None),
 "supabase": ("private", "US", None, None, None, "Felicis led the $80M Series B in May 2022 and has followed on since."),
 "talkiq": ("acquired", None, "below_1b", None, None, "acq. by Dialpad, 2018."),
 "teal-health": ("private", "US", "below_1b", None, None, None),
 "tera-ai": ("private", "US", "below_1b", None, None, None),
}

DISPUTES = {
 "planet":    ("US", "Wikidata joined 'Planet' to a Greek entity; Planet Labs is the San Francisco earth-imaging company (NYSE: PL)."),
 "proton":    ("US", "Wikidata joined 'Proton' to a Ukrainian entity; this row is PRM Solutions, Inc. dba Proton.ai of Cambridge, Massachusetts -- confirmed by the Form D that carries Niki Pezeshki as Director."),
 "slingshot": ("US", "Wikidata joined 'Slingshot' to a New Zealand entity; the Felicis row is a 2024 US seed. Flagged as a desk prior, not an identification."),
 "sphere":    ("US", "Wikidata joined 'Sphere' to a Japanese entity; the Felicis row is a 2023 US seed. Flagged as a desk prior."),
 "stream":    ("US", "Wikidata joined 'Stream' to an Italian entity; getstream.io is headquartered in Boulder, Colorado (with an Amsterdam office)."),
}

STAGE_OVERRIDES = {
 "radiant-nuclear": ("Growth", "model", None),
}

EXTRA = {
 # Status disputes on pre-filled values the queue never asked about (§3, §8 duty 8).
 "proton": {"status": "private", "status_confidence": "high",
   "flags": ["model_disputes_source"],
   "note": "Status disputed: the deterministic layer recorded `acquired`. "
           "Proton.ai (PRM Solutions, Inc., Cambridge MA) is private and "
           "operating; the collision is with Proton AG, the Swiss privacy "
           "company, which is also what put this row in Ukraine."},
 "stream": {"status": "private", "status_confidence": "high",
   "flags": ["model_disputes_source"],
   "note": "Status disputed: the deterministic layer recorded `defunct`. "
           "Stream (getstream.io) is an operating chat/activity-feed API "
           "company; the `defunct` reading is a name collision."},
 "sona": {"flags": ["weak_cik_join"], "hq_country_confidence": "low",
   "note": "Weak CIK join, quarantined (§8 duty 3): the Form D attached to "
           "this row is a Vancouver filer with an $11,189 offering carrying "
           "'John Anderson' as a related person -- the run's largest homonym "
           "cluster. The row itself is a genuine Felicis listing; the filing "
           "evidence is not its own and is not used for any column."},
 "radiant-nuclear": {"entry_stage_confidence": "medium"},
 "slingshot": {"hq_country_confidence": "low", "flags": ["country_prior"]},
 "sphere": {"hq_country_confidence": "low", "flags": ["country_prior"]},
 "pindrop": {"hq_country_confidence": "high"},
}

classify.write(4, classify.build(4, J, country_disputes=DISPUTES,
                                 stage_overrides=STAGE_OVERRIDES, extra=EXTRA))
