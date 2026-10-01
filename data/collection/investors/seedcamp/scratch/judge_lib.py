"""Helpers for the Seedcamp grind (PRO-83), adapted from the Balderton run (PRO-106): build .out.jsonl lines under the
current record contract (COLLECTION.md §6/§8, run.py validate_record).

A member needs TWO lines: the verdict line and a classification line (record
routes a line by the presence of `verdict`; a single line carrying both drops
every classification key). `cls()` emits only the keys it is given, so a line
never clobbers a filing-grade fact it was not asked about.
"""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

WHO = "agent-judge-pro83"
ROOT = Path(__file__).resolve().parents[5]
Q = ROOT / "data" / "collection" / "investors" / "seedcamp" / "scratch" / "queue"
SITE = "https://seedcamp.com/our-companies/"


def verdict(slug, v, basis, ec="site_listing", conf="high", cite=None):
    d = {"slug": slug, "verdict": v, "who": WHO, "evidence_class": ec, "basis": basis,
         "confidence": conf}
    if cite:
        d["citation"] = cite
    return d


def cls(slug, *, status=None, rng=None, usd=None, val_src=None, val_cite=None, asof=None,
        val_conf=None, stage=None, stage_src=None, stage_cite=None, stage_conf=None,
        entry_date=None, grad=None, grad_src=None, grad_cite=None, grad_conf=None,
        grad_asof=None, surfaces=None, country=None, country_src="model_knowledge",
        country_cite=None, city=None, city_src="model_knowledge", focus=None,
        focus_src="model", flags=(), clear=(), note=None, rounds=None, extra=None):
    """One classification line with only the keys given."""
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
        r.update({"valuation_usd": usd, "valuation_source": val_src,
                  "valuation_range_source": val_src})
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
    if focus is not None or "focus" in (extra or {}):
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


def rnd(date, round_, amount_usd=None, lead=None, firm_in_round=None, source=None,
        source_type="press"):
    """One funding_rounds entry in the §6 form."""
    return {"date": date, "round": round_, "amount_usd": amount_usd, "lead": lead,
            "firm_in_round": firm_in_round, "source": source, "source_type": source_type}


def write(name, lines, record=True):
    """Write scratch/queue/<name>.out.jsonl and record it; print record's whole output."""
    Q.mkdir(parents=True, exist_ok=True)
    p = Q / f"{name}.out.jsonl"
    p.write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in lines) + "\n")
    print(f"wrote {p.name}: {len(lines)} lines "
          f"({sum(1 for x in lines if 'verdict' in x)} verdicts)")
    if record:
        r = subprocess.run(["python3", "scripts/run.py", "record", "--investor", "seedcamp",
                            str(p)], cwd=ROOT, capture_output=True, text=True)
        print(r.stdout[-4000:], r.stderr[-2000:])


# ---- Seedcamp-specific helpers (decisions.md D3): the programme's standard deal
# is Pre-Seed / program_terms, cited to the terms document of its era
TERMS = {
    "2007-2009": "https://index.commoncrawl.org/CC-MAIN-2008-2009-index?url=http%3A%2F%2Fwww.seedcamp.com%2Fpages%2Fabout_faqs&output=json",
    "2010-2014": "https://index.commoncrawl.org/CC-MAIN-2012-index?url=http%3A%2F%2Fwww.seedcamp.com%2Ffaq&output=json",
    "2014-2017": "https://seedcamp.com/views/your-first-round-fund/",
    "2017-2020": "https://index.commoncrawl.org/CC-MAIN-2017-51-index?url=http%3A%2F%2Fseedcamp.com%2Ffaq%2Fhow-much-does-seedcamp-typically-invest%2F&output=json",
}
TERMS_WORDS = {
    "2007-2009": "EUR 50K per team for a minority stake (Fund I)",
    "2010-2014": "EUR 50K for 8-10% (Fund II)",
    "2014-2017": "EUR 75K for 7% (Seedcamp III)",
    "2017-2020": "GBP 100K for 7.5% as the lead first cheque (Seedcamp IV)",
}


def era(date: str) -> str:
    d = str(date)
    if d < "2010":
        return "2007-2009"
    if d < "2014-09":
        return "2010-2014"
    if d < "2017-11":
        return "2014-2017"
    return "2017-2020"


def prog(entry_date, cohort=None):
    """kwargs for cls(): a programme entry on its era's standard terms."""
    e = era(entry_date)
    return {"stage": "Pre-Seed", "stage_src": "program_terms", "stage_cite": TERMS[e],
            "stage_conf": "high", "entry_date": str(entry_date),
            "_prog_note": f"programme entry on the standard terms of its era ({TERMS_WORDS[e]})"
                          + (f"; cohort: {cohort}" if cohort else "")}


def c(slug, *, prog_at=None, cohort=None, note=None, **kw):
    """cls() with an optional programme stage folded in and its note joined."""
    if prog_at:
        p = prog(prog_at, cohort)
        pn = p.pop("_prog_note")
        for k, v in p.items():
            kw.setdefault(k, v)
        note = f"{note}; {pn}" if note else pn
    return cls(slug, note=note, **kw)


def loc(country, city=None, cite=None):
    """kwargs for cls(): country and city, cited to the firm's post where it states them."""
    k = {"country": country, "country_src": "web_verified" if cite else "model_knowledge"}
    if cite:
        k["country_cite"] = cite
    if city:
        k["city"] = city
        k["city_src"] = "web_verified" if cite else "model_knowledge"
    return k


def cu(**kw):
    """merge kwargs dicts (loc() + others) for c()."""
    return kw


import re as _re
V = "https://seedcamp.com/views/"
_COH = {}
for _r in json.loads((Path(__file__).resolve().parent.parent / "sources/site/views-cohorts.json").read_text())["rows"]:
    _COH[_re.sub(r"[^a-z0-9]", "", _r["name"].lower())] = _r


def coh(name):
    return _COH[_re.sub(r"[^a-z0-9]", "", name.lower())]


def pc(slug, name, country, city, **kw):
    """A programme-cohort row: Pre-Seed on its era's terms, location cited to the cohort post."""
    r = coh(name)
    return c(slug, prog_at=r["post_date"][:7], cohort=r["url"], **loc(country, city, r["url"]), **kw)


def sc(slug, name, country, city, **kw):
    """A seed-cohort row (the firm names it a seed-fund investment): Seed, first_party, the post cited."""
    r = coh(name)
    kw.setdefault("stage", "Seed"); kw.setdefault("stage_src", "first_party")
    kw.setdefault("stage_cite", r["url"]); kw.setdefault("stage_conf", "high")
    kw.setdefault("entry_date", r["post_date"][:7])
    return c(slug, **loc(country, city, r["url"]), **kw)
