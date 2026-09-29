#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 15 (11 rows): zip .. zynga-inc.
Run: NQ_TAG=b15 python3 judgments-15a.py   (add --dry to resolve citations without recording)."""
import json
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, W, NEWS

HERE = Path(__file__).resolve().parent
DRY = "--dry" in sys.argv
L = []


def BING(slug, sub, host=None):
    """The one Bing News item (bq.py cache for this judge) whose title holds `sub`, on `host`."""
    items = json.loads((HERE / "news-extra-bing-b15.json").read_text()).get(slug, [])
    urls = list(dict.fromkeys(i["url"] for i in items
                              if sub.lower() in i["title"].lower() and (host is None or host in i["url"])))
    if len(urls) != 1:
        raise SystemExit(f"BING({slug!r}, {sub!r}, {host!r}) matched {len(urls)}")
    return urls[0]


def EVSEC(slug, sub):
    """The filing URL at the end of the row's evidence-pack `sec` line containing `sub` (printed by show.py)."""
    lines = [s for s in json.loads((HERE / "evidence-pack.json").read_text())[slug].get("sec", []) if sub in s]
    if len(lines) != 1:
        raise SystemExit(f"EVSEC({slug!r}, {sub!r}) matched {len(lines)}")
    return re.search(r"(https://\S+)$", lines[0]).group(1)


def EVPRESS(slug, sub):
    """The publisher URL on the row's evidence-pack `press` line whose headline holds `sub` (printed by show.py)."""
    lines = [s for s in json.loads((HERE / "evidence-pack.json").read_text())[slug].get("press", [])
             if sub.lower() in s.lower() and "|| URL " in s]
    if len(lines) != 1:
        raise SystemExit(f"EVPRESS({slug!r}, {sub!r}) matched {len(lines)}")
    return re.search(r"\|\| URL (\S+)", lines[0]).group(1)


def SIBCITE(slug, investor):
    """A sibling book's valuation citation for the same company (siblings.json, printed by show.py)."""
    for s in json.loads((HERE / "siblings.json").read_text()).get(slug, []):
        if s["investor"] == investor and s.get("val_cite"):
            return s["val_cite"]
    raise SystemExit(f"SIBCITE({slug!r}, {investor!r}): none")


WV = {"valuation_range_source": "web_verified"}

# ---------------------------------------------------------------- zip
zip_b = NEWS("zip", "Zip lines up $43M at a $1.2B valuation")            # TechCrunch 2022-05-25, Series B
zip_c = EVPRESS("zip", "Procurement platform Zip raises $100M")        # TechCrunch 2023-05-16, Series C
zip_d = BING("zip", "AI procurement platform provider Zip raises $190M", "siliconangle")
zip_a = BING("zip", "Zip: $43 Million Series B Funding", "pulse2")
L.append(verdict("zip", "member",
                 "TechCrunch (2022-05-25): Zip's $43M Series B at a $1.2B valuation was led by YC Continuity with "
                 "Tiger Global and CRV participating; TechCrunch (2023-05-16) has Tiger Global again in the $100M "
                 "Series C. Private rounds naming the firm (T3); no vehicle named, so the home desk (D2)",
                 ec="web", conf="high", cite=zip_b))
