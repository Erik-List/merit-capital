#!/usr/bin/env python3
"""Sutter Hill Ventures' archived portfolio, every era, into
sources/wayback/parsed/<year>.json (wayback-pull.py's row shape).

The firm listed its portfolio from 1999 to 2016 on two mirrored domains
(shv.com, sutterhillventures.com); since 2017 the site is a wordmark and an
address. Four eras, none of which the generic era parsers read:

  table1999   investments.htm (1999 to 2000): one table of every investment
              since 1970, per row the name, a description and the firm's own
              outcome line ("Acquired by Teradyne", "Public company").
  sector2000  software.html, medicaltech.html, networking.html,
              informationtech.html (2000 to 2003): logo grids linking a page
              per company under /soft/, /mt/, /nt/, /it/.
  sector2004  /software/, /healthcare/, /networking/, /business/, /consumer/,
              /investment/ (2004 to 2012): an index page per sector linking a
              page per company; the company page names it in
              <span class="bodylink">.
  drupal2013  /portfolio-full (2013 to 2016): every company with its
              description and its "Managing Director"; /portfolio/<sector>
              filters; a page per company at the site root.

Which years a company was listed comes from the sector index captures (one per
year per page per domain, CDX collapse on the year); the name comes from the
company's own page. Every row cites the capture it was read from
(`capture_url`), so the build uses it verbatim.

A failed fetch is never an empty year: the script records it under
raw/failures.json and exits 3, and a re-run fetches only what is missing
(every capture is cached in raw/ by timestamp and URL).

Usage: python3 data/collection/investors/sutter-hill-ventures/scratch/wayback-eras.py
"""
from __future__ import annotations

import html as H
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
import ia_fetch  # noqa: E402
from paths import Paths, write_atomic  # noqa: E402

P = Paths("sutter-hill-ventures")
RAW = P.wayback / "raw"
PARSED = P.wayback / "parsed"
DOMAINS = ("shv.com", "sutterhillventures.com")
FAILURES: list[str] = []

SECTOR2000 = {"software.html": "Software", "medicaltech.html": "Medical Technology",
              "networking.html": "Networking", "informationtech.html": "Information Technology"}
SECTOR2004 = {"software": "Software", "healthcare": "Healthcare", "networking": "Networking & Computer Technology",
              "business": "Business & Financial Services", "consumer": "Consumer",
              "investment": "Investment Partnerships"}
DRUPAL_SECTORS = {"software": "Software", "consumer": "Consumer", "healthcare": "Healthcare",
                  "investment-partnerships": "Investment Partnerships",
                  "networking-&-computer-technology": "Networking & Computer Technology",
                  "business-&-financial-services": "Business & Financial Services"}


def slug_of(name: str) -> str:
    s = H.unescape(name).lower().replace("&", " and ")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def clean(s: str) -> str:
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    s = H.unescape(s).replace("\xa0", " ")
    return " ".join(s.split())


def cache_name(ts: str, url: str) -> Path:
    return RAW / f"{ts}-{re.sub(r'[^A-Za-z0-9]+', '_', url.split('//')[-1])[:90]}.html"


def fetch(ts: str, url: str) -> str | None:
    """Raw capture body (id_), cached. None on a failed fetch (recorded)."""
    f = cache_name(ts, url)
    if f.exists() and f.stat().st_size > 0:
        return f.read_bytes().decode("latin-1", errors="replace")
    body, code = ia_fetch.get(f"https://web.archive.org/web/{ts}id_/{url}")
    if code != "200" or not body:
        FAILURES.append(f"{code} {ts} {url}")
        return None
    RAW.mkdir(parents=True, exist_ok=True)
    f.write_bytes(body)
    return body.decode("latin-1", errors="replace")


def cdx(url: str, **kw) -> list[list[str]] | None:
    q = "&".join(f"{k}={v}" for k, v in kw.items())
    body, code = ia_fetch.get(f"https://web.archive.org/cdx/search/cdx?url={url}&output=json&{q}")
    if code != "200":
        FAILURES.append(f"cdx {code} {url}")
        return None
    try:
        rows = json.loads(body) if body.strip() else []
    except json.JSONDecodeError:
        FAILURES.append(f"cdx unparsable {url}")
        return None
    return rows[1:] if rows else []


