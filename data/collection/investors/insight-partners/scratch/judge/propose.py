#!/usr/bin/env python3
"""First-party proposals for the judge, per queue row. Nothing here is a
verdict: it reads what the firm's own site and posts state and lays it out so
the judge confirms or overrides each row.

  hq            the panel's location ("Denver, Colorado, U.S."): city and country
  focus         the panel's sectors through config.profile.focus_crosswalk,
                with the playbook's precedence (Security first, then Crypto,
                Healthcare, AI)
  entry_stage   a post of the firm's whose TITLE names a round and whose date
                falls within four months of the panel's first-investment
                month: the firm dates its own entry and the post names the
                round of that date, so the post is the entry's announcement
                (class 1, web_verified, the post as citation). A post with no
                matching first-investment month proposes nothing: an
                announcement names the round the firm LED, which may be a
                follow-on (COLLECTION.md 6).
  control hint  control wording in a post title near the first-investment
                month, or a holding-company Form D ("Parent", "HoldCo",
                "TopCo", "Holdings") signed by the firm's partners

Writes scratch/judge/prefill.json {slug: {...}} and prints nothing unless asked.
Usage: python3 .../scratch/judge/propose.py [--table batch-file]
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

INV = Path(__file__).resolve().parents[2]
CFG = json.load(open(INV / "config.json"))
XW = CFG["profile"]["focus_crosswalk"]
PRECEDENCE = ["Security", "Crypto & Web3", "Healthcare & Bio", "AI & Applied AI", "Fintech & Payments",
              "Data Infrastructure", "DevTools & APIs", "Climate & Energy", "Industrial & Robotics",
              "Media, Gaming & Advertising", "Consumer & Marketplaces", "SaaS"]

COUNTRY = {
    "U.S.": "US", "U.K.": "GB", "Israel": "IL", "Germany": "DE", "Canada": "CA", "Australia": "AU",
    "France": "FR", "Netherlands": "NL", "India": "IN", "Ireland": "IE", "Sweden": "SE", "Belgium": "BE",
    "Singapore": "SG", "Brazil": "BR", "Switzerland": "CH", "Hungary": "HU", "Argentina": "AR",
    "Indonesia": "ID", "Spain": "ES", "Austria": "AT", "Denmark": "DK", "Russia": "RU", "Cyprus": "CY",
    "Bahamas": "BS", "Philippines": "PH", "Norway": "NO", "New Zealand": "NZ", "Hong Kong": "HK",
    "Italy": "IT", "Lithuania": "LT", "CA": "US", "MA": "US",
}
CITY_FIX = {"New York City": "New York", "NYC": "New York", "Tel Aviv-Yafo": "Tel Aviv",
            "Tel-Aviv": "Tel Aviv", "Bengaluru": "Bangalore", "Brooklyn": "New York",
            "Manhattan": "New York", "Washington, D.C.": "Washington", "Washington D.C.": "Washington",
            "München": "Munich", "Köln": "Cologne", "Sao Paulo": "São Paulo"}
ROUND_STAGE = [
    (re.compile(r"\bpre-seed\b", re.I), "Pre-Seed"),
    (re.compile(r"\bseed\b", re.I), "Seed"),
    (re.compile(r"\bseries\s+a\d?\b", re.I), "Series A"),
    (re.compile(r"\bseries\s+[b-k]\d?\b", re.I), "Growth"),
    (re.compile(r"\bgrowth (?:equity |capital )?(?:round|investment|financing|funding)\b|strategic growth investment|minority (?:growth )?investment", re.I), "Growth"),
]
CONTROL_T = re.compile(r"\b(acquires?|to acquire|acquired by|acquisition (?:of|by)|majority|take[- ]private|recapitali[sz]ation|buyout)\b", re.I)
HOLDCO = re.compile(r"\b(parent|holdco|topco|top co|holdings?|buyer|aggregator|ultimate parent|intermediate)\b", re.I)


def months(a: str, b: str) -> int:
    ya, ma = int(a[:4]), int(a[5:7])
    yb, mb = int(b[:4]), int(b[5:7])
    return abs((ya - yb) * 12 + (ma - mb))


def hq_of(loc: str):
    if not loc:
        return None, None
    parts = [p.strip() for p in loc.split(",") if p.strip()]
    cc = COUNTRY.get(parts[-1])
    if not cc:
        return None, None
    city = parts[0]
    city = CITY_FIX.get(city, city)
    if len(parts) == 1 or not city or re.search(r"\d", city) or city in COUNTRY:
        return None, cc
    city = city[0].upper() + city[1:]
    return city, cc


def focus_of(sectors: list[str]):
    got = [XW[s] for s in sectors if s in XW]
    for p in PRECEDENCE:
        if p in got:
            return p
    return None


def stage_from_title(title: str):
    for rx, st in ROUND_STAGE:
        m = rx.search(title)
        if m:
            return st, m.group(0)
    return None, None


def main() -> None:
    site = {r["url"].rstrip("/"): r for r in json.load(open(INV / "sources/site/company-pages.json"))["rows"]}
    posts = json.load(open(INV / "scratch/posts-by-company.json"))
    queue = json.load(open(INV / "scratch/queue/queue.json"))
    out = {}
    for it in queue:
        s = site.get((it.get("site_url") or "").rstrip("/"))
        p = {}
        if s:
            city, cc = hq_of(s.get("location") or "")
            if cc:
                p["hq_country"] = cc
            if city:
                p["hq_city"] = city
            f = focus_of(s.get("sectors") or [])
            if f:
                p["focus"] = f
            if s.get("invest_date"):
                p["entry_date"] = s["invest_date"]
            init = s.get("invest_date") or ""
            for po in posts.get(s["slug"]) or []:
                st, word = stage_from_title(po["title"])
                near = init and months(po["date"][:7], init) <= 4
                if st and near and "entry_stage" not in p:
                    p["entry_stage"] = st
                    p["entry_stage_citation"] = po["url"]
                    p["entry_stage_word"] = f"{po['date'][:7]} '{word}'"
                if CONTROL_T.search(po["title"]) and near and re.search(r"insight", po["title"], re.I):
                    p["control_hint"] = f"post {po['date']}: {po['title'][:110]}"
        if HOLDCO.search(it["name"]) and it.get("partners_formd"):
            p.setdefault("control_hint", f"holding-company Form D signed by {it['partners_formd']}")
        out[it["slug"]] = p
    (INV / "scratch/judge/prefill.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
    n = len(out)
    print(f"proposals for {n} rows: hq_country {sum(1 for v in out.values() if 'hq_country' in v)}, "
          f"hq_city {sum(1 for v in out.values() if 'hq_city' in v)}, "
          f"focus {sum(1 for v in out.values() if 'focus' in v)}, "
          f"entry_stage {sum(1 for v in out.values() if 'entry_stage' in v)}, "
          f"control hints {sum(1 for v in out.values() if 'control_hint' in v)}")


if __name__ == "__main__":
    main()
