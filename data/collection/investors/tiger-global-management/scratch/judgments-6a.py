#!/usr/bin/env python3
"""PRO-167 grind, queue batch 6, chunk a (rows 1-15). Judge b6.

Evidence: the judge view (show.py --batch 5), the evidence pack, the Bing and Google candidate caches, Bing
lookups run with NQ_TAG=b6 (bq.py), sibling books' records, and pages fetched and read in this pass (the
literal URLs below). Every citation is read from disk by a helper or is a page fetched and read here."""
import json
import os
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, W, NEWS, SEC

HERE = Path(__file__).resolve().parent
PKD = json.loads((HERE / "evidence-pack.json").read_text())
BND = json.loads((HERE / "bing-news.json").read_text())
WV = {"valuation_range_source": "web_verified"}


def PK(slug, sub, kind="press"):
    """A URL from the row's evidence-pack lines (press '|| URL', sec line tail, wiki or recall parentheses)."""
    p = PKD.get(slug, {})
    if kind == "recall":
        m = re.findall(r"\((https?://[^)\s]+)\)", p.get("recall_basis") or "")
        if not m:
            raise SystemExit(f"PK recall {slug}")
        return m[-1]
    urls = []
    for x in p.get(kind) or []:
        if sub.lower() not in x.lower():
            continue
        if kind == "press":
            m = re.search(r"\|\| URL (\S+)", x)
        elif kind == "sec":
            m = re.search(r"\| (https?://\S+)\s*$", x)
        else:
            m = re.search(r"\((https?://[^)\s]+)\)", x)
        if m:
            urls.append(m.group(1))
    urls = list(dict.fromkeys(urls))
    if len(urls) != 1:
        raise SystemExit(f"PK({slug!r}, {sub!r}, {kind}) -> {urls}")
    return urls[0]


def BN(key, sub):
    """A publisher URL from the Bing candidate cache (bing-news.json[key]) whose title contains sub."""
    urls = list(dict.fromkeys(i["url"] for i in (BND.get(key) or {}).get("items", [])
                              if sub.lower() in i["title"].lower()))
    if len(urls) != 1:
        raise SystemExit(f"BN({key!r}, {sub!r}) -> {urls}")
    return urls[0]


def SIB(slug, inv):
    """(usd, asof, citation) of a sibling book's mark for the same company, from the evidence pack."""
    for x in PKD.get(slug, {}).get("sib", []):
        if x["investor"] == inv and x.get("val_cite"):
            return int(float(x["usd"])), x["asof"], x["val_cite"]
    raise SystemExit(f"SIB({slug!r}, {inv!r}) missing")
def SIBREC(inv, slug, key):
    """A key of a sibling book's own classification record (data/collection/investors/<inv>), read from disk."""
    d = HERE.parents[1] / inv / "companies"
    rec = {**json.loads((d / "resolved.json").read_text()).get(slug, {}),
           **json.loads((d / "classification.json").read_text()).get(slug, {})}
    if not rec.get(key):
        raise SystemExit(f"SIBREC({inv!r}, {slug!r}, {key!r}) missing")
    return rec[key]


T3 = "13G/13F position in a listed company, no private round naming the firm (T3, D3)"
L = []
CHECK = "2026-09-29"

# ---------------------------------------------------------------- frubana (membership open)
FB_ES = PK("frubana", "Estadao")
FB_END = PK("frubana", "Portafolio | ¿El fin de Frubana")
FB_CO = PK("frubana", "", "recall")
L.append(verdict("frubana", "member",
                 "Estadao (2021-06-02) on the $65M Series B: 'O aporte teve ainda participações de Tiger Global "
                 "Managament, Softbank, Monashees e Lightspeed Venture Partners'; Portafolio calls Tiger a previous "
                 "investor at that round, so the firm held the company through private rounds",
                 ec="web", conf="high", cite=FB_ES))
