#!/usr/bin/env python3
"""Fill the `focus` column over the published base.

COLLECTION.md 6: a single primary value from the closed twelve in
data/taxonomy/focus.json, or null (reported as "outside taxonomy") for a
company that fits none. The queue never asks for focus -- it is not one of
invariant 1's four columns -- so it is authored as its own pass.

Two layers. (1) Battery's OWN sector tags, crosswalked under the standing
precedence rules: Security wins over SaaS/DevTools/Industrial whenever
security is what the company sells; healthcare vertical SaaS is Healthcare &
Bio, not SaaS; "AI & Applied AI" means AI is the product; enterprise
infrastructure and networking is Data Infrastructure; chips are Industrial &
Robotics. (2) For rows Battery tags nothing -- most of them the 1980s-2000s
book the compliance list alone carries -- a keyword read of the company's
name and business, with an explicit override table for the ones worth naming.

Output: scratch/queue/focus.out.jsonl
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
from paths import Paths  # noqa: E402

P = Paths("battery-ventures")
VALID = set(json.load(open(Path("data/taxonomy/focus.json")))["values"])

# (1) Battery's own tags -> the twelve, in precedence order.
TAG_ORDER = [
    ("Security", "Security"),
    ("Financial Tech", "Fintech & Payments"),
    ("Healthcare IT", "Healthcare & Bio"),
    ("AI-Powered Apps", "AI & Applied AI"),
    ("DevOps and Dev Tools", "DevTools & APIs"),
    ("Data/AI", "Data Infrastructure"),
    ("Infrastructure Software", "Data Infrastructure"),
    ("Industrial Tech + Life Science Tools", "Industrial & Robotics"),
    ("Consumer", "Consumer & Marketplaces"),
    ("Sales / Marketing", "SaaS"),
    ("Collaboration & Productivity", "SaaS"),
    ("Industry Specific", "SaaS"),
    ("Tech-Enabled Services", "SaaS"),
    ("Application Software", "SaaS"),
]

# (2) Keyword read for untagged rows, most specific first.
KEYWORDS = [
    (r"crypto|blockchain|coinbase|token|web3|chainalysis|zerotier", "Crypto & Web3"),
    (r"secur|cyber|firewall|encrypt|threat|fraud|siem|vpn|authenticat|identity|"
     r"pentest|malware|ciphertrust|guardicore|cyvera|zimperium|@stake|sensage|"
     r"lightcyber|normalyze|bridgecrew|expel|privacera|opal|hush|koi|tenzai|"
     r"cardinalops|atmosec|octarine|contrast|vera|jask|imper", "Security"),
    (r"bank|payment|lending|insur|fintech|billing|invoic|credit|trading|"
     r"brokerage|treasury|payroll|expense|accounting|tax|wealth|exchange|"
     r"mortgage|underwrit|remitt|escrow|capital market", "Fintech & Payments"),
    (r"health|medic|clinic|pharma|bio|therapeut|patient|hospital|onco|"
     r"diagnos|genom|surg|dental|vet|care|wellness|life science", "Healthcare & Bio"),
    (r"\bai\b|artificial intelligence|machine learning|\bllm\b|neural|"
     r"generative|agentic|copilot|inference|foundation model", "AI & Applied AI"),
    (r"devops|developer|\bapi\b|ci/cd|testing|debug|observab|monitor|"
     r"kubernetes|container|compiler|sdk|version control|code", "DevTools & APIs"),
    (r"database|data warehouse|analytics|storage|cloud|server|network|"
     r"router|switch|optical|fiber|telecom|wireless|broadband|bandwidth|"
     r"datacent|data cent|infrastructur|middleware|integration|hosting|"
     r"cdn|caching|virtualiz|hyperconverg", "Data Infrastructure"),
    (r"semiconduct|chip|silicon|processor|fpga|asic|photonic|sensor|"
     r"instrument|robot|manufactur|industrial|materials|laser|measurement|"
     r"calibration|machining|cad|cam|\beda\b", "Industrial & Robotics"),
    (r"solar|wind|energy|ethanol|battery|clean|carbon|climate|grid|"
     r"emission|renewable", "Climate & Energy"),
    (r"game|gaming|esport|media|advertis|adtech|publish|video|music|"
     r"streaming|content|news|entertainment|sports", "Media, Gaming & Advertising"),
    (r"marketplace|consumer|retail|commerce|shopping|travel|hotel|"
     r"restaurant|food|grocery|fashion|apparel|social|dating|community|"
     r"subscription|delivery|real estate|housing|rental", "Consumer & Marketplaces"),
    (r"software|saas|platform|crm|erp|hr\b|recruit|workforce|procure|"
     r"legal|compliance|productiv|collaborat|workflow|automation", "SaaS"),
]

OVERRIDE = {
    # rows whose right answer the keyword read would miss or get wrong
    "akamai-technologies": "Data Infrastructure", "coinbase": "Crypto & Web3",
    "groupon": "Consumer & Marketplaces", "wayfair": "Consumer & Marketplaces",
    "skullcandy": "Consumer & Marketplaces", "stockx": "Consumer & Marketplaces",
    "glassdoor": "Consumer & Marketplaces", "angie-s-list": "Consumer & Marketplaces",
    "a-place-for-mom": "Consumer & Marketplaces", "dollar-shave": "Consumer & Marketplaces",
    "serena-lily": "Consumer & Marketplaces", "away": "Consumer & Marketplaces",
    "nextel-communications": "Data Infrastructure", "zayo-group": "Data Infrastructure",
    "splunk": "Data Infrastructure", "databricks": "Data Infrastructure",
    "confluent": "Data Infrastructure", "clickhouse": "Data Infrastructure",
    "nutanix": "Data Infrastructure", "cohesity": "Data Infrastructure",
    "influxdata": "Data Infrastructure", "motherduck": "Data Infrastructure",
    "weaviate": "Data Infrastructure", "voltron-data": "Data Infrastructure",
    "collibra": "Data Infrastructure", "mentor-graphics": "Industrial & Robotics",
    "stratasys": "Industrial & Robotics", "xircom": "Data Infrastructure",
    "cullinet-software": "Data Infrastructure", "legent": "Data Infrastructure",
    "marketo": "SaaS", "braze": "SaaS", "amplitude": "SaaS", "jfrog": "DevTools & APIs",
    "jamf": "SaaS", "workato": "SaaS", "postman": "DevTools & APIs",
    "harness": "DevTools & APIs", "sambanova": "Industrial & Robotics",
    "habana-labs": "Industrial & Robotics", "niantic-inc": "Media, Gaming & Advertising",
    "scopely": "Media, Gaming & Advertising", "gen-g": "Media, Gaming & Advertising",
    "affirm": "Fintech & Payments", "wag": "Consumer & Marketplaces",
    "guidewire": "SaaS", "coupa": "SaaS", "bazaarvoice": "SaaS", "exacttarget": "SaaS",
    "olo": "SaaS", "sprinklr": "SaaS", "intacct": "SaaS", "realpage": "SaaS",
    "auditboard": "SaaS", "avalara": "SaaS", "omniture": "SaaS", "hibob": "SaaS",
    "honeybook": "SaaS", "reflection-ai": "AI & Applied AI",
    "chai-discovery": "Healthcare & Bio", "onebrief": "SaaS",
    "forte": "Crypto & Web3", "trip-com": "Consumer & Marketplaces",
    "infoseek": "Media, Gaming & Advertising", "friendster": "Consumer & Marketplaces",
    "pets-com": "Consumer & Marketplaces", "petstore-com": "Consumer & Marketplaces",
}


def crosswalk(tags: str):
    have = {t.strip() for t in (tags or "").split(",") if t.strip()}
    for tag, val in TAG_ORDER:
        if tag in have:
            return val, "site_tag"
    return None, None


def keyword(name: str, desc: str):
    blob = f"{name} {desc}".lower()
    for pat, val in KEYWORDS:
        if re.search(pat, blob):
            return val
    return None


def main() -> None:
    base = json.load(open(P.base_json))
    site = {r["name"]: r for r in json.load(open(P.site / "companies.json"))}
    out, src = [], Counter()
    for r in base:
        s, nm = r["slug"], r["name"]
        desc = (site.get(nm) or {}).get("description") or ""
        if s in OVERRIDE:
            val, how = OVERRIDE[s], "override"
        else:
            val, how = crosswalk(r.get("sector"))
            if not val:
                val, how = keyword(nm, desc), "keyword"
        if val and val not in VALID:
            val = None
        src[how if val else "outside taxonomy"] += 1
        rec = {"slug": s, "focus": val, "focus_source": "model"}
        if not val:
            rec["flags"] = ["focus_outside_taxonomy"]
            rec["note"] = ("No value of the closed twelve fits, so focus is null and the row is "
                           "reported as outside taxonomy rather than force-fitted (COLLECTION.md 6).")
        out.append(rec)
    p = P.queue / "focus.out.jsonl"
    p.write_text("\n".join(json.dumps(r) for r in out) + "\n")
    print(f"wrote {p}: {len(out)} rows; by route {dict(src)}")
    print("distribution:", dict(Counter(r["focus"] or "(null)" for r in out).most_common()))


if __name__ == "__main__":
    main()
