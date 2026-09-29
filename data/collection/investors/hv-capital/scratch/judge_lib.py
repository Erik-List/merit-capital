"""Helpers for the HV Capital grind (PRO-104), adapted from Balderton's (PRO-106):
build .out.jsonl lines under the current record contract (COLLECTION.md s6/s8).

A member needs TWO lines: the verdict line and a classification line (record
routes a line by the presence of `verdict`; a single line carrying both drops
every classification key). `cls()` emits only the keys it is given.

Citations are copied from tool results or files on disk, never typed: `gn(slug,
suffix)` resolves a Google News item the surfaces layer found (by the tail of its
id, as the pack prints it) to the publisher's own URL, cached in gn-decode.json.
"""
from __future__ import annotations

import csv
import importlib.util
import json
import re
import subprocess
from pathlib import Path

WHO = "agent-judge-pro104"
H = Path(__file__).resolve().parent
INV = H.parent
ROOT = INV.parents[3]
Q = H / "queue"
EXPORT = "https://www.hvcapital.com/api/portfolio-csv?lang=en"
ASOF = "2026-09-29"

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


SURF = json.loads((H / "graduation-surfaces.json").read_text()) if (H / "graduation-surfaces.json").exists() else {}
EV = json.loads((H / "archive-evidence.json").read_text())


def _k(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


LIVE = {_k(r["Name"]): r for r in csv.DictReader(open(INV / "sources/site/portfolio-2026.csv", encoding="utf-8-sig"))}
CC = {"Germany": "DE", "United Kingdom": "GB", "United States of America": "US", "USA": "US", "Netherlands": "NL",
      "France": "FR", "Switzerland": "CH", "Spain": "ES", "Austria": "AT", "Denmark": "DK", "Singapore": "SG",
      "Philippines": "PH", "Canada": "CA", "Finland": "FI", "Croatia": "HR", "Italy": "IT", "Sweden": "SE",
      "UK": "GB", "England": "GB", "Russia": "RU", "India": "IN", "Brazil": "BR", "Israel": "IL", "Poland": "PL",
      "Belgium": "BE", "Portugal": "PT", "Ireland": "IE", "Estonia": "EE", "Czech Republic": "CZ", "Norway": "NO",
      "Luxembourg": "LU", "Mexico": "MX", "Argentina": "AR", "Chile": "CL", "Colombia": "CO", "Turkey": "TR",
      "United Arab Emirates": "AE", "Indonesia": "ID", "Malaysia": "MY", "Vietnam": "VN", "Thailand": "TH"}
CITY_FIX = {"München": "Munich", "Köln": "Cologne", "København": "Copenhagen", "Muenchen": "Munich",
            "Wien": "Vienna", "Zürich": "Zurich", "Bayern": None, "SanFrancisco": "San Francisco",
            "ChicagoHeights": "Chicago Heights"}

_DEC = H / "gn-decode.json"
DEC = json.loads(_DEC.read_text()) if _DEC.exists() else {}


def live(slug, name=None):
    return LIVE.get(_k(slug)) or LIVE.get(_k(name))


def ev(slug):
    return EV.get(slug) or {}


def hq(slug, name=None):
    """(country, city, citation) from the firm's own HQ field: the live export
    first, then the archived Storyblok lists (their capture as citation)."""
    r = live(slug, name)
    if r and r["HQ"]:
        parts = [p.strip() for p in r["HQ"].split(",")]
        return CC.get(parts[-1]), CITY_FIX.get(parts[0], parts[0]), EXPORT
    e = ev(slug)
    for h in e.get("hq") or []:
        parts = [p.strip() for p in h.replace("/", ",").split(",") if p.strip()]
        if parts and CC.get(parts[-1]):
            cap = next((u for y, u in sorted(e.get("captures", {}).items(), reverse=True) if "hvcapital" in u), None)
            city = CITY_FIX.get(parts[0], parts[0]) if len(parts) > 1 else None
            return CC.get(parts[-1]), city, cap
    return None, None, None


def firm_cite(slug, name=None):
    """The firm's own listing for this row: the export if live, else the latest archived list capture."""
    if live(slug, name):
        return EXPORT
    e = ev(slug)
    caps = e.get("captures") or {}
    return caps[max(caps)] if caps else None


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
    out = [firm_line or ("firm: hvcapital.com export (2026-09-29), the archived 2015-2025 lists and the firm's "
                         "news feed for the name -> " + finding)]
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


def verdict(slug, v, basis, ec="site_listing", conf="high", cite=None):
    d = {"slug": slug, "verdict": v, "who": WHO, "evidence_class": ec, "basis": basis, "confidence": conf}
    if cite:
        d["citation"] = cite
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
        r = subprocess.run(["python3", "scripts/run.py", "record", "--investor", "hv-capital", str(p)],
                           cwd=ROOT, capture_output=True, text=True)
        print(r.stdout[-6000:], r.stderr[-3000:])
