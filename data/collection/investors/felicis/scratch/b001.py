import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import classify

# (status, hq_country, valuation_range, valuation_usd, citation, note)
# valuation_range None = deferred to the adversarial A/B pass, where the row
# gets a cited figure. Every acquired/defunct row is below_1b with a null
# figure, which is the landed convention across every base in this project.
J = {
 "aardvark": ("acquired", "US", "below_1b", None, None, "acq. by Google, 2010; the social-search app was retired in 2011."),
 "acompli": ("acquired", None, "below_1b", None, None, "acq. by Microsoft, Dec 2014 (~$200M reported); became Outlook Mobile."),
 "adentro": ("private", None, "below_1b", None, None, None),
 "adyen": ("public", None, None, None, None, None),
 "agency": ("private", "US", "below_1b", None, None, None),
 "alloy": ("private", None, None, None, None, None),
 "archil": ("private", "US", "below_1b", None, None, None),
 "armada": ("private", "US", "below_1b", None, None, None),
 "ascend-io": ("private", "US", "below_1b", None, None, None),
 "assort-health": ("private", "US", None, None, None, None),
 "astranis": (None, None, None, None, None, None),
 "atlas-health": ("private", "US", "below_1b", None, None, "Felicis led the $40M Series A of Jan 2022; Atlas Labs, Inc. is the same company's registered name (identity-merges.json)."),
 "attentive": ("private", "US", None, None, None, None),
 "automat": ("private", None, "below_1b", None, None, None),
 "azumio": ("private", "US", "below_1b", None, None, None),
 "bioage-labs": (None, "US", None, None, None, None),
 "blume": ("private", "US", "below_1b", None, None, None),
 "bonobos": (None, None, "below_1b", None, None, "acq. by Walmart, 2017 ($310M)."),
 "brevian": ("private", "US", "below_1b", None, None, None),
 "bright": ("private", None, "below_1b", None, None, None),
 "browser-use": ("private", "US", "below_1b", None, None, None),
 "bunkerhill": ("private", "US", "below_1b", None, None, None),
 "cambridge-terahertz": ("private", "US", "below_1b", None, None, None),
 "canva": (None, None, None, None, None, None),
 "cedar": ("private", None, None, None, None, None),
 "cellino": ("private", "US", "below_1b", None, None, None),
 "chalk": ("private", None, "below_1b", None, None, None),
 "classdojo": (None, None, None, None, None, None),
 "clear-labs": ("private", None, "below_1b", None, None, None),
 "coalition": (None, None, None, None, None, None),
 "condor": ("private", None, "below_1b", None, None, None),
 "conductorone": ("private", None, "below_1b", None, None, None),
 "counterpart": ("private", "US", "below_1b", None, None, None),
 "covalent": ("private", "US", "below_1b", None, None, None),
 "credit-karma": ("acquired", None, "below_1b", None, None, "acq. by Intuit, Dec 2020 ($7.1B). Entry stage: both first-party layers say Seed and the archived ladder is [Seed, Series A, Series B], but TechCrunch's Nov-2009 report names Felicis in the $2.5M Series A led by QED. Recorded Seed at medium confidence on the firm's own record; golden.json lists it unresolved."),
 "crunchbase": ("private", None, "below_1b", None, None, None),
 "crusoe": ("private", "US", None, None, None, None),
 "datagrail": ("private", "US", "below_1b", None, None, None),
 "datology": ("private", "US", "below_1b", None, None, None),
 "dedrone": ("acquired", None, "below_1b", None, None, "acq. by Axon Enterprise, 2024. Aydin Senkut sat as a Form D related person 2018-2022, corroborating the site listing."),
 "deepinfra": ("private", "US", None, None, None, None),
 "deepjudge": ("private", "CH", "below_1b", None, None, "Zurich-based legal-AI search company."),
 "depot": ("private", None, "below_1b", None, None, None),
 "dialpad": ("private", "US", None, None, None, None),
 "diffbot": ("private", None, "below_1b", None, None, None),
}

# Ruling R5: the Wikidata single-token joins. These rows were PRE-FILLED by the
# deterministic layer, so the queue never asked about them and they would have
# published silently (the First Round failure class).
DISPUTES = {
 "alloy":   ("US", "Wikidata joined 'Alloy' to an Australian entity; Alloy is the New York identity-decisioning company (alloy.com)."),
 "automat": ("US", "Wikidata joined 'Automat' to a Netherlands entity; runautomat.com is US-based."),
 "bright":  ("US", "Wikidata joined 'Bright' to a Netherlands entity; Bright Money (brightmoney.co) is US-headquartered."),
 "cedar":   ("US", "Wikidata joined 'Cedar' to a Japanese entity; Cedar is the New York healthcare payments company."),
 "chalk":   ("US", "Wikidata joined 'Chalk' to a Czech entity; chalk.ai is US-based."),
 "condor":  ("US", "Wikidata joined 'Condor' to a French entity; Condor Software is US-based."),
 "depot":   ("US", "Wikidata joined 'Depot' to a Swiss entity; depot.dev is US-based."),
}

STAGE_OVERRIDES = {
 # No site layer carried this row; the record does.
 "bioage-labs": ("Series A", "model", None),
}

EXTRA = {
 "credit-karma": {"entry_stage_confidence": "medium",
                  "flags": ["stage_uncited"]},
 "bioage-labs": {"entry_stage_confidence": "medium"},
}

lines = classify.build(1, J, country_disputes=DISPUTES,
                       stage_overrides=STAGE_OVERRIDES, extra=EXTRA)
classify.write(1, lines)
