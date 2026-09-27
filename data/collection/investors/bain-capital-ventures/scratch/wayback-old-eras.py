#!/usr/bin/env python3
"""Read BCV's 2002 to 2010 portfolio listings from the Internet Archive into
sources/wayback/parsed/<year>.json, in the shape wayback-pull.py writes.

Three markups, none of them slug-per-company, so the generic eras cannot read
them (config.json wayback._note):

  asp2003   portfolio.asp?b=4&l=9 (and the b=2 twin): one <TD class='portfoliolink'
            onClick='doNavigate("portfolio.asp?...&c=<id>")'>Name</TD> per company
  asp2006   portfolio/index.asp?viewType=ByIndustry|ByStage|Alphabetically...: cards,
            <div class="contentText_subTitle">Name</div>, a location div, a
            description and an outcome line ("Acquired", "I.P.O. on 02/20/98")
  aspx2009  Portfolio/Alphabetically.aspx, ByIndustry.aspx, ByStage.aspx: cards,
            <h3>Name</h3>, address, description, outcome line, website

The listing pages are enumerated from the CDX index (one capture per URL per
year), fetched through ia_fetch (shared throttle, status-aware), and cached
under sources/wayback/raw-old/. A failed fetch is logged and never recorded as
an empty year (COLLECTION.md 5). Each row carries the page's own context: the
industry or stage filter it was listed under, whether the view was the
"past companies" view, the outcome line and the location.

Usage: python3 data/collection/investors/bain-capital-ventures/scratch/wayback-old-eras.py
"""
import html
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
import ia_fetch  # noqa: E402
from paths import Paths, write_atomic  # noqa: E402

P = Paths("bain-capital-ventures")
RAW = P.wayback / "raw-old"
PARSED = P.wayback / "parsed"
RAW.mkdir(parents=True, exist_ok=True)
PARSED.mkdir(parents=True, exist_ok=True)

PATTERNS = [
    "baincapitalventures.com/portfolio.asp*",
    "baincapitalventures.com/portfolio/index.asp*",
    "baincapitalventures.com/Portfolio/*",
]


