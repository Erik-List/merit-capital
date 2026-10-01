"""Helpers for the Index Ventures grind (PRO-82), adapted from the Northzone run (PRO-105): build .out.jsonl lines under the
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

WHO = "agent-judge-pro82"
ROOT = Path(__file__).resolve().parents[5]
Q = ROOT / "data" / "collection" / "investors" / "index-ventures" / "scratch" / "queue"
SITE = "https://www.indexventures.com/companies"


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
        r = subprocess.run(["python3", "scripts/run.py", "record", "--investor", "index-ventures",
                            str(p)], cwd=ROOT, capture_output=True, text=True)
        print(r.stdout[-4000:], r.stderr[-2000:])


# ---- Index lookups: citations come from files on disk, never typed (Balderton's lesson)
_H = Path(__file__).resolve().parent
_POSTS = None
_SIB = None
_EV = None
_NA = None
_GS = None


def post(sub: str, sub2: str = "") -> str:
    """URL of the one Perspectives post whose slug or title contains the substrings."""
    global _POSTS
    if _POSTS is None:
        _POSTS = [r for r in json.load(open(_H.parent / "sources" / "site" / "perspectives.json"))["rows"] if not r.get("missing")]
    exact = [r for r in _POSTS if r["slug"] == sub and not sub2]
    if exact:
        return exact[0]["url"]
    hits = [r for r in _POSTS if sub.lower() in (r["slug"] + " " + (r.get("title") or "")).lower()
            and sub2.lower() in (r["slug"] + " " + (r.get("title") or "")).lower()]
    if len(hits) != 1:
        raise KeyError(f"post({sub!r}, {sub2!r}): {len(hits)} hits {[h['slug'] for h in hits][:6]}")
    return hits[0]["url"]


def postdate(sub: str, sub2: str = "") -> str:
    u = post(sub, sub2)
    return next(r["date"] for r in _POSTS if r["url"] == u)


def ev(slug: str) -> dict:
    global _EV
    if _EV is None:
        _EV = json.load(open(_H / "evidence-pack.json"))
    return _EV[slug]


def page(slug: str) -> str:
    """The firm's own live company page for the row."""
    u = (ev(slug).get("site") or {}).get("url")
    if not u:
        raise KeyError(f"page({slug}): not on the live site")
    return u


def arch(slug: str, field: str, value=None) -> str:
    """Capture URL of the archived claim `field` for the row (earliest capture; `value` picks one claim)."""
    a = (ev(slug).get("archive") or {}).get(field) or []
    if value is not None:
        a = [x for x in a if x["value"] == value or (isinstance(x["value"], list) and value in x["value"])]
    if not a:
        raise KeyError(f"arch({slug}, {field}, {value}): no such archived claim")
    return sorted(a, key=lambda x: x["ts"])[0]["capture_url"]


def narch(sub: str, sub2: str = "") -> str:
    """Capture URL of the one archived news item (2002-2019 site) whose title contains the substrings."""
    global _NA
    if _NA is None:
        _NA = json.load(open(_H.parent / "sources" / "wayback" / "news-archive.json"))["rows"]
    hits = [r for r in _NA if sub.lower() in (r.get("title") or "").lower() and sub2.lower() in (r.get("title") or "").lower()]
    if len(hits) != 1:
        raise KeyError(f"narch({sub!r}, {sub2!r}): {len(hits)} hits {[h['title'][:60] for h in hits][:6]}")
    return hits[0]["capture_url"]


def sib(slug: str, investor: str, key: str):
    """A sibling book's published value for the same company (siblings.json)."""
    global _SIB
    if _SIB is None:
        _SIB = json.load(open(_H / "siblings.json"))
    for x in _SIB.get(slug, []):
        if x["investor"] == investor:
            return x[key]
    raise KeyError(f"sib({slug}, {investor}, {key})")


def _gs():
    global _GS
    if _GS is None:
        import importlib.util as iu, sys as _s
        spec = iu.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
        _GS = iu.module_from_spec(spec); a = _s.argv; _s.argv = a[:1]; spec.loader.exec_module(_GS); _s.argv = a
    return _GS


def news(name: str, sub: str) -> str:
    """Publisher URL of the one headline in scratch/news-bulk.json for `name` containing `sub`
    (decoded from Google News on demand, cached back into the file)."""
    p = _H / "news-bulk.json"
    db = json.load(open(p))
    hits = [i for i in db[name]["items"] if sub.lower() in i["title"].lower()]
    if len(hits) != 1:
        raise KeyError(f"news({name!r}, {sub!r}): {len(hits)} hits {[h['title'][:60] for h in hits][:5]}")
    it = hits[0]
    if not it.get("url"):
        it["url"] = _gs().decode(it["gid"]) or ""
        db2 = json.load(open(p))
        for i in db2[name]["items"]:
            if i["gid"] == it["gid"]:
                i["url"] = it["url"]
        p.write_text(json.dumps(db2, indent=1, ensure_ascii=False))
    if not it["url"]:
        raise KeyError(f"news({name!r}, {sub!r}): decode failed")
    return it["url"]


def gsurl(slug: str, sub: str) -> str:
    """Publisher URL of the one headline in scratch/graduation-surfaces.json for `slug` containing `sub`."""
    g = json.load(open(_H / "graduation-surfaces.json"))
    hits = []
    for name, sf in g[slug]["surfaces"].items():
        for i in sf.get("items", []):
            if sub.lower() in i.get("title", "").lower() and all(i.get("title") != h.get("title") for h in hits):
                hits.append(i)
    if len(hits) != 1:
        raise KeyError(f"gsurl({slug!r}, {sub!r}): {len(hits)} hits {[h['title'][:60] for h in hits][:4]}")
    it = hits[0]
    if it.get("link"):
        return it["link"]
    u = _gs().decode(it["gid"]) or ""
    if not u:
        raise KeyError(f"gsurl({slug!r}, {sub!r}): decode failed")
    return u
