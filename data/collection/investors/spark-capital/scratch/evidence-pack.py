#!/usr/bin/env python3
"""Assemble, per base row, every first-party and third-party text the judge reads
(COLLECTION.md §3/§6) for Spark Capital: the live Webflow card (description, exit marker,
website), the archived Webflow cards (years listed, latest exit marker), the 2015-2020
listing labels (sector / geo / seed-venture-growth per year), the firm's archived news
titles naming the company (2006-2016), the Wikipedia insource sentences, the EDGAR
full-text snippets, the Form D sweep (partner seats with years and roles), the issuer
round history (formd-issuer-rounds.json, after prepare) and the fund ownership filings.
Output: scratch/evidence-pack.json plus `render(slug)` used by the gate and the grind.
Sentence splitter keeps decimals ('$5.1M' is not a sentence end; Cherry 2026-09-04)."""
import json, re, sys, html
from pathlib import Path
I = Path("/Users/erik/Developer/merit-capital/data/collection/investors/spark-capital")
S = I / "sources/site"
base = json.load(open(I / "base.json"))
site = {c["slug"]: c for c in json.load(open(S / "companies.json"))}
site_by_key = {re.sub(r"[^a-z0-9]", "", c["name"].lower()): c for c in site.values()}
live = {r["name"]: r for r in json.load(open(S / "webflow-companies.json"))["rows"]}
arch = {r["name"]: r for r in json.load(open(S / "webflow-archive-companies.json"))["rows"]}
tags = {r["slug"]: r for r in json.load(open(S / "wp-companies-2015-2020.json"))["rows"]}
tags_by_name = {re.sub(r"[^a-z0-9]", "", r["name"].lower()): r for r in tags.values()}
news = json.load(open(I / "sources/web/news-archive-urls.json"))["articles"]
wiki_p = I / "sources/web/wikipedia-insource.json"
wiki = json.load(open(wiki_p))["articles"] if wiki_p.exists() else []
fts_p = I / "sources/edgar/fts-hits.json"
fts = json.load(open(fts_p)) if fts_p.exists() else {}
sweep = json.load(open(I / "sources/edgar/formd-sweep.json"))
rounds_p = I / "sources/edgar/formd-issuer-rounds.json"
rounds = json.load(open(rounds_p)) if rounds_p.exists() else {}
edgar = {c["name"]: c for c in json.load(open(I / "sources/edgar/edgar-companies.json"))}
idm = json.load(open(I / "identity-merges.json"))["spark-capital"]["merges"]
aliases = {m["canonical"]: [m["canonical"]] + m["duplicates"] for m in idm}

def loose(n):
    n = re.sub(r"\(.*?\)", "", (n or "").lower())
    n = re.sub(r"\b(inc|corp|corporation|co|company|ltd|limited|llc|lp|l\.p|the|group|holdings?|technologies|technology|labs|networks|systems|software)\b", "", n)
    return re.sub(r"[^a-z0-9]", "", n)

SHORT = {"post", "coin", "hey", "jam", "super", "north", "common", "lift", "relay", "beam", "perch", "clyde", "colu", "lumi", "brud", "ada", "adept", "durable", "garden", "nomad", "convex", "producer", "midas", "medium", "n3", "fig", "x1", "zeal", "zum", "sift", "kik", "diy", "kumu", "goji", "lily", "lola", "haven", "jelly", "jana", "verse", "nift", "pixie", "plume", "snap", "ramp", "deel", "slack", "cameo", "studs", "spinn", "tatch", "noyo", "noom", "sonder", "materia", "helaina", "cimulate", "clora", "carta", "eqal", "intune", "xoova", "sendme", "gdgt", "exfm", "kateeva", "andela", "affirm", "plaid", "boxee", "tumblr", "twitter", "oculus", "cruise", "discord", "niantic"}

def name_variants(row):
    names = {row["name"]}
    for a in aliases.get(row["slug"], []):
        names.add(a.replace("-", " "))
        for k, c in site.items():
            if k == a: names.add(c["name"])
    m = re.match(r"(.+?)\s*\(formerly (.+?)\)", row["name"])
    if m: names |= {m.group(1).strip(), m.group(2).strip()}
    return {n for n in names if n and len(n) > 1}

def mentions(text, names):
    for n in names:
        flags = 0 if (len(n) <= 5 or n.lower() in SHORT) else re.I
        if re.search(r"(?<![A-Za-z0-9])" + re.escape(n) + r"(?![A-Za-z0-9])", text or "", flags):
            return True
    return False

