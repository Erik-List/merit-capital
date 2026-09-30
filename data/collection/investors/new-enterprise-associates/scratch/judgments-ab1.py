"""A/B pass ab1 (COLLECTION.md s7, s8 duty 1, verify rule 4): the private $1B+ rows of NEA (PRO-100), plus the
specific checks koudai, radiology-partners and strive-health. Pass A re-pins unicorn-list marks to the round's own
announcement; pass B records newer rounds, tenders and signed deals. Run with NQ_TAG=ab1."""
import json
from pathlib import Path

import judge_lib as jl

AB = json.loads((Path(__file__).resolve().parent / "ab-news.json").read_text())
INVS = jl.INV.parent
CLS = json.loads((jl.INV / "companies/classification.json").read_text())


def X(slug):
    """The row's ab-news headlines (items dated after its mark), for NEWS(extra=...)."""
    return (AB.get(slug) or {}).get("items_after_mark") or []


def N(slug, sub):
    return jl.NEWS(slug, sub, X(slug))


def SIB(inv, slug):
    """A sibling book's cited mark for the same company, read from its classification on disk."""
    c = json.loads((INVS / inv / "companies/classification.json").read_text())
    c = c.get(inv, c)
    u = (c.get(slug) or {}).get("valuation_citation") or ""
    if not u.startswith("http"):
        raise SystemExit(f"SIB({inv!r}, {slug!r}): no citation on disk")
    return u


def STAGECITE(slug):
    u = (CLS.get(slug) or {}).get("entry_stage_citation") or ""
    if not u.startswith("http"):
        raise SystemExit(f"STAGECITE({slug!r}): none")
    return u


def ROUNDS(slug, *new):
    """The row's recorded funding_rounds plus the new entries (record replaces the list, so pass it whole)."""
    have = list((CLS.get(slug) or {}).get("funding_rounds") or [])
    keys = {(r.get("date"), r.get("round")) for r in have}
    return have + [r for r in new if (r["date"], r["round"]) not in keys]


WV = "web_verified"
VRS = {"valuation_range_source": WV}
CP = "Stage citation attempted 2026-09-30 (Google News, the company's name with NEA): no source names the round NEA entered, so the stage is flagged cite_pending."

L = []

# ---- Pass B: newer priced events

L.append(jl.cls("anyscale", rng="1b_plus", usd=1650000000, val_src=WV,
                val_cite=N("anyscale", "optimization startup Anyscale for reported"), asof="2026-07-30",
                clear=["stale"], extra=VRS,
                note="A/B 2026-09-30: Nscale agreed on 2026-07-30 to buy Anyscale for a reported $1.65B (SiliconANGLE, Bloomberg), with completion expected in the second half of 2026; no closing reported by 2026-09-30, so the row stays private at the agreed price, which replaces the stale 2021 Series C mark. The a16z row still carries the 2021 $1B."))

L.append(jl.cls("elevenlabs", rng="10b_plus", usd=22000000000, val_src=WV,
                val_cite=N("elevenlabs", "voice-agent demand - Reuters"), asof="2026-09-30",
                clear=["unicorn_name_match"], extra=VRS,
                note="A/B 2026-09-30: an employee tender of about $300M at a $22B valuation (Reuters, 2026-09-30) replaces the $11B Series D of February 2026 as the mark; the a16z, ICONIQ, Lightspeed and Sequoia rows still read $11B."))

L.append(jl.cls("plaid", rng="1b_plus", usd=8000000000, val_src=WV,
                val_cite=jl.NEWS("plaid", "Plaid valued at $8B in employee share sale"), asof="2026-02",
                stage="Seed", stage_src=WV, stage_conf="high", stage_cite=jl.W("Plaid Inc."),
                entry_date="2013-09-19", grad="graduated", grad_src=WV, grad_cite=jl.W("Plaid Inc."),
                grad_conf="high",
                flags=["stage_disputes_band"], clear=["unicorn_name_match"], extra=VRS,
                rounds=ROUNDS("plaid",
                              jl.rnd("2013-09-19", "Seed", 2800000, "Spark Capital", True, jl.W("Plaid Inc."), "press"),
                              jl.rnd("2014-11-15", "Series A", 12500000, "New Enterprise Associates", True, jl.W("Plaid Inc."), "press"),
                              jl.rnd("2016-06-19", "Series B", 44000000, "Goldman Sachs Investment Partners", None, jl.W("Plaid Inc."), "press"),
                              jl.rnd("2018-12-11", "Series C", 250000000, "Mary Meeker, Index Ventures, Andreessen Horowitz", None, jl.W("Plaid Inc."), "press"),
                              jl.rnd("2021-04-07", "Series D", 425000000, "Altimeter Capital", None, jl.W("Plaid Inc."), "press"),
                              jl.rnd("2025-04", "Strategic sale", 575000000, "Franklin Templeton", True, jl.W("Plaid Inc."), "press"),
                              jl.rnd("2026-02", "Employee share sale", None, None, None, jl.NEWS("plaid", "Plaid valued at $8B in employee share sale"), "press")),
                note="A/B 2026-09-30: the unicorn-list $13.4B (April 2021 Series D) yields to the $6.1B round of April 2025 and the $8B employee share sale of February 2026 (TechCrunch), so the band moves from 10b_plus to 1b_plus, aligned with the Coatue, GV, Ribbit and Spark rows. Stage: Wikipedia names NEA in the $2.8M seed of 2013-09-19 (the firm's year is 2013) and as lead of the $12.5M Series A of 2014-11-15, so the entry is Seed and graduated; the Form D band's Growth read the 2016 Series B."))