L.append(cls("frubana", status="defunct", rng="below_1b", stage="undetermined",
             country="CO", country_src="web_verified", country_cite=FB_CO, city="Bogotá",
             focus="Consumer & Marketplaces",
             note="B2B food supply marketplace for restaurants, founded in Bogotá (2018, Y Combinator 2019), later in "
                  "Mexico and Brazil. Tiger took part in the $65M Series B of June 2021 as an existing investor "
                  "(Estadao; Portafolio, Semana name Lightspeed as the new one); the round Tiger first entered, "
                  "between the 2019 seed and the $25M Series A of April 2020 led by GGV and Monashees, is not on "
                  "record, so the stage is undetermined. Frubana closed Brazil, its last market, in August 2025 "
                  "(Portafolio, 2025-08-14): defunct (the Lightspeed row still reads private).",
             rounds=[rnd("2021-06-02", "Series B", 65_000_000, "GGV Capital", True, FB_ES, "press")]))

# ---------------------------------------------------------------- ftx (recall seed confirmed)
FT_B = PK("ftx", "", "recall")
L.append(cls("ftx", status="defunct", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=FT_B, stage_conf="medium", entry_date="2021-10-21",
             country="BS", country_src="web_verified", country_cite=W("FTX"), city="Nassau", focus="Crypto & Web3",
             note="FTX Trading, the crypto exchange, Nassau. Tiger is named among the 69 investors of the $420.69M "
                  "round of October 2021 at $25B (The Block), the first round tying the firm to FTX (not named in "
                  "the July 2021 Series B release), and joined the January 2022 Series C at $32B: Growth. Chapter 11 "
                  "from November 2022: defunct under the bankruptcy ruling, aligned with the IVP, Lightspeed, Ribbit "
                  "and Sequoia rows.",
             rounds=[rnd("2021-10-21", "Series B-1", 420_690_000, None, True, FT_B, "press")]))

# ---------------------------------------------------------------- fyle (recall seed confirmed)
FY_A = PK("fyle", "VCCircle | Tiger Global leads Series A funding in expense manager")
FY_M = PK("fyle", "Mint | Fyle raises $4.2 million")
L.append(cls("fyle", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=FY_A, stage_conf="high", entry_date="2019-02-11",
             country="IN", country_src="web_verified", country_cite=FY_M, city="Bangalore", focus="SaaS",
             note="Expense management software, Bengaluru. Tiger led the Series A of February-March 2019 ($4.2M; "
                  "VCCircle, Mint), after a $1.1M seed in April 2018 without Tiger: the firm's entry. Steadview led "
                  "a $4.5M round in October 2019.",
             rounds=[rnd("2019-03-29", "Series A", 4_200_000, "Tiger Global Management", True, FY_M, "press")]))

# ---------------------------------------------------------------- gaana (recall seed replaced)
L.append(verdict("gaana", "not_member",
                 "The recall headline (VCCircle, 2022-01-24) calls Classplus Tiger Global-backed and names Gaana only "
                 "as its new finance executive's former employer; Gaana was funded by Times Internet and Tencent, and "
                 "no record ties Tiger Global to a round of Gaana", ec="web", conf="high", cite=PK("gaana", "", "recall")))

# ---------------------------------------------------------------- games24x7 (recall seed confirmed)
G24_VC = PK("games24x7", "VCCircle | Play Games24x7 discloses investment")
G24_75 = PK("games24x7", "Mint | Games24x7 valued at $2.5 billion")
G24_BAN = NEWS("games24x7", "Games24x7 begins layoffs following govt ban")
L.append(cls("games24x7", status="private", rng="below_1b",
             extra={"valuation_range_source": "web_verified", "valuation_citation": G24_BAN},
             stage="undetermined",
             country="IN", country_src="web_verified", country_cite=W("Games24x7"), city="Mumbai",
             focus="Media, Gaming & Advertising",
             note="Online skill gaming (RummyCircle, My11Circle), Mumbai. Tiger was the company's first institutional "
                  "investor in 2011 (Wikipedia; VCCircle 2012 on the disclosed Tiger investment); no source names the "
                  "round, so the stage is undetermined. Tiger joined the $75M round at $2.5B led by Malabar in March "
                  "2022 (Mint). Collapse evidence: India's August 2025 ban on real-money games ended its core business "
                  "and layoffs followed (Moneycontrol, 2025-09-01); the stale 2022 mark no longer stands, so below $1B "
                  "with no figure (agent reading, listed for review).",
             rounds=[rnd("2011", "first institutional investment (unnamed)", None, "Tiger Global", True, G24_VC, "press"),
                     rnd("2022-03-30", "unnamed ($75M at $2.5B)", 75_000_000, "Malabar Investments", True, G24_75,
                         "press")]))