L.append(cls("zip",
             status="private",
             rng="1b_plus", usd=2_200_000_000, val_src="web_verified", val_cite=zip_d, asof="2024-10-21",
             extra=WV,
             stage="Growth", stage_src="web_verified", stage_cite=zip_b, stage_conf="medium", entry_date="2022-05",
             country="US", country_src="web_verified", country_cite=zip_c,
             city="San Francisco", city_src="web_verified",
             flags=("model_disputes_source",),
             rounds=[rnd(None, "Series A", 25_000_000, None, None, zip_a, "press"),
                     rnd("2022-05-24", "Series B", 43_000_000, "YC Continuity", True, zip_b, "press"),
                     rnd("2023-05-15", "Series C", 100_000_000, "Y Combinator (YC Continuity)", True, zip_c, "press"),
                     rnd("2024-10-21", "Series D", 190_000_000, "BOND", None, zip_d, "press")],
             note="Zip (ZipHQ), the San Francisco procurement software company founded 2020 by Rujul Zaparde and "
                  "Lu Cheng. The prefilled status (acquired by Air Canada) and country (CA) came from a one-word "
                  "Wikidata join to Zip, Air Canada's 2002-2004 low-cost airline, a different company; this Zip is "
                  "private and operating (Zip Forward conference Sept 2026) and TechCrunch places its headquarters "
                  "in San Francisco. Entry: Tiger first appears in the May 2022 $43M Series B at $1.2B (YC "
                  "Continuity led; Tiger Global and CRV participated). The earlier $25M Series A named no investors "
                  "in any source checked (TechCrunch 2022 and 2023, Pulse 2.0, one web search, Tracxn read as a lead "
                  "only), so the entry reads Growth at medium confidence. Mark: $190M Series D at $2.2B led by BOND "
                  "(2024-10-21, SiliconANGLE), matching the YC book's $2.2B. Momentum check 2026-09-29 (Bing News): "
                  "no later priced round."))

# ---------------------------------------------------------------- zipline
zl_rt = NEWS("zipline", "Zipline soars to $7.6 billion")
zl_tc = NEWS("zipline", "Zipline charts drone delivery expansion")
zl_ext = NEWS("zipline", "Zipline snaps up another $200M")
L.append(cls("zipline",
             status="private",
             rng="1b_plus", usd=7_600_000_000, val_src="web_verified", val_cite=zl_rt, asof="2026-01-20",
             extra=WV, clear=("needs_web_value", "unicorn_name_match"),
             stage="Growth", stage_src="web_verified", stage_cite=zl_tc, stage_conf="high", entry_date="2026-01",
             country="US", city="South San Francisco",
             rounds=[rnd("2026-01-20", "funding round ($600M at $7.6B)", 600_000_000, None, True, zl_tc, "press"),
                     rnd("2026-03-23", "extension of the January round", 200_000_000, None, None, zl_ext, "press")],
             note="Zipline, the South San Francisco drone delivery company. Tiger entered in the January 2026 $600M "
                  "round at $7.6B: TechCrunch names 'several existing and new investors, including Fidelity, "
                  "Baillie Gifford, Valor Equity Partners, and Tiger Global'; no earlier Zipline round names Tiger. "
                  "Growth by any reading (the company's Series A was a decade earlier). Mark $7.6B (Reuters "
                  "2026-01-20), the same as the a16z, Felicis and Sequoia books; a $200M extension followed in "
                  "March 2026. Bloomberg reported talks in Sept 2026 to raise about $1B at about $20B: talks, not a "
                  "closed round, so not a mark. The unicorn-list flags are cleared by this cited mark."))

# ---------------------------------------------------------------- zippi
zp_ll = NEWS("zippi", "Brazilian fintech Zippi lands $16M Series A")
zp_fidc = BING("zippi", "Fintech de crédito Zippi capta R$220 mi")
L.append(cls("zippi",
             status="private",
             rng="below_1b", extra={"valuation_range_source": "web_verified", "valuation_citation": zp_fidc,
                                    "valuation_asof": "2026-02-11"},
             stage="Series A", stage_src="web_verified", stage_cite=zp_ll, stage_conf="high", entry_date="2022-06",
             country="BR", country_src="web_verified", country_cite=zp_ll,
             city="São Paulo",
             rounds=[rnd("2022-06-08", "Series A", 16_000_000, "Tiger Global", True, zp_ll, "press")],
             note="Zippi, the São Paulo fintech giving weekly credit to self-employed workers (a Y Combinator "
                  "company). Tiger led the $16M Series A in June 2022 (LatamList; Estadão lists Y Combinator, Volpe "
                  "Capital, Rainfall and others following), its first round in the company. Still operating: FIDC "
                  "credit-fund raises in Sept 2025 and Feb 2026 (R$220M, with Credit Saison entering). Momentum check "
                  "2026-09-29 (Bing News): no equity round since the Series A, none at $1B or more."))

