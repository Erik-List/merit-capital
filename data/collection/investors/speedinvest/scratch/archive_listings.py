#!/usr/bin/env python3
"""Parse Speedinvest's archived site generations (captures under
data/filings/commoncrawl/speedinvest/ from Common Crawl, and under
data/filings/wayback/speedinvest/ from the Internet Archive once pulled) into
sources/wayback/parsed/<year>.json, the shape build-company-base.py reads:
[{slug, name, path, snapshot_ts, capture_url, invest_year?, filters?}].

Page shapes (read 2026-09-30):
- /portfolio/ 2017-2020, WordPress 'enfold': logo tiles, each an <a> to the
  firm's own company page (/portfolio/<slug>/ or /blog/portfolio/<slug>/) or to
  the company's site, wrapping an <img title='tile_<Name>_450'>; section <h3>
  headings (FinTech / InsurTech, DeepTech / B2B, ConsumerTech, Exits) become the
  row's filters.
- /portfolio/<slug>/, /blog/portfolio/<slug>/, /portfolio-item/<slug>/: one
  company per page, <title>Name | Speedinvest</title>, "Investment Manager:
  <partner>" and "Investment Date: <year>".
- /team/ 2017-2019: each partner card carries "Portfolio: A, B, C": the
  partner's own attribution, a first-party list with the deal partner.

Also writes sources/wayback/archive-evidence.json: per base-name key, every
capture that names the company, with the partner and year the firm printed.
"""
import html as H
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
INV = HERE.parent
ROOT = INV.parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import write_atomic  # noqa: E402

CC_RAW = ROOT / "data" / "filings" / "commoncrawl" / "speedinvest"
IA_RAW = ROOT / "data" / "filings" / "wayback" / "speedinvest"
MAN = INV / "sources" / "wayback" / "cc-manifest.json"
IA_MAN = INV / "sources" / "wayback" / "ia-manifest.json"
SECTIONS = {"fintech": "FinTech", "insurtech": "FinTech", "deeptech": "DeepTech", "b2b": "DeepTech",
            "consumertech": "ConsumerTech", "consumer": "ConsumerTech", "exits": "Exits", "exit": "Exits",
            "marketplaces": "Marketplaces", "network effects": "Marketplaces", "health": "Health",
            "industrial": "Industrial", "saas": "SaaS"}
NOT_CO = {"speedinvest", "this could be you", "crunchbase", "portfolio", "team", "blog", "home", ""}


def slugify(s):
    s = H.unescape(s).lower().replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def tile_name(title):
    t = re.sub(r"(?i)^(tile|logo)[_-]+", "", title)
    t = re.sub(r"(?i)[_-]+(tile|logo)$", "", t)
    t = re.sub(r"(?i)[_-]*\d{2,4}x\d{2,4}$", "", t)                # 450x450, _400x400
    t = re.sub(r"(?i)[_-]+\d{2,4}(?:[_-]\d+)?$", "", t)             # _450, _450-1
    t = re.sub(r"(?i)[_-]?(small|hover|grid|team|tile|logo|neu|new|web|final)$", "", t)
    t = re.sub(r"(?i)[_-]+(tile|logo)$", "", t)
    t = re.sub(r"(?i)^(tile|logo)[_-]+", "", t)
    t = t.replace("_", " ").strip()
    return t


def text(s):
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.S)
    return re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def captures():
    out = []
    if MAN.exists():
        for key, m in json.loads(MAN.read_text()).items():
            if m.get("status") == "ok":
                out.append((CC_RAW / key, m))
    if IA_MAN.exists():
        for key, m in json.loads(IA_MAN.read_text()).items():
            if m.get("status") == "ok":
                out.append((IA_RAW / key, m))
    return out


def path_of(url):
    p = re.sub(r"^https?://(www\.)?speedinvest\.com(:\d+)?", "", url.split("?")[0].split("#")[0])
    return p or "/"


