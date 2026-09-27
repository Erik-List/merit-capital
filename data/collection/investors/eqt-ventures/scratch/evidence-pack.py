#!/usr/bin/env python3
"""One evidence view per base row for the judge (the Balderton / Atomico
pattern): the eqtgroup.com Key Facts, the eqtventures.com archive rows (years,
the firm's own announcement or closing dates, exit status), the firm's
announcement posts (stories 2016-2026 and the 2017-2020 articles, the
sentences naming the company), the EDGAR full-text and Wikipedia sentences,
and what sibling books hold. Output: scratch/evidence-pack.json keyed by slug.
"""
import glob, json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402
P = Paths("eqt-ventures")
SUF = r"\b(inc|ltd|limited|gmbh|ab|oy|sa|sas|bv|plc|llc|corp|corporation|co|group|holdings|technologies|technology|labs|the|as|aps)\b\.?"
def norm(s): return re.sub(r"[^a-z0-9]+", "", re.sub(SUF, "", (s or "").lower().replace("&", "and")))
base = json.loads(P.base_json.read_text())
site = {norm(r["name"]): r for r in json.loads((P.site / "companies-eqtgroup.json").read_text())["rows"]}
arch = {}
for f in sorted(glob.glob(str(P.wayback / "parsed" / "*.json"))):
    for r in json.loads(Path(f).read_text()):
        arch.setdefault(r["slug"], []).append(r)
stories = json.loads((P.site / "stories-index.json").read_text())["posts"]
arts = json.loads((P.site / "articles-2017-2020.json").read_text())["rows"]
fts = json.loads((P.edgar / "fts-hits.json").read_text())["registrants"]
wiki = json.loads((P.web / "wikipedia-insource.json").read_text())
warts = wiki.get("articles") or wiki.get("rows") or []
sib = json.loads((HERE / "siblings.json").read_text()) if (HERE / "siblings.json").exists() else {}
merges = json.loads(P.identity_merges.read_text())["eqt-ventures"]["merges"]
alias = {}
for m in merges:
    for d in m["duplicates"]:
        alias.setdefault(m["canonical"], []).append(d)
pack = {}
for row in base:
    s, n = row["slug"], row["name"]
    keys = {norm(n)} | {norm(a.replace("-", " ")) for a in alias.get(s, [])}
    names = {n} | {a.replace("-", " ") for a in alias.get(s, [])}
    v = {}
    for k in keys:
        if k in site:
            c = site[k]; v["site"] = {f: c.get(f) for f in ("desk", "funds", "invest_year", "exit_year", "status_site",
                     "country_site", "sectors", "website", "tagline", "description")}
    ar = []
    for sl in [s] + alias.get(s, []):
        for r in arch.get(sl, []):
            ar.append({f: r.get(f) for f in ("path", "snapshot_ts", "kind", "announced", "announced_text", "closing_date",
                       "geography", "industry", "status_site", "stage_site", "website", "description", "capture_url")})
    if not ar:
        for sl, rs in arch.items():
            if norm(sl.replace("-", " ")) in keys:
                ar += [{f: r.get(f) for f in ("path", "snapshot_ts", "kind", "announced", "closing_date", "geography",
                        "industry", "status_site", "stage_site", "website", "description", "capture_url")} for r in rs]
    if ar:
        dates = sorted({a["announced"] for a in ar if a.get("announced")})
        v["archive"] = {"years": sorted({a["snapshot_ts"][:4] for a in ar}), "announced_dates": dates,
                        "closing_dated": any(a.get("closing_date") for a in ar),
                        "exit_flag": any((a.get("status_site") or "") == "exit" for a in ar),
                        "geography": sorted({a["geography"] for a in ar if a.get("geography")}),
                        "industry": sorted({a["industry"] for a in ar if a.get("industry")}),
                        "stage_card": sorted({a["stage_site"] for a in ar if a.get("stage_site")}),
                        "description": next((a["description"] for a in ar if a.get("description")), None),
                        "website": next((a["website"] for a in ar if a.get("website")), None),
                        "first_capture": min(ar, key=lambda a: a["snapshot_ts"])["capture_url"]}
    ps = []
    for p in stories:
        for nm, h in p["companies"].items():
            if norm(nm) in keys:
                ps.append({"date": p["date"], "title": p["title"], "url": p["url"], "fund_voice": p["fund_voice"],
                           "in_title": h["in_title"], "round_words": h["round_words"], "amounts": h["amounts"],
                           "sentences": [x[:400] for x in h["sentences"][:4]]})
    for a in arts:
        hits = [x.strip() for x in re.split(r"(?<=[.!?])\s+|\n", a["text"])
                if any(re.search(r"(?<![A-Za-z0-9])" + re.escape(nm) + r"(?![A-Za-z0-9])", x, re.I) for nm in names)]
        if hits:
            ps.append({"date": a["date_text"], "title": a["title"], "url": a["capture_url"], "fund_voice": "ventures",
                       "in_title": any(nm.lower() in a["title"].lower() for nm in names), "old_site": a["url"],
                       "sentences": [x[:400] for x in hits if re.search(r"(?i)round|series|seed|led|invest|rais|million|€|\$", x)][:4]})
    if ps:
        v["posts"] = sorted(ps, key=lambda x: x["date"] or "")
    fh = []
    for r in fts:
        for sn in r.get("snippets", []):
            for ctx in sn.get("context", []):
                if any(re.search(r"(?<![A-Za-z0-9])" + re.escape(nm) + r"(?![A-Za-z0-9])", ctx, re.I) for nm in names):
                    fh.append({"registrant": r["registrant"], "form": sn["form"], "date": sn["date"], "url": sn["url"], "context": ctx[:500]})
    if fh:
        v["edgar_fulltext"] = fh[:6]
    wh = []
    for a in warts:
        t = a.get("title") or a.get("article") or ""
        sents = a.get("sentences") or a.get("snippets") or []
        if norm(t.split(" (")[0]) in keys or any(any(nm.lower() in str(x).lower() for nm in names) for x in sents):
            wh.append({"article": t, "url": a.get("url"), "sentences": [str(x)[:400] for x in sents][:4]})
    if wh:
        v["wikipedia"] = wh
    if s in sib:
        v["siblings"] = sib[s]
    pack[s] = v
write_atomic(HERE / "evidence-pack.json", json.dumps(pack, indent=1, ensure_ascii=False))
print(len(pack), "rows;", sum(1 for x in pack.values() if "posts" in x), "with posts;",
      sum(1 for x in pack.values() if "siblings" in x), "with siblings;", sum(1 for x in pack.values() if not x), "empty")