# ---------------------------------------------------------------- ganji-com (recall seed confirmed)
GJ_SEC = PK("ganji-com", "Tiger Global Mauritius Fund", "sec")
GJ_R = NEWS("ganji-com", "58.com to buy 43 percent of rival Ganji")
L.append(cls("ganji-com", status="acquired", rng="below_1b", stage="undetermined",
             country="CN", country_src="web_verified", country_cite=GJ_R, city="Beijing",
             focus="Consumer & Marketplaces",
             note="Ganji.com, online classifieds, Beijing. Tiger Global Mauritius Fund and Internet Fund II sign the "
                  "registration rights agreement as selling Ganji holders when 58.com bought into Ganji in April 2015 "
                  "for cash and 58.com shares (58.com's 20-F exhibit; Reuters, 2015-04-17); the two were combined "
                  "under 58.com, so acquired. The round in which Tiger entered is not on record, so the stage is "
                  "undetermined.",
             rounds=[rnd("2015-04-17", "sale of Ganji shares to 58.com", None, None, True, GJ_SEC, "filing")]))

# ---------------------------------------------------------------- genesis-therapeutics-inc (Form D homonym)
L.append(verdict("genesis-therapeutics-inc", "not_member",
                 "Evan Feinberg on these Form Ds (2020-2023, Burlingame) is Genesis Therapeutics' founder and chief "
                 "executive, listed as executive officer: a homonym of Tiger's Evan Feinberg (D7); no Tiger record "
                 "names the company", ec="formd_adjudicated", conf="high", cite=SEC("genesis-therapeutics-inc")))

# ---------------------------------------------------------------- geniemode (recall seed confirmed)
GM_B = PK("geniemode", "", "recall")
GM_C = NEWS("geniemode", "B2B sourcing platform Geniemode raises over $50 million led by Multiples Alternate")
L.append(cls("geniemode", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=GM_B, stage_conf="high", entry_date="2022-04-28",
             country="IN", country_src="web_verified", country_cite=GM_B, city="Gurugram",
             focus="Consumer & Marketplaces",
             note="B2B fashion and lifestyle sourcing platform, Gurugram. Tiger led the $28M Series B of April 2022 "
                  "at over $160M (Business Line; Entrackr), its first round in the company: Growth. Multiples led a "
                  "Series C of over $50M in February 2025.",
             rounds=[rnd("2022-04-28", "Series B", 28_000_000, "Tiger Global", True, GM_B, "press"),
                     rnd("2025-02-24", "Series C", 50_000_000, "Multiples Alternate", None, GM_C, "press")]))

# ---------------------------------------------------------------- getir (recall seed confirmed)
GT_BI = PK("getir", "", "recall")
GT_UB = NEWS("getir", "Turkey clears Uber")
GT_12 = PK("getir", "retail.economictimes.i | Fast delivery startup Getir closes funding round")
L.append(cls("getir", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=GT_BI, stage_conf="medium", entry_date="2021-01",
             city="Istanbul", focus="Consumer & Marketplaces",
             note="Rapid grocery and food delivery, Istanbul. Tiger backed the $128M round of January 2021 (Business "
                  "Insider headline) and the $300M round at $2.6B of March 2021 (Business Insider), the company's "
                  "third and fourth rounds: Growth. Peak mark $11.8B (March 2022). After a 2024 restructuring under "
                  "Mubadala's control, Uber agreed in February 2026 to buy Getir's delivery business in Turkey for "
                  "about $335M, cleared by the Turkish Competition Board in June 2026: the core business was sold, "
                  "so acquired (the Sequoia row still reads private, below $1B).",
             rounds=[rnd("2021-01-21", "unnamed ($128M)", 128_000_000, None, True, None, "press"),
                     rnd("2021-03-22", "Series C ($300M at $2.6B)", 300_000_000, None, True, GT_BI, "press"),
                     rnd("2022-03-18", "Series E ($768M at $11.8B)", 768_000_000, "Mubadala", None, GT_12, "press")]))

