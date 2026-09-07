import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import classify

M = ("model", None)
J = {
 "sendoso": ("private", "US", "below_1b", None, None, None),
 "sentio": ("private", None, "below_1b", None, None, None),
 "shopittome": ("defunct", "US", "below_1b", None, None, "Shop It To Me shut down in 2017."),
 "siftery": ("acquired", "US", "below_1b", None, None, "acq. by SaaSquatch/Sumo Logic-era consolidation; the product was folded in."),
 "simplifeye": ("private", "US", "below_1b", None, None, None),
 "singularity": ("private", "US", "below_1b", None, None, None),
 "smack": ("private", "US", "below_1b", None, None, None),
 "smartling": ("private", "US", "below_1b", None, None, None),
 "snowball": ("private", None, "below_1b", None, None, None),
 "socialim": ("defunct", "US", "below_1b", None, None, "Social.im of the 2008-2011 era; ceased operations."),
 "sols": ("acquired", "US", "below_1b", None, None, "SOLS (3D-printed orthotics) wound down; assets sold."),
 "solum": ("private", None, "below_1b", None, None, None),
 "solvemedia": ("acquired", "US", "below_1b", None, None, "acq. by Digital River, 2015."),
 "sooth-labs": ("private", "US", "below_1b", None, None, None),
 "spoke": ("acquired", "US", "below_1b", None, None, "acq. by Atlassian, 2021 (as atSpoke)."),
 "spool": ("acquired", "US", "below_1b", None, None, "acq. by Facebook, 2012."),
 "spring-discovery": ("private", "US", "below_1b", None, None, None),
 "sprout": (None, None, "below_1b", None, None, None),
 "sunshine": ("private", None, "below_1b", None, None, "Sunshine (Marissa Mayer's Lumi Labs) -- contacts and photo apps."),
 "survios": ("private", None, "below_1b", None, None, None),
 "swift-navigation": ("private", "US", "below_1b", None, None, None),
 "switch": ("private", None, "below_1b", None, None, None),
 "tapulous": (None, None, "below_1b", None, None, "acq. by Disney, July 2010 (Tap Tap Revenge); the studio was later closed, which is why the layer reads defunct."),
 "teamable": ("private", "US", "below_1b", None, None, None),
 "tello": ("defunct", "US", "below_1b", None, None, None),
 "the-climate-corporation": (None, None, "below_1b", None, None, "acq. by Monsanto, Oct 2013 ($1.1B). The CMS records this entry as 'Common', i.e. a common-stock position rather than a priced round; under D-T3 that is a venture entry taken at scale, so entry_stage is Growth."),
 "the-supplant-company": ("private", "GB", "below_1b", None, None, "Cambridge, UK; sugar replacement from plant fibre."),
 "thinkbright-mx": ("private", "MX", "below_1b", None, None, None),
 "tilt": (None, None, "below_1b", None, None, "acq. by Airbnb, 2017 (acqui-hire); Tilt/Crowdtilt's consumer product was retired."),
 "tivli": ("acquired", "US", "below_1b", None, None, "Tivli became Philo; the campus-TV product was rebuilt as the streaming service."),
 "top-hat-monocle": ("private", "CA", "below_1b", None, None, "Top Hat (formerly Top Hat Monocle), Toronto."),
 "topfunnel": ("acquired", "US", "below_1b", None, None, None),
 "trackvia": ("private", "US", "below_1b", None, None, None),
 "trialspark": ("private", "US", "below_1b", None, None, "Now Formation Bio."),
 "triplebyte": ("acquired", "US", "below_1b", None, None, "acq. by Karat, 2022."),
 "trivop": ("defunct", "US", "below_1b", None, None, None),
 "troops": ("acquired", "US", "below_1b", None, None, "acq. by Salesforce, 2022."),
 "trueaccord": ("private", "US", "below_1b", None, None, None),
 "trusted-health": ("private", "US", "below_1b", None, None, None),
 "turvo": ("private", "US", "below_1b", None, None, None),
 "twice": ("acquired", "US", "below_1b", None, None, "acq. by eBay, 2015."),
}

