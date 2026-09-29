#!/usr/bin/env python3
"""Pull and parse every archived list surface of tcv.com (PRO-169).

The Internet Archive holds a TCV company list in almost every year since 2000,
across seven site generations, each with its own markup:

  alpha2000   2000-2002  /portfolio/alphabetical.html   table: name, city, sector
  sector2003  2002-2006  /companies/<sector>.html        span.text12bold name - city, description
  idx2007     2007-2011  /portfolio/ (index.php4)        <dt>Name - City (Acquired by X)</dt><dd>desc
  all2012     2011-2013  /portfolio/all-portfolio.php4   <dd>Name</dd>, "ALL PORTFOLIO COMPANIES"
  wp2013      2013-2016  /portfolio/ (WordPress theme)   div.partnerships-all classes + h4 name
  list2017    2017-2026  /all-companies                  the compliance list (br-separated, then RSC text)
  grid2017    2017-2023  /companies/ (WordPress grid)    card classes: active, sector, DEAL TYPE, partners
  part2024    2024-2026  /partnerships (Next.js RSC)     companies array: name, slug, status

For each surface and year the FIRST and the LAST 200 capture of the year are
read (a list grows through the year; the first capture dates a row, the last
catches what was added). Raw bodies go to sources/wayback/raw/<surface>/<ts>.html
(id_ replay, the captured bytes), parsed rows to sources/wayback/parsed/<year>.json,
one row per (surface, name) per year, keeping the earliest capture that shows it:
  {slug, name, path, snapshot_ts, capture_url, surface, filters, ...extras}
`filters` carries the grid's own classes for grid2017 (sector, deal type,
active flag, partner slugs), comma-separated, as build-company-base.py reads it.

Every fetch goes through scripts/ia_fetch.py (the machine-wide IA throttle and
the status-aware block handling). A failed fetch is logged and never written
as an empty year (COLLECTION.md 5).
"""
import json
import re
import sys
import time
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
import ia_fetch  # noqa: E402

INV = Path(__file__).resolve().parents[1]
WB = INV / "sources/wayback"
RAW = WB / "raw"
PARSED = WB / "parsed"
LOG = []


