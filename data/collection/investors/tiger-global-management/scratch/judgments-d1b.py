#!/usr/bin/env python3
"""PRO-167 Tiger Global, DELTA batch 1, chunk b (rows 16-30: decolar-com-inc .. komodo-health).
Run: NQ_TAG=d1 python3 judgments-d1b.py

Every citation comes from a helper that reads a URL already on disk: the row's evidence view (PR / REC),
the press caches (NEWS, incl. this judge's Bing and Google items), Wikipedia (W), the EDGAR full-text sweep
(FTSDOC), the verdict ledger (LEDGER_CITE), or a sibling book's recorded citation (V / SIBC)."""
import json
import re
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import judge_lib as jl  # noqa: E402
from judge_lib import verdict, cls, rnd, W, NEWS, SEC  # noqa: E402,F401

PK = json.loads((HERE / "evidence-pack.json").read_text())
SIBS = json.loads((HERE / "siblings.json").read_text())
INV = HERE.parent            # tiger-global-management/
ALL = HERE.parents[1]        # investors/
ASOF = "2026-09-29"
WV = {"valuation_range_source": "web_verified"}
_VENDOR = re.compile(r"sacra\.com|pitchbook|cbinsights|tracxn|crunchbase\.com/organization|dealroom|getlatka|forgeglobal|caplight")


def _one(urls, what):
    urls = list(dict.fromkeys(u for u in urls if u))
    if len(urls) != 1:
        raise SystemExit(f"{what}: {len(urls)} matches {urls[:3]}")
    return urls[0]


def PR(slug, sub):
    """The URL printed on the one press line of the evidence view containing `sub`."""
    out = []
    for x in PK.get(slug, {}).get("press") or []:
        if sub.lower() in x.lower() and "|| URL " in x:
            out.append(x.split("|| URL ", 1)[1].split(" || ")[0].strip())
    return _one(out, f"PR({slug!r}, {sub!r})")


def REC(slug):
    """The citation URL at the end of the row's RECALL line."""
    b = PK.get(slug, {}).get("recall_basis") or ""
    return _one(re.findall(r"\((https?://[^\s)]+)\)\s*$", b), f"REC({slug!r})")


def band(usd):
    return "100b_plus" if usd >= 1e11 else "10b_plus" if usd >= 1e10 else "1b_plus" if usd >= 1e9 else "below_1b"


def V(slug, inv):
    """cls() keywords pinning a sibling book's cited mark for the same company (rule 10)."""
    for x in SIBS.get(slug, []):
        if x["investor"] == inv:
            if not x.get("val_cite") or _VENDOR.search(x["val_cite"]) or not x.get("usd"):
                raise SystemExit(f"V({slug!r}, {inv!r}): no usable citation")
            usd = float(x["usd"])
            return dict(rng=band(usd), usd=usd, val_src="web_verified", val_cite=x["val_cite"],
                        asof=x["asof"], extra=dict(WV))
    raise SystemExit(f"V({slug!r}, {inv!r}): no sibling row")


def SIBC(inv, slug, key):
    """A citation a sibling book recorded on its own row for the same company."""
    c = json.loads((ALL / inv / "companies" / "classification.json").read_text())
    v = (c.get(slug) or {}).get(key)
    if not (isinstance(v, str) and v.startswith("http")) or _VENDOR.search(v):
        raise SystemExit(f"SIBC({inv!r}, {slug!r}, {key!r}): nothing usable on disk")
    return v


def FTSDOC(cik, doc_sub):
    """The filing index URL, from the EDGAR full-text sweep, of the registrant's document whose URL contains doc_sub."""
    f = json.loads((INV / "sources/edgar/fts-hits.json").read_text())
    out = []
    for r in f["registrants"]:
        if str(r.get("cik", "")).lstrip("0") == str(cik):
            out += [x["index"] for x in r.get("filings", []) if doc_sub in x.get("url", "")]
    return _one(out, f"FTSDOC({cik}, {doc_sub!r})")


