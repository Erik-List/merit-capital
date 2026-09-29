#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 7, chunk c (rows 31-45). Run: NQ_TAG=b7 python3 judgments-7c.py"""
import json
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, SEC, W

INV = HERE.parent
CAPS = json.loads(Path("/private/tmp/claude-501/-Users-erik-Developer-merit-capital/"
                       "e4102706-b045-419d-94c7-a1402905b586/scratchpad/j78-caps.json").read_text())


def U(slug, sub, host=None):
    """The one publisher URL on disk (news-extra*.json) whose headline contains `sub`."""
    items = []
    for f in sorted(HERE.glob("news-extra*.json")):
        items += json.loads(f.read_text()).get(slug, [])
    urls = list(dict.fromkeys(i["url"] for i in items if i.get("url") and sub.lower() in i["title"].lower()
                              and (host is None or host in i["url"])))
    if len(urls) != 1:
        raise SystemExit(f"U({slug!r}, {sub!r}, {host!r}) matched {len(urls)}: {urls[:4]}")
    return urls[0]


def LED(slug):
    v = json.loads((INV / "companies/membership-ledger.json").read_text())["tiger-global-management"]["verdicts"]
    c = (v.get(slug) or {}).get("citation")
    if not c:
        raise SystemExit(f"LED({slug!r}): no seed citation")
    return c


def SIB(inv, slug, key):
    c = json.loads((INV.parent / inv / "companies/classification.json").read_text())
    v = (c.get(slug) or {}).get(key)
    if not v:
        raise SystemExit(f"SIB({inv!r}, {slug!r}, {key!r}): missing")
    return v


WV = {"valuation_range_source": "web_verified"}
CLR = ("needs_web_value", "unicorn_name_match")
L = []

# ---- jellyfish
jf = LED("jellyfish")
L.append(cls("jellyfish", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=jf, stage_conf="high", entry_date="2022-02-01",
             city="Boston", focus="SaaS",
             rounds=[rnd("2022-02-01", "Series C", 71_000_000, "Accel, Insight Partners and Tiger Global", True, jf,
                         "company")],
             note="Engineering-management platform (Boston). Tiger co-led the $71M Series C of Feb 2022 with Accel and "
                  "Insight, its first round in the company. Below $1B as in the Accel and Insight rows."))

# ---- jobstreet: a co-investor in SEEK's takeover, a control transaction
L.append(verdict("jobstreet", "not_member",
                 "Tiger came in as a co-investor, with News Corp and Macquarie, in SEEK's 2014 takeover of JobStreet's "
                 "online employment business for RM1.73 billion (Wikipedia): a whole-business purchase by the "
                 "co-investor group from a company listed on Bursa Malaysia, not a financing round (T3, control "
                 "positions)", ec="web", conf="high", cite=W("Jobstreet"), exclusion="control_position"))

# ---- jodo
jd = U("jodo", "Jodo raises $15 million in Series A round led by Tiger Global", "moneycontrol.com")
L.append(cls("jodo", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=jd, stage_conf="high", entry_date="2022-08-08",
             country="IN", country_src="web_verified", country_cite=jd, city="Bangalore", focus="Fintech & Payments",
             rounds=[rnd("2022-08-08", "Series A", 15_000_000, "Tiger Global", True, jd, "press")],
             note="Education-fee financing (Bengaluru). Tiger led the $15M Series A of Aug 2022 at about $90M "
                  "(Entrackr), with existing investors Elevation and Matrix India. Momentum check 2026-09-29 (Bing): no "
                  "later round found."))

# ---- jokr: membership open
jk = U("jokr", "3 Months After Launch, Grocery Platform JOKR Raises $170M")
L.append(verdict("jokr", "member",
                 "Yahoo Finance (Jul 2021): JOKR 'raised $170 million in a Series A investment round led by GGV "
                 "Capital, Balderton Capital and Tiger Global'; Bisnow and TechCrunch say the same, and Tiger joined "
                 "the $260M Series B of Dec 2021", ec="web", conf="high", cite=jk))
