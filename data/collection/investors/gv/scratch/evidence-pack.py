#!/usr/bin/env python3
"""One evidence view per base row for the judge (the BCV / EQT pattern), GV edition:
  site       the live CMS row: sector, website, the deal partners the firm names, its own exit line ("Acquired
             by Nebius, 2026", "NASDAQ: ME"), and on /ai companies the firm's own dated rounds
  archive    the archived listings by year (2012-2026 on googleventures.com and gv.com, Common Crawl), with the
             description, the exit line and the deal partner each era printed
  people     the 2012-13 people pages' own company lists (which partner listed the company)
  posts      the firm's own posts naming the company (gv.com/news), with the sentences that name it
  cases      the firm's case study, where one exists
  gv_filings the GV vehicles' own 13D/G and Forms 3/4 on the company (edgar-companies)
  fts        EDGAR full-text hits whose registrant is the company (S-1 holder tables, IRA signatories)
  wikipedia  the insource sweep's sentences
  siblings   what other books hold for the same company (scratch/siblings.json)
Output: scratch/evidence-pack.json keyed by base slug.
"""
import glob
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

P = Paths("gv")
SUF = r"\b(inc|ltd|limited|llc|corp|corporation|co|group|holdings|technologies|technology|labs|the|software|systems|networks|com|therapeutics|bio|biosciences|health)\b\.?"


def norm(s):
    s = re.sub(r"\(.*?\)", " ", (s or "").lower().replace("&", "and").replace("ö", "o").replace("é", "e"))
    return re.sub(r"[^a-z0-9]+", "", re.sub(SUF, "", s))


def sentences_naming(text, name):
    if not name or len(name) < 3:
        return []
    out = []
    for s in re.split(r"(?<=[.!?])\s+|\n+", text or ""):
        if re.search(r"(?<![A-Za-z])" + re.escape(name) + r"(?![A-Za-z])", s):
            out.append(s.strip()[:400])
    return out[:4]


base = json.loads(P.base_json.read_text())
merges = {}
if P.identity_merges.exists():
    for m in json.loads(P.identity_merges.read_text()).get("gv", {}).get("merges", []):
        merges[m["canonical"]] = m.get("duplicates") or []
site = {}
for r in json.loads((P.site / "company-list.json").read_text())["rows"]:
    site[norm(r["name"])] = r
arch = {}
for f in sorted(glob.glob(str(P.wayback / "parsed" / "*.json"))):
    y = Path(f).stem
    for r in json.loads(Path(f).read_text()):
        for k in {r["slug"], norm(r.get("name") or "")}:
            arch.setdefault(k, []).append({"year": y, **{x: r.get(x) for x in ("name", "era", "website", "about", "exit",
                                                                                 "partners", "tags", "capture_url")}})
people = {}
cc = json.loads((HERE / "roster-cc.json").read_text()) if (HERE / "roster-cc.json").exists() else {}
for s, p in cc.items():
    for y, comps in p.get("companies", {}).items():
        for c in comps:
            people.setdefault(norm(c), []).append(f"{(p['names'] or [s])[0]} ({p['titles'].get(y, '')}, {y} page)")
posts = json.loads((P.site / "news-text.json").read_text())["rows"]
cases = json.loads((P.site / "sanity" / "caseStudy.json").read_text())["rows"]
gvf = {norm(c["name"]): c for c in json.loads((P.edgar / "edgar-companies.json").read_text())}
fts = json.loads((P.edgar / "fts-hits.json").read_text())["registrants"]
wf = P.web / "wikipedia-insource.json"
warts = (json.loads(wf.read_text()).get("articles") or json.loads(wf.read_text()).get("rows") or []) if wf.exists() else []
sib = json.loads((HERE / "siblings.json").read_text()) if (HERE / "siblings.json").exists() else {}

