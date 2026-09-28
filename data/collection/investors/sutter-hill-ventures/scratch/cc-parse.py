#!/usr/bin/env python3
"""Sutter Hill's archived portfolio from the captures already on disk, while the
Internet Archive is in a machine-wide cooldown (Erik 2026-09-26: Common Crawl is
the archive fallback then). Writes sources/wayback/parsed/<year>.json rows in
wayback-pull.py's shape, merged by (slug, path) with whatever is there, so the
IA pull (scratch/wayback-eras.py) converges on the same files after recovery.

Sources:
  Common Crawl  sources/wayback/cc-manifest.json (+ data/filings/commoncrawl/sutter-hill-ventures/):
                2008 to 2012 sector directories (/software/index.html ...) and
                their company pages; 2013 to 2017 /portfolio (every company, as
                links into /portfolio-full) and the root company pages (name,
                description, "Managing Director | <name>").
                capture_url = the index.commoncrawl.org form (COLLECTION.md s1).
  IA, cached    sources/wayback/raw/: the 1999 investments table (every
                investment since 1970 with the firm's outcome line), the 2013
                /portfolio-full, the 2004 software index, fetched before the
                cooldown. capture_url = the web.archive.org capture.

Usage: python3 data/collection/investors/sutter-hill-ventures/scratch/cc-parse.py
"""
from __future__ import annotations

import glob
import html as H
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

P = Paths("sutter-hill-ventures")
CCRAW = ROOT / "data" / "filings" / "commoncrawl" / "sutter-hill-ventures"
MAN = json.loads((P.wayback / "cc-manifest.json").read_text())
SECTORS = {"software": "Software", "healthcare": "Healthcare", "networking": "Networking & Computer Technology",
           "business": "Business & Financial Services", "consumer": "Consumer",
           "investment": "Investment Partnerships"}
NICK = {"Jeffrey": "Jeff", "Michael": "Mike", "Andrew": "Andy", "Samuel": "Sam",
        "James": "Jim", "Gregory": "Greg", "Ronald": "Ron", "Leonard": "Len"}


def slug_of(name: str) -> str:
    s = H.unescape(name).lower().replace("&", " and ")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def clean(s: str) -> str:
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    s = H.unescape(s).replace("\xa0", " ").replace("Â", "")
    return " ".join(s.split())


def roster_map() -> dict:
    out = {}
    for r in json.load(open(P.wayback / "partner-roster.json")):
        toks = [t.rstrip(".,") for t in r["name"].split()]
        toks = [t for t in toks if t not in ("Jr", "III") and len(t) > 1]
        first, last = toks[0], toks[-1]
        names = {first, NICK.get(first, first)}
        if len(toks) > 2:
            names |= {toks[1], NICK.get(toks[1], toks[1])}
        for f in names:
            out[f"{f} {last}".lower()] = r["slug"]
    return out


ROSTER = roster_map()
years: dict[int, dict] = {}


def put(year: int, row: dict) -> None:
    years.setdefault(year, {})[(row["slug"], row["path"])] = row


def cc_items(path_re: str):
    for k, v in sorted(MAN.items(), key=lambda kv: kv[1]["timestamp"]):
        if v.get("status") == "ok" and re.search(path_re, v["path"]):
            yield k, v, (CCRAW / k).read_bytes().decode("latin-1", errors="replace")


# ---- company pages, 2008 to 2012 (CC) and 2004 (IA cache): name and description.
# The page's markup varies ("<a class=bodylinklight>AkaRx, Inc.</a> is developing",
# "Virage was acquired by <span class=bodylink>Autonomy</span>", "<span class=bodylink>Artisan
# Partners Limited Partnership</span> (Artisan Partners) is"), and a bold or linked name can be the
# ACQUIRER. So the name is (1) the firm's own rendering on the 2013 full list whose normalised form
# matches the page's file slug, else (2) the page text's leading phrase before its first verb, else
# (3) nothing (the build names the row from the slug and the judge names it). The whole text is kept
# as the description: it carries the firm's outcome lines ("was acquired by Autonomy").
LEAD = re.compile(r"^(.{2,80}?)\s+(?:\(|is\b|was\b|has\b|provides\b|develops\b|designs\b|offers\b|delivers\b|makes\b|"
                  r"enables\b|builds\b|creates\b|operates\b|merged\b|acquired\b|became\b|,\s+(?:a|an|the)\b)")
