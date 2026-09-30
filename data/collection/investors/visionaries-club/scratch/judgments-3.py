#!/usr/bin/env python3
"""Judgments for research group 3 (PRO-103 grind). Writes queue/batch-g3.out.jsonl."""
from judge_lib import line, rounds, research, write, usd

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

d = research("pave-space")
R.append(base("pave-space", **stage("web_verified", "Seed", d["entry"]["citation"], "2026-03-25"),
    seed_to_a_graduation="censored",
    note="Orbital transfer vehicles moving satellites beyond low orbit (Lausanne; every round article places it in Switzerland, Creandum's row says Munich); Visionaries Club and Creandum co-led the $40M seed (Payload 2026-03-25); the entry is 6 months old, so the graduation is censored"))

# Personio: partner-carried prior-firm deal (Menlo rule) -> verdict only
R.append({"slug": "personio", "verdict": "not_member", "who": "agent-judge-pro103", "evidence_class": "web",
    "confidence": "medium",
    "citation": "https://www.visionaries.vc/#team",
    "basis": "Partner-carried prior-firm deal (COLLECTION.md s1, Erik's ruling of 2026-09-17 on Menlo, which binds every investor): Robert Lacher's own bio on the firm's team section credits Personio to La Famiglia ('Prior to Visionaries, he was the Founding Partner of La Famiglia ... including investments in companies such as Deel, Groq and Personio') while it lists Lovable, n8n, Pigment, Miro, Tacto and Pave Space as his Visionaries deals; Judith Dada's bio also credits it to La Famiglia; no Series C, D or E report (2020-2022) and no register filing names a Visionaries fund, and the firm's listings carry no date; the firm lists it as portfolio and TechCrunch (2022-09-22) repeated that from the fund announcement, so the reading is raised for Erik (decisions.md R1)"})

d = research("pigment")
R.append(base("pigment", **UND,
    valuation_range="1b_plus", valuation_usd=1000000000, valuation_source="web_verified",
    valuation_asof="2024-04-04", valuation_confidence="medium",
    valuation_citation="https://fintech.global/2024/05/08/new-fintech-unicorn-births-remain-stable-with-three-new-additions-in-april-2024/",
    flags=["stale"],
    note="Business planning and forecasting platform (Paris); Robert Lacher's bio names Pigment among his Visionaries deals and the firm has listed it since its first portfolio, but no Series A to D report names Visionaries, so the entry round is undetermined; the $145M Series D of April 2024 gave it a $1B valuation (FinTech Global 2024-05-08, 'France's newest FinTech unicorn'), the IVP and ICONIQ rows' mark; stale beyond 24 months"))

d = research("pivot")
R.append(base("pivot", **stage("web_verified", "Pre-Seed", d["entry"]["citation"], "2023-04"),
    note="AI procure-to-pay platform (Paris); Visionaries was in the EUR 5M pre-seed of April 2023 (tech.eu 2023-10-02, Robert Lacher quoted) and in the $21.6M Series A of Dec 2023 from existing investors 'in particular Visionaries' (TechCrunch 2023-12-12); Series B $40M in May 2026"))

d = research("pledge")
R.append(base("pledge", **stage("web_verified", "Seed", d["entry"]["citation"], "2021-10-22"),
    status="acquired", status_source="web_verified", status_citation=d["status"]["citation"],
    seed_to_a_graduation="graduated", graduation_source="web_verified",
    graduation_citation=d["graduation"]["citation"], graduation_confidence="high",
    note="Carbon measurement and removal API, later logistics emissions accounting (London); Visionaries Club led the $4.5M seed (TechCrunch 2021-10-22); graduated with the $10M Series A of May 2023 (Business Insider); Blue Yonder acquired the business on 2025-05-02, terms undisclosed (ESG Today)"))

d = research("proxima-fusion")
v, det = usd(2400000000, "EUR", "2026-07-07")
R.append(base("proxima-fusion", **stage("web_verified", "Pre-Seed", d["entry"]["citation"], "2023-11-16"),
    valuation_range="1b_plus", valuation_usd=v, valuation_source="web_verified",
    valuation_asof="2026-07-07", valuation_citation=d["valuation"]["citation"], valuation_confidence="high",
    note=f"Stellarator fusion power plants (Munich, Max Planck spin-out); Visionaries Tomorrow came in through the pre-seed extension to EUR 7.5M (tech.eu 2023-11-16), then the EUR 20M seed and the EUR 130M Series A; Tomorrow Fund I is on Proxima Fusion GmbH's shareholder list of 2023-12-14 (register); the EUR 411M round of July 2026 valued it at EUR 2.4B (company release), {det}, the mark the Balderton, Lightspeed and Cherry rows carry"))

d = research("qonversion")
R.append(base("qonversion", **stage("web_verified", "Seed", d["entry"]["citation"], "2021-12"),
    hq_country="GB", hq_city="London", hq_country_confidence="medium", hq_city_confidence="medium",
    hq_country_citation="https://qonversion.io/blog/qonversion-raised-seed-round-2021/",
    hq_city_citation="https://qonversion.io/blog/qonversion-raised-seed-round-2021/",
    note="Subscription infrastructure SDK for mobile apps; Visionaries Club and Flashpoint co-led the $2M seed (the company's own post, Dec 2021), which was to set up its headquarters in London; its current privacy policy gives Qonversion Inc. at a San Francisco shared-office address, read as the US entity's registered address, so London is kept at medium confidence"))

d = research("quantive")
R.append(base("quantive", **stage("web_verified", "Growth", d["entry"]["citation"], "2021-12-16"),
    status="acquired", status_source="web_verified", status_citation=d["status"]["citation"],
    note="OKR and strategy-execution software (Denver; Gtmhub until Dec 2022); Visionaries Club joined Index's $120M Series C as a new investor (PR Newswire 2021-12-16); acquired by WorkBoard on 2025-05-28, terms undisclosed"))

