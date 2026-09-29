#!/usr/bin/env python3
"""PRO-167 Tiger Global, delta queue batch 2 (after the one rebuild), chunk a: Sea Limited/ADR to Unblocked (9 rows).
Evidence: show.py --batch 2, the evidence pack's press and SEC lines, Bing News (bq.py, NQ_TAG=d2), Wikipedia on disk,
WebFetch of press pages (Inc42, dot.la, Crowdfund Insider, AgFunderNews, The AgriBiz, Infomoney, YC's company page,
M13's portfolio page), EDGAR full-text search for Form D filings, and two WebSearch calls (one per S2A no).
Run: NQ_TAG=d2 python3 judgments-d2a.py"""
import json
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, W, SEC, GRADLINES

HERE = Path(__file__).resolve().parent
PKD = json.loads((HERE / "evidence-pack.json").read_text())
CLS_ON_DISK = json.loads((HERE.parent / "companies" / "classification.json").read_text())
WV = {"valuation_range_source": "web_verified"}
CHECK = "2026-09-29"


def PK(slug, kind, sub):
    """The URL on the row's evidence-view line of `kind` ('sec' or 'press') that contains `sub`."""
    urls = []
    for x in (PKD.get(slug, {}).get(kind) or []):
        if sub.lower() not in x.lower():
            continue
        if kind == "sec":
            u = x.rsplit(" | ", 1)[-1].strip()
        else:
            m = re.search(r"\|\| URL (\S+)", x)
            u = m.group(1) if m else ""
        if u.startswith("http"):
            urls.append(u)
    urls = list(dict.fromkeys(urls))
    if len(urls) != 1:
        raise SystemExit(f"PK({slug!r}, {kind!r}, {sub!r}) matched {len(urls)}")
    return urls[0]


def BURL(slug, title_sub, url_sub=""):
    """The one publisher URL among the row's cached news items (news-extra*.json) whose title contains
    `title_sub` and whose URL contains `url_sub`."""
    items = []
    for f in sorted(HERE.glob("news-extra*.json")):
        items += json.loads(f.read_text()).get(slug, [])
    us = list(dict.fromkeys(i["url"] for i in items if i.get("url") and not i.get("gid")
                            and title_sub.lower() in i["title"].lower() and url_sub in i["url"]))
    if len(us) != 1:
        raise SystemExit(f"BURL({slug!r}, {title_sub!r}, {url_sub!r}) matched {len(us)}")
    return us[0]


def ONDISK(slug, key):
    """A key of this book's classification record for the row, read from disk."""
    v = (CLS_ON_DISK.get(slug) or {}).get(key)
    if not v:
        raise SystemExit(f"ONDISK({slug!r}, {key!r}) missing")
    return v


L = []

# ---------------------------------------------------------------- Sea Limited/ADR (ec=filing seed: re-rule)
L.append(verdict("sea-limited-adr", "not_member",
    "13G/13F position in a listed company, no private round naming the firm (T3, D3): the adviser's 13F lines for "
    "Sea start 2018-03-31 and this SC 13G is dated 2018-08-23, both after Sea's NYSE listing of October 2017; no "
    "private round of Sea (Garena) names Tiger. The same company as the excluded row sea-ltd (CIK 1703399), "
    "ruled the same way",
    ec="fund_filing", conf="high", cite=SEC("sea-limited-adr", "edgar")))

# ---------------------------------------------------------------- Shopflo (S2A only)
SF_ACQ = BURL("shopflo", "Pine Labs Acquires Tiger Global-Backed Shopflo", "inc42.com")
SF_SEED = ONDISK("shopflo", "entry_stage_citation")
SF_LINES = GRADLINES("shopflo") + [
    "inc42: Inc42's report of the Pine Labs purchase (2026-04-25, read 2026-09-29) -> 'raised a total of $3.7 Mn to "
    "date', the $2.6M seed of 2022 led by Tiger Global and TQ Ventures the only round it names",
    "bingnews: Bing News, 'Shopflo' with funding, raises, Series A, Binny Bansal and Pine Labs (2026-09-29) -> the "
    "May 2022 seed reports and the April 2026 sale reports only; no later round",
    "web: WebSearch 'Shopflo funding round 2023 OR 2024 OR 2025 raises Series A' (2026-09-29) -> vendor profiles "
    "only (Tracxn, PitchBook and the like): a $1.1M tranche of May 2024 and an unsourced '$20M Series A led by "
    "Binny Bansal' that no publisher reports and that Inc42's $3.7M total contradicts; no press report of a later "
    "round",
]
L.append(cls("shopflo", grad="not_graduated", grad_src="web_verified", grad_cite=SF_ACQ, grad_conf="high",
    grad_asof=CHECK, surfaces=SF_LINES,
    rounds=[rnd("2022-05-11", "Seed", 2_600_000, "Tiger Global and TQ Ventures", True, SF_SEED, "press"),
            rnd("2026-04-25", "Acquisition by Pine Labs (all cash, Rs 88 crore)", None, "Pine Labs", False, SF_ACQ,
                "press")],
    note="S2A not graduated: Pine Labs bought the company in April 2026 (all cash, Rs 88 crore, completed in June), "
         "and Inc42's report of the sale puts total funding at $3.7M, so the $2.6M seed of May 2022 is the last "
         "round of any size on record; nothing reaches a graduation (a named Series A, or an unnamed round of "
         "$5.2M or more). The '$20M Series A' in one web summary comes from vendor profiles and no publisher "
         "reports it."))

