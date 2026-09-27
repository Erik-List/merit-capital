#!/usr/bin/env python3
"""Parse Common Crawl captures of baincapitalventures.com into sources/wayback/parsed/<year>.json
(the shape wayback-pull.py writes; parsed year files MERGE keyed slug+path, COLLECTION.md §5).

Captures come from scratch/cc-cluster.py (index) and scratch/cc-fetch.py (bodies under
data/filings/commoncrawl/bain-capital-ventures/, manifest sources/wayback/cc-manifest.json).
Common Crawl carries the site from 2009 (CC-MAIN-2009-2010); the 2002 to 2008 ASP site is not in
it and stays with scratch/wayback-old-eras.py.

Rows, by site era:
  aspx2009   2009-10 /Portfolio/Alphabetically|ByIndustry|ByStage|Default.aspx: cards (<h3>Name</h3>,
             address, description, outcome line, website); ByStage sections give the firm's stage
             bucket (Early Stage / Midstage / Expansion/Growth Buyout)
  listing    2012-13 /portfolio/ (links to /portfolio/company/<slug>, <h4>Name</h4>) and 2016-22
             WordPress /portfolio/ (links to /portfolio/<slug>/, <h4>Name</h4>)
  page2012   /portfolio/company/<slug> (2011-15): <h1>Name</h1>, the stock-info line ("Lala was
             acquired by Apple, Inc. on December 2009."), the "How we worked with X" narrative
             (often names the round BCV led) and the Related Team Members
  pagewp     /portfolio/<slug>/ (2015-23): title "Name - Bain Capital Ventures", Status (Active /
             Exited), Exit Detail, Stage (Seed/Early Stage, Growth; 2022 on Seed/Early/Growth),
             Sector, BCV Lead, location, Founded
  index      every other capture of a company page in the index, dated by the capture, named from a
             fetched body of the same slug; a digest shared by 3+ slugs in one crawl is a shell.
Every row carries capture_url in the index.commoncrawl.org form (COLLECTION.md §1: a valid citation).
Usage: python3 cc-parse.py
"""
import html, importlib.util, json, re, sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402
spec = importlib.util.spec_from_file_location("woe", HERE / "wayback-old-eras.py")
woe = importlib.util.module_from_spec(spec); spec.loader.exec_module(woe)
I = HERE.parent
RAW = HERE.parents[4] / "data" / "filings" / "commoncrawl" / "bain-capital-ventures"
PARSED = I / "sources" / "wayback" / "parsed"
man = json.loads((I / "sources" / "wayback" / "cc-manifest.json").read_text())
idx = json.loads((HERE / "cc-index-raw.json").read_text())
cfg = json.loads((I / "config.json").read_text())
JUNK = set(cfg["wayback"].get("non_company_slugs") or []) | {"filtered", "filtered-new"}
DOM = re.compile(r"https?://(www\.)?baincapitalventures\.com(:\d+)?", re.I)


