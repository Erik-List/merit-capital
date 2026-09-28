"""Helpers for the Ribbit Capital grind (PRO-161), adapted from the Bain Capital
Ventures run (PRO-162): build .out.jsonl lines under the current record contract
(COLLECTION.md s6/s8, run.py validate_record).

A member needs TWO lines: the verdict line and a classification line (record
routes a line by the presence of `verdict`; a single line carrying both drops
every classification key). `cls()` emits only the keys it is given, so a line
never clobbers a filing-grade fact it was not asked about.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
from pathlib import Path

WHO = "agent-judge-pro161"
ROOT = Path(__file__).resolve().parents[5]
SLUG = "ribbit-capital"
_INV = ROOT / "data" / "collection" / "investors" / SLUG
Q = _INV / "scratch" / "queue"
LISTING = "https://ribbitcap.com/rebels"
ADV = "https://reports.adviserinfo.sec.gov/reports/ADV/165308/PDF/165308.pdf"


def verdict(slug, v, basis, ec="site_listing", conf="high", cite=None, extra=None):
    d = {"slug": slug, "verdict": v, "who": WHO, "evidence_class": ec, "basis": basis,
         "confidence": conf}
    if cite:
        d["citation"] = cite
    if extra:
        d.update(extra)
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
    """One funding_rounds entry in the s6 form."""
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
        r = subprocess.run(["python3", "scripts/run.py", "record", "--investor", SLUG, str(p)],
                           cwd=ROOT, capture_output=True, text=True)
        print(r.stdout[-6000:], r.stderr[-3000:])


# ---- citations read from disk, never typed (the Balderton lesson: 19 typed
# citations were wrong). Each helper refuses an ambiguous or missing match.
_WIKI = json.loads((_INV / "sources/web/wikipedia-insource.json").read_text())
WIKI_CACHE = _INV / "scratch" / "wiki"


def _base():
    return {r["slug"]: r for r in json.loads((_INV / "companies/base.json").read_text())}


def SITE(slug):
    """The firm's live Rebels list, for a row it lists today."""
    u = (_base().get(slug) or {}).get("site_url") or ""
    if "ribbitcap.com" not in u:
        raise SystemExit(f"SITE({slug!r}): not on the live list")
    return LISTING


def ARCH(slug):
    """The row's first archived listing capture (Internet Archive or Common Crawl form)."""
    u = (_base().get(slug) or {}).get("wayback_first_link") or ""
    if not u:
        raise SystemExit(f"ARCH({slug!r}): no archived listing on the row")
    return u


def W(title):
    """A Wikipedia article URL, from a title on disk (the insource sweep, or scratch/wiki/<title>.txt)."""
    for a in (_WIKI.get("articles") or _WIKI.get("rows") or []):
        t = a.get("title") or a.get("article")
        if t == title and a.get("url"):
            return a["url"]
    raw = WIKI_CACHE / (title.replace(" ", "_") + ".txt")
    if raw.exists() and raw.stat().st_size > 1500 and not raw.read_text()[:20].upper().startswith("#REDIRECT"):
        return "https://en.wikipedia.org/wiki/" + title.replace(" ", "_")
    raise SystemExit(f"W({title!r}) not on disk")


# ---- news citations: a headline from scratch/news-sweep.json (or a judge's own
# nq.py query), decoded to the publisher's URL through graduation-surfaces.decode(),
# cached so a re-run is offline. Parallel judges (NQ_TAG set) write their own
# news-extra-<tag>.json and news-decoded-<tag>.json; every judge reads all of them.
_HERE = Path(__file__).resolve().parent
_NEWS = json.loads((_HERE / "news-sweep.json").read_text()) if (_HERE / "news-sweep.json").exists() else {}
_TAG = os.environ.get("NQ_TAG")
_DEC_P = _HERE / (f"news-decoded-{_TAG}.json" if _TAG else "news-decoded.json")
_DEC = {}
for _f in sorted(_HERE.glob("news-decoded*.json")):
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
    """The publisher URL of the one headline in the row's news items whose title
    contains `sub`; refuses an ambiguous or missing match."""
    ex = []
    for _f in sorted(_HERE.glob("news-extra*.json")):
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


# ---- Form D helpers. FORMD_ROUNDS(slug) reads the company's Form D sequence;
# FORMD_CITE(slug, i) is the index URL of round i. SPV(code) is the Form D index
# of one of the firm's single-deal vehicles (sources/registers/spv-decode.json).
_FIR = json.loads((_INV / "sources/edgar/formd-issuer-rounds.json").read_text())
_SPV_P = _INV / "sources/registers/spv-decode.json"


def FORMD_ROUNDS(slug):
    return (_FIR.get(slug) or {}).get("rounds") or []


def FORMD_CITE(slug, i=-1):
    r = FORMD_ROUNDS(slug)[i]
    cik = str(int(r["cik"]))
    return f"https://www.sec.gov/Archives/edgar/data/{cik}/{r['accession'].replace('-', '')}/{r['accession']}-index.htm"


def SPV(code):
    """The Form D index URL of the firm's deal vehicle whose code is `code` (e.g. 'RH-D')."""
    d = json.loads(_SPV_P.read_text())
    m = [v for v in d["vehicles"] if v["code"] == code and v.get("accession")]
    if len(m) != 1:
        raise SystemExit(f"SPV({code!r}) matched {len(m)}")
    v = m[0]
    return (f"https://www.sec.gov/Archives/edgar/data/{int(v['cik'])}/"
            f"{v['accession'].replace('-', '')}/{v['accession']}-index.htm")


# ---- S2A helpers (graduation pass): GRADLINES(slug, ...) writes the absence
# test's graduation_surfaces lines (COLLECTION.md s6) from
# scratch/graduation-surfaces.json, the firm's listing, the Form D sequence and
# sibling rows, so every judge records the same surfaces in the same words.
_GS_FILE = _HERE / "graduation-surfaces.json"
_LABEL = {"googlenews": "Google News, the company's name with round and exit words",
          "googlenews_firm": "Google News, the company's name beside the firm's",
          "googlenews_local": "Google News in the company's own edition and language",
          "techcrunch": "TechCrunch's own search", "crunchbase_news": "Crunchbase News's own search"}
_LATER = re.compile(r"(?i)series [a-h]\b|series-[a-h]\b|\$\d[\d.,]*\s?(m|million|b|billion)\b.*(round|raise|funding|financing)|raises|raised|funding|financing")


def GRADLINES(slug, name=None, firm_note=None, formd_note=None, extra=()):
    """The absence test's surface lines for one row. `firm_note` / `formd_note`
    override the default wording; `extra` appends lines."""
    gs = json.loads(_GS_FILE.read_text()).get(slug) or {} if _GS_FILE.exists() else {}
    b = _base().get(slug) or {}
    name = name or gs.get("name") or b.get("name") or slug
    out = []
    out.append("firm: " + (firm_note or (
        f"the firm's own listings for {name} (live Rebels list, archived Bets / Our Bets pages "
        f"{b.get('wayback_years') or 'none'}) -> the firm publishes names only, no round")))
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