FULL_NAMES: list[str] = []
for _f in glob.glob(str(P.wayback / "raw" / "*www_shv_com_portfolio_full.html")):
    _b = Path(_f).read_bytes().decode("latin-1", errors="replace")
    FULL_NAMES += [clean(a) for a in re.findall(r'(?is)<a[^>]+href="#[^"]*"[^>]*>(.*?)</a>', _b) if clean(a)]


def nkey(s: str) -> str:
    s = re.sub(r"\b(inc|ltd|llc|corp|corporation|co|the|com)\b\.?", "", H.unescape(s).lower())
    return re.sub(r"[^a-z0-9]", "", s)


def list_name(slug: str) -> str:
    k = re.sub(r"[^a-z0-9]", "", slug.lower())
    hits = [n for n in FULL_NAMES if nkey(n) == k] or \
           [n for n in FULL_NAMES if nkey(n).startswith(k) and len(k) >= 4] or \
           [n for n in FULL_NAMES if len(nkey(n)) >= 4 and k.startswith(nkey(n))]
    hits = list(dict.fromkeys(hits))
    return hits[0] if len(hits) == 1 else ""


# Curated names for directory file slugs the firm's own lists never render and
# whose page text names no company cleanly (COLLECTION.md s5: fix filename
# variants in the PARSED SOURCE, before the build). Read off each page's text,
# the 1999 table or the 2013 list; e.g. /healthcare/brp.html is "Blue Ridge
# Pharmaceuticals is a U.S.-based company ...", /investment/indus.html is Indus
# International (merged with MDSI into Ventyx, 2007).
CURATED = {"adexa": "Adexa", "alventive": "Alventive", "atmobile": "@mobile.com",
           "authenticresponse": "Authentic Response", "barrx": "Barrx Medical",
           "brp": "Blue Ridge Pharmaceuticals", "concept": "Concept Shopping", "curis": "Curis",
           "datadomain": "Data Domain", "demandbase": "Demandbase", "freemonee": "FreeMonee",
           "ideas": "IDeaS", "indus": "Indus International", "infomedics": "InfoMedics",
           "interventional": "InterVentional Technologies", "kadoink": "Kadoink",
           "macusight": "MacuSight", "nim": "Networks In Motion", "ourpictures": "OurPictures",
           "pivia": "Pivia", "zilo": "Zilo", "ceon": "Ceon Corporation", "ibalance": "iBalance"}


def company_name(body: str, slug: str) -> tuple[str, str]:
    m = re.search(r'(?is)<td class="bodytext">(.*?)</td>', body)
    text = clean(m.group(1)) if m else ""
    name = CURATED.get(slug) or list_name(slug)
    if not name and text:
        lm = LEAD.match(text)
        if lm:
            cand = lm.group(1).strip(" ,.")
            if len(cand.split()) <= 6 and nkey(cand)[:3] == re.sub(r"[^a-z0-9]", "", slug.lower())[:3]:
                name = cand
    return name, text[:600]


pages: dict[tuple[str, str], dict] = {}
for k, v, body in cc_items(r"^/(software|healthcare|networking|business|consumer|investment)/[a-z0-9_-]+\.html?$"):
    sec, fn = v["path"].strip("/").split("/")
    slug = fn.rsplit(".", 1)[0]
    if slug == "index":
        continue
    name, desc = company_name(body, slug)
    if (name or desc) and (sec, slug) not in pages:
        pages[(sec, slug)] = {"name": name, "description": desc, "capture_url": v["capture_url"],
                              "ts": v["timestamp"]}
for f in glob.glob(str(P.wayback / "raw" / "*.html")):
    m = re.search(r"/(\d{14})-www_shv_com_(software|healthcare|networking|business|consumer|investment)_([a-z0-9_-]+)_html\.html$", f)
    if not m or m.group(3) == "index":
        continue
    body = Path(f).read_bytes().decode("latin-1", errors="replace")
    name, desc = company_name(body, m.group(3))
    if (name or desc) and (m.group(2), m.group(3)) not in pages:
        pages[(m.group(2), m.group(3))] = {
            "name": name, "description": desc, "ts": m.group(1),
            "capture_url": f"https://web.archive.org/web/{m.group(1)}/http://www.shv.com/{m.group(2)}/{m.group(3)}.html"}

