#!/usr/bin/env python3
"""Parse the archived bvp.com portfolio captures into sources/wayback/parsed/<year>.json (the shape
build-company-base.py reads: slug, name, path, snapshot_ts, capture_url, filters) plus the firm's own fields per
row (invest_year, exit_year, about, partners, sectors, geography, acquirer, ticker, fka).

Captures: Common Crawl (sources/wayback/cc-manifest.json, bodies under data/filings/commoncrawl/<slug>/) and the
Internet Archive (sources/wayback/ia-manifest.json, bodies under data/filings/commoncrawl/<slug>/ia/). Every row
carries its own capture URL (COLLECTION.md s1: a capture URL is a valid citation).

Site generations (one domain, bvp.com):
  aspx-list    2008-2012  /Portfolio/Portfolio.aspx: the firm's whole investment list as (year, name) rows with a
                          per-company id (portanchorNNNN), back to 1957
  aspx-desc    2008-2012  every /Portfolio/*.aspx wrapper embeds <div class="desc" link="Team/Default.aspx?id=A;B"
                          id="desc_NNNN"> blocks: the firm's own description and the deal partners' ids, joined to
                          aspx-list on the company id
  aspx-exits   2008-2012  /Portfolio/Report_Frame.aspx: "Top 50 Exits", name | website | partner | paragraph
  drupal-list  2012-2019  /portfolio: <dd id="portcoNN"> cards with Investment Year, Exit Year, Sector, Geography
  drupal-page  2012-2019  /portfolio/<slug>: description and the "Team" (deal partners)
  wp-*         2019-2026  /companies and /companies/<slug> (parsed by the handlers below once read)

A name is stored as the firm rendered it minus its parenthetical ("Skype Technologies (acq. by eBay)" is Skype
Technologies with acquirer eBay; "Yodle (fka NatPal)" is Yodle with fka NatPal; "(NASDAQ:SIRT)" is a ticker).
Usage: python3 bvp-parse.py
"""
from __future__ import annotations

import collections
import html
import json
import re
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

P = Paths("bessemer-venture-partners")
RAW = ROOT / "data" / "filings" / "commoncrawl" / "bessemer-venture-partners"
OUT = P.wayback / "parsed"
NON_COMPANY = {"antiportfolio", "anti-portfolio", "top-exits", "topexits", "default", "portfolio", "report",
               "report_frame", "antiportfolio_frame", "investments", "exits", "all", "feed", "page"}


def slugify(name: str) -> str:
    folded = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", folded.lower().replace("&", " and ").replace("'", "")).strip("-")


def strip_tags(s: str) -> str:
    s = re.sub(r"<(script|style)[\s\S]*?</\1>", " ", s or "", flags=re.I)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).replace("\xa0", " ").strip()


PAREN = re.compile(r"\s*\(([^)]*)\)")


def split_name(raw: str) -> dict:
    """The firm's rendering -> clean name + what its parentheticals say."""
    raw = html.unescape(raw or "").replace("\xa0", " ").strip()
    out = {"name_as_listed": raw}
    name = raw
    for m in PAREN.finditer(raw):
        p = m.group(1).strip()
        low = p.lower()
        if re.match(r"acq(\.|uired)?\s*(by)?\b", low):
            out["acquirer"] = re.sub(r"(?i)^acq(\.|uired)?\s*(by)?\s*", "", p).strip()
        elif re.match(r"(nasdaq|nyse|amex|lse|bse|nse|aim|tsx|otc)[ :]", low):
            out["ticker"] = p
        elif re.match(r"(fka|f/k/a|formerly|aka|nka|now)\b", low):
            out["fka"] = re.sub(r"(?i)^(fka|f/k/a|formerly|aka|nka|now)\s*", "", p).strip()
        else:
            continue
        name = name.replace(m.group(0), " ")
    out["name"] = re.sub(r"\s+", " ", name).strip(" ,")
    return out


LEGAL = re.compile(r",?\s+(inc|incorporated|corp|corporation|ltd|limited|llc|plc|co|company|pvt|private|gmbh|s\.?a|n\.?v|b\.?v)\.?$", re.I)


def base_name(name: str) -> str:
    n = name
    for _ in range(3):
        n = LEGAL.sub("", n).strip(" ,.")
    return n or name