def LEDGER_CITE(slug):
    """The citation of a verdict already in the ledger."""
    led = json.loads((INV / "companies/membership-ledger.json").read_text())["tiger-global-management"]["verdicts"]
    v = (led.get(slug) or {}).get("citation")
    if not (isinstance(v, str) and v.startswith("http")):
        raise SystemExit(f"LEDGER_CITE({slug!r}): none")
    return v


FIRM = ("firm: tigerglobal.com, which publishes no portfolio, posts or announcements (five pages and a login, "
        "read 2026-09-29), and the firm's own fund filings -> no page of the firm names a later round of {}")

L = []

# 16. Decolar.com, Inc.: a Despegar group entity; the group is out as a control position.
DESP = LEDGER_CITE("despegar-com-corp")
L.append(verdict("decolar-com-inc", "not_member",
                 "Control position (T3 addendum), the Despegar group ruling: Decolar.com, Inc. (Buenos Aires) is a Despegar "
                 "group entity whose late-2012 Form D lists Charles Coleman and Scott Shleifer (Tiger) as directors. The "
                 "IPO registration statement shows Tiger's funds (PIP IV, Tiger Global Investments and affiliates) holding "
                 "57.3% of Despegar before the 2017 IPO, a majority stake; same basis as despegar-com-corp.",
                 ec="fund_filing", conf="medium", cite=DESP, exclusion="control_position"))

# 17. Depict.ai: Tiger led the $17M Series A.
u = REC("depict-ai")
u_bw = PR("depict-ai", "Business Wire")
L.append(verdict("depict-ai", "member",
                 "ArcticStartup (2022-02-25): Depict.ai 'has raised 17 million dollars in the Series A funding round led by "
                 "Tiger Global'; the company's release (Business Wire, 2022-02-24) announces the same round.",
                 ec="web", conf="high", cite=u))
L.append(cls("depict-ai", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2022-02-24",
             rounds=[rnd("2021", "Seed", 2_800_000, "Initialized Capital", False, u),
                     rnd("2022-02-24", "Series A", 17_000_000, "Tiger Global", True, u_bw, "company")],
             country="SE", country_src="web_verified", country_cite=u, city="Stockholm", focus="AI & Applied AI",
             note="AI product recommendations for e-commerce, Stockholm (YC). Tiger led the $17M Series A (Feb 2022) after "
                  "the Initialized-led seed of 2021 (EQT Ventures' book), its first round. Momentum slice (AI, first seen "
                  "2022): no later priced round (Bing News 2026-09-29: 2025 product news only; the EQT Ventures book's "
                  "check of 2026-09-27 agrees)."))

# 18. Dianxiaomi: Tiger in the $110M round of August 2022.
u = PR("dianxiaomi", "Yahoo Finance")
L.append(verdict("dianxiaomi", "member",
                 "Reuters via Yahoo Finance (2022-08-16): Dianxiaomi raised $110M in a round led by Sequoia China and "
                 "SoftBank's Vision Fund 2, and 'the investor, China Renaissance, also said the funding round included Tiger "
                 "Global Management and GGV Capital'.",
                 ec="web", conf="high", cite=u))
L.append(cls("dianxiaomi", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="medium", entry_date="2022",
             rounds=[rnd("2022-02", "Series C", 100_000_000, None, None, None),
                     rnd("2022-08-16", "Series D", 110_000_000, "Sequoia China; SoftBank Vision Fund 2", True, u)],
             country="CN", country_src="web_verified", country_cite=u, city="Shenzhen", city_src="web_verified",
             focus="SaaS",
             note="Cross-border e-commerce ERP (店小秘), operated by 深圳美云集网络科技有限责任公司 in Longgang, Shenzhen "
                  "(the company's site footer, read 2026-09-29). Tiger joined the $110M round of August 2022 (Reuters), "
                  "which Chinese press calls the Series D, after a $100M Series C in February 2022 (36Kr) whose investors "
                  "are not on record here: either way a Growth entry, dated to 2022. $210M raised in all; no stated "
                  "valuation, so below $1B (Rule A)."))

