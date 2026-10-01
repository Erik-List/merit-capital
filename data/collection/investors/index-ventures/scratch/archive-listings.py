#!/usr/bin/env python3
"""Parse the archived generations of indexventures.com into
sources/wayback/parsed/<year>.json, one row per company per year with the exact
capture URL (`capture_url`), so every row cites the capture it was read from.

Eras (config wayback._eras_note):
  cc      Common Crawl captures 2008-2025 (sources/wayback/cc-manifest.json, raw
          bodies in data/filings/commoncrawl/index-ventures):
            2008-2013 PHP site   /portfolio..., /index.php/portfolio...: every page
                                 carries <ul id="results"> with the companies its
                                 filter selects (industry 1 Technology / 2 Life
                                 Sciences, status, stage 4 Seed / 1 Early / 2 Growth);
                                 /portfolio/index/company_id/<n> adds Contact, Status,
                                 Sector(s), Geography.
            2014-2019 Drupal     /companies/<slug> (HQ, Born In, Index Team, Sector,
                                 Status, Tags) and the /companies listing.
            2019-2025 Wagtail    /companies/<slug>/ (Index Team, Sector).
  ia      Internet Archive, 1999-2007 (static pages and the CGI site), read when
          the archive answers.

Besides the parsed rows it writes sources/wayback/archive-facts.json: per company
key the firm's own archived claims (desk, status, stage filter, partners, sectors,
HQ, the name's ticker-or-acquirer tag), each with the capture it was read from.
Adapted from the Northzone run (PRO-105).
"""
import html as H
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

def read_raw(f):
    """Raw captures are gzipped on disk (2026-10-01: the machine ran out of space mid-run)."""
    import gzip
    g = Path(str(f) + ".gz")
    if g.exists():
        return gzip.open(g, "rt", errors="replace").read()
    return f.read_text(errors="replace") if f.exists() else None


ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[3]
PARSED = ROOT / "sources" / "wayback" / "parsed"
MANIFEST = ROOT / "sources" / "wayback" / "manifest.json"
FACTS = ROOT / "sources" / "wayback" / "archive-facts.json"
CCRAW = REPO / "data" / "filings" / "commoncrawl" / "index-ventures"
sys.path.insert(0, str(Path(__file__).resolve().parent))

STAGE_FILTER = {"4": "Seed stage", "1": "Early stage", "2": "Growth stage"}
INDUSTRY = {"1": "tech", "2": "life"}


