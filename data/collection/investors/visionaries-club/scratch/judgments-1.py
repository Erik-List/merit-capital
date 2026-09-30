#!/usr/bin/env python3
"""Judgments for research group 1 (PRO-103 grind). Writes queue/batch-g1.out.jsonl."""
import os
from judge_lib import line, rounds, research, write, usd, HERE

R = []


def base(slug, **kw):
    d = research(slug)
    hq = d.get("hq") or {}
    out = dict(
        status=(d.get("status") or {}).get("value") or "private",
        hq_country=hq.get("country"), hq_country_source="web_verified",
        hq_country_citation=hq.get("citation"), hq_country_confidence="high",
        hq_city=hq.get("city"), hq_city_source="web_verified",
        hq_city_citation=hq.get("citation"), hq_city_confidence="high",
        focus=d.get("focus"), focus_source="model",
        valuation_range="below_1b", valuation_usd=None,
        funding_rounds=rounds(slug),
    )
    st = d.get("status") or {}
    if out["status"] in ("acquired", "defunct") and st.get("citation"):
        out["status_citation"] = st["citation"]
        out["status_source"] = "web_verified"
    out.update(kw)
    return line(slug, **out)


def stage(src, stage_, cite, date, conf="high"):
    return dict(entry_stage=stage_, entry_stage_source=src, entry_stage_citation=cite,
                entry_stage_confidence=conf, entry_date=date)


UND = dict(entry_stage="undetermined")

d = research("11x")
R.append(base("11x", **UND,
    valuation_range_source="web_verified", valuation_range_citation=d["valuation"]["citation"],
    note="AI 'digital workers' for sales teams (San Francisco); Visionaries is absent from the pre-seed (2023) and the partial Series A lists (2024-09, Benchmark) and first named among the company's backers in its Series B release (a16z, 2024-11-11), so the entry round is undetermined; the Series B was reported at about $350M (TechCrunch, sources), below $1B"))

d = research("accountable")
R.append(base("accountable", **UND,
    note="Bookkeeping and tax app for the self-employed (Berlin); listed on the firm's 2026 page only, and neither the EUR 6M Series A (2021, Stride.VC) nor its 2022 extension names Visionaries, so the entry round is undetermined; acquired by Visma on 2025-04-25 (Handelsblatt)"))

d = research("adfin")
R.append(base("adfin", **stage("web_verified", "Seed", d["entry"]["citation"], "2024-07", conf="medium"),
    seed_to_a_graduation="graduated", graduation_source="web_verified",
    graduation_citation=d["graduation"]["citation"], graduation_confidence="high",
    note="Payments and cash-flow automation for SMBs (London); Index Ventures and Visionaries Club co-led the $4.9M seed (TechCrunch 2024-07-10, 'has already raised', so the close date is approximate); graduated with Index's $18M Series A of 2026-05-12, Visionaries an existing investor (tech.eu)"))

d = research("allonic")
R.append(base("allonic", **stage("web_verified", "Pre-Seed", d["entry"]["citation"], "2026-02-10"),
    note="Automated manufacturing of robotic bodies, 3D tissue braiding (Budapest; the site's footer names a US parent, Allonic Inc.); Visionaries Club led the $7.2M pre-seed, Hungary's largest (tech.eu 2026-02-10)"))

d = research("ameba")
R.append(base("ameba", entry_stage="Pre-Seed", entry_stage_source="web_verified",
    entry_stage_citation=d["entry"]["citation"], entry_stage_confidence="high",
    note="AI that turns supply-chain emails, PDFs and spreadsheets into live data (London; Ameba Systems Ltd, 2023); Visionaries Club led the pre-seed, undated and unsized, and reinvested in Hedosophia's $7.1M seed of Oct 2024 (tech.eu 2024-10-02)"))

d = research("apron")
R.append(base("apron", **UND,
    note="Invoice and supplier-payment automation for small businesses (London); Visionaries Club is an existing investor at the $15M Series A of 2023-09-28 (UKTN), but the only earlier round, Bessemer's $5.5M seed of June 2023, does not name it, so the entry round is undetermined; Series B $30M in Sept 2024"))

d = research("arago")
R.append(base("arago", **stage("web_verified", "Seed", d["entry"]["citation"], "2025-07-08"),
    seed_to_a_graduation="censored",
    note="Photonic AI accelerator chips (Paris); Earlybird, Protagonist and Visionaries Tomorrow co-led the $26M seed (tech.eu 2025-07-08); the entry is under 24 months old, so the graduation is censored"))

d = research("arculus")
R.append(base("arculus", **stage("web_verified", "Series A", d["entry"]["citation"], "2019-12", conf="medium"),
    status="acquired", status_source="web_verified", status_citation=d["status"]["citation"],
    flags=["model_disputes_source"],
    note="Modular production and autonomous mobile robots (Munich); the firm's text dates its check to a pre-emptive round of Dec 2019 alongside Atomico, which Atomico's post calls the Series A it led; Robert Lacher's earlier seed check was personal (Atomico: 'seed round investor & board member'), not a fund position (decisions.md D6); Growth Fund I is on arculus GmbH's 2020-21 shareholder lists (register); acquired by Jungheinrich on 2021-11-10 (The Robot Report); the pre-filled SEC float came from a weak name join and is overridden"))

