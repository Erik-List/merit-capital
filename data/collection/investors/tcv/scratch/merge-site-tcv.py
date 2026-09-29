#!/usr/bin/env python3
"""Merge TCV's three live first-party surfaces into one row per company (PRO-169).

Inputs (scratch/pull-site-tcv.py): sources/site/all-companies-2026.json (the
compliance list, legal names), partnerships-2026.json (the grid, brand names,
deal teams), jobboard-2026.json (the Getro board).
Output: sources/site/portfolio-2026.json, the one file_list source the config
reads, and sources/site/name-map.json, the join table (curated: which brand on
the grid or the board is which legal name on the list), reused by the archive
layer to name archived renderings.

The published name is the brand (COLLECTION.md 8): the grid's own rendering
where the company is on the grid, else the brand derived from the legal name,
with DISPLAY overriding both where the derivation is wrong.
"""
import json
import re
from pathlib import Path

INV = Path(__file__).resolve().parents[1]
S = INV / "sources/site"

# grid or board name -> the compliance list's legal name (verbatim)
JOIN = {
    "Arize": "Arize AI, Inc.",
    "Corgi": "Corgi Insurance Services, Inc.",
    "Mercury": "Mercury Technologies, Inc.",
    "Passport": "Passport Global Inc.",
    "Brillen (Supervista AG)": "SuperVista AG (dba Brillen.de)",
    "Act-On": "Act-On Software, Inc.",
    "onX": "onXmaps, Inc.",
    "Jane": "Jane Software Inc.",
    "Jane App": "Jane Software Inc.",
    "Fireworks": "Fireworks.ai, Inc.",
    "Grow Therapy": "Grow Care, Inc.",
    "Silver Peak": "Silver Peak Systems, Inc.",
    "Vectra": "Vectra AI, Inc.",
    "Aviatrix": "Aviatrix Systems, Inc.",
    "OSV": "OneSource Virtual, Inc.",
    "Spotify": "Spotify Technology S.A.",
    "Archy": "Archy Dental, Inc.",
    "Oversight Systems": "Oversight Investment Holdings, L.P.",
    "Oversight": "Oversight Investment Holdings, L.P.",
    "Spryker": "Spryker Systems GmbH",
    "FarEye": "Fareye Technologies Private Limited",
    "Darwinbox": "Darwinbox Digital Solutions Private Limited",
    "Aidoc": "Aidoc Medical Ltd.",
    "Attentive": "Attentive Mobile, Inc.",
    "LegalZoom": "LegalZoom.com, Inc.",
    "Peloton": "Peloton Interactive, Inc.",
    "Hotmart": "Hotmart Technology Holding B.V.",
    "Nubank": "Nu Holdings Ltd.",
    "Wealthsimple": "Wealthsimple Financial Corp.",
    "Nagomi": "Nagomi Security, Inc.",
    "Avalor": "Avalor Technologies Ltd.",
    "CCC": "CCC Intelligent Solutions Holdings Inc.",
    "Razorpay": "Razorpay Software Limited",
    "Trade Republic": "Trade Republic Bank GmbH",
    "Retail Merchant Services": "RMS Holdco Limited acquired by Teya Holdings Ltd (fka SaltPay Co Ltd.)",
    "iPipeline": "Internet Pipeline, Inc.",
    "Tastyworks": "Tastytrade, Inc. (fka Dough, Inc.), acquired by IG Group Holdings plc",
    "Perfecto": "Perfecto Mobile Ltd.",
    "Built": "Built Technologies, Inc.",
    "Nerdy (Varsity Tutors)": "Live Learning Technologies, LLC & Nerdy Inc. (the parent company of Varsity Tutors)",
    "Nerdy": "Live Learning Technologies, LLC & Nerdy Inc. (the parent company of Varsity Tutors)",
    "Payoneer": "Payoneer Global Inc.",
    "Relex": "Retail Logistics Excellence - RELEX Oy",
    "Zepz (WorldRemit)": "WorldRemit Group Limited (dba Zepz)",
    "Trulioo": "Trulioo Information Services Inc.",
    "Prodege": "Prodege International Holdings, LLC",
    "FlixBus": "Flix SE",
    "Kipu Health": "Kipu Holdings LLC",
    # the board's Open English is the list's FoxyP2 Inc. (dba Open Education), Open English's
    # parent; flagged for the judge to confirm (decisions.md)
    "Open English": "FoxyP2 Inc. (dba Open Education)",
}

