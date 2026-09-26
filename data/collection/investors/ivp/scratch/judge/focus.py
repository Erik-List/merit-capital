"""Focus pass (COLLECTION.md 6 focus): one primary value from the closed twelve
per row, one parametric pass, precedence rules applied (Security when security
is what is sold; Crypto only for on-chain businesses; consumer devices are
Consumer; healthcare vertical software is Healthcare & Bio; ad networks and
audience monetization are Media; AI only where AI is the product; enterprise
infrastructure and networking is Data Infrastructure; chips and components are
Industrial). Sibling books' values were read for shared companies and followed
where they fit the rules."""
import json
from jl import write
AI, DI, DT, SA, SE, FI, CR, IN, CL, HB, CM, MG = (
    "AI & Applied AI", "Data Infrastructure", "DevTools & APIs", "SaaS", "Security",
    "Fintech & Payments", "Crypto & Web3", "Industrial & Robotics", "Climate & Energy",
    "Healthcare & Bio", "Consumer & Marketplaces", "Media, Gaming & Advertising")
F = {
 "abridge": HB, "accompany-health": HB, "addthis": MG, "advent-software": FI, "aerohive-networks": DI,
 "agile-software": SA, "aiven": DI, "ajaib": FI, "akamai": DI, "aledade": HB, "alienvault": SE,
 "altera": IN, "amati-communications": DI, "amplitude": SA, "anomali": SE, "anthropic": AI,
 "appcharge": FI, "appdynamics": DI, "applied-digital-access": DI, "applied-medical": HB,
 "archive": DI, "arcsight": SE, "argonaut-technologies-inc": HB, "arthrocare-corp": HB,
 "artisan-components": IN, "ask-jeeves": MG, "aspect": DI, "aster-data-systems": DI, "at-road": SA,
 "attentive": SA, "aviron": HB, "ayasdi": AI, "baseten": AI, "biopsys-medical-inc": HB,
 "borland-software": DT, "brex": FI, "bridge-communications": DI, "buddy-media": SA,
 "business-com": MG, "business-insider": MG, "cafepress": CM, "cape": SE, "carbonite": DI,
 "cardiac-pathways-corp": HB, "care-com": CM, "casper": CM, "chainguard": SE, "checkr": SA,
 "chemconnect": CM, "chordiant-software": SA, "cipher-data-products": DI, "circleci": DT,
 "cirrus-logic": IN, "clarify": SA, "clickhouse": DI, "clipboard-health": HB, "coinbase": CR,
 "compass": CM, "comscore-networks": MG, "concur-technologies": SA, "connectandsell": SA,
 "constant-contact": SA, "cortex": DT, "cortina-systems": IN, "cowboy-space-corporation": IN,
 "cradle": HB, "cribl": DI, "crowdstrike": SE, "curology": HB, "cv-therapeutics-inc": HB,
 "cyence": FI, "danger": CM, "data-ai": SA, "data-domain": DI, "datadog": DI, "datalogix": MG,
 "dataminr": AI, "deepl": AI, "deputy": SA, "digital-impact": SA, "digital-river": SA,
 "discord": CM, "domo": SA, "doubleverify": MG, "dream-games": MG, "dropbox": SA, "dropcam": CM,
 "dust-networks": IN, "ehealth": FI, "eightfold": AI, "endosonics-corp": HB, "eucalyptus": DI,
 "exabyte": DI, "excite": MG, "exclusive-resorts-llc": CM, "expanse": SE, "fandom-wikia": MG,
 "fightcamp": CM, "figma": SA, "fleetmatics": SA, "formfactor": IN, "found": HB,
 "foundry-networks": DI, "ftx": CR, "g2": SA, "gaia-interactive": CM, "gamma": AI,
 "general-assembly": CM, "genlogs": AI, "genta-incorporated-de": HB, "giphy": MG, "github": DT,
 "glean": AI, "glossier": CM, "grammarly": AI, "groundtruth": MG, "group-nine-media": MG, "h1": HB,
 "h5": SA, "hands-on-mobile": MG, "harness": DT, "hashicorp": DI, "hearme": MG, "hello-heart": HB,
 "hims-hers": HB, "hipmunk": CM, "homeaway": CM, "hopin": SA, "humu": SA, "iasiaworks-inc": DI,
 "ic-works": IN, "iex": FI, "igo-corp": CM, "imagyn-medical-inc": HB, "indiegogo": CM,
 "inspirato": CM, "integrated-medical-resources-inc": HB, "jasper": AI, "juniper-networks": DI,
 "kalshi": FI, "kayak": CM, "kittl": SA, "klarna": FI, "klout": MG, "langchain": AI, "laurel": AI,
 "legalzoom": CM, "lensvector": IN, "lifelock": SE, "lime": CM, "limelight-networks": DI,
 "liveops": SA, "livingsocial": CM, "looker": DI, "loopnet": CM, "lsi": IN, "lulu-s": CM,
 "lumafield": IN, "luminate-software": SA, "lyra-health": HB, "marketo": SA, "markmonitor": SE,
 "masterclass": CM, "metra-biosystems-inc": HB, "microcide-pharmaceuticals-inc": HB,
 "microtune": IN, "mindbody": SA, "mips-technologies": IN, "mmc-networks": IN, "mobile-365": DI,
 "mobileiron": SE, "monte-carlo": DI, "motion-computing": IN, "motive": SA, "motosport": CM,
 "mtone-wireless": MG, "mulesoft": DT, "mysql": DI, "neocad": DT, "neophotonics": IN,
 "nerdwallet": FI, "netflix": MG, "nextdoor": CM, "nextroll": MG, "ngmoco": MG, "niantic": MG,
 "numeric": FI, "obsidian-security": SE, "omniture": SA, "ondeck-capital": FI, "one-kings-lane": CM,
 "onebox": CM, "onyx-pharmaceuticals-inc": HB, "oportun": FI, "papaya-global": SA, "paper": CM,
 "perplexity": AI, "personal-capital": FI, "pharmacopeia-inc": HB, "pigment": SA, "pindrop": SE,
 "platinum-software": SA, "podium": SA, "polycom": DI, "popsugar": MG, "productiv": SA,
 "prosper": FI, "pure-storage": DI, "quality-semiconductor": IN, "qubole": DI,
 "quigo-technologies": MG, "red-pepper-software": SA, "retailmenot": CM, "rgb-networks": DI,
 "roam": SA, "robinhood": FI, "rubrik": DI, "sage": HB, "santera-systems": DI, "sauce-labs": DT,
 "seagate-technology": DI, "seon": SE, "sequent-computer-systems": DI, "shazam": MG, "skydio": IN,
 "skystream-networks": DI, "slack": SA, "snap": CM, "sofi": FI, "solace-health": HB,
 "solta-medical-inc": HB, "sorare": CR, "soundcloud": MG, "spiceworks": MG, "steelbrick": SA,
 "storm-technology-inc": CM, "stratus-technologies": DI, "sublime-security": SE,
 "successfactors": SA, "sumo-logic": DI, "suno": AI, "supercell": MG, "superhuman": SA,
 "supermetrics": SA, "supportsoft": SA, "surf-air-global-ltd": CM, "symyx-technologies": IN,
 "synchronoss": SA, "synoptics-communications": DI, "tala": FI, "tanium": SE, "taxbit": FI,
 "telcom-semiconductor": IN, "tennr": HB, "teros": SE, "the-honest-company": CM,
 "the-players-tribune": MG, "thrive-global": HB, "tivo": CM, "traceable": SE, "transmeta": IN,
 "tripwire": SE, "tunein": MG, "turnstone-systems-inc": DI, "twitter": CM, "twyla": CM, "uber": CM,
 "uipath": SA, "unify": DI, "uproxx": MG, "varolii": SA, "venice": SE, "vercel": DT, "veriff": SE,
 "verisity": DT, "vessel": MG, "volt": FI, "vonage": CM, "voxer": CM, "walker-company": CM,
 "webex-communications": SA, "websense": SE, "wellfleet-communications": DI,
 "whip-media-group": MG, "whisper": HB, "whistle-communications": DI, "whoop": CM, "wise": FI,
 "wonderful": AI, "yellowbrick-data": DI, "yext": SA, "yodlee": FI, "zefr": MG, "zendesk": SA,
 "zenefits": SA, "zerto": DI, "ziprecruiter": CM, "zynga": MG,
}
base = {r["slug"] for r in json.load(open("../../companies/base.json"))}
missing, extra = sorted(base - set(F)), sorted(set(F) - base)
assert not missing and not extra, (missing, extra)
write("../queue/focus.out.jsonl", [{"slug": s, "focus": v, "focus_source": "model"} for s, v in sorted(F.items())])
