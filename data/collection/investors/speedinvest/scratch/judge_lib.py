"""Helpers for the Speedinvest grind (PRO-84), adapted from Project A's (PRO-102):
build .out.jsonl lines under the current record contract (COLLECTION.md s6/s8).

A member needs TWO lines: the verdict line and a classification line (record
routes a line by the presence of `verdict`; a single line carrying both drops
every classification key). `cls()` emits only the keys it is given.

Citations are copied from files on disk or tool results, never typed: the firm's
live per-company page (the row's site_url), an archive capture (`cap`), a
firm post (`post`), a register page, or a Google News item the surfaces layer
found (`gn`).
"""
from __future__ import annotations

import glob as _glob
import importlib.util
import json
import re
import subprocess
from pathlib import Path

WHO = "agent-judge-pro84"
H = Path(__file__).resolve().parent
INV = H.parent
ROOT = INV.parents[3]
Q = H / "queue"
LISTING = "https://www.speedinvest.com/portfolio"
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


def _k(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def slugify(s):
    import html as _h
    s = _h.unescape(s or "").lower().replace("&", " and ")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


SURF = _load(H / "graduation-surfaces.json", {})
EV = _load(INV / "sources/wayback/archive-evidence.json", {"companies": {}})["companies"]
POSTS = _load(INV / "sources/site/press-archive.json", {"posts": {}})["posts"]
BASE = {r["slug"]: r for r in _load(INV / "companies/base.json", [])}
_DEC = H / "gn-decode.json"
DEC = _load(_DEC, {})
REG = _load(INV / "sources/registers/status-at-de.json", {})

LIVE, BOARD = {}, {}
for _r in _load(INV / "sources/site/companies-2026.json", {"rows": []})["rows"]:
    LIVE[_k(_r["name"])] = _r
    LIVE.setdefault(_k(_r.get("cms_slug")), _r)
for _r in _load(INV / "sources/site/jobboard-companies.json", {"rows": []})["rows"]:
    BOARD[_k(_r["name"])] = _r
    BOARD.setdefault(_k(_r.get("board_name")), _r)

CC = {"Germany": "DE", "United Kingdom": "GB", "United States of America": "US", "France": "FR", "Austria": "AT",
      "Spain": "ES", "Netherlands": "NL", "Switzerland": "CH", "United Arab Emirates": "AE", "Finland": "FI",
      "Kenya": "KE", "Hungary": "HU", "Bulgaria": "BG", "Estonia": "EE", "Denmark": "DK", "Pakistan": "PK",
      "Saudi Arabia": "SA", "Ireland": "IE", "Italy": "IT", "Turkey": "TR", "Brazil": "BR", "Norway": "NO",
      "Croatia": "HR", "Angola": "AO", "Mexico": "MX", "Slovenia": "SI", "Greece": "GR", "Ivory Coast": "CI",
      "Egypt": "EG", "Belgium": "BE", "Nigeria": "NG", "Canada": "CA", "India": "IN", "Ghana": "GH",
      "Poland": "PL", "Sweden": "SE", "South Africa": "ZA", "Ukraine": "UA", "Bangladesh": "BD"}


def row(slug):
    return BASE.get(slug) or {}


def live(slug, name=None):
    name = name or row(slug).get("name")
    return LIVE.get(_k(slug)) or LIVE.get(_k(name))


def board(slug, name=None):
    name = name or row(slug).get("name")
    return BOARD.get(_k(slug)) or BOARD.get(_k(name))


def ev(slug, name=None):
    name = name or row(slug).get("name")
    return EV.get(slug) or EV.get(slugify(name)) or {}


def cap(slug, last=True):
    e = ev(slug)
    c = e.get("last_capture" if last else "first_capture")
    return c["capture_url"] if c else None


def firm_cite(slug, name=None):
    """The firm's own listing for this row: its live per-company page, else the latest archive capture."""
    lv = live(slug, name)
    if lv:
        return lv["url"]
    return cap(slug) or row(slug).get("wayback_first_link") or None


def post(key):
    p = POSTS[key]
    return p["capture_url"], p["title"], p["date"]


def posts_for(slug):
    return {k: v for k, v in POSTS.items() if slug in v.get("companies", [])}


def items(slug):
    g = SURF.get(slug) or {}
    for svc, v in (g.get("surfaces") or {}).items():
        for i in v.get("items") or []:
            yield svc, i


def gn(slug, suffix):
    """Publisher URL of the surfaces item whose Google News id ends with `suffix` (or whose url contains it)."""
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
    """The absence test's surface lines, one per surface the layer ran:
    '<surface>: <what was searched> -> <what it showed>'."""
    g = SURF.get(slug) or {}
    out = [firm_line or ("firm: speedinvest.com portfolio (live 2026-09-30, archived 2017-2025 listings and company "
                         "pages) and the firm's posts 2012-2026 for the name -> " + finding)]
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
        r = subprocess.run(["python3", "scripts/run.py", "record", "--investor", "speedinvest", str(p)],
                           cwd=ROOT, capture_output=True, text=True)
        print(r.stdout[-8000:], r.stderr[-3000:])


# ---- research-agent results (scratch/research/<group>.json, every URL re-loaded by the agent)
RS = {}
for _f in sorted(_glob.glob(str(H / "research" / "*.json"))):
    try:
        RS.update(json.load(open(_f)))
    except ValueError:
        pass