# ---------------------------------------------------------------- getjar (recall seed confirmed)
GJ_BW = PK("getjar", "Business Wire | GetJar Secures $25 Million in Series C")
GJ_WSJ = NEWS("getjar", "China's Sungy Buys App Store GetJar")
L.append(cls("getjar", status="acquired", rng="below_1b", flags=["model_disputes_source"],
             stage="Growth", stage_src="web_verified", stage_cite=GJ_BW, stage_conf="high", entry_date="2011-02-14",
             country="US", country_src="web_verified", country_cite=GJ_WSJ, city="San Mateo", city_src="web_verified",
             focus="Consumer & Marketplaces",
             note="Independent mobile app store and ad network, founded in Lithuania in 2004 and based in San Mateo "
                  "(WSJ, 2014), so US, not the pre-filled LT. Tiger's $25M Series C of February 2011 (the company's "
                  "release) was its entry: Growth. Sungy Mobile bought GetJar in February 2014 for $5.3M in cash plus "
                  "an earn-out (WSJ; VentureBeat): acquired.",
             rounds=[rnd("2011-02-14", "Series C", 25_000_000, "Tiger Global Management", True, GJ_BW, "company")]))

# ---------------------------------------------------------------- getninjas-holdings-ltd (membership open)
GN_ADV = PK("getninjas-holdings-ltd", "ADVFN")
GN_REAG = NEWS("getninjas-holdings-ltd", "REAG Investimentos estreia na Bolsa")
L.append(verdict("getninjas-holdings-ltd", "member",
                 "Evan Feinberg, a Tiger partner in tenure, is director on the June 2015 Form D ($8M) of GetNinjas "
                 "Holdings Ltd., the Cayman parent of the Brazilian services marketplace, and GetNinjas reported in "
                 "May 2021 that Tiger Global sold 3,008,034 shares in its IPO offering, cutting its stake to 13.4% "
                 "(ADVFN): a pre-IPO position taken in a private round", ec="formd_adjudicated", conf="high",
                 cite=SEC("getninjas-holdings-ltd")))
L.append(cls("getninjas-holdings-ltd", status="acquired", rng="below_1b", stage="undetermined",
             country="BR", country_src="web_verified", country_cite=GN_ADV, city="São Paulo",
             focus="Consumer & Marketplaces",
             note="GetNinjas, online marketplace for local service professionals, São Paulo; listed on B3 (NINJ3) in "
                  "2021. The Form D of June 2015 records an $8M sale with Tiger's Evan Feinberg as director, but no "
                  "source names that round or says whether Tiger entered earlier, so the stage is undetermined. REAG "
                  "Investimentos took control through a 2024 tender offer and used the listed company for its reverse "
                  "IPO (Exame, 2025-01-28): acquired.",
             rounds=[rnd("2015-06-15", "Form D sale ($8M)", 8_000_000, None, True, SEC("getninjas-holdings-ltd"),
                         "filing")]))