# legal name -> published brand, where neither the grid nor the derivation gives it
DISPLAY = {
    "Live Learning Technologies, LLC & Nerdy Inc. (the parent company of Varsity Tutors)": "Nerdy",
    "Switchouse,Inc.": "Switchouse",
    "Retail Logistics Excellence - RELEX Oy": "Relex",
    "Nu Holdings Ltd.": "Nubank",
    "IB Holding, LLC (fka Intelligent Beauty, Inc.)": "Intelligent Beauty",
    "v2 Ventures Group LLC (fka Adknowledge, Inc.)": "Adknowledge",
    "RMS Holdco Limited acquired by Teya Holdings Ltd (fka SaltPay Co Ltd.)": "Retail Merchant Services",
    "Oversight Investment Holdings, L.P.": "Oversight Systems",
    "Tastytrade, Inc. (fka Dough, Inc.), acquired by IG Group Holdings plc": "Tastytrade",
    "Grow Care, Inc.": "Grow Therapy",
    "C|NET, Inc.": "CNET",
    "Knight Capital Group, Inc.,": "Knight Capital",
    "Go Daddy Inc.": "GoDaddy",
    "Open Text Corporation": "OpenText",
    "Hotmart Technology Holding B.V.": "Hotmart",
    "Spotify Technology S.A.": "Spotify",
    "SuperVista AG (dba Brillen.de)": "Brillen.de",
    "WorldRemit Group Limited (dba Zepz)": "Zepz",
    "OneSource Virtual, Inc.": "OneSource Virtual",
    "CCC Intelligent Solutions Holdings Inc.": "CCC Intelligent Solutions",
    "LHS Group, Inc.": "LHS Group",
    "Fuze, Inc. (fka ThinkingPhones), acquired by 8x8, Inc.": "Fuze",
    "Humu, Inc. acquired by Perceptyx Holdings, LLC": "Humu",
    "Mattersight Corporation (fka eLoyalty Corporation)": "Mattersight",
    "JellyCloud, Inc. (fka Claria Corporation)": "JellyCloud",
    "TechStyle, Inc. (fka Just Fabulous, Inc.)": "TechStyle",
    "Think Finance, Inc. (fka ThinkCash, Inc.)": "Think Finance",
    "Certinia Inc. (fka FinancialForce.com, Inc.)": "Certinia",
    "NewsEdge Corporation (fka Individual, Inc.)": "NewsEdge",
    "SQL Financials International, Inc. (fka Clarus Corporation)": "SQL Financials International",
    "Foundries Holdings, LLC": "Foundries Holdings",
    "Global 360 Holding Corp.": "Global 360",
    "Payoneer Global Inc.": "Payoneer",
    "Peloton Interactive, Inc.": "Peloton",
    "Aidoc Medical Ltd.": "Aidoc",
    "Darwinbox Digital Solutions Private Limited": "Darwinbox",
    "Fareye Technologies Private Limited": "FarEye",
    "Razorpay Software Limited": "Razorpay",
    "Trade Republic Bank GmbH": "Trade Republic",
    "Trulioo Information Services Inc.": "Trulioo",
    "Wealthsimple Financial Corp.": "Wealthsimple",
    "Spryker Systems GmbH": "Spryker",
    "Prodege International Holdings, LLC": "Prodege",
    "Perfecto Mobile Ltd.": "Perfecto",
    "Avalor Technologies Ltd.": "Avalor",
    "Passport Global Inc.": "Passport",
    "Jane Software Inc.": "Jane",
    "Archy Dental, Inc.": "Archy",
    "Attentive Mobile, Inc.": "Attentive",
    "Silver Peak Systems, Inc.": "Silver Peak",
    "Aviatrix Systems, Inc.": "Aviatrix",
    "Vectra AI, Inc.": "Vectra AI",
    "Built Technologies, Inc.": "Built Technologies",
    "Mercury Technologies, Inc.": "Mercury",
    "Corgi Insurance Services, Inc.": "Corgi",
    "Arize AI, Inc.": "Arize AI",
    "Fireworks.ai, Inc.": "Fireworks AI",
    "onXmaps, Inc.": "onX",
    "Nagomi Security, Inc.": "Nagomi Security",
    "Act-On Software, Inc.": "Act-On",
    "Internet Pipeline, Inc.": "iPipeline",
    "FoxyP2 Inc. (dba Open Education)": "Open English",
}


