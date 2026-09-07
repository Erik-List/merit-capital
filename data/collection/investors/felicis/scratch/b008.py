import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import classify

J = {
 "go-insurance": ("private", "US", "below_1b", None, None, None),
 "go-maps": ("private", "US", "below_1b", None, None, None),
 "gobble": ("private", "US", "below_1b", None, None, None),
 "granular": ("acquired", "US", "below_1b", None, None, "acq. by DuPont Pioneer/Corteva, 2017 ($300M)."),
 "greenhouse": (None, None, "below_1b", None, None, "acq. by TPG, 2024 (majority recapitalisation)."),
 "groupon": ("unknown", "US", "below_1b", None, None, None),
 "grove-labs": ("defunct", "US", "below_1b", None, None, "Indoor-gardening hardware; wound down."),
 "guild": (None, None, "below_1b", None, None, None),
 "gydget": ("defunct", "US", "below_1b", None, None, "A 2008-era felicisventures.com listing; ceased operations."),
 "hailo": (None, None, None, None, None, None),
 "hall": ("private", None, "below_1b", None, None, None),
 "handipoints": ("defunct", "US", "below_1b", None, None, "Children's chore/rewards site of the 2008-2012 era; ceased operations."),
 "happiest-baby": ("private", "US", "below_1b", None, None, "Maker of the SNOO bassinet."),
 "headspin": ("private", "US", "below_1b", None, None, "The 2020 unicorn mark did not survive: the founder's 2021 fraud conviction was followed by a recapitalisation that cut the valuation roughly two thirds, which is documented collapse evidence under §6."),
 "healthiq": ("defunct", "US", "below_1b", None, None, "Health IQ ceased operations in 2024."),
 "heaviside": ("private", "US", "below_1b", None, None, "$60M Series B and a Nammo partnership, 2026."),
 "hireart": ("private", "US", "below_1b", None, None, None),
 "homeboodle": ("defunct", "US", "below_1b", None, None, None),
 "homeroom": ("defunct", "US", "below_1b", None, None, None),
 "humans": ("private", "US", "below_1b", None, None, None),
 "humansand": ("private", "US", "below_1b", None, None, None),
 "hyperscience": ("private", "US", "below_1b", None, None, None),
 "iddiction": ("acquired", "US", "below_1b", None, None, None),
 "incountry": ("private", "US", "below_1b", None, None, None),
 "inkling": ("acquired", "US", "below_1b", None, None, "Merged with Echo360 in 2021."),
 "interaxon": ("private", "CA", "below_1b", None, None, "Toronto-based maker of the Muse headband."),
 "iru": ("private", None, "below_1b", None, None, None),
 "january-ai": ("private", "US", "below_1b", None, None, None),
 "juvena-therapeutics": ("private", "US", "below_1b", None, None, None),
 "kahuna": ("acquired", None, "below_1b", None, None, "Mobile marketing automation; assets went to Tenor/Google in 2017."),
 "karma": (None, None, "below_1b", None, None, None),
 "kinde": ("private", "AU", "below_1b", None, None, "Melbourne-based auth platform."),
 "kissmetrics": ("acquired", "US", "below_1b", None, None, "acq. by Ascendix/After, 2018."),
 "kiwicrate": ("private", "US", "below_1b", None, None, "Now KiwiCo."),
 "komodo": ("private", "US", "below_1b", None, None, None),
 "kryptnostic": ("defunct", "US", "below_1b", None, None, None),
 "lab-genius": ("private", "GB", "below_1b", None, None, "London-based protein engineering (LabGenius)."),
 "leandata": ("private", "US", "below_1b", None, None, None),
 "lighthouse": (None, None, "below_1b", None, None, None),
 "linkedin": ("unknown", "US", "below_1b", None, None, None),
 "living-carbon": ("private", "US", "below_1b", None, None, None),
}