def parse_listing(s):
    """Tiles on a /portfolio/ page: [(name, slug, section, href)]."""
    rows = []
    heads = [(m.start(), text(m.group(1))) for m in re.finditer(r"<h3[^>]*>(.*?)</h3>", s, re.S)]

    def section(pos):
        cur = ""
        for p, h in heads:
            if p < pos:
                low = h.lower()
                for k, v in SECTIONS.items():
                    if k in low:
                        cur = v
                        break
        return cur
    for m in re.finditer(r"<a\s+href=['\"]([^'\"]+)['\"][^>]*>\s*<img([^>]*)>", s, re.S):
        href, img = m.group(1), m.group(2)
        t = re.search(r"title=['\"]([^'\"]*)['\"]", img)
        a = re.search(r"alt=['\"]([^'\"]*)['\"]", img)
        src = re.search(r"src=['\"]([^'\"]+)['\"]", img)
        if not src or "/uploads/" not in src.group(1):
            continue
        name = tile_name(t.group(1)) if t and t.group(1) else (a.group(1).strip() if a else "")
        if not name and src:
            name = tile_name(Path(src.group(1)).stem)
        ms = re.search(r"speedinvest\.com/(?:blog/)?portfolio(?:-item)?/([^/'\"?#]+)", href)
        slug = ms.group(1) if ms else slugify(name)
        if slugify(name) in NOT_CO or slug in NOT_CO:
            continue
        rows.append((name, slug, section(m.start()), href))
    return rows


def parse_grid(s):
    """2018-2020 isotope grid: one <div data-ajax-id> per company with its filter
    classes (sector, Acquired/Active, Pre-Seed), the h2 name, 'Investment Manager',
    'Year invested', 'Sector' and the company's website."""
    rows = []
    parts = re.split(r"(?=<div data-ajax-id=)", s)
    for e in parts[1:]:
        cls = re.search(r"class='([^']*isotope-item[^']*)'", e)
        h2 = re.search(r"<h2[^>]*>(?:<a[^>]*>)?(.*?)(?:</a>)?</h2>", e, re.S)
        if not h2:
            continue
        name = text(h2.group(1))
        href = re.search(r"href='([^']*portfolio-item/([^'/]+)/?)'", e)
        body = text(e)
        mgr = re.search(r"Investment Manager:\s*(.+?)\s+(?:Year invested|Year acquired|Sector|Investment:|Exit:|$)", body)
        acq = re.search(r"Year acquired:\s*((?:19|20)\d\d)", body)
        yr = re.search(r"Year invested:\s*((?:19|20)\d\d)", body)
        sec = re.search(r"Sector:\s*(.+?)(?:\s+(?:Investment Manager|Year invested)|$)", body)
        web = [u for u in re.findall(r'href="(https?://[^"]+)"', e) if "speedinvest" not in u]
        tags = [c[:-5] for c in (cls.group(1).split() if cls else []) if c.endswith("_sort") and c not in ("all_sort", "portfolio_sort")]
        rows.append({"name": name, "slug": href.group(2) if href else slugify(name),
                     "manager": mgr.group(1).strip() if mgr else None, "invest_year": yr.group(1) if yr else None,
                     "sector": sec.group(1).strip() if sec else None, "tags": tags, "website": web[0] if web else None,
                "year_acquired": acq.group(1) if acq else None})
    return rows


# Spelling variants of one company across the firm's own captures, fixed in the
# parsed source (First Round rule: a merge would keep the junk spelling on the
# published row). Keyed on the slugified name; None drops a non-company string.
NAME_MAP = {
    "sip-wise": "Sipwise", "sipwise": "Sipwise",
    "enbrite": "Enbrite.ly", "enbrite-ly": "Enbrite.ly", "enbritely": "Enbrite.ly",
    "datapath": "Datapath.io", "datapath-io": "Datapath.io",
    "indoo-rs": "indoo.rs", "indoors": "indoo.rs",
    "tier-mobility": "TIER", "tourradar": "TourRadar", "iyzico": "iyzico",
    "we-back-amazing-people-with-amazing-stories": None, "speedinvest-portfolio-company": None,
    "a-speedinvest-portfolio-company": None, "speedinvest": None,
}


