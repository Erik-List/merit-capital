"""Helpers for the Bain Capital Ventures grind (PRO-162), adapted from the EQT Ventures run (PRO-163): build .out.jsonl lines under the
current record contract (COLLECTION.md §6/§8, run.py validate_record).

A member needs TWO lines: the verdict line and a classification line (record
routes a line by the presence of `verdict`; a single line carrying both drops
every classification key). `cls()` emits only the keys it is given, so a line
never clobbers a filing-grade fact it was not asked about.
"""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

WHO = "agent-judge-pro162"
ROOT = Path(__file__).resolve().parents[5]
Q = ROOT / "data" / "collection" / "investors" / "bain-capital-ventures" / "scratch" / "queue"


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
        r = subprocess.run(["python3", "scripts/run.py", "record", "--investor", "bain-capital-ventures",
                            str(p)], cwd=ROOT, capture_output=True, text=True)
        print(r.stdout[-4000:], r.stderr[-2000:])


# ---- citations read from disk, never typed (the Balderton lesson: 19 typed
# citations were wrong). Each helper refuses an ambiguous or missing match.
_INV = ROOT / "data" / "collection" / "investors" / "bain-capital-ventures"
_POSTS = json.loads((_INV / "sources/site/insights-text.json").read_text())["rows"]
_WIKI = json.loads((_INV / "sources/web/wikipedia-insource.json").read_text())
WIKI_CACHE = _INV / "scratch" / "wiki"
LISTING = "https://baincapitalventures.com/portfolio/"


def POST(sub):
    """The firm's own insight post whose slug contains `sub` (exactly one)."""
    m = [p for p in _POSTS if sub in (p.get("slug") or "")]
    if len(m) != 1:
        raise SystemExit(f"POST({sub!r}) matched {len(m)}: {[p['slug'] for p in m[:4]]}")
    return f"https://baincapitalventures.com/insight/{m[0]['slug']}/"


def _base():
    return {r["slug"]: r for r in json.loads((_INV / "companies/base.json").read_text())}


def SITE(slug):
    """The company's deep link on baincapitalventures.com, by base slug."""
    u = (_base().get(slug) or {}).get("site_url") or ""
    if "baincapital" not in u:
        raise SystemExit(f"SITE({slug!r}): no firm page on the row")
    return u


def W(title):
    """A Wikipedia article URL, from a title on disk (the insource sweep, or scratch/wiki/<title>.txt)."""
    for a in (_WIKI.get("articles") or _WIKI.get("rows") or []):
        t = a.get("title") or a.get("article")
        if t == title and a.get("url"):
            return a["url"]
    raw = WIKI_CACHE / (title.replace(" ", "_") + ".txt")
    if raw.exists() and raw.stat().st_size > 2000 and not raw.read_text()[:20].upper().startswith("#REDIRECT"):
        return "https://en.wikipedia.org/wiki/" + title.replace(" ", "_")
    raise SystemExit(f"W({title!r}) not on disk")


def ARC(ts, path):
    """An Internet Archive capture of the firm's own page."""
    return f"https://web.archive.org/web/{ts}/http://www.baincapitalventures.com{path}"


# ---- news citations: a headline from scratch/news-sweep.json, decoded to the publisher's URL
# through graduation-surfaces.decode(), cached in scratch/news-decoded.json so a re-run is offline.
_NEWS = json.loads((Path(__file__).with_name("news-sweep.json")).read_text()) \
    if Path(__file__).with_name("news-sweep.json").exists() else {}
# Parallel judges (NQ_TAG set) write their own news-extra-<tag>.json and news-decoded-<tag>.json;
# every judge reads all of them, so a citation found by one is visible to the rest.
import os as _os
_TAG = _os.environ.get("NQ_TAG")
_DEC_P = Path(__file__).with_name(f"news-decoded-{_TAG}.json" if _TAG else "news-decoded.json")
_DEC = {}
for _f in sorted(Path(__file__).parent.glob("news-decoded*.json")):
    _DEC.update(json.loads(_f.read_text()))
_GS = None


def _gs():
    global _GS
    if _GS is None:
        import importlib.util as _u, sys as _s
        sp = _u.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
        m = _u.module_from_spec(sp)
        argv, _s.argv = _s.argv, _s.argv[:1]
        sp.loader.exec_module(m)
        _s.argv = argv
        _GS = m
    return _GS


def NEWS(slug, sub, extra=None):
    """The publisher URL of the one headline in the row's news sweep (or `extra`, a list of items
    from another query) whose title contains `sub`; refuses an ambiguous or missing match."""
    ex = []
    for _f in sorted(Path(__file__).parent.glob("news-extra*.json")):
        ex += json.loads(_f.read_text()).get(slug, [])
    items = list((_NEWS.get(slug) or {}).get("items") or []) + ex + list(extra or [])
    m = [i for i in items if sub.lower() in i["title"].lower()]
    gids = list(dict.fromkeys(i["gid"] for i in m if i.get("gid")))
    if len(gids) != 1:
        raise SystemExit(f"NEWS({slug!r}, {sub!r}) matched {len(gids)}: {[i['title'][:80] for i in m[:4]]}")
    g = gids[0]
    if g not in _DEC:
        url = _gs().decode(g)
        if not url:
            raise SystemExit(f"NEWS({slug!r}, {sub!r}): decode failed")
        _DEC[g] = url
        mine = json.loads(_DEC_P.read_text()) if _DEC_P.exists() else {}
        mine[g] = url
        _DEC_P.write_text(json.dumps(mine, indent=1) + "\n")
    return _DEC[g]


