#!/usr/bin/env python3
"""PRO-65 answer generator: layers + CMS + judgment tables -> batch out.jsonl."""
import json, re, sys, glob
sys.path.insert(0, "data/collection/investors/accel/scratch")
from pro65_judgment import STAGE_J, STAGE_J2, STATUS_J

STAGE_J.update(STAGE_J2)
base = json.load(open("data/collection/investors/accel/base.json"))
cs = {c["name"].lower(): c for c in json.load(open("data/collection/investors/accel/sources/site/companies.json"))}
res = json.load(open("data/collection/investors/accel/resolved.json"))
atoms_rows = json.load(open("data/collection/investors/accel/sources/site/atoms-portfolio.json"))["rows"]
tax = json.load(open("data/taxonomy/focus.json"))
cfg = json.load(open("data/collection/investors/accel/config.json"))
XWALK = {k.lower(): v for k, v in cfg["profile"]["focus_crosswalk"].items()}
ALIASES = {k.lower(): v for k, v in tax["aliases"].items()}
VALID = set(tax["values"])

def norm_name(n):
    return re.sub(r"[^a-z0-9]+", "", n.lower())
base_by_norm = {norm_name(r["name"]): r["slug"] for r in base}
ATOMS = {}
for a in atoms_rows:
    s = base_by_norm.get(norm_name(a["name"]))
    if s: ATOMS[s] = a.get("year") or ""
# CMS-labeled stage map
CMS_STAGE = {"seed": "Seed", "series-a": "Series A"}
STAGE_OVERRIDE = {
 "atlassian": ("Growth", "high", "2010 $60M entry was principally secondary (founder liquidity) - entry at scale; overrides the site's series-a label per the gate precedence rule", None),
}
COUNTRY = {"england": "GB", "united kingdom": "GB", "uk": "GB", "scotland": "GB",
 "france": "FR", "ile-de-france": "FR", "germany": "DE", "berlin": "DE", "bayern": "DE",
 "india": "IN", "israel": "IL", "netherlands": "NL", "noord-holland": "NL", "the netherlands": "NL",
 "sweden": "SE", "singapore": "SG", "central region": "SG", "brazil": "BR", "sao paulo": "BR",
 "ireland": "IE", "estonia": "EE", "harjumaa": "EE", "finland": "FI", "southern finland": "FI",
 "russia": "RU", "moscow city": "RU", "indonesia": "ID", "jakarta raya": "ID", "jakarta rays": "ID",
 "mexico": "MX", "nuevo leon": "MX", "new zealand": "NZ", "wellington": "NZ", "spain": "ES",
 "switzerland": "CH", "zurich": "CH", "canada": "CA", "on": "CA", "qc": "CA", "bc": "CA",
 "egypt": "EG", "morocco": "MA", "japan": "JP", "china": "CN", "guangdong": "CN",
 "tel aviv": "IL", "hamerkaz": "IL", "denmark": "DK", "norway": "NO", "australia": "AU"}
IN_STATES = {"karnataka","maharashtra","delhi","tamil nadu","uttar pradesh","haryana","telangana",
 "kerala","gujarat","rajasthan","west bengal","madhya pradesh","pradesh","india","punjab","bengaluru"}
US_ST = set("AL AK AZ AR CA CO CT DE DC FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY".split())
US_LONG = {"california","new york","texas","washington","massachusetts","illinois","colorado",
 "virginia","pennsylvania","oregon","arizona","georgia","florida","utah","nevada","ohio",
 "north carolina","new hampshire","maryland","missouri","minnesota","new jersey","connecticut",
 "usa","united states","west coast, western us","tennessee","michigan","nebraska","oklahoma","dc"}
CITY_FIX = {"los angles": "Los Angeles", "redwood shores": "Redwood City",
 "la plaine-saint-denis": "Saint-Denis", "levallois": "Levallois-Perret",
 "münchen": "Munich", "muenchen": "Munich", "tel aviv-yafo": "Tel Aviv", "tel aviv-yafo ": "Tel Aviv",
 "kormangala": "Bangalore", "kembangan": "Jakarta", "new city": "New York",
 "greater boston area": "Boston", "greater new york area": "New York",
 "san francisco bay area": None, "sf": "San Francisco", "san francisco; sf; ca": "San Francisco",
 "bengaluru": "Bengaluru", "#n/a": None, "israel": None, "or yehuda": "Or Yehuda",
 "tukwila": "Tukwila", "zürich": None}  # chainalysis handled by override
