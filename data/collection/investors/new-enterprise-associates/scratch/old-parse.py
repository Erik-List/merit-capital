#!/usr/bin/env python3
"""Parse NEA's pre-2013 portfolio pages into sources/wayback/parsed/<year>.json.

Two markups, whichever archive holds the capture (Common Crawl: sources/wayback/cc-manifest.json;
Internet Archive: sources/wayback/ia-manifest.json, same entry shape, bodies under
data/filings/wayback/new-enterprise-associates/):

  old-cf    2003-2010 ColdFusion site: /PortfolioCompanies/... pages, among them the summary reports
            (SummaryReports/Current, Historical, Acquisitions, Public Purchase, VGE) and the sector pages.
            Each company is a row of <table class="portfolio">: <h3>Name</h3>, <h4>(ticker or exit)</h4>,
            description, website, Sector, Company Status, Investment Status.
  old-aspx  2010-2013 ASP.NET site: /Portfolio/CompanyDetail.aspx?id=N, one company per page: the <h3>
            name, "Acquired By: X", description, Sector, Company Status, Investment Status.

One row per company per capture year, carrying the page it came from (`report`: which summary report,
so a "Public Purchase" listing is visible to the judge as the firm's own label) and the capture URL.
Rows of these eras already in a year file are replaced; rows of other eras are kept.
"""
import collections
import html
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import write_atomic  # noqa: E402

WB = HERE.parent / "sources" / "wayback"
OUT = WB / "parsed"
SOURCES = [(WB / "cc-manifest.json", ROOT / "data" / "filings" / "commoncrawl" / "new-enterprise-associates"),
           (WB / "ia-manifest.json", ROOT / "data" / "filings" / "wayback" / "new-enterprise-associates")]
ERAS = ("old-cf", "old-aspx")


def clean(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()


def slug_of(name):
    import unicodedata
    f = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", f.lower()).strip("-")


def lab(block, label):
    m = re.search(r"<strong>\s*" + label + r"\s*:?\s*(?:&nbsp;)?\s*:?\s*</strong>\s*:?\s*([^<]*)", block, re.I)
    return clean(m.group(1)) if m else ""


def parse_cf(body):
    out = []
    t = re.search(r'<table[^>]*class="portfolio"[^>]*>([\s\S]*?)</table>', body, re.I)
    if not t:
        return out
    for row in re.findall(r"<tr[^>]*>([\s\S]*?)</tr>", t.group(1), re.I):
        h3 = re.search(r"<h3>([\s\S]*?)</h3>", row, re.I)
        if not h3:
            continue
        h4 = re.search(r"<h4>([\s\S]*?)</h4>", row, re.I)
        p = re.search(r"</h4>\s*<P>([\s\S]*?)(?:<BR>|</P>)", row, re.I) or re.search(r"<P>([\s\S]*?)(?:<BR>|</P>)", row, re.I)
        web = re.search(r'<A[^>]*HREF="(https?://[^"]+)"', row, re.I)
        exit_ = clean(h4.group(1)).strip("()") if h4 else ""
        out.append({"name": clean(h3.group(1)), "exit": exit_, "about": clean(p.group(1)) if p else "",
                    "website": web.group(1) if web else "",
                    "sector": lab(row, r"Sector"), "company_status": lab(row, r"Company(?:&nbsp;|\s)Status"),
                    "investment_status": lab(row, r"Investment(?:&nbsp;|\s)Status"),
                    "acquirer": (re.search(r"(?i)acquired by:?\s*(.+)", exit_) or [None, ""])[1]})
    return out


def parse_aspx(body):
    m = re.search(r'<div class="CompanyDetail_InfoHolder">([\s\S]*?)</div>', body)
    if not m:
        return []
    blk = m.group(1)
    h3 = re.search(r"<h3>([\s\S]*?)</h3>", blk)
    if not h3:
        return []
    name = clean(h3.group(1).split("<br")[0])
    acq = re.search(r"Acquired By:\s*([^<]+)", h3.group(1))
    tick = re.search(r"<span>\s*(\((?:NASDAQ|NYSE|AMEX)[^<]*)\s*</span>", h3.group(1), re.I)
    d = re.search(r"<p>\s*<span>([\s\S]*?)</span>", blk)
    return [{"name": name, "exit": clean(acq.group(0)) if acq else (clean(tick.group(1)) if tick else ""),
             "acquirer": clean(acq.group(1)) if acq else "", "about": clean(d.group(1)) if d else "",
             "website": "", "sector": lab(blk, "Sector"), "company_status": lab(blk, "Company Status"),
             "investment_status": lab(blk, "Investment Status")}]


def report_of(path):
    m = re.search(r"/SummaryReports/([A-Za-z]+)", path)
    if m:
        return {"Public": "Public Purchase"}.get(m.group(1), m.group(1))
    m = re.search(r"/PortfolioCompanies/([^?]+)", path)
    return m.group(1).strip("/") if m else ""


def main():
    per_year = collections.defaultdict(list)
    stats = collections.Counter()
    for man_p, raw in SOURCES:
        if not man_p.exists():
            continue
        for k, v in json.loads(man_p.read_text()).items():
            if v.get("status") != "ok":
                continue
            path, url, ts = v.get("path", ""), v.get("url", ""), v.get("timestamp", "")
            if "/PortfolioCompanies/" in path or "/portfoliocompanies/" in path.lower():
                era, parse = "old-cf", parse_cf
            elif re.search(r"(?i)/Portfolio/CompanyDetail\.aspx", path):
                era, parse = "old-aspx", parse_aspx
            else:
                continue
            f = raw / k
            if not f.exists():
                continue
            rows = parse(f.read_text(encoding="utf-8", errors="replace"))
            stats[era + " pages"] += 1
            cap = v.get("capture_url") or f"https://web.archive.org/web/{ts}/{url}"
            for r in rows:
                if not r["name"]:
                    continue
                per_year[ts[:4]].append({"slug": slug_of(r["name"]), "name": r["name"], "path": path,
                                         "snapshot_ts": ts, "capture_url": cap, "filters": "", "era": era,
                                         "report": report_of(path), **{x: r[x] for x in (
                                             "about", "exit", "acquirer", "website", "sector", "company_status",
                                             "investment_status")}})
                stats[era + " rows"] += 1
    for y, rows in sorted(per_year.items()):
        # one row per company per year per report, earliest capture first
        seen, keep = set(), []
        for r in sorted(rows, key=lambda r: r["snapshot_ts"]):
            key = (r["slug"], r["report"])
            if key in seen:
                continue
            seen.add(key)
            keep.append(r)
        f = OUT / f"{y}.json"
        old = [r for r in (json.loads(f.read_text()) if f.exists() else []) if r.get("era") not in ERAS]
        write_atomic(f, json.dumps(old + keep, indent=1, ensure_ascii=False) + "\n")
        stats[f"year {y}"] = len({r['slug'] for r in keep})
    print(dict(stats))


if __name__ == "__main__":
    main()
