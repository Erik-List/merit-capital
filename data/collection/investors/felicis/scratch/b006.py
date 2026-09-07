import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import classify

J = {
 "atspoke": ("acquired", "US", "below_1b", None, None, "acq. by Atlassian, 2021."),
 "attendio": ("unknown", "US", "below_1b", None, None, "A 2006-2007 felicisventures.com listing (events discovery); no trace after the era, so the state cannot be established."),
 "avidbots": ("private", "CA", "below_1b", None, None, "Kitchener, Ontario; floor-cleaning robots."),
 "avnio": ("private", "GB", "below_1b", None, None, None),
 "baby-com-br": ("acquired", "BR", "below_1b", None, None, "Brazilian baby-goods retailer; folded into Grupo Netshoes."),
 "bitpay": ("private", None, "below_1b", None, None, None),
 "blomma": ("private", "US", "below_1b", None, None, None),
 "bluecore": (None, None, None, None, None, None),
 "breezy": ("private", "US", "below_1b", None, None, None),
 "brightroll": ("acquired", None, "below_1b", None, None, None),
 "bump-technologies": ("acquired", "US", "below_1b", None, None, "acq. by Google, 2013; the Bump and Flock apps were retired in 2014."),
 "c1": ("private", None, "below_1b", None, None, None),
 "cake-financial": ("acquired", "US", "below_1b", None, None, "acq. by E*TRADE, 2010."),
 "cardash": ("private", "US", "below_1b", None, None, None),
 "cardspring": ("acquired", "US", "below_1b", None, None, "acq. by Twitter, 2014."),
 "carwoo": ("defunct", "US", "below_1b", None, None, "CarWoo! shut down in 2014."),
 "chloe-isabel": ("defunct", "US", "below_1b", None, None, "Chloe + Isabel wound the business down in 2019."),
 "chomp": ("acquired", "US", "below_1b", None, None, "acq. by Apple, Feb 2012."),
 "circulate": ("private", "US", "below_1b", None, None, None),
 "civitas-learning": ("private", "US", "below_1b", None, None, None),
 "clearslide": ("acquired", "US", "below_1b", None, None, "acq. by Corel, 2018."),
 "cleo": ("private", None, "below_1b", None, None, None),
 "clora": ("private", "US", "below_1b", None, None, None),
 "codefights": ("private", "US", "below_1b", None, None, None),
 "codesignal": ("private", "US", "below_1b", None, None, None),
 "column-tax": ("private", "US", "below_1b", None, None, "$21.7M Series A, 2022."),
 "commsor": ("private", "US", "below_1b", None, None, None),
 "contextlogic": (None, "US", None, None, None, None),
 "corridor": ("private", None, "below_1b", None, None, None),
 "counsyl": ("acquired", None, "below_1b", None, None, "acq. by Myriad Genetics, 2018 (~$375M)."),
 "creativelive": ("acquired", "US", "below_1b", None, None, "acq. by Fender, 2021."),
 "criya": ("private", "US", "below_1b", None, None, None),
 "crowdflower": ("acquired", "US", "below_1b", None, None, "Renamed Figure Eight in 2018; acq. by Appen, 2019."),
 "crowdtilt": ("defunct", "US", "below_1b", None, None, "Crowdtilt wound down after pivoting to Crowdhoster."),
 "cruise": ("acquired", "US", "below_1b", None, None, "acq. by General Motors, 2016; GM ended the robotaxi programme in Dec 2024."),
 "cymmetria": ("defunct", "IL", "below_1b", None, None, "Israeli deception-security company; ceased operations."),
 "dailybooth": ("defunct", "US", "below_1b", None, None, "Shut down in 2012."),
 "datologyai": ("private", "US", "below_1b", None, None, None),
 "deeptrace": ("private", "NL", "below_1b", None, None, "Amsterdam-based deepfake detection; now Sensity AI."),
}

DISPUTES = {
 "c1":   ("US", "Wikidata joined 'C1' to a Japanese entity; the Felicis row is a US company. Flagged as a desk prior."),
 "cleo": ("US", "Wikidata joined 'Cleo' to a Canadian entity; the Felicis row is a 2018 US seed. Flagged as a desk prior."),
}

STAGE_OVERRIDES = {
 "avnio": ("Seed", "model", None),
 "bump-technologies": ("Seed", "model", None),
 "cake-financial": ("Seed", "model", None),
 "carwoo": ("Seed", "model", None),
 "clora": ("Series A", "model", None),
 "column-tax": ("Series A", "model", None),
 "commsor": ("Seed", "model", None),
 "contextlogic": ("Seed", "model", None),
 "criya": ("Seed", "model", None),
 "crowdtilt": ("Seed", "model", None),
 "dailybooth": ("Seed", "model", None),
 "datologyai": ("Series A", "model", None),
 "attendio": ("Seed", "model", None),
 # Layers conflict and the golden set lists it unresolved: the CMS says
 # Series A today, but the firm's own listing said Series A in 2012 and then
 # Seed for four straight years (2013-2016). BrightRoll's own ladder is a
 # Nov-2006 Series A, an Oct-2007 Series B, then C and D; Felicis's entry is
 # its 2007 angel era. Published on the firm's sustained reading, medium.
 "brightroll": ("Seed", "model", None),
}

EXTRA = {
 "brightroll": {"entry_stage_confidence": "medium", "flags": ["stage_uncited"],
   "note": "acq. by Yahoo, 2014 ($640M). Entry stage contested: the live CMS "
           "says Series A; the firm's own archived listing said Series A in "
           "2012 and Seed in 2013, 2014, 2015 and 2016. Published Seed on the "
           "firm's sustained reading, at medium confidence; golden.json lists "
           "it unresolved and no contemporaneous source names the round."},
 "codefights": {"flags": ["duplicate_suspected"],
   "note": "CodeFights renamed to CodeSignal; `codesignal` is also a base row (identity-merges.json)."},
 "crowdflower": {"flags": ["duplicate_suspected"],
   "note": "CrowdFlower renamed to Figure Eight; `figure-eight` is also a base row (identity-merges.json)."},
 "contextlogic": {"flags": ["duplicate_suspected"], "entry_stage_confidence": "low",
   "note": "ContextLogic is Wish's registered name; `wish` is also a base row (identity-merges.json)."},
 "datologyai": {"flags": ["duplicate_suspected"], "entry_stage_confidence": "medium",
   "note": "Duplicate rendering of `datology` (identity-merges.json)."},
 "c1": {"hq_country_confidence": "low", "flags": ["country_prior"]},
 "cleo": {"hq_country_confidence": "low", "flags": ["country_prior"]},
 "attendio": {"entry_stage_confidence": "low", "flags": ["stage_prior"]},
 "avnio": {"entry_stage_confidence": "low", "flags": ["stage_prior"]},
 "criya": {"entry_stage_confidence": "low", "flags": ["stage_prior"]},
 "dailybooth": {"entry_stage_confidence": "low", "flags": ["stage_prior"]},
 "crowdtilt": {"entry_stage_confidence": "low", "flags": ["stage_prior"]},
 "carwoo": {"entry_stage_confidence": "medium"},
 "cake-financial": {"entry_stage_confidence": "medium"},
 "bump-technologies": {"entry_stage_confidence": "medium"},
 "clora": {"entry_stage_confidence": "medium"},
 "column-tax": {"entry_stage_confidence": "medium"},
 "commsor": {"entry_stage_confidence": "medium"},
}

classify.write(6, classify.build(6, J, country_disputes=DISPUTES,
                                 stage_overrides=STAGE_OVERRIDES, extra=EXTRA))