pack = {}
for row in base:
    s = row["slug"]
    keys = {s, norm(row["name"])} | set(merges.get(s, [])) | {norm(d.replace("-", " ")) for d in merges.get(s, [])}
    e = {}
    sr = next((site[k] for k in keys if k in site), None)
    if sr:
        e["site"] = {k: sr.get(k) for k in ("name", "gv_lists", "sector", "secondary_sector", "company_site", "partners",
                                             "exited", "exit_line", "more_info", "ai_category", "ai_first_invested",
                                             "ai_rounds") if sr.get(k) not in (None, "", [], False)}
    a = [x for k in keys for x in arch.get(k, [])]
    if a:
        yrs = sorted({x["year"] for x in a})
        info = {"years": yrs, "first": yrs[0], "last": yrs[-1]}
        for k in ("name", "website", "about", "exit"):
            v = next((x[k] for x in sorted(a, key=lambda x: x["year"]) if x.get(k)), "")
            if v:
                info[k] = v
        partners = {}
        for x in a:
            for p in x.get("partners") or []:
                partners.setdefault(p, []).append(x["year"])
        if partners:
            info["partners_by_year"] = {p: f"{min(v)}-{max(v)}" for p, v in partners.items()}
        info["first_capture"] = min(a, key=lambda x: x["year"]).get("capture_url")
        e["archive"] = info
    pp = [x for k in keys for x in people.get(k, [])]
    if pp:
        e["people_pages"] = sorted(set(pp))
    nm = (sr or {}).get("name") or row["name"]
    ps = []
    for p in posts:
        sn = sentences_naming(p["title"] + ". " + p.get("subheading", "") + ". " + p["body"], nm)
        if sn:
            ps.append({"date": p["date"], "title": p["title"], "url": p["url"], "sentences": sn})
    if ps:
        e["posts"] = ps[:6]
    cs = [c for c in cases if norm(c.get("title") or "") in keys]
    if cs:
        e["case_study"] = [f"https://www.gv.com/case-study/{c['slug']['current']}" for c in cs]
    g = next((gvf[k] for k in keys if k in gvf), None)
    if g:
        e["gv_filings"] = {"name": g["name"], "forms": sorted(set(g.get("forms", []))), "first": g.get("first"),
                           "last": g.get("last"), "cik": g.get("cik")}
    n = norm(nm)
    f = [{"registrant": r["registrant"], "forms": list(r["forms"])[:6], "first": r["first_date"],
          "snippets": [f"{sn.get('form')} {sn.get('date')}: " + re.sub(r"\s+", " ", " | ".join(sn.get("context") or []))[:500]
                       for sn in (r.get("snippets") or [])[:2] if isinstance(sn, dict)]}
         for r in fts if r["bucket"] == "third_party" and n and len(n) > 3 and n == norm(r["registrant"])[:len(n)]]
    if f:
        e["edgar_fulltext"] = f
    w = []
    for x in warts:
        t = x.get("title") or x.get("article") or ""
        if n and len(n) > 3 and n == norm(t):
            w.append({"article": t, "url": x.get("url"), "sentences": (x.get("sentences") or [])[:3]})
    if w:
        e["wikipedia"] = w
    if s in sib:
        e["siblings"] = sib[s]
    pack[s] = e
write_atomic(HERE / "evidence-pack.json", json.dumps(pack, indent=1, ensure_ascii=False) + "\n")
print(f"{len(pack)} rows; site {sum('site' in v for v in pack.values())}, archive {sum('archive' in v for v in pack.values())}, "
      f"people {sum('people_pages' in v for v in pack.values())}, posts {sum('posts' in v for v in pack.values())}, "
      f"cases {sum('case_study' in v for v in pack.values())}, gv_filings {sum('gv_filings' in v for v in pack.values())}, "
      f"fts {sum('edgar_fulltext' in v for v in pack.values())}, wiki {sum('wikipedia' in v for v in pack.values())}, "
      f"siblings {sum('siblings' in v for v in pack.values())}")
