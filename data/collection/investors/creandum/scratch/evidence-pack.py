#!/usr/bin/env python3
"""Assemble, per base row, every first-party and third-party text the judge reads
(COLLECTION.md §3/§6): the live CMS row and the 2017-2023 site attributes, the
firm's stories and archived announcements that name the company, the Wikipedia
sentences, the Form D round history. Output: scratch/evidence-pack.json, plus a
`render(slug)` used by the gate and the grind to print one row's evidence."""
import json, re, sys, html
from pathlib import Path
I = Path("data/collection/investors/creandum")
base = json.load(open(I / "base.json"))
site = {c["slug"]: c for c in json.load(open(I / "sources/site/companies.json"))}
arch = {r["slug"].lower(): r for r in json.load(open(I / "sources/site/portfolio-2017-2023.json"))["rows"]}
stories = json.load(open(I / "sources/site/stories.json"))["articles"]
ann = json.load(open(I / "sources/site/announcements.json"))["items"]
wiki = json.load(open(I / "sources/web/wikipedia-insource.json"))["articles"]
rounds = json.load(open(I / "sources/edgar/formd-issuer-rounds.json")) if (I / "sources/edgar/formd-issuer-rounds.json").exists() else {}
merges = json.load(open(I / "identity-merges.json"))["creandum"]["merges"]
aliases = {m["canonical"]: [m["canonical"]] + m["duplicates"] for m in merges}

def loose(n):
    n = re.sub(r"\(.*?\)", "", (n or "").lower())
    n = re.sub(r"\b(inc|ab|as|oy|gmbh|ltd|limited|the|company|formerly)\b", "", n)
    return re.sub(r"[^a-z0-9]", "", n)

SHORT = {"peak", "leap", "tola", "craft", "swan", "bolt", "tide", "pipe", "toit", "voi", "cake", "kive", "osu", "klaus", "topi", "amie", "cint", "jays", "vint", "knc", "knl", "ivy", "bucket", "modal", "midas", "olix", "conduct", "mason", "laka", "twirl", "argent", "ready", "elastic", "blast", "atla", "1302", "fitbay", "syft", "narrative", "instruct", "vay", "8fit", "scapin", "yababa"}

def name_variants(row):
    names = {row["name"]}
    slug = row["slug"]
    names |= {a.replace("-", " ") for a in aliases.get(slug, [])}
    s = site.get(slug)
    if s: names.add(s["name"])
    m = re.match(r"(.+?)\s*\(formerly (.+?)\)", row["name"])
    if m: names |= {m.group(1).strip(), m.group(2).strip()}
    return {n for n in names if n}

def mentions(text, names, strict):
    """Whole-word match of any name variant. Short names (five letters or
    fewer: Peak, Dija, Swan, Tola) match case-sensitively so 'peak
    performance' and 'a swan' do not attach; longer names match
    case-insensitively. `strict` additionally requires the short form to be
    capitalized as the company writes it."""
    for n in names:
        flags = 0 if (strict or len(n) <= 5) else re.I
        if re.search(r"(?<![A-Za-z0-9])" + re.escape(n) + r"(?![A-Za-z0-9])", text, flags):
            return True
    return False

def round_snips(text, names):
    out = []
    for m in re.finditer(r"[^.!?\n]*[.!?]", text or ""):
        s = re.sub(r"\s+", " ", m.group(0)).strip()
        if re.search(r"\b(pre-seed|seed|series [a-e]\b|first (?:venture |institutional )?round|financing round|funding round|led|leading|lead the|co-led|secondary|round of|raises|raised|invest(?:ed|s|ing)? in|backed|backing|acquired|acquisition|IPO|exit)\b", s, re.I) and (mentions(s, names, False) or True):
            out.append(s[:320])
        if len(out) >= 6:
            break
    return out