# ---------------------------------------------------------------- zkh-group-ltd
zkh_drs = EVSEC("zkh-group-ltd", "Internet Fund IV")
zkh_e = NEWS("zkh-group-ltd", "Industrial Supply Platform ZKH Nets $315 Million")
L.append(verdict("zkh-group-ltd", "member",
                 "ZKH's IPO draft registration (2022-03-30) principal-shareholder table: 249,348,600 Series C-1 and "
                 "29,194,100 Series E preferred held by Internet Fund IV Pte. Ltd., a Singapore vehicle advised by "
                 "Tiger Global Management (a private-investment vehicle, D2/D8); Tiger partner Pengfei Wang a "
                 "director of ZKH Industrial Supply since June 2018. A private-round position, not a listed-stock "
                 "purchase (T3); the 2024 13G and 13F lines are the later public holding",
                 ec="fund_filing", conf="high", cite=zkh_drs))
L.append(cls("zkh-group-ltd",
             status="public",
             rng="below_1b", usd=439_410_000, val_src="web_verified",
             val_cite="https://stockanalysis.com/stocks/zkh/market-cap/", asof="2026-09-29", extra=WV,
             stage="Growth", stage_src="web_verified", stage_cite=zkh_drs, stage_conf="high", entry_date="2018",
             country="CN", country_src="web_verified", country_cite=zkh_drs,
             city="Shanghai", city_src="web_verified",
             rounds=[rnd("2018", "Series C-1", None, None, True, zkh_drs, "filing"),
                     rnd("2020-10", "Series E", 315_000_000, None, None, zkh_e, "press"),
                     rnd("2022-02-24", "Series E (further closing)", None, None, True, zkh_drs, "filing")],
             note="ZKH Group (震坤行), the Shanghai MRO industrial-supply procurement platform; principal executive "
                  "offices in Minhang District, Shanghai per the filing. Tiger's vehicle Internet Fund IV holds "
                  "Series C-1 (its first series; the filing's 2021-12-30 issuance dates are the offshore "
                  "restructuring's mirror shares) and bought $5M more Series E on 2022-02-24. The onshore Series C "
                  "is dated to 2018 by Tiger partner Pengfei Wang's seat on ZKH Industrial Supply's board from June "
                  "2018; no press report of that round was found (Bing and Google News, English and Chinese). "
                  "Listed on the NYSE in Dec 2023; market cap $439.41M on 2026-09-29 (stockanalysis.com)."))

# ---------------------------------------------------------------- zo-rooms
zo_a = NEWS("zo-rooms", "Online branded budget hotel aggregator Zo Rooms")
L.append(cls("zo-rooms",
             status="private",
             rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=zo_a, stage_conf="high", entry_date="2015-07",
             country="IN", country_src="web_verified", country_cite=zo_a,
             city="New Delhi", city_src="web_verified",
             rounds=[rnd("2015-07-20", "Series A", None, "Tiger Global", True, zo_a, "press")],
             note="ZO Rooms was the budget-hotel brand of Zostel Hospitality Pvt Ltd, which also runs the Zostel "
                  "hostels. VCCircle (2015-07-20): 'a fresh Series A round of funding led by Tiger Global with "
                  "participation from Orios Venture Partners' (talks in May 2015 were for $10-15M). Status: OYO "
                  "signed a term sheet in Nov 2015 to buy the ZO Rooms business for about 7% of OYO, took over its "
                  "hotels and staff, and never issued the shares; the 2021 arbitral award for Zostel was set aside by "
                  "the Delhi High Court in May 2025 and the Supreme Court dismissed Zostel's petition in July 2025 "
                  "(appeal still listed in 2026). No acquisition closed, and the company Tiger funded still operates "
                  "(Zostel hostels and Zo Houses; new property June 2026), so it reads private. City: 'the "
                  "Delhi-based company' in a 2015 profile (breathedreamgo); no newer head-office statement found."))

