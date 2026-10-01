"""Helpers for the Lakestar grind (PRO-108), adapted from Project A's (PRO-102):
build .out.jsonl lines under the current record contract (COLLECTION.md s6/s8).

A member needs TWO lines: the verdict line and a classification line (record
routes a line by the presence of `verdict`; a single line carrying both drops
every classification key). `cls()` emits only the keys it is given.

Citations are copied from files on disk or tool results, never typed from
memory: an archive capture (`cap`), a press-archive post (`post`), a research
file entry the agent re-loaded (`RS`), or a sibling book's cited value.
"""
from __future__ import annotations

import glob as _glob
import json
import re
import subprocess
from pathlib import Path

WHO = "agent-judge-pro108"
H = Path(__file__).resolve().parent
INV = H.parent
ROOT = INV.parents[3]
Q = H / "queue"
ASOF = "2026-10-01"


def _load(p, default):
    p = Path(p)
    return json.loads(p.read_text()) if p.exists() else default


SURF = _load(H / "graduation-surfaces.json", {})
EV = _load(INV / "sources/wayback/archive-evidence.json", {"companies": {}})["companies"]
PRESS = _load(INV / "sources/site/press-archive.json", {"posts": {}, "by_company": {}})
POSTS = PRESS["posts"]
SIB = _load(H / "siblings.json", {})
BASE = {r["slug"]: r for r in _load(INV / "companies/base.json", [])}


def ev(slug):
    return EV.get(slug) or {}


def cap(slug, last=False):
    """The row's first archived listing capture (URL); the base row's own link otherwise."""
    e = ev(slug)
    if e.get("first_capture_url"):
        return e["first_capture_url"]
    return (BASE.get(slug) or {}).get("wayback_first_link") or (BASE.get(slug) or {}).get("site_url")


def post(key):
    """(capture_url, title, date) of one press-archive post, by post slug."""
    p = POSTS[key]
    return p["capture_url"], p["title"], p["date"]


def surfaces_lines(slug, finding, firm_line=None):
    """The absence test's surface lines, one per surface the layer ran, in the
    recorded form '<surface>: <what was searched> -> <what it showed>'."""
    g = SURF.get(slug) or {}
    out = [firm_line or ("firm: lakestar.com archived portfolio and company pages 2018-2026, the firm's 105 archived "
                         "posts 2018-2026 and the live site (2026-10-01) for the name -> " + finding)]
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
        r = subprocess.run(["python3", "scripts/run.py", "record", "--investor", "lakestar", str(p)],
                           cwd=ROOT, capture_output=True, text=True)
        print(r.stdout[-6000:], r.stderr[-3000:])


# ---- research-agent results (scratch/research-g*.json, every URL re-loaded by the agent)
RS = {}
for _f in sorted(_glob.glob(str(H / "research-*.json"))):
    if _f.endswith("research-groups.json"):
        continue
    try:
        _d = json.load(open(_f))
    except ValueError:
        continue
    for _k, _v in _d.items():
        if not _k.startswith("_") and isinstance(_v, dict):
            RS.setdefault(_k, {}).update(_v)


def rrounds(slug):
    return [rnd(r.get("date"), r.get("round"), r.get("amount_usd"), r.get("lead"), r.get("firm_in_round"),
                r.get("source") if str(r.get("source") or "").startswith("http") else None, r.get("source_type") or "press")
            for r in (RS.get(slug) or {}).get("rounds") or []]