# ---------------------------------------------------------------- Spring Health (wave-2 recall addition)
SH_REC = PK("spring-health", "press", "AlleyWatch")
SH_B = PK("spring-health", "press", "Crunchbase News")
SH_E = BURL("spring-health", "Spring Health garners $100M", "mobihealthnews")
L.append(verdict("spring-health", "member",
    "AlleyWatch (2020-11-20), the founder: 'We raised a $76M Series B led by worldwide investment firm Tiger "
    "Global'; Crunchbase News (2020-11-18): 'The Series B was led by Tiger Global'",
    ec="web", conf="high", cite=SH_REC))
L.append(cls("spring-health", status="private", rng="1b_plus", usd=3_300_000_000, val_src="web_verified",
    val_cite=SH_E, asof="2024-07-31", stage="Growth", stage_src="web_verified", stage_cite=SH_B, stage_conf="high",
    entry_date="2020-11", country="US", city="New York", city_src="web_verified", focus="Healthcare & Bio",
    flags=("stale",),
    note="Mental-health benefits platform founded 2016, based in New York City (Wikipedia). Tiger Global led the $76M "
         "Series B of November 2020 as a new investor (Crunchbase News; AlleyWatch), so the entry is Growth; no "
         "earlier round names the firm. Mark: the $100M Series E of July 2024 at $3.3B led by Generation Investment "
         "Management (MobiHealthNews), stale beyond 24 months; Bing News (2026-09-29) shows no later priced round. "
         "Aligned with the General Catalyst row ($3.3B, 2024-07, New York).",
    rounds=[rnd("2020-11-18", "Series B", 76_000_000, "Tiger Global", True, SH_B, "press"),
            rnd("2024-07-31", "Series E", 100_000_000, "Generation Investment Management", None, SH_E, "press")],
    extra=WV))

# ---------------------------------------------------------------- Sunday Robotics (wave-2 recall addition)
SU_REC = PK("sunday-robotics", "press", "Tech Buzz")
SU_B = BURL("sunday-robotics", "Sunday: $165 Million", "pulse2.com")
L.append(verdict("sunday-robotics", "member",
    "The Tech Buzz (2026-03-12): 'The funding round, led by Coatue, Tiger Global, Benchmark, and Bain Capital'; "
    "Pulse 2.0 (2026-03-14) names Tiger Global among the participants in the $165M Series B that Coatue led",
    ec="web", conf="high", cite=SU_REC))
L.append(cls("sunday-robotics", status="private", rng="1b_plus", usd=1_150_000_000, val_src="web_verified",
    val_cite=SU_B, asof="2026-03-12", stage="Growth", stage_src="web_verified", stage_cite=SU_B, stage_conf="high",
    entry_date="2026-03", country="US", city="Mountain View", city_src="web_verified",
    focus="Industrial & Robotics",
    note="Mountain View maker of autonomous household robots (Pulse 2.0: 'a Mountain View-based AI robotics "
         "startup'). Tiger Global joined the oversubscribed $165M Series B of March 2026 at a $1.15B valuation, led "
         "by Coatue with Bain Capital Ventures, Fidelity, Benchmark, Conviction and Xtal Ventures (Pulse 2.0); no "
         "earlier round on record names the firm, so the entry is the Series B: Growth. Mark $1.15B, aligned with "
         "the Coatue and Bain Capital Ventures rows.",
    rounds=[rnd("2026-03-12", "Series B", 165_000_000, "Coatue", True, SU_B, "press")], extra=WV))

# ---------------------------------------------------------------- Timescale / TigerData (wave-2 recall addition)
TS_REC = PK("timescale", "press", "Pulse 2.0")
TS_C = BURL("timescale", "Timescale Valuation Rockets", "businesswire.com")
TS_R = BURL("timescale", "Timescale Becomes Tigerdata", "menafn")
L.append(verdict("timescale", "member",
    "Pulse 2.0 (2022-03-03): Timescale 'announced a $110 million Series C investment led by Tiger Global with "
    "participation from all existing investors'",
    ec="web", conf="high", cite=TS_REC))
