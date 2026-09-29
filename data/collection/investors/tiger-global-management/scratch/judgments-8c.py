#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 8, chunk c (rows 31-45). Run: NQ_TAG=b8 python3 judgments-8c.py"""
import json
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, SEC, W

INV = HERE.parent
SP = Path("/private/tmp/claude-501/-Users-erik-Developer-merit-capital/e4102706-b045-419d-94c7-a1402905b586/scratchpad")
CAPS = json.loads((SP / "j78-caps.json").read_text())
URLS = json.loads((SP / "j78-urls.json").read_text())
PACK = json.loads((HERE / "evidence-pack.json").read_text())


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


def PKSEC(slug, i=0):
    """The filing URL at the end of the row's i-th `sec` evidence line."""
    return PACK[slug]["sec"][i].rsplit("| ", 1)[-1].strip()


WV = {"valuation_range_source": "web_verified"}
CLR = ("needs_web_value", "unicorn_name_match")
L = []

# ---- makemytrip-ltd (seeded ec=filing): PIP IV and PIP V in the F-1 exhibits
mm = PKSEC("makemytrip-ltd")
cap = CAPS["makemytrip-ltd"]
L.append(verdict("makemytrip-ltd", "member",
                 "The 2010 IPO F-1 exhibits (the fourth amended shareholders agreement of Jul 2010) name Tiger Global "
                 "Private Investment Partners IV and V, together 'Tiger Fund', as pre-IPO shareholders beside SAIF, "
                 "Helion and Sierra: private-equity vehicles holding the company while private (home desk)",
                 ec="fund_filing", conf="high", cite=mm))
L.append(cls("makemytrip-ltd", status="public",
             rng="1b_plus", usd=cap["usd"], val_src="web_verified", val_cite=cap["url"], asof=cap["asof"], extra=WV,
             stage="undetermined",
             country="IN", country_src="web_verified", country_cite=mm, city="Gurugram",
             focus="Consumer & Marketplaces", rounds=[],
             note="Online travel agency (Gurugram), Nasdaq-listed since Aug 2010. Tiger held it before the IPO through "
                  "PIP IV and PIP V (the F-1 shareholders agreement); the round they entered, likely 2007 or 2008 by the "
                  "funds' vintages, is not named in what was read, so the stage is undetermined. Market cap $4.48B on "
                  "2026-09-29 (stockanalysis)."))

# ---- maktoob
mk = W("Maktoob")
L.append(cls("maktoob", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=mk, stage_conf="high", entry_date="2007-12",
             country="JO", country_src="web_verified", country_cite=mk, city="Amman",
             focus="Media, Gaming & Advertising",
             rounds=[rnd("2005-06", None, 5_000_000, "Abraaj Capital", False, mk, "press"),
                     rnd("2007-12", "secondary (Abraaj's stake)", None, None, True, mk, "press")],
             note="Arabic web portal and e-mail service founded in Amman, Jordan (the pre-filled AE reflects its later "
                  "Dubai office). Wikipedia: 'In December 2007, Abraaj sold its share to Tiger Global Management', a "
                  "purchase of an existing stake in a private company, Growth by the secondaries policy; Tiger Global PIP "
                  "Management acted for the holders when Yahoo bought Maktoob in 2009: acquired."))

# ---- mark43
m43 = LED("mark43")
L.append(cls("mark43", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=m43, stage_conf="high", entry_date="2021-07-12",
             country="US", city="New York", focus="SaaS",
             rounds=[rnd("2021-07-12", "Series E", 101_000_000, "The Spruce House Partnership and Tiger Global", True,
                         m43, "company")],
             note="Records and dispatch software for public safety (New York). Tiger co-led the $101M Series E of Jul "
                  "2021 with Spruce House; no earlier round naming Tiger was found, so the E is read as the entry "
                  "(Growth either way). Below $1B as in the General Catalyst and Spark rows."))

