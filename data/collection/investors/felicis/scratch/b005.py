import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import classify

J = {
 "terra-security": ("private", "IL", "below_1b", None, None, None),
 "testbox": ("private", "US", "below_1b", None, None, None),
 "themis": ("private", "US", "below_1b", None, None, None),
 "third-dimension": ("private", "US", "below_1b", None, None, None),
 "thirdlove": ("private", "US", "below_1b", None, None, None),
 "tines": ("private", None, None, None, None, "Dublin-based security automation company; range deferred to the A/B pass."),
 "topkey": ("private", "US", "below_1b", None, None, None),
 "torch": ("private", "US", "below_1b", None, None, None),
 "twitch": ("acquired", "US", "below_1b", None, None, "acq. by Amazon, Aug 2014 (~$970M). Entered as Justin.tv at the 2007 $8M seed."),
 "tynker": ("acquired", None, "below_1b", None, None, "acq. by BYJU'S, 2021."),
 "vannevar-labs": ("private", "US", None, None, None, None),
 "verkada": (None, None, None, None, None, None),
 "violet-labs": ("private", "US", "below_1b", None, None, None),
 "voiceflow": ("private", None, "below_1b", None, None, "Toronto-based conversational-AI design tool; $20M Series A, 2021."),
 "warby-parker": (None, None, None, None, None, None),
 "warmly": ("private", "US", "below_1b", None, None, None),
 "weights-biases": ("acquired", "US", "below_1b", None, None, "acq. by CoreWeave, 2025."),
 "wherobots": ("private", "US", "below_1b", None, None, "$21.5M Series A, Nov 2024."),
 "wish": ("acquired", None, "below_1b", None, None, "The Wish marketplace was sold to Qoo10 in 2024; the listed shell (ContextLogic) retained the NOLs. The operating business changed hands, so the row reads acquired."),
 "wordware": ("private", "US", "below_1b", None, None, None),
 "xilis-2-a44dc1b6-a4d3-4e72-b91c-50b58e3b9307": ("private", None, "below_1b", None, None, None),
 "yutori": ("private", "US", "below_1b", None, None, None),
 "zefr": ("private", "US", "below_1b", None, None, None),
 "zenreach": ("private", "US", "below_1b", None, None, None),
 "zipline": (None, None, None, None, None, None),
 "zubale": ("private", "MX", "below_1b", None, None, "Mexico City-based commerce-operations marketplace."),
 "zylon": ("private", "ES", "below_1b", None, None, "Madrid-based private-GPT company (the PrivateGPT team)."),
 "1000memories": ("acquired", "US", "below_1b", None, None, "acq. by Ancestry.com, 2012."),
 "aaru": ("private", "US", "below_1b", None, None, None),
 "activehours": ("private", "US", "below_1b", None, None, None),
 "adaptive-innovations": ("private", "US", "below_1b", None, None, None),
 "adcopy": ("unknown", "US", "below_1b", None, None, "A 2008-2010 felicisventures.com listing with no trace after the era; state cannot be established."),
 "aira-2": ("private", "US", "below_1b", None, None, None),
 "aira-io": ("private", "US", "below_1b", None, None, None),
 "airware": (None, None, "below_1b", None, None, "Ceased operations Sept 2018; the assets went to Delair, so the row reads acquired with a successor note rather than defunct (§6)."),
 "alma-campus": ("private", "US", "below_1b", None, None, None),
 "aloha": ("private", None, "below_1b", None, None, None),
 "altitude-networks": ("private", "US", "below_1b", None, None, None),
 "any-do": ("private", "IL", "below_1b", None, None, "Tel Aviv-based task manager."),
 "appjet": ("acquired", "US", "below_1b", None, None, "acq. by Google, Dec 2009; AppJet's Etherpad became part of Google Wave and was later open-sourced."),
 "appurify": ("acquired", "US", "below_1b", None, None, "acq. by Google, 2014."),
 "arena": (None, None, None, None, None, None),
 "artemis": ("private", None, "below_1b", None, None, None),
 "artspace": ("private", None, "below_1b", None, None, None),
 "atalanta": ("private", None, "below_1b", None, None, None),
}

DISPUTES = {
 "wish":     ("US", "Wikidata joined 'Wish' to a Japanese entity; Wish (ContextLogic) is the San Francisco marketplace."),
 "aloha":    ("US", "Wikidata joined 'Aloha' to a Philippine entity; the Felicis row is a 2017 US seed. Flagged as a desk prior."),
 "artemis":  ("US", "Wikidata joined 'Artemis' to a German entity; artemissecurity.com is US-based."),
 "atalanta": ("US", "Wikidata joined 'Atalanta' to a French entity; atalanta.tech is US-based."),
 "arena":    ("US", "Wikidata joined 'Arena' to a UK entity; arena.ai is US-based."),
}

STAGE_OVERRIDES = {
 "1000memories": ("Seed", "model", None),
 "aira-2": ("Series A", "model", None),
 "altitude-networks": ("Seed", "model", None),
 "artspace": ("Series A", "model", None),
 "zenreach": ("Series A", "model", None),
 "adcopy": ("Seed", "model", None),
}

EXTRA = {
 # The float sweep's name-collision class (§8 duty 8): a public-float hit is a
 # registrant match, not an identity.
 "arena": {"status": "private", "status_confidence": "high",
   "flags": ["model_disputes_source"],
   "note": "Status disputed: the float sweep recorded `public`, which is a "
           "registrant collision with a listed company sharing the word "
           "'Arena'. Felicis's Arena (arena.ai) is private -- the firm's own "
           "page says it led the Series A after investing in the seed."},
 "xilis-2-a44dc1b6-a4d3-4e72-b91c-50b58e3b9307": {
   "flags": ["duplicate_suspected"],
   "note": "CMS-side artifact: the slug carries a raw UUID suffix, so this is "
           "very likely a duplicate of a `xilis` row. Flagged, not merged (§8). "
           "Xilis is a Durham, NC oncology company."},
 "activehours": {"flags": ["duplicate_suspected"],
   "note": "Activehours renamed to Earnin in 2017; `earnin` is also a base row. "
           "Flagged as a suspected duplicate rather than merged in-run (§8)."},
 "zenreach": {"flags": ["duplicate_suspected"], "entry_stage_confidence": "medium",
   "note": "Zenreach rebranded to Adentro; `adentro` is also a base row. "
           "Flagged as a suspected duplicate rather than merged in-run (§8)."},
 "aira-2": {"flags": ["duplicate_suspected"], "entry_stage_confidence": "low",
   "note": "Very likely a duplicate of `aira-io`. Flagged, not merged."},
 "adcopy": {"entry_stage_confidence": "low", "flags": ["stage_prior"]},
 "1000memories": {"entry_stage_confidence": "medium"},
 "altitude-networks": {"entry_stage_confidence": "medium"},
 "artspace": {"entry_stage_confidence": "low", "flags": ["stage_prior"]},
 "aloha": {"hq_country_confidence": "low", "flags": ["country_prior"]},
 "artemis": {"hq_country_confidence": "medium"},
 "atalanta": {"hq_country_confidence": "medium"},
 "xilis-2-a44dc1b6-a4d3-4e72-b91c-50b58e3b9307_c": {},
}

classify.write(5, classify.build(5, J, country_disputes=DISPUTES,
                                 stage_overrides=STAGE_OVERRIDES, extra=EXTRA))
