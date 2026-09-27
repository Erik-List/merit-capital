"""Helpers for the Headline grind (PRO-164), adapted from the Atomico run (PRO-79): build .out.jsonl lines under the
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

WHO = "agent-judge-pro164"
ROOT = Path(__file__).resolve().parents[5]
Q = ROOT / "data" / "collection" / "investors" / "headline" / "scratch" / "queue"
SITE = "https://headline.com/portfolio/"


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
        r = subprocess.run(["python3", "scripts/run.py", "record", "--investor", "headline",
                            str(p)], cwd=ROOT, capture_output=True, text=True)
        print(r.stdout[-4000:], r.stderr[-2000:])


_PACK = None


def post_url(slug, title_sub):
    """The citation URL of the firm's own post (evidence pack) whose title contains title_sub."""
    global _PACK
    if _PACK is None:
        _PACK = json.loads((Path(__file__).resolve().parent / "evidence-pack.json").read_text())
    for p in _PACK.get(slug, {}).get("posts", []):
        if title_sub.lower() in p["title"].lower():
            return p["url"]
    raise KeyError(f"{slug}: no post titled like {title_sub!r}")


def cc_cite(path_sub, domain="bvcapital.com"):
    """The index.commoncrawl.org citation of a fetched capture whose URL contains path_sub."""
    man = json.loads((Path(__file__).resolve().parents[1] / "sources" / "wayback" / f"cc-manifest-{domain}.json").read_text())
    for k, m in sorted(man.items()):
        if m.get("status") == "ok" and path_sub in m["url"]:
            return m["capture_url"]
    raise KeyError(path_sub)


_SC = None


def cms_cite(slug):
    """The firm's own CMS doc for this company (a Sanity query URL by _id)."""
    global _SC
    import re
    if _SC is None:
        rows = json.loads((Path(__file__).resolve().parents[1] / "sources" / "site" / "sanity-companies.json").read_text())["rows"]
        _SC = {re.sub(r"[^a-z0-9]+", "-", r["name"].lower()).strip("-"): r for r in rows}
    return _SC[slug]["url"]


def cms_stages(slug):
    cms_cite(slug)
    import re
    return (_SC[slug].get("stages") or "")


def note_plus(slug, text):
    """What to put on a line so the stored note ends up as <note> | <text>. `record`
    joins a new note onto the stored one with " | " unless the new note is already
    inside it, in which case it REPLACES the stored note with the new one; so pass
    the addition only, and pass the full stored note when the text is already there
    (a no-op). Returning cur + text duplicated every earlier note (found 2026-09-27)."""
    cur = json.loads((Path(__file__).resolve().parents[1] / "companies" / "classification.json").read_text()).get(slug, {}).get("note") or ""
    return cur if (cur and text in cur) else text