def slug_of(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def clean(s: str) -> str:
    s = html.unescape(re.sub(r"<[^>]+>", " ", s))
    return re.sub(r"\s+", " ", s).strip()


def cdx(pattern: str) -> list[tuple[str, str]]:
    url = (f"https://web.archive.org/cdx/search/cdx?url={quote(pattern, safe='*/:')}"
           f"&output=json&fl=timestamp,original&filter=statuscode:200&limit=5000")
    body, code = ia_fetch.get(url)
    if code != "200":
        raise SystemExit(f"CDX refused ({code}) for {pattern}; re-run later, nothing written")
    rows = json.loads(body or b"[]")
    return [(r[0], r[1]) for r in rows[1:]]


def is_listing(orig: str) -> str | None:
    """The era markup a listing URL carries, or None for a company page or asset."""
    o = orig.lower()
    if re.search(r"\.(gif|jpe?g|png|css|js)$", o):
        return None
    if "portfolio.asp" in o and "&c=" not in o and "l=9" in o:
        return "asp2003"
    if "/portfolio/index.asp" in o and "d_company_id" not in o and "viewty" in o:
        if "recent" in o:
            return None     # a subset of the full views, skipped
        return "asp2006"
    if re.search(r"/portfolio/(alphabetically|byindustry|bystage|default|recentinvestments)\.aspx", o):
        return "aspx2009"
    return None


def context_of(orig: str) -> dict:
    o = orig.lower()
    ctx = {}
    if "past_company=1" in o or "section=5" in o:
        ctx["past_view"] = True
    m = re.search(r"industry_?id=(\w+)", o)
    if m:
        ctx["industry_id"] = m.group(1)
    m = re.search(r"(?:d_investment_stage_id|stageid)=(\w+)", o)
    if m:
        ctx["stage_id"] = m.group(1)
    return ctx


def parse_asp2003(t: str) -> list[dict]:
    out = []
    for cid, name in re.findall(
            r"doNavigate\(\"portfolio\.asp\?[^\"]*?c=(\d+)\"\);'[^>]*>([^<]+)</TD>", t):
        out.append({"name": clean(name), "site_id": f"c{cid}"})
    return out


STAGE_TITLES = ("Early", "Midstage", "Expansion/Growth Buyout")


def parse_cards(t: str, name_re: str, split_re: str) -> list[dict]:
    out = []
    # the current section heading (industry or stage) precedes its cards
    pieces = re.split(split_re, t)
    heading = None
    for piece in pieces[1:]:
        m = re.search(name_re, piece, re.S)
        if not m:
            continue
        name = clean(m.group(1))
        if not name:
            continue
        text = clean(piece)
        row = {"name": name}
        mo = re.search(r"I\.P\.O\.\s*on\s*([\d/]+)(?:\s*\(([^)]+)\))?", text)
        if mo:
            row["outcome"] = f"IPO {mo.group(1)}" + (f" ({mo.group(2)})" if mo.group(2) else "")
        elif re.search(r"\bAcquired\b", text):
            row["outcome"] = "Acquired"
        mw = re.search(r'href="(https?://[^"]+)"[^>]*target="_blank"', piece)
        if mw and "baincapital" not in mw.group(1):
            row["website"] = mw.group(1)
        out.append(row)
    return out


def headings(t: str) -> list[tuple[int, str]]:
    """(offset, heading) for each section title on a listing page."""
    hs = [(m.start(), clean(m.group(1))) for m in re.finditer(
        r'<div class="contentText_subTitle" style="margin-bottom:7px;">(.*?)</div>', t, re.S)]
    hs += [(m.start(), clean(m.group(1))) for m in re.finditer(r"<h2>(.*?)</h2>", t, re.S)]
    return sorted(hs)


def parse_asp2006(t: str) -> list[dict]:
    rows = []
    hs = headings(t)
    for m in re.finditer(r'<div class="portfolioDisplay_portfolioInfo_Box">(.*?)'
                         r'<div class="contentSeperator_dottedLine">', t, re.S):
        block = m.group(1)
        nm = re.search(r'<div class="contentText_subTitle">(.*?)</div>', block, re.S)
        if not nm:
            continue
        row = {"name": clean(nm.group(1))}
        text = clean(block)
        mo = re.search(r"I\.P\.O\.\s*on\s*([\d/]+)(?:\s*\(([^)]+)\))?", text)
        if mo:
            row["outcome"] = f"IPO {mo.group(1)}" + (f" ({mo.group(2)})" if mo.group(2) else "")
        elif re.search(r"\bAcquired\b", text):
            row["outcome"] = "Acquired"
        loc = re.search(r'<div class="portfolioDisplay_companyLocation">(.*?)</div>', block, re.S)
        if loc and clean(loc.group(1)):
            row["location"] = clean(loc.group(1))
        mw = re.search(r'href="(https?://[^"]+)"', block)
        if mw and "baincapital" not in mw.group(1):
            row["website"] = mw.group(1)
        sec = [h for off, h in hs if off < m.start()]
        if sec:
            row["section"] = sec[-1]
        rows.append(row)
    return rows


def parse_aspx2009(t: str) -> list[dict]:
    rows = []
    hs = headings(t)
    for m in re.finditer(r'<div class="portfolio_CompanyHolder">(.*?)<div class="portfolio_LogoHolder">',
                         t, re.S):
        block = m.group(1)
        nm = re.search(r"<h3>(.*?)</h3>", block, re.S)
        if not nm:
            continue
        row = {"name": clean(nm.group(1))}
        text = clean(block)
        mo = re.search(r"I\.P\.O\.\s*on\s*([\d/]+)(?:\s*\(([^)]+)\))?", text) or \
            re.search(r"\bIPO\b\s*([\d/]*)", text)
        if mo:
            row["outcome"] = f"IPO {mo.group(1)}".strip()
        elif re.search(r"\bAcquired\b", text):
            row["outcome"] = "Acquired"
        addr = re.search(r"</h3>\s*<p>(.*?)</p>", block, re.S)
        if addr and clean(addr.group(1)):
            row["location"] = clean(addr.group(1))
        mw = re.search(r'WebsiteLink" href="(https?://[^"]+)"', block)
        if mw:
            row["website"] = mw.group(1)
        sec = [h for off, h in hs if off < m.start()]
        if sec:
            row["section"] = sec[-1]
        rows.append(row)
    return rows


PARSE = {"asp2003": parse_asp2003, "asp2006": parse_asp2006, "aspx2009": parse_aspx2009}
# --cached-only: parse the captures already under raw-old/ and fetch nothing (used while the IA
# cooldown is set); an unfetched capture is listed as skipped, never read as an empty year
CACHED_ONLY = "--cached-only" in sys.argv


DOMAIN_CDX = P.wayback / "cdx-domain.txt"


def main():
    captures = []
    if DOMAIN_CDX.exists():
        # The whole domain's capture index, pulled 2026-09-27 19:10 UTC
        # (url=baincapitalventures.com&matchType=domain, statuscode 200,
        # collapse=urlkey: first capture per URL). Used while CDX answers 503;
        # it lists every listing URL the per-pattern queries would.
        for line in DOMAIN_CDX.read_text().splitlines():
            parts = line.split()
            if len(parts) >= 2:
                orig, ts = parts[0], parts[1]
                kind = is_listing(orig)
                if kind:
                    captures.append((ts, orig, kind))
    else:
        for pat in PATTERNS:
            for ts, orig in cdx(pat):
                kind = is_listing(orig)
                if kind:
                    captures.append((ts, orig, kind))
    # one capture per (url, year)
    seen, picks = set(), []
    for ts, orig, kind in sorted(captures):
        key = (orig.lower().replace(":80", "").replace("www.", ""), ts[:4])
        if key in seen:
            continue
        seen.add(key)
        picks.append((ts, orig, kind))
    print(f"{len(picks)} listing captures to read")
    by_year: dict[int, dict[str, dict]] = {}
    failed, skipped = [], []
    for ts, orig, kind in picks:
        fname = RAW / (ts + "-" + re.sub(r"[^A-Za-z0-9]+", "_", orig.split("baincapitalventures.com")[-1])[:150] + ".html")
        if fname.exists():
            body = fname.read_bytes()
        elif CACHED_ONLY:
            skipped.append((ts, orig))
            continue
        else:
            body, code = ia_fetch.get(f"https://web.archive.org/web/{ts}id_/{orig}")
            if code != "200" or not body:
                failed.append((ts, orig, code))
                print(f"  FAILED {code} {ts} {orig}")
                continue
            write_atomic(fname, body.decode("latin-1"), encoding="latin-1")
        t = body.decode("latin-1")
        rows = PARSE[kind](t)
        ctx = context_of(orig)
        y = int(ts[:4])
        path = "/" + orig.split("baincapitalventures.com", 1)[-1].lstrip(":80").lstrip("/")
        for r in rows:
            slug = slug_of(r["name"])
            if not slug:
                continue
            cur = by_year.setdefault(y, {}).setdefault(slug, {
                "slug": slug, "name": r["name"], "path": path, "snapshot_ts": ts,
                "era": kind, "capture_url": f"https://web.archive.org/web/{ts}/{orig}"})
            for k in ("outcome", "location", "website", "site_id"):
                if r.get(k) and not cur.get(k):
                    cur[k] = r[k]
            # The stage is the page's own: every company on a ByStage view with stage id N is in
            # that stage (2006 and 2009-10 alike: 1 Early, 2 Midstage, 3 Expansion/Growth Buyout).
            # Section headings are NOT read: on the 2006 site they are the left nav, identical on
            # every page, and read as filters they labelled all 101 companies "Business Services,
            # Early" (fixed 2026-09-27).
            sid = ctx.get("stage_id")
            if sid in ("1", "2", "3"):
                cur["stage_bucket"] = {"1": "Early", "2": "Midstage", "3": "Expansion/Growth Buyout"}[sid]
        print(f"  {ts} {kind:8s} {len(rows):4d} rows  {path[:90]}")
    for y, comps in sorted(by_year.items()):
        dest = PARSED / f"{y}.json"
        merged = {(r["slug"], r.get("path")): r
                  for r in (json.loads(dest.read_text()) if dest.exists() else [])}
        for r in comps.values():
            merged[(r["slug"], r.get("path"))] = r
        write_atomic(dest, json.dumps(sorted(merged.values(),
                                             key=lambda r: (r["slug"], r.get("path") or "")),
                                      indent=1) + "\n")
        print(f"{y}: {len(comps)} companies")
    if skipped:
        print(f"{len(skipped)} captures not in the cache, skipped (re-run without --cached-only after the cooldown)")
    if failed:
        write_atomic(RAW / "failed.json", json.dumps(failed, indent=1) + "\n")
        print(f"{len(failed)} captures failed; re-run to retry (cached ones are skipped)")
        sys.exit(3)


if __name__ == "__main__":
    main()
