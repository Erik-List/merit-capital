#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 8, chunk b (rows 16-30). Run: NQ_TAG=b8 python3 judgments-8b.py"""
import json
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, SEC, W, NEWS

INV = HERE.parent
URLS = json.loads(Path("/private/tmp/claude-501/-Users-erik-Developer-merit-capital/"
                       "e4102706-b045-419d-94c7-a1402905b586/scratchpad/j78-urls.json").read_text())


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


WV = {"valuation_range_source": "web_verified"}
CLR = ("needs_web_value", "unicorn_name_match")
L = []

# ---- liquidstack
lq = LED("liquidstack")
L.append(cls("liquidstack", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=lq, stage_conf="high", entry_date="2024-09-19",
             country="US", city="Carrollton", focus="Industrial & Robotics",
             rounds=[rnd("2023-03-22", "Series B", None, "Trane Technologies", False, None, "press"),
                     rnd("2024-09-19", "Series B extension", 20_000_000, "Tiger Global", True, lq, "press")],
             note="Liquid cooling for data centres (Carrollton, Texas). Trane Technologies funded the Series B in 2023; "
                  "Tiger put in the $20M Series B extension of Sep 2024, its entry. Trane completed its acquisition of "
                  f"LiquidStack in Mar 2026 ({U('liquidstack', 'Trane Technologies Completes Acquisition of LiquidStack', 'businesswire.com')}): "
                  "acquired."))

# ---- litify
lt = LED("litify")
L.append(cls("litify", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=lt, stage_conf="high", entry_date="2019-06-07",
             country="US", city="New York", focus="SaaS",
             rounds=[rnd("2019-06-07", "Series A", 50_000_000, "Tiger Global", True, lt, "company"),
                     rnd("2023-02", "majority stake", None, "Bessemer Venture Partners", None, None, "press")],
             note="Legal practice-management software (Brooklyn, New York). Tiger funded the $50M Series A of Jun 2019, "
                  "the company's first outside round. Bessemer bought a majority stake in Feb 2023; the company stays an "
                  "independent private company."))

# ---- live-nation-entertainment-inc (seeded ec=filing): listed-company 13G
L.append(verdict("live-nation-entertainment-inc", "not_member",
                 "13G/13F position in a listed company, no private round naming the firm (T3, D3): Live Nation has "
                 "been listed since its 2005 spin-off (Live Nation Entertainment since the 2010 Ticketmaster merger); "
                 "the adviser's 13G filings run 2010 to 2013", ec="fund_filing", conf="high",
                 cite=SEC("live-nation-entertainment-inc", "edgar")))

# ---- loadshare-networks
ls = LED("loadshare-networks")
L.append(cls("loadshare-networks", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=ls, stage_conf="high", entry_date="2022-02-01",
             country="IN", country_src="web_verified", country_cite=ls, city="Bangalore", focus="SaaS",
             rounds=[rnd("2022-02-01", "Series C", 40_000_000, "Tiger Global", True, ls, "press")],
             note="Tech-run logistics network for e-commerce and food delivery (Bengaluru). Tiger led the $40M Series C "
                  "of Feb 2022 (VCCircle, YourStory), its first round. No $1B mark."))

# ---- locus-robotics
le = NEWS("locus-robotics", "Locus Robotics raises $150M Series E at $1B valuation")
L.append(cls("locus-robotics", status="private",
             rng="1b_plus", usd=1_000_000_000, val_src="web_verified", val_cite=le, asof="2021-02-17", extra=WV,
             stage="Growth", stage_src="web_verified", stage_cite=le, stage_conf="high", entry_date="2021-02-17",
             country="US", city="Wilmington", focus="Industrial & Robotics", flags=("stale",), clear=CLR,
             rounds=[rnd("2021-02-17", "Series E", 150_000_000, "Tiger Global and BOND", True, le, "press"),
                     rnd("2021-09-14", "Series F", 50_000_000, "Tiger Global", True, LED("locus-robotics"), "press")],
             note="Warehouse robots (Wilmington, Massachusetts). The Robot Report: the $150M Series E of Feb 2021 'was "
                  "led by Tiger Global Management and BOND' at a $1B valuation, Tiger's entry; Tiger added $50M in Sep "
                  "2021 (FreightWaves), reported near $2B without a stated figure, so the $1B mark stands (band edge, "
                  "stale). One recall headline on this row ('Falcon Edge leads $22 million funding for Locus; Tiger "
                  "Global joins too', 2019) is about Locus.sh, an Indian logistics-software company, not this one."))