def k(n: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (n or "").lower())


def main():
    ac = json.load(open(S / "all-companies-2026.json"))["rows"]
    pt = json.load(open(S / "partnerships-2026.json"))["rows"]
    jb = json.load(open(S / "jobboard-2026.json"))["rows"]
    by_legal = {r["legal_name"]: r for r in ac}
    by_key = {}
    for r in ac:
        by_key.setdefault(k(r["name"]), r["legal_name"])
        for a in r["aliases"]:
            by_key.setdefault(k(a), r["legal_name"])

    def legal_for(name: str) -> str | None:
        if name in JOIN:
            return JOIN[name]
        return by_key.get(k(name))

    rows = {}
    for r in ac:
        legal = r["legal_name"]
        rows[legal] = {
            "name": DISPLAY.get(legal, r["name"]), "legal_name": legal, "aliases": list(r["aliases"]),
            "lists": ["all-companies"], "list_note": r["note"], "url": r["url"],
        }
    unjoined = []
    for p in pt:
        legal = legal_for(p["name"])
        if legal is None:
            unjoined.append(("partnerships", p["name"]))
            legal = "~" + p["name"]
            rows[legal] = {"name": p["name"], "legal_name": "", "aliases": [], "lists": [], "list_note": "",
                           "url": p["url"]}
        row = rows[legal]
        row["lists"].append("partnerships")
        if legal in by_legal and legal not in DISPLAY and p["name"] not in JOIN:
            row["name"] = p["name"]
        if p["name"] != row["name"] and p["name"] not in row["aliases"]:
            row["aliases"].append(p["name"])
        row["url"] = p["url"]
        row["partnership_url"] = p["url"]
        for key in ("status_site", "location", "continent", "sectors", "description", "year_founded",
                    "company_site", "partners", "articles"):
            if p.get(key) not in (None, "", []):
                row[key] = p[key]
    for j in jb:
        if not j.get("name") or k(j["name"]) in ("technologycrossoverventures", "tcmi"):
            continue
        legal = legal_for(j["name"])
        if legal is None:
            hit = next((lg for lg, rr in rows.items() if k(rr["name"]) == k(j["name"])), None)
            legal = hit
        if legal is None:
            unjoined.append(("jobboard", j["name"]))
            legal = "~" + j["name"]
            rows[legal] = {"name": j["name"], "legal_name": "", "aliases": [], "lists": [], "list_note": "",
                           "url": j["url"]}
        row = rows[legal]
        row["lists"].append("jobboard")
        row["jobboard_url"] = j["url"]
        if j.get("domain"):
            row["domain"] = j["domain"]
        if j["name"] != row["name"] and j["name"] not in row["aliases"]:
            row["aliases"].append(j["name"])
    out = sorted(rows.values(), key=lambda r: r["name"].lower())
    (S / "portfolio-2026.json").write_text(json.dumps({
        "_readme": "One row per company across TCV's live first-party surfaces, merged by scratch/merge-site-tcv.py: "
                   "the compliance list tcv.com/all-companies (legal_name; 'lists' carries all-companies), the "
                   "partnerships grid and pages (status_site, location, sectors, description, the deal team as "
                   "partners, linked articles) and the Getro job board (jobboard_url, domain). name is the brand "
                   "(COLLECTION.md 8). A row with an empty legal_name is on the grid or the board but not on the "
                   "compliance list as of 2026-07-15.",
        "rows": out}, indent=1, ensure_ascii=False))
    nm = {r["name"]: {"legal_name": r["legal_name"], "aliases": r["aliases"]} for r in out}
    (S / "name-map.json").write_text(json.dumps({
        "_readme": "Brand -> the compliance list's legal name and every other rendering the firm's live surfaces "
                   "use (scratch/merge-site-tcv.py, JOIN and DISPLAY curated by hand 2026-09-29). The archive layer "
                   "adds its own renderings under 'archive' (scratch/pull-archive-tcv.py).",
        "map": nm}, indent=1, ensure_ascii=False))
    print(len(out), "rows;", sum(1 for r in out if "partnerships" in r["lists"]), "on the grid;",
          sum(1 for r in out if "jobboard" in r["lists"]), "on the board;",
          sum(1 for r in out if not r["legal_name"]), "not on the compliance list")
    for u in unjoined:
        print("  unjoined:", *u)


if __name__ == "__main__":
    main()
