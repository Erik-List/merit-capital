#!/usr/bin/env python3
"""Read Earlybird's archived site generations into wayback-pull's shapes.

earlybird.com ran five site generations and no generic era parser fits them
(config.json wayback._eras_note). This reads every raw capture on disk:

  Common Crawl   data/filings/commoncrawl/earlybird-venture-capital/<crawl>/...
                 (scratch/cc-cluster.py + scratch/cc-fetch.py; the index
                 records are sources/wayback/cc-index-raw.json)
  Internet Archive  sources/wayback/raw/ia/<ts>-<stem>.html with
                 sources/wayback/raw/ia/manifest.json (scratch/ia_pull.py)
  IA's own index scratch/cdx/earlybird-com-urlkeys.json: the per-company page
                 URLs of 2010-2013 and 2025-2026 exist as captures whether or
                 not their bodies were fetched (first / last capture year).

and writes

  sources/wayback/parsed/<year>.json    one row per company and year:
                                        {slug, name, path, snapshot_ts,
                                         capture_url, invest_year?}
  sources/wayback/archive-evidence.json per company: every dated claim the
                                        firm's own pages made (listed years,
                                        the fund tag Digital West / Digital
                                        East / Health-Tech, Current / Exited,
                                        "investment since", founded, HQ,
                                        description, exit route and date)
  sources/wayback/team-years.json       people -> years seen, team tag,
                                        "Companies I work with"
  sources/web/press-archive.json        the firm's own press releases
                                        2001-2010 (date, title, text)

Every row carries the exact capture it was read from (COLLECTION.md s1: a
capture URL is a valid citation).  Usage: python3 scratch/eb_archive.py
"""
from __future__ import annotations

import hashlib
import html
import json
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[3]
CC_RAW = REPO / "data/filings/commoncrawl/earlybird-venture-capital"
IA_RAW = ROOT / "sources/wayback/raw/ia"
WB = ROOT / "sources/wayback"

MONTHS = {m: i + 1 for i, m in enumerate(
    ["january", "february", "march", "april", "may", "june", "july", "august",
     "september", "october", "november", "december"])}
MONTHS.update({m: i + 1 for i, m in enumerate(
    ["januar", "februar", "märz", "april", "mai", "juni", "juli", "august",
     "september", "oktober", "november", "dezember"])})
MONTHS["maerz"] = 3