# ---------------------------------------------------------------- zomato
zo_ht = NEWS("zomato", "Zomato raises $103 million from Tiger Global, closes in on Swiggy")
zo_j = BING("zomato", "Zomato: $660 Million Series J Funding")
zo_w = W("Eternal Limited")
L.append(cls("zomato",
             status="public",
             rng="10b_plus", usd=31_671_605_912, val_src="web_verified",
             val_cite="https://stockanalysis.com/quote/nse/ETERNAL/market-cap/", asof="2026-09-29", extra=WV,
             stage="Growth", stage_src="web_verified", stage_cite=zo_ht, stage_conf="high", entry_date="2020-09",
             country="IN", country_src="web_verified", country_cite=zo_w,
             city="Gurugram",
             rounds=[rnd("2020-09-10", "Series J (Tiger's tranche)", 103_000_000, "Tiger Global", True, zo_ht, "press"),
                     rnd("2021-01", "Series J", 660_000_000, None, True, zo_j, "press"),
                     rnd("2021-02", "pre-IPO round", 250_000_000, None, True, zo_w, "press")],
             note="Zomato, now Eternal Ltd, the Gurugram food-delivery and quick-commerce company. Tiger's first "
                  "check was about $103M (Rs 760 crore) in Sept 2020 (HT Tech; Techcircle had reported the planned "
                  "raise in Aug 2020), part of the $660M Series J at $3.9B that closed in Jan 2021 (Pulse 2.0 names "
                  "Tiger Global); it joined the Feb 2021 $250M round at $5.4B (Wikipedia). The vehicle was Internet "
                  "Fund III Pte Ltd, a Tiger private-investment vehicle, which sold down in 2022 and exited in Aug "
                  "2023 (Mint). Listed July 2021. Market cap INR 3.04 trillion on 2026-09-29 (stockanalysis.com): "
                  "INR 3040.00B @ ECB 2026-09-29 (INR/EUR 108.991, EUR/USD 1.1355) = $31.67B. Country IN confirmed "
                  "from the company's own record (the prefill was a one-word name join)."))

# ---------------------------------------------------------------- zopper
zop_b = BING("zopper", "Reviews42 raises second round of funding")
zop_seed = BING("zopper", "Product review platform Reviews42 raises funds from Blume")
zop_a = BING("zopper", "Reviews42 raises Series A from Nirvana Ventures")
zop_2015 = NEWS("zopper", "Zopper raises $20 million funding from Tiger Global and Nirvana")
zop_c = NEWS("zopper", "Insurtech SaaS firm Zopper raises $75 million")
zop_inc = BING("zopper", "Insurtech Startup Zopper Raises $75 Mn To Help Insurers Connect")
zop_d = BING("zopper", "Zopper raises $25 million in Series D round", "thehindubusinessline")
L.append(cls("zopper",
             status="private",
             rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=zop_b, stage_conf="high", entry_date="2014-07",
             country="IN", country_src="web_verified", country_cite=zop_inc,
             city="Noida", city_src="web_verified",
             rounds=[rnd("2012-05", "Seed", None, "Blume Ventures, VentureEast", False, zop_seed, "press"),
                     rnd("2013-04", "Series A", None, "Nirvana Venture Advisors", False, zop_a, "press"),
                     rnd("2014-07", "Series B", 5_000_000, None, True, zop_b, "press"),
                     rnd("2015-06", "unnamed", 20_000_000, None, True, zop_2015, "press"),
                     rnd("2022-09-19", "Series C", 75_000_000, "Creaegis", None, zop_c, "press"),
                     rnd("2024-11-20", "Series D", 25_000_000, "Elevation Capital, Dharana Capital", None, zop_d,
                         "press")],
             note="Zopper, formerly Reviews42 (Solvy Tech Solutions), now a Noida insurtech platform. Reviews42 "
                  "raised a seed from Blume Ventures and VentureEast (2012) and a Series A led by Nirvana Venture "
                  "Advisors (2013) without Tiger; Tiger entered in the July 2014 $5M Series B with Nirvana "
                  "(ETRetail), then led a $20M round in June 2015. PhonePe bought only the Zopper Retail "
                  "point-of-sale unit in July 2018; the company continued and raised a $75M Series C (Creaegis, "
                  "2022) and a $25M Series D (Elevation, Dharana, Nov 2024); it targets an IPO around 2028-29. No "
                  "$1B mark (about $125M raised in total by 2025)."))