DISPUTES = {
 "snowball": ("US", "Wikidata joined 'Snowball' to a Chinese entity; flagged as a desk prior."),
 "solum":   ("US", "Wikidata joined 'Solum' to a Norwegian entity; Solum was a Silicon Valley agricultural-analytics company (acq. by Monsanto, 2014)."),
 "sprout":  ("US", "Wikidata joined 'Sprout' to a Japanese entity; flagged as a desk prior."),
 "sunshine": ("US", "Wikidata joined 'Sunshine' to a French entity; Sunshine (Lumi Labs) is a Palo Alto company."),
 "survios": ("US", "Wikidata returned a raw genid URL rather than a country -- not a value at all. Survios is a Los Angeles VR studio."),
 "switch":  ("US", "Wikidata joined 'Switch' to a UK entity; flagged as a desk prior."),
 "sentio":  ("US", "Wikidata's single-token join is unreliable here; flagged as a desk prior."),
}

STAGE_OVERRIDES = {
 "sendoso": ("Series A", *M), "sentio": ("Seed", *M), "shopittome": ("Seed", *M),
 "socialim": ("Seed", *M), "solvemedia": ("Series A", *M),
 "spring-discovery": ("Seed", *M), "sprout": ("Seed", *M),
 "sunshine": ("Seed", *M), "teamable": ("Seed", *M), "tello": ("Seed", *M),
 "the-supplant-company": ("Series A", *M), "thinkbright-mx": ("Seed", *M),
 "tivli": ("Seed", *M), "topfunnel": ("Seed", *M), "trialspark": ("Series A", *M),
 "trivop": ("Seed", *M), "trusted-health": ("Series A", *M), "turvo": ("Series A", *M),
 "twice": ("Seed", *M), "sooth-labs": ("Seed", *M), "snowball": ("Seed", *M),
 "solum": ("Seed", *M), "sols": ("Seed", *M), "siftery": ("Seed", *M),
 "top-hat-monocle": ("Series A", *M),
 "the-climate-corporation": ("Growth", *M),
}

LOW = {"entry_stage_confidence": "low", "flags": ["stage_prior"]}
MED = {"entry_stage_confidence": "medium"}
PRIOR = {"hq_country_confidence": "low", "flags": ["country_prior"]}
EXTRA = {
 "sprout": {"status": "defunct", "status_confidence": "medium",
   "flags": ["model_disputes_source", "country_prior", "stage_prior"],
   "hq_country_confidence": "low", "entry_stage_confidence": "low",
   "note": "Country disputed (Wikidata: Japan); status kept as defunct."},
 "tapulous": {"status": "acquired", "status_confidence": "high",
   "flags": ["model_disputes_source"],
   "note": "Status disputed: the deterministic layer recorded `defunct`. "
           "Tapulous was ACQUIRED by Disney in July 2010; the studio's later "
           "closure is a post-acquisition event (§6)."},
 "tilt": {"status": "acquired", "status_confidence": "high",
   "flags": ["model_disputes_source"],
   "note": "Status disputed: the layer recorded `acquired` and that is right -- "
           "Tilt was bought by Airbnb in 2017; recorded explicitly because the "
           "product shutdown that followed invites a `defunct` reading."},
 "the-climate-corporation": {"entry_stage_confidence": "medium",
   "flags": ["stage_disputes_band"]},
 "survios": {"hq_country_confidence": "high"},
 "snowball": PRIOR, "sentio": PRIOR, "switch": PRIOR,
 "sendoso": MED, "solvemedia": MED, "trialspark": MED, "twice": MED,
 "top-hat-monocle": MED, "the-supplant-company": MED, "tivli": MED,
 "trusted-health": MED, "turvo": MED, "sols": MED, "siftery": MED,
 "socialim": LOW, "shopittome": LOW, "spring-discovery": LOW,
 "teamable": LOW, "tello": LOW, "thinkbright-mx": LOW, "topfunnel": LOW,
 "trivop": LOW, "sooth-labs": LOW, "solum": LOW,
}

classify.write(11, classify.build(11, J, country_disputes=DISPUTES,
                                  stage_overrides=STAGE_OVERRIDES, extra=EXTRA))
