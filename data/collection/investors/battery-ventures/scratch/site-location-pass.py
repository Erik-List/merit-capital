#!/usr/bin/env python3
"""Re-judge hq_country/hq_city from Battery's own Location field.

The Wikidata layer scored badly on this book for exactly the reason
COLLECTION.md 5 records from the First Round run: Battery's portfolio is full
of one-word names (Front, Olo, Plain, Cube, Coram, Cask, Taster, Terminal,
Sage, Marco Polo), and `prepare` filled hq_country on 98 rows from Wikidata
joins that are wrong roughly a quarter of the time -- Front->JP, Olo->FI,
Marco Polo->MA, Carta->NL, Trip.com->CN, Cask->GB -- plus three rows carrying
a footnoted prose string ("Israel /  United States") that is not a country
code at all. The failure is silent: the queue only asks about EMPTY fields, so
those rows would never reach the judge.

Battery publishes its own Location per company on 350 portfolio pages. That is
a first-party layer, it carries the CITY as well, and where the two disagree
the site wins. This pass emits both columns from it, flagging every row where
it overrides a Wikidata value with model_disputes_source.

Output: scratch/queue/site-location.out.jsonl (recorded like any batch).
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
from paths import Paths  # noqa: E402

P = Paths("battery-ventures")
US_STATES = {
    "alabama","alaska","arizona","arkansas","california","colorado","connecticut",
    "delaware","florida","georgia","hawaii","idaho","illinois","indiana","iowa",
    "kansas","kentucky","louisiana","maine","maryland","massachusetts",
    "massachussetts","michigan","minnesota","mississippi","missouri","montana",
    "nebraska","nevada","new hampshire","new jersey","new mexico","new york",
    "north carolina","north dakota","ohio","oklahoma","oregon","pennsylvania",
    "rhode island","south carolina","south dakota","tennessee","texas","utah",
    "vermont","virginia","washington","west virginia","wisconsin","wyoming",
    "washington, d.c.","district of columbia",
}
COUNTRY = {
    "united states":"US","usa":"US","canada":"CA","ontario":"CA","quebec":"CA",
    "québec":"CA","british columbia":"CA","united kingdom":"GB","england":"GB",
    "scotland":"GB","wales":"GB","uk":"GB","israel":"IL","germany":"DE",
    "france":"FR","netherlands":"NL","the netherlands":"NL","belgium":"BE",
    "spain":"ES","italy":"IT","sweden":"SE","norway":"NO","denmark":"DK",
    "finland":"FI","ireland":"IE","switzerland":"CH","austria":"AT",
    "poland":"PL","portugal":"PT","czech republic":"CZ","czechia":"CZ",
    "india":"IN","china":"CN","japan":"JP","south korea":"KR","korea":"KR",
    "singapore":"SG","australia":"AU","new zealand":"NZ","brazil":"BR",
    "mexico":"MX","argentina":"AR","chile":"CL","colombia":"CO","estonia":"EE",
    "lithuania":"LT","latvia":"LV","romania":"RO","bulgaria":"BG","greece":"GR",
    "turkey":"TR","south africa":"ZA","nigeria":"NG","kenya":"KE","egypt":"EG",
    "uae":"AE","united arab emirates":"AE","saudi arabia":"SA","hong kong":"HK",
    "taiwan":"TW","indonesia":"ID","vietnam":"VN","thailand":"TH",
    "philippines":"PH","malaysia":"MY","luxembourg":"LU","hungary":"HU",
    "slovakia":"SK","slovenia":"SI","croatia":"HR","serbia":"RS","ukraine":"UA",
}
# The firm's own spellings, corrected to the municipality the column wants.
CITY_FIX = {
    "herzelia":"Herzliya","ra'anana":"Ra'anana","montreal":"Montreal",
    "washington, d.c.":"Washington","nyc":"New York","new york city":"New York",
    "san francisco bay area":"San Francisco","tel-aviv":"Tel Aviv",
}


def parse(loc: str):
    """'Kitchener, Ontario' -> ('Kitchener','CA'); 'Austin, Texas' -> (...,'US')."""
    if not loc or "&" in loc or loc.count(",") > 2:
        return None, None           # multi-HQ strings are not a single answer
    parts = [p.strip() for p in loc.split(",") if p.strip()]
    if not parts:
        return None, None
    city = parts[0]
    tail = parts[-1].lower() if len(parts) > 1 else ""
    country = None
    if tail in US_STATES:
        country = "US"
    elif tail in COUNTRY:
        country = COUNTRY[tail]
    elif len(parts) == 1 and city.lower() in COUNTRY:
        return None, COUNTRY[city.lower()]
    city = CITY_FIX.get(city.lower(), city)
    city = re.sub(r"\s+", " ", city).strip()
    if city and city == city.lower():
        city = city.title()
    return (city or None), country


def main() -> None:
    site = {r["name"]: r for r in json.load(open(P.site / "companies.json"))}
    base = json.load(open(P.base_json))
    res = json.load(open(P.resolved))
    res = res.get("battery-ventures", res)
    out, stats = [], {"emitted": 0, "disputed": 0, "no_parse": 0}
    for r in base:
        s = site.get(r["name"])
        if not s or not s.get("site_location"):
            continue
        city, country = parse(s["site_location"])
        if not country:
            stats["no_parse"] += 1
            continue
        cur = res.get(r["slug"]) or {}
        rec = {"slug": r["slug"],
               "hq_country": country,
               "hq_country_source": "web_verified",
               "hq_country_citation": s.get("url") or "https://www.battery.com/company/",
               "hq_country_confidence": "high"}
        if city:
            rec.update({"hq_city": city, "hq_city_source": "web_verified",
                        "hq_city_confidence": "high"})
        flags, why = [], []
        old = cur.get("hq_country")
        if old and old != country:
            flags.append("model_disputes_source")
            why.append(f"overrides {cur.get('hq_country_source')} value {old!r}")
            stats["disputed"] += 1
        if flags:
            rec["flags"] = flags
        rec["note"] = ("Battery's own Location field on its company page: "
                       f"'{s['site_location']}'. First-party and city-bearing, so it "
                       "outranks the Wikidata join for this book"
                       + ("; " + "; ".join(why) if why else "") + ".")
        out.append(rec)
        stats["emitted"] += 1
    path = P.queue / "site-location.out.jsonl"
    path.write_text("\n".join(json.dumps(r) for r in out) + "\n")
    print(f"wrote {path}: {stats['emitted']} rows "
          f"({stats['disputed']} overriding a wrong pre-fill, "
          f"{stats['no_parse']} unparseable locations)")


if __name__ == "__main__":
    main()
