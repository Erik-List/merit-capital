#!/usr/bin/env python3
"""One evidence view per queued row, for the judge: the firm's card, archive
years, every press sentence naming 20VC or Harry Stebbings about this company
(sweep, targeted Google News, TechCrunch/Crunchbase News), sibling books' rows
and the deterministic pre-fills. Output: scratch/evidence-pack.json."""
import csv, glob, json, re
from pathlib import Path
HERE = Path(__file__).resolve().parent
I = HERE.parent
ROOT = HERE.parents[4]
base = json.load(open(I / "companies" / "base.json"))
resolved = json.load(open(I / "companies" / "resolved.json"))
site = {r["name"].lower(): r for r in json.load(open(I / "sources" / "site" / "companies-framer.json"))["rows"]}
tri = json.load(open(HERE / "press" / "triage.json"))
wp = json.load(open(HERE / "recall" / "wp.json"))
FIRM = re.compile(r"20\s?VC|Stebbings|20Growth|20Sales|20Product|Twenty", re.I)
ALIAS = {"merge-dev": ["merge.dev", "merge"], "nex-health": ["nexhealth", "nex health"], "junction": ["junction", "vital"],
         "noh-payments": ["noh", "divy"], "techwolf": ["techwolf"], "lottielabs": ["lottielab", "lottielabs", "gifs of the future"],
         "11x": ["11x"], "slay": ["slay", "born"], "fyxer": ["fyxer"], "remote-com": ["remote.com", "remote"],
         "ami-labs": ["ami labs"], "entire": ["entire", "github ceo"], "asklio": ["asklio", "lio"], "grand": ["grand"],
         "zero": ["zero"], "bottlecap": ["bottlecap"], "general-index": ["general index", "gx"], "poolside": ["poolside"],
         "fonio-ai": ["fonio"], "archestra-ai": ["archestra"], "comstruct": ["comstruct"], "allo": ["allo"],
         "datalane": ["datalane"], "cryptotax-calculator": ["cryptotax"], "frankieone": ["frankieone"], "eql": ["eql"],
         "bridgelinx": ["bridgelinx"], "airlift": ["airlift"], "kevin": ["kevin."]}


def key(n): return re.sub(r"[^a-z0-9]", "", n.lower())


sib = {}
for f in glob.glob(str(ROOT / "data/collection/investors/*/companies/base.csv")):
    inv = f.split("/")[-3]
    if inv == "20vc":
        continue
    with open(f, newline="") as fh:
        for row in csv.DictReader(fh):
            sib.setdefault(key(row.get("name", "")), []).append({"inv": inv, **{k: row.get(k) for k in (
                "status", "valuation_range", "valuation_usd", "entry_stage", "entry_date", "hq_country", "hq_city",
                "focus", "seed_to_a_graduation")}, "note": (row.get("note") or "")[:400]})
out = {}
for r in base:
    slug, name = r["slug"], r["name"]
    terms = ALIAS.get(slug, [name.lower()])
    pat = re.compile("|".join(r"(?<![\w-])" + re.escape(t) + r"(?![\w-])" for t in terms), re.I)
    press = []
    for t in tri:
        if not (pat.search(t.get("title") or "") or (t.get("query_name") or "").lower() in terms):
            continue
        for x in t["sentences"]:
            if FIRM.search(x["s"]) and x["tag"] != "podcast":
                press.append({"date": t["date"], "src": t["source"], "s": x["s"][:500], "link": t["link"], "tag": x["tag"]})
    for nm, rec in wp.items():
        if nm.lower() not in terms and key(nm) != key(name):
            continue
        for svc in rec.values():
            for h in svc.get("hits", []):
                for s in h["sentences"]:
                    if pat.search(s) or pat.search(h["title"]):
                        press.append({"date": h["date"], "src": "wp", "s": s[:500], "link": h["link"], "tag": "wp"})
    seen, uniq = set(), []
    for p in sorted(press, key=lambda p: p["date"] or ""):
        k = (p["s"][:120], p["link"])
        if k not in seen:
            seen.add(k)
            uniq.append(p)
    card = site.get(name.lower())
    out[slug] = {"name": name, "card": {k: card.get(k) for k in ("one_liner", "sector_1", "sector_2", "website", "exit_site", "cms_created")} if card else None,
                 "archive_years": r.get("wayback_years"), "notes": r.get("notes"),
                 "prefill": {k: v for k, v in resolved.get(slug, {}).items() if k != "name"},
                 "press": uniq[:14], "siblings": sib.get(key(name), [])}
(HERE / "evidence-pack.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
print(len(out), "rows;", sum(1 for v in out.values() if v["press"]), "with press;", sum(1 for v in out.values() if v["siblings"]), "with siblings")
