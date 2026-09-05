#!/usr/bin/env python3
"""Assemble, per base row, (sentence splitter keeps decimals: '$5.1M' is not a sentence end — the defect that truncated Zaro's and Forgent's round names on 2026-09-04)
 every first-party and third-party text the judge reads
(COLLECTION.md §3/§6) for Cherry Ventures: the 2026 Webflow page fields, the Sanity
CMS row, the archived 2016-2023 listing attributes (investment date, 2016-2019 stage
label, exit years), the job-board row, the firm's posts naming the company (Webflow
news, Sanity articles, recovered WordPress / Common Crawl posts), the Wikipedia
sentences, the Form D round history. Output: scratch/evidence-pack.json plus
`render(slug)` used by the gate and the grind."""
import json, re, sys, html
from pathlib import Path
I = Path("data/collection/investors/cherry")
S = I / "sources/site"
base = json.load(open(I / "base.json"))
site = {c["slug"]: c for c in json.load(open(S / "companies.json"))}
webflow = {r["slug"]: r for r in json.load(open(S / "webflow-companies.json"))["rows"]}
sanity = {r["slug"]: r for r in json.load(open(S / "sanity-companies.json"))["rows"]}
arch = json.load(open(S / "portfolio-2016-2023.json"))["rows"]
board = {r["board_slug"]: r for r in json.load(open(S / "jobs-board-companies.json"))["rows"]}
posts = []
for a in json.load(open(S / "announcements-webflow.json"))["items"]:
    posts.append({"src": "news", "date": a["date_iso"], "title": a["title"], "url": a["url"], "text": a["text"] or "", "related": a.get("related_companies") or []})
for a in json.load(open(S / "sanity-articles.json"))["items"]:
    posts.append({"src": "sanity", "date": a["date"], "title": a["title"], "url": "https://763y4e9t.api.sanity.io/v2021-10-21/data/query/production?query=*[_type=='article' %26%26 slug.current=='" + (a["slug"] or "") + "']", "text": a["text"] or "", "related": []})
for a in json.load(open(S / "announcements-wordpress.json"))["items"]:
    posts.append({"src": "wp", "date": a["date"], "title": a["title"], "url": a["archive_url"] or a["url"], "text": a["text"] or "", "related": []})
for a in json.load(open(S / "announcements-commoncrawl.json"))["items"]:
    posts.append({"src": "cc", "date": a["date"], "title": a["title"], "url": a["url"], "text": a["text"] or "", "related": []})
wiki_p = I / "sources/web/wikipedia-insource.json"
wiki = json.load(open(wiki_p))["articles"] if wiki_p.exists() else []
rounds_p = I / "sources/edgar/formd-issuer-rounds.json"
rounds = json.load(open(rounds_p)) if rounds_p.exists() else {}
merges = json.load(open(I / "identity-merges.json"))["cherry"]["merges"]
aliases = {m["canonical"]: [m["canonical"]] + m["duplicates"] for m in merges}

def loose(n):
    n = re.sub(r"\(.*?\)", "", (n or "").lower())
    n = re.sub(r"\b(inc|ab|as|oy|gmbh|ltd|limited|the|company|group|formerly|se|ag)\b", "", n)
    return re.sub(r"[^a-z0-9]", "", n)

SHORT = {"ben", "bits", "rows", "swap", "mine", "voy", "coral", "light", "klar", "goals", "juni", "moss", "flix", "maze", "beo", "tola", "save", "shift", "soba", "flink", "manual", "together", "plato", "aware", "zaro", "kiku", "swap", "weld", "enfold", "aloha", "lenda", "styla", "curio", "airy", "fizz", "uify", "unlock", "talea", "elise", "hadrian", "vesper", "qura", "numa", "cosi", "wunder", "integral", "finesse", "bunch"}

def name_variants(row):
    names = {row["name"]}
    slug = row["slug"]
    names |= {a.replace("-", " ") for a in aliases.get(slug, [])}
    for r in arch:
        if slug in r["slugs"] or loose(r["name"]) == loose(row["name"]):
            names |= set(r["names"])
    if slug in webflow: names.add(webflow[slug]["name"])
    if slug in sanity: names.add(sanity[slug]["name"])
    m = re.match(r"(.+?)\s*\(formerly (.+?)\)", row["name"])
    if m: names |= {m.group(1).strip(), m.group(2).strip()}
    return {n for n in names if n and len(n) > 1}

def mentions(text, names):
    for n in names:
        flags = 0 if (len(n) <= 5 or n.lower() in SHORT) else re.I
        if re.search(r"(?<![A-Za-z0-9])" + re.escape(n) + r"(?![A-Za-z0-9])", text, flags):
            return True
    return False