L.append(jl.cls("instabase", rng="1b_plus", usd=1240000000, val_src=WV,
                val_cite=jl.NEWS("instabase", "Instabase raises $100M to help companies"), asof="2025-01-17",
                clear=["unicorn_name_match"], extra=VRS,
                rounds=ROUNDS("instabase",
                              jl.rnd("2023-06", "Series C", 45000000, None, None, N("instabase", "Instabase Doubles Valuation to $2B"), "company"),
                              jl.rnd("2025-01-17", "Series D", 100000000, "Qatar Investment Authority", True, jl.NEWS("instabase", "Instabase raises $100M to help companies"), "press")),
                note="A/B 2026-09-30: the $100M Series D of January 2025 led by QIA, with NEA participating, valued Instabase at $1.24B (TechCrunch citing Bloomberg), a down round from the $2B of June 2023; the a16z, General Catalyst, Greylock and Spark rows still read $2B."))

# ---- Pass A: re-pin unicorn-list marks to the round's own announcement

L.append(jl.cls("automation-anywhere", rng="1b_plus", usd=6800000000, val_src=WV,
                val_cite=N("automation-anywhere", "Announces $290 Million in Series B"), asof="2019-11-21",
                stage="Series A", stage_src=WV, stage_conf="high",
                stage_cite=N("automation-anywhere", "Announces $290 Million in Series B"), entry_date="2018",
                flags=["stale", "stage_disputes_band"], clear=["unicorn_name_match"], extra=VRS,
                rounds=ROUNDS("automation-anywhere",
                              jl.rnd("2018", "Series A", 550000000, None, True, N("automation-anywhere", "Announces $290 Million in Series B"), "company"),
                              jl.rnd("2019-11-21", "Series B", 290000000, "Salesforce Ventures", None, N("automation-anywhere", "Announces $290 Million in Series B"), "company")),
                note="The company's release of 2019-11-21 gives the $290M Series B a $6.8B post-money valuation and names NEA among the investors of the $550M Series A announced a year earlier, so the entry is that 2018 Series A (Wikipedia agrees), not the Growth the Form D band read; the mark is stale. The C3.ai merger talks of January 2026 were reported only, with no signed deal."))

L.append(jl.cls("databricks", rng="100b_plus", usd=190000000000, val_src=WV,
                val_cite=SIB("thrive-capital", "databricks"), asof="2026-08-13",
                stage="Growth", stage_src=WV, stage_conf="high", stage_cite=jl.W("Databricks"),
                clear=["unicorn_name_match"], extra=VRS,
                note="A/B 2026-09-30: mark re-pinned to the $5B round that closed on 2026-08-13 at $190B (CNBC, as cited in the Coatue, ICONIQ, Lightspeed, Thrive and Tiger rows). Wikipedia's funding table names NEA the lead of the 2014 Series B, the firm's first year, so the Growth entry is cited."))

L.append(jl.cls("datarobot", rng="1b_plus", usd=6300000000, val_src=WV,
                val_cite=SIB("sutter-hill-ventures", "datarobot"), asof="2021-07-27",
                flags=["stale"], clear=["unicorn_name_match"], extra=VRS,
                note="Mark re-pinned to the $300M Series G of 2021-07-27 at $6.3B (Reuters), stale; no newer priced round. Benzinga (2026-09-22) puts its secondary price 83% under that peak, a secondary estimate that stays out of the figure and still implies about $1B."))

L.append(jl.cls("formlabs", rng="1b_plus", usd=2000000000, val_src=WV,
                val_cite=N("formlabs", "bringing value to $2BN"), asof="2021-05",
                flags=["stale"], clear=["unicorn_name_match"], extra=VRS,
                note="Mark re-pinned to the $150M Series E of May 2021 led by SoftBank Vision Fund 2 at $2B (3D Printing Industry), stale; Bloomberg reported in August 2026 that Formlabs weighs an IPO, with no filing yet."))