def yearly(path: str, y0: int, y1: int) -> dict[int, tuple[str, str]]:
    """year -> (ts, original) for the first 200 capture of `path` in each year,
    either domain, memoised in raw/index-captures.json."""
    memo_f = RAW / "index-captures.json"
    memo = json.loads(memo_f.read_text()) if memo_f.exists() else {}
    out: dict[int, tuple[str, str]] = {}
    for dom in DOMAINS:
        key = f"{dom}/{path}"
        if key not in memo:
            rows = cdx(key, fl="timestamp,original,statuscode", collapse="timestamp:4",
                       filter="statuscode:200")
            if rows is None:
                continue
            memo[key] = rows
            write_atomic(memo_f, json.dumps(memo, indent=0))
        for ts, orig, *_ in memo[key]:
            y = int(ts[:4])
            if y0 <= y <= y1 and y not in out:
                out[y] = (ts, orig)
    return out


def all_captures() -> list[list[str]]:
    rows = []
    for dom in DOMAINS:
        f = P.scratch / f"cdx-{dom}.json"
        rows += json.load(open(f))[1:]
    return rows


def put(years: dict, year: int, row: dict) -> None:
    years.setdefault(year, {})
    k = (row["slug"], row["path"])
    years[year].setdefault(k, row)


# ---------------------------------------------------------------- era 1
def era_table1999(years: dict) -> None:
    for page in ("investments.htm", "professional.htm"):
        for y, (ts, orig) in sorted(yearly(page, 1998, 2001).items()):
            body = fetch(ts, orig)
            if body is None:
                continue
            # Two alphabetical sections, information technology then health
            # care: the section turns where the alphabet restarts.
            section, prev = "Information Technology", ""
            n = 0
            for tr in re.findall(r"(?is)<tr[^>]*>(.*?)</tr>", body):
                cells = [clean(c) for c in re.findall(r"(?is)<t[dh][^>]*>(.*?)</t[dh]>", tr)]
                cells = [c for c in cells if c]
                if len(cells) != 3:
                    continue
                name, desc, outcome = cells
                if name.upper() in ("COMPANY", "NAME"):
                    continue
                first = re.sub(r"[^A-Za-z]", "", name)[:1].upper()
                if prev and first and ord(prev) - ord(first) >= 10:
                    section = "Health Care"
                prev = first or prev
                put(years, y, {"slug": slug_of(name), "name": name, "path": f"/{page}",
                               "snapshot_ts": ts, "era": "table1999",
                               "capture_url": f"https://web.archive.org/web/{ts}/{orig}",
                               "description": desc, "site_outcome": outcome,
                               "site_sector": section})
                n += 1
            print(f"  table1999 {page} {y}: {n} rows ({ts})")


# ---------------------------------------------------------------- company pages
def company_page(path_prefix: str, slug: str) -> dict | None:
    """Name and description off the company's own page, first capture."""
    caps = sorted((r[0], r[1]) for r in all_captures()
                  if re.search(rf"/{re.escape(path_prefix)}/{re.escape(slug)}\.html?$",
                               r[1].split("?")[0]) and r[2] == "200")
    if not caps:
        return None
    ts, orig = caps[0]
    body = fetch(ts, orig)
    if body is None:
        return None
    m = re.search(r'(?is)<span class="bodylink">(.*?)</span>(.*?)</td>', body)
    name = desc = ""
    if m:
        name, desc = clean(m.group(1)), clean(m.group(1) + " " + m.group(2))
    else:
        m = re.search(r'(?is)<td class="bodytext">(.*?)</td>', body)
        if m:
            desc = clean(m.group(1))
            b = re.search(r"(?is)<b>(.*?)</b>", m.group(1))
            name = clean(b.group(1)) if b else ""
    if not name:
        alt = re.search(rf'(?is)<img[^>]+src="[^"]*{re.escape(slug)}[^"]*"[^>]*alt="([^"]+)"', body)
        name = clean(alt.group(1)) if alt else ""
    return {"name": name, "description": desc[:600], "ts": ts, "orig": orig}


def era_sectors(years: dict, era: str, pages: dict, y0: int, y1: int,
                link_re: str, prefix_of) -> None:
    seen_pages: dict[tuple[str, str], dict | None] = {}
    for page, sector in pages.items():
        for y, (ts, orig) in sorted(yearly(page, y0, y1).items()):
            body = fetch(ts, orig)
            if body is None:
                continue
            links = sorted(set(re.findall(link_re, body)))
            n = 0
            for prefix, slug in links:
                prefix = prefix_of(page, prefix)
                if slug in ("index",):
                    continue
                key = (prefix, slug)
                if key not in seen_pages:
                    seen_pages[key] = company_page(prefix, slug)
                cp = seen_pages[key]
                name = (cp or {}).get("name") or ""
                row = {"slug": slug_of(name) if name else slug, "path": f"/{prefix}/{slug}.html",
                       "snapshot_ts": ts, "era": era,
                       "capture_url": (f"https://web.archive.org/web/{cp['ts']}/{cp['orig']}" if cp
                                       else f"https://web.archive.org/web/{ts}/{orig}"),
                       "site_sector": sector}
                if name:
                    row["name"] = name
                if cp and cp.get("description"):
                    row["description"] = cp["description"]
                put(years, y, row)
                n += 1
            print(f"  {era} {page} {y}: {n} companies ({ts})")


