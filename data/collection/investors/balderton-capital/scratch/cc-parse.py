#!/usr/bin/env python3
"""Parse the archived balderton.com listing pages (Common Crawl captures under
data/filings/commoncrawl/balderton-capital/) into sources/wayback/parsed/<year>.json, in the shape
wayback-pull.py writes (slug, name, path, snapshot_ts, capture_url) plus what
each era's card states: description, status, location, sector, partners, the
round label and its year. Year files MERGE, keyed slug+path (COLLECTION.md s5).

Four markups:
  2013        /portfolio     <li class="sortable ..."><a href="/portfolio/<slug>" title="<text>"><img alt="<Name>">
  2015-2017   /portfolio     <a href="<site>" name="<Name>" class="... portfolio-item-contain" data-status data-location data-section> ... <span class="listname">
  2018        /investments/  <div class="box live <region>"> <h3>Name</h3> ... STATUS / FOUNDED / PARTNERS
  2019-2023   /companies/    <div class="box <region> live|exited"> <h3>Name</h3> ... investment-location / -text / -dates
A page that returned bytes and parses to zero rows is reported as a FAILED
pattern, never written as an empty year.
"""
import html, json, re, sys
from collections import defaultdict
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402
# Raw captures are re-downloadable from Common Crawl: they live under data/filings/ (gitignored);
# the manifest with each capture's URL and digest is tracked as sources/wayback/cc-manifest.json.
RAW = HERE.parents[4] / "data" / "filings" / "commoncrawl" / "balderton-capital"
PARSED = HERE.parent / "sources" / "wayback" / "parsed"
man = json.loads((HERE.parent / "sources" / "wayback" / "cc-manifest.json").read_text())

def slug_of(name): return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
def clean(s): return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()

def era_2013(t):
    out = []
    for m in re.finditer(r'<li class="\s*sortable([^"]*)">\s*<a href="(/portfolio/[^"]+)"(?: title="([^"]*)")?[^>]*>\s*<img[^>]*alt="([^"]*)"', t):
        out.append({"name": clean(m.group(4)), "site_slug": m.group(2).split("/")[-1], "description": clean(m.group(3)),
                    "classes": " ".join(m.group(1).split())})
    return out

def era_2015(t):
    out = []
    for m in re.finditer(r'<a href="\s*([^"]*?)\s*"[^>]*?name="([^"]*)"\s*class="[^"]*portfolio-item-contain[^"]*"\s*data-status="([^"]*)"\s*data-location="([^"]*)"\s*data-section="([^"]*)"\s*>((?:(?!</a>).)*)</a>', t, re.S):
        body = m.group(6)
        ln = re.search(r'class="listname">([^<]*)<', body)
        cap = re.search(r'class="caption">((?:(?!</div>).)*)</div>', body, re.S)
        out.append({"name": clean(ln.group(1)) if ln and clean(ln.group(1)) else clean(m.group(2)), "website": m.group(1).strip(),
                    "status_site": clean(m.group(3)), "location": clean(m.group(4)), "sector": clean(m.group(5)),
                    "description": clean(cap.group(1)) if cap else ""})
    return out

def era_2018(t):
    out = []
    for m in re.finditer(r'<div class="box ([^"]*)">((?:(?!<div class="box ).)*)', t, re.S):
        b = m.group(2)
        h = re.search(r"<h3>((?:(?!</h3>).)*)</h3>", b, re.S)
        if not h:
            continue
        d = {"name": clean(h.group(1)), "classes": " ".join(m.group(1).split())}
        w = re.search(r'class="fakeLink" href="([^"]*)"', b)
        if w: d["website"] = w.group(1)
        p = re.search(r"<p>((?:(?!</p>).)*)</p>", b, re.S)
        if p: d["description"] = clean(p.group(1))
        for lab, key in (("STATUS", "status_site"), ("FOUNDED", "location")):
            x = re.search(r"<h4>%s</h4>\s*<span>((?:(?!</span>).)*)</span>" % lab, b, re.S)
            if x: d[key] = clean(x.group(1))
        pr = re.search(r'class="partners">((?:(?!</div>).)*)</div>', b, re.S)
        if pr: d["partners"] = [clean(x) for x in re.findall(r"<a [^>]*>([^<]*)</a>", pr.group(1))]
        for cls, key in (("investment-location", "location"), ("investment-text", "description"), ("investment-dates", "round_label")):
            x = re.search(r'class="%s">((?:(?!</div>).)*)</div>' % cls, b, re.S)
            if x and clean(x.group(1)): d[key] = clean(x.group(1))
        out.append(d)
    return out

# The firm varied three names on its own pages; the parsed rows carry one spelling each and keep the
# archived one as name_archived. Clinical Solutions is the company the desk pages call CAS Services.
NAME_MAP = {"Clinical Solutions": "Cas Services", "Interesolve": "InterResolve", "Inter Resolve": "InterResolve"}

ERAS = [("portfolio", "2013", era_2013), ("portfolio", "2015", era_2015), ("investments", "2018", era_2018), ("companies", "2019", era_2018)]
years = defaultdict(dict)
report = []
for key, m in sorted(man.items()):
    if m["status"] != "ok":
        continue
    path = re.sub(r"https?://(www\.)?balderton\.com", "", m["url"]).split("?")[0]
    top = path.strip("/")
    if top not in ("portfolio", "investments", "companies"):
        continue
    t = (RAW / key).read_text(encoding="utf-8", errors="replace")
    rows = []
    for _, _, fn in ERAS:
        rows = fn(t)
        if len(rows) >= 20:
            break
    y = m["timestamp"][:4]
    report.append((key, len(t), len(rows)))
    if not rows:
        continue
    for r in rows:
        if not r["name"]:
            continue
        if r["name"] in NAME_MAP:
            r["name_archived"], r["name"] = r["name"], NAME_MAP[r["name"]]
        r["slug"] = slug_of(r["name"])
        r["path"] = path if path.startswith("/") else "/" + path
        r["snapshot_ts"] = m["timestamp"]
        r["capture_url"] = m["capture_url"]
        r["surface"] = "commoncrawl:" + m["crawl"]
        lab = r.get("round_label") or ""
        yy = re.search(r"\b(19|20)\d\d\b", lab)
        if yy:
            r["invest_year"] = yy.group(0)
        k = (r["slug"], r["path"])
        prev = years[y].get(k)
        if prev is None or r["snapshot_ts"] < prev["snapshot_ts"]:
            years[y][k] = r
for k, n, rows in report:
    print(f"{'FAILED PATTERN' if not rows else 'ok':14} {k:70} bytes {n:7} rows {rows}")
PARSED.mkdir(parents=True, exist_ok=True)
for y, rows in sorted(years.items()):
    f = PARSED / f"{y}.json"
    old = json.loads(f.read_text()) if f.exists() else []
    keep = {(r["slug"], r["path"]): r for r in old}
    for k, r in rows.items():
        keep[k] = r
    write_atomic(f, json.dumps(sorted(keep.values(), key=lambda r: (r["slug"], r["path"])), indent=1, ensure_ascii=False) + "\n")
    print(y, "rows from balderton.com:", len(rows), "| file now holds", len(keep))