L.append(jl.cls("forter", rng="1b_plus", usd=3000000000, val_src=WV,
                val_cite=SIB("tiger-global-management", "forter"), asof="2021-05-25",
                flags=["stale"], clear=["unicorn_name_match"], extra=VRS,
                note="Mark re-pinned to the $300M round of 2021-05-25 at $3B (Reuters), as the Tiger Global row reads, stale; no newer priced round found."))

L.append(jl.cls("goodleap", rng="10b_plus", usd=12000000000, val_src=WV,
                val_cite=N("goodleap", "brings total value to US$12bn"), asof="2021-10-13",
                flags=["stale"], clear=["unicorn_name_match"], extra=VRS,
                note="Mark re-pinned to the $800M round led by MSD Partners of October 2021 at $12B (PV Tech), as the Ribbit row reads, stale; later news is securitizations, no equity round."))

L.append(jl.cls("houzz", rng="1b_plus", usd=4000000000, val_src=WV,
                val_cite=SIB("iconiq-growth", "houzz"), asof="2017-06",
                flags=["stale"], clear=["unicorn_name_match"], extra=VRS,
                note="Mark re-pinned to the $400M Series E led by ICONIQ at $4B (TechCrunch, June 2017), as the ICONIQ and Sequoia rows read, stale; layoffs in 2019 and 2022 and IPO preparation in 2021 but no newer priced round."))

L.append(jl.cls("masterclass", rng="1b_plus", usd=2750000000, val_src=WV,
                val_cite=SIB("atomico", "masterclass"), asof="2021-05-13",
                flags=["stale"], clear=["unicorn_name_match"], extra=VRS,
                note="Mark re-pinned to the $225M Series F of May 2021 at $2.75B (CNBC), as the Atomico and IVP rows read, stale; no newer priced round found."))

L.append(jl.cls("mindtickle", rng="1b_plus", usd=1200000000, val_src=WV,
                val_cite=SIB("accel", "mindtickle"), asof="2021-08",
                flags=["stale", "cite_pending"], clear=["unicorn_name_match"], extra=VRS,
                note="Mark re-pinned to the company's release of the $100M round led by SoftBank Vision Fund 2 at $1.2B (August 2021), as the Accel row reads, stale. " + CP))

L.append(jl.cls("moonpay", rng="1b_plus", usd=3400000000, val_src=WV,
                val_cite=SIB("coatue", "moonpay"), asof="2021-11-22",
                flags=["stale"], clear=["unicorn_name_match"], extra=VRS,
                note="Mark re-pinned to the $555M Series A of 2021-11-22 at $3.4B (CNBC), as the Coatue, Thrive and Tiger rows read, stale; the 2026 news is acquisitions by MoonPay, no new round."))

L.append(jl.cls("ninjaone", rng="10b_plus", usd=12300000000, val_src=WV,
                val_cite=SIB("coatue", "ninjaone"), asof="2026-06-09",
                clear=["unicorn_name_match"], extra=VRS,
                note="Mark re-pinned to the company's own announcement of the $400M Series C extension at $12.3B (2026-06-09), as the Coatue, ICONIQ and Sequoia rows read."))

L.append(jl.cls("patreon", rng="1b_plus", usd=4000000000, val_src=WV,
                val_cite=SIB("coatue", "patreon"), asof="2021-04-06",
                flags=["stale"], clear=["unicorn_name_match"], extra=VRS,
                note="Mark re-pinned to the $155M Series F of April 2021 at $4B (TechCrunch), as the Coatue, Thrive and Tiger rows read, stale. A leaked 2022 memo put the internal valuation 70% lower (Business Insider), an internal figure, not a priced event, and still about $1.2B; 20% layoffs in July 2026."))

L.append(jl.cls("slash", rng="1b_plus", usd=1400000000, val_src=WV,
                val_cite=jl.NEWS("slash", "raises $100M at $1.4B valuation"), asof="2026-04-16",
                clear=["unicorn_name_match"], extra=VRS,
                note="Mark re-pinned to the $100M Series C at $1.4B (TechCrunch, 2026-04-16), as the Ribbit row dates it."))

L.append(jl.cls("splashtop", rng="1b_plus", usd=1000000000, val_src=WV,
                val_cite=N("splashtop", "Achieving Coveted $1 Billion Valuation"), asof="2021-01-27",
                flags=["stale", "cite_pending"], clear=["unicorn_name_match"], extra=VRS,
                note="Mark re-pinned to the company's release of 2021-01-27: $50M of new funding at a $1B valuation, stale; no newer priced round. " + CP))

