"""HV Capital archive layer: every archived portfolio surface of the firm, parsed
into sources/wayback/parsed/<year>.json (wayback-pull's shape plus capture_url
and, where the surface states it, the firm's own invest_year), and an evidence
side file scratch/archive-evidence.json keyed by company.

Surfaces (config.json wayback._eras_note):
  A  holtzbrinck-ventures.com 2006-2010, phpwcms: index.php?<key>_en / id=... pages;
     the subnav lists the whole Portfolio or Exits section, the section is the
     levelsensitive_active_link.
  B  holtzbrinck-ventures.com 2011-2015, Dutyfarm CMS: ul#pf-teaser anchors
     (title=Name) on every portfolio page; section from the submenu act_path
     (Current / Former Investments; Aktuell / Ehemalige).
  C  holtzbrinck-ventures.com 2015-2018, WordPress: div.tile.portfolio with a
     data-content modal (h2 name, Founded: <founded> | <folio-start = HV's own
     investment year>, HQ, Founders, Website, Representative).
  D  hvcapital.com 2020-2021, WordPress Divi /companies.
  E  hvcapital.com 2022-2025, Next.js /_next/data/<build>/companies.json
     (Storyblok companiesListingData: company_name, entry_date, founded_date,
     partners, city, country, current_stage, company_website).

Usage:
  python3 hv_archive.py fetch   # fetch one capture per (url, year) of A-C and D/E lists
  python3 hv_archive.py parse   # parse everything under raw/ into parsed/ + evidence
"""
from __future__ import annotations

import html
import json
import re
import sys
import urllib.parse
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
INV = HERE.parent
ROOT = INV.parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
import ia_fetch  # noqa: E402

RAW = INV / "sources/wayback/raw"
OLD = RAW / "hv-old"
PARSED = INV / "sources/wayback/parsed"
CDX = HERE / "cdx"

NON_COMPANY_KEYS = {
    "about_us", "contact", "imprint", "impressum_de", "legal-notice", "rechtliche-hinweise_de",
    "history", "historie", "strategy", "partners", "strategic_partners", "strategische_partner",
    "fund-investors", "fund-investoren", "business_plans_en", "facts_and_figures",
    "media_services", "medialeistungen", "investment-strategy", "investmentstrategie",
    "investmentcriteria_and_focus", "investmentkriterien_und_schwerpunkte", "portfolio_de",
    "portfolio_en", "portfolio-aktuell", "portfolio-aktuell_en", "portfolio-ehemalig",
    "portfolio-ehemalig_en", "exits_en", "aktuelle-news", "aktuelle-news_en", "news-archiv",
    "news-archiv_en", "news_en", "team", "our-team", "unser-team_de", "jobs", "jobs_en",
    "kontakt_de", "search", "de", "en", "",
}


def wb_url(ts: str, orig: str) -> str:
    return f"https://web.archive.org/web/{ts}/{orig}"


def norm_key(k: str) -> str:
    return re.sub(r"_(de|en|eng)(-1)?$", "", k).replace("_exits", "")


def slug_of(name: str) -> str:
    import unicodedata
    n = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", n.lower()).strip("-")


def text_of(fragment: str) -> str:
    fragment = re.sub(r"(?s)<(script|style)[^>]*>.*?</\1>", " ", fragment)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", fragment))).strip()


def read(p: Path) -> str:
    b = p.read_bytes()
    for enc in ("utf-8", "latin-1"):
        try:
            return b.decode(enc)
        except UnicodeDecodeError:
            continue
    return b.decode("utf-8", "replace")


# ---------------------------------------------------------------- fetch
def load_captures() -> list[tuple[str, str]]:
    rows = []
    for f in CDX.glob("old-*.tsv"):
        for line in f.read_text().splitlines():
            parts = line.split("\t")
            if len(parts) >= 2 and parts[0].isdigit():
                rows.append((parts[0], parts[1]))
    return rows