def canon(name):
    k = slugify(name)
    if k in NAME_MAP:
        return NAME_MAP[k]
    return name


def parse_company_page(s):
    # The 2023- Webflow pages title every company "A Speedinvest Portfolio Company";
    # the company's own name is the h4 under that line.
    h4 = re.search(r"A Speedinvest Portfolio Company</div>\s*<h4[^>]*>(.*?)</h4>", s, re.S)
    if h4:
        body = text(s)
        yr = re.search(r"Year Invested\s*((?:19|20)\d\d)", body)
        return text(h4.group(1)), None, (yr.group(1) if yr else None)
    t = re.search(r"<title>(.*?)</title>", s, re.S)
    name = re.split(r"\s+[|\u2013-]\s+Speedinvest|\s*\|", text(t.group(1)))[0].strip() if t else ""
    name = re.split(r"\s*:\s+(?=[A-Z])|\s+[\u2013\u2014-]\s+(?=[A-Z])", name)[0].strip()   # "Flaviar: Tasting is Believing", "Tourradar - Compare & Book"
    body = text(s)
    mgr = re.search(r"Investment Manager:\s*(.+?)\s+(?:Investment Date|Investment Facts|Investment:|Exit:|Year acquired|Year invested|Crunchbase|$)", body)
    yr = re.search(r"(?:Investment Date|Year invested|Investment):\s*((?:19|20)\d\d)", body)
    return name, (mgr.group(1).strip() if mgr else None), (yr.group(1) if yr else None)


def parse_team(s):
    """[(partner, [company names])] from the 'Portfolio:' lines of partner cards."""
    body = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.S)
    body = H.unescape(re.sub(r"<[^>]+>", "\n", body))
    lines = [l.strip() for l in body.split("\n") if l.strip()]
    out = []
    for i, l in enumerate(lines):
        if l.startswith("Portfolio:"):
            # partner name: the nearest preceding line pair "Name / Title"
            name = None
            for j in range(i - 1, max(i - 6, 0), -1):
                if re.fullmatch(r"[A-ZÄÖÜ][\w\-äöüßé'. ]+ [A-ZÄÖÜ][\w\-äöüßé'. ]+", lines[j]) and not re.search(
                        r"Partner|Founder|CEO|Office|Associate|Analyst|Principal|Manager|Relations", lines[j]):
                    name = lines[j]
                    break
            cos = [c.strip(" .") for c in re.split(r",|;", l[len("Portfolio:"):]) if c.strip(" .")]
            out.append((name, cos))
    return out


