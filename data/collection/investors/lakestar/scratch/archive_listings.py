#!/usr/bin/env python3
"""Parse the archived lakestar.com captures into the base builder's inputs.

Captures come from two archives, both recorded in manifests:
  Common Crawl      data/filings/commoncrawl/lakestar/<crawl>/<ts>-<path>.html
                    (sources/wayback/cc-manifest.json; capture_url in the
                    index.commoncrawl.org form)
  Internet Archive  sources/wayback/raw/ia/<ts>-<path>.html
                    (sources/wayback/ia-manifest.json; web.archive.org URL)

Site generations and what each carries:
  2011-2013  WordPress: /portfolio (a list) and /portfolio/<slug> pages.
  2018-2019  single page: a logo strip on the homepage (img alt = the name).
  2020-2021  /about "Portfolio highlights" (article.logo, img alt or h3
             title), the homepage's featured cards, and /team, where every
             investing person carries a "Companies" list: the firm's own
             per-partner attribution.
  2022-2026  Next.js on Craft CMS: /portfolio carries the whole companies
             array (title, slug, stage, thesis, urlReference), /company/<slug>
             the company with its teamMembers, /team allTeamMembers with
             position, /team/<slug> the person with companies and boardSeats.
             Read from __NEXT_DATA__ (2022 to mid-2024) or the RSC payload
             (late 2024 on); both hold the same JSON.

Outputs:
  sources/wayback/parsed/<year>.json   one row per company per capture year
       {slug, name, path, snapshot_ts, capture_url, filters}  (builder input;
       filters carries the deal partners' roster slugs)
  sources/wayback/archive-evidence.json  per company: every stage and thesis
       value the CMS ever showed (with capture dates), website, the deal
       partners, the firm's own sentence, linked insights
  scratch/team-archive.json            per person: positions by capture year,
       companies, board seats

Names are reconciled in the PARSED SOURCE through ALIASES (COLLECTION.md s5:
variants of one company are best fixed before the build, so the published
surface never carries the junk spelling).
"""
import html as htmlmod
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

WB = INV / "sources" / "wayback"
CC_RAW = ROOT / "data" / "filings" / "commoncrawl" / "lakestar"

# variant (lowercased) -> the name the firm's 2022-2026 CMS uses (or the
# company's own name where the CMS never carried it)
ALIASES = {
    "blockchain.com": "Blockchain", "five ai": "Five", "fiveai": "Five", "five.ai": "Five",
    "engineer.ai": "Builder.ai", "goeuro": "Omio", "solarisbank": "Solarisbank",
    "getyourguide": "GetYourGuide", "harrys": "Harry's", "harry’s": "Harry's",
    "marleyspoon": "Marley Spoon", "eigen": "Eigen Technologies",
    "nebenan.de": "Nebenan", "shapeshift": "Shapeshift", "zebedee": "ZBD", "fuse": "Fuse Energy",
    "arx robotics": "ARX Robotics", "xing": "Xing", "global leads group": "Global Leads Group", "oscar": "Oscar Health", "eigen technologies": "Eigen Technologies",
    "sennder": "Sennder", "hometogo1": "HomeToGo", "taulialogo": "Taulia",
    "welend": "WeLend", "king": "King", "sofi": "SoFi", "plus dental": "PlusDental",
    "one football": "OneFootball", "heaven hr": "HeavenHR", "mc makler": "McMakler",
    "dashdash": "Rows", "accurx": "AccuRx", "botsandus": "Dexory", "bots and us": "Dexory",
    "kinta": "Kinta AI", "mcmakler": "McMakler", "glovo": "Glovo", "limehome": "Limehome",
    "oneshot.earth": "oneshot.earth", "terraquantum": "Terra Quantum",
    "maker studios": "Maker Studios", "makerstudios": "Maker Studios",
    "priori data": "Priori Data", "prioridata": "Priori Data",
    "profit bricks": "ProfitBricks", "true motion": "TrueMotion",
}


def canon(name: str) -> str:
    n = htmlmod.unescape(name or "").strip()
    n = re.sub(r"\s+", " ", n)
    return ALIASES.get(n.lower(), n)