# 19. Drizly: Tiger an existing investor by the 2020 Series C; absent from the 2015 A and 2016 B.
u = PR("drizly", "PR Newswire")  # the recall line's release (its URL is cut short on the RECALL line)
L.append(verdict("drizly", "member",
                 "PR Newswire (2020-08-20): Drizly 'has closed a $50 million Series C funding round, led by Avenir ... with "
                 "participation by Tiger Global'; pymnts: 'Tiger Global and other existing investors also participated'.",
                 ec="web", conf="high", cite=u))
L.append(cls("drizly", status="acquired", rng="below_1b",
             stage="Growth", stage_src="model", stage_conf="medium",
             rounds=[rnd("2015", "Series A", 13_000_000, "Polaris Partners", False, W("Drizly")),
                     rnd("2016-08-04", "Series B", 15_000_000, "Polaris Partners", False,
                         NEWS("drizly", "Liquor-delivery startup Drizly laps up")),
                     rnd("2020-08-20", "Series C", 50_000_000, "Avenir", True, u, "company"),
                     rnd("2021-10", "Acquisition (Uber, $1.1B)", None, "Uber", None, W("Drizly"))],
             country="US", city="Boston", focus="Consumer & Marketplaces",
             note="Alcohol delivery marketplace, Boston. Tiger is absent from the 2015 Series A (Polaris, Suffolk, Cava, "
                  "Fairhaven, First Beverage; Wikipedia) and the August 2016 $15M Series B (Polaris, Fairhaven, Suffolk; "
                  "Boston Globe), and is an existing investor by the August 2020 Series C: it came in between, after the "
                  "Series B, so Growth from the named deals; the date is not on record. Uber bought Drizly for $1.1B "
                  "(closed October 2021) and folded it into Uber Eats in 2024 (Wikipedia): acquired."))

# 20. eLong: PIP I bought Series A preferred in the August 2003 placement (the 2004 F-1).
F1 = FTSDOC(1290903, "df1.htm")
L.append(verdict("elong-inc", "member",
                 "eLong's IPO F-1 (October 2004): the investors agreement gives Tiger Technology Private Investment "
                 "Partners, L.P. (PIP I, the private-equity desk) a board seat 'for as long as [it] owns at least 50% of our "
                 "Series A preferred shares originally acquired by' it, the Series A preferred sold to outside investors on "
                 "August 29, 2003; the investors' rights agreement exhibit is signed by PIP I and by Tiger Technology II, "
                 "L.P., both selling shareholders to IAC in 2004. A PIP vehicle in a private round: home desk. Replaces the "
                 "seed-evidence verdict (13G only).",
                 ec="fund_filing", conf="high", cite=F1))
L.append(cls("elong-inc", status="acquired", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=F1, stage_conf="high", entry_date="2003-08-29",
             rounds=[rnd("2003-08-29", "Series A preferred (9,787,494 shares at $1.5325)", 14_999_335, None, True, F1,
                         "filing")],
             country="CN", country_src="web_verified", country_cite=F1, city="Beijing",
             focus="Consumer & Marketplaces",
             note="Online travel agency, Beijing (the F-1's address; Nasdaq: LONG from October 2004). Tiger's PIP I bought "
                  "Series A preferred in the $15.0M placement of August 2003 and sold part to IAC in 2004 (F-1). eLong was "
                  "taken private in 2016 and merged with Tongcheng in 2017 into Tongcheng-Elong (model knowledge): "
                  "acquired."))

# 21. GoExpedi: Tiger among new investors in the $33M round of November 2022, after the Series A and B.
u = REC("goexpedi")
L.append(verdict("goexpedi", "member",
                 "FreightWaves (2022-11-23): GoExpedi 'announced Wednesday it has closed on $33 million in additional "
                 "funding from new investors Tiger Global, Labyrinth Capital Partners, Cortes Capital (Love's private equity "
                 "group), I2BF and FJ Labs'.",
                 ec="web", conf="high", cite=u))