L.append(jl.cls("together-ai", rng="1b_plus", usd=8300000000, val_src=WV,
                val_cite=SIB("coatue", "together-ai"), asof="2026-07-01",
                clear=["unicorn_name_match"], extra=VRS,
                note="Mark re-pinned to the company's release of the $800M Series C at $8.3B (2026-07-01), as the Coatue, First Round and General Catalyst rows cite."))

L.append(jl.cls("vast-data", rng="10b_plus", usd=30000000000, val_src=WV,
                val_cite=N("vast-data", "Vast Data secures financing at a $30B valuation"), asof="2026-04-22",
                clear=["unicorn_name_match"], extra=VRS,
                note="Mark re-pinned to the $1B Series F of 2026-04-22 at $30B (Axios), as the Tiger Global row reads."))

L.append(jl.cls("zuoyebang", stage="Growth", stage_src=WV, stage_conf="high",
                stage_cite=jl.NEWS("zuoyebang", "Zuoyebang Raises $350M To Help"), entry_date="2018-07-18",
                clear=["unicorn_name_match"],
                rounds=ROUNDS("zuoyebang",
                              jl.rnd("2018-07-18", "Series D", 350000000, "Coatue Management", True,
                                     jl.NEWS("zuoyebang", "Zuoyebang Raises $350M To Help"), "press")),
                note="Stage cited 2026-09-30: Crunchbase News names New Enterprise Associates among the participants in the $350M Series D led by Coatue (2018-07-18), the firm's first year, so the Growth entry is web_verified."))

# ---- Specific checks

L.append(jl.cls("chinaway-technologies-limited", flags=["cite_pending"],
                note="Identity cited 2026-09-30: The Org's company page for G7 Networks reads 'G7 Networks (formerly \"Chinaway\") is China's technology leader for the logistics sector' (https://theorg.com/org/g7-networks), matching the firm's 2013 description (information services for China's logistics industry), so the G7 mark stands, stale. G7 completed a merger with E6 Technology on 2022-06-10 with G7's CEO as chairman and CEO of the merged group (PR Newswire), so the row stays private. " + CP))

L.append(jl.cls("koudai", rng="below_1b", clear=["needs_web_value"],
                note="Web value check 2026-09-30: the Tencent-led $350M Series C of October 2014 disclosed no valuation (TechCrunch: 'did not reveal what valuation'), and no later priced round with a figure was found (Google News, one web search); the $1.4B that vendor profiles attach to that round never bands a row (Rule A), so the row reads below_1b and the flag is cleared."))

L.append(jl.cls("radiology-partners",
                note="R6 check 2026-09-30: NEA was the founding and only institutional investor until Starr Investment Holdings' $700M in July 2019, but it did not control the company: the release gives NEA one seat on an 11-member board led by the CEO with six independent directors (https://www.radpartners.com/2019/07/radiology-partners-receives-700-million-investment-from-starr-investment-holdings/), and physicians hold about a third of the equity, more than the largest outside investor (AuntMinnie, 2021-12-14, https://www.auntminnie.com/industry-news/article/15630042/whats-the-endgame-for-private-equity-in-radiology); so it stays a member (flagged in the report for Erik under R6). The $720M growth equity of February 2024 came with a debt restructuring and no valuation, so the 2019 $4B mark stands, stale."))

L.append(jl.cls("strive-health",
                note="R6 check 2026-09-30: NEA incubated Strive in 2018 (the firm's 2021 post), but it was formed to build a kidney-care service, not to buy operating businesses, and its rounds are syndicated (CapitalG co-led the $140M Series B, CVS Health Ventures led the $166M Series C), so it stays a member."))

L.append(jl.cls("world-labs", flags=["cite_pending"],
                note="A/B 2026-09-30: AMD's all-stock agreement of 2026-09-29 at $8.2B is signed and not closed, so the row stays private at the agreed price; the a16z AI row still reads $5B. " + CP))

L.append(jl.cls("iobeam", flags=["identity_conflated", "cite_pending"],
                note="iobeam is TigerData under its first name (the firm's own iobeam page links timescale.com; identity-merges.json groups timescale and 440-labs-inc under tigerdata but not iobeam), so this row double-counts TigerData's $1B mark and should join that merge at the next rebuild. " + CP))

for s in ("bloomreach", "bytedance-toutiao", "collective-health", "genies", "physical-intelligence", "tigerdata"):
    L.append(jl.cls(s, flags=["cite_pending"], note=CP))

jl.write("ab1", L)
