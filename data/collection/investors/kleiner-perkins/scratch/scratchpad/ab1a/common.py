"""Shared helpers of the A/B pass ab1a (PRO-99 Kleiner Perkins; COLLECTION.md s7, s8 duty 1, verify rule 4).
Citations are read from disk (the row's own record, a sibling book, the news caches) or are pages this pass read
itself on 2026-09-30 (READ, each fetched with scratchpad/ab1a/grab.py or WebFetch and checked for the sentence
cited). Run with NQ_TAG=ab1a."""
import json

import judge_lib as jl

INV = jl.INV
INVS = INV.parent
_C = json.loads((INV / "companies/classification.json").read_text())
_C = _C.get("kleiner-perkins", _C)
_R = json.loads((INV / "companies/resolved.json").read_text())
_R = _R.get("kleiner-perkins", _R)
WV = "web_verified"
VRS = {"valuation_range_source": WV}
AB = "A/B 2026-09-30: "

# Pages read by this pass (found through WebSearch or a sibling's citation, then fetched and read).
READ = {
    # "Ilya Fushman joined Index Ventures in 2015 where he ... held board positions in companies such as Slack,
    # Intercom, Optimizely, KeepTruckin, CultureAmp, Built, CoverWallet, Scratch, and Nova Credit."
    "kp-fushman": "https://www.kleinerperkins.com/perspectives/ilya-fushman-joins-kleiner-perkins-as-general-partner-and-managing-member/",
    # "The funding round was led by Index Ventures along with Felicis Ventures and Blackbird Ventures. Index partner
    # Ilya Fushman will join the Australian company's board" (2016-03-07)
    "techeu-cultureamp": "https://tech.eu/2016/03/07/culture-amp-london-office/",
    # "has raised $10 million in a Series A round. The funding comes from Mamoon Hamid from Social Capital along
    # with Slack CEO Stewart Butterfield and Intercom CEO Eoghan McCabe." (2016-05-26)
    "techeu-front": "https://tech.eu/2016/05/26/front-10-million/",
}


def row(slug):
    return {**_R.get(slug, {}), **_C.get(slug, {})}


def have(slug):
    return [dict(r) for r in (row(slug).get("funding_rounds") or [])]


def ROUNDS(slug, *new, drop=()):
    """The row's recorded funding_rounds plus the new entries (record replaces the list, so it is passed whole).
    `drop` names recorded rounds (by their `round` word) that a new entry restates with a better source."""
    old = [r for r in have(slug) if r.get("round") not in drop]
    keys = {(r.get("date"), r.get("round")) for r in old}
    out = old + [r for r in new if (r["date"], r["round"]) not in keys]
    return sorted(out, key=lambda r: str(r.get("date") or ""))


def RC(slug, sub):
    """A URL already on the row (its funding_rounds or its valuation or stage citation) containing `sub`."""
    r = row(slug)
    urls = {x.get("source") for x in have(slug)} | {r.get("valuation_citation"), r.get("entry_stage_citation")}
    m = sorted(u for u in urls if u and sub in u)
    if len(m) != 1:
        raise SystemExit(f"RC({slug!r}, {sub!r}) matched {len(m)}: {m}")
    return m[0]


def SIB(inv, slug):
    """A sibling book's cited mark for the same company, read from its classification on disk."""
    c = json.loads((INVS / inv / "companies/classification.json").read_text())
    c = c.get(inv, c)
    u = (c.get(slug) or {}).get("valuation_citation") or ""
    if not u.startswith("http"):
        raise SystemExit(f"SIB({inv!r}, {slug!r}): no citation on disk")
    return u


def N(slug, sub):
    return jl.NEWS(slug, sub)


def CP(slug):
    """cite_pending for a $1B+ row whose entry round this pass could not cite, unless the stage pass (sta/stb,
    running beside this one) has cited it in the meantime."""
    r = row(slug)
    cited = bool((r.get("entry_stage_citation") or "").strip()) or r.get("entry_stage_source") == "formd_structural"
    return [] if cited else ["cite_pending"]


def keep(slug, text, flags=(), **kw):
    """A defended row: nothing changes but the dated note."""
    return jl.cls(slug, note=AB + text, flags=flags, **kw)
