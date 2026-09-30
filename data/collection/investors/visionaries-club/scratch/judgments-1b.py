#!/usr/bin/env python3
"""Judgments for the last three rows of research group 1 (PRO-103). Writes queue/batch-g1b.out.jsonl."""
import importlib.util
from judge_lib import line, research, write, HERE
spec = importlib.util.spec_from_file_location("j1", HERE / "judgments-1.py")

from judge_lib import rounds


def base(slug, **kw):
    d = research(slug)
    hq = d.get("hq") or {}
    out = dict(status=(d.get("status") or {}).get("value") or "private",
               hq_country=hq.get("country"), hq_country_source="web_verified",
               hq_country_citation=hq.get("citation"), hq_country_confidence="high",
               hq_city=hq.get("city"), hq_city_source="web_verified",
               hq_city_citation=hq.get("citation"), hq_city_confidence="high",
               focus=d.get("focus"), focus_source="model",
               valuation_range="below_1b", valuation_usd=None, funding_rounds=rounds(slug))
    out.update(kw)
    return line(slug, **out)


R = []
d = research("cycle")
R.append(base("cycle", entry_stage="Seed", entry_stage_source="web_verified",
    entry_stage_citation=d["entry"]["citation"], entry_stage_confidence="high", entry_date="2022-05-10",
    seed_to_a_graduation="graduated", graduation_source="web_verified",
    graduation_citation=d["graduation"]["citation"], graduation_confidence="high",
    note="E-bike and e-cargo-bike leasing for couriers and delivery fleets (Berlin; GetHenry until July 2022); Visionaries Club joined LocalGlobe's $17.4M seed of EUR 10M equity and EUR 6.5M debt (TechCrunch 2022-05-10); graduated with Scania Growth Capital's $11.3M Series A of July 2023, Visionaries an existing investor (the company's release); 20VC's 'Cycle' is a different company (Paris product-feedback software), ruled distinct"))
d = research("getharley")
R.append(base("getharley", entry_stage="undetermined",
    note="Skincare telehealth platform (London); the firm listed it before the Index-led $52M round of June 2023 in which Visionaries Club is named (TechCrunch 2023-06-06), and only vendor data puts it in the April 2021 Series A, so the entry round is undetermined, as on Headline's row"))
d = research("getmomo")
R.append(base("getmomo", entry_stage="undetermined",
    note="Rent-deposit guarantees and payments for landlords (Berlin); Seed Fund I is on GetMomo Financial GmbH's shareholder list of 2020-07-13 (register), two years before the unnamed EUR 3.5M round with Element, Atlantic Labs, Visionaries Club and GFC reported in June 2022 (FinanceFWD); no source names the 2020 round, so the entry stage is undetermined"))
write("batch-g1b.out.jsonl", R)
