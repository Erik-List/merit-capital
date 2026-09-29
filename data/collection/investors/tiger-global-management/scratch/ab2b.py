#!/usr/bin/env python3
"""A/B pass, slice 2, chunk b (PRO-167): private rows where pass A or pass B changed something:
a fresher priced mark (Innovaccer), a figure the company itself states in USD (Mews), a relocated
head office (Ivalua), better or readable citations (PhonePe, Porter), a note correction (Public.com)
and a newer unpriced round (Rogo). Citations come from the news caches through judge_lib.NEWS, or
from this pass's Bing cache through NB() when one title appears under several publishers.
Run: NQ_TAG=ab2 python3 ab2b.py"""
import json
from pathlib import Path

import judge_lib as jl
from judge_lib import cls, rnd, NEWS

HERE = Path(__file__).resolve().parent
BING = json.loads((HERE / "news-extra-bing-ab2.json").read_text())
CLS = json.loads((HERE.parent / "companies" / "classification.json").read_text())


def NB(slug, sub, source):
    """The one URL in this pass's Bing cache whose title holds `sub` from publisher `source`."""
    urls = {i["url"] for i in BING.get(slug, []) if sub.lower() in i["title"].lower() and i.get("source") == source}
    if len(urls) != 1:
        raise SystemExit(f"NB({slug!r}, {sub!r}, {source!r}) matched {len(urls)}")
    return urls.pop()


def rounds(slug, drop=(), add=()):
    """The row's recorded funding_rounds without the entries dated in `drop`, plus `add`."""
    kept = [r for r in (CLS.get(slug, {}).get("funding_rounds") or []) if r.get("date") not in drop]
    return kept + list(add)


mews_cite = NB("mews", "Mews Secures $300 million", "Yahoo Finance")
public_d2 = NEWS("public-com", "Secures $135m")

L = [
    cls("innovaccer", rng="1b_plus", usd=3450000000, val_src="web_verified",
        val_cite=NEWS("innovaccer", "healthcare's AI powerhouse"), asof="2025-01-09", val_conf="medium",
        clear=("stale",), note=(
            "A/B pass 2026-09-29: fresher priced mark. TechCrunch (2025-01-09, syndicated on Yahoo Finance): the "
            "company declined to give a valuation, but a source put the post-money of the primary part of the $275M "
            "Series F at about $3.45B, up from the $3.2B of December 2021 (the round mixed primary and secondary, and "
            "its named investors do not include Tiger). The mark moves to $3.45B (2025-01-09) and is no longer stale; "
            "layoffs in May 2026 came with no new price. The General Catalyst row still carries $1.3B (2021).")),
    cls("ivalua", city="Massy", city_src="web_verified", note=(
        "A/B pass 2026-09-29: the company's own offices page (ivalua.com/company/offices, read 2026-09-29) lists "
        "its EMEA headquarters at 102 avenue de Paris, Massy, and its Americas headquarters in Redwood City, the "
        "dateline of its releases; no Orsay office remains, so the French head office reads Massy and the country "
        "stays FR. No priced round since the May 2019 $1B mark, which stays stale; the company still operates "
        "(releases through September 2026).")),
    cls("mews", rng="1b_plus", usd=2500000000, val_src="web_verified", val_cite=mews_cite, asof="2026-01-22",
        val_conf="high", flags=("model_disputes_source",),
        rounds=rounds("mews", drop=("2026-01-26",), add=[
            rnd("2026-01-22", "Series D", 300000000, lead="EQT Growth", firm_in_round=True, source=mews_cite,
                source_type="company")]),
        note=(
            "A/B pass 2026-09-29: the company's release of 2026-01-22 (PR Newswire, on Yahoo Finance) says the "
            "$300M Series D led by EQT Growth, with Tiger Global among the existing investors taking part, 'values "
            "the company at $2.5 billion'. The figure is USD at source, so it replaces the EUR 2B of NL Times "
            "converted at the ECB rate ($2.37B). The Atomico row ($2.37B) should follow; the Battery row already "
            "reads $2.5B, with London where this row and Atomico's read Amsterdam.")),
    cls("phonepe", usd=12000000000, val_src="web_verified",
        val_cite=NEWS("phonepe", "PhonePe raises $100 mn from Ribbit Capital"), asof="2023-02-14", note=(
            "A/B pass 2026-09-29: the mark is now cited to the press report of the priced round (Business Today, "
            "2023-02-14: $100M from Ribbit, Tiger Global and TVS Capital at a $12B valuation) instead of Wikipedia. "
            "No priced event since: the IPO papers of 2025-2026 set no price, Reuters (2026-03-04) reported a target "
            "of $9B to $10.5B, below the 2023 round, before the IPO was paused in March 2026, and a target is not a "
            "priced event, so the 2023 mark stands, stale.")),
    cls("porter", usd=1200000000, val_src="web_verified",
        val_cite=NEWS("porter", "Porter raises $200 million in Series F"), asof="2025-05-08", note=(
            "A/B pass 2026-09-29: the valuation citation moves from an MSN page that renders no text to The New "
            "Indian Express report of the same round ($200M Series F led by Kedaara and Wellington, valuation about "
            "$1.2B). No later priced round found (FY26 results reported in August 2026).")),
    cls("public-com", rounds=rounds("public-com", drop=("2025-03",), add=[
            rnd("2024-12-02", "Series D-2", 105000000, lead="Accel", firm_in_round=None, source=public_d2)]),
        note=(
            "A/B pass 2026-09-29: correction to the note above. The FinTech Futures report of a Tiger-led $200M "
            "investment is the February 2021 round (Google News dated a re-publication 2025-03-26), not a 2025 deal, "
            "and its funding-round entry is removed. The later Series D-2 of December 2024 ($105M equity and $30M "
            "debt, led by Accel; LeapRate) disclosed no valuation. Vendor figures (Forge, Tracxn, GetLatka) range "
            "from about $0.5B to $2B and do not band a row (Rule A), so the February 2021 $1.2B mark stands, stale. "
            "The Accel row reads below_1b with no mark or note.")),
    cls("rogo", rounds=rounds("rogo", add=[
            rnd("2026-09-10", "Strategic", None, lead=None, firm_in_round=None,
                source=NEWS("rogo", "Rogo secures strategic investments"))]),
        note=(
            "A/B pass 2026-09-29: the September 2026 strategic investments by Citi, Barclays, BNP Paribas, Societe "
            "Generale and MUFG (Capital Brief, 2026-09-10; reported at about $30M) came with no stated valuation, so "
            "the April 2026 Series D at $2B stays the mark. The Sequoia and Thrive rows still read below_1b.")),
]

if __name__ == "__main__":
    jl.write("ab-2b", L)
