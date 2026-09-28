#!/usr/bin/env python3
"""The archive years Common Crawl cannot supply (2000 to 2007, plus 2009 and
2011 where no CC crawl caught the site), from the Internet Archive once its
cooldown lifts. Same row shape and same naming rules as scratch/cc-parse.py
(the firm's own 2013 rendering first, then a curated slug map, then the page's
leading phrase), merged into sources/wayback/parsed/<year>.json by (slug, path),
so the one scheduled rebuild picks the rows up. It also records the capture
years of every people page (scratch/roster-captures.json) so the roster's
tenure windows rest on every year a page was served, not only its first.

Paced by ia_fetch (status-aware, machine-wide cooldown). A failed fetch is
recorded in raw/failures.json and never read as an empty year; exit 3 then,
and a re-run fetches only what is missing (every body is cached in raw/).

Usage: python3 data/collection/investors/sutter-hill-ventures/scratch/ia-eras.py
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
import ia_fetch  # noqa: E402
from paths import Paths, write_atomic  # noqa: E402

P = Paths("sutter-hill-ventures")
RAW = P.wayback / "raw"
DOMAINS = ("shv.com", "sutterhillventures.com")
FAIL: list[str] = []
SEC2000 = {"software.html": ("soft", "Software"), "medicaltech.html": ("mt", "Medical Technology"),
           "networking.html": ("nt", "Networking"), "informationtech.html": ("it", "Information Technology")}
SEC2004 = {"software": "Software", "healthcare": "Healthcare", "networking": "Networking & Computer Technology",
           "business": "Business & Financial Services", "consumer": "Consumer", "investment": "Investment Partnerships"}

# the same naming rules as cc-parse.py
CURATED = {"adexa": "Adexa", "alventive": "Alventive", "atmobile": "@mobile.com",
           "authenticresponse": "Authentic Response", "barrx": "Barrx Medical",
           "brp": "Blue Ridge Pharmaceuticals", "concept": "Concept Shopping", "curis": "Curis",
           "datadomain": "Data Domain", "demandbase": "Demandbase", "freemonee": "FreeMonee",
           "ideas": "IDeaS", "indus": "Indus International", "infomedics": "InfoMedics",
           "interventional": "InterVentional Technologies", "kadoink": "Kadoink",
           "macusight": "MacuSight", "nim": "Networks In Motion", "ourpictures": "OurPictures",
           "pivia": "Pivia", "zilo": "Zilo", "ceon": "Ceon Corporation", "ibalance": "iBalance",
           "networkappliance": "Network Appliance", "grandjunction": "Grand Junction",
           "coppermountain": "Copper Mountain", "primaryaccess": "Primary Access", "k2optronics": "K2 Optronics",
           "banyansystems": "Banyan Systems", "epresence": "ePresence", "lsi": "LSI Logic",
           "linear": "Linear Technology", "mips": "Mips Computer", "pmc": "PMC", "jpkids": "JP Kids",
           "hearme": "HearMe", "erewards": "e-Rewards", "eloyalty": "eLoyalty", "returnpath": "Return Path",
           "quinstreet": "QuinStreet", "wildcard": "WildCard Systems", "facetime": "FaceTime Communications",
           "amberpoint": "AmberPoint", "amber": "AmberPoint", "closedloop": "Closedloop Solutions",
           "digidesign": "Digidesign", "directag": "DirectAg.com", "synapix": "Synapix", "virage": "Virage",
           "vitria": "Vitria Technology", "legato": "Legato Systems", "mentor": "Mentor Graphics",
           "broadvision": "BroadVision", "avant": "Avant!", "avid": "Avid Technology", "clarus": "Clarus",
           "brierley": "Brierley & Partners", "lucy": "Lucy", "lynk": "Lynk", "there": "There",
           "thermawave": "Therma-Wave", "apollo": "Apollo Computer", "celeritek": "Celeritek",
           "dionex": "Dionex", "line6": "Line 6", "omnicell": "Omnicell", "palm": "Palm", "pyxis": "Pyxis",
           "radiance": "Radiance Technologies", "satmetrix": "Satmetrix Systems", "nvidia": "NVIDIA",
           "alteon": "Alteon WebSystems", "onstream": "OnStream Networks", "symmetricom": "Symmetricom",
           "tellabs": "Tellabs", "tollbridge": "TollBridge Technologies", "vivace": "Vivace Networks",
           "infinera": "Infinera", "kineto": "Kineto Wireless", "acacia": "Acacia Venture Partners",
           "aksys": "Aksys", "amerigroup": "AmeriGroup", "amira": "Amira Medical", "amylin": "Amylin",
           "aspect": "Aspect Medical Systems", "cardica": "Cardica", "cor": "COR Therapeutics",
           "corcept": "Corcept Therapeutics", "corixa": "Corixa", "hybritech": "Hybritech", "idexx": "IDEXX",
           "isis": "Isis", "lifescan": "LifeScan", "molecular": "Molecular Devices", "neurex": "Neurex",
           "praecis": "Praecis Pharmaceuticals", "threshold": "Threshold Pharmaceuticals", "vical": "Vical",
           "visionary": "Visionary Design Systems", "ipin": "Ipin", "collabrys": "Collabrys",
           "crossweave": "CrossWeave", "kovair": "Kovair", "saltare": "Saltare", "websentric": "WebSentric",
           "conscium": "Conscium", "iei": "IEI"}
LEAD = re.compile(r"^(.{2,80}?)\s+(?:\(|is\b|was\b|has\b|provides\b|develops\b|designs\b|offers\b|delivers\b|makes\b|"
                  r"enables\b|builds\b|creates\b|operates\b|merged\b|acquired\b|became\b|,\s+(?:a|an|the)\b)")


def slug_of(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", H.unescape(name).lower().replace("&", " and ")).strip("-")


def clean(s: str) -> str:
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    return " ".join(H.unescape(s).replace("\xa0", " ").replace("Â", "").split())


FULL = []
for _f in glob.glob(str(RAW / "*www_shv_com_portfolio_full.html")):
    _b = Path(_f).read_bytes().decode("latin-1", errors="replace")
    FULL += [clean(a) for a in re.findall(r'(?is)<a[^>]+href="#[^"]*"[^>]*>(.*?)</a>', _b) if clean(a)]


def nkey(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", re.sub(r"\b(inc|ltd|llc|corp|corporation|co|the|com)\b\.?", "", H.unescape(s).lower()))


def list_name(slug: str) -> str:
    k = re.sub(r"[^a-z0-9]", "", slug.lower())
    hits = [n for n in FULL if nkey(n) == k] or [n for n in FULL if nkey(n).startswith(k) and len(k) >= 4] \
        or [n for n in FULL if len(nkey(n)) >= 4 and k.startswith(nkey(n))]
    hits = list(dict.fromkeys(hits))
    return hits[0] if len(hits) == 1 else ""


def page_name(body: str, slug: str) -> tuple[str, str]:
    m = re.search(r'(?is)<td class="bodytext">(.*?)</td>', body) or re.search(r"(?is)<body[^>]*>(.*)</body>", body)
    text = clean(m.group(1)) if m else ""
    name = CURATED.get(slug) or list_name(slug)
    if not name and text:
        lm = LEAD.match(text)
        if lm:
            cand = lm.group(1).strip(" ,.")
            if len(cand.split()) <= 6 and nkey(cand)[:3] == re.sub(r"[^a-z0-9]", "", slug)[:3]:
                name = cand
    return name, text[:600]


def fetch(ts: str, url: str) -> str | None:
    f = RAW / f"{ts}-{re.sub(r'[^A-Za-z0-9]+', '_', url.split('//')[-1])[:90]}.html"
    if f.exists() and f.stat().st_size > 0:
        return f.read_bytes().decode("latin-1", errors="replace")
    body, code = ia_fetch.get(f"https://web.archive.org/web/{ts}id_/{url}")
    if code != "200" or not body:
        FAIL.append(f"{code} {ts} {url}")
        return None
    f.write_bytes(body)
    return body.decode("latin-1", errors="replace")


MEMO = RAW / "index-captures.json"


def yearly(path: str) -> dict[int, tuple[str, str]]:
    memo = json.loads(MEMO.read_text()) if MEMO.exists() else {}
    out: dict[int, tuple[str, str]] = {}
    for dom in DOMAINS:
        key = f"{dom}/{path}"
        if key not in memo:
            body, code = ia_fetch.get(f"https://web.archive.org/cdx/search/cdx?url={key}&output=json"
                                      f"&fl=timestamp,original,statuscode&collapse=timestamp:4&filter=statuscode:200")
            if code != "200":
                FAIL.append(f"cdx {code} {key}")
                continue
            try:
                memo[key] = (json.loads(body) if body.strip() else [[]])[1:]
            except json.JSONDecodeError:
                FAIL.append(f"cdx unparsable {key}")
                continue
            write_atomic(MEMO, json.dumps(memo, indent=0))
        for ts, orig, *_ in memo[key]:
            out.setdefault(int(ts[:4]), (ts, orig))
    return out


FIRSTCAP = {}
for dom in DOMAINS:
    for r in json.load(open(P.scratch / f"cdx-{dom}.json"))[1:]:
        if r[2] == "200":
            p = re.sub(r"^https?://[^/]+", "", r[1]).replace(":80", "").split("?")[0]
            FIRSTCAP.setdefault(p, (r[0], r[1]))


def company(prefix: str, slug: str) -> dict:
    name = CURATED.get(slug) or list_name(slug)
    cap = FIRSTCAP.get(f"/{prefix}/{slug}.html") or FIRSTCAP.get(f"/{prefix}/{slug}.htm")
    desc, ts, orig = "", None, None
    if cap:
        ts, orig = cap
        body = fetch(ts, orig)
        if body:
            n2, desc = page_name(body, slug)
            name = name or n2
    return {"name": name, "description": desc, "ts": ts, "orig": orig}


years: dict[int, dict] = {}


def put(y: int, row: dict) -> None:
    years.setdefault(y, {})[(row["slug"], row["path"])] = row


seen: dict[tuple[str, str], dict] = {}
# 2000 to 2003: root sector pages linking /soft/ /mt/ /nt/ /it/ company pages
for page, (prefix, sector) in SEC2000.items():
    for y, (ts, orig) in sorted(yearly(page).items()):
        if not 2000 <= y <= 2004:
            continue
        body = fetch(ts, orig)
        if body is None:
            continue
        n = 0
        for slug in sorted(set(re.findall(rf'href="{prefix}/([a-z0-9_-]+)\.html?"', body))):
            cp = seen.setdefault((prefix, slug), company(prefix, slug))
            row = {"slug": slug_of(cp["name"]) if cp["name"] else slug, "path": f"/{prefix}/{slug}.html",
                   "snapshot_ts": ts, "era": "sector2000", "site_sector": sector,
                   "capture_url": f"https://web.archive.org/web/{cp['ts']}/{cp['orig']}" if cp["ts"]
                   else f"https://web.archive.org/web/{ts}/{orig}"}
            if cp["name"]:
                row["name"] = cp["name"]
            if cp["description"]:
                row["description"] = cp["description"]
            put(y, row)
            n += 1
        print(f"  {page} {y}: {n}", flush=True)
# 2004 to 2012: sector directories (IA years CC lacks: 2004-2007, 2009, 2011)
for sec, sector in SEC2004.items():
    for y, (ts, orig) in sorted(yearly(f"{sec}/index.html").items()):
        if y not in (2004, 2005, 2006, 2007, 2009, 2011):
            continue
        body = fetch(ts, orig)
        if body is None:
            continue
        n = 0
        for slug in sorted(set(re.findall(rf'href="(?:\.\./{sec}/)?([a-z0-9_-]+)\.html?"', body))):
            if slug == "index":
                continue
            cp = seen.setdefault((sec, slug), company(sec, slug))
            row = {"slug": slug_of(cp["name"]) if cp["name"] else slug, "path": f"/{sec}/{slug}.html",
                   "snapshot_ts": ts, "era": "sector2004", "site_sector": sector,
                   "capture_url": f"https://web.archive.org/web/{cp['ts']}/{cp['orig']}" if cp["ts"]
                   else f"https://web.archive.org/web/{ts}/{orig}"}
            if cp["name"]:
                row["name"] = cp["name"]
            if cp["description"]:
                row["description"] = cp["description"]
            put(y, row)
            n += 1
        print(f"  {sec}/index.html {y}: {n}", flush=True)
# the 1999 to 2000 table at its true capture dates
for y, (ts, orig) in sorted(yearly("investments.htm").items()):
    body = fetch(ts, orig)
    if body is None:
        continue
    section, prev, n = "Information Technology", "", 0
    for tr in re.findall(r"(?is)<tr[^>]*>(.*?)</tr>", body):
        cells = [c for c in (clean(c) for c in re.findall(r"(?is)<t[dh][^>]*>(.*?)</t[dh]>", tr)) if c]
        if len(cells) != 3:
            continue
        name, desc, outcome = cells
        first = re.sub(r"[^A-Za-z]", "", name)[:1].upper()
        if prev and first and ord(prev) - ord(first) >= 10:
            section = "Health Care"
        prev = first or prev
        put(y, {"slug": slug_of(name), "name": name, "path": "/investments.htm", "snapshot_ts": ts,
                "era": "table1999", "capture_url": f"https://web.archive.org/web/{ts}/{orig}",
                "description": desc, "site_outcome": outcome, "site_sector": section})
        n += 1
    print(f"  investments.htm {y}: {n}", flush=True)
# people pages: every capture year (roster tenure windows)
people = sorted({p for p in FIRSTCAP if re.match(r"^/(team/)?[a-z]+(-[a-z]+)?\.html?$", p) or
                 re.match(r"^/(andy-sheehan|jeff-bird|jim-white|len-baker|mike-speiser|sam-pullara|stefan-dyckerhoff|tench-coxe)$", p)})
caps = []
for p in people:
    for dom in DOMAINS:
        body, code = ia_fetch.get(f"https://web.archive.org/cdx/search/cdx?url={dom}{p}&output=json"
                                  f"&fl=timestamp,original,statuscode&collapse=timestamp:4&filter=statuscode:200")
        if code != "200":
            FAIL.append(f"cdx {code} {dom}{p}")
            continue
        try:
            caps += (json.loads(body) if body.strip() else [[]])[1:]
        except json.JSONDecodeError:
            FAIL.append(f"cdx unparsable {dom}{p}")
write_atomic(P.scratch / "roster-captures.json", json.dumps(caps, indent=0))
print(f"  people pages: {len(people)} paths, {len(caps)} yearly captures", flush=True)

for y, rows in sorted(years.items()):
    f = P.wayback / "parsed" / f"{y}.json"
    old = {(r["slug"], r["path"]): r for r in json.load(open(f))} if f.exists() else {}
    old.update(rows)
    write_atomic(f, json.dumps(sorted(old.values(), key=lambda r: (r["slug"], r["path"])), indent=1,
                               ensure_ascii=False) + "\n")
    print(f"{y}: {len(old)} rows")
if FAIL:
    write_atomic(RAW / "failures.json", json.dumps(FAIL, indent=1))
    print(f"!! {len(FAIL)} failed fetches in raw/failures.json; re-run before reading any absence", file=sys.stderr)
    sys.exit(3)
