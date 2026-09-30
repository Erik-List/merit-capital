#!/usr/bin/env python3
"""Judgments for research groups 2 and 4 (PRO-103 grind). Writes
queue/batch-g24.out.jsonl: one classification line per member row (every row
here is already a seeded site_listing member; Uify and Loxo are merge
duplicates of turian and Pallery and get no line)."""
from judge_lib import line, rounds, research, write, usd

R = []


def base(slug, **kw):
    """Research-derived defaults the judge accepted; kw overrides."""
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

# ---------------- group 2 ----------------
d = research("hades-mining")
R.append(base("hades-mining", **stage("web_verified", "Pre-Seed", d["entry"]["citation"], "2025-08-20"),
    valuation_range_source="web_verified", valuation_range_citation="https://sifted.eu/articles/hades-15-million-fundraise-critical-minerals",
    note="Laser drilling for ultra-deep geothermal heat and critical-mineral recovery (Hades Resources GmbH, Munich); Visionaries Tomorrow joined the EUR 5.5M pre-seed led by Project A (tech.eu 2025-08-20; the firm's post: 'We first backed Hades in its EUR 5.5M Pre-Seed') and followed on in the EUR 15M seed of Feb 2026 at a stated EUR 67.5M valuation (Sifted), far below $1B; Tomorrow Fund I is on Hades Resources GmbH's 2026 shareholder lists (register)"))

d = research("hakuna")
R.append(base("hakuna", **stage("web_verified", "Pre-Seed", d["entry"]["citation"], "2021-12-10"),
    focus="Fintech & Payments",
    note="Embedded product-protection insurance sold at checkout (Hakuna GmbH; legal notice Unterhaching, near Munich; registered Berlin-Charlottenburg); Visionaries Club led the EUR 1.5M pre-seed (tech.eu 2021-12-10, Sebastian Pollok quoted) and followed on in Earlybird's EUR 4M seed (tech.eu 2022-09-21); no priced valuation, no later round found"))

R.append(base("hestia-energy", **UND,
    note="Natural (geologic) hydrogen exploration (Hestia Energy Corp., San Francisco; Wyoming project with the University of Wyoming); on tomorrow.vc from April 2025; no source ties Visionaries Tomorrow to a round (Axios reported a $12M seed being raised in June 2026, not closed), so the round is undetermined"))

d = research("incident-io")
R.append(base("incident-io", **UND,
    valuation_range_source="web_verified", valuation_range_citation=d["valuation"]["citation"],
    note="Incident management and on-call platform (London); Visionaries is named in none of the seed, Series A (2022-07, $28.7M) or Series B (2025-04, $62M, Insight) reports, and the firm first listed it between its 2023-06 and 2024-04 portfolio captures, so the entry round is undetermined (possibly a secondary); the Series B was reported at about $400M (TechCrunch, sources), below $1B; Point Nine and Insight hold the same row"))

d = research("insify")
R.append(base("insify", **stage("web_verified", "Series A", d["entry"]["citation"], "2022-02-10"),
    note="Digital SME insurer (MGA; Amsterdam); Visionaries Club joined Accel's EUR 15M Series A as a new investor (TechCrunch 2022-02-10), followed on in Munich Re Ventures' 2023 extension and the EUR 16.3M Series B of Sept 2025 (Evli Growth Partners); no priced valuation published"))

R.append(base("introw", **UND, focus="SaaS",
    note="AI partner relationship management for B2B sales (Introw BV, Ghent); Visionaries Club led an unnamed $3M round in Nov 2025 (the company's own post), after a EUR 1M first round in 2023 without it; no source names the round, so the stage is undetermined"))

d = research("kabilio")
R.append(base("kabilio", **stage("web_verified", "Pre-Seed", d["entry"]["citation"], "2025-11-05"),
    note="Generative-AI platform for Spanish accounting firms (Barcelona); Visionaries Club and Picus Capital co-led the EUR 4M pre-seed (tech.eu 2025-11-05)"))

R.append(base("langdock", **UND,
    note="Model-agnostic enterprise AI platform (Berlin); the public record gives only YC's S23 cheque and the $3M 2024 seed from General Catalyst and La Famiglia (TechCrunch 2024-04-19), neither naming Visionaries; the firm lists it from late 2025 and its GP Judith Dada joined Langdock as co-CEO ('We are partnering with Langdock', visionaries.vc editorial), so the fund's entry round is undetermined; Langdock moved its parent from Delaware to a German SE in Sept 2026 (Euronews 2026-09-16)"))