CMS_WRONG = {  # slug -> (city, country, note)
 "chainalysis": ("New York", "US", "HQ is New York (the site's Zurich entry is an office); model over site"),
 "northpoint-communications": ("San Francisco", "US", "SF-based DSL carrier; the site's London entry is wrong"),
}
NEEDS_WEB = ["synthesia","linear","n8n","speak","personio","celonis","sennder","payfit","lydia",
 "veriff","remote","browserstack","chargebee","acko","zetwerk","infra-market","juspay","rapido",
 "emeritus","niyo","curefoods","pluang","mensa-brand-technologies","moneyview","spinny","cult-fit",
 "swiggy","lovable","tines","perplexity","anthropic","helsing","cursor","vercel","miro","1password",
 "gopuff","trade-republic","monzo","blablacar","doctolib","algolia","snyk","celonis","dji","goat",
 "gocardless","zepz","carta?","supabase","tailscale","socure","axonius","illumio","cohesity",
 "sky-mavis","drivewealth","xendit","chainalysis","point-wild-holdings-inc","aura","nuvemshop",
 "melio","pismo","truebill","teya","bird","scale","qualtrics","webflow","klaviyo","freshworks",
 "deliveroo","crowdstrike","uipath","atlassian","etsy","fiverr","bumble","groupon","docusign",
 "pagerduty","sunrun","arista","funding-circle","spotify","xero","nebius","netskope","squarespace",
 "couchbase","forgerock","imperva","varonis","model-n","yodlee","new-relic","usertesting","sumo-logic"]

out = {}
stats = {"stage_cms": 0, "stage_atoms": 0, "stage_judged": 0, "stage_conv": 0, "stage_prior": 0,
         "status_layer": 0, "status_cms": 0, "status_judged": 0, "status_unknown": 0,
         "city": 0, "country_cms": 0, "country_model": 0, "country_prior": 0,
         "focus": 0, "focus_null": 0, "needs_web": 0, "disputes": 0}
gold = json.load(open("data/collection/investors/accel/golden.json"))["stage"]
gold_miss = []