L.append(cls("goexpedi", status="private", rng="below_1b",
             stage="Growth", stage_src="model", stage_conf="high", entry_date="2022-11-23",
             rounds=[rnd("2019-02-26", "Series A", 8_000_000, None, False, NEWS("goexpedi", "Raises $8M Series A")),
                     rnd("2019-11-20", "Series B", 25_000_000, "Top Tier Capital Partners", False,
                         NEWS("goexpedi", "rakes in $25 mln Series B")),
                     rnd("2020-09-15", "unnamed round at about $225M", 25_000_000, "Top Tier Capital Partners", False,
                         NEWS("goexpedi", "Top Tier Capital Partners Doubles Down")),
                     rnd("2022-11-23", "unnamed round", 33_000_000, None, True, u)],
             country="US", city="Houston", focus="Consumer & Marketplaces",
             note="E-commerce and supply-chain platform for industrial and energy MRO parts, Houston. Tiger was among the "
                  "new investors in the $33M round of November 2022 (FreightWaves), which followed the $8M Series A (2019), "
                  "the $25M Series B (2019, PE Hub) and a $25M round at about $225M (2020, WSJ): a post-Series B round, "
                  "Growth from the named deals. No stated valuation at or above $1B."))

# 22. Guideline: Tiger led the $35M Series C; Gusto bought the company in 2025.
u = REC("guideline")
u_g = NEWS("guideline", "Gusto paid $600M")
L.append(verdict("guideline", "member",
                 "WealthManagement.com (December 2018): 401(k) startup Guideline 'has raised a $35 million Series C, led by "
                 "Tiger Global Management' (the recall line's page, misdated 2025 by the crawler).",
                 ec="web", conf="high", cite=u))
L.append(cls("guideline", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2018-12",
             rounds=[rnd("2018-12", "Series C", 35_000_000, "Tiger Global", True, u),
                     rnd("2025-08-27", "Acquisition (Gusto, about $600M)", None, "Gusto", None, u_g)],
             city="Burlingame", focus="Fintech & Payments",
             note="401(k) plans for small businesses, Burlingame (as in the Felicis book). Tiger led the $35M Series C of "
                  "December 2018, its first round. Gusto agreed to buy Guideline in August 2025 (CNBC) for about $600M "
                  "(TechCrunch's sources) and launched Gusto 401(k) on it by November 2025: acquired."))

# 23. Habi: Tiger co-led the pre-seed (pre-launch) round of November 2019.
u_t = PR("habi", "Terra")
u_v = PR("habi", "El Colombiano")
L.append(verdict("habi", "member",
                 "Terra (2019-11-15, the company's release): Habi 'fechou uma rodada de pré-lançamento de US$ 5,5 milhões "
                 "liderada pela Tiger Global Management, bem como pela Homebrew e Zigg' (a $5.5M pre-launch round co-led by "
                 "Tiger); Forbes Colombia (2020) names Tiger among its first investors.",
                 ec="web", conf="high", cite=u_t))
L.append(cls("habi", status="private", rng="1b_plus", usd=1_000_000_000, val_src="web_verified", val_cite=u_v,
             asof="2022-05-11", extra=dict(WV), flags=["stale"],
             stage="Pre-Seed", stage_src="web_verified", stage_cite=u_t, stage_conf="high", entry_date="2019-11-15",
             rounds=[rnd("2019-11-15", "Pre-Seed (pre-launch)", 5_500_000, "Tiger Global; Homebrew; Zigg", True, u_t),
                     rnd("2020-08-27", "unnamed round", 10_000_000, None, None, REC("habi")),
                     rnd("2021-06-23", "Series B", 100_000_000, "SoftBank Latin America Fund", True,
                         PR("habi", "larepublica")),
                     rnd("2022-05-11", "Series C", 200_000_000, None, True, u_v)],
             country="CO", country_src="web_verified", country_cite=u_t, city="Bogotá",
             focus="Consumer & Marketplaces",
             note="Residential real-estate platform (buys, sells and finances used homes), Bogotá. Tiger co-led the $5.5M "
                  "pre-launch round of November 2019 with Homebrew and Zigg (the release; FinSMEs calls it pre-seed): a "
                  "Pre-Seed entry, so the seed-to-A column does not apply. The $200M round of May 2022 made it a unicorn, "
                  "'ya vale más US$1.000 millones' (El Colombiano): the stated floor, at the band edge, and older than 24 "
                  "months (stale). Later financing found is debt (a $100M credit line, 2023)."))