L.append(cls("jokr", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=jk, stage_conf="high", entry_date="2021-07-20",
             country="US", city="New York", focus="Consumer & Marketplaces",
             rounds=[rnd("2021-07-20", "Series A", 170_000_000, "GGV Capital, Balderton Capital and Tiger Global", True,
                         jk, "press"),
                     rnd("2021-12-02", "Series B", 260_000_000, None, True, None, "press"),
                     rnd("2023-09", "Series D", 50_000_000, None, None,
                         SIB("balderton-capital", "jokr", "valuation_citation"), "press")],
             note="Quick-commerce grocery delivery (New York, operating in Latin America). Tiger co-led the $170M Series "
                  "A of Jul 2021 (Polish press had named Tiger among the backers at the April launch, the same round) "
                  "and joined the $260M Series B at $1.2B. Aligned with Balderton's row: the Sep 2023 Series D priced "
                  "it at $800M post-money (PYMNTS), below the 2021 to 2023 marks, so below $1B. It left the US and Europe "
                  "in 2022 and Colombia in Apr 2026; still operating elsewhere."))

# ---- jupiter
jp = U("jupiter", "Neobank Startup Jupiter Mops Up $87 Mn")
jb = U("jupiter", "Nubank co-leads $45 million investment", "finance.yahoo.com")
L.append(cls("jupiter", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=jp, stage_conf="high", entry_date="2021-12-27",
             country="IN", country_src="web_verified", country_cite=jb, city="Bangalore", focus="Fintech & Payments",
             rounds=[rnd("2021-08-05", "Series B", 45_000_000, "Nubank, Global Founders Capital, Sequoia, Matrix", False,
                         jb, "press"),
                     rnd("2021-12-27", "Series C", 87_000_000, "Tiger Global and Sequoia India", True, jp, "press")],
             note="Consumer neobank (Bangalore and Mumbai, TechCrunch; the pre-filled JP is a wrong join). The Aug 2021 "
                  "Series B was co-led by Nubank, Global Founders Capital, Sequoia and Matrix, with no Tiger; Tiger came "
                  "in on the Series C of Dec 2021 (inc42), valued about $710M by late 2022. Momentum check: the Oct 2025 "
                  "$15M came from existing backers at a flat value (Economic Times B2B); no $1B round. Y Combinator's "
                  "'Jupiter' row is a different company with the same name: not aligned."))

# ---- just-eat-takeaway-com-n-v (seeded ec=filing): listed-company 13G
L.append(verdict("just-eat-takeaway-com-n-v", "not_member",
                 "13G/13F position in a listed company, no private round naming the firm (T3, D3): Just Eat "
                 "Takeaway.com (Takeaway.com listed in 2016) appears in the adviser's 13G filings 2021 to 2023 and in "
                 "its 13F only 2021-06 to 2021-12", ec="fund_filing", conf="high",
                 cite=SEC("just-eat-takeaway-com-n-v", "edgar")))

# ---- juul
L.append(cls("juul", status="private", rng="below_1b", stage="undetermined",
             city="Washington", focus="Consumer & Marketplaces", flags=("model_disputes_source",),
             rounds=[rnd("2018-07-10", None, 650_000_000, None, None, None, "press")],
             note="Juul Labs, e-cigarettes (Washington, DC). The pre-filled 'acquired' is disputed: Altria bought a 35% "
                  "minority stake in Dec 2018 (Tiger sold part of its holding into that deal, Bloomberg) and exchanged "
                  "it back for IP in Mar 2023; Juul is an independent private company. Membership rests on the CMBS "
                  "filing naming Tiger among private Juul's investors; Tiger's entry round is not named in anything "
                  "read (it was an early investor and cut its own mark to $19B in Dec 2019, WSJ), so stage undetermined. "
                  "Below $1B on the collapse evidence Coatue's row cites (Altria wrote its stake down to $250M)."))