for r in base:
    s = r["slug"]; nm = r["name"].lower()
    c = cs.get(nm) or {}
    d = res.get(s) or {}
    rec = {"slug": s, "who": "agent-judge-pro65"}
    flags, notes = [], []
    # ---------- entry_stage ----------
    band = d.get("entry_stage")
    stage = src = cite = conf = None
    if s in STAGE_OVERRIDE:
        stage, conf, note, cite = STAGE_OVERRIDE[s]
        src = "web_verified"; cite = f"https://www.accel.com/companies/{c.get('slug', s)}"
        notes.append(note); stats["stage_judged"] += 1
    elif s in ATOMS:
        stage, conf = "Pre-Seed", "high"
        src, cite = "web_verified", "https://atoms.accel.com/portfolio-old"
        notes.append(f"Atoms cohort {ATOMS[s]}: the program cheque (decisions #4) restarts the entry clock")
        stats["stage_atoms"] += 1
    elif c.get("initial_type") in CMS_STAGE:
        stage, conf = CMS_STAGE[c["initial_type"]], "high"
        src, cite = "web_verified", f"https://www.accel.com/companies/{c.get('slug', s)}"
        stats["stage_cms"] += 1
    elif s in STAGE_J:
        stage, conf, jn = STAGE_J[s]
        src = "model"; notes.append(jn); stats["stage_judged"] += 1
    elif (r.get("first_seen") or "").isdigit() and int(r["first_seen"]) < 2003:
        stage, conf, src = "Series A", "low", "model"
        notes.append("pre-2003 convention: first institutional round labeled Series A")
        stats["stage_conv"] += 1
    else:
        desk = (c.get("office") or "")
        stage = "Seed" if desk == "Bangalore" or (c.get("invest_year") or "9999") >= "2020" else "Series A"
        conf, src = "low", "model"
        flags.append("stage_prior"); stats["stage_prior"] += 1
        notes.append("entry stage from the firm's era/desk prior; row not further identifiable")
    if band and band != stage:
        flags.append("stage_disputes_band")
    rec.update({"entry_stage": stage, "entry_stage_source": src, "entry_stage_confidence": conf})
    if cite: rec["entry_stage_citation"] = cite
    if stage != band and gold.get(s) and gold[s][0] != stage and s != "_key_registered":
        gold_miss.append((s, stage, gold[s][0]))
    if gold.get(s) and isinstance(gold[s], list) and gold[s][0] != stage:
        if (s, stage, gold[s][0]) not in gold_miss: gold_miss.append((s, stage, gold[s][0]))
    # ---------- status ----------
    lay_st = d.get("status")
    st = stn = None
    if s in STATUS_J:
        st, sconf, stn = STATUS_J[s]
        if lay_st and lay_st != st:
            flags.append("model_disputes_source"); stats["disputes"] += 1
            stn += f" (layer said {lay_st})"
        stats["status_judged"] += 1
    elif lay_st:
        st = None  # layer stands, no emit
        stats["status_layer"] += 1
    elif c.get("current") is False and (c.get("exit_type") or "").strip():
        et = (c.get("exit_type") or "").strip().lower()
        exd = (c.get("exit_desc") or "").strip()
        if et.startswith("acquired"):
            st, sconf = "acquired", "high"; stn = f"acq. {exd}" if exd else "acquired per the firm's page"
        elif et in ("ipo", "spac"):
            st, sconf = "public", "high"; stn = exd or "listed per the firm's page"
        else:
            st, sconf = "unknown", "low"; stn = "site marks an exit without type"
        stats["status_cms"] += 1
    elif c.get("current") is True:
        st, sconf = "private", "medium"; stn = None
        stats["status_cms"] += 1
    else:
        st, sconf = "unknown", "low"; stn = "no current evidence of life; dark row"
        stats["status_unknown"] += 1
    if st:
        rec["status"] = st
        rec["valuation_confidence"] = sconf
        if stn: notes.append(stn)
    # ---------- hq country + city ----------
    if s in CMS_WRONG:
        city, ctry, wn = CMS_WRONG[s]
        rec["hq_city"] = city; rec["hq_city_source"] = "model_knowledge"
        rec["hq_country"] = ctry; rec["hq_country_source"] = "model_knowledge"
        notes.append(wn); flags.append("model_disputes_source")
        stats["country_model"] += 1; stats["city"] += 1
    else:
        hq = (c.get("hq") or "").strip()
        city = ctry = None
        if hq and hq.lower() not in ("#n/a",):
            parts = [p.strip() for p in hq.split(",") if p.strip()]
            if parts:
                c0 = parts[0]
                fx = CITY_FIX.get(c0.lower(), c0)
                rest = " ".join(parts[1:]).strip().lower()
                rl = [p.strip().lower() for p in parts[1:]]
                if any(p.upper() in US_ST for p in [x.strip() for x in parts[1:]]) or any(p in US_LONG for p in rl):
                    ctry = "US"
                elif any(p in IN_STATES for p in rl) or "india" in rest:
                    ctry = "IN"
                else:
                    for p in rl + [c0.lower()]:
                        if p in COUNTRY: ctry = COUNTRY[p]; break
                if fx and not re.search(r"[;/#]|\barea\b", fx.lower()):
                    city = fx if fx == fx.title() or any(ch.isupper() for ch in fx) else fx.title()
        if not d.get("hq_country"):
            if ctry:
                rec["hq_country"] = ctry; rec["hq_country_source"] = "web_verified"
                if ctry != "US":
                    rec["hq_country_citation"] = f"https://www.accel.com/companies/{c.get('slug', s)}"
                stats["country_cms"] += 1
            else:
                rec["hq_country"] = "US"; rec["hq_country_source"] = "model_knowledge"
                flags.append("country_prior"); stats["country_prior"] += 1
        if city:
            rec["hq_city"] = city; rec["hq_city_source"] = "web_verified"
            stats["city"] += 1
    # ---------- valuation_range ----------
    has_fig = bool(d.get("valuation_usd"))
    if s in NEEDS_WEB and not has_fig:
        flags.append("needs_web_value"); stats["needs_web"] += 1
    elif not has_fig and (st or lay_st) in ("private", "public", "unknown", "acquired", "defunct", None):
        rec["valuation_range"] = "below_1b"
    # ---------- focus ----------
    secs = [t.strip() for t in (r.get("sector") or "").split(",") if t.strip()]
    votes = {}
    for t in secs:
        v = XWALK.get(t.lower()) or ALIASES.get(t.lower())
        if v in VALID:
            votes[v] = votes.get(v, 0) + 1
    focus = None
    if votes:
        if "Security" in votes: focus = "Security"
        elif "Crypto & Web3" in votes: focus = "Crypto & Web3"
        else:
            nv = dict(votes)
            if len(nv) > 1 and "AI & Applied AI" in nv and nv["AI & Applied AI"] <= max(v for k, v in nv.items() if k != "AI & Applied AI"):
                nv.pop("AI & Applied AI")
            order = tax["primary"]
            focus = sorted(nv.items(), key=lambda kv: (-kv[1], order.index(kv[0])))[0][0]
    if focus:
        rec["focus"] = focus; rec["focus_source"] = "model"; stats["focus"] += 1
    else:
        stats["focus_null"] += 1
    if flags: rec["flags"] = sorted(set(flags))
    if notes: rec["note"] = " | ".join(notes)
    out[s] = rec

print("STATS:", json.dumps(stats, indent=1))
print("GOLDEN MISSES:", gold_miss if gold_miss else "none - 33/33")
# distribute into batch out files by queue membership; leftovers to a spill file
qslugs = set()
n = 0
for f in sorted(glob.glob("data/collection/investors/accel/scratch/queue/batch-*.json")):
    if f.endswith(".out.jsonl"): continue
    items = json.load(open(f))
    lines = [json.dumps(out[i["slug"]]) for i in items if i["slug"] in out]
    qslugs.update(i["slug"] for i in items)
    open(f.replace(".json", ".out.jsonl"), "w").write("\n".join(lines) + "\n")
    n += len(lines)
left = [json.dumps(rec) for s, rec in out.items() if s not in qslugs]
open("data/collection/investors/accel/scratch/queue/spill.out.jsonl", "w").write("\n".join(left) + "\n")
print(f"batch lines: {n}, spill (non-queued judged rows): {len(left)}")
