#!/usr/bin/env python3
"""Recall probe candidates (COLLECTION.md s3): companies an independent source ties to
Speedinvest that the base does not hold.

Sources: the Google News sweep (scratch/recall-news.json, headlines naming
Speedinvest), the register's named holdings of Speedinvest vehicles
(sources/registers/nd-vehicles.json), the firm's own posts (company names in
"our investment in X" titles), the Internet Archive's 2012-2016 listings once
parsed (sources/wayback/parsed/<year>.json rows not in the base), and the
acquired companies behind the sale-consideration rows.

Writes scratch/recall-candidates.json: [{name, source, evidence}], base rows removed.
"""
import html
import json
import re
from pathlib import Path

H = Path(__file__).resolve().parent
INV = H.parent


def k(s):
    s = html.unescape(s or "").lower()
    s = re.sub(r"\b(gmbh|ag|se|ltd|limited|inc|sas|bv|oü|ou|s\.r\.o|kft|holding|technologies|technology|group)\b\.?", "", s)
    return re.sub(r"[^a-z0-9]", "", s)


base = json.loads((INV / "companies/base.json").read_text())
known = {k(r["name"]) for r in base} | {k(r["slug"]) for r in base}
ev = json.loads((INV / "sources/wayback/archive-evidence.json").read_text())["companies"]
for s, v in ev.items():
    for n in v["names"]:
        known.add(k(n))
cands = {}


def add(name, source, evidence):
    kk = k(name)
    if not kk or kk in known or len(kk) < 3:
        return
    c = cands.setdefault(kk, {"name": name, "sources": [], "evidence": []})
    if source not in c["sources"]:
        c["sources"].append(source)
    if evidence not in c["evidence"] and len(c["evidence"]) < 4:
        c["evidence"].append(evidence)


# 1. Google News headlines naming Speedinvest
rn = H / "recall-news.json"
if rn.exists():
    for title, v in json.loads(rn.read_text()).items():
        t = title.rsplit(" - ", 1)[0]
        m = (re.match(r"^([A-Z][\w.&'’ -]{1,40}?)\s+(?:raises|secures|closes|lands|bags|gets|nets|announces|completes|sammelt|erhält|holt|lève|boucle)\b", t)
             or re.search(r"(?:invests? in|backs|leads [^ ]+ (?:round|investment) in|investment in)\s+([A-Z][\w.&'’-]+(?: [A-Z][\w.&'’-]+)?)", t))
        if m:
            add(m.group(1).strip(), "googlenews", f"{v.get('date')} | {title[:160]}")
# 2. Register-named holdings of Speedinvest vehicles
nv = INV / "sources/registers/nd-vehicles.json"
if nv.exists():
    for veh, v in json.loads(nv.read_text()).items():
        for n in v.get("named_holdings") or []:
            for x in re.split(r",\s*(?=[A-Z])", n):
                x = x.strip()
                if x and not x.startswith("GmbH"):
                    add(x, "register", f"{veh.split(',')[0].strip('/')} ({v['url']})")
# 3. The firm's own posts: "Our investment in X", "Why we invested in X", "welcome X"
pa = INV / "sources/site/press-archive.json"
if pa.exists():
    for key, p in json.loads(pa.read_text())["posts"].items():
        for m in re.finditer(r"(?:[Oo]ur [Ii]nvestment in|[Ww]hy [Ww]e [Ii]nvested in|[Ww]e [Ii]nvested in|[Ii]nvesting in|[Ww]elcome)\s+([A-Z][\w.&'’-]+(?: [A-Z][\w.&'’-]+)?)", p.get("title") or ""):
            add(m.group(1), "firm_post", f"{p.get('date')} | {p.get('title')} | {p.get('capture_url')}")
# 4. Archive rows not in the base (e.g. Internet Archive 2012-2016 once parsed)
for f in sorted((INV / "sources/wayback/parsed").glob("*.json")):
    for r in json.loads(f.read_text()):
        add(r.get("name") or r["slug"], f"archive-{f.stem}", r.get("capture_url") or "")
out = sorted(cands.values(), key=lambda c: (-len(c["sources"]), c["name"].lower()))
(H / "recall-candidates.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
print(len(out), "candidates")
for c in out[:80]:
    print(f"  {c['name'][:40]:40} {','.join(c['sources']):30} {c['evidence'][0][:110]}")