_MAN = json.loads((_INV / "sources/wayback/cc-manifest.json").read_text()) \
    if (_INV / "sources/wayback/cc-manifest.json").exists() else {}


def CCPAGE(path_sub):
    """The Common Crawl capture URL (index form) of the firm's own archived page whose path contains
    `path_sub` (the earliest capture); refuses a missing match."""
    m = sorted((v for v in _MAN.values() if v.get("status") == "ok" and path_sub in v.get("path", "")),
               key=lambda v: v["timestamp"])
    if not m:
        raise SystemExit(f"CCPAGE({path_sub!r}) matched nothing")
    return m[0]["capture_url"]


# ---- S2A helpers (graduation pass). FORMD_ROUNDS(slug) reads the company's Form D sequence; FORMD_CITE(slug, i) is
# the index URL of round i (the accessions are the citation for a formd graduation); GRADLINES(slug, ...) writes the
# absence test's graduation_surfaces lines (COLLECTION.md s6) from scratch/graduation-surfaces.json, the firm's posts,
# the Form D sequence and sibling rows, so every judge records the same surfaces in the same words.
_GS_FILE = Path(__file__).with_name("graduation-surfaces.json")
_FIR = json.loads((_INV / "sources/edgar/formd-issuer-rounds.json").read_text())
_LABEL = {"googlenews": "Google News, the company's name with round and exit words",
          "googlenews_firm": "Google News, the company's name beside the firm's",
          "googlenews_local": "Google News in the company's own edition and language",
          "techcrunch": "TechCrunch's own search", "crunchbase_news": "Crunchbase News's own search"}
_LATER = re.compile(r"(?i)series [a-h]\b|series-[a-h]\b|\$\d[\d.,]*\s?(m|million|b|billion)\b.*(round|raise|funding|financing)|raises|raised|funding|financing")


def FORMD_ROUNDS(slug):
    return (_FIR.get(slug) or {}).get("rounds") or []


def FORMD_CITE(slug, i=-1):
    r = FORMD_ROUNDS(slug)[i]
    cik = str(int(r["cik"]))
    return f"https://www.sec.gov/Archives/edgar/data/{cik}/{r['accession'].replace('-', '')}/{r['accession']}-index.htm"


def GRADLINES(slug, name=None, firm_note=None, formd_note=None, extra=()):
    """The absence test's surface lines for one row. `firm_note` / `formd_note` override the default wording of those two
    surfaces; `extra` appends lines (e.g. 'sibling:usv: ... -> ...', 'company: ... -> ...', 'wikipedia: ... -> ...')."""
    gs = json.loads(_GS_FILE.read_text()).get(slug) or {}
    name = name or gs.get("name") or (_base().get(slug) or {}).get("name") or slug
    out = []
    posts = [p for p in _POSTS if name.split(" (")[0].lower() in ((p.get("title") or "") + " " + (p.get("body") or "")).lower()]
    if firm_note:
        out.append("firm: " + firm_note)
    else:
        newest = max(posts, key=lambda p: p.get("date") or "") if posts else None
        out.append(f"firm: the firm's own posts and portfolio page for {name} -> "
                   + (f"{len(posts)} post(s), the newest '{newest['title'][:90]}' ({(newest.get('date') or '')[:10]}); none names a later round"
                      if newest else "no post names the company beyond the listing"))
    if formd_note:
        out.append("formd: " + formd_note)
    else:
        rs = FORMD_ROUNDS(slug)
        out.append("formd: the company's Form D filings on EDGAR -> " + (
            "; ".join(f"{(r.get('sale_date') or r.get('quarter'))[:10]} ${r.get('offering_usd') or 0:,.0f}" for r in rs)
            + "; no later priced round at twice the entry" if rs else "no filing by the company"))
    for surf, v in (gs.get("surfaces") or {}).items():
        its = [i for i in v.get("items", []) if i.get("names")]
        fund = [i for i in its if _LATER.search(i["title"])]
        newest = max(fund, key=lambda i: i["date"]) if fund else None
        out.append(f"{surf}: {_LABEL.get(surf, surf)} -> "
                   + (f"{len(its)} headline(s) naming the company, the newest funding report '{newest['title'][:100]}' ({newest['date']}); no Series A or later round"
                      if newest else f"{len(v.get('items', []))} result(s), none reporting a later round of the company"))
    for sb in gs.get("siblings") or []:
        out.append(f"sibling:{sb.get('investor')}: its row for {sb.get('name')} -> "
                   + (f"S2A {sb.get('seed_to_a_graduation')} ({sb.get('graduation_source')})" if sb.get("seed_to_a_graduation") else "no later round in its note"))
    return out + list(extra)
