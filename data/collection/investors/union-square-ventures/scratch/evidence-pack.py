#!/usr/bin/env python3
"""Assemble, per base row, every first-party and third-party text the judge reads (COLLECTION.md
§3/§6) for Union Square Ventures: the live list row (first-investment label, year, exit detail,
excerpt, sectors, status/entry-point terms, post link), the archived listing years, the firm's
2013-2015 per-card attributes (series, year, city, categories, current/past) and 2016-2019 card
meta, the firm's posts naming the company (title matches first, then text mentions; sentences with
round words kept, decimals preserved), the Wikipedia insource sentences, the EDGAR full-text hits,
the ownership forms, and the Form D round history (formd-issuer-rounds.json after prepare).
Output: scratch/evidence-pack.json plus render(slug) used by the gate and the grind."""
import json, re, html
from pathlib import Path
I = Path("/Users/erik/Developer/merit-capital/data/collection/investors/union-square-ventures")
S = I / "sources/site"
base = json.load(open(I / "base.json"))
live = {r["name"].lower(): r for r in json.load(open(S / "live-companies.json"))["rows"]}
a13 = {r["slug"]: r["by_capture"] for r in json.load(open(S / "portfolio-2013-2015.json"))["rows"]}
a16 = {r["slug"]: r["by_capture"] for r in json.load(open(S / "portfolio-2016-2019.json"))["rows"]}
posts = json.load(open(S / "wp-posts.json"))["posts"]
merges = json.load(open(I / "identity-merges.json"))["union-square-ventures"]["merges"]
aliases = {m["canonical"]: m["duplicates"] for m in merges}
wiki_p = I / "sources/web/wikipedia-insource.json"
wiki = json.load(open(wiki_p)).get("articles", []) if wiki_p.exists() else []
fts_p = I / "sources/edgar/fts-hits.json"
fts = json.load(open(fts_p)) if fts_p.exists() else {}
rounds_p = I / "sources/edgar/formd-issuer-rounds.json"
rounds = json.load(open(rounds_p)) if rounds_p.exists() else {}
resolved_p = I / "resolved.json"
resolved = json.load(open(resolved_p)) if resolved_p.exists() else {}
def slug_of(n): return re.sub(r"[^a-z0-9]+", "-", n.lower()).strip("-")
def loose(n):
    n = re.sub(r"\(.*?\)", "", (n or "").lower())
    n = re.sub(r"\b(inc|the|company|corp|llc|ltd|labs?|technologies)\b", "", n)
    return re.sub(r"[^a-z0-9]", "", n)
SHORT = {"code", "board", "anon", "glow", "flip", "leap", "wren", "sift", "sling", "sora", "otis", "juro", "koko", "dia", "jam", "karat", "kiosk", "recall", "presto", "supper", "ghost", "slope", "props", "noah", "ncx", "bolt", "canvas", "consensus", "daylight", "daybreak", "mindset", "odyssey", "radiant", "remora", "reservoir", "scroll", "tapestry", "unigrid", "viam", "stacks", "pilot", "clue", "stash", "upgrade", "splice", "amino", "assembly", "brewster", "tracked", "hashable", "indeed", "twitter", "dune", "meetup", "kik", "etsy", "revel", "revos", "human dx", "figure1", "figure 1", "fomo", "pascal", "gritt", "suno", "miren", "cactos", "lydian", "neynar", "farcaster", "generalist", "mundi", "mombak", "ostrom", "zanskar", "xfuel", "veniam", "vhx", "sigfig", "soona", "m3ter", "isembard", "pluralis", "volteras", "electroflow", "doctronic", "teamshares", "transmutex", "top hat", "outschool", "paragraph", "possible finance"}
def name_variants(row):
    names = {row["name"]}
    names |= {a.replace("-", " ") for a in aliases.get(row["slug"], [])}
    m = re.match(r"(.+?)\s*\((.+?)\)", row["name"])
    if m: names |= {m.group(1).strip(), m.group(2).strip()}
    if "/" in row["name"]: names |= {p.strip() for p in row["name"].split("/")}
    return {n for n in names if n and len(n) > 1}
def mentions(text, names):
    for n in names:
        flags = 0 if (len(n) <= 5 or n.lower() in SHORT) else re.I
        if re.search(r"(?<![A-Za-z0-9])" + re.escape(n) + r"(?![A-Za-z0-9])", text, flags):
            return True
    return False
RW = re.compile(r"\b(Series [A-F]\b|seed|Seed|pre-seed|led |lead |round|financing|invest(?:ed|ment|ing)\b|raise[ds]?|acquired|acquisition|shut|wind|IPO|public|valuation|billion|million)", re.I)
def sentences(text):
    # split on sentence ends but never at a decimal point ("$5.1M")
    parts = re.split(r"(?<!\d)\.(?!\d)\s+|[!?]\s+", text)
    return [p.strip() for p in parts if p.strip()]
