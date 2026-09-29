#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 7, chunk a (rows 1-15). Run: NQ_TAG=b7 python3 judgments-7a.py"""
import json
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, SEC

INV = HERE.parent


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
    """The citation of the row's recall seed in the ledger."""
    v = json.loads((INV / "companies/membership-ledger.json").read_text())["tiger-global-management"]["verdicts"]
    c = (v.get(slug) or {}).get("citation")
    if not c:
        raise SystemExit(f"LED({slug!r}): no seed citation")
    return c


def SIB(inv, slug, key):
    """A sibling book's cited value (rule 10 alignment), read from its classification file."""
    c = json.loads((INV.parent / inv / "companies/classification.json").read_text())
    v = (c.get(slug) or {}).get(key)
    if not v:
        raise SystemExit(f"SIB({inv!r}, {slug!r}, {key!r}): missing")
    return v


WV = {"valuation_range_source": "web_verified"}
CLR = ("needs_web_value", "unicorn_name_match")
L = []

# ---- honeybook
hb = U("honeybook", "valued at $2.4 bln", "reuters.com")
L.append(cls("honeybook", status="private",
             rng="1b_plus", usd=2_400_000_000, val_src="web_verified", val_cite=hb, asof="2021-11-03",
             stage="Growth", stage_src="web_verified", stage_cite=hb, stage_conf="high", entry_date="2021-11-03",
             country="US", city="San Francisco", focus="SaaS", flags=("stale",), clear=CLR, extra=WV,
             rounds=[rnd("2021-05-04", "Series D", 155_000_000, "Durable Capital Partners", None,
                         U("honeybook", "HoneyBook raises $155 million, becomes unicorn"), "press"),
                     rnd("2021-11-03", "Series E", 250_000_000, "Tiger Global", True, hb, "press")],
             note="Client-management and payments software for independent businesses (San Francisco, Israeli-founded). "
                  "Tiger led the $250M Series E of Nov 2021 at $2.4B (Reuters); the May 2021 $155M Series D was led by "
                  "Durable Capital at $1.1B and no source read names Tiger in it, so the entry is read at the Series E "
                  "(Growth either way). No later priced round: TechCrunch (Mar 2025) still gives the late-2021 $2.4B as "
                  "the last valuation; mark stale, no collapse evidence found. Matches Battery's $2.4B."))

# ---- hopin
hp = U("hopin", "Hopin raises $125 mln", "reuters.com")
L.append(cls("hopin", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=hp, stage_conf="high", entry_date="2020-11-10",
             country="GB", country_src="web_verified", country_cite=hp, city="London", focus="SaaS",
             rounds=[rnd("2020-11-10", "Series B", 125_000_000, "IVP and Tiger Global", True, hp, "press")],
             note="Virtual events platform, London. Tiger came in on the $125M Series B of Nov 2020 (Reuters: raises "
                  "$125M from Tiger Global, Accel; Coatue's row reads it as led by IVP and Tiger Global); the $40M "
                  "Series A of Jun 2020 was IVP-led with no Tiger. RingCentral bought the events business in Aug 2023 "
                  "and Bending Spoons the rest in 2024: acquired, as in the a16z, Accel, Coatue, General Catalyst, IVP "
                  "and 20VC rows."))

# ---- horizon-lines-inc (seeded ec=filing): listed-company 13G
L.append(verdict("horizon-lines-inc", "not_member",
                 "13G/13F position in a listed company, no private round naming the firm (T3, D3): Horizon Lines "
                 "listed on the NYSE in 2005; the adviser's 13G filings run 2007 to 2009 and its 13F lists the stock "
                 "2007-03 to 2008-03", ec="fund_filing", conf="high", cite=SEC("horizon-lines-inc", "edgar")))

# ---- hotel-urbano (Hurb)
hu = U("hotel-urbano", "cancela cadastro da empresa Hurb")
L.append(cls("hotel-urbano", status="defunct", rng="below_1b", stage="undetermined",
             city="Rio de Janeiro", focus="Consumer & Marketplaces", rounds=[],
             note="Hotel Urbano, renamed Hurb, online travel agency, Rio de Janeiro. Membership rests on Wikipedia's "
                  "infobox naming Tiger Global among the owners; no source read names Tiger's round (Bing, 'Hotel "
                  "Urbano' with 'Tiger Global', English and Portuguese, 2026-09-29: none), so the stage is undetermined. "
                  "Status defunct on fresher evidence than Insight's 'unknown': after two years of unpaid refunds the "
                  "Ministry of Tourism cancelled the company's registration in April 2025, barring it from operating "
                  f"in travel ({hu}), sales were suspended and staff laid off; no sale of the business is reported."))

