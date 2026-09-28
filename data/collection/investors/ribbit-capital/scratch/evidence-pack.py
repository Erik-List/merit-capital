#!/usr/bin/env python3
"""One evidence view per base row for the judge (the BCV / EQT pattern), adapted
for Ribbit: the live Rebels row (founders, the firm's link to the company), the
archived listing rows by year (era, the firm's own country label, its link, the
2012-2014 one-line description), the firm's deal vehicles decoded to this
company (sources/registers/spv-decode.json), the adviser's 13F lines, the EDGAR
full-text and Wikipedia sentences, and what sibling books hold
(scratch/siblings.json). Output: scratch/evidence-pack.json keyed by slug.
"""
import glob
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

P = Paths("ribbit-capital")
SUF = r"\b(inc|ltd|limited|llc|corp|corporation|co|group|holdings|technologies|technology|labs|the|com)\b\.?"


def norm(s):
    s = re.sub(r"\(.*?\)", " ", (s or "").lower().replace("&", "and"))
    return re.sub(r"[^a-z0-9]+", "", re.sub(SUF, "", s))


base = json.loads(P.base_json.read_text())
site = {}
for r in json.loads((P.site / "rebels.json").read_text())["rows"]:
    site[r["slug"]] = r
    site.setdefault(norm(r["name"]), r)
arch = {}
for f in sorted(glob.glob(str(P.wayback / "parsed" / "*.json"))):
    y = Path(f).stem
    for r in json.loads(Path(f).read_text()):
        for k in {r["slug"], norm(r.get("name") or r["slug"].replace("-", " "))}:
            arch.setdefault(k, []).append({"year": y, **{x: r[x] for x in r if x != "slug"}})
merges = {}
if P.identity_merges.exists():
    for m in json.loads(P.identity_merges.read_text()).get(P.slug, {}).get("merges", []):
        merges.setdefault(m["canonical"], []).extend(m["duplicates"])
spv = json.loads((P.root / "sources/registers/spv-decode.json").read_text())["vehicles"]
f13 = json.loads((P.edgar / "13f-holdings.json").read_text())["issuers"] if (P.edgar / "13f-holdings.json").exists() else {}
fts = json.loads((P.edgar / "fts-hits.json").read_text())["registrants"]
wiki = json.loads((P.web / "wikipedia-insource.json").read_text())
warts = wiki.get("articles") or wiki.get("rows") or []
sib = json.loads((HERE / "siblings.json").read_text()) if (HERE / "siblings.json").exists() else {}

pack = {}
for row in base:
    s = row["slug"]
    keys = {s, norm(row["name"])} | set(merges.get(s, []))
    e = {}
    sr = site.get(s) or site.get(norm(row["name"]))
    if sr:
        e["site"] = {"name": sr["name"], "founders": sr.get("founders"), "company_url": sr.get("company_url")}
    a = []
    for k in keys:
        a += arch.get(k, [])
    if a:
        yrs = sorted({x["year"] for x in a})
        info = {}
        for x in sorted(a, key=lambda x: x["year"]):
            for k in ("name", "company_url", "country_label", "about", "era"):
                if x.get(k) and k not in info:
                    info[k] = x[k]
        e["archive"] = {"years": yrs, **info,
                        "first_capture": min((x.get("snapshot_ts") or "") for x in a)}
    v = [x for x in spv if x.get("company") == s]
    if v:
        e["spv"] = [{"code": x["code"], "vehicle": x["vehicle"], "quarter": x.get("quarter"),
                     "sold": x.get("total_sold"), "round_as_coded": x.get("round_as_coded"),
                     "decode": x["decode"]} for x in v]
    nm = norm(row["name"])
    t13 = [dict(name=v["name"], first=v["first_period"], last=v["last_period"], max_usd=v["max_value_usd"])
           for k, v in f13.items() if nm and len(nm) > 3 and nm in norm(v["name"])]
    if t13:
        e["13f"] = t13
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
      f"spv {sum('spv' in v for v in pack.values())}, 13f {sum('13f' in v for v in pack.values())}, "
      f"fts {sum('edgar_fulltext' in v for v in pack.values())}, wiki {sum('wikipedia' in v for v in pack.values())}, "
      f"siblings {sum('siblings' in v for v in pack.values())}")