DISPUTES = {
 "guild": ("US", "Wikidata joined 'Guild' to a Japanese entity; Guild Education is the Denver workforce-education company."),
 "hall":  ("US", "Wikidata joined 'HALL' to a Czech entity; the Felicis row is a 2015 US company. Flagged as a desk prior."),
 "karma": ("US", "Wikidata returned 'Czechoslovakia', which is neither a current state nor an ISO 3166-1 code."),
 "iru":   ("US", "Wikidata's join is unreliable on this single-token name; US is a flagged desk prior."),
 "lighthouse": ("US", "Wikidata joined 'Lighthouse' to a UK entity; flagged as a desk prior rather than an identification."),
 "hailo": ("IL", "Wikidata joined 'Hailo' to the UK taxi app of the same name. Felicis's Hailo is the Israeli AI-chip company (Tel Aviv), which is also why the $1B+ mark is plausible."),
}

STAGE_OVERRIDES = {
 "go-insurance": ("Seed", "model", None), "go-maps": ("Seed", "model", None),
 "headspin": ("Series B", "model", None), "healthiq": ("Series A", "model", None),
 "hireart": ("Seed", "model", None), "homeboodle": ("Seed", "model", None),
 "homeroom": ("Seed", "model", None), "humansand": ("Seed", "model", None),
 "incountry": ("Series A", "model", None), "january-ai": ("Series A", "model", None),
 "juvena-therapeutics": ("Seed", "model", None), "kinde": ("Seed", "model", None),
 "lab-genius": ("Series A", "model", None), "living-carbon": ("Series A", "model", None),
 "gydget": ("Seed", "model", None), "groupon": ("Seed", "model", None),
 "linkedin": ("Seed", "model", None), "granular": ("Series A", "model", None),
}

LOW = {"entry_stage_confidence": "low", "flags": ["stage_prior"]}
MED = {"entry_stage_confidence": "medium"}
EXTRA = {
 "greenhouse": {"hq_country": "US", "hq_country_source": "model_knowledge",
   "hq_country_confidence": "high", "flags": ["model_disputes_source"],
   "note": "Wikidata joined 'Greenhouse' to a Czech entity; Greenhouse Software is a New York company. acq. by TPG, 2024."},
 "karma": {"status": "defunct", "status_confidence": "medium",
   "flags": ["model_disputes_source"],
   "note": "Country disputed: Wikidata returned 'Czechoslovakia'. Status kept as defunct."},
 "lighthouse": {"status": "defunct", "status_confidence": "medium",
   "flags": ["model_disputes_source"],
   "note": "Country disputed (Wikidata: UK); status kept as defunct."},
 "hailo": {"hq_country_confidence": "medium"},
 "hall": {"hq_country_confidence": "low", "flags": ["country_prior"]},
 "iru": {"hq_country_confidence": "low", "flags": ["country_prior", "stage_prior"]},
 "headspin": MED, "healthiq": MED, "incountry": MED, "january-ai": MED,
 "lab-genius": MED, "living-carbon": MED, "granular": MED,
 "go-insurance": LOW, "go-maps": LOW, "hireart": LOW, "homeboodle": LOW,
 "homeroom": LOW, "humansand": LOW, "juvena-therapeutics": LOW,
 "kinde": LOW, "gydget": LOW,
 "groupon": {**LOW, "flags": ["stage_prior", "parser_artifact"],
   "note": "PARSER ARTIFACT, not a member: the 2011 listing rendered the site's "
           "social footer with the same images/logos/ path as its portfolio "
           "cards. Removed from the parsed source; this row disappears at the "
           "scheduled rebuild (decisions.md R7)."},
 "linkedin": {**LOW, "flags": ["stage_prior", "parser_artifact"],
   "note": "PARSER ARTIFACT, not a member -- site chrome, same cause as the "
           "Groupon row. Removed from the parsed source; disappears at the rebuild."},
 "iddiction": MED,
}

classify.write(8, classify.build(8, J, country_disputes=DISPUTES,
                                 stage_overrides=STAGE_OVERRIDES, extra=EXTRA))
