import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import classify
from emit import WHO

M = ("model", None)
J = {
 "literati": ("defunct", None, "below_1b", None, None, "Austin-based children's book-club subscription; wound down in 2024."),
 "xilis": ("private", None, "below_1b", None, None, "Durham, NC oncology (patient-derived micro-organospheres)."),
 "bioage": (None, "US", None, None, None, None),
 "bookfresh": ("acquired", "US", "below_1b", None, None, "acq. by Square, 2014."),
 "buzzlogic": ("acquired", "US", "below_1b", None, None, "Social-media influence analytics of the 2006-2010 era; assets sold."),
 "dig-security-2": ("acquired", "US", "below_1b", None, None, "acq. by Palo Alto Networks, 2023."),
 "dogster": ("acquired", None, "below_1b", None, None, "Dogster/Catster acq. by Say Media, 2011; later sold on to Belvoir Media."),
 "drive-fm": ("private", "US", "below_1b", None, None, None),
 "foodzie": ("acquired", "US", "below_1b", None, None, "acq. by Joyus, 2013."),
 "glencoco": ("private", "US", "below_1b", None, None, None),
 "imageshack": ("private", None, "below_1b", None, None, "Image-hosting service of the 2008-2010 era; still operating."),
 "justin-tv": ("acquired", "US", "below_1b", None, None, "Justin.tv became Twitch; acq. by Amazon, 2014."),
 "kyklo": ("private", "SG", "below_1b", None, None, "Singapore-based electrical and automation product data."),
 "loomia": ("acquired", "US", "below_1b", None, None, "Recommendation engine of the 2006-2010 era; acq. by Aggregate Knowledge, 2009."),
 "made-renovation": ("defunct", "US", "below_1b", None, None, "Bathroom-renovation startup; ceased operations."),
 "mochi-media": ("acquired", None, "below_1b", None, None, "acq. by Shanda Games, Jan 2010 ($80M)."),
 "nimblerx": ("private", "US", "below_1b", None, None, "Digital pharmacy; distinct from the `nimble` row."),
 "omnidrive": ("defunct", "US", "below_1b", None, None, "Online storage of the 2007-2008 era; ceased operations in 2008."),
 "optrip-new": ("defunct", "US", "below_1b", None, None, None),
 "oro-labs-2": ("private", "US", "below_1b", None, None, None),
 "pantheon-ai": ("private", "US", "below_1b", None, None, None),
 "r2c": ("private", "US", "below_1b", None, None, "r2c renamed itself Semgrep."),
 "rapleaf": ("acquired", "US", "below_1b", None, None, "Rapleaf's data business became LiveRamp, which Acxiom acquired in 2014; the residual consumer-data business was wound down."),
 "redactive": ("private", "AU", "below_1b", None, None, "Sydney-based; $7.5M seed, 2024."),
 "sgn": ("acquired", None, "below_1b", None, None, "Social Gaming Network became MindJolt, then S囧GN/Tapjoy-era consolidation; the studio business changed hands."),
 "social-gaming-network": ("acquired", "US", "below_1b", None, None, "Duplicate rendering of `sgn`."),
 "social-im": ("defunct", "US", "below_1b", None, None, None),
 "the-auteurs": ("private", "GB", "below_1b", None, None, "The Auteurs became Mubi, the London-based film streaming service."),
 "walnut": ("private", "US", "below_1b", None, None, None),
 "walnut-io": ("private", "US", "below_1b", None, None, "Duplicate rendering of `walnut`."),
 "yamli": ("private", None, "below_1b", None, None, "Arabic search and transliteration."),
}

DISPUTES = {
 "sgn": ("US", "Wikidata joined 'SGN' to a UK entity; Social Gaming Network was a Palo Alto studio."),
}