# ---- maxab: the Tiger money was Wasoko's
mx = U("maxab", "Two of Africa’s largest B2B e-commerce platforms, MaxAB and Wasoko", "techcrunch.com")
L.append(verdict("maxab", "not_member",
                 "The recall sentence lists Tiger Global among the investors who 'collectively invested over $240 "
                 "million in Wasoko and MaxAB before this merger'; TechCrunch (Dec 2023) places Tiger in Wasoko's "
                 "Series B, and no source ties Tiger to a MaxAB round. Tiger's route into MaxAB is the 2024 merger "
                 "(shares received for Wasoko, which is its own row), not a financing of MaxAB",
                 ec="web", conf="high", cite=mx))

# ---- mayfair
my = LED("mayfair")
L.append(cls("mayfair", status="private", rng="below_1b", stage="undetermined",
             country="US", city="San Francisco", focus="Fintech & Payments",
             rounds=[rnd(None, "pre-seed", 2_000_000, None, None, my, "press"),
                     rnd(None, "Seed", 8_000_000, None, None, my, "press")],
             note="Business cash-management fintech (San Francisco, per its Jan 2023 launch release; the pre-filled FR is "
                  "a wrong join). TechCrunch (Jan 2023): 'backed by Tiger Global', having raised a $2M pre-seed and an "
                  "$8M seed before the downturn; which of the two Tiger joined is not stated, so the stage is "
                  "undetermined. Momentum check 2026-09-29 (Bing): nothing after the Jan 2023 launch."))

# ---- medable
md = U("medable", "Medable Secures $304 Million in Funding at $2.1 Billion Valuation", "nasdaq.com")
L.append(cls("medable", status="private",
             rng="1b_plus", usd=2_100_000_000, val_src="web_verified", val_cite=md, asof="2021-10-26", extra=WV,
             stage="Growth", stage_src="web_verified", stage_cite=md, stage_conf="high", entry_date="2021-10-26",
             country="US", city="Palo Alto", focus="Healthcare & Bio", flags=("stale",),
             rounds=[rnd("2020-11-19", "Series C", 91_000_000, None, None, None, "press"),
                     rnd("2021-10-26", "Series D", 304_000_000, "Blackstone Growth, GSR Ventures and Tiger Global", True,
                         md, "company")],
             note="Decentralised clinical-trial software (Palo Alto). Tiger co-led the $304M round of Oct 2021 at $2.1B "
                  "with Blackstone Growth and GSR, its first round per the coverage (the Nov 2020 $91M round names no "
                  "Tiger). No later priced round found; stale."))

# ---- meesho
mc = URLS["meesho_cap"]
L.append(cls("meesho", status="public",
             rng="10b_plus", usd=10_730_840_161, val_src="web_verified", val_cite=mc, asof="2026-09-29", extra=WV,
             stage="Growth", stage_src="model", stage_conf="medium", entry_date="2024-05",
             country="IN", country_src="web_verified", country_cite=LED("meesho"), city="Bangalore",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2024-05-10", None, 275_000_000, None, True,
                         U("meesho", "raises $275M", "techcrunch.com"), "press")],
             note="Social e-commerce marketplace (Bengaluru), listed on NSE and BSE since Dec 2025. Tiger's first money "
                  "is the 2024 round: Moneycontrol and the Financial Express (Mar 2024) report Tiger and SoftBank "
                  "committing to it at about $3.9B, and TechCrunch reports the $275M closing in May 2024 (investor names "
                  "not read, so model at medium). Market cap INR 1,030B on 2026-09-29 (stockanalysis) @ ECB 2026-09-29 "
                  "(INR/EUR 108.991, EUR/USD 1.1355) = $10.73B, so 10b_plus: fresher than the Y Combinator row's $8.69B "
                  "listing-day mark, which should follow."))