# ---- kajabi
kj = LED("kajabi")
L.append(cls("kajabi", status="private",
             rng="1b_plus", usd=2_000_000_000, val_src="web_verified", val_cite=kj, asof="2021-05-04",
             stage="Growth", stage_src="web_verified", stage_cite=kj, stage_conf="high", entry_date="2021-05-04",
             city="Irvine", focus="SaaS", flags=("stale",), extra=WV,
             rounds=[rnd("2021-05-04", "growth financing", 550_000_000, "Tiger Global", True, kj, "company")],
             note="Platform for creators selling courses and memberships (Irvine). Bootstrapped until Tiger led the "
                  "$550M growth financing of May 2021, 'valuation over $2 billion' (the release), read as $2B; no later "
                  "priced round found, stale."))

# ---- kanzhun-boss-zhipin
kz = CAPS["kanzhun-boss-zhipin"]
L.append(cls("kanzhun-boss-zhipin", status="public",
             rng="1b_plus", usd=kz["usd"], val_src="web_verified", val_cite=kz["url"], asof=kz["asof"], extra=WV,
             stage="undetermined",
             country="CN", country_src="web_verified", country_cite=LED("kanzhun-boss-zhipin"), city="Beijing",
             focus="Consumer & Marketplaces", rounds=[],
             note="Kanzhun, operator of the BOSS Zhipin recruitment app (Beijing; Nasdaq BZ since Jun 2021, also Hong "
                  "Kong). The F-1/A calls Tiger Global Investments, L.P. (a public-desk fund) 'another affiliate of one "
                  "of our shareholders', so a Tiger entity held shares before the IPO; the holding vehicle and the round "
                  "are not named (principal-holder table lists no Tiger), so the stage is undetermined, and the IPO "
                  "subscription itself is not a venture entry. Market cap $6.36B on 2026-09-29 (stockanalysis)."))

# ---- karat (Seattle technical interviewing; not the Los Angeles Karat Financial)
kr = LED("karat")
kv = U("karat", "Karat raises $110M on a $1.1B valuation")
L.append(cls("karat", status="private",
             rng="1b_plus", usd=1_100_000_000, val_src="web_verified", val_cite=kv, asof="2021-10-13", extra=WV,
             stage="Growth", stage_src="web_verified", stage_cite=kr, stage_conf="high", entry_date="2019-05-15",
             country="US", city="Seattle", focus="SaaS", flags=("stale", "model_disputes_source"),
             rounds=[rnd("2019-05-15", "Series B", 28_000_000, "Tiger Global", True, kr, "company"),
                     rnd("2021-10-13", None, 110_000_000, "Tiger Global", True, kv, "press")],
             note="Karat, technical interviewing as a service (Seattle). The pre-filled status 'defunct' and country RU "
                  "come from a wrong Wikidata join: the company operates (it bought Byteboard in Jan 2025, GeekWire). "
                  "Tiger led the $28M Series B of May 2019 (the release: 'Series B', with Norwest and 8VC existing), its "
                  "entry, and the $110M round of Oct 2021 at $1.1B, the last priced mark (stale). The Coatue and Union "
                  "Square Ventures 'Karat' rows are Karat Financial of Los Angeles, a different company: not aligned."))

# ---- kard: membership open
kd = U("kard", "Kard Finalizes $23M Series A", "crowdfundinsider")
L.append(verdict("kard", "member",
                 "Crowdfund Insider (May 2022): Kard 'secured $23 million via a Series A round led by Tiger'; Citi's "
                 "own release of Aug 2026 names Tiger Global among Kard's backers", ec="web", conf="high", cite=kd))