def slugify(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def read(path: Path) -> str:
    b = path.read_bytes()
    head = b[:3000].lower()
    if b"charset=utf-8" in head or b'charset="utf-8"' in head:
        return b.decode("utf-8", "replace")
    try:
        return b.decode("utf-8")
    except UnicodeDecodeError:
        return b.decode("cp1252", "replace")


def text_lines(s: str) -> list[str]:
    t = re.sub(r"(?is)<script.*?</script>|<style.*?</style>|<!--.*?-->", "", s)
    t = html.unescape(re.sub(r"<[^>]+>", "\n", t))
    return [l.strip() for l in t.split("\n") if l.strip()]


def clean(s: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def captures():
    """Every capture on disk: (path_on_site, timestamp, capture_url, file)."""
    out = []
    idx = WB / "cc-index-raw.json"
    if idx.exists():
        for cid, v in sorted(json.loads(idx.read_text()).items()):
            for r in v.get("records", []):
                path = re.sub(r"https?://(?:www\.|health\.)?earlybird\.com(?::80)?", "", r["url"])
                stem = re.sub(r"[^A-Za-z0-9._-]+", "_", path.strip("/")) or "root"
                if len(stem) > 120:
                    stem = stem[:100] + "-" + hashlib.sha1(stem.encode()).hexdigest()[:10]
                f = CC_RAW / cid / f"{r['timestamp']}-{stem}.html"
                if f.exists() and f.stat().st_size > 200:
                    out.append((path or "/", r["timestamp"],
                                f"https://index.commoncrawl.org/{cid}-index?url={quote(r['url'], safe='')}&output=json",
                                f, "health." in r["url"]))
    man = IA_RAW / "manifest.json"
    if man.exists():
        for key, m in json.loads(man.read_text()).items():
            f = IA_RAW / key
            if m.get("status") == "ok" and f.exists() and f.stat().st_size > 200:
                path = re.sub(r"https?://(?:www\.|health\.)?earlybird\.com(?::80)?", "", m["original"])
                out.append((path or "/", m["timestamp"],
                            f"https://web.archive.org/web/{m['timestamp']}/{m['original']}",
                            f, "health." in m["original"]))
    return out


class Book:
    """Per-company evidence, keyed loosely on the name."""

    def __init__(self):
        self.co: dict[str, dict] = {}
        self.rows: dict[tuple[str, int], dict] = {}   # (key, year) -> parsed row

    @staticmethod
    def key(name: str) -> str:
        n = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode().lower()
        n = re.sub(r"\((formerly|ex|former)[^)]*\)", " ", n)
        n = re.sub(r"\b(gmbh|ag|inc|ltd|limited|s\.?a\.?s?|s\.p\.a|spa|ab|plc|corp|co|kg|se|oy|bv|b\.v|llc|technologies|technology)\b\.?", " ", n)
        n = re.sub(r"\.(com|de|net|io|ai)\b", " ", n)
        return re.sub(r"[^a-z0-9]+", "", n) or re.sub(r"[^a-z0-9]+", "", name.lower())

    def add(self, name: str, ts: str, path: str, capture_url: str, surface: str, **facts):
        name = re.sub(r"\s+", " ", name).strip(" ,;·")
        if not name or len(name) > 90:
            return
        k = self.key(name)
        c = self.co.setdefault(k, {"names": {}, "years": {}, "claims": []})
        c["names"][name] = c["names"].get(name, 0) + 1
        year = int(ts[:4])
        c["years"].setdefault(str(year), surface)
        facts = {a: b for a, b in facts.items() if b not in (None, "", [], {})}
        if facts:
            c["claims"].append({"ts": ts, "surface": surface, "capture_url": capture_url, **facts})
        row = self.rows.get((k, year))
        if row is None or ts < row["snapshot_ts"]:
            self.rows[(k, year)] = {"slug": slugify(name), "name": name, "path": path,
                                    "snapshot_ts": ts, "capture_url": capture_url}
        iy = facts.get("invest_year")
        if iy:
            r = self.rows[(k, year)]
            r["invest_year"] = min(int(iy), int(r.get("invest_year") or iy))


# ---- page parsers -----------------------------------------------------

def p_az(s, ts, path, cap, book: Book):
    """2002-2010 A-Z list: <b id="klein">NAME</b><br>CITY ... site ... description."""
    n = 0
    for m in re.finditer(
            r'(?is)<b id="?klein"?>(?P<name>.*?)</b>\s*<br>\s*(?P<city>[^<]*)</td>(?P<rest>.*?)</tr>', s):
        name, city = clean(m.group("name")), clean(m.group("city"))
        rest = m.group("rest")
        site = re.search(r'href="(https?://[^"]+)"', rest)
        tds = [clean(x) for x in re.findall(r"(?is)<td[^>]*valign=top[^>]*>(.*?)</td>", rest)]
        desc = tds[-1] if tds else None
        if desc and site and desc.replace("www.", "") in site.group(1):
            desc = None
        book.add(name, ts, path, cap, "a_z", hq=city, website=site.group(1) if site else None,
                 description=desc)
        n += 1
    return n


def p_recent(s, ts, path, cap, book: Book):
    """2002-2010 'recent investments': Name · City | Month Year | text."""
    L = text_lines(s)
    n = 0
    for i, l in enumerate(L[:-1]):
        m = re.match(r"^(?P<name>[^·|]{2,60})\s*·\s*(?P<city>.+)$", l)
        d = re.match(r"^(?P<mon>[A-Za-zä]+)\s+(?P<y>(?:19|20)\d\d)$", L[i + 1])
        if m and d and d.group("mon").lower() in MONTHS:
            book.add(m.group("name"), ts, path, cap, "recent", hq=m.group("city").strip(),
                     recent_listed="%s-%02d" % (d.group("y"), MONTHS[d.group("mon").lower()]),
                     description=L[i + 2] if i + 2 < len(L) else None)
            n += 1
    return n


def p_exits(s, ts, path, cap, book: Book):
    """2005-2010 exit lists: Month Year | Company | site | route."""
    L = text_lines(s)
    kind = "ipo" if "ipos" in path else "trade_sale"
    n = 0
    for i, l in enumerate(L):
        d = re.match(r"^(?P<mon>[A-Za-zä]+)\s+(?P<y>(?:19|20)\d\d)$", l)
        if not d or d.group("mon").lower() not in MONTHS or i + 2 >= len(L):
            continue
        name = L[i + 1]
        tail = L[i + 2:i + 4]
        route = next((t for t in tail if not t.lower().startswith("www.")), None)
        book.add(name, ts, path, cap, "exits", exit_kind=kind, exit_route=route,
                 exit_date="%s-%02d" % (d.group("y"), MONTHS[d.group("mon").lower()]))
        n += 1
    return n


def p_2010(s, ts, path, cap, book: Book):
    """2010-2013 TYPO3 pages: the left menu lists every company of the desk; the
    page itself gives 'Earlybird investment since YYYY'."""
    n = 0
    for href, inner in re.findall(
            r'(?is)<a[^>]+href="[^"]*?((?:en/companies|de/unternehmen)/(?:tech|health-tech)/(?:portfolio|exited)/[^"]+\.html)"[^>]*>(.*?)</a>', s):
        alt = re.search(r'alt="([^"]+)"', inner)
        name = clean(inner) or (alt.group(1) if alt else "")
        if not name or name.upper() in ("PORTFOLIO", "EXITED", "TECH", "HEALTH TECH", "DEUTSCH",
                                        "ENGLISH", "ITALIANO", "WANT TO READ MORE?"):
            continue
        desk = "health-tech" if "/health-tech/" in href else "tech"
        status = "Exited" if "/exited/" in href else "Current"
        if name.isupper():
            name = name.title() if len(name) > 4 else name
        book.add(name, ts, "/" + href, cap, "2010-nav", desk_tag=desk, status_tag=status,
                 page_slug=href.rsplit("/", 1)[-1][:-5])
        n += 1
    m = re.search(r"(?is)<h1[^>]*>(.*?)</h1>", s)
    L = text_lines(s)
    since = next((re.search(r"(?:investment since|Investment seit|investiert seit)\s+((?:19|20)\d\d)", l, re.I)
                  for l in L if re.search(r"(?:investment since|Investment seit|investiert seit)", l, re.I)), None)
    if since and re.search(r"/(portfolio|exited)/[^/]+\.html", path):
        title = next((l for l in L if l.startswith("EARLYBIRD") is False and re.search(r"Venture Capital:\s*(.+)", l)), None)
        nm = re.search(r"Venture Capital:\s*(.+)", title).group(1) if title else None
        if not nm and m:
            nm = clean(m.group(1))
        if nm:
            if nm.isupper():
                nm = nm.title()
            i = next((k for k, l in enumerate(L) if "investment since" in l.lower() or "seit" in l.lower()), 0)
            book.add(nm, ts, path, cap, "2010-page", invest_year=int(since.group(1)),
                     desk_tag="health-tech" if "/health-tech/" in path else "tech",
                     status_tag="Exited" if "/exited/" in path else "Current",
                     description=" ".join(L[i + 1:i + 3])[:600])
            n += 1
    return n


def p_strip(s, ts, path, cap, book: Book):
    """2014-2017 one-page site: <ul class="companies-strip"> logo list."""
    n = 0
    for cls, site, name, desc in re.findall(
            r"""(?is)<li class=['"]([^'"]*)['"]>\s*<a href=['"]([^'"]*)['"][^>]*>\s*<img title=['"]([^'"]+)['"][^>]*>\s*<p>(.*?)</p>""", s):
        tag = cls.replace("active", "").strip()
        book.add(html.unescape(name), ts, path, cap, "2014-strip", website=site,
                 description=clean(desc), sector_tag=tag)
        n += 1
    return n


def p_wp(s, ts, path, cap, book: Book):
    """2018-2024 WordPress /portfolio: one <li class="company"> per company with the
    firm's own Status and Team (fund) tags and a Milestones block."""
    n = 0
    for m in re.finditer(r'(?is)<li class="company[^"]*"(?P<attrs>[^>]*)>(?P<body>.*?)(?=<li class="company|</ul>\s*</section|$)', s):
        attrs, body = m.group("attrs"), m.group("body")
        a = dict(re.findall(r'data-(location|status|industry|tag)="([^"]*)"', attrs))
        nm = re.search(r'<img class="company-logo"[^>]*alt="([^"]*)"', body)
        if not nm or not nm.group(1).strip():
            continue
        mil = re.search(r"(?is)Milestones</p>\s*<p>(.*?)</p>", body)
        founded = invested = None
        if mil:
            t = clean(mil.group(1).replace("<br />", " | ").replace("<br>", " | "))
            f = re.search(r"Founded:\s*((?:19|20)\d\d)", t)
            i = re.search(r"Invested:\s*((?:19|20)\d\d)", t)
            founded, invested = (int(f.group(1)) if f else None), (int(i.group(1)) if i else None)
            exit_m = re.search(r"(Exit(?:ed)?|IPO|Acquired)[^|]*", t)
        else:
            t, exit_m = None, None
        hq = re.search(r'(?is)<p class="title">HQ</p>\s*<p>(.*?)</p>', body)
        fo = re.search(r'(?is)<p class="title">Founders?</p>\s*<p>(.*?)</p>', body)
        site = re.search(r'icon-website"><a href="([^"]*)"', body)
        tagline = re.search(r'(?is)<div class="companies_baseline[^>]*>\s*<p>(.*?)</p>', body)
        desc = re.search(r'(?is)<div class="lightbox-body--main">(.*?)</div>\s*</div>', body)
        tags = re.findall(r'<span class="will-go-away">([^<]*)</span>', body)
        book.add(html.unescape(nm.group(1)), ts, path, cap, "wp-portfolio",
                 desk_tag=a.get("tag") or (tags[0] if tags else None), status_tag=a.get("status"),
                 industry=a.get("industry"), location=a.get("location"),
                 founded=founded, invest_year=invested, milestones=t,
                 hq=clean(hq.group(1)) if hq else None,
                 founders=clean(fo.group(1).replace("<br />", ", ")) if fo else None,
                 website=site.group(1) if site else None,
                 tagline=clean(tagline.group(1)) if tagline else None,
                 description=clean(desc.group(1))[:700] if desc else None)
        n += 1
    return n


def p_framer(s, ts, path, cap, book: Book, health=False):
    """2025- Framer: the list page's anchors and each company page's text."""
    n = 0
    surface = "framer-health" if health else "framer"
    if re.fullmatch(r"/companies/?", path.split("?")[0]):
        for slug, inner in re.findall(r'(?is)<a[^>]+href="\./companies/([^"]+)"[^>]*>(.*?)</a>', s):
            parts = [p.strip() for p in html.unescape(re.sub(r"<[^>]+>", "|", inner)).split("|") if p.strip()]
            if not parts:
                continue
            rest = [p for p in parts[1:] if p != "Spotlights"]
            status = rest[0] if rest and rest[0] in ("Active", "Exit") else None
            stage = next((p for p in rest if p in ("Pre-Seed", "Seed", "Series A", "Series B", "Series C", "Growth")), None)
            book.add(parts[0], ts, f"/companies/{slug}", cap, surface + "-list", status_tag=status,
                     stage_site=stage, desk_tag="health" if health else None)
            n += 1
        return n
    m = re.match(r"/companies/([^/?#]+)", path)
    if not m:
        return 0
    L = text_lines(s)
    h1 = re.findall(r"(?is)<h1[^>]*>(.*?)</h1>", s)
    names = [clean(x) for x in h1 if clean(x) and clean(x).upper() not in ("ABOUT US", "PORTFOLIO", "APPROACH", "PERSPECTIVES", "JOBS")]
    if not names:
        return 0
    txt = " | ".join(L)
    f = re.search(r"Founded:\s*((?:19|20)\d\d)", txt)
    i = re.search(r"Invested:\s*((?:19|20)\d\d)", txt)
    marker = "Digital East Fund" if "Digital East Fund*" in txt else None
    team = None
    if "Investment Team" in L:
        k = L.index("Investment Team")
        team = [x for x in L[k + 1:k + 6] if x not in ("THE PORTFOLIO", "SIMILAR COMPANIES", "Digital East Fund*") and len(x) < 40][:4]
        stop = next((j for j, x in enumerate(L[k + 1:k + 6]) if x in ("THE PORTFOLIO", "Digital East Fund*")), None)
        if stop is not None:
            team = L[k + 1:k + 1 + stop]
    hq = L[L.index("HQ") + 1] if "HQ" in L and L.index("HQ") + 1 < len(L) else None
    book.add(names[-1], ts, path, cap, surface + "-page", founded=int(f.group(1)) if f else None,
             invest_year=int(i.group(1)) if i else None, fund_marker=marker, hq=hq,
             partners_site=team, desk_tag="digital-east" if marker else ("health" if health else None))
    return 1


def p_team(s, ts, path, cap, team: dict):
    """2018-2024 WordPress /team: one card per person with Office / Team / Companies I work with."""
    L = text_lines(s)
    n = 0
    for k, l in enumerate(L):
        if l != "Office" or k + 3 >= len(L):
            continue
        # walk back to the person's name: the card starts "Name | Title | Name | Title"
        name = title = None
        for j in range(k - 1, max(k - 60, 1), -1):
            if j + 2 < len(L) and L[j] == L[j + 2] and len(L[j]) < 40 and j + 3 < len(L) and L[j + 1] == L[j + 3]:
                name, title = L[j], L[j + 1]
                break
        if not name:
            continue
        seg = L[k:k + 12]
        tag = seg[seg.index("Team") + 1] if "Team" in seg and seg.index("Team") + 1 < len(seg) else None
        comp = seg[seg.index("Companies I work with") + 1] if "Companies I work with" in seg and seg.index("Companies I work with") + 1 < len(seg) else None
        p = team.setdefault(name, {"years": set(), "titles": {}, "team_tags": {}, "companies": {}})
        y = int(ts[:4])
        p["years"].add(y)
        if title:
            p["titles"][str(y)] = title
        if tag:
            p["team_tags"][str(y)] = tag
        if comp:
            p["companies"][str(y)] = comp
        p.setdefault("capture_urls", {})[str(y)] = cap
        n += 1
    return n


def p_press(s, ts, path, cap, press: dict):
    """The firm's own press releases 2001-2010 (and its portfolio-news posts)."""
    m = re.search(r"/(en|de)/press/(release|portfolio)/(\d+)", path)
    if not m:
        return 0
    L = text_lines(s)
    body = [l for l in L if not l.startswith("EARLYBIRD") and l != "Venture Capital"]
    if len(body) < 3:
        return 0
    date, k = None, None
    for j, l in enumerate(body[:4]):
        d = re.match(r"^(?:[A-Za-z]+,?\s+)?([A-Za-zä]+)\s+(\d{1,2}),\s*((?:19|20)\d\d)$", l) or \
            re.match(r"^(?:[A-Za-z]+,?\s+)?(\d{1,2})\.\s*([A-Za-zä]+)\s+((?:19|20)\d\d)$", l)
        if d:
            g = d.groups()
            mon, day, yr = (g[0], g[1], g[2]) if g[0].lower() in MONTHS else (g[1], g[0], g[2])
            if mon.lower() in MONTHS:
                date = "%s-%02d-%02d" % (yr, MONTHS[mon.lower()], int(day))
                k = j
                break
    title = body[k + 1] if k is not None and k + 1 < len(body) else body[0]
    text = " ".join(body[k + 2:] if k is not None else body[1:])
    text = re.split(r"\s(?:Print version|Druckversion|back to overview|zurück zur Übersicht)\b", text)[0]
    key = f"{m.group(1)}/{m.group(2)}/{m.group(3)}"
    if key not in press or ts < press[key]["snapshot_ts"]:
        press[key] = {"lang": m.group(1), "kind": m.group(2), "id": int(m.group(3)), "date": date,
                      "title": title, "text": text[:6000], "path": path, "snapshot_ts": ts,
                      "capture_url": cap}
    return 1


# A page's URL slug is not the company's name (COLLECTION.md s5: "the site's own
# rendering owns name and slug"); these map the firm's own page slugs onto the
# name the same site renders elsewhere, so an index-only page joins its row.
PAGE_SLUG_ALIAS = {
    "alantos-pharmaceuticals": "alantos-pharmaceuticals-ag", "calypso": "calypso-medical",
    "mikini-media": "mikini-media-gmbh", "music-networx": "music-networx-gmbh",
    "urbiacom": "urbia", "urbia-com": "urbia", "zonare": "zonare-inc",
    "aleph-alpha2": "aleph-alpha", "go-deed-inc": "deed", "m-0": "m0", "m-zero": "m0",
    "snyk-limited": "snyk", "ubitricty": "ubitricity", "tastyurban": "tastyurban-gmbh",
    "terralayr-ag": "terralayr", "isar-aerospace-technologies-gmbh": "isar-aerospace",
    "crossenagage": "crossengage", "gittigidiyor": "gitti-gidiyor",
    "propertyfinder-ae": "propertyfinder", "yemeksepeti": "yemek-sepeti",
    "alokai-(formerly-vue-storefront)": "alokai-formerly-vue-storefront",
    "crosslend-gmbh-(the-thing-gmbh)": "crosslend-gmbh-the-thing-gmbh",
    "obligate-(ex-fqx)": "obligate-ex-fqx", "sennder-gmbh-(ex-everoad-s-a-s-)": "sennder",
    "simr-s-(formerly-ubercloud)": "simr",
    # 2001-2010 page slugs
    "novasonics": "zonare-inc", "esmertec": "esmertec-ag", "music-networx": "music-networx-gmbh",
    "therascope": "alantos-pharmaceuticals-ag", "clean-mobile": "clean-mobile-ag",
    "light-blue-optics": "light-blue-optics-ltd", "sidec": "sidec-technologies-ab", "upek": "upek-inc",
    "scoreloop": "scoreloop-ag", "smoodoos": "smoodoos-com", "mergeoptics": "mergeoptics-gmbh",
    "lumics": "lumics-gmbh", "conject": "conject-ag", "entelos": "entelos-inc", "alantos": "alantos-pharmaceuticals-ag",
    "mikini-media": "mikini-media-gmbh", "purple-labs": "purple-labs-s-a", "bmeye": "bmeye",
}


def from_cdx_index(book: Book):
    """Per-company page URLs the Internet Archive holds (bodies not needed for the
    listing fact): 2010-2013 TYPO3 pages and 2025-2026 Framer pages."""
    f = ROOT / "scratch/cdx/earlybird-com-urlkeys.json"
    if not f.exists():
        return 0
    n = 0
    for original, ts, ets, _gc, _sc, _mt in json.loads(f.read_text())[1:]:
        path = re.sub(r"^https?://(www\.)?earlybird\.com(:80)?", "", original).split("?")[0]
        m = re.match(r"/en/companies/(tech|health-tech)/(portfolio|exited)/([^/]+)\.html$", path)
        fr = re.match(r"/companies/([^/]+)$", path)
        old = re.match(r"/(?:en|de)/portfolio/(recent|investment)/([a-z0-9_]+)(?:/|\.html)$", path)
        if old and old.group(2) in ("index", "index_left", "index_left_02", "index_left_03"):
            old = None
        if old:
            # 2001-2010: one page per company under "recent investments" and (2001)
            # "investment". The page existed and was captured; its body names the
            # company once the Internet Archive serves it again.
            for year in range(int(ts[:4]), int(ets[:4]) + 1):
                stamp = ts if year == int(ts[:4]) else f"{year}0101000000"
                book.index_rows.append({"era": "2001", "page_slug": old.group(2).replace("_", "-"), "year": year,
                                        "path": path, "snapshot_ts": stamp,
                                        "capture_url": f"https://web.archive.org/web/{stamp}/{original}"})
                n += 1
            continue
        if not m and not fr:
            continue
        for year in range(int(ts[:4]), int(ets[:4]) + 1):
            stamp = ts if year == int(ts[:4]) else f"{year}0101000000"
            cap = f"https://web.archive.org/web/{stamp}/{original}"
            if m:
                k_slug = m.group(3)
                book.index_rows.append({"era": "2010", "page_slug": k_slug, "year": year, "path": path,
                                        "snapshot_ts": stamp, "capture_url": cap,
                                        "desk_tag": m.group(1), "status_tag": "Exited" if m.group(2) == "exited" else "Current"})
            else:
                book.index_rows.append({"era": "framer", "page_slug": fr.group(1), "year": year, "path": path,
                                        "snapshot_ts": stamp, "capture_url": cap})
            n += 1
    return n


def main() -> None:
    book = Book()
    book.index_rows = []
    team: dict[str, dict] = {}
    press: dict[str, dict] = {}
    stats = defaultdict(int)
    for path, ts, cap, f, health in captures():
        p = path.split("?")[0]
        try:
            s = read(f)
        except OSError:
            continue
        if re.search(r"/(en|de)/portfolio/a_z", p):
            stats["a_z"] += p_az(s, ts, p, cap, book)
        elif re.search(r"/(en|de)/portfolio/recent/?$", p):
            stats["recent"] += p_recent(s, ts, p, cap, book)
        elif re.search(r"/(en|de)/exits/(ipos|trade_sales)", p):
            stats["exits"] += p_exits(s, ts, p, cap, book)
        elif re.search(r"/(en/companies|de/unternehmen)", p):
            stats["2010"] += p_2010(s, ts, p, cap, book)
        elif re.search(r"/(en|de)/press/", p):
            stats["press"] += p_press(s, ts, p, cap, press)
        elif re.fullmatch(r"/?(en|de)?/?(index\.(php|html))?", p) and "companies-strip" in s:
            stats["strip"] += p_strip(s, ts, p or "/", cap, book)
        elif re.fullmatch(r"/portfolio/?", p):
            stats["wp"] += p_wp(s, ts, p, cap, book)
        elif re.fullmatch(r"/team/?", p):
            stats["team"] += p_team(s, ts, p, cap, team)
        elif p.startswith("/companies"):
            stats["framer"] += p_framer(s, ts, p, cap, book, health)
    stats["cdx-index"] = from_cdx_index(book)

    # per-company pages known from the index: attach to the company whose page
    # slug or name key they match, else create a slug-named row (no name: the
    # builder treats a slug-derived display as provisional)
    slug_to_key = {}
    for k, c in book.co.items():
        for cl in c["claims"]:
            if cl.get("page_slug"):
                slug_to_key[cl["page_slug"]] = k
        for nm in c["names"]:
            slug_to_key.setdefault(slugify(nm), k)
    unnamed = {}
    for r in book.index_rows:
        ps = PAGE_SLUG_ALIAS.get(r["page_slug"], r["page_slug"])
        k = slug_to_key.get(ps) or slug_to_key.get(re.sub(r"-(gmbh|ag|inc|ltd|sa|s-a-s)$", "", ps)) \
            or (Book.key(ps.replace("-", " ")) if Book.key(ps.replace("-", " ")) in book.co else None)
        if k:
            c = book.co[k]
            c["years"].setdefault(str(r["year"]), "ia-index")
            name = max(c["names"], key=c["names"].get)
            if (k, r["year"]) not in book.rows:
                book.rows[(k, r["year"])] = {"slug": slugify(name), "name": name, "path": r["path"],
                                             "snapshot_ts": r["snapshot_ts"], "capture_url": r["capture_url"]}
        else:
            unnamed.setdefault((ps, r["year"]), {"slug": ps, "path": r["path"],
                                                 "snapshot_ts": r["snapshot_ts"],
                                                 "capture_url": r["capture_url"]})

    by_year: dict[int, list] = defaultdict(list)
    for (k, year), row in book.rows.items():
        by_year[year].append(row)
    for (ps, year), row in unnamed.items():
        by_year[year].append(row)
    (WB / "parsed").mkdir(parents=True, exist_ok=True)
    for old in (WB / "parsed").glob("*.json"):
        old.unlink()
    for year, rows in sorted(by_year.items()):
        rows.sort(key=lambda r: r["slug"])
        (WB / "parsed" / f"{year}.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False) + "\n")

    ev = {}
    for k, c in sorted(book.co.items()):
        name = max(c["names"], key=c["names"].get)
        ev[k] = {"name": name, "names": sorted(c["names"]), "years": dict(sorted(c["years"].items())),
                 "claims": sorted(c["claims"], key=lambda x: x["ts"])}
    (WB / "archive-evidence.json").write_text(json.dumps({
        "_readme": "Per company, every dated claim Earlybird's own archived pages made, each with its capture. Written by scratch/eb_archive.py.",
        "companies": ev,
        "index_only_slugs": sorted({ps for ps, _ in unnamed})}, indent=1, ensure_ascii=False) + "\n")
    (WB / "team-years.json").write_text(json.dumps({
        "_readme": "People on the archived /team pages (2018-2024): years seen, the site's own Team tag (Digital West / Digital East / Health-Tech / Operations), title and 'Companies I work with'.",
        "people": {n: sorted(p["years"]) for n, p in sorted(team.items())},
        "detail": {n: {"titles": p["titles"], "team_tags": p["team_tags"], "companies": p["companies"],
                       "capture_urls": p.get("capture_urls", {})} for n, p in sorted(team.items())}},
        indent=1, ensure_ascii=False) + "\n")
    (ROOT / "sources/web").mkdir(exist_ok=True)
    (ROOT / "sources/web/press-archive.json").write_text(json.dumps({
        "_readme": "Earlybird's own press pages 2001-2010 (/en|de/press/release/<id> the firm's releases, /press/portfolio/<id> its portfolio news), read from archived captures by scratch/eb_archive.py.",
        "items": sorted(press.values(), key=lambda x: (x["date"] or "", x["id"]))}, indent=1, ensure_ascii=False) + "\n")
    print(dict(stats))
    print(f"companies: {len(ev)}  index-only page slugs: {len({ps for ps, _ in unnamed})}  "
          f"years: {min(by_year) if by_year else '-'}-{max(by_year) if by_year else '-'}  "
          f"people: {len(team)}  press items: {len(press)}")
    for year in sorted(by_year):
        print(f"  {year}: {len(by_year[year])}")


if __name__ == "__main__":
    main()
