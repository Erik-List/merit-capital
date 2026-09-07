import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import classify

J = {
 "kick": ("private", "US", "below_1b", None, None, None),
 "kiwico": ("private", "US", "below_1b", None, None, None),
 "knox": ("private", None, "below_1b", None, None, None),
 "komodo-health": ("private", "US", None, None, None, None),
 "komodor": ("private", "IL", "below_1b", None, None, "Tel Aviv-based Kubernetes troubleshooting platform."),
 "kudo": ("private", None, "below_1b", None, None, None),
 "letta": ("private", "US", "below_1b", None, None, None),
 "literati-2": ("private", None, "below_1b", None, None, None),
 "liveramp": (None, "US", None, None, None, None),
 "luminal": ("private", "US", "below_1b", None, None, None),
 "mark-one-lifestyle-inc": ("defunct", None, "below_1b", None, None, "Mark One (the Vessyl smart cup) wound down; no trace of operations after the Pryme Vessyl era."),
 "matterport": ("acquired", None, "below_1b", None, None, "acq. by CoStar Group, closed Feb 2025."),
 "maze": ("private", "US", "below_1b", None, None, None),
 "meilisearch": ("private", "FR", "below_1b", None, None, "Paris-based open-source search engine."),
 "mercor": (None, None, None, None, None, None),
 "metaplane": ("acquired", "US", "below_1b", None, None, "acq. by Datadog, 2025."),
 "midi-health": ("private", "US", "below_1b", None, None, None),
 "milo": ("acquired", None, "below_1b", None, None, "acq. by eBay, Dec 2010 (~$75M reported)."),
 "mon-ami": ("private", "US", "below_1b", None, None, None),
 "moondream": ("private", "US", "below_1b", None, None, None),
 "motherduck": ("private", "US", "below_1b", None, None, None),
 "n8n": ("private", "DE", None, None, None, "Berlin-based workflow automation company."),
 "nayya": ("private", None, "below_1b", None, None, None),
 "nilus": ("private", "US", "below_1b", None, None, None),
 "nimble": ("private", "US", "below_1b", None, None, None),
 "notion": (None, None, None, None, None, None),
 "novi-connect": ("private", "US", "below_1b", None, None, None),
 "observo-ai": ("private", "US", "below_1b", None, None, None),
 "octave": ("private", "US", "below_1b", None, None, None),
 "ontic": ("private", "US", "below_1b", None, None, None),
 "opendoor": ("public", "US", None, None, None, None),
 "operand": ("private", "US", "below_1b", None, None, None),
 "operant": ("private", "US", "below_1b", None, None, None),
 "opsera": ("private", None, "below_1b", None, None, None),
 "orca-bio": ("private", "US", None, None, None, None),
 "origin": ("private", None, "below_1b", None, None, None),
 "oro-labs": ("private", "US", "below_1b", None, None, None),
 "osmosis": ("private", "US", "below_1b", None, None, None),
 "oso": ("private", "US", "below_1b", None, None, None),
 "paraform": ("private", "US", "below_1b", None, None, None),
 "paytient": ("private", "US", "below_1b", None, None, None),
 "pendulum": ("private", "US", "below_1b", None, None, None),
 "periodic-labs": ("private", "US", None, None, None, None),
 "permitflow": ("private", "US", "below_1b", None, None, None),
 "pharos": ("private", "US", "below_1b", None, None, "$5M seed led by Felicis, Oct 2024 (Y Combinator company)."),
}

DISPUTES = {
 "mercor": ("US", "Wikidata joined 'Mercor' to a Latvian entity; Mercor is the San Francisco AI-talent marketplace."),
 "milo":   ("US", "Wikidata returned 'Czechoslovakia' -- a state that no longer exists and not an ISO 3166-1 code. Milo.com was a Palo Alto local-shopping search engine, acquired by eBay in 2010."),
 "origin": ("US", "Wikidata joined 'Origin' to a UK entity; the Felicis row is the US personal-finance company. US is a flagged desk prior rather than a firm identification."),
}

STAGE_OVERRIDES = {
 # Layers conflict (CMS 'Series A' vs the archived circles 'Series C'), so
 # build-entry-stage-layer.py withheld it and it is judged here. Contemporary
 # press places Felicis in the Oct-2015 $80M Series C, which agrees with the
 # firm's own archived ladder; one vendor profile claims a 2014 seed entry.
 # Recorded Growth at medium confidence and listed in golden.json unresolved.
 "opendoor": ("Growth", "model", None),
 "midi-health": ("Series A", "model", None),
 "orca-bio": ("Series A", "model", None),
 "literati-2": ("Series A", "model", None),
 "kudo": ("Series A", "model", None),
}

EXTRA = {
 "opendoor": {"entry_stage_confidence": "medium", "flags": ["stage_uncited"],
   "note": "Entry stage contested: the live CMS says Series A, the firm's own "
           "2011-2019 listing ladder says Series C, and press places Felicis "
           "in the Oct-2015 $80M Series C. Two of the three agree on the C, so "
           "the row publishes Growth at medium confidence."},
 "origin": {"hq_country_confidence": "low", "flags": ["country_prior"]},
 "literati-2": {"entry_stage_confidence": "low", "flags": ["stage_prior", "duplicate_suspected"],
   "note": "Slug shape 'literati-2' suggests a CMS-side duplicate of a "
           "`literati` row; flagged rather than merged (§8)."},
 "kudo": {"entry_stage_confidence": "medium"},
 "midi-health": {"entry_stage_confidence": "medium"},
 "orca-bio": {"entry_stage_confidence": "medium"},
 "maze": {"hq_country_confidence": "medium"},
 "nilus": {"hq_country_confidence": "medium"},
}

classify.write(3, classify.build(3, J, country_disputes=DISPUTES,
                                 stage_overrides=STAGE_OVERRIDES, extra=EXTRA))
