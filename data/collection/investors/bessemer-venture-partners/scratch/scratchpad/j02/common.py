"""Shared helpers for judge j02 (PRO-80 Bessemer, batches 3 and 4). Citations are read from disk: the siblings
table, sibling books' classification files and the judge's own decoded Google News items (judge_lib.NEWS)."""
import json
import judge_lib as jl

WV, FP = "web_verified", "first_party"
VRS = {"valuation_range_source": "web_verified"}
MOM = "Momentum check 2026-10-01 (Google News, the company's name with round and valuation words): "
GRAD_LATER = "Graduation left for the graduation pass."
_SIB = json.loads((jl.INV / "scratch" / "siblings.json").read_text())


def SIBVAL(slug, investor):
    """The valuation citation a sibling book carries for the same company."""
    m = [x for x in _SIB.get(slug, []) if x["investor"] == investor and x.get("val_cite")]
    if len(m) != 1:
        raise SystemExit(f"SIBVAL({slug!r}, {investor!r}) matched {len(m)}")
    return m[0]["val_cite"]


def SIBCLS(investor, slug, key):
    """One field of a sibling book's classification row (read only)."""
    c = json.loads((jl.INV.parent / investor / "companies" / "classification.json").read_text())
    v = (c.get(slug) or {}).get(key)
    if not v:
        raise SystemExit(f"SIBCLS({investor!r}, {slug!r}, {key!r}) empty")
    return v


# URLs found with WebSearch and read with WebFetch on 2026-10-01 (each says what the row cites it for)
READ = {
    "cents-seed": "https://www.trycents.com/news/cents-announces-4.25m-fundraising-round",
    "crosschq-seed": "https://www.crosschq.com/press/2019/08/07/in-the-news-4/",
    "clarity-money-b": "https://www.fstech.co.uk/fst/Clarity_Money_Series_B_Funding_Round.php",
    "enjoei-lavca": "https://www.lavca.org/bessemer-ventures-leads-r18m-investment-in-enjoei-em-portugues/",
    "doubleai-memo": "https://illai.substack.com/p/the-memo-doubleai-and-the-rise-of",
    "copilotiq-site": "https://copilotiq.com/",
    "criteo-cap": "https://stockanalysis.com/stocks/crto/market-cap/",
    "law-cap": "https://stockanalysis.com/stocks/law/market-cap/",
    "electric-d1": "https://electric.ai/blog/electric-secures-20m-in-d-1-funding-round-bringing-valuation-over-1b",
}
