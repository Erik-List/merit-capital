"""Helpers for the EQT Ventures grind (PRO-163), adapted from the Balderton run (PRO-106): build .out.jsonl lines under the
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

WHO = "agent-judge-pro163"
ROOT = Path(__file__).resolve().parents[5]
Q = ROOT / "data" / "collection" / "investors" / "eqt-ventures" / "scratch" / "queue"
SITE = "https://eqtgroup.com/about/current-portfolio"


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
        r = subprocess.run(["python3", "scripts/run.py", "record", "--investor", "eqt-ventures",
                            str(p)], cwd=ROOT, capture_output=True, text=True)
        print(r.stdout[-4000:], r.stderr[-2000:])


# ---- citations read from disk, never typed (the Balderton lesson: 19 typed
# citations were wrong). Each helper refuses an ambiguous or missing match.
_INV = ROOT / "data" / "collection" / "investors" / "eqt-ventures"
_STORIES = [r["url"] for r in json.loads((_INV / "sources/site/stories.json").read_text())["rows"]]
_ARTS = json.loads((_INV / "sources/site/articles-2017-2020.json").read_text())["rows"]
_SITE = {r["site_id"]: r["url"] for r in json.loads((_INV / "sources/site/companies-eqtgroup.json").read_text())["rows"]}
_WIKI = json.loads((_INV / "sources/web/wikipedia-insource.json").read_text())


def S(sub):
    """The firm's stories post whose URL contains `sub` (exactly one)."""
    m = [u for u in _STORIES if sub in u]
    if len(m) != 1:
        raise SystemExit(f"S({sub!r}) matched {len(m)}: {m[:3]}")
    return m[0]


def A(sub):
    """The Common Crawl capture URL of the 2017-2020 article whose slug contains `sub`."""
    m = [r["capture_url"] for r in _ARTS if sub in r["slug"]]
    if len(m) != 1:
        raise SystemExit(f"A({sub!r}) matched {len(m)}")
    return m[0]


_BASE_SITE = {r["slug"]: r.get("site_url") for r in json.loads((_INV / "companies/base.json").read_text())}


def SITE(slug):
    """The company's eqtgroup.com portfolio page (the firm's Key Facts), by base slug."""
    u = _BASE_SITE.get(slug) or _SITE.get(slug)
    if not u or "eqtgroup.com" not in u:
        raise SystemExit(f"SITE({slug!r}): no eqtgroup.com page on the row")
    return u


def W(title):
    """A Wikipedia article URL, from a title that exists on disk (insource sweep or fetched raw)."""
    arts = _WIKI.get("articles") or _WIKI.get("rows") or []
    for a in arts:
        t = a.get("title") or a.get("article")
        if t == title and a.get("url"):
            return a["url"]
    raw = ROOT / "data" / "filings" / "eqt-ventures" / "wikipedia" / (title.replace(" ", "_") + ".txt")
    if raw.exists() and raw.stat().st_size > 3000 and not raw.read_text()[:20].startswith("#REDIRECT"):
        return "https://en.wikipedia.org/wiki/" + title.replace(" ", "_")
    raise SystemExit(f"W({title!r}) not on disk")


_PACK = json.loads((Path(__file__).with_name("evidence-pack.json")).read_text())


def ARC(slug):
    """The first Common Crawl capture of the firm's own eqtventures.com page for the row (Geography, dates)."""
    u = ((_PACK.get(slug) or {}).get("archive") or {}).get("first_capture")
    if not u:
        raise SystemExit(f"ARC({slug!r}): no archive capture")
    return u