# ---- loftsmart
L.append(cls("loftsmart", status="unknown", rng="below_1b", stage="undetermined",
             country="US", city="New York", focus="Consumer & Marketplaces", rounds=[],
             note="Student-housing rental platform. Membership rests on a 2026 SEC filing's director bio: LoftSmart "
                  "'raised over $40 million from Tiger Global, Tribeca Venture Partners, and other institutional "
                  "investors'. No round naming Tiger was found (Bing, 2026-09-29, no items), so the stage is undetermined, "
                  "and no current news establishes whether it still operates: status unknown."))

# ---- loginext
lx = LED("loginext")
L.append(cls("loginext", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=lx, stage_conf="high", entry_date="2020-01-24",
             country="IN", country_src="web_verified", country_cite=lx, city="Mumbai", focus="SaaS",
             rounds=[rnd("2020-01-24", "Series B", 39_000_000, "Tiger Global and Steadview Capital", True, lx, "press")],
             note="Logistics and delivery-management software (Mumbai, with a New York office). Tiger and Steadview led "
                  "the $39M Series B of Jan 2020 at about $100M (ET Auto), Tiger's entry. No $1B mark."))

# ---- logistics-innovation-technologies-corp (seeded ec=filing): a SPAC shell
L.append(verdict("logistics-innovation-technologies-corp", "not_member",
                 "A blank-check company (a SPAC shell listed in 2021, no operating business: T5); the adviser's 13G "
                 "filings of 2021 to 2023 report listed units, not a private round (T3, D3)", ec="fund_filing",
                 conf="high", cite=SEC("logistics-innovation-technologies-corp", "edgar")))

# ---- longtop-financial-technologies-ltd (seeded ec=filing): PIP III and PIP IV in the F-1
f1 = URLS["longtop_f1"]
L.append(verdict("longtop-financial-technologies-ltd", "member",
                 "The 2007 F-1's principal-shareholder table lists Tiger Global Private Investment Partners III, L.P. "
                 "(4,028,000 convertible Series A preferred shares) and PIP IV, L.P. as pre-IPO holders, and PIP IV signs "
                 "a preferred holders' agreement of Dec 2006: private-equity vehicles in private rounds (home desk)",
                 ec="fund_filing", conf="high", cite=f1))
L.append(cls("longtop-financial-technologies-ltd", status="defunct", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=f1, stage_conf="medium", entry_date="2006",
             country="CN", country_src="web_verified", country_cite=f1, city="Xiamen", focus="SaaS",
             rounds=[rnd("2006", "Series A preferred", None, None, True, f1, "filing"),
                     rnd("2006-12-19", "Series B preferred", None, None, True,
                         json.loads((HERE / "evidence-pack.json").read_text())["longtop-financial-technologies-ltd"]["sec"][0]
                         .rsplit("| ", 1)[-1].strip(), "filing")],
             note="Banking software for Chinese banks (Xiamen). The F-1 shows PIP III holding Series A preferred and PIP "
                  "IV holding preferred under a Dec 2006 agreement, with a Tiger managing director on the board from Jun "
                  "2006: entry at the Series A (2006), medium because the issue date of the Series A is not read. Listed "
                  "on the NYSE in Oct 2007; collapsed in the 2011 accounting fraud (auditor resignation, delisting, "
                  "registration revoked, liquidation): defunct."))

# ---- lumentum: a listed-stock purchase
L.append(verdict("lumentum", "not_member",
                 "13G/13F position in a listed company, no private round naming the firm (T3, D3): the recall headline "
                 "reports a new stake in listed Lumentum stock in Q1 2026 (13F); Lumentum has been listed since its 2015 "
                 "spin-off from JDSU", ec="web", conf="high", cite=LED("lumentum")))

