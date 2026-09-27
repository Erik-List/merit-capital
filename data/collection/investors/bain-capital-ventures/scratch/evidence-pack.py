#!/usr/bin/env python3
"""One evidence view per base row for the judge (the EQT / Balderton pattern):
the live CMS row (the firm's year of investment, stage tag, outcome tag, deal
partners, HQ, founded), the archive rows by year (2002 to 2023 listings, with
the old sites' outcome lines "Acquired" / "IPO 02/20/98" and locations), the
firm's own posts naming the company (scratch/insights-pack.json), the EDGAR
full-text and Wikipedia sentences, and what sibling books hold
(scratch/siblings.json). Output: scratch/evidence-pack.json keyed by slug.
"""
import glob, json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402
P = Paths("bain-capital-ventures")
SUF = r"\b(inc|ltd|limited|llc|corp|corporation|co|group|holdings|technologies|technology|labs|the|software|systems|networks|com)\b\.?"


def norm(s):
    s = re.sub(r"\(.*?\)", " ", (s or "").lower().replace("&", "and"))
    return re.sub(r"[^a-z0-9]+", "", re.sub(SUF, "", s))


base = json.loads(P.base_json.read_text())
site = {}
for r in json.loads((P.site / "company-pages.json").read_text())["rows"]:
    site[r["slug"]] = r
    site.setdefault(norm(r["name"]), r)
crypto = {r["slug"]: r for r in json.loads((P.site / "crypto-portfolio.json").read_text())["rows"]}
arch = {}
for f in sorted(glob.glob(str(P.wayback / "parsed" / "*.json"))):
    y = Path(f).stem
    for r in json.loads(Path(f).read_text()):
        for k in {r["slug"], norm(r.get("name") or r["slug"].replace("-", " "))}:
            arch.setdefault(k, []).append({"year": y, **{x: r[x] for x in r if x not in ("slug",)}})
posts = json.loads((HERE / "insights-pack.json").read_text()) if (HERE / "insights-pack.json").exists() else {}
fts = json.loads((P.edgar / "fts-hits.json").read_text())["registrants"]
wiki = json.loads((P.web / "wikipedia-insource.json").read_text())
warts = wiki.get("articles") or wiki.get("rows") or []
sib = json.loads((HERE / "siblings.json").read_text()) if (HERE / "siblings.json").exists() else {}
merges = {}
if P.identity_merges.exists():
    im = json.loads(P.identity_merges.read_text()).get(P.slug, {})
    for m in im.get("merges", []):
        for s in m.get("slugs", [])[1:] if isinstance(m.get("slugs"), list) else []:
            merges.setdefault(m["slugs"][0], []).append(s)

pack = {}
for row in base:
    s = row["slug"]
    keys = {s, norm(row["name"])} | set(merges.get(s, []))
    for alias in (row.get("aliases") or []):
        keys.add(norm(alias))
    e = {}
    sr = site.get(s) or site.get(norm(row["name"]))
    if sr:
        e["site"] = {k: sr.get(k) for k in ("name", "invest_year", "site_stage", "site_outcome", "partners",
                                             "location", "founded", "company_site", "about", "popover")}
    if s in crypto:
        e["crypto_site"] = {k: crypto[s].get(k) for k in ("name", "published", "content")}
    a = []
    for k in keys:
        a += arch.get(k, [])
    if a:
        seen = set()
        yrs = sorted({x["year"] for x in a})
        info = {}
        for x in a:
            for k in ("name", "outcome", "location", "website", "era", "stage_bucket", "stage_wp", "site_status",
                      "partners", "worked_with", "founded"):
                if x.get(k) and k not in info:
                    info[k] = x[k]
        e["archive"] = {"years": yrs, "first": min(yrs), "last": max(yrs), **info,
                        "first_capture": min((x.get("snapshot_ts") or "") for x in a),
                        "paths": sorted({x.get("path") for x in a if x.get("path")})[:3]}
    if s in posts:
        e["posts"] = posts[s]
    nm = norm(row["name"])
    f = [{"registrant": r["registrant"], "forms": list(r["forms"])[:6], "first": r["first_date"],
          "snippets": [f"{sn.get('form')} {sn.get('date')}: " + re.sub(r"\s+", " ", " | ".join(sn.get("context") or []))[:500]
                       for sn in (r.get("snippets") or [])[:2] if isinstance(sn, dict)]}
         for r in fts if r["bucket"] == "third_party" and nm and len(nm) > 3 and nm in norm(r["registrant"])]
    if f:
        e["edgar_fulltext"] = f
    w = []
    for x in warts:
        t = x.get("title") or x.get("article") or ""
        if nm and len(nm) > 3 and nm in norm(t):
            w.append({"article": t, "url": x.get("url"), "sentences": (x.get("sentences") or [])[:3]})
    if w:
        e["wikipedia"] = w
    if s in sib:
        e["siblings"] = sib[s]
    pack[s] = e
write_atomic(HERE / "evidence-pack.json", json.dumps(pack, indent=1, ensure_ascii=False) + "\n")
print(f"{len(pack)} rows; site {sum('site' in v for v in pack.values())}, archive {sum('archive' in v for v in pack.values())}, "
      f"posts {sum('posts' in v for v in pack.values())}, fts {sum('edgar_fulltext' in v for v in pack.values())}, "
      f"wiki {sum('wikipedia' in v for v in pack.values())}, siblings {sum('siblings' in v for v in pack.values())}")