# ---- sector index pages, per capture year: which companies were listed
def sector_index(body: str, sec: str, ts: str, cap: str, era: str) -> int:
    n = 0
    for slug in sorted(set(re.findall(rf'href="(?:\.\./{sec}/)?([a-z0-9_-]+)\.html?"', body))):
        if slug == "index":
            continue
        cp = pages.get((sec, slug)) or ({"name": CURATED.get(slug) or list_name(slug), "description": "",
                                         "capture_url": cap} if (CURATED.get(slug) or list_name(slug)) else None)
        row = {"slug": slug_of(cp["name"]) if cp and cp["name"] else slug, "path": f"/{sec}/{slug}.html",
               "snapshot_ts": ts, "era": era, "capture_url": cp["capture_url"] if cp else cap,
               "site_sector": SECTORS[sec]}
        if cp and cp["name"]:
            row["name"] = cp["name"]
        if cp and cp["description"]:
            row["description"] = cp["description"]
        put(int(ts[:4]), row)
        n += 1
    return n


for k, v, body in cc_items(r"^/(software|healthcare|networking|business|consumer|investment)/(index\.html)?$"):
    sec = v["path"].strip("/").split("/")[0]
    n = sector_index(body, sec, v["timestamp"], v["capture_url"], "sector2004")
    print(f"  cc sector {sec} {v['timestamp'][:8]}: {n}")
for f in glob.glob(str(P.wayback / "raw" / "*_index_html.html")):
    m = re.search(r"/(\d{14})-www_shv_com_(software|healthcare|networking|business|consumer|investment)_index_html\.html$", f)
    if not m:
        continue
    body = Path(f).read_bytes().decode("latin-1", errors="replace")
    cap = f"https://web.archive.org/web/{m.group(1)}/http://www.shv.com/{m.group(2)}/index.html"
    n = sector_index(body, m.group(2), m.group(1), cap, "sector2004")
    print(f"  ia sector {m.group(2)} {m.group(1)[:8]}: {n}")

# ---- 2013 to 2017: /portfolio (names as links into /portfolio-full) and /portfolio-full
def md_of(seg: str) -> str:
    mm = re.search(r"Managing Director\s*\|?\s*([A-Z][a-z]+ [A-Z][A-Za-z]+)", seg)
    return mm.group(1) if mm else ""


ANCHOR_NAME: dict[str, str] = {}


