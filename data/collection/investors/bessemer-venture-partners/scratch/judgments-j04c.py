"""PRO-80 Bessemer, judge j04, file c: batch 8 rows nala .. nym (23 rows)."""
import json
import os

os.environ.setdefault("NQ_TAG", "j04")
import judge_lib as jl
from judge_lib import cls, verdict, rnd, POST, SITE, ARCH, W, NEWS

_SIB = json.loads((jl.INV / "scratch" / "siblings.json").read_text())
_FTS = json.loads((jl.INV / "sources/edgar/fts-hits.json").read_text())["registrants"]


def SIB(slug, investor):
    m = [x for x in _SIB.get(slug, []) if x["investor"] == investor and x.get("val_cite")]
    if len(m) != 1:
        raise SystemExit(f"SIB({slug!r}, {investor!r}) matched {len(m)}")
    return m[0]["val_cite"]


def FTSURL(sub):
    m = {f["url"] for r in _FTS for f in r.get("filings", []) if sub in f["url"]}
    if len(m) != 1:
        raise SystemExit(f"FTSURL({sub!r}) matched {len(m)}")
    return m.pop()


# market-cap page read with curl on 2026-10-01 (stockanalysis.com, the pattern the brief names)
SA_NEPHRO = "https://stockanalysis.com/quote/nse/NEPHROPLUS/market-cap/"

nala_seed = NEWS("nala", "NALA raises $10M seed to build Revolut")
nala_a = NEWS("nala", "NALA raises $40m series A funding")
ncino_val = SIB("ncino", "insight-partners")
ncino_drs = FTSURL("000095012319011979/filename1.htm")
nephro_b = NEWS("nephroplus", "NephroPlus raises $10 mn from IFC, Bessemer")
netlify_val = SIB("netlify", "kleiner-perkins")
netog_a = NEWS("netography", "startup Netography raises $45M")
netog_acq = NEWS("netography", "Vectra AI Acquires Netography to Expand")
netsmart_8k = FTSURL("v058518_8k.htm")
newton_a = NEWS("newton-research", "Announces $9 Million Series A")
nilus_seed = NEWS("nilus", "just landed $8.5M led by Bessemer")
nilus_2025 = NEWS("nilus", "Nilus nets $10M")
noded_tc = NEWS("noded-ai", "wants to make your notes the center")
nova_a = NEWS("nova-benefits", "Series A funding led by SIG, Bessemer")
ntoggle_acq = NEWS("ntoggle", "Rubicon Project Acquires NToggle")
nydig_val = SIB("nydig", "ribbit-capital")
nym_seed = NEWS("nym", "Secures $6M Seed Round")
nym_a = NEWS("nym", "round A led by Google")