def slug_of(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def clean(t: str) -> str:
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", unescape(t)).strip()


def cdx(url: str) -> list[tuple[str, str]]:
    body, code = ia_fetch.get(
        f"https://web.archive.org/cdx/search/cdx?url={url}&output=json&fl=timestamp,original,statuscode"
        f"&filter=statuscode:200&limit=5000")
    if code != "200":
        LOG.append(f"CDX FAILED {url} {code}")
        return []
    rows = json.loads(body or b"[]")[1:]
    return [(r[0], r[1]) for r in rows]


def first_last(caps, y0, y1):
    by = {}
    for ts, orig in sorted(caps):
        y = int(ts[:4])
        if y0 <= y <= y1:
            by.setdefault(y, []).append((ts, orig))
    out = []
    for y, lst in sorted(by.items()):
        out.append(lst[0])
        if len(lst) > 1:
            out.append(lst[-1])
    return out


def fetch(surface: str, ts: str, orig: str) -> str:
    dest = RAW / surface / f"{ts}-{slug_of(orig.split('tcv.com', 1)[-1]) or 'root'}.html"
    if dest.exists() and dest.stat().st_size > 0:
        return dest.read_text(encoding="utf-8", errors="replace")
    body, code = ia_fetch.get(f"https://web.archive.org/web/{ts}id_/{orig}")
    if body[:2] == b"\x1f\x8b":
        import gzip
        try:
            body = gzip.decompress(body)
        except OSError:
            pass
    if code != "200" or not body:
        LOG.append(f"FETCH FAILED {surface} {ts} {orig} {code}")
        return ""
    dest.parent.mkdir(parents=True, exist_ok=True)
    txt = body.decode("utf-8", errors="replace")
    dest.write_text(txt)
    return txt


# ---------------------------------------------------------------- parsers
def p_alpha2000(h):
    rows = []
    for m in re.finditer(r"<TR><TD>(?:<A HREF=\"([^\"]*)\"[^>]*>)?<SMALL>(.*?)</SMALL>(?:</A>)?</TD><TD><SMALL>(.*?)</SMALL></TD><TD><SMALL>(.*?)</SMALL></TD></TR>", h, re.I | re.S):
        name = clean(m.group(2))
        if name and name.lower() != "company":
            rows.append({"name": name, "company_site": m.group(1) or "", "city": clean(m.group(3)), "sector_site": clean(m.group(4))})
    return rows


def p_sector2003(h):
    rows = []
    for m in re.finditer(r'(?:<a href="([^"]*)"[^>]*>)?<img src="[^"]*logo-([a-z0-9_-]+)\.gif"[^>]*>(?:</a>)?</td>\s*<td[^>]*>\s*<span class="text12bold">(.*?)</span>(.*?)<br>(.*?)</td>', h, re.I | re.S):
        name = clean(m.group(3))
        rest = clean(m.group(4)).lstrip("- ").strip()
        rows.append({"name": name, "logo_slug": m.group(2), "company_site": m.group(1) or "", "city": rest, "description": clean(m.group(5))})
    return rows


def p_idx2007(h):
    rows = []
    for m in re.finditer(r"<dt>(.*?)</dt>\s*<dd>(.*?)</dd>", h, re.I | re.S):
        dt = m.group(1)
        a = re.search(r"<a [^>]*>(.*?)</a>", dt, re.S)
        if not a:
            continue
        head = clean(a.group(1))
        name, _, city = head.partition(" - ")
        exit_note = re.search(r"\((?:<em>)?(.*?)(?:</em>)?\)\s*<a", dt, re.S)
        rows.append({"name": name.strip(), "city": city.strip(), "note": clean(exit_note.group(1)) if exit_note else "",
                     "description": clean(m.group(2))})
    return rows


def p_all2012(h):
    i = h.find("ALPHABETICALLY")
    seg = h[i:] if i >= 0 else h
    return [{"name": clean(x)} for x in re.findall(r"<dd>(.*?)</dd>", seg, re.S) if clean(x)]


def p_wp2013(h):
    rows = []
    for m in re.finditer(r'<div class="partnerships-all([^"]*)">(.*?)<h4>(.*?)</h4>\s*<small>(.*?)</small>\s*<div class="description">(.*?)</div>', h, re.S):
        classes = [c for c in re.split(r"[\s*]+", m.group(1)) if c]
        small = clean(m.group(4))
        city, _, note = small.partition(" - ")
        rows.append({"name": clean(m.group(3)), "filters": ",".join(classes), "city": city.strip(),
                     "note": note.strip().strip("()"), "description": clean(m.group(5)),
                     "current": "current-partnerships" in classes})
    return rows


def _list_names(names, known):
    """Re-join a name the list wrapped over two <br /> lines ("Advanced Switching" +
    "Communications, Inc."), where the joined form is a name some capture shows whole."""
    out, i = [], 0
    kn = {re.sub(r"[^a-z0-9]", "", k.lower()) for k in known}
    while i < len(names):
        a = names[i]
        if i + 1 < len(names):
            j = re.sub(r"[^a-z0-9]", "", (a + " " + names[i + 1]).lower())
            if j in kn and re.sub(r"[^a-z0-9]", "", a.lower()) not in kn:
                out.append(a + " " + names[i + 1]); i += 2; continue
        out.append(a); i += 1
    return out


KNOWN_WHOLE: set[str] = set()


def p_list2017(h):
    # WordPress era (2017-2023): the list follows the disclaimer as <br />-separated
    # names, in a <div class="row all-companies"> of three columns (2019 on) or one
    # block (2017); it ends at the footer or the page's own "Note:" paragraph
    i = h.find("equal the performance")
    if i >= 0 and "<br" in h[i:i + 8000]:
        seg = h[h.find("</p>", i) + 4 if h.find("</p>", i) > 0 else i:]
        ends = [x for x in (seg.find("<footer"), seg.find("Note:"), seg.find("Does not include"),
                            seg.find('<div class="row footer'), seg.find("</section>")) if x > 0]
        seg = seg[:min(ends)] if ends else seg[:60000]
        parts = [clean(x) for x in re.split(r"<br\s*/?>|</p>|</div>|<div[^>]*>|<p[^>]*>", seg)]
        names = [p for p in parts if p and len(p) < 120 and not p.lower().startswith(("no assumptions", "it should", "note:"))]
        return [{"name": n} for n in _list_names(names, KNOWN_WHOLE)]
    # Next.js era: the RSC text block, "*as of ..." then one name per line
    chunks = re.findall(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)', h, flags=re.S)
    s = "".join(json.loads('"' + c + '"') for c in chunks) if chunks else h
    m = re.search(r"\n[0-9a-f]+:T([0-9a-f]+),", s)
    if not m:
        return []
    block = s[m.end():].encode("utf-8")[:int(m.group(1), 16)].decode("utf-8", "ignore")
    lines = [l.strip() for l in block.split("\n") if l.strip()]
    asof = lines[0] if lines and lines[0].startswith("*") else ""
    return [{"name": l, "list_asof": asof} for l in lines if not l.startswith("*")]


def p_grid2017(h):
    rows = []
    for m in re.finditer(r'<div class="([^"]*\bgrid-item\b[^"]*)">\s*<a href="[^"]*/companies/([^/"]+)/?"><img [^>]*alt="([^"]*)"', h, re.S):
        classes = [c for c in m.group(1).split() if c not in ("col-xs-6", "col-sm-4", "col-md-3", "columns", "text-center", "grid-item")]
        deal = next((c for c in classes if c in ("minority", "majority", "public")), "")
        rows.append({"name": unescape(m.group(3)).strip(), "page_slug": m.group(2), "filters": ",".join(classes),
                     "deal_type": deal, "active": "active-investments" in classes,
                     "page_url": f"https://www.tcv.com/companies/{m.group(2)}/"})
    return rows


def p_part2024(h):
    chunks = re.findall(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)', h, flags=re.S)
    s = "".join(json.loads('"' + c + '"') for c in chunks) if chunks else h
    rows = []
    for m in re.finditer(r'"name":"([^"]+)","sectors2":\{"items":\[(.*?)\]\},"slug":"([^"]+)","status":"([^"]+)"', s):
        secs = re.findall(r'"name":"([^"]+)"', m.group(2))
        rows.append({"name": unescape(m.group(1)), "page_slug": m.group(3), "status_site": m.group(4),
                     "filters": ",".join(slug_of(x) for x in secs)})
    return rows


SURFACES = [
    ("alpha2000", ["tcv.com/portfolio/alphabetical.html"], 2000, 2002, p_alpha2000),
    ("sector2003", ["tcv.com/companies/communications.html", "tcv.com/companies/software.html",
                    "tcv.com/companies/services.html", "tcv.com/companies/other.html",
                    "tcv.com/companies/internet.html", "tcv.com/companies/financial.html"], 2002, 2006, p_sector2003),
    ("idx2007", ["tcv.com/portfolio/", "tcv.com/portfolio/index.php4"], 2006, 2012, p_idx2007),
    ("all2012", ["tcv.com/portfolio/all-portfolio.php4"], 2010, 2013, p_all2012),
    ("wp2013", ["tcv.com/portfolio/"], 2013, 2016, p_wp2013),
    ("list2017", ["tcv.com/all-companies/", "tcv.com/all-companies"], 2017, 2026, p_list2017),
    ("grid2017", ["tcv.com/companies/"], 2017, 2023, p_grid2017),
    ("part2024", ["tcv.com/partnerships"], 2024, 2026, p_part2024),
]


def main():
    only = set(sys.argv[1:])
    live = INV / "sources/site/all-companies-2026.json"
    if live.exists():
        KNOWN_WHOLE.update(r["legal_name"] for r in json.load(open(live))["rows"])
    per_year: dict[int, dict[tuple, dict]] = {}
    for f in PARSED.glob("*.json"):
        per_year[int(f.stem)] = {(r["surface"], r["slug"]): r for r in json.load(open(f))}
    summary = []
    for surface, urls, y0, y1, parser in SURFACES:
        if only and surface not in only:
            continue
        caps = []
        for u in urls:
            caps += cdx(u)
        # the idx2007 generation shares /portfolio/ with wp2013: the year range splits them
        picks = first_last(caps, y0, y1)
        for ts, orig in picks:
            h = fetch(surface, ts, orig)
            if not h:
                continue
            rows = parser(h)
            y = int(ts[:4])
            summary.append((surface, ts, orig.split("tcv.com", 1)[-1], len(rows)))
            bucket = per_year.setdefault(y, {})
            path = "/" + orig.split("tcv.com", 1)[-1].lstrip(":80").lstrip("/")
            for r in rows:
                nm = r.get("name") or ""
                slug = slug_of(nm) or r.get("logo_slug") or r.get("page_slug") or ""
                if not slug:
                    continue
                key = (surface, slug)
                if key in bucket and bucket[key]["snapshot_ts"] <= ts:
                    continue
                bucket[key] = {"slug": slug, "name": nm, "path": path, "snapshot_ts": ts,
                               "capture_url": f"https://web.archive.org/web/{ts}/{orig}",
                               "surface": surface, **{k: v for k, v in r.items() if k != "name"}}
    PARSED.mkdir(parents=True, exist_ok=True)
    for y, bucket in sorted(per_year.items()):
        (PARSED / f"{y}.json").write_text(json.dumps(sorted(bucket.values(), key=lambda r: (r["surface"], r["slug"])),
                                                      indent=1, ensure_ascii=False))
    for s in summary:
        print(*s)
    for l in LOG:
        print(l)
    print({y: len(b) for y, b in sorted(per_year.items())})


if __name__ == "__main__":
    main()
