#!/usr/bin/env python3
"""Name every archived rendering after the live row it is (PRO-169).

The archive layer carries each generation's own rendering: legal names on the
compliance lists ("Act-On Software, Inc."), brands on the grids ("Act-On"),
spellings that drifted ("Alteon WebSystemc", "Actuate Software Corp."). The
builder keys rows by the normalised display name, so an unmapped rendering
becomes a second row for one company. This maps each parsed row onto the live
site row (sources/site/portfolio-2026.json) and rewrites `name` to the live
brand, keeping the archive's own text in `name_listed`.

Match order, first hit wins: (1) the live row's brand, legal name or aliases,
normalised; (2) the same with a wider suffix list (Software, Systems,
Networks, Technologies, Communications, .com ...); (3) MANUAL below, curated
by hand from the unmatched list this script prints; (4) no match: the row
keeps its own name and becomes its own base row, to be judged.
Idempotent: a row already carrying name_listed is re-mapped from name_listed.
"""
import json
import re
from pathlib import Path

INV = Path(__file__).resolve().parents[1]
PARSED = INV / "sources/wayback/parsed"
SITE = json.load(open(INV / "sources/site/portfolio-2026.json"))["rows"]

STOP1 = r"inc|incorporated|corp|corporation|co|company|ltd|limited|llc|lp|plc|gmbh|ag|nv|sa|sas|se|bv|oy|pbc|holdings?|group|the"
STOP2 = STOP1 + r"|software|systems?|networks?|technolog(?:y|ies)|communications?|com|net|interactive|international|solutions|services|online|mobile|media|labs?|global|worldwide|ai|io|app"

# archived rendering (normalised by k1) -> live brand; curated from the unmatched list
MANUAL = {
    # compliance-list spellings and registered names (2017-2026 lists)
    "adevintaas": "Adevinta", "adevintaasa": "Adevinta", "believedigital": "Believe", "cogniteas": "Cognite",
    "desertnewco": "GoDaddy",   # Desert Newco, LLC: GoDaddy's operating company, the 2011 KKR / Silver Lake / TCV buyout vehicle (GoDaddy S-1)
    "greenedentopcosca": "Genesys", "grupapracujspzoo": "Grupa Pracuj", "pracuj": "Grupa Pracuj",
    "karna": "Klarna", "klarnaab": "Klarna", "livelearningtechnologies": "Nerdy", "molliebv": "Mollie",
    "opisoftoware": "Opi Software", "razorpaysoftwareprivate": "Razorpay", "rmsholdco": "Retail Merchant Services",
    "roboticwaresprivate": "FarEye", "switchhouse": "Switchouse", "tastytradefkadoughacquiredbyig": "Tastytrade",
    "techstylefashion": "TechStyle", "vendioservices": "AuctionWatch.com", "foundriesfkaraza": "Foundries Holdings",
    "swagbucks": "Prodege",           # Swagbucks is Prodege's consumer brand (the firm's own 2016 post)
    "hhealth": "Hinge Health",        # "H Health Holding LLC" on the 2023 list only, "Hinge Health, Inc." from 2024
    # renames and brands on the grids (2013-2023)
    "advanceme": "Capital Access Network",   # AdvanceMe, Kennesaw GA: Capital Access Network's brand
    "bluecoatsystems": "CacheFlow",          # CacheFlow renamed itself Blue Coat Systems in 2002
    "cccinformationservices": "CCC Intelligent Solutions", "cnetnetworks": "CNET", "elevate": "Elevate Credit",
    "flixmobility": "Flix", "genesystelecommunicationslaboratories": "Genesys", "gmi": "Global Market Insite",
    "varsitytutors": "Nerdy", "maas360": "Fiberlink Communications", "meta": "Facebook",
    "originhealthcaresolutions": "Origin", "savillesystems": "Saville Systems Ireland", "xata": "XRS",
    "dermstore": "Intelligent Beauty", "sensaproducts": "Intelligent Beauty",   # IB Holding's businesses
    # the 2013-2014 grid's cards for the Travelport and Orbitz businesses
    "galileointernational": "Travelport", "gulliverstravelassociates": "Travelport", "octopustravelcom": "Travelport",
    "cheaptickets": "Orbitz Worldwide", "ebookerscom": "Orbitz Worldwide",
    # the 2008-2013 index.php4 and all-portfolio.php4 renderings (city suffixes after an en dash, typos)
    "alteonwebsystemc": "Alteon WebSystems", "casteksoftwarestallionenergy": "Castek Software",
    "eladianpartnersnewyorkny": "Eladian Partners", "embanet": "EmbanetCompass", "envestnetchicagoil": "Envestnet",
    "fxalliancenewyorkcityny": "FX Alliance", "infonxxbethlehempa": "kgb", "rjobrienassociates": "R.J. O’Brien",
    "smthldg": "Seismic Micro-Technology", "solecttech": "Solect Technology", "technicalcommunitiesdbatestmart": "TestMart",
    "webrootbroomfield": "Webroot Software", "webtonetechnologiess": "WebTone Technologies", "zxaccttechnologies": "XACCT Technologies",
    "sunburstcommunications": "Tenth Planet Explorations",   # "Sunburst Communications, Inc (acq. Tenth Planet)": the acquirer's line for TCV's Tenth Planet position
}


def k(n, stop):
    n = (n or "").lower().replace("&amp;", "&")
    n = re.sub(r"\(.*?\)", " ", n)
    n = re.sub(r"[^a-z0-9 ]+", " ", n)
    n = re.sub(rf"\b({stop})\b", " ", n)
    return re.sub(r"\s+", "", n)


idx1, idx2 = {}, {}
for r in SITE:
    for n in [r["name"], r.get("legal_name") or ""] + (r.get("aliases") or []):
        if n:
            idx1.setdefault(k(n, STOP1), r["name"])
            idx2.setdefault(k(n, STOP2), r["name"])


def canon(name):
    a = k(name, STOP1)
    if a in MANUAL:
        return MANUAL[a], "manual"
    if a and a in idx1:
        return idx1[a], "exact"
    b = k(name, STOP2)
    if b and len(b) >= 3 and b in idx2:
        return idx2[b], "wide"
    return None, None


def main():
    unmatched = {}
    stats = {"exact": 0, "wide": 0, "manual": 0, "none": 0}
    for f in sorted(PARSED.glob("*.json")):
        rows = json.load(open(f))
        for r in rows:
            listed = r.get("name_listed") or r.get("name") or ""
            if not listed:
                continue
            c, how = canon(listed)
            if c:
                r["name_listed"] = listed
                r["name"] = c
                stats[how] += 1
            else:
                r["name"] = listed
                r.pop("name_listed", None)
                stats["none"] += 1
                unmatched.setdefault(listed, set()).add(f"{r['surface']}:{f.stem}")
        f.write_text(json.dumps(rows, indent=1, ensure_ascii=False))
    print(stats)
    for n, where in sorted(unmatched.items(), key=lambda x: x[0].lower()):
        print(f"  {n!r:50} {k(n, STOP1)!r:30} {sorted(where)[:3]}")
    print(len(unmatched), "unmatched renderings")


if __name__ == "__main__":
    main()