d = research("radical-dot")
R.append(base("radical-dot", **stage("first_party", "Pre-Seed", d["entry"]["citation"], "2025-03-03"),
    note="Catalytic upcycling of mixed plastic waste into chemical building blocks (Munich); Visionaries Tomorrow and UVC Partners co-led the EUR 2.7M pre-seed (the firm's own post, 2025-03-03)"))

d = research("rows")
R.append(base("rows", entry_stage="Growth", entry_stage_source="model", entry_stage_confidence="medium",
    entry_date="2020",
    status="acquired", status_source="web_verified", status_citation=d["status"]["citation"],
    note="Collaborative spreadsheet with an AI analyst (Berlin); Growth Fund I is on Rows GmbH's shareholder lists from 2020 (register), but no report names Visionaries in a round; Growth by construction, since Rows' $8M Series A (May 2018) predates the firm, so any Visionaries entry was a later round; acquired by Superhuman (formerly Grammarly) on 2026-02-24, terms undisclosed (inventure.com.ua), which the Cherry and Accel rows do not yet carry"))

d = research("secjur")
R.append(base("secjur", **stage("web_verified", "Seed", d["entry"]["citation"], "2022-12-05"),
    focus="SaaS",
    note="Compliance automation for SMEs: data protection, information security, whistleblowing (Hamburg); Visionaries Club led the EUR 5.5M seed, the company's first outside capital (Startup City Hamburg 2022-12-05); a Nov 2024 round carries no amount or round name"))

d = research("sirenopt")
R.append(base("sirenopt", **stage("web_verified", "Seed", d["entry"]["citation"], "2024-07-23"),
    note="Plasma sensing plus machine learning for real-time inspection of coatings (Oakland; UC Berkeley spin-out); Voyager Ventures and Visionaries Tomorrow co-led the $6.6M seed (the company's release, 2024-07-23); an unnamed $6.5M round of Oct 2025 is below twice the seed"))

d = research("solve-intelligence")
R.append(base("solve-intelligence", **stage("web_verified", "Growth", d["entry"]["citation"], "2025-12-09"),
    note="AI for drafting and analysing patents (London and San Francisco; YC S23); Visionaries led the $40M Series B with 20VC co-leading (IPWatchdog release 2025-12-09), absent from the Series A; London kept to agree with the 20VC and YC rows"))

d = research("superlist")
R.append(base("superlist", **UND,
    note="Task management from the Wunderlist founders (Berlin); Visionaries Club was an existing investor at EQT Ventures' EUR 10M seed of April 2022 (ArcticStartup), so it entered through the unnamed earlier capital of 2020-21; Seed Fund I is on Superlist Software GmbH's 2025 shareholder lists (register); the entry round is unnamed, so the stage is undetermined"))

d = research("tacto")
R.append(base("tacto", **stage("first_party", "Pre-Seed",
    "https://www.visionaries.vc/editorial/tacto-ai-why-we-love-to-back-founders-before-day-one", "2020-06"),
    note="AI procurement operating system for industrial SMEs (Munich); the firm's own post says it signed a term sheet on 2020-06-12 'to lead Tacto's pre-seed round' before the company was incorporated, and Seed Fund I is on Tacto Technology GmbH's shareholder list of 2020-08-24 (register); Visionaries followed on in the EUR 5.3M seed (2022) and the EUR 50M Series A led by Sequoia (Dec 2023)"))

d = research("taktile")
R.append(base("taktile", **UND,
    note="AI decision platform for credit, risk and fraud (Berlin-founded, now New York-headquartered per tech.eu 2022-11-22; the Balderton, Tiger and YC rows say Berlin); Visionaries Club is named as an existing investor at the $54M Series B of Feb 2025 (Pulse 2.0), but no source ties it to the 2021 seed or the 2022 Series A, so the entry round is undetermined"))

d = research("tandem-health")
R.append(base("tandem-health", **stage("web_verified", "Series A", d["entry"]["citation"], "2025-06-30"),
    note="AI clinical assistant and clinic operating system (Stockholm); Visionaries joined Kinnevik's $50M Series A, absent from the 2024 seed (SiliconANGLE 2025-06-30), and followed on in the $100M Series B of Sept 2026; no valuation disclosed"))

d = research("taxdoo")
R.append(base("taxdoo", **stage("web_verified", "Series A", d["entry"]["citation"], "2020-12-15"),
    note="VAT and accounting compliance for cross-border e-commerce (Hamburg); Visionaries Club joined Accel's $21M Series A as a new investor (TechCrunch 2020-12-15) and the EUR 57M Series B (Dec 2021); Growth Fund I is on Taxdoo GmbH's 2023 shareholder list (register); in 2025 Taxdoo was a buyer (accountDigital), not a target"))

R.append(base("tendrils-compute", **UND,
    note="Many-core chip architecture built on interaction nets (Cambridge, UK; weak: the jobs page's preferred location); listed on the firm's 2026 page with no announced round; Tendrils Compute Limited was incorporated on 2026-09-29 at a London law-firm address, so the entry round is undetermined"))

d = research("thaleron")
R.append(base("thaleron", **UND,
    hq_city="Maidenhead", hq_country="GB",
    note="Undersea flywheel long-duration energy storage (Maidenhead; registered office Woking); only vendor feeds date a $12.7M round of Oct 2023 with Visionaries Club and Firstminute (Nordic9), which may band nothing and name no stage (Rule A), and a Companies House allotment of 2023-12-07 corroborates a late-2023 raise; the entry round is undetermined"))

write("batch-g3.out.jsonl", R)