pack = {}
for row in base:
    slug = row["slug"]; names = name_variants(row); lname = loose(row["name"])
    rel_stories, text_stories = [], []
    for a in stories:
        rel = {loose(c.get("title")) for c in a.get("related_companies", [])}
        if lname in rel or any(loose(n) in rel for n in names):
            rel_stories.append(a)
        elif a["text"] and mentions(a["title"] or "", names, True):
            text_stories.append(a)
        elif a["text"] and len(row["name"]) > 5 and slug not in SHORT and mentions(a["text"], names, True):
            text_stories.append(a)
    ann_hits = [x for x in ann if x.get("text") and mentions((x.get("h1") or "") + " " + (x.get("title") or "") + " " + x["text"], names, True)]
    wiki_hits = [w for w in wiki if loose(w["title"]) == lname or w.get("in_base") == slug]
    s = site.get(slug, {})
    a = None
    for al in aliases.get(slug, [slug]):
        a = a or arch.get(al) or next((v for k, v in arch.items() if loose(v["name"]) == loose(al.replace("-", " "))), None)
    a = a or arch.get(slug)
    pack[slug] = {
        "name": row["name"], "tier": row["tier"], "first_seen": row["first_seen"],
        "wayback_years": row["wayback_years"], "partners_site": row["partners_site"], "partners_formd": row["partners_formd"],
        "site": {k: s.get(k) for k in ("invest_year", "exited", "state", "sectors", "partners", "url", "foundedDate", "founderName", "lists")} if s else None,
        "archive_2017_2023": {k: a.get(k) for k in ("invest_year", "status_site", "type", "partners", "url", "founded", "years_listed", "story")} if a else None,
        "stories": [{"date": x["date"], "title": x["title"], "url": x["url"], "related": [c.get("title") for c in x.get("related_companies", [])], "snips": round_snips(x["text"], names)} for x in (rel_stories + text_stories)[:8]],
        "announcements": [{"year": x.get("year"), "title": (x.get("h1") or x.get("title") or "")[:120], "url": x.get("archive_url"), "snips": round_snips(x["text"], names)} for x in ann_hits[:6]],
        "wikipedia": [{"title": w["title"], "url": w["url"], "sentences": w["sentences"]} for w in wiki_hits],
        "formd_rounds": [{"q": r.get("quarter"), "usd": r.get("offering_usd"), "sale": r.get("sale_date")} for r in rounds.get(slug, {}).get("rounds", [])],
    }
(I / "scratch/evidence-pack.json").write_text(json.dumps(pack, indent=1, ensure_ascii=False))
n_st = sum(1 for v in pack.values() if v["stories"]); n_an = sum(1 for v in pack.values() if v["announcements"]); n_w = sum(1 for v in pack.values() if v["wikipedia"])
print(f"pack: {len(pack)} rows; with stories {n_st}, announcements {n_an}, wikipedia {n_w}, form d {sum(1 for v in pack.values() if v['formd_rounds'])}")

def render(slug, p=None):
    p = p or pack[slug]
    L = [f"### {slug} | {p['name']} | tier {p['tier']} | first_seen {p['first_seen']} | wb {p['wayback_years'][:60]} | partners {p['partners_site'] or p['partners_formd']}"]
    if p["site"]: L.append(f"  site: {json.dumps(p['site'], ensure_ascii=False)}")
    if p["archive_2017_2023"]: L.append(f"  2017-23: {json.dumps({k: v for k, v in p['archive_2017_2023'].items() if k != 'story'}, ensure_ascii=False)} | {p['archive_2017_2023'].get('story', '')[:160]}")
    for x in p["stories"]:
        L.append(f"  story {x['date']} {x['title'][:70]} rel={x['related']} {x['url']}")
        for sn in x["snips"][:4]: L.append(f"     - {sn}")
    for x in p["announcements"]:
        L.append(f"  news {x['year']} {x['title'][:80]} {x['url']}")
        for sn in x["snips"][:3]: L.append(f"     - {sn}")
    for w in p["wikipedia"]:
        L.append(f"  wiki {w['title']} {w['url']}")
        for sn in w["sentences"][:3]: L.append(f"     - {sn[:300]}")
    if p["formd_rounds"]: L.append(f"  formd: {p['formd_rounds']}")
    return "\n".join(L)

if __name__ == "__main__" and len(sys.argv) > 1:
    for s in sys.argv[1:]:
        print(render(s)); print()
