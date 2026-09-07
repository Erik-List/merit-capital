import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import classify

J = {
 "dig-security": ("acquired", "US", "below_1b", None, None, "acq. by Palo Alto Networks, 2023 (~$400M reported)."),
 "disco-technology": ("private", "US", "below_1b", None, None, None),
 "distributed-spectrum": ("private", "US", "below_1b", None, None, None),
 "distru": ("private", "US", "below_1b", None, None, None),
 "donotpay": ("private", "US", "below_1b", None, None, None),
 "dovetail": ("private", None, "below_1b", None, None, None),
 "dylibso": ("private", "US", "below_1b", None, None, None),
 "earnin": ("private", "US", "below_1b", None, None, "Formerly Activehours."),
 "edia": ("private", None, "below_1b", None, None, None),
 "elemy": ("private", "US", None, None, None, None),
 "elevate": ("private", "US", "below_1b", None, None, None),
 "emailage": ("acquired", None, "below_1b", None, None, "acq. by LexisNexis Risk Solutions, 2020 (~$480M reported)."),
 "entalpic": ("private", "FR", "below_1b", None, None, "Paris-based AI-for-materials company."),
 "entire": ("private", "US", "below_1b", None, None, None),
 "ethena": ("private", None, "below_1b", None, None, None),
 "eventual-computing": ("private", "US", "below_1b", None, None, None),
 "evertune": ("private", None, "below_1b", None, None, None),
 "exowatt": ("private", "US", "below_1b", None, None, None),
 "extra-by-buildforever": ("private", "US", "below_1b", None, None, None),
 "fellow": ("private", "US", "below_1b", None, None, None),
 "fifth-door": ("private", "US", "below_1b", None, None, None),
 "fitbit": (None, None, "below_1b", None, None, "acq. by Google, Jan 2021 ($2.1B). Acquired rows carry a null figure."),
 "flexport": (None, None, None, None, None, None),
 "flower-labs": ("private", "US", "below_1b", None, None, None),
 "fluxx": ("private", "US", "below_1b", None, None, None),
 "formation-bio": ("private", "US", None, None, None, None),
 "fundersclub": ("private", "US", "below_1b", None, None, None),
 "general-proximity": ("private", "US", "below_1b", None, None, None),
 "genesis-therapeutics": ("private", "US", "below_1b", None, None, None),
 "ginkgo-bioworks": (None, None, None, None, None, None),
 "goldsky": ("private", "US", "below_1b", None, None, None),
 "good-dog": ("private", "US", "below_1b", None, None, None),
 "granza-bio": ("private", "GB", "below_1b", None, None, "Oxford spin-out; $7M seed from Felicis and Y Combinator, 2024."),
 "greenhouse-software": (None, "US", "below_1b", None, None, "acq. by TPG, 2024 (majority recapitalisation)."),
 "greenplaces": ("private", None, "below_1b", None, None, None),
 "groundswell": ("private", "US", "below_1b", None, None, None),
 "guardant-health": (None, None, None, None, None, None),
 "guideline": ("private", "US", None, None, None, None),
 "guild-education": ("private", "US", None, None, None, None),
 "gusto": (None, None, None, None, None, None),
 "hearsay-systems": ("private", "US", "below_1b", None, None, None),
 "hippo-insurance": ("public", "US", None, None, None, "NYSE: HIPO. Range deferred to the A/B pass for a cited market cap."),
 "juniper-square": ("private", "US", None, None, None, None),
 "kandji": ("private", None, "below_1b", None, None, None),
 "key": ("private", None, "below_1b", None, None, None),
}

DISPUTES = {
 "gusto": ("US", "Wikidata joined 'Gusto' to a Netherlands entity; Gusto is the San Francisco payroll company."),
 "key":   ("US", "Wikidata joined 'Key' to a Japanese entity (the visual-novel studio). The Felicis row is a 2024 seed on a US company; US is a flagged desk prior, not an identification."),
}

STAGE_OVERRIDES = {
 # The golden key's diagnostic row: the CMS enum says Seed (Ginkgo's stage
 # when listed -- the seed was Y Combinator's S14) and the circles ladder says
 # Series A. Felicis entered at the $9M Series A of March 2015. The layers
 # conflict, so build-entry-stage-layer.py withheld the row and it is judged
 # here against the external citation.
 "ginkgo-bioworks": ("Series A", "web_verified",
   "https://www.businesswire.com/news/home/20150318005213/en/Ginkgo-Bioworks-Raises-9-Million-in-Funding-from-Felicis-Ventures-OS-Fund-and-Data-Collective"),
 "eventual-computing": ("Series A", "model", None),
 "extra-by-buildforever": ("Seed", "model", None),
 "genesis-therapeutics": ("Series A", "model", None),
 "hearsay-systems": ("Series A", "model", None),
}

EXTRA = {
 # Deliberate dispute of a pre-filled value the queue never asked about:
 # the deterministic layer marked Ginkgo `acquired`, but it went public by
 # SPAC in 2021 and still trades as DNA on the NYSE. §3: never silently
 # accept a value known to be wrong.
 "ginkgo-bioworks": {"status": "public", "status_confidence": "high",
   "flags": ["model_disputes_source"],
   "note": "Status disputed: the deterministic layer recorded `acquired`; "
           "Ginkgo Bioworks went public via SPAC in Sep 2021 and trades as "
           "DNA on the NYSE. Range deferred to the A/B pass for a cited cap. "
           "Entry stage is the golden set's diagnostic row -- the CMS enum "
           "said Seed, the archived circles ladder said Series A, and the "
           "March-2015 $9M Series A is the entry."},
 "key": {"hq_country_confidence": "low", "flags": ["country_prior"]},
 "eventual-computing": {"entry_stage_confidence": "medium"},
 "extra-by-buildforever": {"entry_stage_confidence": "low", "flags": ["stage_prior"]},
 "genesis-therapeutics": {"entry_stage_confidence": "medium"},
 "hearsay-systems": {"entry_stage_confidence": "medium"},
 "flower-labs": {"hq_country_confidence": "medium"},
}

classify.write(2, classify.build(2, J, country_disputes=DISPUTES,
                                 stage_overrides=STAGE_OVERRIDES, extra=EXTRA))
