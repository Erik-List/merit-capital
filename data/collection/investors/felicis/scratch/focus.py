#!/usr/bin/env python3
"""The `focus` column: one primary value from the closed twelve (§6).

Two passes, in the order §6 prescribes:

1. **The firm's own sector tags**, crosswalked (config.profile.focus_crosswalk).
   Covers 273 of the 277 rows the live CMS tags. The four `Education` rows are
   deliberately left NULL -- education has no home in the closed twelve and
   force-fitting it to SaaS would corrupt the distribution ("null over
   force-fit").
2. **One parametric pass** over the 216 rows with no site tag, which are the
   archived eras the CMS no longer carries.

§6's standing precedence rules are applied over the alias table, not around
it: Security beats SaaS/DevTools/Industrial when security is what the company
sells; Crypto & Web3 beats Fintech for on-chain businesses; consumer devices
are Consumer & Marketplaces; healthcare vertical SaaS is Healthcare & Bio; ad
networks and audience monetization are Media while martech sold as software
stays SaaS; AI & Applied AI means AI is the product, not that the company uses
ML; enterprise infrastructure and networking is Data Infrastructure; chips are
Industrial & Robotics.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from emit import WHO  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "scratch" / "queue" / "focus.out.jsonl"

AI = "AI & Applied AI"; SAAS = "SaaS"; CONS = "Consumer & Marketplaces"
FIN = "Fintech & Payments"; HEALTH = "Healthcare & Bio"; SEC = "Security"
DATA = "Data Infrastructure"; DEV = "DevTools & APIs"; IND = "Industrial & Robotics"
CLIM = "Climate & Energy"; MEDIA = "Media, Gaming & Advertising"; CRYPTO = "Crypto & Web3"

# The 216 rows with no site tag. `None` = outside the closed twelve, reported.
PARAMETRIC = {
 "adentro": SAAS, "conductorone": SEC, "guild-education": None, "kandji": SEC,
 "kudo": SAAS, "literati": CONS, "mark-one-lifestyle-inc": CONS, "talkiq": AI,
 "xilis": HEALTH, "1000memories": CONS, "adcopy": MEDIA, "aira-io": CONS,
 "airware": IND, "alma-campus": None, "aloha": CONS, "any-do": CONS,
 "artspace": CONS, "attendio": CONS, "avidbots": IND, "avnio": SAAS,
 "baby-com-br": CONS, "bitpay": CRYPTO, "bluecore": SAAS, "bookfresh": SAAS,
 "breezy": SAAS, "bump-technologies": CONS, "buzzlogic": MEDIA,
 "cake-financial": FIN, "cardash": CONS, "carwoo": CONS, "chloe-isabel": CONS,
 "civitas-learning": None, "clearslide": SAAS, "cleo": FIN, "clora": HEALTH,
 "codesignal": SAAS, "column-tax": FIN, "commsor": SAAS, "counsyl": HEALTH,
 "creativelive": MEDIA, "criya": SAAS, "crowdtilt": FIN, "cymmetria": SEC,
 "dailybooth": CONS, "dinda-com-br": CONS, "dna-nexus": HEALTH, "dnovo": AI,
 "dogster": CONS, "dojo": SAAS, "dots": MEDIA, "drive-fm": MEDIA,
 "drivetime": MEDIA, "drum-technologies": SAAS, "erply": SAAS, "explo": DATA,
 "factual": DATA, "farmwise": IND, "feedjit": MEDIA, "feedster": MEDIA,
 "feel": HEALTH, "figure-eight": AI, "first-opinion": HEALTH,
 "floravere": CONS, "foodzie": CONS, "freewebs": SAAS, "gali-health": HEALTH,
 "gamalon": AI, "gigster": CONS, "glencoco": SAAS,
 "go-2-ec105164-e34f-460d-92be-c4f14caf5327": None, "go-insurance": FIN,
 "go-maps": CONS, "gobble": CONS, "granular": IND, "greenhouse": SAAS,
 "grove-labs": CONS, "gydget": MEDIA, "hailo": IND, "hall": SAAS,
 "happiest-baby": CONS, "headspin": DEV, "healthiq": HEALTH, "hireart": SAAS,
 "homeboodle": CONS, "homeroom": None, "humansand": AI, "hyperscience": AI,
 "iddiction": MEDIA, "imageshack": CONS, "incountry": DATA, "inkling": None,
 "interaxon": CONS, "january-ai": HEALTH, "juvena-therapeutics": HEALTH,
 "kahuna": SAAS, "kinde": DEV, "kissmetrics": SAAS, "kiwicrate": CONS,
 "komodo": HEALTH, "kryptnostic": SEC, "kyklo": SAAS, "lab-genius": HEALTH,
 "leandata": SAAS, "lighthouse": SAAS, "living-carbon": CLIM, "lm-arena": AI,
 "loomia": DATA, "lovely": CONS, "lucy": CONS, "luma": CONS,
 "made-renovation": CONS, "madkudu": SAAS, "madvertise": MEDIA,
 "marchex-voicestar": MEDIA, "marigold-health": HEALTH, "matchbox": CONS,
 "mattermark": DATA, "mecommerce": CONS, "meili": SAAS, "mindsnacks": None,
 "mixer-labs": DEV, "mobile-action": SAAS, "mobily": CONS,
 "modern-health": HEALTH, "modus": SAAS, "motif-analytics": DATA,
 "muse": CONS, "mylikes": MEDIA, "naked-poppy": CONS, "nimblerx": HEALTH,
 "okera": DATA, "omnidrive": DATA, "optrip-new": CONS,
 "overture-life": HEALTH, "pantheon-ai": AI, "paravision-ai": AI,
 "peerstreet": FIN, "petasense": IND, "pf-logo": None, "philo": MEDIA,
 "pickwick-weller": CONS, "plancast": CONS, "planet-labs": IND,
 "plotwatt": CLIM, "postroller": MEDIA, "practice-fusion": HEALTH,
 "proteinqure": HEALTH, "quartz-systems": SAAS, "rapleaf": DATA,
 "recursion-pharmaceuticals": HEALTH, "redactive": AI,
 "reservoir-neuroscience": HEALTH, "resourcely": SEC, "richrelevance": SAAS,
 "romotive": IND, "room-77": CONS, "rr-logo": None, "salvo-health": HEALTH,
 "sano-intelligence": HEALTH, "savioke": IND, "scaled-interference": AI,
 "scanscout": MEDIA, "sendoso": SAAS, "sentio": DEV, "sgn": MEDIA,
 "shopittome": CONS, "siftery": SAAS, "simplifeye": HEALTH, "smartling": SAAS,
 "snowball": FIN, "social-im": CONS, "sols": CONS, "solum": IND,
 "solvemedia": SEC, "spoke": SAAS, "spring-discovery": HEALTH, "sprout": CONS,
 "sunshine": CONS, "survios": MEDIA, "swift-navigation": IND, "switch": SAAS,
 "teamable": SAAS, "tello": CONS, "the-auteurs": MEDIA,
 "the-supplant-company": IND, "thinkbright-mx": None, "tilt": FIN,
 "tivli": MEDIA, "top-hat-monocle": None, "topfunnel": SAAS,
 "trackvia": SAAS, "trialspark": HEALTH, "triplebyte": SAAS, "trivop": MEDIA,
 "troops": SAAS, "trueaccord": FIN, "trusted-health": HEALTH, "turvo": SAAS,
 "twice": CONS, "venturebeat": MEDIA, "vessyl": CONS, "voi": CONS,
 "vook": MEDIA, "votizen": None, "walker-company": CONS, "walnut": SAAS,
 "walrus-ai": AI, "weatherbill": FIN, "wedding-party": CONS,
 "weddington-way": CONS, "wild-earth": CONS, "workbase": SAAS, "woven": SAAS,
 "yamli": CONS, "yotascale": DATA, "zaarly": CONS,
}

# Rows where the crosswalk's answer is overridden by §6's precedence rules.
OVERRIDE = {
 "coalition": SEC,          # cyber insurance, sold as security
 "sentilink": SEC,          # identity fraud
 "dedrone": SEC,            # counter-drone
 "verkada": SEC,
 "semgrep": SEC,            # security for developers -> Security, not DevTools
 "rapidfort": SEC,
 "observo-ai": SEC,
 "terra-security": SEC,
 "knox": SEC,
 "operant": SEC,
 "themis": SEC,
 "altitude-networks": SEC,
 "pindrop": SEC,
 "dig-security": SEC,
 "covalent": IND,           # manufacturing network, not consumer commerce
 "astranis": IND,           # satellites
 "rigetti": IND,            # quantum hardware
 "cambridge-terahertz": IND,
 "distributed-spectrum": IND,
 "vannevar-labs": IND,
 "armada": IND,
 "exowatt": CLIM,
 "crusoe": CLIM,            # energy-first data centres
 "radiant-nuclear": CLIM,
 "zubale": CONS,
 "fitbit": CONS,            # consumer device
 "ring": CONS,
 "dropcam": CONS,
 "matterport": IND,
 "twitch": MEDIA,
 "scopely": MEDIA,
 "rovio": MEDIA,
 "zefr": MEDIA,
 "mochi": MEDIA,
 "brightroll": MEDIA,
 "yume": MEDIA,
 "wildfire": MEDIA,
 "mightyhive": MEDIA,
 "quartz": MEDIA,
 "guardant-health": HEALTH,
 "recursion": HEALTH,
 "ginkgo-bioworks": HEALTH,
 "bioage-labs": HEALTH,
 "genesis-therapeutics": HEALTH,
 "orca-bio": HEALTH,
 "prenuvo": HEALTH,
 "picnichealth": HEALTH,
 "cedar": HEALTH,           # healthcare vertical SaaS -> Healthcare & Bio
 "assort-health": HEALTH,
 "komodo-health": HEALTH,
 "midi-health": HEALTH,
 "teal-health": HEALTH,
 "octave": HEALTH,
 "osmosis": HEALTH,
 "bunkerhill": HEALTH,
 "cellino": HEALTH,
 "atlas-health": HEALTH,
 "elemy": HEALTH,
 "goldsky": CRYPTO,         # on-chain data -> Crypto & Web3 over Data Infra
 "supabase": DATA,
 "motherduck": DATA,
 "n8n": DEV,
 "sourcegraph": DEV,
 "stainless": DEV,
 "depot": DEV,
 "chalk": DATA,
 "dylibso": DEV,
 "oso": DEV,
 "meilisearch": DEV,
 "predibase": AI,
 "deepinfra": AI,
 "poolside": AI,
 "runway": AI,
 "mercor": AI,
 "periodic-labs": AI,
 "browser-use": AI,
 "letta": AI,
 "moondream": AI,
 "datology": AI,
 "skild-ai": AI,
 "flower-labs": AI,
 "wordware": AI,
 "yutori": AI,
 "simular": AI,
 "luminal": AI,
 "tera-ai": AI,
 "eventual-computing": DATA,
 "plaid": FIN,
 "adyen": FIN,
 "credit-karma": FIN,
 "alloy": FIN,
 "earnin": FIN,
 "hippo-insurance": FIN,
 "counterpart": FIN,
 "paytient": FIN,
 "nilus": FIN,
 "juniper-square": FIN,
 "guideline": FIN,
 "gusto": SAAS,
 "opendoor": CONS,
 "shopify": CONS,
 "canva": SAAS,
 "notion": SAAS,
 "flexport": CONS,
 "warby-parker": CONS,
 "wish": CONS,
 "bonobos": CONS,
 "dollar-shave-club": CONS,
 "thirdlove": CONS,
 "cruise": IND,
 "zipline": IND,
 "planet": IND,
 "soundhound": AI,
 "weights-biases": AI,
 "attentive": SAAS,
 "dialpad": SAAS,
 "culture-amp": SAAS,
 "greenhouse-software": SAAS,
 "classdojo": None,         # education -> outside the closed twelve
}


def main() -> None:
    base = json.loads((ROOT / "base.json").read_text())
    cfg = json.loads((ROOT / "config.json").read_text())
    cw = cfg["profile"]["focus_crosswalk"]

    lines, outside, from_tags, from_model, overridden = [], [], 0, 0, 0
    for r in base:
        slug = r["slug"]
        val, src = None, "model"
        tags = [t.strip() for t in (r.get("sector") or "").split(",") if t.strip()]
        mapped = [cw[t] for t in tags if t in cw]
        if mapped:
            val, src = mapped[0], "model"
            from_tags += 1
        elif slug in PARAMETRIC:
            val = PARAMETRIC[slug]
            from_model += 1
        if slug in OVERRIDE:
            if val != OVERRIDE[slug]:
                overridden += 1
            val = OVERRIDE[slug]
        row = {"slug": slug, "who": WHO}
        if val:
            row["focus"] = val
            row["focus_source"] = src
        else:
            outside.append(slug)
            continue
        lines.append(row)

    OUT.write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in lines) + "\n")
    import collections
    print(f"wrote {OUT.name}: {len(lines)} rows with a focus")
    print(f"  from the firm's own tags : {from_tags}")
    print(f"  parametric               : {from_model}")
    print(f"  §6 precedence overrides  : {overridden}")
    print(f"  OUTSIDE the taxonomy     : {len(outside)}  {outside}")
    print("  distribution:", dict(collections.Counter(
        x["focus"] for x in lines).most_common()))


if __name__ == "__main__":
    main()