d = research("leapsome")
R.append(base("leapsome", **stage("web_verified", "Series A", d["entry"]["citation"], "2022-03-24"),
    note="People-enablement platform (Berlin); its $60M Series A led by Insight was its first outside capital after bootstrapping (Startbase 2022-03-24), with Visionaries Club in the round; Growth Fund I is on Leapsome GmbH's 2022 shareholder list (register); no later priced round found"))

d = research("ledgy")
R.append(base("ledgy", **stage("web_verified", "Series A", d["entry"]["citation"], "2021-09-07"),
    note="Equity-management software (Zurich); Visionaries Club joined Sequoia's $10M Series A as a new investor (Startupticker 2021-09-07) and followed on in NEA's EUR 22M Series B (eu-startups 2022-09-21); no priced valuation"))

d = research("level-nine")
R.append(base("level-nine", **stage("web_verified", "Seed", d["entry"]["citation"], "2026-03-17"),
    seed_to_a_graduation="censored",
    note="ML-designed nanozyme catalysts turning biomass into chemical building blocks (Berlin); Visionaries Tomorrow led the EUR 4M seed (tech.eu 2026-03-17), new to the company; the entry is 6 months old, so the graduation is censored"))

d = research("lindus-health")
R.append(base("lindus-health", **stage("web_verified", "Growth", d["entry"]["citation"], "2025-01-22"),
    note="Tech-enabled clinical research organisation (London); Visionaries joined Balderton's $55M Series B as a new investor (PR Newswire 2025-01-22); in Aug 2026 it sold its CRO assets to Curavit Clinical Research and continues as Lindus Therapeutics (Curavit release, PR Newswire 2026-08-18), so the company is still private; no priced valuation"))

d = research("localyze")
R.append(base("localyze", **stage("web_verified", "Growth", d["entry"]["citation"], "2022-09-07"),
    note="Global-mobility software (Hamburg); Visionaries Club joined General Catalyst's $35M Series B (Startup City Hamburg 2022-09-07; Personalwirtschaft); acquired by Boundless Immigration on 2025-10-01, terms undisclosed (Boundless release)"))

d = research("lovable")
R.append(base("lovable", **stage("web_verified", "Seed", d["entry"]["citation"], "2025-02-25"),
    status="private", valuation_range="10b_plus", valuation_usd=13300000000, valuation_source="web_verified",
    valuation_asof="2026-08-12", valuation_citation=d["valuation"]["citation"], valuation_confidence="high",
    seed_to_a_graduation="graduated", graduation_source="web_verified",
    graduation_citation=d["graduation"]["citation"], graduation_confidence="high",
    clear_flags=["unicorn_name_match"],
    note="AI app builder (Stockholm); Visionaries was not in the Oct 2024 pre-seed and entered with Creandum's $15M pre-Series A of Feb 2025 (TechCrunch 2025-02-25), a round before the A read as Seed as on Creandum's row; graduated with Accel's $200M Series A of 2025-07-17 at $1.8B, Visionaries an existing investor (TechCrunch); latest priced round $13.3B (TechCrunch 2026-08-12)"))

d = research("miro")
R.append(base("miro", entry_stage="Growth", entry_stage_source="model", entry_stage_confidence="medium",
    status="private", valuation_range="1b_plus", valuation_usd=1790000000, valuation_source="web_verified",
    valuation_asof="2026-09-10", valuation_citation=d["valuation"]["citation"], valuation_confidence="high",
    hq_country="US", hq_city="San Francisco",
    flags=["model_disputes_source", "cite_pending"], clear_flags=["unicorn_name_match"],
    note="Visual collaboration platform (San Francisco); the firm lists Miro from its first portfolio and TechCrunch named it among Visionaries' investments on 2022-09-22, but neither the Series B (2020-04, ICONIQ) nor the Series C (2022-01, $400M at $17.5B) release names Visionaries, so the round is uncited; it is Growth by construction, since Miro's Series A (2018, Accel) predates the firm (founded 2018-19) and every later round or secondary is Growth; Bending Spoons signed on 2026-09-10 to buy Miro at an equity value of about $1.79B, closing expected Q4 2026, so the row stays private at the agreed price (COLLECTION.md s6); the unicorn list's $17.5B (2022) and Wikidata's NL are overridden"))