STAGE_OVERRIDES = {
 "literati": ("Series A", *M), "xilis": ("Series A", *M), "bioage": ("Series A", *M),
 "bookfresh": ("Seed", *M), "buzzlogic": ("Series A", *M),
 "dig-security-2": ("Series A", *M), "dogster": ("Seed", *M),
 "drive-fm": ("Seed", *M), "foodzie": ("Seed", *M), "glencoco": ("Seed", *M),
 "imageshack": ("Series A", *M), "justin-tv": ("Seed", *M), "kyklo": ("Seed", *M),
 "loomia": ("Seed", *M), "made-renovation": ("Seed", *M),
 "mochi-media": ("Growth", *M), "nimblerx": ("Series A", *M),
 "omnidrive": ("Seed", *M), "optrip-new": ("Seed", *M), "oro-labs-2": ("Series B", *M),
 "pantheon-ai": ("Seed", *M), "r2c": ("Series A", *M), "rapleaf": ("Seed", *M),
 "redactive": ("Seed", *M), "sgn": ("Series A", *M),
 "social-gaming-network": ("Series A", *M), "social-im": ("Seed", *M),
 "the-auteurs": ("Seed", *M), "walnut": ("Seed", *M), "walnut-io": ("Seed", *M),
 "yamli": ("Seed", *M),
}

LOW = {"entry_stage_confidence": "low", "flags": ["stage_prior"]}
MED = {"entry_stage_confidence": "medium"}
DUP = {"flags": ["duplicate_suspected"]}
EXTRA = {
 "bioage": {"status": "public", "status_confidence": "high",
   "valuation_range": "below_1b", "valuation_confidence": "high",
   **DUP, **MED,
   "note": "Duplicate rendering of `bioage-labs` (Nasdaq: BIOA); merged at the "
           "final rebuild."},
 "dig-security-2": {**DUP, **MED, "note": "Duplicate rendering of `dig-security`."},
 "oro-labs-2": {**DUP, **MED, "note": "Duplicate rendering of `oro-labs`."},
 "walnut-io": {**DUP, **LOW, "note": "Duplicate rendering of `walnut`."},
 "social-gaming-network": {**DUP, **MED, "note": "Duplicate rendering of `sgn`."},
 "mochi-media": {**DUP, **MED, "note": "Duplicate rendering of `mochi`."},
 "optrip-new": {**DUP, **LOW, "note": "Duplicate rendering of `optrip`."},
 "the-auteurs": {**DUP, **LOW, "note": "Duplicate rendering of `auteurs`."},
 "justin-tv": {**DUP, **MED, "note": "Duplicate rendering of `twitch`."},
 "social-im": {**DUP, **LOW, "note": "Duplicate rendering of `socialim`."},
 "r2c": {**DUP, **MED, "note": "Duplicate rendering of `semgrep`."},
 "sgn": {"hq_country_confidence": "medium", **MED},
 "literati": MED, "xilis": MED, "buzzlogic": MED, "imageshack": MED,
 "loomia": MED, "rapleaf": MED, "nimblerx": MED, "redactive": MED,
 "dogster": MED, "foodzie": MED, "bookfresh": MED, "kyklo": MED,
 "drive-fm": LOW, "glencoco": LOW, "made-renovation": LOW, "omnidrive": LOW,
 "pantheon-ai": LOW, "walnut": LOW, "yamli": LOW,
}

lines = classify.build(1, J, country_disputes=DISPUTES,
                       stage_overrides=STAGE_OVERRIDES, extra=EXTRA)

# Two membership rows: the same homonym clusters, under registrant names the
# rebuild re-keyed. §8 warns that a membership verdict in the delta needs one
# more rebuild, and these two are why this run runs a second.
for slug, person, basis in [
    ("carbonone-holdings-corp", "Danny Lee",
     "Cluster ruling (decisions.md, 'Danny Lee'): a Vancouver resource filer, "
     "no Felicis listing in any era, no fund vehicle on the filing. Re-keyed by "
     "the rebuild from `carbonone-technologies-inc`, which carried the same verdict."),
    ("mexican-gold-corp", "John Anderson",
     "Cluster ruling (decisions.md, 'John Anderson'): a Thunder Bay mining "
     "filer from the run's largest homonym cluster. Re-keyed by the rebuild "
     "from `mexican-gold-mining-corp`."),
]:
    lines.append({"slug": slug, "who": WHO, "verdict": "not_member",
                  "evidence_class": "web", "confidence": "high",
                  "exclusion_class": "homonym", "basis": basis})

classify.write(1, lines)