# 24. idealista: Tiger held part of the 46% Apax bought in 2015.
u = REC("idealista")
L.append(verdict("idealista", "member",
                 "Novobrief (2015-07-27): Apax 'had agreed to buy most of the company, acquiring the stakes owned by Tiger "
                 "Global Capital, Bonsai Venture Capital and Kutxabank' (about 46% between them), stakes held while idealista "
                 "was private; the founder says Tiger, a hedge fund, had asked for an exit. When Tiger bought in is not on "
                 "record.",
                 ec="web", conf="medium", cite=u))
L.append(cls("idealista", status="acquired", rng="below_1b", stage="undetermined",
             rounds=[rnd("2015-07", "Acquisition of a controlling stake (Apax Partners)", None, "Apax Partners", None, u)],
             country="ES", country_src="web_verified", country_cite=u, city="Madrid",
             focus="Consumer & Marketplaces",
             note="Online real-estate classifieds in Spain, Italy and Portugal, Madrid. Tiger held part of the 46% that "
                  "Apax bought from Tiger, Bonsai Venture Capital and Kutxabank in July 2015 (Novobrief); the year and round "
                  "of Tiger's entry are not on record, so the stage is undetermined. Apax took control in 2015, EQT bought "
                  "the company in 2020 and Cinven in 2024 (model knowledge): acquired."))

# 25. Indecomm: an early investor beside WestBridge and IFC; exited in 2016.
u = REC("indecomm")
u_vc = PR("indecomm", "VCCircle")
L.append(verdict("indecomm", "member",
                 "Times of India (2016-08-08): 'The Bengaluru-based Indecomm Global Services ... counted WestBridge Capital, "
                 "Tiger Global and International Finance Corporation as its early investors'; in 2012 Tiger and IFC held 25% "
                 "(Times of India). Holdings in the private company; the round is not on record.",
                 ec="web", conf="medium", cite=u))
L.append(cls("indecomm", status="acquired", rng="below_1b", stage="undetermined",
             rounds=[rnd("2016-08", "Acquisition of about 55% (Capital Square Partners); early investors exit", None,
                         "Capital Square Partners", False, u_vc)],
             country="IN", country_src="web_verified", country_cite=u_vc, city="Bangalore",
             focus="Fintech & Payments",
             note="Technology-enabled services and outsourcing for mortgage lenders, founded by Naresh Ponnapa, "
                  "Bangalore-headquartered (VCCircle). Tiger was an early investor beside WestBridge and IFC; when and in "
                  "which round is not on record, so the stage is undetermined. Capital Square Partners bought about 55% in "
                  "August 2016, when Tiger exited: acquired. Focus read as Fintech & Payments (mortgage-lending technology "
                  "and services), a close call."))

# 26. Instacart: Tiger backed the 2018 Series F, the earliest round naming it.
u = REC("instacart")
L.append(verdict("instacart", "member",
                 "Global Venturing (2020-06-12): 'D1 Capital Partners led the $600m first tranche of Instacart's series F "
                 "round, which closed at $871m in November 2018 with backing from Tiger Global Management, Coatue Management "
                 "and Valiant Capital'.",
                 ec="web", conf="high", cite=u))
L.append(cls("instacart", status="public", **V("instacart", "coatue"),
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="medium", entry_date="2018",
             rounds=[rnd("2018", "Series F", 871_000_000, "D1 Capital Partners", True, u)],
             city="San Francisco", focus="Consumer & Marketplaces",
             note="Grocery delivery (Maplebear, Nasdaq: CART since September 2023), San Francisco. The Series F of 2018 "
                  "(D1-led first tranche of $600M, closed at $871M) is the earliest round that names Tiger (Global "
                  "Venturing); Khosla's seed, Sequoia's Series A and the a16z, Thrive and Coatue rounds came before, so "
                  "Growth. Market cap $10.0B on 2026-09-25 (stockanalysis, as in the Coatue and General Catalyst books), "
                  "within 5% of the $10B band edge."))