# ---- humane
L.append(cls("humane", status="acquired", rng="below_1b",
             stage="Growth", stage_src="model", stage_conf="medium", entry_date="2021-09",
             country="US", city="San Francisco", focus="Consumer & Marketplaces",
             rounds=[rnd("2021-09-01", "Series B", 100_000_000, "Tiger Global", True, None, "press"),
                     rnd("2023-03-08", "Series C", 100_000_000, None, None,
                         U("humane", "raises another $100M"), "press")],
             note="Maker of the Ai Pin (San Francisco). Wikipedia lists Tiger Global among its investors; Tiger led "
                  "the $100M Series B of Sep 2021 (PR Newswire, 'Humane Raises $100m in Series B'; the release text was "
                  "not read, so model at medium). HP bought Humane's software platform, patents and team for $116M "
                  "in Feb 2025 and the Ai Pin was shut down: acquired (the deal was announced as an acquisition)."))

# ---- hyperscience
hs = U("hyperscience", "Series D Led by Tiger Global", "nasdaq.com")
L.append(cls("hyperscience", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=hs, stage_conf="high", entry_date="2020-10-19",
             country="US", city="New York", focus="AI & Applied AI",
             rounds=[rnd("2020-05", "Series C", 60_000_000, None, None, None, "press"),
                     rnd("2020-10-19", "Series D", 80_000_000, "Tiger Global", True, hs, "press")],
             note="Machine-learning document processing, New York. Tiger led the $80M Series D of Oct 2020, five "
                  "months after the Series C; no source read names Tiger in the Series C, so the entry is the D "
                  "(Growth either way). Below $1B as in the Battery and Felicis rows; no later priced $1B round found."))

# ---- hyphen
hy = LED("hyphen")
L.append(cls("hyphen", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=hy, stage_conf="high", entry_date="2022-02-15",
             country="US", city="San Jose", focus="Industrial & Robotics",
             rounds=[rnd("2022-02-15", "Series A", 24_000_000, "Tiger Global", True, hy, "company"),
                     rnd("2022-07-21", "strategic", None, "Chipotle (Cultivate Next)", True,
                         U("hyphen", "Chipotle Mexican Grill Makes Strategic Investment in Hyphen"), "company")],
             note="Robotic makelines for restaurant kitchens; the release is datelined San Jose. Tiger led the $24M "
                  "Series A (Feb 2022) and joined Chipotle's strategic round (Jul 2022). Y Combinator's 'Hyphen' row "
                  "(W25, medical data annotation) is a different company with the same name: not aligned."))

# ---- icon
ic = LED("icon")
L.append(cls("icon", status="private",
             rng="1b_plus", usd=2_000_000_000, val_src="web_verified", val_cite=ic, asof="2022-02-18",
             stage="Growth", stage_src="web_verified", stage_cite=ic, stage_conf="high", entry_date="2022-02-18",
             country="US", city="Austin", focus="Industrial & Robotics", flags=("stale",), extra=WV,
             rounds=[rnd("2022-02-18", "Series B", 185_000_000, "Tiger Global", True, ic, "press"),
                     rnd("2025-02-14", "Series C", 56_000_000, "Norwest and Tiger Global", True, None, "press")],
             note="3D-printed homes, Austin. Tiger led the $185M Series B of Feb 2022 (TechCrunch; its URL reads "
                  "'at a $2B valuation', the edited headline 'now approaching $2B'), no Tiger round before it. The "
                  "Feb 2025 $56M Series C (Norwest and Tiger) came with layoffs and no stated valuation; no documented "
                  "down round, so the 2022 mark stands, stale."))

# ---- indmoney and indwealth: ONE company (Finzoom Investment Advisors; INDwealth renamed INDmoney)
iw_cc = U("indwealth", "INDwealth Bags $15 Mn Funding From Tiger Global")
IND_ROUNDS = [rnd("2019-08-22", None, 15_000_000, "Tiger Global", True, LED("indwealth"), "press"),
              rnd("2020-01-27", "Series C", 12_000_000, None, None,
                  U("indwealth", "INDwealth pulls in Series C funding"), "press"),
              rnd("2022-01-17", "Series D", 86_000_000, "Tiger Global, Steadview Capital, Dragoneer", True,
                  U("indmoney", "INDmoney raises $86 mn from Tiger Global", "moneycontrol.com"), "press")]
IND_NOTE = ("Wealth and investment app of Finzoom Investment Advisors (Gurugram), launched as INDwealth and renamed "
            "INDmoney: the rows 'indwealth' and 'indmoney' are one company. Tiger's first money is the $15M round of "
            "Aug 2019, which no source read names (Mint and inc42 say only 'a funding round'); the next round was the "
            "Series C of Jan 2020, so the stage is left undetermined. Tiger co-led the $86M Series D of Jan 2022 at about "
            "$640M. Momentum check 2026-09-29 (Bing): no later round at $1B or more.")
for s in ("indmoney", "indwealth"):
    L.append(cls(s, status="private", rng="below_1b", stage="undetermined",
                 country="IN", country_src="web_verified", country_cite=iw_cc, city="Gurugram",
                 focus="Fintech & Payments", rounds=IND_ROUNDS, note=IND_NOTE))