def slug_of(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def clean(s: str) -> str:
    return re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def split_tag(display: str):
    """'Addex Pharma (Zurich:ADXN)' -> ('Addex Pharma', 'Zurich:ADXN');
    'Qt (formerly Trolltech) (Nokia)' -> ('Qt', 'formerly Trolltech; Nokia')."""
    display = clean(display)
    tags = re.findall(r"\(([^()]*)\)", display)
    name = re.sub(r"\s*\([^()]*\)", "", display).strip()
    return name, "; ".join(t.strip() for t in tags) if tags else None


def write(rows_by_year, era):
    PARSED.mkdir(parents=True, exist_ok=True)
    for year, rows in rows_by_year.items():
        f = PARSED / f"{year}.json"
        cur = json.loads(f.read_text()) if f.exists() else []
        keep = {(r["slug"], r["path"]): r for r in cur if r.get("era") != era}
        for r in rows:
            keep.setdefault((r["slug"], r["path"]), r)
        f.write_text(json.dumps(sorted(keep.values(), key=lambda r: (r["path"], r["slug"])),
                                indent=1, ensure_ascii=False) + "\n")
    man = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
    man[era] = {str(y): len(r) for y, r in sorted(rows_by_year.items())}
    MANIFEST.write_text(json.dumps(man, indent=1) + "\n")


def fact(facts, key, field, value, cap, ts):
    """Keep every distinct value of a claim with its earliest capture."""
    if value in (None, "", []):
        return
    v = json.dumps(value, ensure_ascii=False, sort_keys=True)
    slot = facts[key].setdefault(field, {})
    if v not in slot or ts < slot[v]["ts"]:
        slot[v] = {"value": value, "ts": ts, "capture_url": cap}


def dl_field(body, label):
    m = re.search(rf"<dt>\s*{label}:?\s*</dt>\s*<dd>(.*?)</dd>", body, flags=re.S)
    if not m:
        return []
    items = re.findall(r"<li>(.*?)</li>", m.group(1), flags=re.S) or [m.group(1)]
    return [clean(i) for i in items if clean(i)]


def cc_eras():
    man = json.loads((ROOT / "sources" / "wayback" / "cc-manifest.json").read_text())
    rows = defaultdict(list)
    facts = defaultdict(dict)
    stats = defaultdict(int)
    for key, v in sorted(man.items()):
        if v.get("status") != "ok":
            continue
        ts = v["timestamp"]; year = int(ts[:4])
        url = v["url"]
        path = re.sub(r"https?://(www\.)?indexventures\.com(:80|:443)?", "", url, flags=re.I).split("?")[0]
        path = re.sub(r"^/index\.php", "", path) or "/"
        f = CCRAW / key
        body = read_raw(f)
        if body is None:
            continue
        cap = v["capture_url"]
        surface = "commoncrawl:" + v["crawl"]

        # ---- 2008-2013 PHP site: any /portfolio page lists the companies its filter selects
        if path.startswith("/portfolio") and year <= 2014 and 'id="results"' in body:
            res = re.search(r'<ul id="results">(.*?)</ul>', body, flags=re.S)
            items = re.findall(r'id="company_(\d+)"[^>]*>(.*?)</a>', res.group(1), flags=re.S) if res else []
            ind = re.search(r"/industry_id/(\d+)", path)
            status = re.search(r"/company_status/(\w+)", path)
            stage = re.search(r"/company_stage/(\d+)", path)
            for cid, disp in items:
                name, tag = split_tag(disp)
                if not name or name.lower() == "index ventures":
                    continue
                k = slug_of(name)
                rows[year].append(dict(name=name, slug=k, path="/portfolio", snapshot_ts=ts, capture_url=cap,
                                       surface=surface, site_id=f"company_id/{cid}", era="cc"))
                fact(facts, k, "name", name, cap, ts)
                fact(facts, k, "list_tag", tag, cap, ts)
                fact(facts, k, "site_id", f"company_id/{cid}", cap, ts)
                if ind and ind.group(1) in INDUSTRY:
                    fact(facts, k, "desk", INDUSTRY[ind.group(1)], cap, ts)
                if status:
                    fact(facts, k, "status_site", status.group(1), cap, ts)
                if stage and stage.group(1) in STAGE_FILTER:
                    fact(facts, k, "stage_filter", STAGE_FILTER[stage.group(1)], cap, ts)
            stats["php_listing_pages"] += 1
            # a company_id page also carries the details of one company
            cm = re.search(r"/company_id/(\d+)", path)
            if cm:
                txt = [H.unescape(x.strip()) for x in re.sub(r"<[^>]+>", "\n", re.sub(
                    r"<script.*?</script>|<style.*?</style>|<!--.*?-->", "", body, flags=re.S)).split("\n") if x.strip()]
                if "Details" in txt:
                    i = txt.index("Details")
                    det = txt[i:i + 60]
                    nm = dict(items).get(cm.group(1))
                    if nm:
                        name, _ = split_tag(nm)
                        k = slug_of(name)

                        def grab(label, stop):
                            if label not in det:
                                return []
                            j = det.index(label) + 1
                            out = []
                            while j < len(det) and det[j] not in stop:
                                if det[j] != ",":
                                    out.append(det[j])
                                j += 1
                            return out
                        stops = {"Contact:", "Website:", "Status:", "Sector(s):", "Geography:", "News", "Jobs", "Stage:"}
                        fact(facts, k, "partners", grab("Contact:", stops), cap, ts)
                        st = grab("Status:", stops)
                        fact(facts, k, "status_site", st[0].lower() if st else None, cap, ts)
                        fact(facts, k, "sectors", grab("Sector(s):", stops), cap, ts)
                        fact(facts, k, "geography", grab("Geography:", stops), cap, ts)
                        fact(facts, k, "website", (grab("Website:", stops) or [None])[0], cap, ts)
                        sg = grab("Stage:", stops)
                        fact(facts, k, "stage_page", sg[0] if sg else None, cap, ts)
                        desc = txt[i - 1] if i > 0 else None
                        fact(facts, k, "description", desc, cap, ts)
                        stats["php_company_pages"] += 1
            continue

        # ---- 2014-2025: one page per company
        m = re.fullmatch(r"/companies/([^/]+)/?", path)
        if m and m.group(1) not in ("a-z", "backed"):
            t = re.search(r"<title>(.*?)</title>", body, flags=re.S)
            title = clean(t.group(1)) if t else ""
            title = re.split(r"\s+\|\s+Index Ventures", title)[0].strip()
            title = re.sub(r"^Index Ventures\s*[|:]\s*", "", title).strip()
            if not title or re.search(r"page not found|^companies$|^index ventures$|404", title, flags=re.I):
                stats["company_pages_skipped"] += 1
                continue
            name, tag = split_tag(title)
            if not name:
                continue
            k = slug_of(name)
            rows[year].append(dict(name=name, slug=k, path=f"/companies/{m.group(1)}", snapshot_ts=ts,
                                   capture_url=cap, surface=surface, site_slug=m.group(1), era="cc"))
            fact(facts, k, "name", name, cap, ts)
            fact(facts, k, "list_tag", tag, cap, ts)
            fact(facts, k, "site_slug", m.group(1), cap, ts)
            if "<dt>" in body:                                   # Drupal 2014-2019
                fact(facts, k, "partners", dl_field(body, "Index Team"), cap, ts)
                fact(facts, k, "sectors", dl_field(body, "Sector"), cap, ts)
                st = dl_field(body, "Status")
                fact(facts, k, "status_site", st[0].lower() if st else None, cap, ts)
                hq = re.search(r"<strong>HQ</strong>:\s*(.*?)</li>", body, flags=re.S)
                born = re.search(r"<strong>Born In</strong>:\s*(.*?)</li>", body, flags=re.S)
                fact(facts, k, "hq", clean(hq.group(1)) if hq else None, cap, ts)
                fact(facts, k, "born_in", clean(born.group(1)) if born else None, cap, ts)
                tg = re.search(r'<div class="tags">(.*?)</ul>', body, flags=re.S)
                fact(facts, k, "tags", [clean(x) for x in re.findall(r"<li>(.*?)</li>", tg.group(1), flags=re.S)] if tg else None, cap, ts)
                web = dl_field(body, "Website")
                fact(facts, k, "website", web[0] if web else None, cap, ts)
                stats["drupal_company_pages"] += 1
            else:                                                 # Wagtail 2019-
                main = body[body.find('<article role="main"'):] if '<article role="main"' in body else body
                lines = [H.unescape(x.strip()) for x in re.sub(r"<[^>]+>", "\n", re.sub(
                    r"<script.*?</script>|<style.*?</style>|<svg.*?</svg>", "", main.split("<footer")[0], flags=re.S)).split("\n") if x.strip()]
                labels = {"Founders/CEOs", "Founder/CEO", "Founders", "Index Team", "Sector", "Sectors", "Website"}

                def block(label):
                    if label not in lines:
                        return []
                    j = lines.index(label) + 1
                    out = []
                    while j < len(lines) and lines[j] not in labels and not lines[j].startswith(("Opens in", "This link opens", "View all")):
                        out.append(lines[j].rstrip(",").strip())
                        j += 1
                    return [x for x in out if x]
                fact(facts, k, "partners", block("Index Team"), cap, ts)
                fact(facts, k, "sectors", block("Sector") or block("Sectors"), cap, ts)
                stats["wagtail_company_pages"] += 1
            continue

        # ---- 2014-2019 Drupal listing pages: names with HQ
        if re.fullmatch(r"/companies/?", path) and "views-row" in body:
            for href, inner in re.findall(r'<li class="views-row[^"]*">\s*<a href="(/companies/[^"]+)">(.*?)</a>\s*</li>', body, flags=re.S):
                nm = re.search(r'<div class="field-content name">(.*?)</div>', inner, flags=re.S)
                if not nm:
                    continue
                name, tag = split_tag(nm.group(1))
                if not name:
                    continue
                k = slug_of(name)
                rows[year].append(dict(name=name, slug=k, path=href, snapshot_ts=ts, capture_url=cap,
                                       surface=surface, site_slug=href.split("/")[-1], era="cc"))
                fact(facts, k, "name", name, cap, ts)
                fact(facts, k, "list_tag", tag, cap, ts)
            stats["drupal_listing_pages"] += 1

    # one row per (year, slug): keep the earliest capture of the year
    out = defaultdict(list)
    for y, rs in rows.items():
        best = {}
        for r in sorted(rs, key=lambda r: r["snapshot_ts"]):
            best.setdefault(r["slug"], r)
        out[y] = list(best.values())
    # drop this era's old rows, then write
    write(out, "cc")
    cur = json.loads(FACTS.read_text()) if FACTS.exists() else {}
    cur["cc"] = {k: {f: sorted(vals.values(), key=lambda x: x["ts"]) for f, vals in v.items()} for k, v in sorted(facts.items())}
    FACTS.write_text(json.dumps(cur, indent=1, ensure_ascii=False) + "\n")
    print(dict(stats))
    print({y: len(r) for y, r in sorted(out.items())}, "distinct", len(facts))


ERAS = {"cc": cc_eras}

if __name__ == "__main__":
    for era in (sys.argv[1:] or list(ERAS)):
        ERAS[era]()