# ---------------------------------------------------------------- zovi
zv_b = BING("zovi", "Zovi discloses $10M in series B funding")
zv_m = BING("zovi", "Zovi & Inkfruit to merge")
zv_blr = BING("zovi", "Online retailer Zovi snaps up rival Inkfruit")
L.append(cls("zovi",
             status="defunct",
             rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=zv_b, stage_conf="high", entry_date="2012-05",
             country="IN", country_src="web_verified", country_cite=zv_blr,
             city="Bangalore", city_src="web_verified",
             rounds=[rnd("2012-05-31", "Series B", 10_000_000, None, True, zv_b, "press"),
                     rnd("2013-02", "funding with the Inkfruit merger", 10_000_000, None, True, zv_m, "press")],
             note="Zovi (Robemall Apparels), the Bangalore private-label fashion e-tailer. VCCircle (2012-05-31): a "
                  "$10M Series B 'from Tiger Global besides existing investor' SAIF Partners, so Tiger's first round "
                  "was the B. SAIF and Tiger put in $10M more when Zovi took over Inkfruit (Feb 2013). In July 2015 "
                  "the founders raised $50M from Paytm, SAIF and Tiger for a new deals app, Little (a separate "
                  "venture, not this row). The Zovi store was reported out of order and near closure in Aug 2016 "
                  "(Economic Times; YourStory) with no buyer named: defunct."))

# ---------------------------------------------------------------- zowie
zw_bi = NEWS("zowie", "US tech investing giant Tiger Global leads $14 million Series A")
zw_pr = BING("zowie", "Zowie Closes $14M Series A From Tiger Global", "prnewswire")
zw_seed = BING("zowie", "Gradient, 10xFounders back Zowie", "techcrunch.com")
L.append(cls("zowie",
             status="private",
             rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=zw_bi, stage_conf="high", entry_date="2022-05",
             country="US", city="New York", city_src="web_verified",
             rounds=[rnd("2022-01-17", "Seed", 5_000_000, "Gradient Ventures, 10xFounders", False, zw_seed, "press"),
                     rnd("2022-05-24", "Series A", 14_000_000, "Tiger Global", True, zw_pr, "press")],
             note="Zowie, the AI customer-service agent platform founded 2019 by Maja Schaefer and Matt Ciolek. "
                  "Tiger led the $14M Series A in May 2022 (Business Insider; the company's release) after a $5M "
                  "seed led by Gradient Ventures and 10xFounders in Jan 2022 without Tiger (TechCrunch). Place: the "
                  "release says it 'operates between its commercial office in New York with development offices "
                  "across Poland' (dateline New York), read as a New York head office with Polish engineering. Still "
                  "operating (listed among enterprise AI voice-agent platforms, Sept 2026). Momentum check "
                  "2026-09-29 (Bing News): no later priced round found, none at $1B or more."))