# ---- lummo (formerly BukuKas)
lu = U("lummo", "Sequoia co-leads US$80m funding in Indonesia", "businesstimes")
L.append(cls("lummo", status="unknown", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=lu, stage_conf="high", entry_date="2022-01-19",
             country="ID", country_src="web_verified", country_cite=U("lummo", "Lummo, formerly Bukukas, secures $80 million"),
             city="Jakarta", focus="SaaS",
             rounds=[rnd("2022-01-19", "Series C", 80_000_000, "Sequoia Capital India and Tiger Global", True, lu, "press")],
             note="Lummo, formerly BukuKas, SME software (Jakarta). Business Times: the $80M Series C of Jan 2022 was "
                  "co-led by returning investor Sequoia India and 'new investor' Tiger, Tiger's entry. After layoffs "
                  "(Jun 2022) Moneycontrol reported in Apr 2023 that it was weighing a sale or a shutdown; the outcome was "
                  "not found (Bing, 2026-09-29): status unknown."))

# ---- lybrate
ly = W("Lybrate")
L.append(cls("lybrate", status="acquired", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=ly, stage_conf="high", entry_date="2015-07",
             country="IN", country_src="web_verified", country_cite=ly, city="New Delhi", focus="Healthcare & Bio",
             rounds=[rnd("2015-07-08", "Series A", 10_200_000, "Tiger Global, Nexus and Ratan Tata", True, ly, "press")],
             note="Doctor consultation platform (New Delhi). Wikipedia: the $10.2M Series A of Jul 2015 was led by Tiger "
                  "Global, Nexus and Ratan Tata, Tiger's entry; Tiger joined a Rs 64 crore round in 2019. Pristyn Care "
                  "bought Lybrate in Jun 2022: acquired."))

# ---- lysto (the Bengaluru web3 gaming company; not Y Combinator's Lysto)
lyy = U("lysto", "Gaming platform Lysto raises $12M in Pre-Series A funding", "yourstory")
L.append(cls("lysto", status="private", rng="below_1b", stage="undetermined",
             country="IN", country_src="web_verified", country_cite=lyy, city="Bangalore", focus="Crypto & Web3",
             rounds=[rnd("2022-08-10", "pre-Series A", 12_000_000, None, True, lyy, "press")],
             note="Web3 gamer-credential and growth platform ('a Singapore and Bengaluru-based platform', YourStory). "
                  "Tiger joined the $12M pre-Series A of Aug 2022 with Square Peg, Beenext and Hashed. A pre-Series A "
                  "straddles Seed and Series A, so the stage is undetermined (as Balderton ruled on kbox-global and "
                  "Headline on robot-com). It signed an LOI with Nazara in Dec 2024. Y Combinator's 'Lysto' row (S23 "
                  "revenue intelligence) is a different company with the same name: not aligned."))

# ---- m2p-fintech
mp = LED("m2p-fintech")
L.append(cls("m2p-fintech", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=mp, stage_conf="high", entry_date="2021-10-12",
             country="IN", country_src="web_verified", country_cite=mp, city="Chennai", focus="Fintech & Payments",
             rounds=[rnd("2021-10-12", None, 35_000_000, "Tiger Global", True, mp, "press"),
                     rnd("2024-09-24", None, 102_000_000, "Helios", None, None, "press")],
             note="Card and lending infrastructure APIs (Chennai). Tiger led the $35M round of Oct 2021 at $335M (The "
                  "News Minute, Economic Times), a later round after earlier Beenext-backed rounds: Growth. Momentum "
                  "check: the Sep 2024 Helios-led $102M round was reported in talks at about $900M (Crowdfund Insider, "
                  "Jul 2024); no $1B mark."))

# ---- mail-ru
mr = LED("mail-ru")
L.append(cls("mail-ru", status="acquired", rng="below_1b", stage="undetermined",
             country="RU", country_src="web_verified", country_cite=mr, city="Moscow",
             focus="Media, Gaming & Advertising", rounds=[],
             note="Mail.ru, the Russian e-mail and portal company. Naspers' Jan 2007 filing says it bought 30% of the "
                  "private company from Digital Sky Technologies and Tiger Global, 'who remain shareholders', so Tiger "
                  "held it while private; the round Tiger entered is not named (stage undetermined). The company was "
                  "folded into Digital Sky Technologies, renamed Mail.ru Group in 2010 and VK in 2021, so the original "
                  "company reads acquired (successor-entity ambiguity, §6)."))

if __name__ == "__main__":
    jl.write("batch-008b", L)
