#!/usr/bin/env python3
"""Northzone's archived portfolio listings, 2003-2025, into
sources/wayback/parsed/<year>.json (the builder's wayback layer), one row per
company per year with the exact capture URL (`capture_url`), so every row cites
the capture it came from.

Six site generations (config.json wayback._eras_note). Each era below names
its listing URL(s) and a parser; captures are chosen from the CDX index, two
per year (first and second half), status 200 only, and every fetch goes
through scripts/ia_fetch via scratch/ia.py (machine-wide throttle and
cooldown). A failed fetch is recorded as failed in the manifest, never as an
empty year (COLLECTION.md §5).

Usage: python3 scratch/archive-listings.py [era ...]
"""
import html as H
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import ia  # noqa: E402

ROOT = HERE.parent
PARSED = ROOT / "sources" / "wayback" / "parsed"
MANIFEST = ROOT / "sources" / "wayback" / "manifest.json"


def slug_of(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", H.unescape(name).lower()).strip("-")
    return s


def text_lines(h: str) -> list[str]:
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", h, flags=re.S | re.I)
    return [H.unescape(x.strip()) for x in re.sub(r"<[^>]+>", "\n", t).split("\n") if x.strip()]


def captures(url: str, y0: int, y1: int, per_year: int = 2) -> list[tuple[str, str]]:
    """(timestamp, original) for up to `per_year` 200-status captures a year."""
    rows = ia.cdx(f"url={url}&output=json&fl=timestamp,original,statuscode,digest"
                  f"&from={y0}&to={y1}&limit=5000")
    by = defaultdict(list)
    for ts, orig, sc, dg in rows[1:]:
        if sc == "200":
            by[ts[:4]].append((ts, orig, dg))
    out = []
    for y, xs in sorted(by.items()):
        xs.sort()
        halves = [[x for x in xs if x[0][4:6] <= "06"], [x for x in xs if x[0][4:6] > "06"]]
        picked = [h[0] for h in halves if h][:per_year] or xs[:1]
        seen = set()
        for ts, orig, dg in picked:
            if dg in seen:
                continue
            seen.add(dg)
            out.append((ts, orig))
    return out


def add(rows_by_year, year, name, path, ts, orig, **extra):
    name = re.sub(r"\s+", " ", H.unescape(name)).strip()
    if not name:
        return
    rows_by_year[year].append(dict(
        name=name, slug=extra.pop("slug", None) or slug_of(name), path=path,
        snapshot_ts=ts, capture_url=f"https://web.archive.org/web/{ts}/{orig}",
        surface="wayback", **extra))


def write(rows_by_year, era):
    PARSED.mkdir(parents=True, exist_ok=True)
    for year, rows in rows_by_year.items():
        f = PARSED / f"{year}.json"
        cur = json.loads(f.read_text()) if f.exists() else []
        keep = {(r["slug"], r["path"]): r for r in cur}
        for r in rows:
            keep.setdefault((r["slug"], r["path"]), r)
        f.write_text(json.dumps(sorted(keep.values(), key=lambda r: (r["path"], r["slug"])),
                                indent=1, ensure_ascii=False) + "\n")
    man = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
    man[era] = {y: len(r) for y, r in sorted(rows_by_year.items())}
    MANIFEST.write_text(json.dumps(man, indent=1) + "\n")


ERAS = {}


# ---- Common Crawl captures, 2013-2025 (sources/wayback/cc-manifest.json, raw bodies in data/filings/commoncrawl/northzone)
CCRAW = Path(__file__).resolve().parents[5] / "data" / "filings" / "commoncrawl" / "northzone"
SKIP_SLUGS = {"page", "feed", "category", "tag"}
BAD_TITLES = ("one moment", "page not found", "investment archive", "portfolio - northzone", "not found", "active investments", "exits", "portfolio")


def clean_title(t: str) -> str:
    t = H.unescape(re.sub(r"\s+", " ", t)).strip()
    t = re.split(r"\s+[-|–—]\s+Northzone", t)[0].strip()
    return t


def cc_eras():
    man = json.loads((ROOT / "sources" / "wayback" / "cc-manifest.json").read_text())
    rows = defaultdict(list)
    for key, v in sorted(man.items()):
        if v.get("status") != "ok":
            continue
        ts = v["timestamp"]; year = int(ts[:4])
        path = re.sub(r"https?://(www\.)?northzone\.com", "", v["url"]).split("?")[0]
        body = (CCRAW / key).read_text(errors="replace")
        extra = dict(surface="commoncrawl:" + v["crawl"])
        cap = v["capture_url"]
        # 2012-2014 listing: /investments with /investments/<id> anchors naming each company in <strong>
        if re.fullmatch(r"/investments/?", path) and year <= 2014:
            for href, inner in re.findall(r'<a[^>]+href="(/investments/\d+)"[^>]*>(.*?)</a>', body, flags=re.S):
                nm = re.search(r"<strong>(.*?)</strong>", inner, flags=re.S)
                if nm:
                    rows[year].append(dict(name=clean_title(nm.group(1)), slug=slug_of(clean_title(nm.group(1))),
                                           path="/investments", snapshot_ts=ts, capture_url=cap, site_id=href, **extra))
            continue
        seg = re.fullmatch(r"/portfolio/investments-by-segment/[^/]+/([^/]+)/?", path)
        act = re.fullmatch(r"/portfolio/(active-investments|exits)/?", path) and "investment=" in v["url"]
        m = re.fullmatch(r"/(investments|portfolio)/([^/]+)/?", path)
        if seg:
            m = re.match(r"/(portfolio)/investments-by-segment/[^/]+/([^/]+)", path)
        elif act:
            m = re.match(r"/(portfolio)/(active-investments|exits)", path)
            path = path.rstrip("/") + "/?investment=" + v["url"].split("investment=")[1]
        elif not m or m.group(2) in SKIP_SLUGS or m.group(2) in ("active-investments", "exits", "investments-by-segment"):
            continue
        t = re.search(r"<title>(.*?)</title>", body, flags=re.S)
        name = clean_title(t.group(1)) if t else ""
        if not name or any(b in name.lower() for b in BAD_TITLES):
            continue
        desc = None
        if seg or act:
            txt = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>|<style.*?</style>", "", body, flags=re.S))))
            k0 = txt.rfind(name.split()[0] + ":") if (name.split()[0] + ":") in txt else txt.rfind(name)
            if k0 >= 0:
                desc = txt[k0:k0 + 600].strip()
        extra2 = {"description": desc} if desc else {}
        rows[year].append(dict(**extra2, name=name, slug=slug_of(name), path=path if (seg or act) else f"/{m.group(1)}/{m.group(2)}",
                               snapshot_ts=ts, capture_url=cap, site_slug=m.group(2), **extra))
    # one row per (year, slug): keep the earliest capture of the year
    out = defaultdict(list)
    for y, rs in rows.items():
        best = {}
        for r in sorted(rs, key=lambda r: r["snapshot_ts"]):
            best.setdefault((r["slug"], r["path"].split("/")[1]), r)
        out[y] = list(best.values())
    write(out, "commoncrawl-2013-2025")
    print({y: len(r) for y, r in sorted(out.items())})


ERAS["cc"] = cc_eras


W5_2003 = {  # the 2003 page's own description -> the company its 2010 page describes in near-identical words
 "Mobile Instant Messaging (MIM)": "Colibria", "chaos based encryption": "Cryptico", "eLearning needs": "Edvantage Group",
 "Computer Telephony Integration": "Envox", ".name top-level domain": "Global Name Registry",
 "distributors of corporate financial information": "Hugin", "Purchasing software and services": "Ibistic",
 "fixed flat rate per month per user": "Intility", "CRM and e-commerce software for SMEs": "Mamut",
 "broadband Internet access and services to SME": "NextGenTel", "light modulator technology": "Photonyx",
 "number portability": "Port IT", "ski- and online booking": "Skiinfo", "marketplace and service provider for property services": "Tinde",
 "Linux software development tools": "Trolltech"}


def w5_2003():
    ts, orig = "20031017", "http://www.northzone.com:80/portfolio"
    h = ia.replay(ts, orig)
    rows = defaultdict(list)
    cells = re.findall(r'<A href="(/[0-9A-F-]+\.W5Doc)"[^>]*>.*?</A></TD>\s*<TD[^>]*>(.*?)</TD>', h, flags=re.S | re.I)
    unmatched = []
    for href, cell in cells:
        text = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", cell))).strip()
        name = next((n for k, n in W5_2003.items() if k.lower() in text.lower()), None)
        if not name:
            unmatched.append(text); continue
        rows[2003].append(dict(name=name, slug=slug_of(name), path="/portfolio", snapshot_ts=ts,
                               capture_url=f"https://web.archive.org/web/{ts}/{orig}", surface="wayback",
                               description=text, w5doc=href, match_basis="the 2003 description matches the company's 2010 page"))
    write(rows, "w5-2003")
    print(len(rows[2003]), "named;", len(unmatched), "unmatched:", unmatched)
    (ROOT / "sources" / "wayback" / "w5-2003-unmatched.json").write_text(json.dumps(unmatched, indent=1) + "\n")


ERAS["w5"] = w5_2003

if __name__ == "__main__":
    for era in (sys.argv[1:] or list(ERAS)):
        ERAS[era]()