def round_snips(text, names):
    out = []
    for m in re.finditer(r"(?:[^.!?\n]|\.(?=\d))*[.!?](?!\d)", text or ""):
        s = re.sub(r"\s+", " ", m.group(0)).strip()
        if mentions(s, names) and re.search(r"\b(pre-seed|seed|series [a-e]\b|first (?:institutional )?(?:round|investment|check)|financing round|funding round|led|leading|lead|co-led|secondary|round of|raises|raised|invest(?:ed|s|ing|ment)? in|backed|backing|acquired|acquisition|IPO|exit|insolven|shut|closed down|valuation|unicorn|billion)\b", s, re.I):
            out.append(s[:320])
        if len(out) >= 6: break
    return out

pack = {}
for row in base:
    slug = row["slug"]; names = name_variants(row); lname = loose(row["name"])
    hits = []
    for p in posts:
        body = (p["title"] or "") + ". " + p["text"]
        if slug in p["related"] or mentions(p["title"] or "", names) or (len(row["name"]) > 3 and mentions(p["text"], names)):
            sn = round_snips(body, names)
            if sn or slug in p["related"] or mentions(p["title"] or "", names):
                hits.append({"src": p["src"], "date": p["date"], "title": (p["title"] or "")[:100], "url": p["url"], "snips": sn[:5]})
    hits.sort(key=lambda h: h["date"] or "")
    ar = next((r for r in arch if slug in r["slugs"] or loose(r["name"]) == lname or any(loose(n) == lname for n in r["names"])), None)
    bd = next((b for b in board.values() if loose(b["name"]) == lname or any(loose(n) == loose(b["name"]) for n in names)), None)
    wk = [w for w in wiki if loose(w["title"]) == lname or w.get("in_base") == slug]
    pack[slug] = {
        "name": row["name"], "tier": row["tier"], "first_seen": row["first_seen"], "wayback_years": row["wayback_years"],
        "partners_site": row["partners_site"], "partners_formd": row["partners_formd"], "formd_links": row["formd_links"],
        "webflow": {k: webflow[slug].get(k) for k in ("industry", "location", "founded", "founders", "website", "description", "exit_tag", "on_founders_list")} if slug in webflow else None,
        "sanity": {k: sanity[slug].get(k) for k in ("date", "invest_year", "founded_site", "tag_titles", "exit_tag", "website", "description", "founders")} if slug in sanity else None,
        "archive": {k: ar.get(k) for k in ("names", "invest_date", "invest_year", "stage_site", "launch_year", "founders", "website", "sectors", "status_site", "exit_years", "years_listed", "description")} if ar else None,
        "board": {k: bd.get(k) for k in ("stage", "industry_tags", "locations", "founded", "head_count", "org_type", "website", "description")} if bd else None,
        "posts": hits[:8],
        "wikipedia": [{"title": w["title"], "url": w["url"], "sentences": w["sentences"][:3]} for w in wk],
        "formd_rounds": [{"q": r.get("quarter"), "usd": r.get("offering_usd"), "sale": r.get("sale_date")} for r in rounds.get(slug, {}).get("rounds", [])],
    }
(I / "scratch/evidence-pack.json").write_text(json.dumps(pack, indent=1, ensure_ascii=False))
print(f"pack: {len(pack)} rows; with posts {sum(1 for v in pack.values() if v['posts'])}, webflow {sum(1 for v in pack.values() if v['webflow'])}, sanity {sum(1 for v in pack.values() if v['sanity'])}, archive {sum(1 for v in pack.values() if v['archive'])}, board {sum(1 for v in pack.values() if v['board'])}, wiki {sum(1 for v in pack.values() if v['wikipedia'])}")

def render(slug, p=None):
    p = p or pack[slug]
    L = [f"### {slug} | {p['name']} | tier {p['tier']} | first_seen {p['first_seen']} | wb {p['wayback_years'][:70]} | formd {p['partners_formd'] or ''}"]
    if p["webflow"]: L.append(f"  webflow: {json.dumps(p['webflow'], ensure_ascii=False)[:400]}")
    if p["sanity"]: L.append(f"  sanity: {json.dumps(p['sanity'], ensure_ascii=False)[:300]}")
    if p["archive"]: L.append(f"  archive: {json.dumps(p['archive'], ensure_ascii=False)[:420]}")
    if p["board"]: L.append(f"  board: {json.dumps(p['board'], ensure_ascii=False)[:260]}")
    for x in p["posts"][:6]:
        L.append(f"  post {x['date']} [{x['src']}] {x['title'][:70]}")
        for sn in x["snips"][:3]: L.append(f"     - {sn[:240]}")
    for w in p["wikipedia"]:
        L.append(f"  wiki {w['title']} {w['url']}")
        for sn in w["sentences"][:2]: L.append(f"     - {sn[:240]}")
    if p["formd_rounds"]: L.append(f"  formd: {p['formd_rounds']}")
    return "\n".join(L)

if __name__ == "__main__" and len(sys.argv) > 1:
    for s in sys.argv[1:]:
        print(render(s)); print()