# ---- infinite-uptime
iu = LED("infinite-uptime")
L.append(cls("infinite-uptime", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=iu, stage_conf="high", entry_date="2023-05-22",
             country="IN", country_src="web_verified", country_cite=iu, city="Pune", focus="Industrial & Robotics",
             rounds=[rnd("2023-05-22", "Series B3", 18_850_000, "Tiger Global", True, iu, "press"),
                     rnd("2025-03-10", "Series C", 35_000_000, "Avataar Ventures", None,
                         U("infinite-uptime", "Infinite Uptime bags $35M"), "press")],
             note="Industrial IoT and predictive maintenance (Pune). Tiger led the $18.85M Series B3 of May 2023, its "
                  "first round in the company per the coverage ('second investment in India in 2023'). The $35M Series "
                  "C of Mar 2025 was Avataar-led; no $1B mark."))

# ---- infra-market
im_a = U("infra-market", "Tiger Global leads Series A funding")
L.append(cls("infra-market", status="private",
             rng="1b_plus", usd=2_800_000_000, val_src="web_verified",
             val_cite=SIB("accel", "infra-market", "valuation_citation"), asof="2025-09", extra=WV, clear=CLR,
             stage="Series A", stage_src="web_verified", stage_cite=im_a, stage_conf="high", entry_date="2019-12-01",
             country="IN", country_src="web_verified",
             country_cite=U("infra-market", "Tiger Global Leads $20 Mn Series A In Infrastructure"),
             city="Thane", focus="Consumer & Marketplaces",
             rounds=[rnd("2019-12-01", "Series A", 20_000_000, "Tiger Global", True, im_a, "press"),
                     rnd("2021-02-25", "Series C", 100_000_000, "Tiger Global", True, None, "press"),
                     rnd("2021-08-03", "Series D", 125_000_000, "Tiger Global", True, LED("infra-market"), "press"),
                     rnd("2025-01-23", None, 121_000_000, None, True,
                         U("infra-market", "IPO-bound Infra.Market raises $121 million"), "press")],
             note="B2B construction-materials platform (Thane, Mumbai region). Tiger led the $20M Series A of Dec 2019 "
                  "(VCCircle, inc42), after talks reported in Aug 2019, then the $100M unicorn round (Feb 2021) and the "
                  "$125M Series D at $2.5B (Aug 2021). Mark aligned with Accel's row: about $2.8B at the flat round of "
                  "Sep 2025. Not listed: a May 2026 pre-IPO raise at about $2.6B was reported in talks and an Aug 2026 "
                  "reverse listing through Shalimar Paints is only proposed."))

# ---- innovaccer
inv = U("innovaccer", "valued at $3.2 bln")
L.append(cls("innovaccer", status="private",
             rng="1b_plus", usd=3_200_000_000, val_src="web_verified", val_cite=inv, asof="2021-12-15",
             stage="Growth", stage_src="model", stage_conf="medium", entry_date="2020-02-14",
             country="US", city="San Francisco", focus="Healthcare & Bio", flags=("stale",), clear=CLR, extra=WV,
             rounds=[rnd("2020-02-14", None, 70_000_000, None, True, None, "company"),
                     rnd("2021-02-24", "Series D", 105_000_000, "Tiger Global", True, LED("innovaccer"), "press"),
                     rnd("2021-12-15", "Series E", 150_000_000, "Mubadala", None, inv, "press"),
                     rnd("2025-01-09", "Series F", 275_000_000, None, None,
                         U("innovaccer", "Innovaccer: Healthcare AI Company Raises $275 Million"), "press")],
             note="Healthcare data and AI platform (San Francisco, engineering in Noida). Tiger's first money is the "
                  "$70M round of Feb 2020 ('Raises $70 Million From Tiger Global, Steadview Capital, Dragoneer...', PR "
                  "Newswire title; the release was not read, so model at medium), a late round (Growth); it led the "
                  "Feb 2021 unicorn round. Mark: $3.2B at the Dec 2021 Mubadala-led round (Reuters via Yahoo), fresher "
                  "than General Catalyst's $1.3B of Feb 2021; the Jan 2025 $275M Series F reported no valuation. Stale."))

# ---- innovapptive
ia = LED("innovapptive")
L.append(cls("innovapptive", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=ia, stage_conf="high", entry_date="2020-02-26",
             country="US", city="Houston", focus="SaaS",
             rounds=[rnd("2020-02-26", "Series A", 16_300_000, "Tiger Global", True, ia, "press"),
                     rnd("2023-05-09", "Series B", 50_000_000, "Vista Equity Partners", None, None, "press")],
             note="Connected-worker software for industrial frontline teams (Houston). Tiger led the $16.3M Series A "
                  "of Feb 2020, the company's first institutional round; Vista led the Series B (May 2023)."))

# ---- inphonic-inc (seeded ec=filing): listed-company 13G
L.append(verdict("inphonic-inc", "not_member",
                 "13G/13F position in a listed company, no private round naming the firm (T3, D3): InPhonic listed "
                 "on Nasdaq in Nov 2004; the 2005 13G is filed under Rule 13d-1(c) (a passive holder after listing, "
                 "not 13d-1(d) for a pre-IPO holder) with Tiger Global Performance, the public funds' GP, among the "
                 "reporting persons", ec="fund_filing", conf="high", cite=SEC("inphonic-inc", "edgar")))

if __name__ == "__main__":
    jl.write("batch-007a", L)