d = research("n8n")
R.append(base("n8n", **stage("web_verified", "Growth", d["entry"]["citation"], "2025-10-09"),
    valuation_range="1b_plus", valuation_usd=5200000000, valuation_source="web_verified",
    valuation_asof="2026-05-12", valuation_citation=d["valuation"]["citation"], valuation_confidence="high",
    focus="AI & Applied AI",
    note="Workflow automation and AI orchestration (Berlin); Visionaries joined Accel's $180M Series C at $2.5B as a new investor (n8n's own post, 2025-10-09; tech.eu); Growth Fund II is on n8n GmbH's shareholder lists from 2025-09-30 (register); SAP bought in through a secondary share sale that n8n said values it at $5.2B (tech.eu 2026-05-12), the mark Sequoia, Felicis and Accel carry"))

d = research("nyxium")
R.append(base("nyxium", **stage("web_verified", "Pre-Seed", d["entry"]["citation"], "2026-02-05"),
    note="Agentic AI for siting and permitting energy infrastructure (London); Visionaries Tomorrow led the GBP 2.4M pre-seed (UK Tech News 2026-02-05)"))

d = research("omnia")
R.append(base("omnia", **stage("web_verified", "Pre-Seed", d["entry"]["citation"], "2025-10-16"),
    hq_country="ES", flags=["model_disputes_source"],
    note="Tracks and improves how AI assistants present a brand (Madrid); Visionaries led the EUR 3.5M pre-seed (Tech Funding News 2025-10-16); Wikidata's FI was a one-word name join to another company and is overridden"))

d = research("orbio")
R.append(base("orbio", **UND,
    note="AI-native HR platform for frontline workforces (Madrid); Visionaries Club led an undisclosed first round in 2025 and led again the $7.6M round of Sept 2025 ('led for the second time by Visionaries Club', the company's release on capital-riesgo.es), then joined Dawn Capital's $21M Series A (tech.eu 2026-06-15); the first round is unnamed and undated, so the entry stage is undetermined"))

R.append(base("pallery", **UND,
    note="Buyer-enablement platform for B2B SaaS sales (London), formerly Loxo (loxoapp.com), listed by the firm as Loxo in 2024 and as Pallery since; no announced round under either name (vendor profiles date a 2021 seed with Visionaries and LocalGlobe, not citable), so the entry stage is undetermined"))

# ---------------- group 4 ----------------
R.append(base("the-token-company", **UND,
    note="Compresses LLM prompts to cut cost and latency (San Francisco; YC W26); listed on the firm's 2026 page, but no source ties Visionaries to a round (the ~$500k pre-seed of Dec 2025 names Wave Ventures and Inception Fund), so the entry stage is undetermined"))

d = research("truelayer")
R.append(base("truelayer", **stage("web_verified", "Growth", d["entry"]["citation"], "2021-04-08"),
    status="private", valuation_range="below_1b", valuation_usd=None,
    valuation_range_source="web_verified", valuation_range_citation=d["valuation"]["citation"],
    flags=["model_disputes_source"],
    note="Open-banking payments network (London); Visionaries Club joined the $70M Series D as a new investor (tech.eu 2021-04-08); the 2021 Series E valued it above $1B, but the $50M Series E extension of Oct 2024 was reported at about $700M (Bloomberg via Yahoo, 'loses unicorn'), the latest priced event, so the band is below $1B as on the Northzone and Tiger rows; the unicorn list's $1B is overridden"))

d = research("turian")
R.append(base("turian", **UND, focus="AI & Applied AI",
    note="AI agents that process sales documents (Berlin), renamed from Uify on 2024-10-07 (the firm listed Uify 2023-24); Cherry Ventures and Visionaries Club invested in its first registered round of Aug 2022 (Deutsche Startups 2022-09-20), which no source names, so the entry stage is undetermined"))

d = research("two")
R.append(base("two", **stage("web_verified", "Seed", d["entry"]["citation"], "2021-02-11", conf="medium"),
    status="private", hq_country="NO", hq_city="Oslo",
    seed_to_a_graduation="graduated", graduation_source="web_verified",
    graduation_citation=d["graduation"]["citation"], graduation_confidence="high",
    flags=["model_disputes_source"],
    note="B2B buy-now-pay-later checkout (Oslo; Tillit until 2022); TechCrunch (2021-02-11) names Visionaries Club among the seed investors in the EUR 2.5M round Sequoia led before launch; graduated with the EUR 18M Series A of 2023-03-21 led by Shine Capital and Antler (tech.eu); raised EUR 13M more in July 2025, so it was not acquired: the pre-filled 'acquired' came from a name join and is overridden"))

d = research("vay")
R.append(base("vay", **stage("web_verified", "Growth", d["entry"]["citation"], "2021-12-14"),
    focus="Industrial & Robotics",
    note="Teledriven electric car rental (Berlin); Visionaries Club joined the $95M Series B as a new investor (Vay's own release 2021-12-14); Growth Fund I is on Vay Technology GmbH's shareholder lists (register); Grab's Nov 2025 deal ($60M upfront, up to $350M more) carries no valuation"))