# ---------------------------------------------------------------- zuoyebang
zy_tn = NEWS("zuoyebang", "Chinese edtech giant Zuoyebang raises $750 million")
zy_2018 = BING("zuoyebang", "Chinese online tutor Zuoyebang raises $750 million in fresh round", "investing.com")
zy_scmp = NEWS("zuoyebang", "Chinese online tutor Zuoyebang raises more than US$1.6 billion from Alibaba")
zy_eq = SIBCITE("zuoyebang", "coatue")
L.append(cls("zuoyebang",
             status="private",
             rng="1b_plus", usd=9_600_000_000, val_src="web_verified", val_cite=zy_eq, asof="2020-12",
             extra=WV, clear=("needs_web_value", "unicorn_name_match"), flags=("stale",),
             stage="Growth", stage_src="web_verified", stage_cite=zy_tn, stage_conf="high", entry_date="2020-06",
             country="CN", country_src="web_verified", country_cite=zy_scmp,
             city="Beijing",
             rounds=[rnd("2018-07", "Series D", 350_000_000, None, None, zy_2018, "press"),
                     rnd("2018-11", "Series D+", 500_000_000, "SoftBank Vision Fund I", None, zy_tn, "press"),
                     rnd("2020-06-29", "Series E", 750_000_000, "FountainVest Partners and Tiger Global", True,
                         zy_tn, "press"),
                     rnd("2020-12-28", "Series E+", 1_600_000_000, None, True, zy_eq, "press")],
             note="Zuoyebang, the Beijing online tutoring company spun out of Baidu in 2015. Tiger's first round is "
                  "the June 2020 $750M Series E it co-led with FountainVest (TechNode). The model-memory lead that "
                  "Tiger co-led a 2018 round did not hold: Reuters' June 2020 investor list (Goldman Sachs, Sequoia "
                  "China, Coatue, GGV) omits Tiger, and the Coatue book records Coatue leading the July 2018 $350M "
                  "Series D. Tiger joined the Dec 2020 $1.6B Series E+ at $9.6B post-money (equalocean names Tiger), "
                  "the last priced round and the Coatue book's mark. China's July 2021 after-school tutoring rules "
                  "hit the sector, but no priced round, tender or sale since was found (Bing News 2026-09-29), so "
                  "the last primary stands, stale-flagged."))

# ---------------------------------------------------------------- zynga-inc
zy_ira = EVSEC("zynga-inc", "rights agreement")
L.append(verdict("zynga-inc", "member",
                 "Zynga's Fifth Amended and Restated Investors' Rights Agreement (dated 2011-02-18, filed as an "
                 "exhibit to the IPO S-1/A 2011-08-11) lists Tiger Global Private Investment Partners V, L.P. (a PIP "
                 "vehicle, the home desk) among the investors, with 554,362 registrable shares: a position in the "
                 "private company before the Dec 2011 IPO (T3, D6). The 2012-2013 13G filings and 2013-2014 13F "
                 "listings are the later public holding, not the entry",
                 ec="fund_filing", conf="high", cite=zy_ira))
L.append(cls("zynga-inc",
             rng="below_1b",
             stage="Growth", stage_src="model", stage_conf="medium", entry_date="2011",
             country="US", city="San Francisco",
             rounds=[rnd("2011-02-18", "Series C", 490_000_000, None, None, zy_ira, "filing")],
             note="Zynga, the San Francisco social-games company, bought by Take-Two Interactive (closed May 2022). "
                  "The rights agreement signed at the Feb 2011 Series C closing lists Tiger PIP V as a holder, but "
                  "the S-1/A names Tiger in no issuance (the $490M Series C went to five new investors and one "
                  "existing one) and records heavy secondary trading from late 2009; so Tiger entered either in the "
                  "Series C or by a secondary purchase in 2010-2011. Either reads Growth (the company had closed its "
                  "Series A to B-2 by 2010, at a $4.25B valuation in April 2010). The entry date is the agreement's "
                  "year, the earliest dated record of the position."))

if __name__ == "__main__":
    for x in L:
        for k, v in x.items():
            if isinstance(v, str) and "—" in v:
                raise SystemExit(f"em-dash in {x['slug']}.{k}")
    if DRY:
        print(json.dumps(L, ensure_ascii=False, indent=1)[:200])
        print(f"{len(L)} lines resolved")
    else:
        jl.write("batch-015a", L)