# ---- meicai: membership open
mcy = U("meicai", "Chinese Veggie Supplier Meicai Files Confidentially", "//finance.yahoo.com")
L.append(verdict("meicai", "member",
                 "Bloomberg via Yahoo Finance (May 2021): 'Meicai, which counts Tiger Global Management, Hillhouse "
                 "Capital, GGV Capital, Genesis Capital and CMC Capital Group among its backers' (repeated in Jul 2021); "
                 "the company has never listed, so the holding came through a private round", ec="web", conf="medium",
                 cite=mcy))
L.append(cls("meicai", status="private",
             rng="1b_plus", usd=7_000_000_000, val_src="web_verified", val_cite=mcy, asof="2018", extra=WV,
             stage="undetermined",
             country="CN", country_src="web_verified", country_cite=mcy, city="Beijing",
             focus="Consumer & Marketplaces", flags=("stale",),
             rounds=[rnd("2018", None, 800_000_000, None, None, mcy, "press")],
             note="B2B fresh-food supply to restaurants (Beijing). Bloomberg names Tiger among the backers; the round Tiger "
                  "entered is not named in anything read (a 2018 lead with Hillhouse is only a model recall), so the "
                  "stage is undetermined. Mark: the 2018 raise of about $800M at a $7B post-money valuation (Bloomberg); "
                  "the 2021 US and Hong Kong IPO plans were shelved; stale, no documented down round found."))

# ---- mensa-brands
mb = LED("mensa-brands")
L.append(cls("mensa-brands", status="private", stage="undetermined",
             country="IN", country_src="web_verified", country_cite=mb, city="Bangalore",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2021-05-31", "Series A", 50_000_000, None, False, None, "press"),
                     rnd("2021-09-15", None, None, "Tiger Global", True, None, "press"),
                     rnd("2021-11", "Series B", 135_000_000, "Alpha Wave, Tiger Global and Accel", True, None, "press")],
             note="Roll-up of D2C brands (Bengaluru). Tiger was in talks in Aug 2021 (Entrackr, the seed headline) and "
                  "invested at over $250M in Sep 2021 (Entrackr), after the May 2021 $50M Series A; that Sep 2021 round "
                  "is not named, so the stage is undetermined. The Nov 2021 $135M Series B made it a unicorn at about "
                  "$1.2B, but no citable copy of that figure was found here: the valuation is left for the web pass "
                  "(needs_web_value kept)."))

# ---- meow
mw = U("meow", "Meow Closes $22 Million Series A", "businesswire.com")
L.append(cls("meow", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=mw, stage_conf="high", entry_date="2022-07-18",
             country="US", city="New York", focus="Fintech & Payments",
             rounds=[rnd("2021-11-08", "Seed", 5_000_000, "Coinbase Ventures, Gemini Frontier Fund, Lux", False,
                         U("meow", "Meow raises $5 million in seed funding"), "press"),
                     rnd("2022-07-18", "Series A", 22_000_000, "Tiger Global", True, mw, "company")],
             note="Treasury and business-banking platform founded by ex-Gemini staff (New York); it began with crypto "
                  "yields for corporate treasuries. The $5M seed (Nov 2021) had no Tiger; Tiger led the $22M Series A "
                  "of Jul 2022. Momentum check 2026-09-29 (Bing): no later round found."))

# ---- mesh-payments
mh = LED("mesh-payments")
L.append(cls("mesh-payments", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=mh, stage_conf="high", entry_date="2021-12-14",
             country="US", city="New York", focus="Fintech & Payments",
             rounds=[rnd("2021-12-14", "Series B", 50_000_000, "Tiger Global", True, mh, "company"),
                     rnd("2022-09-07", "Series C", 60_000_000, None, None, None, "press")],
             note="Corporate cards, payments and travel-expense management (release datelined New York; R&D in Israel). "
                  "Tiger led the $50M Series B of Dec 2021, its entry; a $60M Series C followed in Sep 2022. Momentum "
                  "check 2026-09-29 (Bing): SoFi became its sponsor bank in Dec 2024; no $1B round."))

