#!/usr/bin/env python3
"""Parse NEA's archived per-company pages (nea.com/portfolio/<slug>, 2013 on) from
Common Crawl into sources/wayback/parsed/<year>.json.

One row per slug per year in which Common Crawl holds a 200 capture of the page
(the index says the page existed that year; no fetch is needed for that). The
page's content comes from the one fetched capture of the slug (cc-fetch.py
--first-per-path): the firm's own name (the h1 logo's alt, else the title
tag), description, "Year invested", "Investment Stage", sectors, "Investment
Status" (Current / Historic) and "Company Status" with the acquirer in
brackets ("IPO/Public (by Amgen)").

A catch-all shell (one body served for any slug) is dropped by digest: a digest
shared by more than two slugs is not a company page (COLLECTION.md 5).
Each row's capture_url is that year's first capture, in index.commoncrawl.org
form, used verbatim as the row's wayback_first_link.
Usage: python3 cc-parse.py
"""
import collections
import html
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import write_atomic  # noqa: E402

IDX = HERE / "cc-index-raw.json"
MAN = HERE.parent / "sources" / "wayback" / "cc-manifest.json"
RAW = ROOT / "data" / "filings" / "commoncrawl" / "new-enterprise-associates"
OUT = HERE.parent / "sources" / "wayback" / "parsed"
PAGE = re.compile(r"^https?://(?:www\.)?nea\.com(?::\d+)?/portfolio/([^/?#]+)/?$", re.I)
NOT_COMPANY = {"default.aspx", "casestudies.aspx", "casestudydetail.aspx", "companydetail.aspx",
               "programs-events", "resources"}


def clean(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()


def field(body, label):
    m = re.search(r'<strong class="label">\s*' + re.escape(label) + r'\s*</strong>([\s\S]*?)</li>\s*(?=<li|</ul>)',
                  body, re.I)
    return clean(m.group(1)) if m else ""


def parse(body):
    out = {}
    m = re.search(r'<h1>\s*<img[^>]*alt="([^"]*)"', body)
    name = html.unescape(m.group(1)).strip() if m else ""
    if not name:
        # skip the 2019-23 site's screen-reader <h1>NEA</h1>
        for m in re.finditer(r"<h1[^>]*>([\s\S]*?)</h1>", body):
            if clean(m.group(1)).upper() != "NEA":
                name = clean(m.group(1))
                break
    if not name or name.upper() == "NEA":
        m = re.search(r"<title>([\s\S]*?)</title>", body, re.I)
        name = re.split(r"\s*[|\-–]\s*NEA\b", clean(m.group(1)) if m else "")[0].strip()
    # the 2024+ Next.js pages have no h1 logo; their <title> reads "NEA Portfolio: <name>"
    out["name"] = re.sub(r"^(?:NEA Portfolio:|NEA \|)\s*", "", name).strip()
    m = re.search(r'<div class="text text-tight padded">\s*<p>([\s\S]*?)</p>', body)
    out["about"] = clean(m.group(1)) if m else ""
    out["invest_year"] = (re.search(r"\b(19[5-9]\d|20[0-2]\d)\b", field(body, "Year invested")) or [""])[0] \
        if field(body, "Year invested") else ""
    out["stage_site"] = field(body, "Investment Stage")
    sm = re.search(r'<strong class="label">\s*Sectors\s*</strong>([\s\S]*?)</ul>', body)
    out["sectors"] = [clean(x) for x in re.findall(r"<a [^>]*>([\s\S]*?)</a>", sm.group(1))] if sm else []
    out["investment_status"] = field(body, "Investment Status")
    cs = field(body, "Company Status")
    out["exit"] = cs
    m = re.search(r"\(by ([^)]+)\)", cs)
    out["acquirer"] = m.group(1).strip() if m else ""
    return out


def main():
    idx = json.loads(IDX.read_text())
    man = json.loads(MAN.read_text())
    # slug -> year -> first capture (timestamp, crawl, url, digest)
    caps = collections.defaultdict(dict)
    for cid, slots in idx.items():
        for _k, v in slots.items():
            for r in v.get("records", []):
                m = PAGE.match(r["url"])
                if not m or r.get("status") != "200":
                    continue
                slug = m.group(1).lower().rstrip(".")
                if slug in NOT_COMPANY:
                    continue
                y = r["timestamp"][:4]
                cur = caps[slug].get(y)
                if cur is None or r["timestamp"] < cur[0]:
                    caps[slug][y] = (r["timestamp"], cid, r["url"], r.get("digest"))
    # the fetched body per slug
    body_of = {}
    for k, v in man.items():
        if v.get("status") != "ok":
            continue
        m = PAGE.match(v["url"])
        if m:
            body_of.setdefault(m.group(1).lower().rstrip("."), (k, v))
    # catch-all shell filter: a digest shared across slugs
    dig_slugs = collections.defaultdict(set)
    for slug, ys in caps.items():
        for y, (_ts, _cid, _u, d) in ys.items():
            if d:
                dig_slugs[d].add(slug)
    shell = {d for d, s in dig_slugs.items() if len(s) > 2}
    per_year = collections.defaultdict(list)
    stats = collections.Counter()
    for slug, ys in sorted(caps.items()):
        info = {}
        if slug in body_of:
            k, v = body_of[slug]
            if v.get("digest") in shell:
                stats["shell_body"] += 1
                continue
            info = parse((RAW / k).read_text(encoding="utf-8", errors="replace"))
            info["content_ts"] = v["timestamp"]
        else:
            stats["no_body"] += 1
        for y, (ts, cid, url, d) in sorted(ys.items()):
            if d in shell:
                stats["shell_year"] += 1
                continue
            per_year[y].append({
                "slug": slug, "name": info.get("name") or "", "path": f"/portfolio/{slug}",
                "snapshot_ts": ts,
                "capture_url": f"https://index.commoncrawl.org/{cid}-index?url={quote(url, safe='')}&output=json",
                "filters": "", "era": "cc-company-page",
                "about": info.get("about", ""), "invest_year": info.get("invest_year", ""),
                "stage_site": info.get("stage_site", ""), "sectors": info.get("sectors", []),
                "investment_status": info.get("investment_status", ""), "exit": info.get("exit", ""),
                "acquirer": info.get("acquirer", ""), "content_ts": info.get("content_ts", ""),
            })
    OUT.mkdir(parents=True, exist_ok=True)
    for y, rows in sorted(per_year.items()):
        # merge rather than replace (COLLECTION.md 5): rows of another era already in the year file are kept
        f = OUT / f"{y}.json"
        old = [r for r in (json.loads(f.read_text()) if f.exists() else []) if r.get("era") != "cc-company-page"]
        write_atomic(f, json.dumps(old + rows, indent=1, ensure_ascii=False) + "\n")
        stats[f"year {y}"] = len(rows)
    named = sum(1 for s in caps if s in body_of)
    print(f"{len(caps)} slugs, {named} with a fetched body, {len(shell)} shell digests; {dict(stats)}")


if __name__ == "__main__":
    main()
