"""Helpers for the Project A grind (PRO-102), adapted from HV Capital's (PRO-104):
build .out.jsonl lines under the current record contract (COLLECTION.md s6/s8).

A member needs TWO lines: the verdict line and a classification line (record
routes a line by the presence of `verdict`; a single line carrying both drops
every classification key). `cls()` emits only the keys it is given.

Citations are copied from files on disk or tool results, never typed: the live
CMS listing (LISTING), an archive capture (`firm_cite`, `cap`), a press-archive
post (`post`), or a Google News item the surfaces layer found (`gn`).
"""
from __future__ import annotations

import importlib.util
import json
import re
import subprocess
from pathlib import Path

WHO = "agent-judge-pro102"
H = Path(__file__).resolve().parent
INV = H.parent
ROOT = INV.parents[3]
Q = H / "queue"
LISTING = "https://www.project-a.vc/companies"
ASOF = "2026-09-30"

_spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
_gs = None


def _gsmod():
    global _gs
    if _gs is None:
        import sys
        argv = sys.argv
        sys.argv = sys.argv[:1]
        _gs = importlib.util.module_from_spec(_spec)
        _spec.loader.exec_module(_gs)
        sys.argv = argv
    return _gs


def _load(p, default):
    p = Path(p)
    return json.loads(p.read_text()) if p.exists() else default


SURF = _load(H / "graduation-surfaces.json", {})
EV = _load(INV / "sources/wayback/archive-evidence.json", {"companies": {}})["companies"]
POSTS = _load(INV / "sources/site/press-archive.json", {"posts": {}})["posts"]
_DEC = H / "gn-decode.json"
DEC = _load(_DEC, {})


