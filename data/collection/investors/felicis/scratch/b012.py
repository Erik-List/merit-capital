import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import classify

M = ("model", None)
J = {
 "twitter": ("unknown", "US", "below_1b", None, None, None),
 "ultimate-ai": ("acquired", "FI", "below_1b", None, None, "Helsinki-based; acq. by Zendesk, 2024."),
 "unconventional-ai": ("private", "US", "below_1b", None, None, None),
 "venturebeat": ("private", "US", "below_1b", None, None, "A genuine 2008-2010 portfolio card in the firm's own ASP.NET repeater, with the company URL on the card."),
 "vessyl": ("defunct", "US", "below_1b", None, None, "Mark One's Vessyl smart cup; the company wound down."),
 "vicarious": ("acquired", None, "below_1b", None, None, "Vicarious AI acq. by Alphabet/Intrinsic, 2022."),
 "voi": (None, None, None, None, None, None),
 "voicestar": ("acquired", "US", "below_1b", None, None, "acq. by Marchex, 2007 ($28M)."),
 "vook": ("acquired", "US", "below_1b", None, None, "Vook became Pronoun; wound down in 2016."),
 "votizen": ("acquired", None, "below_1b", None, None, "acq. by Causes/Brigade, 2013."),
 "walker-company": (None, None, "below_1b", None, None, "Walker & Company Brands (Bevel, Form) acq. by Procter & Gamble, 2018."),
 "walrus-ai": ("acquired", "US", "below_1b", None, None, None),
 "wavii": ("acquired", "US", "below_1b", None, None, "acq. by Google, 2013 (~$30M)."),
 "weatherbill": ("acquired", "US", "below_1b", None, None, "WeatherBill renamed itself The Climate Corporation; acq. by Monsanto, 2013."),
 "webs": ("acquired", "US", "below_1b", None, None, "Webs.com (formerly Freewebs) acq. by Vistaprint, 2011 ($117.5M)."),
 "wedding-party": ("acquired", "US", "below_1b", None, None, "acq. by WeddingWire, 2015."),
 "weddington-way": ("acquired", "US", "below_1b", None, None, "acq. by Gap Inc., 2016."),
 "weebly": ("acquired", "US", "below_1b", None, None, "acq. by Square/Block, 2018 ($365M)."),
 "wild-earth": ("private", "US", "below_1b", None, None, None),
 "wildfire": ("acquired", None, "below_1b", None, None, "Wildfire Interactive acq. by Google, 2012 (~$350M)."),
 "workbase": ("defunct", "US", "below_1b", None, None, None),
 "woven": ("acquired", "US", "below_1b", None, None, "acq. by Slack, 2021."),
 "yapta": ("acquired", "US", "below_1b", None, None, "acq. by Coupa, 2020."),
 "yes-inc": ("defunct", "US", "below_1b", None, None, None),
 "yotascale": ("private", "US", "below_1b", None, None, None),
 "yume": (None, "US", "below_1b", None, None, "acq. by RhythmOne, 2018; YuMe had IPO'd in 2013, and §6 reads IPO'd-then-acquired as acquired."),
 "zaarly": ("defunct", "US", "below_1b", None, None, None),
 "zinch": ("acquired", "US", "below_1b", None, None, "acq. by Chegg, 2011."),
 "zodiac": ("acquired", "US", "below_1b", None, None, "acq. by Nike, 2018."),
}

DISPUTES = {
 "voi": ("SE", "Kept the Wikidata country (Sweden) -- Voi Technology is Stockholm-based and this is a multi-token-grade join that checks out; recorded explicitly because ruling R5 demotes the layer by default."),
}

STAGE_OVERRIDES = {
 "twitter": ("Seed", *M), "unconventional-ai": ("Seed", *M),
 "venturebeat": ("Seed", *M), "walrus-ai": ("Seed", *M),
 "weatherbill": ("Series A", *M), "wedding-party": ("Seed", *M),
 "weddington-way": ("Series A", *M), "workbase": ("Seed", *M),
 "woven": ("Seed", *M), "yotascale": ("Series A", *M),
 "voi": ("Growth", *M), "vicarious": ("Seed", *M), "votizen": ("Seed", *M),
 "walker-company": ("Growth", *M), "wavii": ("Seed", *M), "webs": ("Seed", *M),
}

LOW = {"entry_stage_confidence": "low", "flags": ["stage_prior"]}
MED = {"entry_stage_confidence": "medium"}
EXTRA = {
 "twitter": {**LOW, "flags": ["stage_prior", "parser_artifact"],
   "note": "PARSER ARTIFACT, not a member: the 2011 listing rendered the site's "
           "social footer (twitter-small.jpg) with the same images/logos/ path "
           "as its portfolio cards. Removed from the parsed source; this row "
           "disappears at the scheduled rebuild (decisions.md R7)."},
 "yume": {"status": "acquired", "status_confidence": "high"},
 "walker-company": {"status": "acquired", "status_confidence": "high", **MED},
 "voi": {"hq_country_confidence": "high", **MED},
 "venturebeat": MED, "weatherbill": MED, "weddington-way": MED,
 "yotascale": MED, "vicarious": MED, "votizen": MED, "wavii": MED,
 "webs": MED, "woven": MED, "wedding-party": MED,
 "unconventional-ai": LOW, "walrus-ai": LOW, "workbase": LOW,
}

classify.write(12, classify.build(12, J, country_disputes=DISPUTES,
                                  stage_overrides=STAGE_OVERRIDES, extra=EXTRA))