def nkey(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", unicodedata.normalize("NFKD", base_name(name)).encode("ascii", "ignore").decode().lower().replace("&", "and"))


# One company under two names on the firm's own lists across site generations, read from the listings themselves
# ("Determina (fka Araksha)", "Medsite.com (fka American Medical Communications)") or from the record (a rename, a
# merger of equals). Old rendering -> the name the later lists carry.
# 1999-2001 pages print a listed company's exchange symbol where its name would be (the name is in the logo
# image): symbol -> the company the entry's own sentence describes.
TICKER_NAMES = {"CMGI": "Flycast", "HOTJ": "HotJobs", "KEYN": "Keynote Systems", "MDRX": "Allscripts", "MSPG": "Mindspring",
                "NEWZ": "Individual", "NTGX": "NetGenesis", "ONTC": "ON Technology", "PSIX": "PSINet", "RCOM": "Register.com",
                "SONS": "Sonus Networks", "SQST": "SciQuest.com", "TLCT": "Telocity", "TMWD": "Tumbleweed",
                "VNWI": "VIA NET.WORKS", "VRIO": "Verio", "VRSN": "VeriSign", "VRYA": "ViryaNet", "VSVR": "VideoServer",
                "WCOM": "Unipalm", "WTLK": "Worldtalk", "CIEN": "Ciena", "ITCD": "ITC DeltaCom", "MAKR": "Maker Communications",
                "QEDI": "Quantum Effect Devices", "FCST": "Flycast", "ELNK": "Mindspring"}

ALIASES = {
    "ART Advanced Recognition Technologies": "Advanced Recognition Technologies",
    "Advanced Memory Systems": "Intersil/Advanced Memory Systems",
    "Allscripts Healthcare Solutions": "Allscripts",
    "Fort James": "James River",                       # James River merged with Fort Howard into Fort James (1997)
    "James River Corp. of Virginia": "James River",
    "IPC": "IPC The Hospitalist",                      # listed as InPatient Consultants Management
    "Motilal Oswal Financial Services": "Motilal Oswal",
    "TriNet Group": "Trinet",
    "T3Ci": "Retail Solutions",
    "AIT Group": "Portrait Software",                  # AIT Group plc renamed Portrait Software (2004)
    "Araksha": "Determina",
    "hyperNOC": "Sequation",
    "Vestmark": "LifeHarbor",                          # "Vestmark (mgr with LifeHarbor)"
    "Medsite.com": "American Medical Communications",
    "SWsoft": "Parallels",                             # SWsoft renamed Parallels (2008)
    "Visto": "Good Technology",                        # Visto bought Good Technology (2009) and took its name
    "Allscripts Pharmaceuticals": "Allscripts",
    "BeachFire Technologies": "Beachfire",
    "BlueNile.com": "Blue Nile",
    "Counterpane Systems": "Counterpane",
    "EXP.com": "EXP Systems",
    "ePIT": "ePIT Systems",
    "Metapath Software International": "Metapath",
    "National Transportation Exchanges": "NTE",
    "PSI": "PSINet",
    "QUALYS Technologies": "Qualys",
    "Quantum Effect Design": "Quantum Effect Devices",
    "THINQ": "Thinq Learning Solutions",
    "TrainingNet.com": "Thinq Learning Solutions",      # "THINQ, originally TrainingNet"
    "The Extraprise Group": "Extraprise",
    "Zones.com": "Zones",
    "NewsEdge": "Individual",                           # "BVP invested in Individual, which was later acquired" (NewsEdge)
    "Hotjobs": "HotJobs",
    "Vestmark (mgr with LifeHarbor)": "LifeHarbor",
    "ezenia!": "VideoServer",                           # VideoServer renamed itself Ezenia! (1999)
    "Catena Technologies": "Catena Networks",
}


def regroup(rows):
    """One company, one name: rows that share the firm's own per-company id or URL slug across years (aspx
    portanchor id, Drupal node id, Drupal /portfolio/<slug>, WordPress /companies/<slug>) or the same name minus a
    legal suffix are one company. The group takes the live site's name where the live list carries it, else its
    most recent archived rendering minus the legal suffix; the rendering the firm used at the time stays on the row
    as name_as_listed. Fixed here, in the parsed source, so no junk name survives as a merge duplicate
    (COLLECTION.md s5, First Round)."""
    live = json.loads((P.site / "company-list.json").read_text())
    parent: dict = {}

    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    def keys(r):
        ks = [("name", nkey(r["name"]))]
        if r.get("bvp_id"):
            ks.append(("aspx", r["bvp_id"]))
        if r.get("asp_id"):
            ks.append(("asp", r["asp_id"]))
        if r.get("drupal_id"):
            ks.append(("dnode", r["drupal_id"]))
        if r.get("site_slug"):
            ks.append((("wslug" if r["era"] in ("wp-list", "live") else "dslug"), r["site_slug"]))
        return ks

    for c in live:
        r = {"name": c["name"], "era": "live", "site_slug": c["site_slug"]}
        ks = keys(r)
        leg = (c.get("legacy_url") or "").rstrip("/").rsplit("/", 1)[-1]
        if leg:
            ks.append(("wslug", leg))
        for k in ks[1:]:
            union(ks[0], k)
    for y in rows:
        for r in rows[y].values():
            ks = keys(r)
            for k in ks[1:]:
                union(ks[0], k)
    for old, new in ALIASES.items():
        union(("name", nkey(new)), ("name", nkey(old)))
    # The 2012-2015 site (era drupal-list) printed the investment year one year early wherever the stored date was a
    # January 1 placeholder (a time-zone shift in its date formatter: Staples reads 1985 there and 1986 on every
    # other generation, Ciena 1994 against 1995). Where every other generation of the firm's list agrees on Y+1, the
    # drupal-list year is corrected to it and the printed year is kept as invest_year_as_printed.
    era_years = collections.defaultdict(lambda: collections.defaultdict(set))
    for y in rows:
        for r in rows[y].values():
            if r.get("invest_year"):
                era_years[find(("name", nkey(r["name"])))][r["era"]].add(int(r["invest_year"]))
    shifted = 0
    for y in rows:
        for r in rows[y].values():
            if r["era"] != "drupal-list" or not r.get("invest_year"):
                continue
            e = era_years[find(("name", nkey(r["name"])))]
            others = set().union(*[v for k, v in e.items() if k not in ("drupal-list", "asp-success")])
            d = int(r["invest_year"])
            if others == {d + 1}:
                r["invest_year_as_printed"], r["invest_year"] = str(d), str(d + 1)
                shifted += 1
    print(f"drupal-list years corrected by one (January 1 placeholder): {shifted} rows")
    live_name = {find(("name", nkey(c["name"]))): c["name"] for c in live}
    latest: dict = {}
    for y in sorted(rows):
        for r in rows[y].values():
            g = find(("name", nkey(r["name"])))
            latest[g] = (y, base_name(r["name"]))
    canon = {g: live_name.get(g) or latest[g][1] for g in latest}
    out = collections.defaultdict(dict)
    groups = collections.defaultdict(set)
    for y in sorted(rows):
        for r in rows[y].values():
            g = find(("name", nkey(r["name"])))
            name = canon[g]
            groups[name].add(r.get("name_as_listed") or r["name"])
            if name != r["name"]:
                r.setdefault("name_as_listed", r["name"])
            r = {**r, "name": name, "slug": slugify(name)}
            cur = out[y].get(r["slug"])
            if cur is None:
                out[y][r["slug"]] = r
            else:
                for k, val in r.items():
                    if k in ("snapshot_ts", "capture_url", "path", "era"):
                        continue
                    if val not in (None, "", [], {}) and cur.get(k) in (None, "", [], {}):
                        cur[k] = val
    return out, {k: sorted(v) for k, v in sorted(groups.items()) if len(v) > 1 or next(iter(v)) != k}


def cc_url(v: dict) -> str:
    return v.get("capture_url") or ""


RAW_IA = RAW.parents[1] / "wayback" / RAW.name     # Internet Archive bodies (scratch/ia-pre2008.py)


def load_manifests() -> list[tuple[Path, dict]]:
    out = []
    for mf in sorted(P.wayback.glob("*-manifest*.json")):
        root = RAW_IA if mf.name.startswith("ia-") else RAW
        for key, v in json.loads(mf.read_text()).items():
            if v.get("status") == "ok" and (root / key).exists():
                out.append((root / key, v))
    return sorted(out, key=lambda kv: kv[1]["timestamp"])


def main() -> None:
    caps = load_manifests()
    investors: dict[str, str] = {}          # aspx team id -> name
    descs: dict[str, dict] = {}             # aspx company id -> {about, partner_ids, ts, capture_url}
    rows: dict[int, dict[str, dict]] = collections.defaultdict(dict)   # year -> slug -> row
    stats = collections.Counter()
    bodies = {}

    def body(path: Path) -> str:
        if path not in bodies:
            bodies[path] = path.read_bytes().decode("utf-8", "replace")
        return bodies[path]

    def put(year: int, row: dict) -> None:
        cur = rows[year].get(row["slug"])
        if cur is None:
            rows[year][row["slug"]] = row
            return
        # one row per company and year: keep the earliest capture, fill gaps from later ones
        for k, val in row.items():
            if k in ("snapshot_ts", "capture_url", "path", "era"):
                continue
            if val not in (None, "", [], {}) and cur.get(k) in (None, "", [], {}):
                cur[k] = val
        if row.get("partners"):
            cur["partners"] = sorted(set(cur.get("partners") or []) | set(row["partners"]))

    # pass 1: aspx investor ids and descriptions (any aspx wrapper page)
    for path, v in caps:
        if ".aspx" not in v["url"].lower():
            continue
        s = body(path)
        for i, n in re.findall(r"selectInvestor\((\d+), '([^']+)'\)", s):
            investors.setdefault(i, n)
        for link, cid, inner in re.findall(r'<div class="desc" link="([^"]*)" id="desc_(\d+)">(.*?)</div>', s, flags=re.S):
            about = strip_tags(inner)
            d = descs.setdefault(cid, {"about": "", "partner_ids": [], "ts": v["timestamp"], "capture_url": cc_url(v)})
            if about and len(about) > len(d["about"]):
                d["about"] = about
            ids = re.findall(r"\d+", link.split("id=", 1)[1]) if "id=" in link else []
            if ids:
                d["partner_ids"] = sorted(set(d["partner_ids"]) | set(ids))
    # team ids also resolve through the team wrapper pages' own titles (Team/Default.aspx?id=N -> "<Name> - Bessemer")
    for path, v in caps:
        m = re.search(r"/Team/Default\.aspx\?id=(\d+)", v["url"], flags=re.I)
        if m:
            t = re.search(r"<title>\s*(.*?)\s*-\s*Bessemer", body(path), flags=re.S)
            if t and t.group(1).strip():
                investors.setdefault(m.group(1), strip_tags(t.group(1)))

    # pass 2: listings
    anti: dict[str, dict] = {}
    for path, v in caps:
        url, ts = v["url"], v["timestamp"]
        year = int(ts[:4])
        low = url.lower().split("?")[0]
        s = body(path)
        if re.search(r"anti-?portfolio|/port/anti|/people/anti", low):
            # the firm's own list of companies it passed on (decisions.md D10): names only, never rows
            names = set()
            for a in re.findall(r'<img[^>]*alt="([^"]+)"', s):
                names.add(html.unescape(a))
            for a in re.findall(r"<h[2-4][^>]*>(.*?)</h[2-4]>", s, flags=re.S):
                names.add(strip_tags(a))
            for a in re.findall(r'data-name="([^"]+)"', s):
                names.add(html.unescape(a))
            for a in re.findall(r"(?:uploadedImages|files|uploads)/[^\"']*?/([A-Za-z0-9_%-]+)\.(?:gif|jpg|png|svg|webp)", s):
                names.add("img:" + a)
            anti[ts] = {"url": url, "capture_url": cc_url(v), "names": sorted(n for n in names if n and len(n) < 60)}
            continue
        # --- html-people: /people/<practice>/<sub>.html and /people/subindustry.asp (1999-2001, Internet Archive): the
        # portfolio by practice. Each company is a logo image followed by <STRONG>Name[<br>TICKER]</STRONG><BR>
        # description. YEAR, partner link(s)<BR> site. The practice essays on the same pages carry no logo and are
        # skipped. A listed company whose <STRONG> holds only its ticker takes its name from TICKER_NAMES.
        if re.search(r"/people/", low) and "/anti" not in low and "<strong>" in s.lower():
            for head, rest in re.findall(r'(?is)<img\s+src="[^"]*logos/[^"]*"[^>]*>\s*(?:</a>)?\s*</p>\s*(?:<a[^>]*>\s*)?<strong>(.*?)</strong>(.*?)'
                                         r'(?=<img[^>]*grey\.gif|<p\s+align|<a name=|</td>)', s):
                hp = [strip_tags(x) for x in re.split(r"(?i)<br\s*/?>", head) if strip_tags(x)]
                if not hp:
                    continue
                tick = next((x for x in hp if re.match(r"(?i)(nasdaq|nyse|amex)\s*:", x)), "")
                names = [x for x in hp if x != tick]
                raw_name = names[0] if names else TICKER_NAMES.get(tick.split(":")[-1].strip().upper(), "")
                nm = split_name(raw_name)
                if not nm["name"] or len(nm["name"]) > 60:
                    stats["html-people unnamed"] += 1
                    continue
                people = [strip_tags(x).replace("\xa0", " ") for x in re.findall(r'(?i)<a href="[^"]*(?:bios/|bio\.asp|investor\.asp)[^"]*"[^>]*>(.*?)</a>', rest, flags=re.S)]
                site = re.search(r'(?i)<a href="(https?://[^"]+)"', rest)
                desc = strip_tags(re.split(r'(?i)<a href', rest)[0])
                ym = re.search(r"((?:19|20)\d{2})\s*[,.]?\s*$", desc)
                put(year, {"slug": slugify(nm["name"]), "name": nm["name"], "path": re.sub(r"^https?://[^/]+", "", url), "snapshot_ts": ts,
                           "capture_url": cc_url(v), "era": "html-people", "invest_year": ym.group(1) if ym else None,
                           "about": re.sub(r"\s*,?\s*(?:19|20)\d{2}\s*[,.]?\s*$", "", desc).strip() or None,
                           "company_site": site.group(1) if site else None, "partners": people, "filters": "",
                           "ticker": tick or nm.get("ticker"),
                           **{k: nm[k] for k in ("name_as_listed", "acquirer", "fka") if nm.get(k)}})
                stats["html-people rows"] += 1
            stats["html-people captures"] += 1
            continue
        # --- asp-onepage: /port/onepage.asp 2002-2007 (Internet Archive), the whole current portfolio on one page:
        # <A NAME="<id>"> logo, then name <br> site <br> [ticker <br>] sector <br> partner links, then a description
        if "/port/onepage.asp" in low and '<A NAME="' in s:
            parts = re.split(r'<A NAME="(\d+)">', s)[1:]
            for cid, blk in zip(parts[0::2], parts[1::2]):
                tds = re.findall(r"<td[^>]*>(.*?)</td>", blk, flags=re.S)
                info = next((t for t in tds if "<br" in t.lower() and strip_tags(t)), "")
                if not info:
                    continue
                segs = re.split(r"<br\s*/?>", info, flags=re.I)
                nm = split_name(strip_tags(segs[0]))
                if not nm["name"]:
                    continue
                site = re.search(r'<a href="(https?://[^"]+)"', info, flags=re.I)
                people = [strip_tags(x) for x in re.findall(r'<a href="/about/bio\.asp\?id=\d+"[^>]*>(.*?)</a>', info, flags=re.S | re.I)]
                plain = [strip_tags(x) for x in segs[1:] if "<a " not in x.lower() and strip_tags(x)]
                tick = next((x for x in plain if re.match(r"(?i)(nasdaq|nyse|amex|lse|aim|tse|otc)\b", x)), "")
                sector = next((x for x in plain if x != tick), "")
                di = tds.index(info)
                about = next((strip_tags(t) for t in tds[di + 1:di + 3] if len(strip_tags(t)) > 25), "")
                put(year, {"slug": slugify(nm["name"]), "name": nm["name"], "path": "/port/onepage.asp", "snapshot_ts": ts,
                           "capture_url": cc_url(v), "era": "asp-onepage", "asp_id": cid,
                           "sectors": [x.strip() for x in sector.split(",") if x.strip()], "about": about or None,
                           "company_site": site.group(1) if site else None, "partners": people, "filters": "",
                           "ticker": tick or nm.get("ticker"),
                           **{k: nm[k] for k in ("name_as_listed", "acquirer", "fka") if nm.get(k)}})
                stats["asp-onepage rows"] += 1
            stats["asp-onepage captures"] += 1
            continue
        # --- asp-success: /port/success.asp 2002-2003 ("BVP Successes"): investment month and year, name, site,
        # ticker or acquirer, partners, and a paragraph that often names the round
        if "/port/success.asp" in low:
            for when, name, site, mark, who, about in re.findall(
                    r'<br>\s*((?:[A-Z][a-z]+ )?\d{4})\s*<br>\s*([^<]+?),?\s*<a href="([^"]+)"[^>]*>[^<]*</a>\s*<br>([^<]*)<br>(.*?)</td>'
                    r'\s*</tr>\s*<tr>\s*<td[^>]*>\s*<p>(.*?)</p>', s, flags=re.S):
                nm = split_name(strip_tags(name).rstrip(","))
                if not nm["name"]:
                    continue
                mon = re.match(r"([A-Z][a-z]+) (\d{4})", when)
                months = "January February March April May June July August September October November December".split()
                idate = f"{mon.group(2)}-{months.index(mon.group(1)) + 1:02d}" if mon and mon.group(1) in months else None
                mark = strip_tags(mark)
                acq = re.search(r"\((?:acquired by|merged with)\s+([^)]+)\)", mark)
                put(year, {"slug": slugify(nm["name"]), "name": nm["name"], "path": "/port/success.asp", "snapshot_ts": ts,
                           "capture_url": cc_url(v), "era": "asp-success", "invest_year": when[-4:], "invest_date": idate,
                           "company_site": site, "partners": [strip_tags(x) for x in re.findall(r"<a [^>]*>(.*?)</a>", who, flags=re.S)],
                           "exit_note": strip_tags(about), "about": strip_tags(about), "top_exit": True, "filters": "",
                           "ticker": re.sub(r"\s*\(.*", "", mark) or None, "acquirer": acq.group(1).strip() if acq else nm.get("acquirer"),
                           **{k: nm[k] for k in ("name_as_listed", "fka") if nm.get(k)}})
                stats["asp-success rows"] += 1
            stats["asp-success captures"] += 1
            continue
        # --- aspx-list
        anchors = re.findall(r'<div class="portfoliolist-date">\s*(\d{4})?\s*</div>\s*<div class="portfoliolist">\s*'
                             r'<a id="portanchor(\d+)" href="([^"]+)"[^>]*>(.*?)</a>', s, flags=re.S)
        if anchors and "?" not in url.replace("?cid=330", ""):
            for iy, cid, href, raw in anchors:
                nm = split_name(strip_tags(raw))
                if not nm["name"]:
                    continue
                d = descs.get(cid, {})
                partners = [investors[i] for i in d.get("partner_ids", []) if i in investors]
                row = {"slug": slugify(nm["name"]), "name": nm["name"], "path": "/Portfolio/" + href,
                       "snapshot_ts": ts, "capture_url": cc_url(v), "era": "aspx-list", "bvp_id": cid,
                       "invest_year": iy or None, "about": d.get("about") or None, "partners": partners,
                       "filters": ",".join(slugify(x) for x in partners),
                       **{k: nm[k] for k in ("name_as_listed", "acquirer", "ticker", "fka") if nm.get(k)}}
                put(year, row)
                stats["aspx-list rows"] += 1
            stats["aspx-list captures"] += 1
        # --- aspx-exits (Top 50 Exits report): rows of name | site | partner + paragraph
        if "report_frame" in low:
            for blk in re.split(r"<tr><td width=\"95\"", s)[1:]:
                m = re.search(r'<span style="font-weight:bold">(.*?)</span>(.*?)(?=<tr>|</table>|$)', blk, flags=re.S)
                if not m:
                    continue
                nm = split_name(strip_tags(m.group(1)))
                rest = m.group(2)
                site = re.search(r'href="(http[^"]+)"', rest)
                # after the name: "| <a>site</a> | Partner Name <p>paragraph</p>" (site and partner both optional;
                # the paragraph is not always wrapped in <p>, then it starts on the next line)
                tail = re.sub(r"^.*?</a>", "", rest, count=1, flags=re.S) if site else rest
                tail = re.sub(r"^\s*\|", "", tail)
                pm = re.match(r"\s*([A-Z][A-Za-z.]+(?: [A-Z][A-Za-z.]+){1,3})\s*(?:<p|\n|\r)", tail)
                partner = pm.group(1).strip() if pm else ""
                para = strip_tags(tail[pm.end(1):] if pm else tail)
                row = {"slug": slugify(nm["name"]), "name": nm["name"], "path": "/Portfolio/Report_Frame.aspx",
                       "snapshot_ts": ts, "capture_url": cc_url(v), "era": "aspx-exits", "top_exit": True,
                       "exit_note": para or None, "company_site": site.group(1) if site else None,
                       "partners": [partner] if partner else [], "filters": slugify(partner) if partner else "",
                       **{k: nm[k] for k in ("name_as_listed", "acquirer", "ticker", "fka") if nm.get(k)}}
                put(year, row)
                stats["aspx-exits rows"] += 1
        # --- drupal-list: <dd id="portcoNN"> cards
        cards = re.findall(r'<dd id="portco(\d+)">(.*?)</dd>', s, flags=re.S)
        if cards and "sec%5b" not in url.lower() and "sec[" not in url.lower() and "geog" not in url.lower():
            india = "/in/" in low
            for cid, blk in cards:
                t = re.search(r'<div class="title">(.*?)</div>', blk, flags=re.S)
                if not t:
                    continue
                nm = split_name(strip_tags(t.group(1)))
                if not nm["name"]:
                    continue
                about = re.search(r'<div class="company-description">(.*?)</div>', blk, flags=re.S)
                f = {strip_tags(k).rstrip(":"): strip_tags(val) for k, val in
                     re.findall(r"<li><strong>(.*?)</strong>(.*?)(?=<li>|</ul>)", blk, flags=re.S)}
                href = re.search(r'href="(/(?:in/)?portfolio/[^"]+)"', blk)
                row = {"slug": slugify(nm["name"]), "name": nm["name"],
                       "path": href.group(1) if href else "/portfolio", "snapshot_ts": ts, "capture_url": cc_url(v),
                       "era": "drupal-list", "drupal_id": cid,
                       "site_slug": href.group(1).rsplit("/", 1)[-1] if href else None,
                       "invest_year": (re.search(r"\d{4}", f.get("Investment Year", "")) or [None])[0] if f.get("Investment Year") else None,
                       "exit_year": (re.search(r"\d{4}", f.get("Exit Year", "")) or [None])[0] if f.get("Exit Year") else None,
                       "sectors": [x.strip() for x in f.get("Sector", "").split(",") if x.strip()],
                       "geography": f.get("Geography") or None,
                       "about": strip_tags(about.group(1)) if about else None, "filters": "",
                       "india_list": india or None,
                       **{k: nm[k] for k in ("name_as_listed", "acquirer", "ticker", "fka") if nm.get(k)}}
                iy = row["invest_year"]
                row["invest_year"] = iy if isinstance(iy, str) else (iy.group(0) if iy else None)
                ey = row["exit_year"]
                row["exit_year"] = ey if isinstance(ey, str) else (ey.group(0) if ey else None)
                put(year, row)
                stats["drupal-list rows"] += 1
            stats["drupal-list captures"] += 1
        # --- site2019-list: /companies, <article class="box investment tag-<sector>"> cards (2019-2020)
        arts = [] if 'with-overlay-on-open' in s else re.findall(r'<article class="box investment([^"]*)"[^>]*>(.*?)</article>', s, flags=re.S)
        if arts:
            for cls_, blk in arts:
                h3 = re.search(r"<h3>(.*?)</h3>", blk, flags=re.S)
                if not h3:
                    continue
                nm = split_name(strip_tags(h3.group(1)))
                if not nm["name"]:
                    continue
                h4 = re.search(r'<h4 class="enduring">(.*?)</h4>', blk, flags=re.S)
                mark = strip_tags(h4.group(1)) if h4 else ""
                about = re.search(r"<p>(.*?)</p>", blk, flags=re.S)
                site = re.search(r'<a href="(http[^"]+)"[^>]*>\s*Visit Website', blk)
                row = {"slug": slugify(nm["name"]), "name": nm["name"], "path": "/companies", "snapshot_ts": ts,
                       "capture_url": cc_url(v), "era": "site2019-list",
                       "sectors": [t[4:].replace("-", " ").title() for t in cls_.split() if t.startswith("tag-")],
                       "about": strip_tags(about.group(1)) if about else None,
                       "company_site": site.group(1) if site else None, "enduring": bool(h4) or None,
                       "acquirer": (re.sub(r"(?i)^acquired by:?\s*", "", mark).title() if mark.upper().startswith("ACQUIRED") else nm.get("acquirer")),
                       "ticker": (mark if re.match(r"(?i)(nasdaq|nyse|lse|bse|nse|tsx|asx)", mark) else nm.get("ticker")),
                       "filters": "", **{k: nm[k] for k in ("name_as_listed", "fka") if nm.get(k)}}
                put(year, row)
                stats["site2019-list rows"] += 1
            stats["site2019-list captures"] += 1
        # --- wp-list: /companies, <article class="box investment with-overlay-on-open" data-name=...> (2023-2026):
        # name, ticker or acquirer ("enduring"), description, the Bessemer investors on the deal, Founded, Partnered
        warts = re.findall(r'<article class="box investment with-overlay-on-open"([^>]*)>(.*?)</article>', s, flags=re.S)
        if warts:
            for attrs, blk in warts:
                a = re.search(r'<h3[^>]*>\s*<a href="([^"]+)"[^>]*>(.*?)</a>', blk, flags=re.S)
                h3 = re.search(r"<h3[^>]*>(.*?)</h3>", blk, flags=re.S)
                nm = split_name(strip_tags(a.group(2) if a else (h3.group(1) if h3 else "")))
                if not nm["name"]:
                    continue
                href = a.group(1) if a else ""
                site_slug = href.rstrip("/").rsplit("/", 1)[-1] if "/companies/" in href else None
                mark = re.search(r'<div class="enduring(?:-text)?">(.*?)</div>', blk, flags=re.S)
                mark = strip_tags(mark.group(1)) if mark else ""
                intro = re.search(r'<div class="intro">(.*?)</div>', blk, flags=re.S)
                team = [strip_tags(x) for x in re.findall(r'<a class="team"[^>]*>(.*?)</a>', blk, flags=re.S)]
                founded = re.search(r'<div class="founded">.*?<span class="year">(\d{4})', blk, flags=re.S)
                partnered = re.search(r'<div class="partnered">.*?<span class="year">(\d{4})', blk, flags=re.S)
                site = re.search(r'<a class="cta button white" href="(http[^"]+)"[^>]*>\s*Visit Website', blk)
                roadmaps = [strip_tags(x) for x in re.findall(r'<a class="roadmap"[^>]*>(.*?)</a>', blk, flags=re.S)]
                row = {"slug": slugify(nm["name"]), "name": nm["name"],
                       "path": "/companies/" + site_slug if site_slug else "/companies", "snapshot_ts": ts,
                       "capture_url": cc_url(v), "era": "wp-list", "site_slug": site_slug,
                       "sectors": list(dict.fromkeys(roadmaps)), "about": strip_tags(intro.group(1)) if intro else None,
                       "company_site": site.group(1) if site else None, "partners": list(dict.fromkeys(team)),
                       "filters": ",".join(slugify(x) for x in dict.fromkeys(team)),
                       "invest_year": partnered.group(1) if partnered else None,
                       "founded_year": founded.group(1) if founded else None,
                       "acquirer": (re.sub(r"(?i)^acquired by:?\s*", "", mark).strip() if mark.upper().startswith("ACQUIRED") else nm.get("acquirer")),
                       "ticker": (mark if re.match(r"(?i)(nasdaq|nyse|lse|bse|nse|tsx|asx|tase)", mark) else nm.get("ticker")),
                       **{k: nm[k] for k in ("name_as_listed", "fka") if nm.get(k)}}
                put(year, row)
                stats["wp-list rows"] += 1
            stats["wp-list captures"] += 1
        # --- drupal2-list: /portfolio 2015-2019, <div class="node view-mode-grid-item has-overlay portco" about="/portfolio/<slug>">:
        # name, summary, the firm's own Investment Date (a full date in the content attribute), Exit Year, strategies, geography
        nodes = re.split(r'<div class="node view-mode-grid-item has-overlay portco"\s+about="', s)[1:]
        if nodes:
            for blk in nodes:
                about_path = blk.split('"', 1)[0]
                h3 = re.search(r"<h3>(.*?)</h3>", blk, flags=re.S)
                nm = split_name(strip_tags(h3.group(1)) if h3 else "")
                if not nm["name"] or "/portfolio/" not in about_path:
                    continue
                summ = re.search(r'field-name-field-summary.*?<div class="field-item even">(.*?)</div>', blk, flags=re.S)
                idate = re.search(r'Investment Date:.*?content="(\d{4}-\d{2}-\d{2})', blk, flags=re.S)
                ey = re.search(r'Exit Year:.*?<div class="field-item even">\s*(\d{4})', blk, flags=re.S)
                strat = re.search(r'Related Strategy:(.*?)(?=<div class="field field-name|<div class="social-links"|$)', blk, flags=re.S)
                geo = re.search(r'Geography:(.*?)(?=<div class="field field-name|<div class="social-links"|$)', blk, flags=re.S)
                site_slug = about_path.rstrip("/").rsplit("/", 1)[-1]
                row = {"slug": slugify(nm["name"]), "name": nm["name"], "path": about_path, "snapshot_ts": ts,
                       "capture_url": cc_url(v), "era": "drupal2-list", "site_slug": site_slug,
                       "about": strip_tags(summ.group(1)) if summ else None,
                       "invest_date": idate.group(1) if idate else None, "invest_year": idate.group(1)[:4] if idate else None,
                       "exit_year": ey.group(1) if ey else None,
                       "sectors": [strip_tags(x) for x in re.findall(r"<a [^>]*>(.*?)</a>", strat.group(1), flags=re.S)] if strat else [],
                       "geography": ", ".join(strip_tags(x) for x in re.findall(r"<a [^>]*>(.*?)</a>", geo.group(1), flags=re.S)) if geo else None,
                       "filters": "", **{k: nm[k] for k in ("name_as_listed", "acquirer", "ticker", "fka") if nm.get(k)}}
                put(year, row)
                stats["drupal2-list rows"] += 1
            stats["drupal2-list captures"] += 1
        # --- drupal-page: /portfolio/<slug>
        m = re.match(r"^https?://(?:www\.)?bvp\.com/(?:in/)?portfolio/([a-z0-9%_.-]+)/?$", url.split("?")[0], flags=re.I)
        if m and m.group(1).lower() not in NON_COMPANY and ".aspx" not in low and 'class="portfolio-main"' not in s and not nodes:
            title = re.search(r"<title>\s*(.*?)\s*\|\s*Bessemer", s, flags=re.S)
            h1 = re.search(r"<h1[^>]*>(.*?)</h1>", s, flags=re.S)
            raw = strip_tags(title.group(1)) if title else (strip_tags(h1.group(1)) if h1 else "")
            nm = split_name(raw)
            if nm["name"] and not re.search(r"page not found|access denied", nm["name"], flags=re.I):
                txt = re.sub(r"<(script|style)[\s\S]*?</\1>", " ", s, flags=re.I)
                team = []
                tm = re.search(r">\s*Team\s*</h\d>(.*?)(?=<h\d|<div class=\"(?:news|spotlight)|$)", txt, flags=re.S)
                if tm:
                    team = [strip_tags(x) for x in re.findall(r'<a href="/(?:in/)?team/[^"]+"[^>]*>(.*?)</a>', tm.group(1), flags=re.S)]
                    team = [x for x in dict.fromkeys(team) if x and len(x.split()) >= 2]
                about = re.search(r'<div class="(?:field[^"]*body[^"]*|company-description|content)">(.*?)</div>', txt, flags=re.S)
                row = {"slug": slugify(nm["name"]), "name": nm["name"], "path": "/portfolio/" + m.group(1).lower(),
                       "snapshot_ts": ts, "capture_url": cc_url(v), "era": "drupal-page", "site_slug": m.group(1).lower(),
                       "partners": team, "filters": ",".join(slugify(x) for x in team),
                       "about": (strip_tags(about.group(1))[:900] if about else None),
                       **{k: nm[k] for k in ("name_as_listed", "acquirer", "ticker", "fka") if nm.get(k)}}
                put(year, row)
                stats["drupal-page rows"] += 1

    write_atomic(HERE / "anti-portfolio-captures.json", json.dumps(anti, indent=1, ensure_ascii=False) + "\n")
    rows, groups = regroup(rows)
    write_atomic(HERE / "name-groups.json", json.dumps(groups, indent=1, ensure_ascii=False) + "\n")
    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("*.json"):
        old.unlink()
    for year in sorted(rows):
        out = sorted(rows[year].values(), key=lambda r: r["slug"])
        out = [{k: val for k, val in r.items() if val not in (None, "", [], {})} | {"filters": r.get("filters", "")} for r in out]
        write_atomic(OUT / f"{year}.json", json.dumps(out, indent=1, ensure_ascii=False) + "\n")
        print(year, len(out), dict(collections.Counter(r["era"] for r in out)))
    write_atomic(HERE / "aspx-investors.json", json.dumps(investors, indent=1) + "\n")
    print(dict(stats), "| aspx descs", len(descs), "| investor ids", len(investors))


if __name__ == "__main__":
    main()