L.append(cls("kard", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=kd, stage_conf="high", entry_date="2022-04-27",
             country="US", city="New York", focus="Fintech & Payments",
             rounds=[rnd("2022-04-27", "Series A", 23_000_000, "Tiger Global", True, kd, "press")],
             note="Card-rewards API (New York). Tiger led the $23M Series A of Apr 2022. Citi agreed in Aug 2026 to buy "
                  f"Kard ({U('kard', 'Citi Expands Customer Engagement', 'nasdaq.com')}), price not disclosed; still 'plans to acquire' on 2026-09-25, so the row stays "
                  "private until the deal closes. Momentum check: no $1B round."))

# ---- kaskada-inc: Lee Fixel's 2020 seat is Addition's
L.append(verdict("kaskada-inc", "not_member",
                 "Lee Fixel's director seat on Kaskada's 2020 Form D falls after he left Tiger in early 2019 to found "
                 "Addition, and decisions.md D7 names Kaskada among Addition's seats; no Tiger round names the company",
                 ec="formd_adjudicated", conf="high", cite=SEC("kaskada-inc")))

# ---- katapult-holdings-inc (seeded ec=filing): shares taken at the SPAC merger
L.append(verdict("katapult-holdings-inc", "not_member",
                 "Tiger Global Investments, L.P., a public-desk fund, reported 5,000,000 shares (5.6%) on a Rule "
                 "13d-1(c) 13G with a date of event of 2021-06-09, the closing of Katapult's merger with FinServ "
                 "Acquisition Corp: a block taken at the listing (PIPE-sized), and no private round names the firm "
                 "(T3, D3, D6)", ec="fund_filing", conf="high", cite=SEC("katapult-holdings-inc", "edgar")))
L.append(cls("katapult-holdings-inc", flags=("boundary",),
             note="Not a member: shares first held at the 2021 de-SPAC closing by a public-desk fund (D6, boundary)."))

# ---- kavak
kvk = W("Kavak (company)")
L.append(cls("kavak", status="private",
             rng="1b_plus", usd=2_200_000_000, val_src="web_verified",
             val_cite=SIB("ribbit-capital", "kavak", "valuation_citation"), asof="2025-03", extra=WV, clear=CLR,
             stage="undetermined",
             country="MX", country_src="web_verified", country_cite=kvk, city="Mexico City",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2021-04", "Series D", 485_000_000, "D1, Founders Fund, Ribbit, BOND", None, None, "press"),
                     rnd("2021-09", "Series E", 700_000_000, "General Catalyst", None, None, "press"),
                     rnd("2025-03", None, 127_000_000, "SoftBank and General Atlantic", None,
                         SIB("ribbit-capital", "kavak", "valuation_citation"), "press"),
                     rnd("2026-02-17", "Series F", 300_000_000, "Andreessen Horowitz", None,
                         U("kavak", "Kavak Raises $300 Million In Series F"), "press")],
             note="Used-car marketplace and financing (Mexico City). Wikipedia names Tiger Global among Kavak's investors "
                  "but no source read ties Tiger to a round (Bing, 2026-09-29), so the stage is undetermined. Mark "
                  "aligned with Ribbit's row: $2.2B at the Mar 2025 round (Contxto), the collapse from the $8.7B of "
                  "Sep 2021; the Feb 2026 $300M Series F (a16z) was reported without a valuation."))

# ---- klue
kl = LED("klue")
L.append(cls("klue", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=kl, stage_conf="medium", entry_date="2021-12-01",
             country="CA", country_src="web_verified",
             country_cite=U("klue", "Vancouver’s Klue raises US$62-million", "theglobeandmail.com"),
             city="Vancouver", focus="SaaS",
             rounds=[rnd("2021-12-01", "Series B", 62_000_000, "Tiger Global", True, kl, "press")],
             note="Competitive-intelligence software (Vancouver). Tiger led the US$62M round of Dec 2021 (TechCrunch; "
                  "the Globe and Mail: 'Tiger bites further into Canadian tech'), its first, after earlier seed and "
                  "Series A money: a later round, Growth. No $1B mark."))

if __name__ == "__main__":
    jl.write("batch-007c", L)