L.append(cls("timescale", status="private", rng="1b_plus", usd=1_000_000_000, val_src="web_verified",
    val_cite=TS_C, asof="2022-02-22", stage="Growth", stage_src="web_verified", stage_cite=TS_C, stage_conf="high",
    entry_date="2022-02", country="US", city="New York", city_src="web_verified", focus="Data Infrastructure",
    flags=("stale",),
    note="Time-series and PostgreSQL database company, renamed TigerData in June 2025 (its release, datelined New "
         "York, as is the 2022 release). Tiger Global, a new investor, led the $110M Series C of 2022-02-22 that "
         "valued the company at over $1B (Business Wire), so the entry is Growth; Redpoint's card places the Series "
         "B in 2021 without Tiger. Mark: 'over $1B', recorded at $1B (at the band edge), stale beyond 24 months. "
         "Momentum check (data infrastructure, first seen 2022): Bing News on 2026-09-29 shows no later priced "
         "round; the 2025 rename release names none. Aligned with the Benchmark and Redpoint rows ($1B).",
    rounds=[rnd("2022-02-22", "Series C", 110_000_000, "Tiger Global", True, TS_C, "company")], extra=WV))

# ---------------------------------------------------------------- Traive (wave-2 recall addition)
TR_A = PK("traive", "press", "AgFunderNews")
TR_V = PK("traive", "press", "AgriBiz")
TR_BR = BURL("traive", "Traive fecha acordo", "infomoney")
TR_ES = BURL("traive", "Com nova captação", "estadao")
L.append(verdict("traive", "member",
    "AgFunderNews (2021-11-04) on Traive's $17M Series A: 'Tiger Global Management, Bread and Butter Ventures, "
    "Minerva VC, Syngenta Group Ventures, Serasa Experian VC, YellowRockets.vc, and CSN Inova Ventures also "
    "participated'; The AgriBiz (2024-02-05) lists Tiger Global among its shareholders",
    ec="web", conf="high", cite=TR_A))
L.append(cls("traive", status="private", rng="below_1b", usd=84_000_000, val_src="web_verified", val_cite=TR_V,
    asof="2024-02-05", stage="Series A", stage_src="web_verified", stage_cite=TR_A, stage_conf="high",
    entry_date="2021-10", country="BR", country_src="web_verified", country_cite=TR_BR, focus="Fintech & Payments",
    flags=("stale", "city_unknown"),
    note="Agricultural credit platform (agfintech) founded in 2018 in the United States by Brazilians (Estadão) to "
         "serve Brazilian farmers; AgFunderNews says it is based in the US and Brazil, and the Brazilian press "
         "calls it Brazilian (Infomoney, 2024), so BR. No source names a head-office city: city_unknown. Tiger "
         "Global joined the $17M Series A led by SP Ventures and Astella, raised in October 2021 (Estadão, "
         "2021-10-18; AgFunderNews); the 2020 pre-Series A led by SP Ventures does not name the firm, so the entry "
         "is the Series A. Mark: a $20M round co-led by Banco do Brasil's venture fund and Astella in February 2024 "
         "at $84M post-money (The AgriBiz), below $1B and stale. Momentum check (fintech, first seen 2024): Bing "
         "News on 2026-09-29 shows no later priced round.",
    rounds=[rnd("2020", "Pre-Series A", None, "SP Ventures", None, TR_A, "press"),
            rnd("2021-10", "Series A", 17_000_000, "SP Ventures; Astella", True, TR_A, "press"),
            rnd("2024-02-05", "Unnamed ($84M post-money)", 20_000_000, "Banco do Brasil; Astella", None, TR_V,
                "press")],
    extra=WV))

# ---------------------------------------------------------------- treble.ai (wave-2 recall addition)
TB_A = PK("treble-ai", "press", "contxto")
TB_YC = "https://www.ycombinator.com/companies/treble-ai"   # read with WebFetch 2026-09-29: 'Location: São Paulo, Brazil'
L.append(verdict("treble-ai", "member",
    "contxto (2022-07-21): the startup 'raised an investment of US $15 million in a Series A led by Tiger Global "
    "and with participation from Twilio Ventures, Funders Club'",
    ec="web", conf="high", cite=TB_A))