def fetch_news() -> None:
    """One capture per firm news post (2010-2015), by the post's own slug."""
    NEWS = RAW / "hv-news"
    NEWS.mkdir(parents=True, exist_ok=True)
    rows = json.loads((CDX / "holtzbrinck-ventures.com.json").read_text())[1:]
    per = {}
    for ts, orig, st, *_ in rows:
        m = re.search(r"newsdetail=(\d{8})-\d+_([^&]+)", orig)
        if m and st == "200":
            key = m.group(1) + "_" + m.group(2)[:90]
            # prefer the English channel (-292/-294) where both exist
            if key not in per or "-292_" in orig:
                per[key] = (ts, orig)
    print(f"{len(per)} news posts")
    got = 0
    for key, (ts, orig) in sorted(per.items()):
        dest = NEWS / f"{key[:110]}.html"
        if dest.exists() and dest.stat().st_size:
            continue
        body, st = ia_fetch.get(f"https://web.archive.org/web/{ts}id_/{orig}")
        if st.startswith("2") and body:
            dest.write_bytes(body)
            (NEWS / (dest.name + ".url")).write_text(f"{ts}\t{orig}\n")
            got += 1
        else:
            print(f"  {st} {ts} {orig}")
    print(f"fetched {got} news posts")


def parse_news() -> None:
    NEWS = RAW / "hv-news"
    out = []
    for f in sorted(NEWS.glob("*.html")):
        meta = NEWS / (f.name + ".url")
        if not meta.exists():
            continue
        ts, orig = meta.read_text().strip().split("\t", 1)
        s = read(f)
        h1 = re.search(r"<h1>(.*?)</h1>", s, re.S)
        body = re.search(r'(?s)<div class="(?:news-detail|newsdetail|articleText|pf-right|col)"[^>]*>(.*?)</div>\s*</div>', s)
        text = text_of(body.group(1)) if body else text_of(s)
        m = re.search(r"newsdetail=(\d{4})(\d{2})(\d{2})", orig)
        out.append({"date": f"{m.group(1)}-{m.group(2)}-{m.group(3)}" if m else ts[:8],
                    "title": text_of(h1.group(1)) if h1 else f.stem,
                    "capture_url": wb_url(ts, orig), "text": text[:4000]})
    (HERE / "firm-news.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(f"parsed {len(out)} news posts -> scratch/firm-news.json")


def fetch() -> None:
    OLD.mkdir(parents=True, exist_ok=True)
    caps = load_captures()
    per = {}
    for ts, orig in caps:
        if re.search(r"news|newsdetail|newspage|\.(jpg|png|gif|css|js)$", orig, re.I):
            continue
        q = orig.split("?", 1)[1] if "?" in orig else orig
        key = (re.sub(r"^https?://[^/]+", "", orig.split("?")[0]).rstrip("/") + "?" + q, ts[:4])
        per.setdefault(key, (ts, orig))
    todo = sorted(per.values())
    print(f"{len(caps)} captures -> {len(todo)} (url, year) pairs to hold")
    got = 0
    for ts, orig in todo:
        dest = OLD / f"{ts}-{slug_of(orig.split('holtzbrinck-ventures.com', 1)[-1])[:80]}.html"
        if dest.exists() and dest.stat().st_size:
            continue
        body, st = ia_fetch.get(f"https://web.archive.org/web/{ts}id_/{orig}")
        if st.startswith("2") and body:
            dest.write_bytes(body)
            (OLD / (dest.name + ".url")).write_text(f"{ts}\t{orig}\n")
            got += 1
        else:
            print(f"  {st} {ts} {orig}")
        if got and got % 25 == 0:
            print(f"  fetched {got}")
    print(f"fetched {got} new captures")


# ---------------------------------------------------------------- parse
def parse_A(s: str):
    """2006-2010 phpwcms page: (section, [(key, name)], h1, body text)."""
    act = re.search(r'id="levelsensitive_active_link">([^<]+)<', s)
    section = (act.group(1).strip().lower() if act else "")
    sub = re.search(r'(?s)<ul id="subnav_ul">(.*?)</ul>', s)
    items = []
    if sub:
        for key, name in re.findall(r'<a href="index\.php\?([^"&]+)"[^>]*>([^<]+)</a>', sub.group(1)):
            items.append((key, html.unescape(name).strip()))
    h1 = re.search(r"<h1>(.*?)</h1>", s, re.S)
    content = re.search(r'(?s)<div id="content">(.*?)(?:<div id="footer"|<!-- FOOTER|$)', s)
    return section, items, text_of(h1.group(1)) if h1 else "", text_of(content.group(1))[:1500] if content else ""


def parse_B(s: str):
    """2011-2015 Dutyfarm page: (section, [(key, name)], h1, body text)."""
    sec = ""
    m = re.search(r'<li class="subitem\s+act_path"><a href="index\.php\?([^"]+)"[^>]*>([^<]+)</a>', s)
    if m and "portfolio" in m.group(1):
        sec = "former" if "ehemalig" in m.group(1) else "current"
    items = []
    teaser = re.search(r'(?s)<ul id="pf-teaser">(.*?)</ul>', s)
    if teaser:
        for key, title in re.findall(r'<a href="index\.php\?([^"&]+)" title="([^"]*)"', teaser.group(1)):
            items.append((key, html.unescape(title).strip()))
    h1 = re.search(r"<h1>(.*?)</h1>", s, re.S)
    body = re.search(r'(?s)<div class="pf-right"(.*?)</div>\s*</div>\s*</div>', s)
    return sec, items, text_of(h1.group(1)) if h1 else "", text_of(body.group(1))[:1500] if body else ""


def parse_C(s: str):
    """2015-2018 WordPress tiles: [dict(name, founded, invest_year, hq, founders, website, representative, text)]."""
    out = []
    for dc in re.findall(r'<div class="tile portfolio[^"]*" data-id="\d+" data-content="(.*?)"\s*>', s, re.S):
        d = html.unescape(dc)
        name = re.search(r"<h2>(.*?)</h2>", d, re.S)
        if not name:
            continue
        rec = {"name": text_of(name.group(1))}
        fs = re.search(r"<dt>Founded:</dt>\s*<dd>\s*(\d{4})?.*?folio-start\">\s*(\d{4})", d, re.S)
        if fs:
            rec["founded"], rec["invest_year"] = fs.group(1) or "", fs.group(2)
        for lab, k in (("HQ", "hq"), ("Founders", "founders"), ("Website", "website")):
            m = re.search(rf"<dt>{lab}:</dt>\s*<dd>(.*?)</dd>", d, re.S)
            if m:
                rec[k] = text_of(m.group(1))
        rep = re.search(r"Representative:?\s*</?[^>]*>?\s*([^<]+)", d)
        t = text_of(d)
        r2 = re.search(r"Representatives?:\s*([A-Z][^\n]{2,60}?)\s+(General Partner|Partner|Principal|Investment Manager|Managing|Venture Partner|Senior|Associate|Vice President|See all)", t)
        rec["representative"] = r2.group(1).strip() if r2 else ""
        rec["text"] = t[:1200]
        out.append(rec)
    return out


def parse_E(d: dict):
    """Next.js companies.json -> [dict]."""
    body = d.get("pageProps", {}).get("otherComponentProps", {}).get("body", [])
    rows = []
    for comp in body:
        if isinstance(comp, dict) and comp.get("companiesListingData"):
            for c in comp["companiesListingData"]:
                ct = c.get("content", {})
                rows.append({
                    "name": (ct.get("company_name") or c.get("name") or "").strip(),
                    "story_slug": c.get("slug") or "",
                    "invest_date": (ct.get("entry_date") or "")[:10],
                    "founded_date": (ct.get("founded_date") or "")[:10],
                    "city": ct.get("city") or "", "country": ct.get("country") or "",
                    "current_stage": ct.get("current_stage") or "",
                    "sector": ct.get("sector") or "",
                    "partners": [p.get("name") for p in (ct.get("partners") or []) if isinstance(p, dict) and p.get("name")],
                    "website": ((ct.get("company_website") or {}).get("url") or "") if isinstance(ct.get("company_website"), dict) else "",
                    "founders": ct.get("founders_names") or "",
                    "description": (ct.get("list_description") or ct.get("slogan") or "")[:400],
                })
    return rows


def parse() -> None:
    parsed = defaultdict(dict)            # year -> slug -> row
    ev = defaultdict(lambda: {"names": set(), "listed": defaultdict(set), "captures": {},
                              "invest_years": set(), "founded": set(), "partners": set(),
                              "hq": set(), "websites": set(), "texts": [], "current_stage": {}})

    def add(year, name, key_path, ts, orig, section, **extra):
        if not name:
            return
        slug = slug_of(name)
        if not slug:
            return
        cap = wb_url(ts, orig)
        row = parsed[year].setdefault(slug, {"slug": slug, "name": name, "path": key_path,
                                              "snapshot_ts": ts, "capture_url": cap})
        if ts < row["snapshot_ts"]:
            row.update(snapshot_ts=ts, capture_url=cap, path=key_path)
        if extra.get("invest_year"):
            row["invest_year"] = min(extra["invest_year"], row.get("invest_year") or extra["invest_year"])
        e = ev[slug]
        e["names"].add(name)
        e["listed"][year].add(section or "listed")
        e["captures"].setdefault(str(year), cap)
        for k in ("invest_year", "founded"):
            if extra.get(k):
                (e["invest_years"] if k == "invest_year" else e["founded"]).add(extra[k])
        for p in extra.get("partners") or []:
            e["partners"].add(p)
        if extra.get("hq"):
            e["hq"].add(extra["hq"])
        if extra.get("website"):
            e["websites"].add(extra["website"])
        if extra.get("text") and len(e["texts"]) < 3:
            e["texts"].append({"ts": ts, "url": cap, "text": extra["text"][:900]})
        if extra.get("current_stage"):
            e["current_stage"][str(year)] = extra["current_stage"]

    # A-C: the old domain
    pages = 0
    for f in sorted(OLD.glob("*.html")):
        meta = OLD / (f.name + ".url")
        if meta.exists():
            ts, orig = meta.read_text().strip().split("\t", 1)
        else:
            continue
        s = read(f)
        year = int(ts[:4])
        pages += 1
        if 'id="subnav_ul"' in s or "levelsensitive" in s:
            section, items, h1, body = parse_A(s)
            sec = {"portfolio": "current", "exits": "former"}.get(section, "")
            if not sec:
                continue
            for key, name in items:
                if norm_key(key) in NON_COMPANY_KEYS:
                    continue
                add(year, name, f"/index.php?{key}", ts, orig, sec)
            # the page's own company (its h1) carries the body text
            q = orig.split("?", 1)[1] if "?" in orig else ""
            own = [n for k, n in items if k == q.split("&")[0]]
            if own and body:
                add(year, own[0], f"/index.php?{q}", ts, orig, sec, text=body)
        elif 'id="pf-teaser"' in s:
            sec, items, h1, body = parse_B(s)
            if not sec:
                continue
            for key, name in items:
                if norm_key(key) in NON_COMPANY_KEYS:
                    continue
                add(year, name, f"/index.php?{key}", ts, orig, sec)
            q = orig.split("?", 1)[1] if "?" in orig else ""
            own = [n for k, n in items if k == q.split("&")[0]]
            rep = re.search(r"Representative\s+([A-Z][a-zäöüß]+ [A-Z][a-zäöüß]+)", body)
            if own and body:
                add(year, own[0], f"/index.php?{q}", ts, orig, sec, text=body,
                    partners=[rep.group(1)] if rep else [])
        elif "tile portfolio" in s:
            for rec in parse_C(s):
                add(year, rec["name"], "/portfolio/", ts, orig, "listed",
                    invest_year=rec.get("invest_year"), founded=rec.get("founded"),
                    hq=rec.get("hq"), website=rec.get("website"),
                    partners=[rec["representative"]] if rec.get("representative") else [],
                    text=rec.get("text"))
    # D/E: hvcapital.com
    for f in sorted(RAW.glob("hvcapital-companies-*.json")):
        ts = re.search(r"(\d{14})", f.name).group(1)
        year = int(ts[:4])
        build = None
        try:
            d = json.loads(read(f))
        except json.JSONDecodeError:
            continue
        cdx = json.loads((CDX / "hvcapital.com.json").read_text())[1:]
        orig = next((o for t, o, *_ in cdx if t == ts and o.endswith("companies.json")), "")
        for r in parse_E(d):
            iy = r["invest_date"][:4] if r["invest_date"][:4].isdigit() else ""
            add(year, r["name"], "/companies", ts, orig, r["current_stage"] or "listed",
                invest_year=iy, founded=r["founded_date"][:4], partners=r["partners"],
                hq=", ".join(x for x in (r["city"], r["country"]) if x), website=r["website"],
                current_stage=r["current_stage"])
            ev[slug_of(r["name"])].setdefault("invest_dates", set()).add(r["invest_date"])
    for f in sorted(RAW.glob("hvcapital-companies-*.html")):
        ts = re.search(r"(\d{14})", f.name).group(1)
        s = read(f)
        orig = "https://www.hvcapital.com/companies"
        names = parse_D(s)
        for n in names:
            add(int(ts[:4]), n, "/companies", ts, orig, "listed")

    PARSED.mkdir(parents=True, exist_ok=True)
    for year, rows in sorted(parsed.items()):
        (PARSED / f"{year}.json").write_text(json.dumps(sorted(rows.values(), key=lambda r: r["slug"]),
                                                        indent=1, ensure_ascii=False) + "\n")
        print(f"  {year}: {len(rows)} companies")
    out = {}
    for slug, e in sorted(ev.items()):
        out[slug] = {"names": sorted(e["names"]),
                     "listed": {y: sorted(v) for y, v in sorted(e["listed"].items())},
                     "captures": e["captures"], "invest_years": sorted(e["invest_years"]),
                     "invest_dates": sorted(e.get("invest_dates", set())),
                     "founded": sorted(e["founded"]), "partners": sorted(e["partners"]),
                     "hq": sorted(e["hq"]), "websites": sorted(e["websites"]),
                     "current_stage": e["current_stage"], "texts": e["texts"]}
    (HERE / "archive-evidence.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(f"parsed {pages} old-domain pages; {len(out)} companies in the evidence file")


def parse_D(s: str) -> list[str]:
    """2020-2021 WordPress Divi /companies: company names off the portfolio cards."""
    names = []
    for m in re.finditer(r'<h[234][^>]*class="[^"]*(?:et_pb_module_header|company|portfolio)[^"]*"[^>]*>(.*?)</h[234]>', s, re.S):
        t = text_of(m.group(1))
        if t and len(t) < 60:
            names.append(t)
    if not names:
        for m in re.finditer(r'href="https?://(?:www\.)?hvcapital\.com/companies/([a-z0-9-]+)/?"[^>]*>(.*?)</a>', s, re.S):
            t = text_of(m.group(2)) or m.group(1).replace("-", " ").title()
            if t and len(t) < 60:
                names.append(t)
    return list(dict.fromkeys(names))


if __name__ == "__main__":
    {"fetch": fetch, "parse": parse, "fetch_news": fetch_news, "parse_news": parse_news}[sys.argv[1]]()