def clean(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()


def cap_url(cid, url):
    return f"https://index.commoncrawl.org/{cid}-index?url={quote(url, safe='')}&output=json"


def body(k):
    return (RAW / k).read_bytes().decode("utf-8", "replace")


rows = defaultdict(list)                 # year -> rows
names = {"company": {}, "wp": {}}        # slug -> the site's rendering, per URL namespace


def field(txt, label, stop):
    m = re.search(re.escape(label) + r"\s*\|\s*(.*?)\s*\|\s*(?:" + stop + ")", txt)
    return m.group(1).strip() if m else ""


def page_text(t):
    main = re.sub(r"<script.*?</script>|<style.*?</style>|<nav.*?</nav>|<header class=\"site-header.*?</header>|<footer.*?</footer>",
                  "", t, flags=re.S | re.I)
    x = html.unescape(re.sub(r"<[^>]+>", " | ", main))
    return re.sub(r"(\s*\|\s*)+", " | ", x)


counts = defaultdict(int)
for k, v in sorted(man.items(), key=lambda kv: kv[1]["timestamp"]):
    if v["status"] != "ok":
        continue
    path, ts, year = v["path"], v["timestamp"], v["timestamp"][:4]
    t = body(k)
    cid = k.split("/")[0]
    # --- 2009-10 ASPX listings
    if re.match(r"(?i)^/portfolio/(alphabetically|byindustry|bystage|default|recentinvestments)\.aspx$", path):
        for r in woe.parse_aspx2009(t):
            slug = woe.slug_of(r["name"])
            if not slug:
                continue
            row = {"slug": slug, "name": r["name"], "path": path, "snapshot_ts": ts, "era": "aspx2009",
                   "source": "commoncrawl-listing", "capture_url": v["capture_url"]}
            for f in ("outcome", "location", "website"):
                if r.get(f):
                    row[f] = r[f]
            sid = re.search(r"(?i)stageid=(\d)", v["url"])
            if "bystage" in path.lower() and sid:
                # the page's own nav: stageid 1 Early Stage, 2 Midstage, 3 Expansion/Growth Buyout
                row["stage_bucket"] = {"1": "Early Stage", "2": "Midstage", "3": "Expansion/Growth Buyout"}.get(sid.group(1), "")
            row["path"] = path + ("?" + v["url"].split("?", 1)[1] if "?" in v["url"] else "")
            rows[year].append(row)
            counts["aspx2009"] += 1
        continue
    # --- listings of 2012-13 and 2016-22
    if path in ("/portfolio", "/portfolio/"):
        got = 0
        for m in re.finditer(r'href="[^"]*?/portfolio/(company/)?([A-Za-z0-9_.\-]+)/?"[^>]*>(?:(?!</li>|View More).){0,700}?<h4>(.*?)</h4>', t, re.S):
            ns, slug, nm = ("company" if m.group(1) else "wp"), m.group(2).lower(), clean(m.group(3))
            if slug in JUNK or not nm:
                continue
            names[ns].setdefault(slug, nm)
            rows[year].append({"slug": slug, "name": nm, "path": f"/portfolio/{m.group(1) or ''}{slug}",
                               "snapshot_ts": ts, "era": "listing" + ("2012" if ns == "company" else "wp"),
                               "source": "commoncrawl-listing", "capture_url": v["capture_url"]})
            got += 1
        counts["listing"] += got
        continue
    # --- 2011-15 company pages
    m = re.match(r"^/portfolio/company/([A-Za-z0-9_.\-]+)/?$", path)
    if m:
        slug = m.group(1).lower()
        h1 = re.search(r"<h1>(.*?)</h1>", t, re.S)
        nm = clean(h1.group(1)) if h1 else ""
        if not nm or nm.lower() == "portfolio":
            continue
        names["company"].setdefault(slug, nm)
        row = {"slug": slug, "name": nm, "path": f"/portfolio/company/{slug}", "snapshot_ts": ts, "era": "page2012",
               "source": "commoncrawl-page", "capture_url": v["capture_url"]}
        si = re.search(r'<span class="stock-info">(.*?)</span>', t, re.S)
        if si and clean(si.group(1)):
            row["outcome"] = clean(si.group(1))[:300]
        ww = re.search(r"How we worked with.*?</h3>\s*<div class=\"accordion-view\">(.*?)</div>", t, re.S)
        if ww:
            row["worked_with"] = clean(ww.group(1))[:1500]
        rel = re.search(r"Related Team Members(.*?)</ul>", t, re.S)
        if rel:
            row["partners"] = [clean(x) for x in re.findall(r'<span class="item-name">(.*?)</span>', rel.group(1), re.S)]
        rows[year].append(row)
        counts["page2012"] += 1
        continue
    # --- WordPress-era company pages
    m = re.match(r"^/portfolio/([A-Za-z0-9_.\-]+)/?$", path)
    if m and m.group(1).lower() not in JUNK:
        slug = m.group(1).lower()
        ti = re.search(r"<title>(.*?)</title>", t, re.S)
        nm = clean(ti.group(1)) if ti else ""
        nm = re.sub(r"\s*[-–|]\s*Bain Capital Ventures\s*$", "", nm).strip()
        if not nm or nm.lower() in ("portfolio", "page not found"):
            continue
        names["wp"].setdefault(slug, nm)
        x = page_text(t)
        row = {"slug": slug, "name": nm, "path": f"/portfolio/{slug}", "snapshot_ts": ts, "era": "pagewp",
               "source": "commoncrawl-page", "capture_url": v["capture_url"]}
        st = field(x, "Status:", "Exit Detail:|Stage:")
        ex = field(x, "Exit Detail:", "Stage:|Sector:")
        sg = field(x, "Stage:", "Sector:|BCV Lead:")
        ml = re.search(r"BCV Lead:\s*\|\s*([^|]{3,40}?)\s*\|", x)
        lead = ml.group(1).strip() if ml else ""
        if st:
            row["site_status"] = st
        if ex and ex.lower() != "current":
            row["outcome"] = ex
        if sg:
            row["stage_wp"] = sg
        if lead:
            row["partners"] = [lead]
        if not sg:   # the 2022 layout: "| Seed | Commerce | Apps | Founded | 2020 | City |"
            m2 = re.search(r"\|\s*(Seed|Early|Growth|Pre-Seed)\s*\|", x[:1500])
            if m2:
                row["stage_wp"] = m2.group(1)
        fo = re.search(r"\|\s*Founded\s*\|\s*(\d{4})\s*\|\s*([^|]{3,40})\|", x)
        if fo:
            row["founded"] = fo.group(1)
            row["location"] = fo.group(2).strip()
        rows[year].append(row)
        counts["pagewp"] += 1

# --- index rows: every capture of a company page, dated by the capture
per_crawl_digest = defaultdict(lambda: defaultdict(set))
recs = []
for cid, v in idx.items():
    for r in v.get("records", []):
        p = DOM.sub("", r["url"]).split("?")[0]
        m = re.match(r"^/portfolio/(company/)?([A-Za-z0-9_.\-]+)/?$", p)
        if not m or m.group(2).lower() in JUNK:
            continue
        slug = m.group(2).lower()
        per_crawl_digest[cid][r.get("digest")].add(slug)
        recs.append((cid, r, "company" if m.group(1) else "wp", slug))
seen, shells = set(), 0
for cid, r, ns, slug in sorted(recs, key=lambda x: x[1]["timestamp"]):
    if len(per_crawl_digest[cid][r.get("digest")]) >= 3:
        shells += 1
        continue
    year = r["timestamp"][:4]
    path = f"/portfolio/{'company/' if ns == 'company' else ''}{slug}"
    if (year, path) in seen:
        continue
    seen.add((year, path))
    row = {"slug": slug, "path": path, "snapshot_ts": r["timestamp"], "source": "commoncrawl-index",
           "capture_url": cap_url(cid, r["url"])}
    if names[ns].get(slug):
        row["name"] = names[ns][slug]
    rows[year].append(row)
print(dict(counts), f"| index rows {len(seen)}, shells dropped {shells}")

# deal partners ride the build's `filters` string: a tag that is a roster slug lands in
# partners_site (build-company-base.py layer 1); name variants fold onto the roster's slug
VAR = {"mike-krupka": "michael-krupka", "j-benjamin-nye": "ben-nye", "j-benjamin-h-nye": "ben-nye",
       "benjamin-nye": "ben-nye", "jeffrey-schwartz": "jeff-schwartz", "john-m-connolly": "john-connolly",
       "indy-guha": "indranil-guha", "jeffrey-glass": "jeff-glass", "jeffrey-crisan": "jeff-crisan"}
for year, new in rows.items():
    for r in new:
        if r.get("partners"):
            tags = [VAR.get(t, t) for t in (re.sub(r"[^a-z0-9]+", "-", p.lower()).strip("-") for p in r["partners"]) if t]
            r["filters"] = ",".join(dict.fromkeys(tags))

for year, new in sorted(rows.items()):
    f = PARSED / f"{year}.json"
    old = json.loads(f.read_text()) if f.exists() else []
    have = {(r["slug"], r.get("path")): r for r in old}
    add = []
    for r in new:
        cur = have.get((r["slug"], r.get("path")))
        if cur is None:
            have[(r["slug"], r.get("path"))] = r
            add.append(r)
        else:   # enrich an existing row with fields it lacks, never overwrite
            for kk, vv in r.items():
                cur.setdefault(kk, vv)
    write_atomic(f, json.dumps(sorted(have.values(), key=lambda r: (r["slug"], r.get("path") or "")),
                               indent=1, ensure_ascii=False) + "\n")
    print(year, "+", len(add), "rows, file holds", len(have))