R.append(base("workflex", **UND, focus="SaaS",
    note="Automates compliance for business travel and work abroad (Amsterdam); Visionaries Club is named as a backer of the EUR 37M Spectrum Equity growth investment of 2026-03-17 (vestbee), apparently as an existing investor; the round it entered is not reported, so the stage is undetermined"))

d = research("xentral")
R.append(base("xentral", **stage("web_verified", "Series A", d["entry"]["citation"], "2021-01-13"),
    note="Cloud ERP for online merchants (Augsburg); Visionaries Club was in Sequoia's $20M Series A (TechCrunch 2021-01-13) and Robert Lacher joined the board (VC Magazin 2021-01-19); Growth Fund I and the single-company vehicle Late Growth I are on Xentral ERP Software GmbH's shareholder lists (register 2021-11, 2023); Series B $75M in Aug 2021"))

d = research("yokoy")
R.append(base("yokoy", **stage("web_verified", "Growth", d["entry"]["citation"], "2022-03-29"),
    status="acquired", status_source="web_verified", status_citation=d["status"]["citation"],
    note="Spend management (Zurich); Visionaries Club joined Sequoia's $80M Series B as a new investor (PYMNTS 2022-03-29); acquired by TravelPerk in an all-equity deal on 2025-01-28 (TravelPerk release)"))

d = research("ziggiz")
R.append(base("ziggiz", **UND, focus="Security",
    note="Security data lakehouse (Zigguratum Inc., Chattanooga; listed by the firm as Zigguratum 2024-25); its first Form D (2026-03, $10.75M sold including a converted SAFE) lists Visionaries partner Marton Sarkadi Nagy as a director, but neither the filing nor the press names the round the fund entered (a 2024 $5M seed is vendor-only), so the entry stage is undetermined"))

d = research("tactic")
R.append(base("tactic", **stage("web_verified", "Seed", d["entry"]["citation"], "2022-03-10"),
    status="unknown",
    note="AI account research for sales teams (London); Visionaries Club joined Index's $4.5M seed (TechCrunch 2022-03-10) and listed it until 2023; its UK entity Quantcopy Growth AI Ltd cancelled its bought-back shares in Sept 2025 and was struck off on 2026-02-17 (Companies House) while tactic.fyi stays live, so the state cannot be established: unknown"))

R.append(base("sustained", **UND,
    note="Environmental footprint software for food products (Unimagined Ltd, London); listed on the firm's 2023 portfolio, which suffices for membership (COLLECTION.md s1); the UK entity's only allotment is 2020 and its Estonian parent shows the founders only, so the Visionaries position was likely a convertible; no round is reported, so the stage is undetermined"))

d = research("tytan-technologies")
R.append(base("tytan-technologies", **UND,
    note="AI interceptor drones and counter-drone systems (Munich); Seed Fund II is on TYTAN Technologies GmbH's shareholder list of 2025-08-06 (register), the round of Aug 2025 later confirmed at EUR 16M but never named (Resilience Media 2026-02-24); Visionaries followed on in the EUR 30M Series A of Feb 2026 co-led by Armira and the NATO Innovation Fund; the entry round is unnamed, so the stage is undetermined"))

R.append(base("contextfab", **UND,
    note="Agent operating system for manufacturing (ContextFab GmbH, Munich, founded 2025 as SemSight Ventures); Seed Fund II is on its shareholder list of 2025-10-09 (register), the company's first capital increase; Deutsche Startups (2026-06-02) names Visionaries Club among its investors without naming the round, so the stage is undetermined"))

d = research("acapela")
R.append(base("acapela", **UND, status="defunct", status_source="web_verified",
    status_citation="https://www.northdata.com/Acapela%20GmbH,%20Berlin",
    note="Asynchronous meeting app from Dubsmash co-founder Roland Grenke (Berlin); Visionaries Club led its EUR 2.5M launch round (TechCrunch 2020-10-21), which no source names, and Seed Fund I is on Acapela GmbH's 2020-11-02 shareholder list (register); the company went into liquidation on 2022-09-28 with no sale found (register), so it is defunct"))

DELTA = {"tytan-technologies", "contextfab", "acapela"}
write("batch-g24.out.jsonl", [r for r in R if r["slug"] not in DELTA])
write("delta-g24.out.jsonl", [r for r in R if r["slug"] in DELTA])
