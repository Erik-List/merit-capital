"""Helpers for the Northzone grind (PRO-105), copied from the Balderton run (PRO-106): build .out.jsonl lines under the
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

WHO = "agent-judge-pro105"
ROOT = Path(__file__).resolve().parents[5]
Q = ROOT / "data" / "collection" / "investors" / "northzone" / "scratch" / "queue"
SITE = "https://northzone.com/portfolio"


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
        r = subprocess.run(["python3", "scripts/run.py", "record", "--investor", "northzone",
                            str(p)], cwd=ROOT, capture_output=True, text=True)
        print(r.stdout[-4000:], r.stderr[-2000:])


# ---- Northzone lookups: citations come from files on disk, never typed (Balderton's lesson)
_H = Path(__file__).resolve().parent
_INS = None
_SIB = None


def post(slug_or_title: str, sub: str = "", kind=None) -> str:
    """URL of the firm's insights post whose slug or title contains the substrings."""
    global _INS
    if _INS is None:
        _INS = json.load(open(_H.parent / "sources" / "site" / "insights.json"))["rows"]
    exact = [r for r in _INS if r["slug"] == slug_or_title and not sub]
    if exact:
        return exact[0]["url"]
    hits = [r for r in _INS if (slug_or_title.lower() in (r["slug"] + " " + (r.get("title") or "")).lower())
            and sub.lower() in (r["slug"] + " " + (r.get("title") or "")).lower() and (kind is None or r.get("kind") == kind)]
    if len(hits) != 1:
        raise KeyError(f"post({slug_or_title!r}, {sub!r}): {len(hits)} hits {[h['slug'] for h in hits][:5]}")
    return hits[0]["url"]


def art(slug_or_title: str, sub: str = "") -> str:
    """Outbound press article of the firm's Press post matching the substrings."""
    global _INS
    if _INS is None:
        post("__none__") if False else None
        _INS = json.load(open(_H.parent / "sources" / "site" / "insights.json"))["rows"]
    hits = [r for r in _INS if r.get("article_url") and slug_or_title.lower() in (r["slug"] + " " + (r.get("title") or "")).lower()
            and sub.lower() in (r["slug"] + " " + (r.get("title") or "")).lower()]
    if len(hits) != 1:
        raise KeyError(f"art({slug_or_title!r}, {sub!r}): {len(hits)} hits {[h['slug'] for h in hits][:5]}")
    return hits[0]["article_url"]


def sib(slug: str, investor: str, key: str):
    """A sibling book's published value for the same company (siblings.json)."""
    global _SIB
    if _SIB is None:
        _SIB = json.load(open(_H / "siblings.json"))
    for x in _SIB.get(slug, []):
        if x["investor"] == investor:
            return x[key]
    raise KeyError(f"sib({slug}, {investor}, {key})")


def page(slug: str) -> str:
    """The firm's own company page for the row (site list)."""
    return f"https://northzone.com/portfolio/{slug}"


_GS = None
_NEWS = None


def news(name: str, sub: str) -> str:
    """Publisher URL of the one headline in scratch/news-bulk.json for `name` containing `sub`
    (decoded from Google News on demand, cached back into the file)."""
    global _GS, _NEWS
    p = _H / "news-bulk.json"
    _NEWS = json.load(open(p))
    hits = [i for i in _NEWS[name]["items"] if sub.lower() in i["title"].lower()]
    if len(hits) != 1:
        raise KeyError(f"news({name!r}, {sub!r}): {len(hits)} hits {[h['title'][:60] for h in hits][:4]}")
    it = hits[0]
    if not it.get("url"):
        if _GS is None:
            import importlib.util as iu, sys as _s
            spec = iu.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
            _GS = iu.module_from_spec(spec); a = _s.argv; _s.argv = a[:1]; spec.loader.exec_module(_GS); _s.argv = a
        it["url"] = _GS.decode(it["gid"]) or ""
        p.write_text(json.dumps(_NEWS, indent=1, ensure_ascii=False))
    if not it["url"]:
        raise KeyError(f"news({name!r}, {sub!r}): decode failed")
    return it["url"]


def wp(slug: str) -> str:
    """Archived capture of the firm's own WordPress post /YYYY/MM/DD/<slug>/ (scratch/wp-posts-index.json:
    [date, original URL, first capture timestamp]); the capture is the citation where the live site dropped it."""
    idx = json.load(open(_H / "wp-posts-index.json"))
    d, orig, ts = idx[slug]
    return f"https://web.archive.org/web/{ts}/{orig}"


def gsurl(slug: str, sub: str) -> str:
    """Publisher URL of the one headline in scratch/graduation-surfaces.json for `slug` containing `sub`
    (Google News items decoded on demand; other surfaces carry their own link)."""
    global _GS
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
    if _GS is None:
        import importlib.util as iu, sys as _s
        spec = iu.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
        _GS = iu.module_from_spec(spec); a = _s.argv; _s.argv = a[:1]; spec.loader.exec_module(_GS); _s.argv = a
    u = _GS.decode(it["gid"]) or ""
    if not u:
        raise KeyError(f"gsurl({slug!r}, {sub!r}): decode failed")
    return u