# 27. Inventa: Tiger joined the January 2022 Series A.
u = REC("inventa")
u_ex = PR("inventa", "Exame")
L.append(verdict("inventa", "member",
                 "Pequenas Empresas & Grandes Negocios (2022-01-24): Inventa's round 'foi liderado pelos fundos Andreessen "
                 "Horowitz e Monashees e contou com a participação de Founders Fund, Greenoaks, Greylock e Tiger Global' "
                 "(Tiger joined the round); Exame (April 2022) lists Tiger in the Greylock-led Series B as well.",
                 ec="web", conf="high", cite=u))
L.append(cls("inventa", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=u, stage_conf="medium", entry_date="2022-01",
             rounds=[rnd("2021-10", "Seed", None, None, None, u_ex),
                     rnd("2022-01-24", "Series A", None, "Andreessen Horowitz; Monashees", True, u),
                     rnd("2022-04-27", "Series B", 55_000_000, "Greylock Partners", True, u_ex)],
             country="BR", country_src="web_verified", country_cite=u, city="São Paulo",
             focus="Consumer & Marketplaces",
             note="B2B marketplace for small and mid-sized retailers, São Paulo. Tiger joined the January 2022 round led by "
                  "a16z and Monashees, which Exame calls the Series A (as do the a16z and Greylock books), after an October "
                  "2021 seed whose investors are not tied to Tiger here; it also joined the Greylock-led $55M Series B "
                  "(April 2022). The Battery Ventures row named Inventa (Santa Clara, acquired) is a different company."))

# 28. Jit: Tiger joined the $38.5M seed; Torq bought the company in May 2026 (a cited end).
u = REC("jit")
u_s = NEWS("jit", "Product Security-as-Code Pioneer Emerges")
u_end = PR("jit", "SiliconANGLE")
L.append(verdict("jit", "member",
                 "Globes (2022-06-15): 'Israeli security-as-code company Jit has announced the completion of a $38.5 million "
                 "seed financing round led by Boldstart Ventures with the participation of Insight Partners, Tiger Global "
                 "Management, and strategic angel investors'.",
                 ec="web", conf="high", cite=u))
L.append(cls("jit", status="acquired", rng="below_1b",
             stage="Seed", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2022-06",
             grad="not_graduated", grad_src="web_verified", grad_cite=u_end, grad_conf="high", grad_asof=ASOF,
             surfaces=[FIRM.format("Jit"),
                       "formd: EDGAR full-text search of Form D filings for 'Jit Technologies' and 'Jit.io' (2026-09-29) -> "
                       "none; no filing by the company and no single-deal vehicle named after it",
                       "googlenews: Google News, \"Jit\" security with round and exit words (2026-09-29) -> the April-May "
                       "2026 Torq acquisition coverage (Business Insider, Calcalist, SiliconANGLE, Business Wire, SC Media); "
                       "no round after the June 2022 seed",
                       "bingnews: Bing News, \"Jit\" security raises and \"Jit\" Torq (2026-09-29) -> the June 2022 $38.5M "
                       "seed release (Business Wire) and the 2026 acquisition coverage (Pulse 2.0: Jit 'raised nearly $40 "
                       "million'); no later round",
                       "sibling:insight-partners: its row for Jit (jit-fka-cbrix) -> S2A not_graduated (web_verified): "
                       "Torq bought Jit for an estimated $70M (Calcalist); the seed was its last round"],
             rounds=[rnd("2022-06-14", "Seed", 38_500_000, "Boldstart Ventures", True, u_s, "company"),
                     rnd("2026-05-19", "Acquisition (Torq)", None, "Torq", None, u_end)],
             country="US", city="Boston", city_src="web_verified", focus="Security",
             note="Developer-first product security (Jit.io), founded in Tel Aviv (the 2022 seed release is datelined "
                  "there); by 2026 the acquirer's release and the press call it Boston-based (Torq, Business Insider), so "
                  "the last known head office is Boston, US; the Insight Partners book holds Tel Aviv, IL (fresher evidence "
                  "here). The pre-filled Japan is a wrong Wikidata join on a one-word name. S2A: the June 2022 $38.5M seed "
                  "was its last round (Pulse 2.0 on the sale: 'raised nearly $40 million'); Torq bought the company in May "
                  "2026 (SiliconANGLE) -> not graduated, a cited end."))