def main():
    years = defaultdict(dict)          # year -> slug -> row
    evidence = defaultdict(lambda: {"captures": [], "partners": set(), "invest_years": set(), "sections": set()})
    team_attr = []
    for f, m in captures():
        if not f.exists():
            continue
        s = f.read_text(errors="replace")
        path = path_of(m["url"])
        ts = m["timestamp"]
        year = int(ts[:4])
        cap = m.get("capture_url") or f"https://web.archive.org/web/{ts}/{m['url']}"
        if re.fullmatch(r"/(?:en/|de/)?portfolio/?", path) and "data-ajax-id=" in s:
            for g in parse_grid(s):
                g["name"] = canon(g["name"])
                if not g["name"]:
                    continue
                slug = slugify(g["name"])
                row = {"slug": slug, "name": g["name"], "path": path, "snapshot_ts": ts, "capture_url": cap,
                       "filters": ",".join(t for t in g["tags"])}
                if g["invest_year"]:
                    row["invest_year"] = g["invest_year"]
                old = years[year].get(slug)
                if not old or ts < old["snapshot_ts"]:
                    years[year][slug] = row
                e = evidence[slugify(g["name"])]
                e["captures"].append({"ts": ts, "path": path, "capture_url": cap, "name": g["name"],
                                      "manager": g["manager"], "invest_year": g["invest_year"],
                                      "sector": g["sector"], "tags": g["tags"], "website": g["website"],
                                      "year_acquired": g.get("year_acquired")})
                if g["manager"]:
                    e["partners"].add(g["manager"])
                if g["invest_year"]:
                    e["invest_years"].add(g["invest_year"])
                for t in g["tags"]:
                    e["sections"].add(t)
        elif re.fullmatch(r"/(?:en/|de/)?portfolio/?", path):
            for name, slug, sec, href in parse_listing(s):
                name = canon(name)
                if not name:
                    continue
                slug = slugify(name)
                row = years[year].get(slug)
                if not row or ts < row["snapshot_ts"]:
                    years[year][slug] = {"slug": slug, "name": name, "path": path, "snapshot_ts": ts,
                                         "capture_url": cap, "filters": sec, "href": href}
                e = evidence[slugify(name)]
                e["captures"].append({"ts": ts, "path": path, "capture_url": cap, "section": sec, "name": name})
                if sec:
                    e["sections"].add(sec)
        elif re.fullmatch(r"/(?:blog/)?portfolio(?:-item)?/[^/]+/?", path):
            name, mgr, yr = parse_company_page(s)
            if not name or re.search(r"(?i)portfolio company", name):
                name = " ".join(w.capitalize() for w in path.strip("/").split("/")[-1].split("-"))
            name = canon(name)
            if not name or slugify(name) in NOT_CO:
                continue
            slug = slugify(name)
            row = {"slug": slug, "name": name, "path": path, "snapshot_ts": ts, "capture_url": cap}
            if yr:
                row["invest_year"] = yr
            old = years[year].get(slug)
            if not old or ts < old["snapshot_ts"]:
                years[year][slug] = {**(old or {}), **row}
            e = evidence[slugify(name)]
            e["captures"].append({"ts": ts, "path": path, "capture_url": cap, "name": name,
                                  "manager": mgr, "invest_year": yr})
            if mgr:
                e["partners"].add(mgr)
            if yr:
                e["invest_years"].add(yr)
        elif re.fullmatch(r"/team/?", path):
            for partner, cos in parse_team(s):
                team_attr.append({"ts": ts, "capture_url": cap, "partner": partner, "companies": cos})
                for c in cos:
                    c = canon(c)
                    if not c:
                        continue
                    slug = slugify(c)
                    if slug in NOT_CO:
                        continue
                    if slug not in years[year]:
                        years[year][slug] = {"slug": slug, "name": c, "path": path, "snapshot_ts": ts,
                                             "capture_url": cap, "filters": "team-page"}
                    e = evidence[slug]
                    e["captures"].append({"ts": ts, "path": path, "capture_url": cap, "name": c,
                                          "manager": partner})
                    if partner:
                        e["partners"].add(partner)
    outdir = INV / "sources" / "wayback" / "parsed"
    outdir.mkdir(parents=True, exist_ok=True)
    for y, rows in sorted(years.items()):
        write_atomic(outdir / f"{y}.json", json.dumps(sorted(rows.values(), key=lambda r: r["slug"]), indent=1,
                                                   ensure_ascii=False) + "\n")
        print(y, len(rows))
    ev = {}
    for k, e in evidence.items():
        caps = sorted(e["captures"], key=lambda c: c["ts"])
        ev[k] = {"names": sorted({c["name"] for c in caps}), "first_capture": caps[0], "last_capture": caps[-1],
                 "n_captures": len(caps), "partners": sorted(p for p in e["partners"] if p),
                 "invest_years": sorted(e["invest_years"]), "sections": sorted(e["sections"])}
    write_atomic(INV / "sources" / "wayback" / "archive-evidence.json", json.dumps(
        {"_readme": "Per company (slugified name): every archived Speedinvest capture naming it, the deal partner "
                    "the firm printed (company page 'Investment Manager', team-card 'Portfolio:' lines), the "
                    "'Investment Date' year and the listing section. scratch/archive_listings.py.",
         "companies": ev, "team_attribution": team_attr}, indent=1, ensure_ascii=False) + "\n")
    print(len(ev), "companies in the archive evidence;", len(team_attr), "team cards with a Portfolio line")


if __name__ == "__main__":
    main()
