#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 4, chunk a (ClearTax to CoinSwitch Kuber, 15 rows).
Evidence: show.py --batch 4, SEC filings (read), press pages in the caches (read), Bing/Google News under
NQ_TAG=b4, Wikipedia (insource sweep), sibling marks from siblings.json.
Run: NQ_TAG=b4 python3 judgments-4a.py"""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, W, NEWS, SEC

HERE = Path(__file__).resolve().parent
SIBS = json.loads((HERE / "siblings.json").read_text())
WV = {"valuation_range_source": "web_verified"}


def URLOF(slug, title_sub, url_sub):
    items = []
    for f in sorted(HERE.glob("news-extra*.json")):
        items += json.loads(f.read_text()).get(slug, [])
    us = list(dict.fromkeys(i["url"] for i in items if i.get("url") and title_sub.lower() in i["title"].lower()
                            and url_sub in i["url"]))
    if len(us) != 1:
        raise SystemExit(f"URLOF({slug!r}, {title_sub!r}, {url_sub!r}) matched {len(us)}")
    return us[0]


def SIB(slug, investor):
    for x in SIBS.get(slug, []):
        if x["investor"] == investor and (x.get("val_cite") or "").startswith("http"):
            return x["val_cite"]
    raise SystemExit(f"SIB({slug!r}, {investor!r}): no citation")


T3 = "13G/13F position in a listed company, no private round naming the firm (T3, D3)"
L = []

# ---------------------------------------------------------------- ClearTax (talks only)
L.append(verdict("cleartax", "not_member",
    "The recall headline reports talks ('Tiger Global to lead ClearTax round', March 2021). The round Clear closed, "
    "the $75M Series C of October 2021, was led by Kora Capital with Stripe, Alua and Think, and Entrackr reports that "
    "the talks with Tiger Global 'did not materialize'; no record ties a Tiger fund to a Clear round",
    ec="web", conf="high", cite=NEWS("cleartax", "Clear raises $75 Mn in Series C")))

# ---------------------------------------------------------------- CleverTap
CT_W = W("CleverTap")
CT_C = NEWS("clevertap", "CleverTap raises $35M in Series C round led by Tiger Global Management")
L.append(cls("clevertap", status="private", rng="below_1b", stage="Growth", stage_src="web_verified",
    stage_conf="high", stage_cite=CT_W, entry_date="2019-04", city="San Francisco", focus="SaaS",
    note="Customer engagement software company (San Francisco and Mumbai). Tiger Global first invested in the $26M "
         "Series B of April 2019 led by Sequoia India, as a new investor (Wikipedia; PR Newswire), co-led the $35M "
         "Series C of October 2019 (YourStory) and joined the $105M Series D of 2022 led by CDPQ (Wikipedia). City "
         "aligned with the Accel book.",
    rounds=[rnd("2019-04-09", "Series B", 26_000_000, "Sequoia Capital India", True, CT_W, "press"),
            rnd("2019-10-15", "Series C", 35_000_000, "Tiger Global; Sequoia Capital India", True, CT_C, "press"),
            rnd("2022-08", "Series D", 105_000_000, "CDPQ; IIFL", True, CT_W, "press")]))

# ---------------------------------------------------------------- Click Commerce (13G only)
L.append(verdict("click-commerce-inc", "not_member",
    T3 + ": Click Commerce listed on Nasdaq in June 2000, before the firm began; Tiger's 13G filings date from 2005 "
    "and 2006 (the Insight book holds the company through its own pre-IPO round)",
    ec="fund_filing", conf="high", cite=SEC("click-commerce-inc", "edgar", 0)))

# ---------------------------------------------------------------- ClickUp (article evidence)
CU_TC = NEWS("clickup", "acquires calendar startup Hypercal")
L.append(verdict("clickup", "member",
    "TechCrunch (2024-01-30): 'ClickUp last raised $400 million in Series C funding co-led by Andreessen Horowitz "
    "and Tiger Global'; TechCrunch (2023) also names Tiger among its backers",
    ec="web", conf="high", cite=CU_TC))
L.append(cls("clickup", status="private", rng="1b_plus", usd=4_000_000_000, val_src="web_verified",
    val_cite=SIB("clickup", "a16z"), asof="2021-10", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=CU_TC, entry_date="2021-10", country="US", city="San Diego", focus="SaaS", flags=("stale",),
    note="San Diego productivity software company. Andreessen Horowitz and Tiger Global co-led the $400M Series C of "
         "October 2021 at a $4B valuation (TechCrunch; Forbes), the first round naming Tiger. Mark $4B as of 2021-10, "
         "stale, as the a16z and Lightspeed books carry; no later priced round or documented collapse found.",
    rounds=[rnd("2021-10", "Series C", 400_000_000, "Andreessen Horowitz; Tiger Global", True, CU_TC, "press")],
    extra=WV))

# ---------------------------------------------------------------- clicOH
CO_A = URLOF("clicoh", "Series A Funding Led by Tiger Global", "businesswire.com")
CO_P = NEWS("clicoh", "la empresa cordobesa de logística")
L.append(cls("clicoh", status="private", rng="below_1b", stage="Series A", stage_src="web_verified",
    stage_conf="high", stage_cite=CO_A, entry_date="2022-05", country="AR", country_src="web_verified",
    country_cite=CO_P, city="Córdoba", city_src="web_verified", focus="SaaS",
    note="Argentine e-commerce logistics platform from Córdoba ('la empresa cordobesa de logística', Perfil, 2024; "
         "'startup de Córdoba', La Voz). Tiger Global led the $25M Series A of May 2022 (Business Wire). The Y "
         "Combinator book places it in Buenos Aires; this row cites Córdoba.",
    rounds=[rnd("2022-05-23", "Series A", 25_000_000, "Tiger Global", True, CO_A, "company")]))

# ---------------------------------------------------------------- Clobotics (investor identity open)
CB_K = NEWS("clobotics", "Clobotics bags USD 10 million")
L.append(verdict("clobotics", "uncertain",
    "KrASIA (from 36Kr, 2020-01-16) reports a $10M Series Pre-B+ round 'from Tiger Investment'; the article's URL says "
    "tiger-global but its headline and text name 'Tiger Investment', and no other source ties Tiger Global to "
    "Clobotics (Google News and Bing checked). Whether the investor is Tiger Global is open",
    ec="web", conf="low", cite=CB_K))
L.append(cls("clobotics", status="private", rng="below_1b", stage="undetermined", country="CN",
    country_src="web_verified", country_cite=CB_K, city="Shanghai", focus="AI & Applied AI",
    note="Shanghai and Seattle computer-vision company for wind power and retail (KrASIA). The only round tied to a "
         "'Tiger' is the $10M Series Pre-B+ of January 2020; its investor is not established as Tiger Global.",
    rounds=[rnd("2020-01", "Series Pre-B+", 10_000_000, "Tiger Investment", None, CB_K, "press")]))

# ---------------------------------------------------------------- Cloudsmith
CS_A = URLOF("cloudsmith", "Cloudsmith raises $15M Series A led by Tiger Global", "techcrunch.com")
CS_IT = NEWS("cloudsmith", "Belfast-based software company Cloudsmith raises $15m")
CS_B = NEWS("cloudsmith", "Cloudsmith raises $23M to improve software supply chain security")
CS_C = URLOF("cloudsmith", "Cloudsmith Raises $72M Series C Led by TCV", "yahoo.com")
L.append(cls("cloudsmith", status="private", rng="below_1b", stage="Series A", stage_src="web_verified",
    stage_conf="high", stage_cite=CS_A, entry_date="2021-09", country="GB", country_src="web_verified",
    country_cite=CS_IT, city="Belfast", focus="DevTools & APIs",
    note="Belfast software supply-chain (artifact management) company. Tiger Global led the $15M Series A of September "
         "2021 (TechCrunch). Momentum check: the $23M Series B of March 2025 (TCV, Insight) and the $72M Series C of "
         "April 2026 led by TCV (Business Wire) disclose no valuation; no priced round at $1B or more found.",
    rounds=[rnd("2021-09-22", "Series A", 15_000_000, "Tiger Global", True, CS_A, "press"),
            rnd("2025-03-03", "Series B", 23_000_000, "TCV; Insight Partners", None, CS_B, "press"),
            rnd("2026-04-23", "Series C", 72_000_000, "TCV", None, CS_C, "company")], extra=WV))

# ---------------------------------------------------------------- CloudTrucks
CTR = URLOF("cloudtrucks", "CloudTrucks Raises $115 Million at $850 Million Valuation", "businesswire.com")
L.append(cls("cloudtrucks", status="private", rng="below_1b", stage="Growth", stage_src="web_verified",
    stage_conf="high", stage_cite=CTR, entry_date="2021-11", country="US", city="San Francisco", focus="SaaS",
    note="San Francisco platform for independent truck drivers. Tiger Global led the $115M Series B of November 2021 "
         "at an $850M valuation (Business Wire); the Khosla book holds the earlier seed. Below $1B on that mark; "
         "layoffs followed in 2023 and no later priced round was found.",
    rounds=[rnd("2021-11-30", "Series B", 115_000_000, "Tiger Global", True, CTR, "company")]))

# ---------------------------------------------------------------- Clubhouse
CH_C = NEWS("clubhouse", "Clubhouse raises Series C funding from Andreessen Horowitz, DST Global, Tiger Global")
L.append(cls("clubhouse", status="private", rng="1b_plus", usd=4_000_000_000, val_src="web_verified",
    val_cite=SIB("clubhouse", "20vc"), asof="2021-04-18", stage="Growth", stage_src="web_verified",
    stage_conf="high", stage_cite=CH_C, entry_date="2021-04", country="US", city="San Francisco",
    focus="Consumer & Marketplaces", flags=("stale", "model_disputes_source"), clear=("needs_web_value",),
    note="Clubhouse, the San Francisco social audio app (Alpha Exploration Co.). Andreessen Horowitz led the Series C "
         "of April 2021 at $4B with DST Global and Tiger Global participating (Moneycontrol; Voicebot), the first round "
         "naming Tiger. Mark $4B as of 2021-04, stale, as the 20VC and a16z books carry. The Wikidata GB claim is a "
         "join on another company, disputed. The Greylock row 'clubhouse' is the New York project-management company "
         "(Clubhouse.io): a name collision, not aligned.",
    rounds=[rnd("2021-04-18", "Series C", None, "Andreessen Horowitz", True, CH_C, "press")], extra=WV))

# ---------------------------------------------------------------- Cobone.com (control position)
L.append(verdict("cobone-com", "not_member",
    "Tiger Global bought Cobone.com outright ('Tiger Global acquires Cobone.com', Gulf News; 'Dubai's Cobone.com "
    "bought by US investment firm', Arabian Business): a whole-company purchase, not a minority round, so a control "
    "position (T3 addendum); the site was sold on to ME Digital Group in 2014",
    ec="web", conf="high", cite=NEWS("cobone-com", "Tiger Global acquires Cobone.com"), exclusion="control_position"))

# ---------------------------------------------------------------- Codat
CD_B = URLOF("codat", "Codat raises $40M from Tiger", "finance.yahoo.com")
CD_V = NEWS("codat", "JPMorgan backs software startup Codat at US$825m valuation")
L.append(cls("codat", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=CD_B, entry_date="2021-07", country="GB", country_src="web_verified", country_cite=CD_V,
    city="London", focus="DevTools & APIs",
    note="London provider of APIs for small-business financial data. Tiger Global led the $40M round of July 2021, a "
         "year after the $10M Series A led by Index (TechCrunch), so a later-stage entry: Growth. Momentum check: the "
         "$100M round led by J.P. Morgan in June 2022 valued it at $825M (Business Times); no later priced round at "
         "$1B or more found.",
    rounds=[rnd("2020", "Series A", 10_000_000, "Index Ventures", False, CD_B, "press"),
            rnd("2021-07-01", "Series B", 40_000_000, "Tiger Global", True, CD_B, "press"),
            rnd("2022-06", "Series C", 100_000_000, "J.P. Morgan", None, CD_V, "press")], extra=WV))

# ---------------------------------------------------------------- Cohere
CO_W = W("Cohere")
CO_V = NEWS("cohere", "$500 Million Raised At $6.8 Billion Valuation")
L.append(cls("cohere", status="private", rng="1b_plus", usd=6_800_000_000, val_src="web_verified", val_cite=CO_V,
    asof="2025-08", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=CO_W, entry_date="2022-02",
    country="CA", country_src="web_verified", country_cite=CO_W, city="Toronto", focus="AI & Applied AI",
    clear=("needs_web_value",),
    note="Toronto enterprise large-language-model company. Tiger Global led the $125M Series B of February 2022 "
         "(Wikipedia; The Globe and Mail), after the Index-led Series A. Mark: the $500M round of August 2025 at $6.8B "
         "(Pulse 2.0). In September 2026 Cohere was reported in talks to raise $2B-3B at about $20B (Globe and Mail via "
         "Benzinga): talks, not a mark. The Lightspeed row 'cohere' (Santa Clara, Cohere Technologies, wireless) and "
         "the Y Combinator row 'cohere' are other companies: name collisions, not aligned.",
    rounds=[rnd("2022-02-15", "Series B", 125_000_000, "Tiger Global", True, CO_W, "press"),
            rnd("2025-08", "Unnamed", 500_000_000, None, None, CO_V, "press")], extra=WV))

# ---------------------------------------------------------------- Coinbase
CN_E = NEWS("coinbase", "Coinbase raises Series E round of financing")
L.append(cls("coinbase", status="public", rng="10b_plus", usd=50_570_000_000, val_src="web_verified",
    val_cite=SIB("coinbase", "ribbit-capital"), asof="2026-09-28", stage="Growth", stage_src="web_verified",
    stage_conf="high", stage_cite=CN_E, entry_date="2018-10", city="San Francisco", focus="Crypto & Web3",
    note="Crypto exchange, listed on Nasdaq since April 2021. Tiger Global led the $300M Series E of October 2018 at "
         "$8B (Coinbase's own post); the 2020 DRS lists Tiger Global Private Investment Partners XI with 13.5% of the "
         "Class A stock before the listing. Market cap $50.57B on 2026-09-28 (stockanalysis.com), the figure the Ribbit "
         "book carries.",
    rounds=[rnd("2018-10-30", "Series E", 300_000_000, "Tiger Global", True, CN_E, "company")], extra=WV))

# ---------------------------------------------------------------- Coinshift
CS_PR = URLOF("coinshift", "Coinshift Closes $15 Million Series A Led by Tiger Global, Sequoia Capital India, Alameda",
              "prnewswire.com/news-releases")
L.append(cls("coinshift", status="private", rng="below_1b", stage="Series A", stage_src="web_verified",
    stage_conf="high", stage_cite=CS_PR, entry_date="2022-05", country="US", focus="Crypto & Web3",
    flags=("city_unknown",),
    note="Treasury management platform for DAOs and crypto businesses. Tiger Global led the $15M Series A of May 2022 "
         "with existing investor Sequoia Capital India (PR Newswire; SiliconIndia). The release is datelined Sheridan, "
         "Wyoming, a registration address; the team appears India-based, but no source read places the head office, "
         "so the country follows the release and the city is left unknown.",
    rounds=[rnd("2022-05-17", "Series A", 15_000_000, "Tiger Global", True, CS_PR, "company")]))

# ---------------------------------------------------------------- CoinSwitch Kuber
CW_B = NEWS("coinswitch-kuber", "valued at $500 million after raising")
CW_C = NEWS("coinswitch-kuber", "raises $260 million, valued at $1.9 billion")
L.append(cls("coinswitch-kuber", status="private", rng="1b_plus", usd=1_910_000_000, val_src="web_verified",
    val_cite=CW_C, asof="2021-10", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=CW_B,
    entry_date="2021-04", country="IN", country_src="web_verified", country_cite=CW_B, city="Bangalore",
    focus="Crypto & Web3", flags=("stale",), clear=("needs_web_value",),
    note="Bangalore crypto exchange. Tiger Global led the $25M round of April 2021 at $500M (The Economic Times), its "
         "Series B after the 2020 Series A that did not include Tiger, and joined the $260M Series C of October 2021 "
         "at $1.9B led by Coinbase Ventures and a16z (Times of India). Mark $1.9B as of 2021-10, stale; no later "
         "priced round or documented collapse found.",
    rounds=[rnd("2021-04-22", "Series B", 25_000_000, "Tiger Global", True, CW_B, "press"),
            rnd("2021-10", "Series C", 260_000_000, "Coinbase Ventures; Andreessen Horowitz", True, CW_C, "press")],
    extra=WV))

if __name__ == "__main__":
    jl.write("batch-004a", L)