pack = {}
for row in base:
    slug = row["slug"]; names = name_variants(row)
    lv = live.get(row["name"].lower())
    e = {"slug": slug, "name": row["name"], "tier": row.get("tier"), "first_seen": row.get("first_seen"), "wayback_years": row.get("wayback_years"), "site_url": row.get("site_url"),
         "edgar_forms": row.get("edgar_forms"), "edgar_links": row.get("edgar_links"), "formd_partners": row.get("partners_formd"), "formd_links": row.get("formd_links"), "formd_span": row.get("formd_span"), "formd_max_round_usd": row.get("formd_max_round_usd"), "notes": row.get("notes")}
    if lv:
        e["live"] = {k: lv.get(k) for k in ("first_investment", "round_site", "invest_year", "exit_detail", "excerpt", "post", "sectors", "status_site", "entry_point_site", "url")}
    for s in [slug] + aliases.get(slug, []):
        if s in a13: e["archived_2013_2015"] = a13[s]
        if s in a16: e["archived_2016_2019"] = a16[s]
    # posts: the linked post first, then title matches, then text mentions (max 8)
    hits = []
    linked = (lv or {}).get("post")
    for p in posts:
        title_hit = mentions(p["title"], names)
        is_linked = linked and p["link"].rstrip("/") == linked.rstrip("/")
        if is_linked or title_hit or mentions(p["text"][:20000], names):
            sents = [s for s in sentences(p["text"]) if mentions(s, names) or (is_linked and RW.search(s))]
            keep = [s[:300] for s in sents if RW.search(s)][:5] or [s[:300] for s in sents[:2]]
            hits.append({"date": p["date"][:10], "title": p["title"], "url": p["link"], "linked": bool(is_linked), "title_match": title_hit, "sentences": keep})
    hits.sort(key=lambda h: (not h["linked"], not h["title_match"], h["date"]))
    e["posts"] = hits[:8]; e["post_hits_total"] = len(hits)
    e["wikipedia"] = [{"title": a.get("title"), "url": a.get("url"), "sentences": (a.get("sentences") or a.get("naming_sentences") or [])[:3]} for a in wiki if mentions(json.dumps(a)[:5000], names)][:3]
    fts_hits = []
    for r in (fts.get("registrants") or []):
        if r.get("bucket") in ("own", "lp", "own_entity", "lp_fund"): continue
        blob = r.get("registrant", "") + " " + json.dumps(r.get("filings") or [])[:6000]
        if mentions(blob, names):
            sents = [s for x in (r.get("filings") or []) for s in (x.get("sentences") or x.get("snippets") or [])][:3]
            fts_hits.append({"registrant": r.get("registrant"), "bucket": r.get("bucket"), "forms": r.get("forms"), "first_date": r.get("first_date"), "sentences": [str(t)[:300] for t in sents]})
    e["fts"] = fts_hits[:3]
    e["formd_rounds"] = rounds.get(slug, {}).get("rounds")
    e["deterministic"] = resolved.get(slug)
    pack[slug] = e
json.dump(pack, open(I / "scratch/evidence-pack.json", "w"), indent=1, ensure_ascii=False)
print("pack rows", len(pack), "with live", sum(1 for e in pack.values() if "live" in e), "with posts", sum(1 for e in pack.values() if e["posts"]), "with archived labels", sum(1 for e in pack.values() if "archived_2013_2015" in e or "archived_2016_2019" in e))
def render(slug):
    e = pack[slug]; out = [f"## {e['name']} ({slug}) tier {e['tier']} first_seen {e['first_seen']} wayback {e['wayback_years']}"]
    if e.get("live"): out.append("LIVE: " + json.dumps(e["live"], ensure_ascii=False))
    for k in ("archived_2013_2015", "archived_2016_2019"):
        if e.get(k): out.append(f"{k}: " + json.dumps(e[k], ensure_ascii=False)[:600])
    out.append(f"EDGAR forms {e['edgar_forms']} | Form D partners {e['formd_partners']} span {e['formd_span']} max {e['formd_max_round_usd']} | notes {e['notes']}")
    if e.get("formd_rounds"): out.append("FORM D ROUNDS: " + json.dumps(e["formd_rounds"], ensure_ascii=False)[:800])
    if e.get("deterministic"): out.append("DETERMINISTIC: " + json.dumps(e["deterministic"], ensure_ascii=False)[:500])
    for p in e["posts"]:
        out.append(f"POST {p['date']} {'[linked] ' if p['linked'] else ''}{p['title']} <{p['url']}>"); out += ["   - " + s for s in p["sentences"]]
    for w in e["wikipedia"]: out.append(f"WIKI {w['title']} <{w['url']}> " + " | ".join(w["sentences"]))
    for f in e["fts"]: out.append(f"FTS [{f['bucket']}] {f['registrant']} {f['first_date']} {f['forms']} " + " | ".join(f["sentences"])[:500])
    return "\n".join(out)
if __name__ == "__main__":
    import sys
    for s in sys.argv[1:]: print(render(s)); print()