lines = [
    cls("nala", status="private", rng="below_1b",
        stage="Seed", stage_src="web_verified", stage_cite=nala_seed, stage_conf="high", entry_date="2022-01-27",
        grad="graduated", grad_src="web_verified", grad_cite=nala_a, grad_conf="high",
        country="US", city="New York", focus="Fintech & Payments", flags=["model_disputes_source"],
        rounds=[rnd("2022-01-27", "Seed", 10000000, "Amplo", True, nala_seed, "press"),
                rnd("2024-07-09", "Series A", 40000000, "Acrew Capital", None, nala_a, "press")],
        note="NALA, cross-border payments for Africa, founded in Tanzania with a US parent; New York as in the Y Combinator "
             "book, not the Wikidata GB. TechCrunch (2022-01-27): the $10M seed 'includes lead investor Amplo, Accel and "
             "Bessemer Partners', two years before the firm's listing year of 2024. The $40M Series A of July 2024 that "
             "Acrew led (Technext) graduates the row. Momentum check 2026-10-01: no priced round at $1B or more (a $50M "
             "credit line in 2026)."),

    cls("ncino", status="public", rng="1b_plus", usd=2050000000, val_src="web_verified", val_cite=ncino_val,
        asof="2026-09-25", flags=["model_disputes_source"],
        stage="Growth", stage_src="web_verified", stage_cite=ncino_drs, stage_conf="high", entry_date="2018-07",
        country="US", city="Wilmington", focus="Fintech & Payments",
        rounds=[rnd("2018-07", "tender offer", None, "Insight Partners, Wellington and Bessemer", True, ncino_drs,
                    "filing")],
        note="nCino, cloud banking software, Wilmington NC (NASDAQ: NCNO). Its draft registration statement: the second "
             "tender offer 'was conducted by each of Insight Partners, Wellington and Bessemer Venture Partners in July "
             "2018', the firm's listing year: a tender entry, Growth. The prefilled 'acquired' is the 2022 holding company "
             "reorganisation, not a sale: the stock trades, market cap $2.05B on 2026-09-25 as the Insight book records it "
             "(the same page read $2.00B on 2026-10-01)."),

    cls("neo", status="private", rng="below_1b",
        stage="Series A", stage_src="first_party", stage_cite=POST("neo-securing-ai-agents"), stage_conf="high",
        entry_date="2026-07-20",
        country="US", city="Boston", city_src="web_verified", focus="Security",
        rounds=[rnd("2026-07-20", "Series A", 100000000, "Andreessen Horowitz and Bessemer", True,
                    POST("neo-securing-ai-agents"), "firm")],
        note="Neo Security, endpoint security for AI agents, Boston (the firm's listing and the release dateline). The firm's "
             "own post: 'Bessemer Venture Partners leads Neo Security's $100M Series A' (2026-07-20), with Andreessen "
             "Horowitz; no valuation was disclosed. The unresolved 'Neo' row of the a16z book is probably this company."),

    cls("nephroplus", status="public", rng="below_1b", usd=676019700, val_src="web_verified", val_cite=SA_NEPHRO,
        asof="2026-10-01",
        stage="Series A", stage_src="model", stage_conf="medium", entry_date="2011-11-22",
        country="IN", country_src="web_verified", country_cite=SITE("nephroplus"), city="Hyderabad",
        focus="Healthcare & Bio",
        rounds=[rnd("2011-11-22", "Series A", None, "Bessemer Venture Partners", True, None, "press"),
                rnd("2014-06-12", "Series B", 10000000, "IFC", True, nephro_b, "press")],
        note="NephroPlus (Nephrocare Health Services), dialysis centres, Hyderabad ('India's highest quality dialysis' "
             "provider in the firm's listing); listed on the NSE in December 2025. INR 65.12B @ ECB 2026-10-01 (INR/EUR "
             "108.832, EUR/USD 1.1298) = $676.0M (stockanalysis.com). Bessemer led the Series A of November 2011, the first "
             "institutional round (named from knowledge; the firm's archive dates it 2011-11-22), before the IFC round of "
             "2014 (Livemint)."),

    cls("netdata", status="private", rng="below_1b",
        stage="Series A", stage_src="web_verified", stage_cite=W("Netdata"), stage_conf="high", entry_date="2020-09-22",
        country="US", city="San Francisco", focus="Data Infrastructure",
        rounds=[rnd("2019-09", "Series A", 17000000, "Bain Capital Ventures", False, W("Netdata"), "press"),
                rnd("2020-09-22", "Series A extension", 14200000, "Bessemer Venture Partners", True,
                    NEWS("netdata", "Extends Series A Funding to $31M"), "company")],
        note="Netdata, open-source infrastructure monitoring, San Francisco as in the Bain Capital Ventures book. Wikipedia: "
             "'In September 2020, the company extended its Series A with an additional $14.2 million led by Bessemer "
             "Venture Partners' (the company's release of 2020-09-22)."),

    cls("netlify", status="private", rng="1b_plus", usd=2000000000, val_src="web_verified", val_cite=netlify_val,
        asof="2021-11-17", flags=["stale"],
        stage="Growth", stage_src="first_party", stage_cite=POST("why-netlify-is-the-architecture"), stage_conf="high",
        entry_date="2021-11-17",
        city="San Francisco", focus="DevTools & APIs",
        rounds=[rnd("2021-11-17", "Series D", 105000000, "Bessemer Venture Partners", True,
                    POST("why-netlify-is-the-architecture"), "firm")],
        note="Netlify, web development platform, San Francisco. The firm's own post: 'we lead Netlify's $105 million Series D "
             "at a $2 billion valuation' (2021-11-17; TechCrunch the same day). No later priced round found; stale."),

    cls("netography", status="acquired", rng="below_1b",
        stage="Series A", stage_src="web_verified", stage_cite=netog_a, stage_conf="high", entry_date="2021-11-15",
        country="US", city="Annapolis", focus="Security",
        rounds=[rnd("2021-11-15", "Series A", 45000000, "Bessemer Venture Partners and SYN Ventures", True, netog_a,
                    "press")],
        note="Netography, network detection and response, Annapolis. SiliconANGLE (2021-11-15): 'Bessemer Venture Partners "
             "and SYN Ventures led the Series A round' of $45M. Acq. by Vectra AI, announced 2025-10-02 (Vectra's release), "
             "which is fresher than the private status in the a16z book."),

    verdict("netsmart-technologies", "not_member",
            "Control position: Netsmart was taken private in 2006-2007 by Insight Venture Partners and Bessemer Venture "
            "Partners for about $115M (the company's 8-K of 2006-11-20: 'a definitive agreement for Netsmart to be acquired "
            "by Insight Venture Partners and Bessemer Venture Partners'); an acquisition of control with a co-investor "
            "group is not a venture round (COLLECTION.md s1 control positions, decisions.md D5)",
            ec="web", conf="high", cite=netsmart_8k),

    cls("netuitive-software", status="acquired", rng="below_1b", city="Reston", focus="Data Infrastructure",
        stage="undetermined", entry_date="2000", rounds=[],
        note="Netuitive, IT performance analytics, Reston; renamed Metricly in 2017 and bought by Virtual Instruments "
             "(Virtana) in 2019 (from knowledge; no page read today). The firm's list gives 2000, which replaces the 2010 "
             "Form D date; no source names the round it entered."),

    cls("neuehealth", rng="below_1b", country="US", city="Doral", focus="Healthcare & Bio",
        stage="Series A", stage_src="first_party", stage_cite=POST("our-deep-health-seed-program"), stage_conf="high",
        entry_date="2016",
        rounds=[rnd("2016", "Series A", None, "Bessemer Venture Partners", True, POST("our-deep-health-seed-program"),
                    "firm")],
        note="NeueHealth (formerly Bright Health), health plans and care delivery; IPO 2021, taken private by New Enterprise "
             "Associates in 2025. The firm's own post: 'We led the Series A of ... Bright Health'; Steve Kraus joined the "
             "board in March 2016. The company moved from Minneapolis to Doral FL (the NEA and Tiger Global books carry "
             "both readings). The base row bright-health-group is the same company."),

    cls("newfront-insurance", status="acquired", rng="below_1b",
        stage="undetermined", entry_date="2017",
        country="US", city="San Francisco", focus="Fintech & Payments", rounds=[],
        note="Newfront, technology-led insurance brokerage, San Francisco; acq. by WTW, completed 2026-01-27 (about $1.3B; "
             "Yahoo Finance, Wikipedia). The firm's year is 2017, the founding year; no source read names the round, so "
             "undetermined. Its 2022 round was priced at $2.2B."),

    cls("newton-research", status="private", rng="below_1b", city="Boston", city_src="web_verified",
        focus="AI & Applied AI", entry_date="2023-12-19",
        grad="graduated", grad_src="web_verified", grad_cite=newton_a, grad_conf="high",
        rounds=[rnd("2023-12-19", "seed", 5100000, None, True, jl.FORMD_CITE("newton-research", 0), "filing"),
                rnd("2025-08-05", "Series A", 9000000, "Greycroft and Bessemer Venture Partners", True, newton_a,
                    "company")],
        note="Newton Research, AI agents for marketing analytics, Boston (its release; the Form D address is Needham). "
             "'Newton Research today announced an oversubscribed $9 Million Series A ... Greycroft and Bessemer Venture "
             "Partners co-led the round' (ADWEEK wire, 2025-08-05): a named Series A graduates the December 2023 seed "
             "whatever the amounts. Momentum check 2026-10-01: no priced round at $1B or more."),

    cls("newvoicemedia", status="acquired", rng="below_1b",
        stage="Growth", stage_src="model", stage_conf="medium", entry_date="2013-08-30",
        country="GB", country_src="web_verified", country_cite=POST("newvoicemedia-joins-vonage"), city="Basingstoke",
        focus="SaaS",
        rounds=[rnd("2013-08-30", "Series D", 35000000, "Bessemer Venture Partners", True, None, "press")],
        note="NewVoiceMedia, cloud contact centre software, Basingstoke UK (the firm's post: 'based in Basingstoke, UK'); "
             "acq. by Vonage, 2018. The firm 'first partnered with NewVoiceMedia back in 2013'; that was the $35M round it "
             "led after Highland's round earlier in the year, a Series D (named from knowledge), before TCV's Series E of "
             "2014."),

    cls("nido-biosciences", status="defunct", rng="below_1b", city="Cambridge", city_src="formd_address",
        focus="Healthcare & Bio",
        note="Nido Biosciences, small molecules for neurological disease, Boston area (Cambridge per its Form D). Boston "
             "Business Journal (2025-12-30): 'Nido Biosciences to shut down after neurological drug trial fails'; no sale "
             "reported, so defunct."),

    cls("nilus", status="private", rng="below_1b",
        stage="Seed", stage_src="web_verified", stage_cite=nilus_seed, stage_conf="high", entry_date="2022-12-14",
        country="US", city="New York", focus="Fintech & Payments",
        rounds=[rnd("2022-12-14", "Seed", 8500000, "Bessemer Venture Partners", True, nilus_seed, "press"),
                rnd("2025-01-16", "unnamed", 10000000, "Felicis and Vesey Ventures", True, nilus_2025, "press")],
        note="Nilus, AI treasury management, headquartered in New York with engineering in Tel Aviv (TechCrunch). "
             "'Nilus has raised $8.5 million in a seed funding round led by Bessemer Venture Partners' (2022-12-14). The "
             "$10M round of January 2025 led by Felicis and Vesey carries no round name in Calcalist and does not double "
             "the seed. Graduation left for the graduation pass. Momentum check 2026-10-01: no priced round at $1B or more."),

    cls("noda-ai", status="private", rng="below_1b",
        stage="Series A", stage_src="first_party", stage_cite=POST("noda-ai-building-the-future"), stage_conf="high",
        entry_date="2026-02-26",
        country="US", city="Austin", city_src="web_verified", focus="AI & Applied AI",
        rounds=[rnd("2026-02-26", "Series A", 25000000, "Bessemer Venture Partners", True,
                    POST("noda-ai-building-the-future"), "firm")],
        note="NODA AI, orchestration software for unmanned defence systems, Austin (the release dateline). The firm's own "
             "post: 'Bessemer Venture Partners leads NODA AI's $25M Series A' (2026-02-26); the company had only pre-seed "
             "money before. Momentum check 2026-10-01: the Series A was reported at a $125M valuation (Tectonic Defense)."),

    cls("noded-ai", status="private", rng="below_1b",
        stage="undetermined", entry_date="2024-07-23",
        country="US", focus="AI & Applied AI", flags=["city_unknown"],
        rounds=[rnd("2024-07-23", "unnamed", 4000000, "Boldstart Ventures", True, noded_tc, "press")],
        note="Noded AI, AI note-taking for work. TechCrunch (2024-07-23): 'Today's $4 million investment was led by "
             "Boldstart Ventures with participation from Bessemer Venture Partners, 20VC and First Hand Ventures'; the round "
             "is not named, as in the 20VC book. No source read places the company in a city. Momentum check 2026-10-01: "
             "no priced round at $1B or more."),

    cls("nominum", status="acquired", rng="below_1b", city="Redwood City", focus="Data Infrastructure",
        stage="undetermined", entry_date="2001-08-24", rounds=[],
        note="Nominum, DNS software for network operators, Redwood City; acq. by Akamai, 2017 (ZDNet). The firm's archive "
             "dates its investment to August 2001; no source found names that round."),

    cls("nova-benefits", status="private", rng="below_1b",
        stage="Series A", stage_src="web_verified", stage_cite=nova_a, stage_conf="high", entry_date="2021-09-09",
        country="IN", country_src="web_verified", country_cite=SITE("nova-benefits"), city="Bangalore",
        focus="Healthcare & Bio",
        rounds=[rnd("2021-09-09", "Series A", 10000000, "SIG and Bessemer Venture Partners", True, nova_a, "press")],
        note="Nova Benefits, employee health benefits platform, Bangalore ('an India-based health benefits platform' in the "
             "firm's listing). VCCircle (2021-09-09): 'Nova Benefits bags Series A funding led by SIG, Bessemer', $10M."),

    cls("npm", status="acquired", rng="below_1b", city="Oakland", focus="DevTools & APIs",
        note="npm, the JavaScript package registry, Oakland; acq. by GitHub, 2020 (the firm's listing)."),

    cls("ntoggle", status="acquired", rng="below_1b", city="Boston", focus="Media, Gaming & Advertising",
        rounds=[rnd("2015-01-26", "unnamed (Form D)", 5575396, None, True, jl.FORMD_CITE("ntoggle", 0), "filing")],
        note="nToggle, traffic shaping for programmatic advertising, Boston; acq. by Rubicon Project, July 2017 ($38.5M, "
             "AdExchanger). No round after the January 2015 one was found. Graduation left for the graduation pass."),

    cls("nydig", status="private", rng="1b_plus", usd=7000000000, val_src="web_verified", val_cite=nydig_val,
        asof="2021-12-14", flags=["stale"],
        stage="undetermined", entry_date="2017",
        country="US", city="New York", focus="Crypto & Web3",
        rounds=[rnd("2017", "initial early-stage investment (unnamed)", None, None, True,
                    POST("out-of-stealth-nydig-raises"), "firm"),
                rnd("2020-10-13", "growth equity round", 50000000, "FinTech Collective", True,
                    POST("out-of-stealth-nydig-raises"), "firm"),
                rnd("2021-12-14", "growth round", 1000000000, "WestCap", None, nydig_val, "company")],
        note="NYDIG, bitcoin custody and financial services, New York. The firm's 2020 post speaks of 'Bessemer's initial "
             "early-stage investment' when NYDIG spun out of Stone Ridge three years earlier; 'early-stage' names no round, "
             "so undetermined, dated 2017 from the listing. The $1 billion round of December 2021 valued it at more than "
             "$7 billion (the company's release), as in the Ribbit book; stale."),

    cls("nym", status="private", rng="below_1b",
        stage="Seed", stage_src="web_verified", stage_cite=nym_seed, stage_conf="high", entry_date="2019-06-13",
        grad="graduated", grad_src="web_verified", grad_cite=nym_a, grad_conf="high",
        country="US", city="New York", focus="Healthcare & Bio",
        rounds=[rnd("2019-06-13", "Seed", 6000000, "Bessemer Venture Partners", True, nym_seed, "press"),
                rnd("2020-10-14", "Series A", 16500000, "GV", None, nym_a, "press")],
        note="Nym Health, autonomous medical coding, New York with its research in Tel Aviv. NoCamels (2019-06-13): 'a $6 "
             "million seed investment round led by Bessemer Venture Partners'. Calcalist (2020-10-14): 'Nym Health raises "
             "$16.5 million round A led by Google's investment arm', which graduates the row. The 'Nym' rows of the a16z and "
             "Lightspeed books are the privacy network, a different company; Lightspeed's nym-health row reads the 2020 "
             "round as a seed."),
]

jl.write("j04c", lines)
