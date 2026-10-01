#!/usr/bin/env python3
"""One evidence view per base row for the grind (adapted from the Northzone run):
  site     the live company page (Index Team, sector, backed-at-Seed mark, ticker or
           acquirer tag, founders, website, description, regions)
  archive  the firm's own archived claims (sources/wayback/archive-facts.json): desk
           (tech / life), status, the 2012-13 stage filter, Index Team, sectors, HQ,
           born-in, tags, the name's ticker-or-acquirer tag, each with its capture
  posts    every Perspectives post that links the company page or names the company
           in its title (date, title, round sentences)
  news     the archived news items (2008-2019 site) naming the company
  formd    partners on the Form D sweep and the issuer's filings
  fts      full-text sweep registrants that name the company
Output scratch/evidence-pack.json keyed by base slug. Citations are read from here
by key, never typed (Balderton's lesson)."""
import json, re
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def loose(s):
    s = re.sub(r"\(.*?\)", "", s or "")
    return re.sub(r"[^a-z0-9]+", "", re.sub(r"\b(inc|ltd|ab|as|gmbh|limited|corp|corporation|llc|bv|oy|aps|sa|se|plc|pbc|co)\b\.?", "", s.lower()))


def slug_of(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


base = json.load(open(ROOT / "companies" / "base.json"))
site = {r["url"]: r for r in json.load(open(ROOT / "sources" / "site" / "companies-wagtail.json"))["rows"]}
facts = json.load(open(ROOT / "sources" / "wayback" / "archive-facts.json"))
facts_all = {}
for era, d in facts.items():
    for k, v in d.items():
        facts_all.setdefault(k, {}).update({f"{f}": v[f] for f in v})
posts = json.load(open(ROOT / "sources" / "site" / "perspectives.json"))["rows"]
news_p = ROOT / "sources" / "wayback" / "news-archive.json"
news = json.load(open(news_p))["rows"] if news_p.exists() else []
fts = json.load(open(ROOT / "sources" / "edgar" / "fts-hits.json"))["registrants"]
merges_p = ROOT / "companies" / "identity-merges.json"
dups = {}
if merges_p.exists():
    for m in json.load(open(merges_p)).get("index-ventures", {}).get("merges", []):
        dups.setdefault(m["canonical"], []).extend(m["duplicates"])

out = {}
for r in base:
    s = site.get(r.get("site_url") or "")
    page_slug = (r.get("site_url") or "").rstrip("/").rsplit("/", 1)[-1]
    k = loose(r["name"])
    keys = {r["slug"], slug_of(r["name"])} | set(dups.get(r["slug"], []))
    alts = {r["name"]} | {kk.replace("-inc", "").replace("-", " ") for kk in dups.get(r["slug"], [])}
    NAME = re.compile(r"(?<![A-Za-z0-9])(" + "|".join(re.escape(re.sub(r"\s*\(.*?\)|,? Inc\.?$|\.com$", "", a).strip()) for a in alts if len(a) >= 2) + r")(?![A-Za-z0-9])", re.I)
    arch = {}
    for kk in keys:
        for f, vals in (facts_all.get(kk) or {}).items():
            arch.setdefault(f, [])
            for v in vals:
                if v not in arch[f]:
                    arch[f].append(v)
    ps = []
    for p in posts:
        if p.get("missing"):
            continue
        t = p.get("title") or ""
        in_title = bool(NAME.search(t))
        linked = bool(page_slug and page_slug in (p.get("companies") or []))
        if in_title or linked:
            ss = p.get("round_sentences") or []
            named = [x for x in ss if NAME.search(x)]
            ps.append({"url": p["url"], "date": p.get("date"), "title": t, "kind": p.get("kind"), "author": p.get("author"),
                       "in_title": in_title, "sents": (named + ([x for x in ss if x not in named] if in_title else []))[:6]})
    ns = [n for n in news if NAME.search(n.get("title") or "")]
    out[r["slug"]] = {
        "name": r["name"], "tier": r.get("tier"), "first_seen": r.get("first_seen"),
        "site": ({k2: s.get(k2) for k2 in ("url", "partners", "sectors_page", "backed", "regions", "list_tag", "founders",
                                           "website", "description")} if s else None),
        "archive": arch or None,
        "partners_formd": r.get("partners_formd"), "formd_links": r.get("formd_links"),
        "posts": sorted(ps, key=lambda x: (not x["in_title"] and not x["sents"], x["date"] or "9999")),
        "news": sorted(ns, key=lambda x: x.get("date") or "9999")[:12],
        "fts": [{"registrant": f["registrant"], "forms": f["forms"], "first": f["first_date"],
                 "url": f["filings"][0]["url"]} for f in fts if k and len(k) >= 4 and k in loose(f["registrant"])],
    }
(HERE / "evidence-pack.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
print(len(out), "rows;", sum(1 for v in out.values() if v["posts"]), "with posts;", sum(1 for v in out.values() if v["archive"]),
      "with archive facts;", sum(1 for v in out.values() if v["news"]), "with archived news")