pack = {}
for row in base:
    slug = row["slug"]; names = name_variants(row); lk = loose(row["name"])
    e = {"slug": slug, "name": row["name"], "tier": row["tier"], "first_seen": row["first_seen"],
         "wayback_years": row["wayback_years"], "site_url": row["site_url"], "sector": row["sector"],
         "partners_site": row["partners_site"], "partners_formd": row["partners_formd"],
         "formd_span": row["formd_span"], "formd_links": row["formd_links"], "edgar_forms": row["edgar_forms"],
         "edgar_links": row["edgar_links"], "wayback_first_link": row["wayback_first_link"], "notes": row["notes"]}
    sc = site.get(slug) or site_by_key.get(re.sub(r"[^a-z0-9]", "", row["name"].lower()))
    if sc:
        e["site"] = {k: sc.get(k) for k in ("lists", "description", "acquisition_spec", "years_listed", "stage_site_first", "stage_site_all", "geo_site", "sectors") if sc.get(k) not in (None, "", [])}
    for nm in names:
        if nm in live: e["live_card"] = {k: live[nm].get(k) for k in ("description", "acquisition_spec", "url", "sectors_site")}
        if nm in arch: e["archive_card"] = {k: arch[nm].get(k) for k in ("acquisition_spec", "years_listed", "description")}
    t = tags.get(slug) or tags_by_name.get(re.sub(r"[^a-z0-9]", "", row["name"].lower()))
    if t: e["site_labels"] = {"stage_first": t["stage_site_first"], "stage_all": t["stage_site_all"], "sectors": t["sectors_site"], "geo": t["geo_site"], "years": t["years_listed"], "by_year": t["labels"]}
    hits = [a for a in news if mentions(a["title_guess"], names) or lk and lk in loose(a["title_guess"])]
    if hits: e["news_titles"] = [{"year": a["first_capture"][:4], "title": a["title_guess"], "path": a["path"]} for a in hits[:8]]
    w = [a for a in wiki if a.get("in_base") == slug or loose(a["title"]) == lk]
    if w: e["wikipedia"] = [{"title": a["title"], "sentences": (a.get("sentences") or [])[:4]} for a in w]
    f = [h for h in (fts.get("registrants") or fts if isinstance(fts, dict) else []) if False]
    seats = []
    for acc, r in sweep.items():
        if loose(r.get("issuer")) == lk or (row["formd_accessions"] and acc in row["formd_accessions"]):
            for p in r["persons"]:
                seats.append({"acc": acc, "issuer": r.get("issuer"), "person": p["person"], "role": p.get("relationship"), "q": p.get("quarter"), "sold": r.get("total_sold"), "offering": r.get("total_offering"), "industry": r.get("industry_group"), "city": r.get("city"), "state": r.get("state")})
    if seats: e["formd_seats"] = sorted(seats, key=lambda s: s["q"] or "")
    if slug in rounds: e["rounds"] = [{k: r.get(k) for k in ("quarter", "sale_date", "filing_date", "offering_usd", "sold_usd", "is_partner_round") if r.get(k) is not None} for r in rounds[slug].get("rounds", [])][:12]
    for nm, c in edgar.items():
        if loose(nm) == lk: e["edgar_filings"] = {k: c.get(k) for k in ("forms", "first", "last", "cik", "roles")}
    pack[slug] = e
json.dump(pack, open(I / "scratch/evidence-pack.json", "w"), indent=1)

def render(slug, width=110):
    e = pack[slug]; out = [f"## {e['name']} ({slug}) tier {e['tier']} first_seen {e['first_seen']} wayback {e['wayback_years'] or '-'}"]
    for k in ("site", "live_card", "archive_card", "site_labels", "news_titles", "wikipedia", "formd_seats", "rounds", "edgar_filings"):
        if e.get(k): out.append(f"- {k}: {json.dumps(e[k], ensure_ascii=False)[:1400]}")
    if e.get("notes"): out.append(f"- notes: {e['notes'][:300]}")
    return "\n".join(out)

if __name__ == "__main__":
    print(len(pack), "rows packed;", sum(1 for e in pack.values() if e.get("news_titles")), "with firm news titles;", sum(1 for e in pack.values() if e.get("site_labels")), "with site labels;", sum(1 for e in pack.values() if e.get("formd_seats")), "with Form D seats;", sum(1 for e in pack.values() if e.get("rounds")), "with round histories")
    for s in sys.argv[1:]: print(render(s))