# ---------------------------------------------------------------- era 4
def era_drupal(years: dict, roster: dict) -> None:
    for page in ("portfolio-full", "portfolio"):
        for y, (ts, orig) in sorted(yearly(page, 2013, 2017).items()):
            body = fetch(ts, orig)
            if body is None:
                continue
            n = 0
            # anchors of the company list, then one block per company
            names = [clean(a) for a in re.findall(r'(?is)<a href="#[^"]*"[^>]*>(.*?)</a>', body)]
            text = clean(re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", body))
            for name in dict.fromkeys(names):
                if not name or name.lower() in ("portfolio", "clear filter"):
                    continue
                md = ""
                i = text.find(name + " " + name)
                if i >= 0:
                    seg = text[i:i + 1500]
                    mm = re.search(r"Managing Director\s*\|?\s*([A-Z][a-z]+ [A-Z][a-z]+)", seg)
                    md = mm.group(1) if mm else ""
                row = {"slug": slug_of(name), "name": name, "path": f"/{page}", "snapshot_ts": ts,
                       "era": "drupal2013", "capture_url": f"https://web.archive.org/web/{ts}/{orig}"}
                if md:
                    row["site_md"] = md
                    rs = roster.get(md.lower())
                    if rs:
                        row["filters"] = rs
                put(years, y, row)
                n += 1
            print(f"  drupal2013 {page} {y}: {n} companies ({ts})")
    for seg, sector in DRUPAL_SECTORS.items():
        for y, (ts, orig) in sorted(yearly(f"portfolio/{seg}", 2013, 2017).items()):
            body = fetch(ts, orig)
            if body is None:
                continue
            names = [clean(a) for a in re.findall(r'(?is)<a href="#[^"]*"[^>]*>(.*?)</a>', body)]
            n = 0
            for name in dict.fromkeys(names):
                if not name or name.lower() in ("portfolio", "clear filter"):
                    continue
                put(years, y, {"slug": slug_of(name), "name": name, "path": f"/portfolio/{seg}",
                               "snapshot_ts": ts, "era": "drupal2013",
                               "capture_url": f"https://web.archive.org/web/{ts}/{orig}",
                               "site_sector": sector})
                n += 1
            print(f"  drupal2013 portfolio/{seg} {y}: {n} companies ({ts})")


def main() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    # "Managing Director | Jeff Bird" -> the roster slug, so the build reads
    # the firm's own deal attribution into partners_site.
    nick = {"Jeffrey": "Jeff", "Michael": "Mike", "Andrew": "Andy", "Samuel": "Sam",
            "James": "Jim", "Gregory": "Greg", "Ronald": "Ron", "Leonard": "Len"}
    roster = {}
    for r in json.load(open(P.wayback / "partner-roster.json")):
        toks = [t.rstrip(".,") for t in r["name"].split()]
        toks = [t for t in toks if t not in ("Jr", "III") and len(t) > 1]
        first, last = toks[0], toks[-1]
        for f in {first, nick.get(first, first)} | ({toks[1], nick.get(toks[1], toks[1])} if len(toks) > 2 else set()):
            roster[f"{f} {last}".lower()] = r["slug"]
    years: dict[int, dict] = {}
    era_table1999(years)
    era_sectors(years, "sector2000", SECTOR2000, 2000, 2003,
                r'href="(soft|mt|nt|it)/([a-z0-9_-]+)\.html?"', lambda page, pre: pre)
    era_sectors(years, "sector2004", {f"{k}/index.html": v for k, v in SECTOR2004.items()}, 2004, 2012,
                r'href="()([a-z0-9_-]+)\.html?"', lambda page, pre: page.split("/")[0])
    era_drupal(years, roster)
    PARSED.mkdir(parents=True, exist_ok=True)
    for y, rows in sorted(years.items()):
        f = PARSED / f"{y}.json"
        old = {(r["slug"], r["path"]): r for r in json.load(open(f))} if f.exists() else {}
        old.update(rows)
        write_atomic(f, json.dumps(sorted(old.values(), key=lambda r: (r["slug"], r["path"])),
                                   indent=1, ensure_ascii=False) + "\n")
        print(f"{y}: {len(old)} rows")
    if FAILURES:
        write_atomic(RAW / "failures.json", json.dumps(FAILURES, indent=1))
        print(f"!! {len(FAILURES)} failed fetches recorded in raw/failures.json; re-run before "
              f"reading any absence", file=sys.stderr)
        sys.exit(3)


if __name__ == "__main__":
    main()