# ---------------------------------------------------------------- gitlab (recall seed confirmed)
GL_IRA = PK("gitlab", "PIP XI", "sec")
gl_usd, gl_asof, gl_cite = SIB("gitlab", "coatue")
L.append(cls("gitlab", rng="1b_plus", usd=gl_usd, val_src="web_verified", val_cite=gl_cite, asof=gl_asof, extra=WV,
             flags=["model_disputes_source"],
             stage="Growth", stage_src="web_verified", stage_cite=GL_IRA, stage_conf="medium", entry_date="2019-09-10",
             country="US", city="San Francisco", focus="DevTools & APIs",
             note="DevOps platform (Nasdaq: GTLB since October 2021), San Francisco address. Tiger Global Private "
                  "Investment Partners XI and Tiger Global Investments sign the investors' rights agreement of "
                  "2019-09-10 that accompanies the Series E preferred (the IPO filing's exhibit), the $268M round led "
                  "by Goldman Sachs and ICONIQ: Tiger's entry, Growth; no earlier Tiger round is on record. The "
                  "agreement names a private-equity fund beside a public-desk fund, so the row stays on the home desk "
                  "(X1 does not apply). Market cap replaces the SEC float: $7.81B (2026-09-25), as the Coatue row reads.",
             rounds=[rnd("2019-09-10", "Series E", 268_000_000, "Goldman Sachs, ICONIQ", True, GL_IRA, "filing")]))

# ---------------------------------------------------------------- glassdoor-inc (membership open)
GD_ON = PK("glassdoor-inc", "Online Recruitment")
L.append(verdict("glassdoor-inc", "member",
                 "Online Recruitment (2015-01-08): 'Glassdoor raises $70 million led by Google Capital and Tiger "
                 "Global Management', a private round; Lee Fixel, in his Tiger tenure, is director on the company's "
                 "2015-2016 Form Ds", ec="web", conf="high", cite=GD_ON))
L.append(cls("glassdoor-inc", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=GD_ON, stage_conf="high", entry_date="2015-01",
             flags=["stage_disputes_band"], city="San Francisco", focus="Consumer & Marketplaces",
             note="Jobs and company reviews site. Google Capital and Tiger led the $70M round of January 2015, "
                  "Tiger's entry into a company founded in 2007 that had raised several rounds: Growth. The Form D "
                  "band's Pre-Seed read a 2012 filing that predates Tiger. Recruit bought Glassdoor for $1.2B in "
                  "2018: acquired. City San Francisco as the Sutter Hill row reads (the Battery row reads Sausalito, "
                  "the founding town).",
             rounds=[rnd("2015-01-08", "unnamed ($70M)", 70_000_000, "Google Capital, Tiger Global", True, GD_ON,
                         "press")]))

# ---------------------------------------------------------------- glossier (recall seed confirmed)
GS_D = PK("glossier", "", "recall")
L.append(cls("glossier", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=GS_D, stage_conf="high", entry_date="2019-03-19",
             country="US", city="New York", focus="Consumer & Marketplaces",
             note="Beauty brand, New York. Tiger joined the $100M Series D led by Sequoia (March 2019, Reuters via "
                  "Yahoo), its first round in the company: Growth. The $1.8B mark of the 2021 Series E did not hold: "
                  "the 2025 raise was sought at under $1B (Forbes, 2025-04-11, as the IVP, Sequoia, Spark and Thrive "
                  "rows record), and the company raised again in 2026 after closing most stores; below $1B, aligned.",
             rounds=[rnd("2019-03-19", "Series D", 100_000_000, "Sequoia Capital", True, GS_D, "press")]))

# ---------------------------------------------------------------- goat-brand-labs (recall seed confirmed)
GB_A = PK("goat-brand-labs", "", "recall")
L.append(cls("goat-brand-labs", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=GB_A, stage_conf="medium", entry_date="2021-07-26",
             country="IN", country_src="web_verified", country_cite=GB_A, city="Bangalore",
             focus="Consumer & Marketplaces",
             note="Aggregator of digital-first consumer brands, Bengaluru. Tiger Global and Flipkart Ventures led the "
                  "company's $36M first round of July 2021 (This Week India), which Exchange4Media names its Series A: "
                  "Tiger's entry. It raised $21M in 2024 and put its Pepe innerwear business up for sale in 2026.",
             rounds=[rnd("2021-07-26", "Series A", 36_000_000, "Tiger Global, Flipkart Ventures", True, GB_A,
                         "press")]))

if __name__ == "__main__":
    jl.write("batch-006a", L, record=os.environ.get("DRY") != "1")