def _k(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


LIVE = {}
for _r in _load(INV / "sources/site/companies-2026.json", {"rows": []})["rows"]:
    LIVE[_k(_r["name"])] = _r
    if _r.get("cms_slug"):
        LIVE.setdefault(_k(_r["cms_slug"]), _r)

CC = {"Germany": "DE", "United Kingdom": "GB", "UK": "GB", "United States": "US", "USA": "US", "US": "US",
      "Netherlands": "NL", "The Netherlands": "NL", "France": "FR", "Switzerland": "CH", "Spain": "ES",
      "Austria": "AT", "Denmark": "DK", "Singapore": "SG", "Sweden": "SE", "Finland": "FI", "Italy": "IT",
      "Brazil": "BR", "Estonia": "EE", "Belgium": "BE", "Portugal": "PT", "Ireland": "IE", "Poland": "PL",
      "Norway": "NO", "Luxembourg": "LU", "Israel": "IL", "Canada": "CA", "Peru": "PE", "Japan": "JP",
      "Australia": "AU", "Czech Republic": "CZ", "India": "IN", "Turkey": "TR", "Greece": "GR", "Ukraine": "UA"}
CITY_FIX = {"München": "Munich", "Köln": "Cologne", "Zürich": "Zurich", "Hannover": "Hanover", "Wien": "Vienna",
            "Frankfurt am Main": "Frankfurt", "Frankfurt": "Frankfurt", "São Paulo": "São Paulo",
            "Neustadt": "Neustadt an der Aisch", "Hackney": "London"}


def live(slug, name=None):
    return LIVE.get(_k(slug)) or LIVE.get(_k(name))


def ev(slug):
    return EV.get(slug) or {}


def fields(slug, key):
    """Values of one archive field for a row, oldest capture first: [(value, capture_url)]."""
    f = (ev(slug).get("fields") or {}).get(key) or {}
    return list(f.items())


def cap(slug, last=True):
    """The row's first or last archived listing capture (URL)."""
    e = ev(slug)
    c = e.get("last_capture" if last else "first_capture")
    return c["capture_url"] if c else None


def firm_cite(slug, name=None):
    """The firm's own listing for this row: the live CMS listing if live, else the latest archive capture."""
    if live(slug, name):
        return LISTING
    return cap(slug)


def post(key):
    """(capture_url, title, date) of one press-archive post, by post slug (prefix 'vc:' for project-a.vc)."""
    p = POSTS[key]
    return p["capture_url"], p["title"], p["date"]


def posts_for(slug):
    return {k: v for k, v in POSTS.items() if slug in v.get("companies", [])}


def hq(slug, name=None):
    """(country, city, citation) from the firm's own HQ field: the live CMS first, then the archive."""
    r = live(slug, name)
    if r and r.get("hq_country_site"):
        return CC.get(r["hq_country_site"]), CITY_FIX.get(r.get("hq_city_site"), r.get("hq_city_site")), LISTING
    for val, c in fields(slug, "cf_location") + fields(slug, "page_location"):
        first = re.split(r"\s*/\s*|\s+Founders?:|\s+Management", val)[0]
        m = re.match(r"(.+?)\s*\((.+?)\)", first) or re.match(r"(.+?),\s*(.+)", first)
        if m and CC.get(m.group(2).strip()):
            city = m.group(1).strip()
            return CC[m.group(2).strip()], CITY_FIX.get(city, city), c
    return None, None, None


def items(slug):
    g = SURF.get(slug) or {}
    for svc, v in (g.get("surfaces") or {}).items():
        for i in v.get("items") or []:
            yield svc, i


def gn(slug, suffix):
    """Publisher URL of the surfaces item whose Google News id ends with `suffix`
    (or whose url contains it)."""
    for svc, i in items(slug):
        gid = i.get("gid") or ""
        if (gid and gid.endswith(suffix)) or (i.get("url") and suffix in i["url"]):
            if i.get("url"):
                return i["url"]
            if gid in DEC:
                return DEC[gid]
            url = _gsmod().decode(gid)
            if isinstance(url, dict):
                url = url.get("url")
            if url and url.startswith("http") and "news.google.com" not in url:
                DEC[gid] = url
                _DEC.write_text(json.dumps(DEC, indent=1))
                return url
            raise RuntimeError(f"decode failed for {slug} {suffix}: {url}")
    raise KeyError(f"no surfaces item {suffix} on {slug}")


def surfaces_lines(slug, finding, firm_line=None):
    """The absence test's surface lines, one per surface the layer ran, in the
    recorded form '<surface>: <what was searched> -> <what it showed>'."""
    g = SURF.get(slug) or {}
    out = [firm_line or ("firm: project-a.vc CMS (2026-09-30), the archived 2012-2024 project-a.com listings and "
                         "company pages, and the firm's press archive 2012-2019 and blog 2019-2025 for the name -> "
                         + finding)]
    for svc in ("googlenews", "googlenews_firm", "techcrunch", "crunchbase_news", "googlenews_local"):
        v = (g.get("surfaces") or {}).get(svc)
        if not v:
            continue
        if v.get("status") != "ok":
            raise RuntimeError(f"{slug}: surface {svc} not ok ({v.get('status')}); re-run surfaces before a no")
        n = v.get("n", len(v.get("items") or []))
        named = sum(1 for i in v.get("items") or [] if i.get("names"))
        out.append(f"{svc}: {v.get('query') or g.get('query_name')} -> {n} results, {named} naming the company; {finding}")
    return out


def verdict(slug, v, basis, ec="site_listing", conf="high", cite=None, exclusion=None):
    d = {"slug": slug, "verdict": v, "who": WHO, "evidence_class": ec, "basis": basis, "confidence": conf}
    if cite:
        d["citation"] = cite
    if exclusion:
        d["exclusion"] = exclusion
    return d


def cls(slug, *, status=None, rng=None, usd=None, val_src=None, val_cite=None, asof=None,
        val_conf=None, stage=None, stage_src=None, stage_cite=None, stage_conf=None,
        entry_date=None, grad=None, grad_src=None, grad_cite=None, grad_conf=None,
        grad_asof=None, surfaces=None, country=None, country_src="web_verified",
        country_cite=None, city=None, city_src="web_verified", focus=None,
        focus_src="model", flags=(), clear=(), note=None, rounds=None, extra=None):
    r = {"slug": slug, "who": WHO}
    if status is not None:
        r["status"] = status
    if rng is not None:
        r["valuation_range"] = rng
        if rng != "undetermined":
            r["valuation_usd"] = usd
        if val_conf:
            r["valuation_confidence"] = val_conf
    if usd is not None:
        r.update({"valuation_usd": usd, "valuation_source": val_src, "valuation_range_source": val_src})
        if asof:
            r["valuation_asof"] = asof
        if val_cite:
            r["valuation_citation"] = val_cite
    if stage is not None:
        r["entry_stage"] = stage
        if stage != "undetermined":
            r["entry_stage_source"] = stage_src
            if stage_conf:
                r["entry_stage_confidence"] = stage_conf
            if stage_cite:
                r["entry_stage_citation"] = stage_cite
    if entry_date is not None:
        r["entry_date"] = str(entry_date)
    if grad is not None:
        r["seed_to_a_graduation"] = grad
        if grad_src:
            r["graduation_source"] = grad_src
        if grad_cite:
            r["graduation_citation"] = grad_cite
        if grad_conf:
            r["graduation_confidence"] = grad_conf
        if grad_asof:
            r["graduation_asof"] = grad_asof
        if surfaces:
            r["graduation_surfaces"] = list(surfaces)
    if country is not None:
        r["hq_country"] = country
        r["hq_country_source"] = country_src
        if country_cite:
            r["hq_country_citation"] = country_cite
    if city is not None:
        r["hq_city"] = city
        r["hq_city_source"] = city_src
    if focus is not None:
        r["focus"] = focus
        r["focus_source"] = focus_src
    if flags:
        r["flags"] = sorted(set(flags))
    if clear:
        r["clear_flags"] = sorted(set(clear))
    if note:
        r["note"] = note
    if rounds is not None:
        r["funding_rounds"] = rounds
    if extra:
        r.update(extra)
    return r


def rnd(date, round_, amount_usd=None, lead=None, firm_in_round=None, source=None, source_type="press"):
    return {"date": date, "round": round_, "amount_usd": amount_usd, "lead": lead,
            "firm_in_round": firm_in_round, "source": source, "source_type": source_type}


def write(name, lines, record=True):
    Q.mkdir(parents=True, exist_ok=True)
    p = Q / f"{name}.out.jsonl"
    p.write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in lines) + "\n")
    print(f"wrote {p.name}: {len(lines)} lines ({sum(1 for x in lines if 'verdict' in x)} verdicts)")
    if record:
        r = subprocess.run(["python3", "scripts/run.py", "record", "--investor", "project-a-ventures", str(p)],
                           cwd=ROOT, capture_output=True, text=True)
        print(r.stdout[-6000:], r.stderr[-3000:])


# ---- research-agent results (scratch/research-g*.json, every URL re-loaded by the agent)
import glob as _glob

RS = {}
for _f in sorted(_glob.glob(str(H / "research-g[0-9].json"))):
    try:
        RS.update(json.load(open(_f)))
    except ValueError:
        pass


def rrounds(slug):
    return [rnd(r.get("date"), r.get("round"), r.get("amount_usd"), r.get("lead"), r.get("firm_in_round"),
                r.get("source") if str(r.get("source") or "").startswith("http") else None, r.get("source_type") or "press")
            for r in RS[slug].get("rounds") or []]


def ec(slug):
    return RS[slug]["entry"]["citation"]


def sc(slug):
    return RS[slug]["status_citation"]


def gc(slug):
    return RS[slug]["graduation"]["citation"]