L.append(cls("treble-ai", status="private", rng="below_1b", stage="Series A", stage_src="web_verified",
    stage_cite=TB_A, stage_conf="high", entry_date="2022-07", country="BR", country_src="web_verified",
    country_cite=TB_YC, city="São Paulo", city_src="web_verified", focus="SaaS",
    note="WhatsApp marketing-automation software (YC Summer 2019), founded in Colombia by Felipe Otálora and Sebastián "
         "Valencia: the 2022 press calls it Bogotá-based (contxto) and a 2023 piece Colombian (Yahoo Finanzas), but "
         "YC's company page, read 2026-09-29, gives its location as São Paulo, Brazil, with status Active; the "
         "current head office is used and the row aligns with the Y Combinator book (São Paulo, BR). Tiger Global "
         "led the $15M Series A of July 2022 (contxto), the firm's first round in the company, so the entry is the "
         "Series A.",
    rounds=[rnd("2022-07-21", "Series A", 15_000_000, "Tiger Global", True, TB_A, "press")]))

# ---------------------------------------------------------------- Trendyol (hq_country claim)
L.append(cls("trendyol", country="TR", country_src="web_verified", country_cite=W("Trendyol"),
    note="Country confirmed from the company's own record: Wikipedia calls Trendyol 'a Turkish e-commerce platform "
         "headquartered in Istanbul'."))

# ---------------------------------------------------------------- Unblocked (S2A; identity corrected)
UB_SEED = BURL("unblocked", "NFT Firm Unblocked Raises", "crowdfundinsider")
UB_LA = "https://dot.la/music-nfts-2656503598.html"   # printed by WebSearch 2026-09-29; read with WebFetch
UB_LINES = [
    GRADLINES("unblocked")[0],
    "formd: EDGAR full-text search of Form D filings (2026-09-29) for 'Non-Fungible Token Company' (no hit) and "
    "'Unblocked' (15 hits, all fund vehicles such as 'RedBird Capital Partners Fund IV (Unblocked), L.P.') -> no "
    "filing by the company",
    "googlenews: Google News, 'Unblocked' with round and exit words -> 30 headlines, none about this company after "
    "its January 2022 seed (the word matches unrelated news)",
    "googlenews_firm: Google News, 'Unblocked' beside 'Tiger Global' -> 2 headlines, both the January 2022 seed "
    "(Forbes, The Mac Observer); no later round",
    "techcrunch: TechCrunch's own search -> 2 headlines naming 'Unblocked', both about the Vancouver developer-tools "
    "namesake (its $20M round of May 2025); none about this company",
    "crunchbase_news: Crunchbase News's own search -> 0 results",
    "bingnews: Bing News, 'Unblocked' with NFT, 'Harrison Wang' and 'NFTCo' (2026-09-29) -> the January 2022 seed "
    "reports only (Forbes, Crowdfund Insider)",
    "web: WebSearch 'Unblocked NFT company Harrison Wang NFTCo funding OR shut down OR acquired' (2026-09-29) -> the "
    "January 2022 seed reports (dot.la, Built In LA, FinSMEs, Crowdfund Insider) and investor pages; no later round",
    "m13: M13's portfolio page for the company (read 2026-09-29) -> 'Unblocked Brands', stage Seed, 'Initial "
    "investment', status Current; now brand discovery and social-proof tools (unblockedbrands.com)",
    "sibling:first-round-capital: its row 'Unblocked' is a different company (the Vancouver developer-tools startup "
    "whose $8.3M seed Amplify Partners led); its May 2025 Series A does not graduate this row",
]
L.append(cls("unblocked", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=CHECK,
    surfaces=UB_LINES, country="US", country_src="web_verified", country_cite=UB_LA, city="Los Angeles",
    city_src="web_verified", focus="Crypto & Web3",
    rounds=[rnd("2021", "Pre-Seed", 5_000_000, None, None, UB_SEED, "press"),
            rnd("2022-01-28", "Seed ($90M post-money)", 10_000_000, None, True, UB_SEED, "press")],
    note="CORRECTION: this row is the Los Angeles NFT company Unblocked, also called The Non Fungible Token Company "
         "(NFTCo), co-founded by Harrison Wang (dot.la: 'The Los Angeles-based startup'; Crowdfund Insider), whose "
         "$10M seed of January 2022 at a $90M valuation named Tiger Global, Dapper Labs and Marcy Venture Partners "
         "among its investors, after a $5M pre-seed in 2021. It is NOT First Round's Vancouver developer-tools "
         "Unblocked (Dennis Pilarinos; $8.3M seed led by Amplify, $20M round in May 2025): the First Round row "
         "flags the same trap, so the Vancouver city, the CA country and the DevTools focus are replaced (Los "
         "Angeles, US, Crypto & Web3) and the two rows are a name collision, not siblings. M13's portfolio page "
         "shows the company now operating as Unblocked Brands (stage Seed, status Current). S2A not graduated: no "
         "surface reports a round after the January 2022 seed."))

if __name__ == "__main__":
    jl.write("delta-002a", L)