def slug_of(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def captures():
    out = []
    cm = WB / "cc-manifest.json"
    if cm.exists():
        for key, v in json.loads(cm.read_text()).items():
            if v.get("status") == "ok" and (CC_RAW / key).exists():
                out.append({"src": "cc", "file": CC_RAW / key, "ts": v["timestamp"], "url": v["url"],
                            "capture_url": v["capture_url"]})
    im = WB / "ia-manifest.json"
    if im.exists():
        for key, v in json.loads(im.read_text()).items():
            f = WB / "raw" / "ia" / f"{key}.html"
            if v.get("status") == "ok" and f.exists():
                out.append({"src": "ia", "file": f, "ts": v["timestamp"], "url": v["url"],
                            "capture_url": v["capture_url"]})
    for c in out:
        p = re.sub(r"^https?://(www\.)?lakestar\.com(:\d+)?", "", c["url"])
        c["path"] = "/" + p.split("?")[0].strip("/")
        c["query"] = p.split("?", 1)[1] if "?" in p else ""
    return sorted(out, key=lambda c: (c["ts"], c["path"]))


def page_json_text(h: str) -> str:
    """The page's data as one JSON-ish text: __NEXT_DATA__ where present,
    else the concatenated RSC payload strings, unescaped."""
    m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', h, re.S)
    if m:
        return m.group(1)
    parts = []
    for ch in re.findall(r'self\.__next_f\.push\(\[1,("(?:[^"\\]|\\.)*")\]\)', h, re.S):
        try:
            parts.append(json.loads(ch))
        except ValueError:
            pass
    return "".join(parts)


def find_values(txt: str, key_re: str):
    """Every JSON value stored under a key matching key_re, by raw decode."""
    dec = json.JSONDecoder()
    out = []
    for m in re.finditer(r'"(' + key_re + r')":\s*(?=[\[{])', txt):
        try:
            val, _ = dec.raw_decode(txt, m.end())
        except ValueError:
            continue
        out.append((m.group(1), val))
    return out


def strip_tags(s: str) -> str:
    return re.sub(r"\s+", " ", htmlmod.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()


def main() -> None:
    caps = captures()
    rows = defaultdict(dict)          # year -> slug -> row
    ev = {}                           # slug -> evidence
    people = {}                       # person slug -> record

    def company(name, cap, cms_slug=None, website=None, partners=(), stage=None, thesis=None,
                intro=None, surface=None):
        name = canon(name)
        if not name:
            return
        slug = slug_of(name)
        year = cap["ts"][:4]
        r = rows[year].get(slug)
        if r is None or cap["ts"] < r["snapshot_ts"]:
            keep = r["_partners"] if r else set()
            rows[year][slug] = r = {"slug": slug, "name": name, "path": cap["path"],
                                    "snapshot_ts": cap["ts"], "capture_url": cap["capture_url"],
                                    "_partners": keep}
        r["_partners"].update(partners)
        e = ev.setdefault(slug, {"name": name, "cms_slugs": [], "websites": [], "stages": {},
                                 "theses": {}, "partners": {}, "intro": "", "surfaces": {},
                                 "first_capture": cap["ts"], "last_capture": cap["ts"],
                                 "first_capture_url": cap["capture_url"], "insights": []})
        if cap["ts"] < e["first_capture"]:
            e["first_capture"], e["first_capture_url"] = cap["ts"], cap["capture_url"]
        e["last_capture"] = max(e["last_capture"], cap["ts"])
        if cms_slug and cms_slug not in e["cms_slugs"]:
            e["cms_slugs"].append(cms_slug)
        if website and website not in e["websites"]:
            e["websites"].append(website)
        if stage is not None:
            e["stages"].setdefault(" | ".join(stage) or "(none)", []).append(cap["ts"][:8])
            e.setdefault("stage_urls", {}).setdefault(" | ".join(stage) or "(none)", cap["capture_url"])
        if thesis:
            for t in thesis:
                e["theses"].setdefault(t, []).append(cap["ts"][:8])
        for p in partners:
            e["partners"].setdefault(p, []).append(cap["ts"][:8])
        if intro and len(intro) > len(e["intro"]):
            e["intro"] = intro
        if surface:
            e["surfaces"].setdefault(surface, []).append(cap["ts"][:8])

    def person(name, cap, position=None, slug=None, companies=(), board=(), group=None):
        name = re.sub(r"\s+", " ", htmlmod.unescape(name or "")).strip()
        if not name:
            return
        ps = slug or slug_of(name)
        p = people.setdefault(ps, {"slug": ps, "name": name, "positions": {}, "years": set(),
                                   "companies": set(), "board_seats": set(), "groups": set()})
        p["years"].add(int(cap["ts"][:4]))
        if position:
            p["positions"].setdefault(position.strip(), []).append(cap["ts"][:8])
        p["companies"].update(canon(c) for c in companies if c)
        p["board_seats"].update(canon(c) for c in board if c)
        if group:
            p["groups"].add(group)

    stats = defaultdict(int)
    for cap in caps:
        h = cap["file"].read_text(encoding="utf-8", errors="replace")
        path = cap["path"]
        year = cap["ts"][:4]
        # ---- 2011-2013 WordPress site: /portfolio (list) and /portfolio/<slug> pages
        if year <= "2013":
            body = re.sub(r"<script.*?</script>|<style.*?</style>", " ", h, flags=re.S)
            if path == "/portfolio":
                for slug13, nm in re.findall(r'href="[^"]*?/portfolio/([a-z0-9-]+)/?"[^>]*>\s*(?:<[^>]+>\s*)*([^<]{2,60}?)\s*<', body):
                    if nm.strip() and len(nm.strip()) <= 22 and not nm.strip().endswith(".") \
                            and slug13 not in ("feed", "search") and nm.strip().lower() != "search":
                        company(nm.strip(), cap, surface="site-2013")
                        stats["site-2013-list"] += 1
            elif path.startswith("/portfolio/"):
                t = htmlmod.unescape(re.sub(r"<[^>]+>", "\n", body))
                t = re.sub(r"\n\s*\n+", "\n", t)
                m = re.search(r"Portfolio\n > ([^\n]+)\n(.*?)\nSearch\n", t, re.S)
                if m:
                    desc = re.sub(r"\s+", " ", m.group(2)).strip()
                    site = re.search(r"https?://\S+", desc)
                    company(m.group(1).strip(), cap, website=site.group(0) if site else None,
                            intro=desc[:400], surface="site-2013")
                    stats["site-2013-page"] += 1
                else:
                    ttl = re.search(r"<title>\s*([^|<]+?)\s*[|<]", h)
                    if ttl and ttl.group(1).strip().lower() not in ("lakestar", "portfolio", "page not found"):
                        company(ttl.group(1).strip(), cap, surface="site-2013")
                        stats["site-2013-title"] += 1
            continue
        # ---- 2018-2021 server-rendered site
        if year <= "2021":
            if path == "/":
                for href, alt in re.findall(
                        r'<a href="([^"]*)"[^>]*class="logos__link">\s*<img[^>]*alt="([^"]+)"', h):
                    company(alt, cap, website=href, surface="home-logos")
                    stats["home-logos"] += 1
            for art in re.findall(r'<article class="component logo[^"]*"[^>]*>(.*?)</article>', h, re.S):
                m = re.search(r'<h3 class="logo__title">\s*(.*?)\s*</h3>', art, re.S) or \
                    re.search(r'<img[^>]*alt="([^"]+)"', art)
                if not m:
                    continue
                link = re.search(r'<a href="([^"]+)"[^>]*class="logo__link"', art)
                intro = re.search(r'<div class="logo__content">\s*(.*?)\s*</div>', art, re.S)
                company(strip_tags(m.group(1)), cap, website=link.group(1) if link else None,
                        intro=strip_tags(intro.group(1)) if intro else None,
                        surface="about-highlights" if path == "/about" else "home-featured")
                stats["logo-articles"] += 1
            if path == "/team":
                for art in re.findall(r'<article class="component team team--modal">(.*?)</article>', h, re.S):
                    nm = re.search(r'<h2 class="team__heading[^>]*>\s*(.*?)\s*</h2>', art, re.S)
                    role = re.search(r'<h3 class="team__role[^>]*>\s*(.*?)\s*</h3>', art, re.S)
                    comp = re.search(r"<h3>Companies</h3>\s*<ul[^>]*>(.*?)</ul>", art, re.S)
                    comps = [strip_tags(x) for x in re.findall(r"<li>(.*?)</li>", comp.group(1), re.S)] if comp else []
                    if not nm:
                        continue
                    pname = strip_tags(nm.group(1))
                    person(pname, cap, position=strip_tags(role.group(1)) if role else None, companies=comps)
                    for c in comps:
                        company(c, cap, partners=[slug_of(pname)], surface="team-companies")
                        stats["team-companies"] += 1
                # cards without a modal (operations staff, advisors) still name a person
                for nm, role in re.findall(
                        r'<h2 class="team__heading[^>]*>\s*(.*?)\s*</h2>\s*<h3 class="team__role[^>]*>\s*(.*?)\s*</h3>',
                        h, re.S):
                    person(strip_tags(nm), cap, position=strip_tags(role))
            continue
        # ---- 2022-2026 Next.js / Craft CMS
        txt = page_json_text(h)
        if not txt:
            stats["no-json"] += 1
            continue
        if path == "/portfolio" or path.startswith("/thesis/") or path == "/":
            for key, arr in find_values(txt, r"companies_\d+|companies"):
                if not isinstance(arr, list):
                    continue
                for c in arr:
                    if not isinstance(c, dict) or c.get("typeHandle") not in (None, "portfolio") or not c.get("title"):
                        continue
                    company(c["title"], cap, cms_slug=c.get("slug"), website=c.get("urlReference"),
                            stage=[s.get("title") for s in (c.get("stage") or [])] if path == "/portfolio" else None,
                            thesis=[t.get("title") for t in (c.get("thesis") or [])],
                            intro=strip_tags(c.get("introduction") or ""),
                            surface="portfolio" if path == "/portfolio" else "thesis-or-home")
                    stats["cms-list"] += 1
        if path.startswith("/company/"):
            for key, c in find_values(txt, r"company"):
                if not isinstance(c, dict) or not c.get("title") or "teamMembers" not in c:
                    continue
                tms = c.get("teamMembers") or []
                for t in tms:
                    person(t.get("fullName"), cap, position=t.get("position"), slug=t.get("slug"),
                           companies=[c["title"]])
                company(c["title"], cap, cms_slug=c.get("slug"), website=c.get("urlReference"),
                        partners=[t.get("slug") for t in tms if t.get("slug")],
                        thesis=[t.get("title") for t in (c.get("thesis") or [])],
                        intro=strip_tags(c.get("sectionContent") or ""), surface="company-page")
                stats["company-page"] += 1
                e = ev[slug_of(canon(c["title"]))]
                for key2, ins in find_values(txt, r"insights"):
                    for i in ins if isinstance(ins, list) else []:
                        rec = {"title": i.get("title"), "date": (i.get("postDate") or "")[:10],
                               "uri": i.get("uri"), "external": i.get("externalUrl")}
                        if rec not in e["insights"]:
                            e["insights"].append(rec)
                break
        if path == "/team":
            for key, arr in find_values(txt, r"allTeamMembers|allAdvisors"):
                for p in arr if isinstance(arr, list) else []:
                    if isinstance(p, dict) and p.get("fullName"):
                        person(p["fullName"], cap, position=p.get("position"), slug=p.get("slug"),
                               group="advisor" if key == "allAdvisors" else "team")
                        stats["team-list"] += 1
        if path.startswith("/team/"):
            mem = [v for k, v in find_values(txt, r"member") if isinstance(v, dict) and v.get("fullName")]
            if mem:
                m0 = mem[0]
                comps = [c.get("title") for k, arr in find_values(txt, r"companies|keyCompanies")
                         for c in (arr if isinstance(arr, list) else []) if isinstance(c, dict) and c.get("title")]
                board = [c.get("title") for k, arr in find_values(txt, r"boardSeats")
                         for c in (arr if isinstance(arr, list) else []) if isinstance(c, dict) and c.get("title")]
                person(m0["fullName"], cap, position=m0.get("position"), slug=m0.get("slug"),
                       companies=comps, board=board)
                for c in set(comps) | set(board):
                    company(c, cap, partners=[m0.get("slug") or slug_of(m0["fullName"])], surface="person-page")
                stats["person-page"] += 1

    # ---- write
    (WB / "parsed").mkdir(parents=True, exist_ok=True)
    for f in (WB / "parsed").glob("*.json"):
        f.unlink()
    for year in sorted(rows):
        out = []
        for slug, r in sorted(rows[year].items()):
            r = dict(r)
            r["filters"] = ",".join(sorted(r.pop("_partners")))
            out.append(r)
        write_atomic(WB / "parsed" / f"{year}.json", json.dumps(out, indent=1, ensure_ascii=False) + "\n")
        print(f"  {year}: {len(out)} companies")
    write_atomic(WB / "archive-evidence.json", json.dumps(
        {"_readme": __doc__.split("Outputs:")[0].strip(), "companies": dict(sorted(ev.items()))},
        indent=1, ensure_ascii=False) + "\n")
    ppl = []
    for p in sorted(people.values(), key=lambda p: p["slug"]):
        p = dict(p)
        p["years"] = sorted(p["years"])
        p["companies"] = sorted(p["companies"])
        p["board_seats"] = sorted(p["board_seats"])
        p["groups"] = sorted(p["groups"])
        ppl.append(p)
    write_atomic(HERE / "team-archive.json", json.dumps(ppl, indent=1, ensure_ascii=False) + "\n")
    print(f"captures read: {len(caps)}; companies: {len(ev)}; people: {len(ppl)}; {dict(stats)}")


if __name__ == "__main__":
    main()
