#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 4, chunk b (Coleman Cleat to Ctrip, 15 rows).
Evidence: show.py --batch 4, SEC filings (read; Ctrip's 2003 F-1 found through EDGAR full-text search for the firm's
old name 'Tiger Technology'), press pages in the caches (read), Bing/Google News under NQ_TAG=b4, Wikipedia,
sibling marks from siblings.json, stockanalysis.com (WebSearch). Run: NQ_TAG=b4 python3 judgments-4b.py"""
import hashlib
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, W, NEWS, SEC

HERE = Path(__file__).resolve().parent
PK = json.loads((HERE / "evidence-pack.json").read_text())
SIBS = json.loads((HERE / "siblings.json").read_text())
WV = {"valuation_range_source": "web_verified"}
SCR = Path("/private/tmp/claude-501/-Users-erik-Developer-merit-capital/e4102706-b045-419d-94c7-a1402905b586/scratchpad")


def PACK(slug, kind="sec", i=0):
    line = (PK.get(slug) or {}).get(kind, [])[i]
    u = line.rsplit("| ", 1)[-1].strip()
    if not u.startswith("https://"):
        raise SystemExit(f"PACK({slug!r}, {kind!r}, {i}): no URL on the line")
    return u


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


def READ(url, phrase):
    """A filing URL this judge fetched and read: the cached copy must hold the phrase it is cited for."""
    h = hashlib.md5(url.encode()).hexdigest()
    for d in (SCR / "sec-cache", SCR / "j34" / "sec-cache"):
        f = d / h
        if f.exists() and phrase in f.read_text(errors="replace"):
            return url
    raise SystemExit(f"READ({url!r}): not read, or the phrase is missing")


T3 = "13G/13F position in a listed company, no private round naming the firm (T3, D3)"
L = []

# ---------------------------------------------------------------- Coleman Cleat (homonym)
L.append(verdict("coleman-cleat-llc", "not_member",
    "Chuck Coleman is the executive officer of Coleman Cleat, LLC, a Kent, Washington issuer that sold $108,000 in "
    "2009: a homonym of Charles P. Coleman III, and no Tiger vehicle or round names the company",
    ec="formd_adjudicated", conf="high", cite=SEC("coleman-cleat-llc")))

# ---------------------------------------------------------------- Colony Labs
CL_M = NEWS("colony-labs", "Colony Labs, Inc. announced that it has received")
L.append(cls("colony-labs", status="private", rng="below_1b", stage="undetermined", country="US",
    flags=("city_unknown",),
    note="Colony Labs, Inc. received $75M in November 2025 from StepStone, Amplify Partners, Redpoint, Tiger Global "
         "Management, Morado, New York Life Ventures and others (MarketScreener). The round's name, the company's "
         "business and its city could not be established (the page is blocked; Bing and Google News return only this "
         "item and an unrelated 2022 Avalanche token project of the same name), so the stage is undetermined and the "
         "city unknown. No priced round at $1B or more found.",
    rounds=[rnd("2025-11-10", "Unnamed", 75_000_000, None, True, CL_M, "press")]))

# ---------------------------------------------------------------- CommonFloor
CF_C = URLOF("commonfloor", "secures $7.5M in Series C from Tiger Global", "vccircle.com")
CF_4 = NEWS("commonfloor", "Commonfloor Raises Rs.64 Cr in 4th Round")
CF_E = URLOF("commonfloor", "raises $30M in Series E round from existing investor Tiger Global", "vccircle.com")
L.append(cls("commonfloor", status="acquired", rng="below_1b", stage="undetermined", country="IN",
    country_src="web_verified", country_cite=CF_C, city="Bangalore", focus="Consumer & Marketplaces",
    note="Bangalore real estate portal (maxHeap Technologies). Tiger Global was already an existing investor, beside "
         "Accel, when both put in the $7.5M Series C of July 2013 (VCCircle), so the firm entered in an earlier round "
         "the record does not name: stage undetermined. Tiger led later rounds (Rs 64 crore in January 2014; the $30M "
         "Series E of September 2014). Quikr bought CommonFloor in 2016: acquired.",
    rounds=[rnd("2013-07-05", "Series C", 7_500_000, None, True, CF_C, "press"),
            rnd("2014-01", "Unnamed (4th round)", 10_000_000, "Tiger Global; Accel", True, CF_4, "press"),
            rnd("2014-09", "Series E", 30_000_000, "Tiger Global", True, CF_E, "press")]))

# ---------------------------------------------------------------- Confluent
CF_IRA = PACK("confluent")
L.append(cls("confluent", status="acquired", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium",
    stage_cite=CF_IRA, entry_date="2020-03", country="US", city="Mountain View", focus="Data Infrastructure",
    note="Mountain View data-streaming company, listed on Nasdaq in June 2021 and bought by IBM, which completed the "
         "acquisition on 2026-03-17 (IBM's release, cited by the Benchmark and Sequoia books): acquired. Tiger Global "
         "PIP XII-6 LLC is listed among the investors in the rights agreement of 2020-03-20 that accompanied the "
         "Series E, so Tiger held preferred stock by then; whether it bought Series E shares or earlier shares on the "
         "secondary market is not stated, and both read Growth (model, medium).",
    rounds=[rnd("2020-03-20", "Series E", None, None, True, CF_IRA, "filing")]))

# ---------------------------------------------------------------- Connecteam (article evidence)
CN_J = NEWS("connecteam", "Worker management tool Connecteam closes Series C")
L.append(verdict("connecteam", "member",
    "The Jerusalem Post (2022-03-06): Connecteam raised $120M in a Series C 'led by ... Stripes, and ... Insight "
    "Partners, with participation from Tiger Global, Qumra Capital, and Eyal Ofer's O.G.'",
    ec="web", conf="high", cite=CN_J))
L.append(cls("connecteam", status="private", rng="below_1b", stage="Growth", stage_src="web_verified",
    stage_conf="high", stage_cite=CN_J, entry_date="2022-03", country="IL", country_src="web_verified",
    country_cite=CN_J, city="Tel Aviv", focus="SaaS",
    note="Israeli software for managing deskless workers. Tiger Global joined the $120M Series C of March 2022 led by "
         "Stripes and Insight Partners (The Jerusalem Post), at a valuation reported above $800M (TechCrunch); no "
         "earlier round names the firm. City aligned with the Insight book.",
    rounds=[rnd("2022-03", "Series C", 120_000_000, "Stripes; Insight Partners", True, CN_J, "press")]))

# ---------------------------------------------------------------- Contentful
CT_W = W("Contentful")
CT_S = NEWS("contentful", "Salesforce Acquires Contentful to Power Agentforce Content")
L.append(cls("contentful", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified",
    stage_conf="high", stage_cite=CT_W, entry_date="2021-07", country="DE", country_src="web_verified",
    country_cite=CT_W, city="Berlin", focus="DevTools & APIs", clear=("needs_web_value",),
    note="Berlin headless content platform. Tiger Global's private-equity arm led the $175M Series F of July 2021 at "
         "$3B (Wikipedia), the first round naming the firm. Salesforce signed a definitive agreement to buy Contentful "
         "on 2026-06-01 (Web CMS) and the purchase completed in September 2026 (Dealroom's deal record): acquired, as "
         "the Balderton, Benchmark, General Catalyst and Point Nine books read. The Wikidata DE claim is confirmed.",
    rounds=[rnd("2021-07-28", "Series F", 175_000_000, "Tiger Global", True, CT_W, "press"),
            rnd("2026-06-01", "Acquisition (Salesforce)", None, "Salesforce", False, CT_S, "press")]))

# ---------------------------------------------------------------- Cora (Brazil)
CR_B = NEWS("cora", "Brazilian fintech Cora raises $116M Series B")
L.append(cls("cora", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=CR_B, entry_date="2021-08", country="BR", country_src="web_verified", country_cite=CR_B,
    city="São Paulo", focus="Fintech & Payments", flags=("model_disputes_source",),
    note="São Paulo digital bank for small businesses (TechCrunch). Greenoaks led the $116M Series B of August 2021 "
         "with Tiger Global and Tencent joining as new investors; the $26.7M Series A of April 2021 was led by Ribbit "
         "(TechCrunch). The Wikidata Canada claim is a join on another company, disputed. The Y Combinator row 'cora' "
         "is another company: a name collision, not aligned.",
    rounds=[rnd("2021-04", "Series A", 26_700_000, "Ribbit Capital", False, CR_B, "press"),
            rnd("2021-08-24", "Series B", 116_000_000, "Greenoaks Capital", True, CR_B, "press")]))

# ---------------------------------------------------------------- Coupang (13F position)
L.append(verdict("coupang", "not_member",
    T3 + ": the recall item is a hedge-fund news roundup; Tiger's 13F lists Coupang from the quarter of its March 2021 "
    "NYSE listing (2021-03-31), and no prospectus, holder table or private round names a Tiger vehicle",
    ec="web", conf="medium", cite=NEWS("coupang", "Hedge Fund and Insider Trading News")))

# ---------------------------------------------------------------- Craftsy
L.append(cls("craftsy", status="acquired", rng="below_1b", stage="undetermined", country="US", city="Denver",
    focus="Consumer & Marketplaces",
    note="Denver online craft-class company (Sympoz Inc., founded April 2010). Wikipedia says it raised $15M from "
         "Access Venture Partners, Foundry Group, Harrison Metal and Tiger Global Management before and around its "
         "2011 launch, calling it an angel round; the round's label and the firm's part in it cannot be established, so "
         "the stage is undetermined. NBCUniversal bought Craftsy in 2017 for about $230M (Vox): acquired.",
    rounds=[rnd("2010", "Unnamed", 15_000_000, None, True, W("Craftsy"), "press")]))

# ---------------------------------------------------------------- CRED
CD_B = NEWS("cred", "9-month-old CRED raises $120M")
L.append(cls("cred", status="private", rng="1b_plus", usd=4_500_000_000, val_src="web_verified",
    val_cite=SIB("cred", "coatue"), asof="2026-06", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=CD_B, entry_date="2019-08", country="IN", country_src="web_verified", country_cite=CD_B,
    city="Bangalore", focus="Fintech & Payments", clear=("needs_web_value",),
    note="Bangalore credit-card rewards and payments company. Tiger Global joined the $120M Series B of August 2019 led "
         "by Sequoia, Ribbit and DST's Gemini (TechCrunch, from a regulatory filing), and took part in the Series C "
         "($806M post), the Series E it co-led ($4.01B) and the Series F ($6.4B) (Wikipedia). Mark: Meta's $900M for a "
         "20% stake in June 2026, $4.5B, the figure the Coatue and General Catalyst books carry (after a 2025 round at "
         "$3.5B). The Wikidata IN claim is confirmed.",
    rounds=[rnd("2019-08-26", "Series B", 120_000_000, "Sequoia Capital; Ribbit Capital; Gemini Investments", True,
                CD_B, "press"),
            rnd("2021-01", "Series C", 81_000_000, "DST Global", True,
                NEWS("cred", "India-Based Fintech CRED Secures $81 Million"), "press"),
            rnd("2026-06-22", "Series H", 900_000_000, "Meta Platforms", False, SIB("cred", "coatue"), "press")],
    extra=WV))

# ---------------------------------------------------------------- Credit Karma
CK_W = W("Credit Karma")
L.append(cls("credit-karma", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified",
    stage_conf="high", stage_cite=CK_W, entry_date="2014-03", city="Oakland", focus="Fintech & Payments",
    note="Consumer credit and finance platform, bought by Intuit in December 2020: acquired. Tiger Global contributed to "
         "the $85M Series C of March 2014 led by CapitalG, alongside existing investors, and to the $75M follow-on of "
         "September 2014 (Wikipedia); Intuit's S-4 shows Tiger PIP VII and IX with 11.9% and a Tiger management rights "
         "agreement effective 2014-02-14. Headquarters Oakland since its 2020 move (the Ribbit book; the Felicis book "
         "still reads San Francisco).",
    rounds=[rnd("2014-03", "Series C", 85_000_000, "CapitalG", True, CK_W, "press"),
            rnd("2014-09", "Unnamed", 75_000_000, "CapitalG", True, CK_W, "press")]))

# ---------------------------------------------------------------- CreditBook (Pakistan)
CB_T = URLOF("creditbook", "Tiger Global backs fintech CreditBook in first Pakistan investment", "techcrunch.com")
L.append(cls("creditbook", status="private", rng="below_1b", stage="Seed", stage_src="web_verified",
    stage_conf="medium", stage_cite=CB_T, entry_date="2021-12", country="PK", country_src="web_verified",
    country_cite=CB_T, city="Karachi", focus="Fintech & Payments",
    note="Pakistani bookkeeping and payments app for merchants, Karachi. Tiger Global backed the $11M pre-Series A "
         "round of December 2021, its first Pakistan investment, with Better Tomorrow, Firstminute and others "
         "(TechCrunch); a pre-Series A round reads Seed. Graduation left for the graduation pass.",
    rounds=[rnd("2021-12-16", "Pre-Series A", 11_000_000, "Tiger Global", True, CB_T, "press")]))

# ---------------------------------------------------------------- Cribl
CR_W = W("Cribl.io")
L.append(cls("cribl", status="private", rng="1b_plus", usd=3_500_000_000, val_src="web_verified",
    val_cite=SIB("cribl", "ivp"), asof="2024-08-27", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=CR_W, entry_date="2022", country="US", city="San Francisco", focus="Data Infrastructure",
    flags=("stale",), clear=("needs_web_value",),
    note="San Francisco data-pipeline company. Tiger Global led the $150M Series D of 2022, joined by existing "
         "investors IVP, CRV, Redpoint, Sequoia and Greylock (Wikipedia). Mark: the $319M Series E of August 2024 at "
         "$3.5B led by GV (Cribl's release; TechCrunch), just over 24 months old, stale. Momentum check: no later "
         "priced round found (Bing, 2026-09-29).",
    rounds=[rnd("2022", "Series D", 150_000_000, "Tiger Global", True, CR_W, "press"),
            rnd("2024-08-27", "Series E", 319_000_000, "GV", None, SIB("cribl", "ivp"), "company")], extra=WV))

# ---------------------------------------------------------------- CrowdStrike (13F position)
L.append(verdict("crowdstrike", "not_member",
    T3 + ": the recall headline reports Tiger's 13F sales of CrowdStrike stock; CrowdStrike listed on Nasdaq in June "
    "2019 and no prospectus or private round names a Tiger vehicle",
    ec="web", conf="high", cite=URLOF("crowdstrike", "Dumped 44%", "fool.com")))

# ---------------------------------------------------------------- Ctrip / Trip.com (pre-IPO Series C, 2003)
CTRIP_F1 = READ("https://www.sec.gov/Archives/edgar/data/1269238/000114554903001453/u98691fv1.htm",
                "Tiger Technology Private Investment Partners")
TCOM_CAP = "https://stockanalysis.com/stocks/tcom/market-cap/"   # printed by WebSearch, read 2026-09-29
L.append(verdict("ctrip-com-international-ltd", "member",
    "Ctrip's 2003 F-1 records that Tiger Technology Private Investment Partners, L.P. (the firm's first private-equity "
    "fund) and Tiger Technology II, L.P. bought 2,180,755 Series C preferred shares in a private placement on "
    "2003-09-04 at $4.5856 (about $10M, 8.1% before the December 2003 IPO); the 13G of January 2004 lists the same "
    "PIP vehicle. A private round naming a PIP vehicle, so the 13G is not the entry",
    ec="fund_filing", conf="high", cite=CTRIP_F1))
L.append(cls("ctrip-com-international-ltd", status="public", rng="10b_plus", usd=24_230_000_000,
    val_src="web_verified", val_cite=TCOM_CAP, asof="2026-09-29", stage="Growth", stage_src="web_verified",
    stage_conf="high", stage_cite=CTRIP_F1, entry_date="2003-09-04", country="CN", country_src="web_verified",
    country_cite=CTRIP_F1, city="Shanghai", focus="Consumer & Marketplaces", flags=("model_disputes_source",),
    note="Ctrip.com International, now Trip.com Group, the Shanghai online travel company, listed on Nasdaq since "
         "December 2003 (TCOM) and in Hong Kong since 2021. Tiger's PIP I entered in the Series C of September 2003 "
         "(F-1). The prefill read acquired from a stale float record, disputed: the company is listed. Market cap "
         "$24.23B on 2026-09-29 (stockanalysis.com).",
    rounds=[rnd("2003-09-04", "Series C", 10_000_000, "Tiger Technology Private Investment Partners", True, CTRIP_F1,
                "filing")], extra=WV))

if __name__ == "__main__":
    jl.write("batch-004b", L)