# ---- metafy: membership open
mt = U("metafy", "Metafy lands $25M to scale its gaming coaching platform", "techcrunch.com")
mta = U("metafy", "Metafy just raised a $25M Series A", "technical.ly")
L.append(verdict("metafy", "member",
                 "TechCrunch (Feb 2022): 'Tiger Global and Seven Seven Six led the funding round' of $25M; "
                 "Technical.ly: 'We're officially announcing our $25m Series A led by Tiger Global and 776'",
                 ec="web", conf="high", cite=mt))
L.append(cls("metafy", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=mta, stage_conf="high", entry_date="2022-02-01",
             country="US", city="Pittsburgh", focus="Consumer & Marketplaces",
             rounds=[rnd("2021-05-06", "Seed extension", 5_500_000, None, False,
                         U("metafy", "Metafy adds $5.5M to its seed round"), "press"),
                     rnd("2022-02-01", "Series A", 25_000_000, "Tiger Global and Seven Seven Six", True, mta, "press")],
             note="Marketplace for video-game coaching (a distributed company that Technical.ly places in Pittsburgh). "
                  "The $3.15M seed and its $5.5M extension (2021) had no Tiger; Tiger co-led the $25M Series A of Feb "
                  "2022. It cut 23% of staff in Sep 2022; no later round or closure found."))

# ---- metrc
mr = LED("metrc")
L.append(cls("metrc", status="private", rng="below_1b", stage="undetermined",
             country="US", city="Lakeland", focus="SaaS",
             rounds=[rnd("2018-10-25", None, 50_000_000, "Casa Verde Capital and Tiger Global", True, mr, "press")],
             note="Cannabis seed-to-sale tracking software for state regulators (Lakeland, Florida). Tiger and Casa Verde "
                  "put $50M into the company in Oct 2018 (TechCrunch, Crunchbase News), its first outside round, which "
                  "the coverage does not name: stage undetermined. No $1B mark."))

# ---- mews
mws = LED("mews")
L.append(cls("mews", status="private",
             rng="1b_plus", usd=2_367_200_000, val_src="web_verified",
             val_cite=SIB("atomico", "mews", "valuation_citation"), asof="2026-01-26", extra=WV, clear=CLR,
             stage="Growth", stage_src="web_verified", stage_cite=mws, stage_conf="high", entry_date="2025-03-04",
             country="NL", country_src="web_verified",
             country_cite=U("mews", "Dutch hospitality scaleup Mews", "thenextweb.com"), city="Amsterdam",
             focus="SaaS",
             rounds=[rnd("2025-03-04", None, 75_000_000, "Tiger Global", True, mws, "press"),
                     rnd("2026-01-26", "Series D", 300_000_000, None, None,
                         SIB("atomico", "mews", "valuation_citation"), "press")],
             note="Hotel operations and payments software (Amsterdam head office, Prague-founded; the pre-filled IE is a "
                  "wrong join). Tiger led the $75M round of Mar 2025 (TechCrunch; Wikipedia), its entry. Mark aligned "
                  "with Atomico's row: the Jan 2026 $300M round at EUR 2B ($2.37B at the ECB rate, NL Times). Battery's "
                  "row carries London and $2.5B for the same company."))

# ---- microsoft: a listed holding; the seed headline is about PhonePe
L.append(verdict("microsoft", "not_member",
                 "13G/13F position in a listed company, no private round naming the firm (T3, D3): the recall "
                 "headline is about Tiger Global and Microsoft both exiting PhonePe, not an investment in Microsoft; "
                 "the adviser's 13F lists Microsoft stock from 2001 on, and Microsoft has been listed since 1986",
                 ec="web", conf="high", cite=LED("microsoft")))

if __name__ == "__main__":
    jl.write("batch-008c", L)