def anchor_key(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", H.unescape(s).lower())


def drupal_list(body: str, ts: str, cap: str, path: str) -> int:
    pairs = re.findall(r'(?is)<a[^>]+href="(?:http://www\.shv\.com/portfolio-full)?#([^"]*)"[^>]*>(.*?)</a>', body)
    names = []
    for anchor, inner in pairs:
        nm = clean(inner)
        if nm:
            ANCHOR_NAME.setdefault(anchor_key(anchor), nm)
        else:
            # the 2013 to 2017 /portfolio grid links a logo with alt="": the
            # anchor is the only text, so name it from the full list's own
            # rendering, else from the company's page title, else split the
            # anchor's CamelCase ("BenuNetworksInc" -> "Benu Networks Inc")
            nm = ANCHOR_NAME.get(anchor_key(anchor)) or re.sub(r"(?<=[a-z])(?=[A-Z])", " ", H.unescape(anchor))
            nm = {"Inventional Technologies": "InterVentional Technologies"}.get(nm, nm)
        names.append(nm)
    text = clean(re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", body))
    n = 0
    for name in dict.fromkeys(names):
        if not name or name.lower() in ("portfolio", "clear filter"):
            continue
        row = {"slug": slug_of(name), "name": name, "path": path, "snapshot_ts": ts,
               "era": "drupal2013", "capture_url": cap}
        i = text.find(name + " " + name)
        if i >= 0:
            seg = text[i + 2 * len(name) + 1:i + 1600]
            nxt = min([seg.find(o + " " + o) for o in names if o != name and seg.find(o + " " + o) > 0] or [len(seg)])
            seg = seg[:nxt]
            md = md_of(seg)
            if md:
                row["site_md"] = md
                if ROSTER.get(md.lower()):
                    row["filters"] = ROSTER[md.lower()]
            desc = re.sub(r"\s*Managing Director.*$", "", seg).strip(" |")
            if desc:
                row["description"] = desc[:600]
        put(int(ts[:4]), row)
        n += 1
    return n


for f in glob.glob(str(P.wayback / "raw" / "*www_shv_com_portfolio*.html")):
    m = re.search(r"/(\d{14})-www_shv_com_(portfolio(?:_full)?)\.html$", f)
    if not m:
        continue
    path = "/" + m.group(2).replace("_", "-")
    body = Path(f).read_bytes().decode("latin-1", errors="replace")
    cap = f"https://web.archive.org/web/{m.group(1)}/http://www.shv.com{path}"
    print(f"  ia {path} {m.group(1)[:8]}: {drupal_list(body, m.group(1), cap, path)}")

# root company pages 2013 to 2017: "<Name> | Sutter Hill Ventures", description, MD
NONCO = {"approach", "directions", "meet-team", "team", "portfolio", "portfolio-full", "index.html", "about.html",
         "contact.html", "news.html", "philosophy.html", "doing_business.html", "portfolio.html", "team.html", ""}
for k, v, body in cc_items(r"^/[a-z0-9-]+$"):
    seg = v["path"].strip("/")
    if seg in NONCO or seg.endswith(".html"):
        continue
    t = re.search(r"(?is)<title>(.*?)\|\s*Sutter Hill Ventures</title>", body)
    if not t:
        continue
    name = clean(t.group(1))
    text = clean(re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", body))
    if any(n in name for n in ("Approach", "Team", "Portfolio", "Directions")) or ROSTER.get(name.lower()):
        continue  # a person's page or navigation
    i = text.rfind(name)
    seg2 = text[i + len(name):] if i >= 0 else ""
    md = md_of(seg2)
    row = {"slug": slug_of(name), "name": name, "path": v["path"], "snapshot_ts": v["timestamp"],
           "era": "drupal2013", "capture_url": v["capture_url"]}
    desc = re.sub(r"\s*(Managing Director|©|&copy;).*$", "", seg2).strip(" |")
    if desc:
        row["description"] = desc[:600]
    if md:
        row["site_md"] = md
        if ROSTER.get(md.lower()):
            row["filters"] = ROSTER[md.lower()]
    put(int(v["timestamp"][:4]), row)

for _k, _v, _b in cc_items(r"^/[a-z0-9-]+$"):
    _t = re.search(r"(?is)<title>(.*?)\|\s*Sutter Hill Ventures</title>", _b)
    if _t:
        ANCHOR_NAME.setdefault(anchor_key(clean(_t.group(1))), clean(_t.group(1)))
for k, v, body in cc_items(r"^/portfolio(-full)?$"):
    print(f"  cc {v['path']} {v['timestamp'][:8]}: {drupal_list(body, v['timestamp'], v['capture_url'], v['path'])}")

# ---- the 1999 table (IA cache): every investment since 1970 with the firm's outcome line
for f in glob.glob(str(P.wayback / "raw" / "*investments_htm.html")):
    ts = re.search(r"/(\d{14})-", f).group(1)
    body = Path(f).read_bytes().decode("latin-1", errors="replace")
    section, prev, n = "Information Technology", "", 0
    for tr in re.findall(r"(?is)<tr[^>]*>(.*?)</tr>", body):
        cells = [clean(c) for c in re.findall(r"(?is)<t[dh][^>]*>(.*?)</t[dh]>", tr)]
        cells = [c for c in cells if c]
        if len(cells) != 3:
            continue
        name, desc, outcome = cells
        first = re.sub(r"[^A-Za-z]", "", name)[:1].upper()
        if prev and first and ord(prev) - ord(first) >= 10:
            section = "Health Care"
        prev = first or prev
        put(1999, {"slug": slug_of(name), "name": name, "path": "/investments.htm", "snapshot_ts": ts,
                   "era": "table1999", "capture_url": f"https://web.archive.org/web/{ts}/http://www.shv.com/investments.htm",
                   "description": desc, "site_outcome": outcome, "site_sector": section})
        n += 1
    print(f"  ia /investments.htm {ts[:8]}: {n}")

(P.wayback / "parsed").mkdir(parents=True, exist_ok=True)
for y, rows in sorted(years.items()):
    f = P.wayback / "parsed" / f"{y}.json"
    old = {(r["slug"], r["path"]): r for r in json.load(open(f))} if f.exists() else {}
    old.update(rows)
    write_atomic(f, json.dumps(sorted(old.values(), key=lambda r: (r["slug"], r["path"])), indent=1,
                               ensure_ascii=False) + "\n")
    print(f"{y}: {len(old)} rows ({len({r['slug'] for r in old.values()})} companies)")
