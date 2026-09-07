import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import classify

M = ("model", None)
J = {
 "outright": ("acquired", None, "below_1b", None, None, "acq. by GoDaddy, 2012 (became GoDaddy Bookkeeping)."),
 "overture-life": ("private", "ES", "below_1b", None, None, "Barcelona-based fertility automation."),
 "paravision-ai": ("private", "US", "below_1b", None, None, None),
 "peerstreet": ("defunct", "US", "below_1b", None, None, "Filed for Chapter 11 in June 2023 and wound down; §6 reads a bankruptcy filing with no sale as defunct."),
 "perfect-coffee": ("acquired", "US", "below_1b", None, None, None),
 "petasense": ("private", "US", "below_1b", None, None, None),
 "pf-logo": ("unknown", "US", "below_1b", None, None, None),
 "philo": ("private", None, "below_1b", None, None, None),
 "pickwick-weller": ("defunct", "US", "below_1b", None, None, None),
 "plancast": ("acquired", "US", "below_1b", None, None, "acq. by Active.com, 2012."),
 "planet-labs": ("public", None, None, None, None, "NYSE: PL. Range deferred to the A/B pass. Duplicate rendering of `planet`."),
 "plotwatt": ("defunct", "US", "below_1b", None, None, None),
 "plusmo": ("defunct", "US", "below_1b", None, None, "Mobile widgets company of the 2006-2010 era."),
 "posterous": (None, "US", "below_1b", None, None, "acq. by Twitter, 2012; the service was shut down in 2013, which is why the deterministic layer reads defunct."),
 "postroller": ("defunct", "US", "below_1b", None, None, None),
 "powerset": (None, None, "below_1b", None, None, "acq. by Microsoft, 2008 (~$100M); the semantic-search technology went into Bing."),
 "practice-fusion": ("acquired", None, "below_1b", None, None, "acq. by Allscripts, 2018 ($100M)."),
 "predictspring": ("private", "US", "below_1b", None, None, None),
 "producteev": ("acquired", "US", "below_1b", None, None, "acq. by Jive Software, 2012."),
 "proteinqure": ("private", "CA", "below_1b", None, None, "Toronto-based computational protein design."),
 "quarterzip": ("private", "US", "below_1b", None, None, None),
 "quartz-systems": ("private", "US", "below_1b", None, None, None),
 "recursion-pharmaceuticals": (None, None, None, None, None, "Duplicate rendering of `recursion` (Nasdaq: RXRX)."),
 "relateiq": ("acquired", None, "below_1b", None, None, "acq. by Salesforce, 2014 (~$390M); became SalesforceIQ."),
 "reservoir-neuroscience": ("private", "US", "below_1b", None, None, None),
 "resourcely": ("private", "US", "below_1b", None, None, None),
 "richrelevance": ("acquired", "US", "below_1b", None, None, "acq. by Algonomy/Manthan, 2021."),
 "romotive": ("defunct", "US", "below_1b", None, None, None),
 "room-77": ("defunct", "US", "below_1b", None, None, "Hotel search; the technology went to Google in 2014 and the consumer site closed."),
 "rr-logo": ("unknown", "US", "below_1b", None, None, None),
 "runway": ("private", "US", None, None, None, "Felicis led the $50M Series C in Dec 2022 at a $500M valuation."),
 "salvo-health": ("private", "US", "below_1b", None, None, None),
 "sano-intelligence": ("defunct", "US", "below_1b", None, None, None),
 "savioke": ("acquired", None, "below_1b", None, None, "Savioke became Relay Robotics."),
 "saynow": ("acquired", "US", "below_1b", None, None, "acq. by Google, Jan 2011."),
 "scaled-interference": ("private", "US", "below_1b", None, None, None),
 "scalyr": ("acquired", "US", "below_1b", None, None, "acq. by SentinelOne, 2021 ($155M)."),
 "scanscout": ("acquired", "US", "below_1b", None, None, "acq. by Tremor Media, 2011 (became Tremor Video)."),
 "sendori": ("acquired", "US", "below_1b", None, None, "acq. by IAC, 2011."),
}

DISPUTES = {
 "philo": ("US", "Wikidata joined 'Philo' to a German entity; Philo is the San Francisco streaming-TV company."),
}

STAGE_OVERRIDES = {
 "overture-life": ("Seed", *M), "paravision-ai": ("Series A", *M),
 "pf-logo": ("Seed", *M), "pickwick-weller": ("Seed", *M),
 "plancast": ("Seed", *M), "postroller": ("Seed", *M),
 "proteinqure": ("Seed", *M), "quartz-systems": ("Seed", *M),
 "reservoir-neuroscience": ("Seed", *M), "resourcely": ("Seed", *M),
 "romotive": ("Seed", *M), "room-77": ("Seed", *M), "rr-logo": ("Seed", *M),
 "salvo-health": ("Seed", *M), "scanscout": ("Series A", *M),
 "producteev": ("Seed", *M), "perfect-coffee": ("Seed", *M),
 "quarterzip": ("Seed", *M), "recursion-pharmaceuticals": ("Series A", *M),
 "planet-labs": ("Growth", *M),
}

LOW = {"entry_stage_confidence": "low", "flags": ["stage_prior"]}
MED = {"entry_stage_confidence": "medium"}
EXTRA = {
 "posterous": {"status": "acquired", "status_confidence": "high",
   "flags": ["model_disputes_source"],
   "note": "Status disputed: the deterministic layer recorded `defunct`. "
           "Posterous was ACQUIRED by Twitter in March 2012; the service was "
           "shut down afterwards, which is a post-acquisition event and does "
           "not change the outcome class (§6: IPO'd-then-acquired is acquired, "
           "and so is acquired-then-shut)."},
 "pf-logo": {**LOW, "flags": ["stage_prior", "parser_artifact"],
   "note": "Unresolved logo-file slug from the 2010 era (decisions.md R6); no "
           "company could be identified from two letters, so it is reported "
           "rather than guessed."},
 "rr-logo": {**LOW, "flags": ["stage_prior", "parser_artifact"],
   "note": "Unresolved logo-file slug from the 2008-2010 eras (decisions.md R6)."},
 "planet-labs": {"flags": ["duplicate_suspected"], **MED,
   "note": "Duplicate rendering of `planet` (Planet Labs, NYSE: PL)."},
 "recursion-pharmaceuticals": {"flags": ["duplicate_suspected"], **MED,
   "note": "Duplicate rendering of `recursion`."},
 "overture-life": MED, "paravision-ai": MED, "proteinqure": MED,
 "scanscout": MED, "producteev": MED, "room-77": MED, "plancast": MED,
 "pickwick-weller": LOW, "postroller": LOW, "quartz-systems": LOW,
 "reservoir-neuroscience": LOW, "resourcely": LOW, "romotive": LOW,
 "salvo-health": LOW, "quarterzip": LOW, "perfect-coffee": LOW,
}

classify.write(10, classify.build(10, J, country_disputes=DISPUTES,
                                  stage_overrides=STAGE_OVERRIDES, extra=EXTRA))
