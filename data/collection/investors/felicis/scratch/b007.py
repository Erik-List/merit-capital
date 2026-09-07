import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import classify

J = {
 "dinda-com-br": ("defunct", "BR", "below_1b", None, None, "Brazilian e-commerce; ceased operations."),
 "disqus": ("acquired", "US", "below_1b", None, None, "acq. by Zeta Global, 2017."),
 "dna-nexus": ("private", "US", "below_1b", None, None, None),
 "dnovo": ("private", "US", "below_1b", None, None, None),
 "dojo": ("private", "US", "below_1b", None, None, None),
 "dollar-shave-club": (None, None, "below_1b", None, None, "acq. by Unilever, 2016 ($1B); Nexus Capital bought a majority back in 2023. Acquired rows carry a null figure."),
 "dots": ("defunct", "US", "below_1b", None, None, "The Dots game studio wound down."),
 "dreambase": ("private", "US", "below_1b", None, None, None),
 "drivetime": ("private", "US", "below_1b", None, None, None),
 "dropcam": (None, None, "below_1b", None, None, "acq. by Nest/Google, 2014 ($555M)."),
 "drum-technologies": ("private", "US", "below_1b", None, None, None),
 "elevateapp-com": ("private", "US", "below_1b", None, None, None),
 "endurance-energy": ("unknown", "US", "below_1b", None, None, "An early-era listing with no traceable operations today."),
 "ent": ("private", "US", None, None, None, "Reported a $100M seed round in 2026; range deferred to the A/B pass."),
 "epinomics": ("acquired", "US", "below_1b", None, None, "acq. by 10x Genomics, 2018."),
 "erply": ("private", None, "below_1b", None, None, "Estonian retail POS software."),
 "everalbum": ("private", "US", "below_1b", None, None, None),
 "exa": (None, "US", "below_1b", None, None, None),
 "explo": ("private", "US", "below_1b", None, None, None),
 "factual": ("acquired", None, "below_1b", None, None, "acq. by Foursquare, 2020."),
 "farmwise": ("acquired", "US", "below_1b", None, None, "FarmWise wound down in 2024 and its weeding technology went to Toro; recorded acquired with a successor note rather than defunct (§6)."),
 "feedjit": ("unknown", "US", "below_1b", None, None, "A 2008-era listing; no traceable operations."),
 "feedster": ("defunct", "US", "below_1b", None, None, "RSS search engine of the 2005-2008 era; ceased operations."),
 "feel": ("private", None, "below_1b", None, None, None),
 "figure-eight": ("acquired", None, "below_1b", None, None, "acq. by Appen, 2019 (~$300M). Formerly CrowdFlower."),
 "first-opinion": ("defunct", "US", "below_1b", None, None, "The consumer doctor-chat service was retired."),
 "floored": ("acquired", "US", "below_1b", None, None, "acq. by CBRE, 2017."),
 "floravere": ("defunct", "US", "below_1b", None, None, "Direct-to-consumer bridal; ceased operations."),
 "foodspotting": ("acquired", "US", "below_1b", None, None, "acq. by OpenTable, 2013 ($10M)."),
 "fractile": ("private", "GB", "below_1b", None, None, "London-based AI inference chips."),
 "freewebs": ("acquired", "US", "below_1b", None, None, "Freewebs became Webs.com; acq. by Vistaprint, 2011 ($117.5M)."),
 "gali-health": ("private", "US", "below_1b", None, None, None),
 "gamalon": ("private", "US", "below_1b", None, None, None),
 "geoapi-mixer-labs": ("acquired", "US", "below_1b", None, None, "Mixer Labs (GeoAPI) acq. by Twitter, Dec 2009."),
 "gigster": ("private", None, "below_1b", None, None, None),
 "gingko-bioworks": ("public", "US", None, None, None, None),
 "go-2-ec105164-e34f-460d-92be-c4f14caf5327": ("private", "US", "below_1b", None, None, None),
}

DISPUTES = {
 "feel": ("US", "Wikidata joined 'Feel' to a Norwegian entity; the Felicis row is a 2023 US company. Flagged as a desk prior."),
}

STAGE_OVERRIDES = {
 "dnovo": ("Seed", "model", None),
 "dojo": ("Seed", "model", None),
 "drum-technologies": ("Seed", "model", None),
 "elevateapp-com": ("Seed", "model", None),
 "endurance-energy": ("Series A", "model", None),
 "everalbum": ("Series A", "model", None),
 "explo": ("Seed", "model", None),
 "farmwise": ("Series A", "model", None),
 "feedjit": ("Seed", "model", None),
 "feedster": ("Seed", "model", None),
 "feel": ("Seed", "model", None),
 "first-opinion": ("Seed", "model", None),
 "floravere": ("Seed", "model", None),
 "freewebs": ("Seed", "model", None),
 "gali-health": ("Seed", "model", None),
 "geoapi-mixer-labs": ("Seed", "model", None),
 "gingko-bioworks": ("Series A", "model", None),
 "go-2-ec105164-e34f-460d-92be-c4f14caf5327": ("Seed", "model", None),
}

LOW = {"entry_stage_confidence": "low", "flags": ["stage_prior"]}
MED = {"entry_stage_confidence": "medium"}
EXTRA = {
 "exa": {"status": "private", "status_confidence": "high",
   "flags": ["model_disputes_source"],
   "note": "Status disputed: the deterministic layer recorded `acquired`. "
           "Exa (exa.ai) is a private, operating search-API company; the "
           "reading is a name collision."},
 "gingko-bioworks": {"flags": ["duplicate_suspected"], "entry_stage_confidence": "medium",
   "note": "CMS typo of Ginkgo Bioworks; `ginkgo-bioworks` is the canonical "
           "row (identity-merges.json). Range deferred to the A/B pass."},
 "everalbum": {"flags": ["duplicate_suspected"], "entry_stage_confidence": "medium",
   "note": "Everalbum renamed itself Paravision; `paravision` is also a base "
           "row (identity-merges.json)."},
 "elevateapp-com": {"flags": ["duplicate_suspected"], **LOW,
   "note": "Domain-form duplicate of `elevate` (identity-merges.json)."},
 "go-2-ec105164-e34f-460d-92be-c4f14caf5327": {**LOW,
   "flags": ["stage_prior", "duplicate_suspected"],
   "note": "Unresolved CMS slug artifact carrying a raw UUID. The base holds "
           "both `go-maps` and `go-insurance` and this row could be either, so "
           "it is reported rather than guessed into one of them (decisions.md R6)."},
 "feel": {"hq_country_confidence": "low", "flags": ["country_prior", "stage_prior"],
          "entry_stage_confidence": "low"},
 "dnovo": LOW, "dojo": LOW, "drum-technologies": LOW, "explo": LOW,
 "endurance-energy": LOW, "feedjit": LOW, "feedster": LOW,
 "first-opinion": LOW, "floravere": LOW, "gali-health": LOW,
 "farmwise": MED, "freewebs": MED, "geoapi-mixer-labs": MED,
}

classify.write(7, classify.build(7, J, country_disputes=DISPUTES,
                                 stage_overrides=STAGE_OVERRIDES, extra=EXTRA))
