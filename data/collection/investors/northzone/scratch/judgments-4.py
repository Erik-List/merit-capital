"""PRO-105 grind, batch-004: xbow..zopa (live list) and the 34 Form D name-match rows.
Evidence: scratch/evidence-pack.json, scratch/siblings.json, the Form D sweep grouped by person
(run-log 18:45), and the web checks named per line. Graduation is judged in its own pass;
playdots-inc and sellersfunding-corp are absorbed by identity-merges.json at the rebuild."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd, post, art, sib, page = jl.cls, jl.verdict, jl.rnd, jl.post, jl.art, jl.sib, jl.page
L = []

# ---- Form D name-match rows (decisions.md D9; COLLECTION.md s1 evidence rules, s3 cluster-first)
NO = "not_member"
def pm(slug, why):
    L.append(verdict(slug, NO, why, ec="formd_adjudicated", conf="high"))
HOM = "a 'Paul Murphy' Form D name-match with no corroboration: the Paul Murphy cluster (50 filings) is Del Taco, Sentinel Capital, Canadian gold miners and a surgery centre, other men of that name; "
for s in ["alamos-gold-inc", "collective-mining-ltd", "continental-gold-ltd", "g2-goldfields-inc", "generation-mining-ltd",
          "gpm-metals-inc", "guyana-goldfields-inc", "s2-minerals-inc"]:
    pm(s, HOM + "a Toronto mining issuer whose Paul Murphy is its own officer or director, not a venture seat")
for s in ["del-taco-holdings-inc", "f-c-restaurant-holding-co", "sagittarius-restaurants-llc"]:
    pm(s, HOM + "a restaurant holding issuer (Lake Forest, CA) whose Paul Murphy is its executive officer")
pm("pembina-pipeline-corp", HOM + "a Calgary pipeline operator's executive officer")
pm("critical-solutions-international-inc", HOM + "a Carrollton, TX issuer's executive officer")
pm("ucsd-ambulatory-surgery-center-llc", HOM + "a San Diego surgery centre's director")
pm("clarify-inc", HOM + "an Austin issuer of 2014 whose Paul Murphy is its executive officer, four years before the Northzone Paul Murphy joined (Feb 2018)")
pm("aviary-inc", "Paul Murphy as executive officer of Aviary (2012): six years before the Northzone Paul Murphy joined (Feb 2018); an operator role or a homonym either way, never a Northzone seat (decisions.md D9)")
pm("kumospace-inc", "Paul Murphy as director of Kumospace in 2021-Q4: he announced his move to Lightspeed on 2021-02-26 (TechCrunch), so the seat is Lightspeed's (decisions.md D9)")
pm("good-game-inc", "Paul Murphy as director of Good Game in 2022-Q1: after his move to Lightspeed (2021-02-26), so Lightspeed's seat (decisions.md D9)")
pm("believer-entertainment-inc", "Paul Murphy as director of Believer Entertainment in 2023-Q2: after his move to Lightspeed (2021-02-26), so Lightspeed's seat (decisions.md D9)")
pm("psy-therapeutics-inc", "Paul Murphy as director of Psy Therapeutics (Boston) 2024-25: three years after the Northzone Paul Murphy left (2021); a homonym or another firm's seat, never Northzone's")
pm("fossa-inc", "Paul Murphy as director on FOSSA's 2020-Q1 Form D, inside his Northzone tenure, but 'Paul Murphy' is not a distinctive name (50 unrelated filings) and FOSSA's rounds name no Northzone money: the $23.2M Series B of Oct 2020 was Bain Capital Ventures, Canvas and Costanoa (fossa.com/blog/fossa-raises-series-b), and BCV's own book records no Northzone round; a name-match without corroboration (COLLECTION.md s1)")
for s in ["bioarray-genetics-inc", "etouches-inc", "fitscript-llc", "fmp-products-inc", "shoptext-inc", "summit-street-medical-ioio",
          "xlerant-inc", "zadspace-inc"]:
    pm(s, "a prefix match: the filing's related person is Pauline Murphy, a Connecticut director, not Paul Murphy")
pm("dupont-hospital-llc", "an 'Amit Sanghvi' name-match on a Franklin, TN hospital LLC: a homonym, and no Northzone person of that name held an investing role")
pm("persefoni-ai-inc", "an 'Aaron Liu' name-match on Persefoni (Mesa, AZ) 2023: a common name with no corroboration; no Northzone post, listing or press ties Persefoni to the firm")

# Realize: the director-of-record pattern (COLLECTION.md s1; a16z 2026-08-29, narrowed 2026-08-31)
fd = "https://www.sec.gov/Archives/edgar/data/1896662/000189666224000002/0001896662-24-000002-index.htm"
L.append(verdict("realize-inc", "member",
    "director-of-record pattern: Molly Alter, a current Northzone partner (joined 2023-07-13, the firm's post; partner 2024-08-01), is a director "
    "on Realize, Inc.'s Form Ds of 2024-Q1 ($10.3M) and 2026-Q1 ($25.4M), inside her tenure; the name is distinctive and the issuer resolves to a "
    "real operating company (Realize, New York, an AI capture, proposal and contract management platform, founded 2021 by Curtis Mason, Sean Doherty "
    "and Timothy Goltser; AlleyWatch, 2026-01-05). No Northzone listing or announcement: an unannounced deal, medium confidence, flagged for the A/B "
    "pass; she was at Index Ventures before July 2023, so whether the seat began there is raised in report.md",
    ec="formd_adjudicated", conf="medium", cite=fd))
L.append(cls("realize-inc", status="private", city="New York", rng="below_1b", stage="undetermined",
    focus="AI & Applied AI", flags=["boundary"],
    note="AI capture, proposal and contract management software (New York, founded 2021); Form Ds 2021-Q4 $0.3M, 2024-Q1 $10.3M, 2026-Q1 $25.4M; no round is named anywhere and the Form D band is withheld on a three-year-old issuer, so the entry round is undetermined; $25.4M raised 2025-12/2026-01 at an undisclosed price (AlleyWatch)",
    rounds=[]))

# ---- live list
L.append(cls("xbow", status="private", country="US", country_src="web_verified", country_cite=page("xbow"), city="Seattle",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=post("xbow", "partnering"), entry_date="2026-03",
    rng="1b_plus", usd=1000000000, val_src="web_verified", val_cite=art("xbow", "billion"), asof="2026-03-18", val_conf="medium",
    focus="Security",
    note="Autonomous AI penetration testing (founder Oege de Moor, ex-GitHub); Northzone co-led the $120M Series C of March 2026 (the firm's post), its first investment; Bloomberg 2026-03-18: valued at more than $1 billion (the figure is the floor the report states)",
    rounds=[rnd("2026-03-18", "Series C", 120000000, "co-led: Northzone", True, post("xbow", "partnering"), "firm")]))
L.append(cls("yonder", status="private", country="GB", country_src="web_verified", country_cite=page("yonder"), city="London",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=post("yonder", "our investment"), entry_date="2022-03",
    rng="below_1b", focus="Fintech & Payments", flags=["model_disputes_source"],
    note="UK challenger credit card (London); Northzone co-led the GBP 20m seed with LocalGlobe (the firm's post, 2022-03-31); the pre-filled US country is a one-word Wikidata join and is disputed; not Lux's Yonder (Austin, security)",
    rounds=[rnd("2022-03-31", "Seed", None, "co-led: Northzone, LocalGlobe", True, post("yonder", "our investment"), "firm")]))
L.append(cls("yope", status="private", country="GB", country_src="web_verified", country_cite=page("yope"), city="London",
    stage="undetermined", rng="below_1b", focus="Consumer & Marketplaces",
    note="Private social app for Gen Z (Kyiv-founded, the firm lists the UK); Northzone led the $12.3M round of July 2026, which the record calls 'Pre Series A' (FinSMEs, 2026-07-23) and TechCrunch only 'raises $12.3M': the word straddles Seed and Series A, so it dates the entry and names no stage (Balderton R5); an earlier $4.65M round at $50M (ain.ua, 2025-02-25) had no Northzone",
    rounds=[rnd("2025-02", "undisclosed", 4650000, None, False, None, "press"),
            rnd("2026-07-22", "Pre Series A", 12300000, "Northzone", True, None, "press")]))
L.append(cls("zeal", status="private", country="GB", country_src="web_verified", country_cite=page("zeal"), city="London",
    stage="undetermined", rng="below_1b", focus="Crypto & Web3", flags=["model_disputes_source"],
    note="Self-custody crypto wallet and card (founded by ex-Revolut staff; The Block, 2023-11-21); the firm lists Partnered 2021 and the UK; no round naming Northzone found on the firm's posts or in press, so the stage is undetermined; the pre-filled JP is a one-word Wikidata join, disputed; not the San Francisco Zeal of Spark and YC (payroll API)",
    rounds=[]))
L.append(cls("zervant", status="acquired", country="FI", country_src="web_verified", country_cite=page("zervant"), city="Espoo",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=post("zervant", "leads"), entry_date="2016-08",
    rng="below_1b", focus="SaaS",
    note="SMB invoicing software (Espoo, Finland); Northzone and Conor led the EUR 4M Series A (the firm's post, 2016-08-16); acq. by Ageras Group, 2021 (the firm's post 2021-09-08; the Finnish register shows the entity as Ageras Oy, now Shine Europe Oy)",
    rounds=[rnd("2016-08-16", "Series A", None, "Northzone, Conor Venture Partners", True, post("zervant", "leads"), "firm")]))
L.append(cls("zettle", country="SE", country_src="web_verified", country_cite=page("zettle"), city="Stockholm",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=post("izettle", "series b"), entry_date="2012-06",
    rng="below_1b", focus="Fintech & Payments",
    note="iZettle, mobile card payments (Stockholm); Northzone came in at the $31.4M Series B with Greylock (the firm's post, 2012-06-15; the founder: 'In the Series B round, Northzone came along'); acq. by PayPal, 2018 ($2.2B)",
    rounds=[rnd("2012-06-15", "Series B", 31400000, None, True, post("izettle", "series b"), "firm")]))
L.append(cls("zopa", status="private", country="GB", country_src="web_verified", country_cite=page("zopa"), city="London",
    stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.cnbc.com/2017/06/02/zopa-raises-41-point-2-million-for-challenger-bank-launch.html", entry_date="2017-06",
    rng="1b_plus", usd=sib("zopa", "balderton-capital", "usd") and int(float(sib("zopa", "balderton-capital", "usd"))),
    val_src="web_verified", val_cite=sib("zopa", "balderton-capital", "val_cite"), asof=sib("zopa", "balderton-capital", "asof"),
    focus="Fintech & Payments",
    note="UK digital bank (founded 2005); Northzone's entry is the GBP 32m ($41.2M) round of June 2017 from Wadhawan Global Capital and Northzone, Jeppe Zink quoted (CNBC, 2017-06-02), a late round in a company whose 2021 round was its Series H: Growth; valued at about $1B in the GBP 68m round of Dec 2024 (aligned to Balderton's cited mark)",
    rounds=[rnd("2017-06-02", "undisclosed (late round)", 41200000, None, True,
                "https://www.cnbc.com/2017/06/02/zopa-raises-41-point-2-million-for-challenger-bank-launch.html", "press")]))

jl.write("batch-004", L)