d = research("autarc")
R.append(base("autarc", **stage("web_verified", "Seed", d["entry"]["citation"], "2024-12", conf="medium"),
    focus="SaaS", seed_to_a_graduation="censored",
    note="Planning, quoting and field software for heat-pump and solar installers (Berlin; YC S24); the founders write that the seed closed 'mit Visionaries Club' (pv magazine 2025-03-18, which prints 'Ende 2025' for a close it already reports, read as end of 2024, when the firm first lists it); a coarse 2024-12 entry is still inside the 24-month window, so the graduation is censored"))

d = research("automaited")
R.append(base("automaited", **stage("web_verified", "Pre-Seed", d["entry"]["citation"], "2021-01", conf="medium"),
    note="AI agents that key customer sales orders into ERP systems (Cologne); pre-seed in early 2021 from TechVision Fonds I, Visionaries Club and angels (the company's seed release of 2022-04-28); Visionaries followed on in Headline's EUR 4M seed"))

d = research("black-forest-labs")
R.append(base("black-forest-labs", **stage("web_verified", "Growth", d["entry"]["citation"], "2025-12-01"),
    valuation_range="1b_plus", valuation_usd=3250000000, valuation_source="web_verified",
    valuation_asof="2025-12-01", valuation_citation=d["valuation"]["citation"], valuation_confidence="high",
    note="Frontier image-generation lab behind FLUX (Freiburg); Visionaries Club is among the new investors in the $300M Series B at a $3.25B post-money, co-led by Salesforce Ventures and AMP (tech.eu 2025-12-01; the company's release), absent from the a16z seed and Series A"))

d = research("causaly")
R.append(base("causaly", **UND,
    note="AI platform for biomedical research and drug discovery (London); Visionaries is not named in the 2019 or May 2021 Series A releases but is a returning investor in the $60M Series B of July 2023 (the company's release; TechCrunch), so it entered between them through an unannounced round or a secondary; the entry round is undetermined"))

d = research("choco")
R.append(base("choco", **stage("web_verified", "Series A", d["entry"]["citation"], "2019-10-28", conf="medium"),
    valuation_range="1b_plus", valuation_usd=1200000000, valuation_source="web_verified",
    valuation_asof="2022-04-12", valuation_citation=d["valuation"]["citation"], valuation_confidence="high",
    flags=["stale"],
    note="Ordering and AI-agent software for food distributors and restaurants (Berlin); TechCrunch lists Visionaries Club among the investors at the Bessemer-led $33.5M Series A (2019-10-28) and Crunchbase News confirms it as an existing backer in Coatue's $30.2M tranche (2020-04-16); the firm dates from late 2018, so an earlier seed check is unlikely but not excluded (medium); Growth Fund I is on Choco Communications GmbH's shareholder lists 2020-2025 (register); the $111M Series B2 of April 2022 valued it at $1.2B (Restaurant Business), the Coatue and Insight rows' mark, stale beyond 24 months"))

d = research("codewords")
R.append(base("codewords", **stage("web_verified", "Seed", d["entry"]["citation"], "2026-05-07"),
    seed_to_a_graduation="censored",
    note="Proactive AI automation agent for business workflows (London; formerly Agemo); Visionaries led the $9M seed (tech.eu 2026-05-07), not named in the earlier pre-seed; the entry is under 24 months old, so the graduation is censored"))

d = research("cosmic-aerospace")
R.append(base("cosmic-aerospace", **stage("web_verified", "Seed", d["entry"]["citation"], "2024-02-06"),
    hq_country_confidence="medium", hq_city_confidence="medium",
    note="All-electric regional aircraft (Brussels per AeroTime; tech.eu calls it US-European, with a demonstrator site near Denver); Visionaries Tomorrow joined Pale blue dot's $4.5M seed (tech.eu 2024-02-06)"))

d = research("courtcorrect")
R.append(base("courtcorrect", **stage("web_verified", "Seed", d["entry"]["citation"], "2021-11"),
    note="AI complaints-management software for regulated firms (London); Visionaries Club participated in the GBP 2.2M ($2.95M) seed of Nov 2021 (Business Insider 2021-12-08), as on 20VC's row"))

d = research("h-company")
R.append(base("h-company", **stage("web_verified", "Seed", d["entry"]["citation"], "2024-05-21"),
    note="Paris AI lab building agentic computer-use models (formerly Holistic AI); Visionaries Club is among the investors in the $220M seed of May 2024 (TechCrunch 2024-05-21), partly convertible debt, so no priced valuation; all five co-founders have left and an ex-Palantir executive runs it (Maddyness 2026-09-07); still private and operating"))

for slug in ("cycle", "getharley", "getmomo"):
    if os.path.exists(HERE / "research" / f"{slug}.json"):
        print("NOTE: research for", slug, "is ready; add its judgment")

write("batch-g1.out.jsonl", R)
