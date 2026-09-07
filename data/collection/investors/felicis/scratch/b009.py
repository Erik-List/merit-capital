import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import classify

J = {
 "lm-arena": ("private", "US", "below_1b", None, None, None),
 "lovely": ("acquired", "US", "below_1b", None, None, "acq. by RentPath, 2017."),
 "lucy": ("private", "US", "below_1b", None, None, None),
 "luma": ("acquired", "US", "below_1b", None, None, "Luma (mesh WiFi) acq. by First Alert/Newell, 2018."),
 "madkudu": ("private", "US", "below_1b", None, None, None),
 "madvertise": ("acquired", "DE", "below_1b", None, None, "German mobile ad network; folded into Azerion."),
 "marchex-voicestar": ("acquired", "US", "below_1b", None, None, "VoiceStar acq. by Marchex, 2007 ($28M)."),
 "marigold-health": ("private", "US", "below_1b", None, None, None),
 "mashery": ("acquired", "US", "below_1b", None, None, "acq. by Intel, 2013; sold on to TIBCO, 2015."),
 "matchbox": ("private", None, "below_1b", None, None, None),
 "mattermark": ("acquired", "US", "below_1b", None, None, "acq. by FullContact, 2017."),
 "mecommerce": ("defunct", "US", "below_1b", None, None, None),
 "meili": ("private", None, "below_1b", None, None, None),
 "melodis": ("private", "US", "below_1b", None, None, None),
 "meraki": ("acquired", "US", "below_1b", None, None, "acq. by Cisco, Nov 2012 ($1.2B). One of the firm's 2007-era angel positions."),
 "mesmo-tv": ("defunct", "US", "below_1b", None, None, None),
 "metromile": ("acquired", "US", "below_1b", None, None, "acq. by Lemonade, 2022."),
 "mightyhive": ("acquired", "US", "below_1b", None, None, "acq. by S4 Capital, 2018."),
 "mindsnacks": ("defunct", "US", "below_1b", None, None, None),
 "mint": ("acquired", "US", "below_1b", None, None, "acq. by Intuit, Nov 2009 ($170M). A 2007-era angel position, and Intuit retired the Mint app in 2024."),
 "mixer-labs": ("acquired", "US", "below_1b", None, None, "acq. by Twitter, Dec 2009."),
 "mob-ly": ("acquired", "BR", "below_1b", None, None, "Brazilian mobile commerce; acq. by Walmart, 2011."),
 "mobile-action": ("private", "US", "below_1b", None, None, None),
 "mobily": (None, None, "below_1b", None, None, None),
 "mochi": ("acquired", None, "below_1b", None, None, "Mochi Media acq. by Shanda Games, Jan 2010 ($80M)."),
 "modern-health": ("private", "US", None, None, None, None),
 "modus": ("private", None, "below_1b", None, None, None),
 "monami-io": ("private", "US", "below_1b", None, None, None),
 "motif-analytics": ("private", "US", "below_1b", None, None, None),
 "movity": ("acquired", "US", "below_1b", None, None, "acq. by Trulia, 2011."),
 "muse": ("private", None, "below_1b", None, None, None),
 "mylikes": ("defunct", "US", "below_1b", None, None, None),
 "naked-poppy": ("defunct", "US", "below_1b", None, None, None),
 "octopart": ("acquired", None, "below_1b", None, None, "acq. by Altium, 2015."),
 "okera": ("acquired", "US", "below_1b", None, None, "acq. by Databricks, 2023."),
 "optimizely": ("acquired", None, "below_1b", None, None, "acq. by Episerver, 2020; the combined company kept the Optimizely name."),
}

DISPUTES = {
 "matchbox": ("US", "Wikidata joined 'Matchbox' to an Australian entity; flagged as a desk prior rather than an identification."),
 "meili":    ("US", "Wikidata joined 'Meili' to a Swiss entity; flagged as a desk prior."),
 "mobily":   ("US", "Wikidata joined 'Mobily' to the Saudi telecom operator Etihad Etisalat -- a company Felicis has no relationship with. Flagged as a desk prior."),
 "mochi":    ("US", "Wikidata joined 'Mochi' to an Indian entity; Mochi Media was a San Francisco casual-games network."),
 "modus":    ("US", "Wikidata joined 'Modus' to a Canadian entity; flagged as a desk prior."),
}

M = ("model", None)
STAGE_OVERRIDES = {
 "lm-arena": ("Seed", *M), "lovely": ("Seed", *M), "luma": ("Seed", *M),
 "madkudu": ("Seed", *M), "madvertise": ("Series A", *M),
 "marchex-voicestar": ("Seed", *M), "marigold-health": ("Seed", *M),
 "mecommerce": ("Seed", *M), "meili": ("Seed", *M), "melodis": ("Seed", *M),
 "mesmo-tv": ("Seed", *M), "mixer-labs": ("Seed", *M),
 "mobile-action": ("Series A", *M), "mobily": ("Seed", *M),
 "modern-health": ("Series A", *M), "modus": ("Seed", *M),
 "monami-io": ("Seed", *M), "motif-analytics": ("Seed", *M),
 "movity": ("Seed", *M), "mylikes": ("Series A", *M),
 "naked-poppy": ("Seed", *M), "okera": ("Seed", *M),
 "matchbox": ("Seed", *M), "mindsnacks": ("Seed", *M),
 "metromile": ("Series B", *M), "mightyhive": ("Seed", *M),
 "mattermark": ("Seed", *M), "lucy": ("Seed", *M), "mashery": ("Series A", *M),
}

LOW = {"entry_stage_confidence": "low", "flags": ["stage_prior"]}
MED = {"entry_stage_confidence": "medium"}
PRIOR = {"hq_country_confidence": "low", "flags": ["country_prior"]}
EXTRA = {
 "mobily": {"status": "private", "status_confidence": "low",
   "flags": ["model_disputes_source", "country_prior", "stage_prior"],
   "entry_stage_confidence": "low", "hq_country_confidence": "low",
   "note": "Both the status and the country came from a join to the Saudi "
           "telecom operator Etihad Etisalat ('Mobily'), which is not this "
           "company. Status disputed to private; country and stage carry "
           "flagged priors rather than that join's values."},
 "melodis": {"flags": ["duplicate_suspected"], **LOW,
   "note": "Melodis renamed itself SoundHound in 2010; `soundhound` is the canonical row (identity-merges.json)."},
 "mixer-labs": {"flags": ["duplicate_suspected"], **MED,
   "note": "Canonical for the GeoAPI/Mixer Labs pair (identity-merges.json)."},
 "monami-io": {"flags": ["duplicate_suspected"], **LOW,
   "note": "Domain-form duplicate of `mon-ami` (identity-merges.json)."},
 "matchbox": PRIOR, "meili": PRIOR, "modus": PRIOR,
 "lm-arena": MED, "madkudu": LOW, "marigold-health": LOW, "lucy": LOW,
 "mecommerce": LOW, "mesmo-tv": LOW, "motif-analytics": LOW,
 "naked-poppy": LOW, "monami-io_x": {},
 "madvertise": MED, "marchex-voicestar": MED, "mobile-action": MED,
 "modern-health": MED, "movity": MED, "mylikes": MED, "okera": MED,
 "mindsnacks": LOW, "metromile": MED, "mightyhive": MED, "mattermark": MED,
 "mashery": MED, "luma": MED, "lovely": MED,
}

classify.write(9, classify.build(9, J, country_disputes=DISPUTES,
                                 stage_overrides=STAGE_OVERRIDES, extra=EXTRA))