# 29. Just Dial: a pre-IPO venture holder; public, below $1B.
u = REC("just-dial")
L.append(verdict("just-dial", "member",
                 "Techcircle (2013-05-13): 'Just Dial's venture capital investors including SAIF Partners, Tiger Global, "
                 "Sequoia Capital and SAP Ventures will sell part of their holdings in this issue' and 'Tiger Global is also "
                 "expected to make 8x-9x returns on its investment': a position bought while the company was private. The "
                 "round is not on record.",
                 ec="web", conf="medium", cite=u))
L.append(cls("just-dial", status="public", rng="below_1b", usd=583_841_051, val_src="web_verified",
             val_cite="https://stockanalysis.com/quote/nse/JUSTDIAL/market-cap/", asof=ASOF, extra=dict(WV),
             stage="undetermined", rounds=[],
             country="IN", country_src="web_verified", country_cite=W("Justdial"), city="Mumbai",
             focus="Consumer & Marketplaces",
             note="Local search and listings, Mumbai (NSE: JUSTDIAL since June 2013; Reliance Retail has held a majority "
                  "since 2021 and the shares still trade). Tiger was a pre-IPO venture investor beside SAIF, Sequoia and SAP "
                  "Ventures, sold part of its holding in the 2013 IPO and exited in 2015 (Techcircle, Firstpost); Business "
                  "Today puts the investors' entry five to six years before the IPO, but no source names Tiger's round, so "
                  "the stage is undetermined (the searches ran; no round found). Market cap INR 56.04B on 2026-09-29 "
                  "(stockanalysis) @ ECB 2026-09-29 (INR/EUR 108.991, EUR/USD 1.1355) = $583.8M."))

# 30. Komodo Health: Tiger led the $220M Series E at $3.3B.
u = REC("komodo-health")
u_co = SIBC("iconiq-growth", "komodo-health", "entry_stage_citation")
L.append(verdict("komodo-health", "member",
                 "Mercom (2021-03-23): 'Komodo Health Raises $220 Million for Healthcare Data Analytics Platform ... Tiger "
                 "Global Management led the funding round'; the company's own release is titled 'Komodo Health secures $220M "
                 "in funding led by Tiger Global'.",
                 ec="web", conf="high", cite=u))
L.append(cls("komodo-health", status="private", **V("komodo-health", "iconiq-growth"), flags=["stale"],
             stage="Growth", stage_src="web_verified", stage_cite=u_co, stage_conf="high", entry_date="2021-03",
             rounds=[rnd("2021-03-22", "Series E", 220_000_000, "Tiger Global", True, u_co, "company")],
             country="US", city="San Francisco", focus="Healthcare & Bio",
             note="Healthcare data and analytics, San Francisco. Tiger led the $220M Series E at $3.3B (March 2021; the "
                  "company's release, MobiHealthNews as in the ICONIQ book) after a16z's Series C (2020) and ICONIQ's "
                  "Series D (January 2021), so the Series E is its entry. It is the last stated valuation (the late-2022 "
                  "structured equity from Dragoneer and Coatue named none): stale. The a16z book's $3.71B is a Forge "
                  "secondary estimate (Rule A), not a priced event. The param line's '2022, co-led with ICONIQ' is wrong."))

if __name__ == "__main__":
    jl.write("delta-001b", L)
