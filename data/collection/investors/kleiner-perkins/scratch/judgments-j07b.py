"""PRO-99 Kleiner Perkins, judge j07, batch 14 (plus one correction to batch 13's emdeon-corporation).
Run: NQ_TAG=j07 python3 judgments-j07b.py"""
import json
import judge_lib as jl
from judge_lib import cls, rnd, verdict, W, ARCH, SITE, POST, FTS

L = []
A = L.append
U = "Graduation left for the graduation pass."
_CLS = json.loads((jl.INV / "companies/classification.json").read_text())


def cited(slug, key):
    """A citation already recorded on another row of this book (read from disk, never typed)."""
    v = (_CLS.get(slug) or {}).get(key)
    if not v:
        raise SystemExit(f"cited({slug!r}, {key!r}): nothing on disk")
    return v


def sib(inv, slug, key):
    v = (json.loads((jl.ROOT / "data/collection/investors" / inv / "companies/classification.json").read_text())
         .get(slug) or {}).get(key)
    if not v:
        raise SystemExit(f"sib({inv!r}, {slug!r}, {key!r}): nothing on disk")
    return v


SIBS = json.loads((jl.INV / "scratch/siblings.json").read_text())


def sibcite(slug, inv):
    v = next((e.get("val_cite") for e in SIBS.get(slug, []) if e["investor"] == inv), "")
    if not v:
        raise SystemExit(f"sibcite({slug!r}, {inv!r}): none")
    return v


# etched: KP participated in the $700M round at $21B (2026-08-18)
et = sibcite("etched", "bain-capital-ventures")
A(cls("etched", stage="Growth", stage_src="web_verified", stage_cite=et, stage_conf="high", entry_date="2026-08-18",
      city="Cupertino",
      rounds=[rnd("2026-08-18", "$700M round at $21B", 700000000, "Jane Street", True, et, "company")],
      note="The company's release of 2026-08-18 names Kleiner Perkins among the investors in the $700M round at $21B "
           "led by Jane Street, the day of the firm's own post; the site lists Etched as a 2026 Growth entry. City "
           "Cupertino as in the sibling rows (the release carries a San Jose dateline)."))

# evalve
A(cls("evalve", status="acquired", rng="below_1b", stage="undetermined", rounds=[], entry_date="1999",
      country="US", city="Menlo Park", focus="Healthcare & Bio",
      note="Evalve (catheter mitral valve repair, Menlo Park) was acquired by Abbott per the firm's own exit field; "
           "since-year 1999, and no source names the firm's round."))

# everlane
A(cls("everlane", rng="below_1b", stage="undetermined", rounds=[], city="San Francisco",
      note="Everlane (San Francisco, sFund on the firm's 2012-14 pages) was bought by Shein for $100M in May 2026 "
           "(Wikipedia, which also reports a planned move to Los Angeles); the firm's round is not on record."))

# expansion-therapeutics
A(cls("expansion-therapeutics", status="private", rng="below_1b", stage="undetermined", rounds=[
          rnd("2018-01-03", "Series A", 55300000, None, None, None, "press"),
          rnd("2021-09-29", "Series B", 80000000, None, None, None, "company")],
      country="US", city="San Diego", focus="Healthcare & Bio",
      note="Expansion Therapeutics (RNA-targeted small molecules, expansionrx.com) is on the firm's health-care list "
           "from 2018 to 2026. Google News shows a $55.3M Series A (January 2018) and an $80M Series B (September 2021), "
           "neither headline naming the firm, so the entry round is not established."))

# fal: KP co-led the October 2025 $250M round at over $4B; Series D $140M at $4.5B (December 2025)
tfn = "https://techfundingnews.com/ex-coinbase-amazon-engineers-fal-ai-raises-250m-to-power-next-gen-multimedia-tools-valuation-tops-4b/"
fd = sibcite("fal", "a16z")
A(cls("fal", status="private", rng="1b_plus", usd=4500000000, val_src="web_verified", val_cite=fd, asof="2025-12-09",
      stage="Growth", stage_src="web_verified", stage_cite=tfn, stage_conf="medium", entry_date="2025-10-23",
      country="US", city="San Francisco", focus="AI & Applied AI", extra={"valuation_range_source": "web_verified"},
      rounds=[rnd("2025-07", "Series C", 125000000, None, None, tfn, "press"),
              rnd("2025-10-23", "$250M round at over $4B", 250000000, "Kleiner Perkins, Sequoia", True, tfn, "press"),
              rnd("2025-12-09", "Series D", 140000000, "Sequoia", True, fd, "company")],
      note="Kleiner Perkins co-led fal's $250M round in October 2025, three months after the $125M Series C (Tech Funding "
           "News, 2025-10-23), the first round found naming the firm, which lists fal as a 2025 Growth entry. Mark: the "
           "$140M Series D at $4.5B (December 2025, the company's release). Momentum check 2026-09-30: talks at about $8B "
           "(March 2026) are reported, not closed."))

# feather (acquired by Vesta, November 2023, as in BCV's row)
A(cls("feather", status="acquired", rng="below_1b", stage="undetermined", rounds=[
          rnd("2019-05-15", "Series A", 12000000, "Spark Capital", None, None, "press"),
          rnd("2020-02-19", "Series B", 30000000, None, None, None, "press")],
      country="US", city="New York", focus="Consumer & Marketplaces",
      note="Feather (furniture rental, New York) was acquired by Vesta with Fernish in November 2023 (Retail Dive "
           "2023-11-13, Modern Retail), acquired as in BCV's row and fresher than Spark's private. The firm's tile "
           "appears from 2018; the round it entered is not named in the coverage found."))

# final (aligned with Y Combinator's row)
A(cls("final", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
      country="US", city="San Francisco", focus="Fintech & Payments",
      note="Final (a credit card startup) wound down in 2017-18 and its team joined Goldman Sachs; acquired as in Y "
           "Combinator's row (an acqui-hire question for Erik's 2026-09-20 rule). The firm's round is not on record."))

# firstbase: KP led the Series B (2022-03); acquired by AppDirect (2024-12-17)
A(cls("firstbase", status="acquired", rng="below_1b", stage="Growth", stage_src="first_party",
      stage_cite=POST("firstbase-series-b"), stage_conf="high", entry_date="2022-03",
      country="US", city="New York", focus="SaaS", flags=["country_conflict"],
      rounds=[rnd("2021", "Series A", None, "a16z", None, None, "press"),
              rnd("2022-03-25", "Series B", None, "Kleiner Perkins", True, POST("firstbase-series-b"), "firm")],
      note="The firm's own post (2022-03-25) says it led Firstbase's Series B, after a16z's 2021 Series A; the firm lists "
           "it among alumni, and AppDirect announced its acquisition on 2024-12-17 (Business Wire). New York from model "
           "knowledge; a16z's row reads Aberdeen, the founder's home, so the two books disagree on the headquarters."))

# fizz (joinfizz.com, New York; the prefilled acquired/GB is a one-word join to another Fizz)
tc = jl.NEWS("fizz", "Kleiner Perkins leads $14.4M seed")
mine = sib("cherry", "fizz", "graduation_citation")
A(cls("fizz", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_cite=tc,
      stage_conf="high", entry_date="2024-06-06", grad="graduated", grad_src="web_verified", grad_cite=mine,
      grad_conf="medium", country="US", city="New York", focus="Fintech & Payments", flags=["model_disputes_source"],
      rounds=[rnd("2024-06-06", "Seed", 14400000, "Kleiner Perkins", True, tc, "press"),
              rnd("2026-01", "Series A (as Mine)", 14000000, "359 Capital", None, mine, "press")],
      note="Kleiner Perkins led the $14.4M seed of Fizz, the New York credit-building debit card (TechCrunch, "
           "2024-06-06; AlleyWatch). Fizz rebranded as Mine and raised a $14M Series A led by 359 Capital in January 2026 "
           "(Pulse 2.0, as in Cherry's row), so the seed graduated. Status and country disputed: the prefilled acquired "
           "and GB match another company named Fizz."))

# fleksy
A(cls("fleksy", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
      country="US", city="San Francisco", focus="Consumer & Marketplaces",
      note="Fleksy (keyboard app, Fleksy Inc., founded 2011) was acquired by Pinterest on 2016-06-15 and then by "
           "ThingThing in 2017 (Wikipedia). The firm's round (Bing Gordon) is not on record."))

# flextronics-international
A(cls("flextronics-international", stage="undetermined", rounds=[], country="US", city="Austin",
      note="Flex (Flextronics, founded 1969) has its corporate headquarters in Austin, Texas (Wikipedia), though the "
           "parent is Singapore-registered. The firm's round is not on record."))

# flodesign-wind-turbine
A(cls("flodesign-wind-turbine", status="defunct", rng="below_1b", stage="undetermined", rounds=[],
      country="US", city="Waltham", focus="Climate & Energy",
      note="FloDesign Wind Turbine renamed itself Ogin and ceased operations in the mid-2010s (model knowledge); the "
           "firm's round (Bill Joy, David Wells, John Doerr) is not on record."))

# focal-systems (aligned with Y Combinator's row)
A(cls("focal-systems", status="private", rng="below_1b", stage="undetermined", rounds=[],
      country="US", city="San Francisco", focus="AI & Applied AI",
      note="Focal Systems (retail computer vision, focal.systems) is on the firm's list from 2021 to 2024; private and "
           "San Francisco as in Y Combinator's row. No round naming Kleiner Perkins was found."))

# focus-media: the trap
A(verdict("focus-media", "not_member",
          "partner-carried: Tina Ju's TDF Capital deal before KPCB China (Erik 2026-09-17 partner-carried rule; "
          "decisions.md X1). No KPCB China fund's own round in Focus Media was found.", ec="site_listing", conf="high"))

# friedola
A(cls("friedola", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
      country="DE", country_src="web_verified", country_cite=ARCH("friedola"), flags=["city_unknown"],
      focus="Industrial & Robotics",
      note="Friedola, a German recycled lightweight plastics company (the firm's own 2013-18 page, Green Growth Fund); "
           "its site no longer answers, its city and current state are not established, and the round is not cited."))

# friendster
fr = W("Friendster")
A(cls("friendster", rng="below_1b", stage="undetermined", country="MY", country_src="web_verified", country_cite=fr,
      city="Kuala Lumpur",
      rounds=[rnd("2003-10", "venture round at a reported $53M valuation", None, "Kleiner Perkins, Benchmark", True, fr, "press"),
              rnd("2006-02", "follow-on", 3000000, None, True, fr, "press")],
      note="Friendster (founded in Mountain View) was funded by Kleiner Perkins and Benchmark in October 2003 at a "
           "reported $53M valuation (Wikipedia), a round Wikipedia does not name; MOL Global of Kuala Lumpur bought it "
           "in 2009 and the site shut in 2015, so the country MY is confirmed and the city is its last owner's."))

# front: the prefilled JP is a one-word join; Front is San Francisco
fb = sibcite("front", "battery-ventures")
A(cls("front", status="private", rng="1b_plus", usd=1700000000, val_src="web_verified", val_cite=fb, asof="2022-06-28",
      stage="undetermined", rounds=[], country="US", city="San Francisco", focus="SaaS",
      flags=["stale", "model_disputes_source"], extra={"valuation_range_source": "web_verified"},
      note="Front (customer communication hub, San Francisco, not the prefilled JP) was last priced at $1.7B in its "
           "June 2022 Series D (the company's blog), a mark older than 24 months. The firm lists it Early 2016 and Prior; "
           "no round naming Kleiner Perkins was found, so the 2016 entry is not established."))

# gambit
ga = "https://gambit.security/announcement/gambit-out-of-stealth"
A(cls("gambit", status="private", rng="below_1b", stage="undetermined", country="US", flags=["city_unknown"],
      focus="Security", extra={"valuation_range_source": "web_verified", "valuation_citation": ga,
                               "valuation_asof": "2026-02-25", "hq_country_confidence": "low"},
      rounds=[rnd("2026-02-25", "Seed and Series A ($61M total)", 61000000, None, True, ga, "company")],
      note="Gambit Security emerged on 2026-02-25 with $61M in seed and Series A funding from Spark Capital, Kleiner "
           "Perkins and Cyberstarts (its own announcement), which does not say which round the firm entered. Momentum "
           "check 2026-09-30: no valuation disclosed and no later round found. Israeli founders; the headquarters "
           "country is inferred US at low confidence."))

# garner-health: KP led the $118M Series D at $1.35B (2026-02-13); Series E $100M at $2.74B (2026-05)
gh = "https://hlth.com/insights/news/garner-health-raises-118m-at-1-35b-valuation-to-scale-doctor-quality-analytics-platform-2026-02-13"
ge = "https://news.fundsforngos.org/2026/06/01/garner-health-raises-100m-to-scale-ai-powered-digital-care-platform/"
A(cls("garner-health", status="private", rng="1b_plus", usd=2740000000, val_src="web_verified", val_cite=ge,
      asof="2026-05", stage="Growth", stage_src="web_verified", stage_cite=gh, stage_conf="medium", entry_date="2024",
      country="US", city="New York", focus="Healthcare & Bio", extra={"valuation_range_source": "web_verified"},
      rounds=[rnd("2026-02-13", "Series D", 118000000, "Kleiner Perkins", True, gh, "press"),
              rnd("2026-05", "Series E", 100000000, "Index Ventures", True, ge, "press")],
      note="Kleiner Perkins led Garner Health's $118M Series D at $1.35B (HLTH, 2026-02-13; New York) and joined the "
           "$100M Series E at $2.74B led by Index Ventures (May 2026), fresher than the siblings' below_1b. The site gives "
           "a 2024 Growth since-year, so the entry date is 2024 and the stage Growth either way."))

# gen-probe-incorporated
A(cls("gen-probe-incorporated", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
      country="US", city="San Diego", focus="Healthcare & Bio",
      note="Gen-Probe (molecular diagnostics, San Diego; Brook Byers) was acquired by Hologic in 2012; the firm's "
           "round is not on record."))

# gen110
A(cls("gen110", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
      country="US", flags=["city_unknown"], focus="Climate & Energy",
      note="Gen110 (residential solar origination, Green Growth Fund, Daniel Oros) shows as Merged on the firm's 2014 "
           "page; the counterparty, its city and the round are not established."))

# genetrix: cannot be identified
A(cls("genetrix", status="unknown", rng="undetermined", stage="undetermined", grad="undetermined",
      country="US", flags=["identity_unresolved", "model_disputes_source"],
      extra={"hq_country_confidence": "low"},
      note="Genetrix appears only as a tile on the firm's 2021-24 all-companies grid linking to a Bloomberg private-company "
           "snapshot that no longer answers; the company could not be identified. The prefilled ES joins the Spanish "
           "biotech group on the one-word name with nothing tying it to the firm, so the country is inferred US at low "
           "confidence."))

# genpharm
A(cls("genpharm", status="acquired", rng="below_1b", stage="undetermined", rounds=[], entry_date="1989",
      country="US", city="Mountain View", focus="Healthcare & Bio",
      note="GenPharm International (transgenic antibody mice) was acquired by Medarex per the firm's own exit field; "
           "since-year 1989, no round named."))

# genscript (KPCB China; listed in Hong Kong 2015)
gs_cap = "https://stockanalysis.com/quote/hkg/1548/market-cap/"
A(cls("genscript", status="public", rng="10b_plus", usd=13037953869, val_src="web_verified", val_cite=gs_cap,
      asof="2026-09-30", stage="undetermined", rounds=[], country="CN", country_src="web_verified",
      country_cite=W("GenScript Biotech"), city="Nanjing", focus="Healthcare & Bio", flags=["kpcb_china"],
      extra={"valuation_range_source": "web_verified"},
      note="GenScript Biotech (HKEX 1548, listed 2015; headquartered in Nanjing per Wikipedia) held by KPCB China (James "
           "Huang) before its listing. Market cap HKD 102.30B @ ECB 2026-09-30 (HKD/EUR 8.9095, EUR/USD 1.1355) = "
           "$13.04B (stockanalysis.com). The round KPCB China entered is not named."))

# gmz-energy
A(cls("gmz-energy", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
      country="US", city="Waltham", focus="Climate & Energy",
      note="GMZ Energy (thermoelectric materials, Massachusetts; Bill Joy) is on the firm's 2012-18 pages; its current "
           "state and the round are not established."))

# goeuro: the same company as the base row omio-formerly-goeuro; aligned with that row
A(cls("goeuro", status="private", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium",
      entry_date="2015", rounds=[], country="DE", country_src="web_verified", country_cite=W("Omio"), city="Berlin",
      focus="Consumer & Marketplaces",
      note="GoEuro is Omio (renamed 2019), the same company as the base row omio-formerly-goeuro, aligned with it: KPCB's "
           "growth team led GoEuro's 2015 round of about $70M after the 2013-14 seed and first rounds, a Growth entry; "
           "Berlin (Wikipedia); no priced mark at $1B or more cited."))

# granola: KP joined the $125M Series C at $1.5B (2026-03-25)
gt = sibcite("granola", "lightspeed")
A(cls("granola", stage="Growth", stage_src="web_verified", stage_cite=gt, stage_conf="high", entry_date="2026-03-25",
      country="GB", country_src="web_verified", country_cite="https://www.granola.ai/jobs", city="London",
      rounds=[rnd("2026-03-25", "Series C", 125000000, "Index Ventures", True, gt, "press")],
      note="Kleiner Perkins participated in Granola's $125M Series C at $1.5B led by Index Ventures (TechCrunch, "
           "2026-03-25, the day of the firm's own post); the site lists it as a 2026 Growth entry. GB confirmed: the "
           "company's own jobs page says 'Designed in London' (Shoreditch), as in the Lightspeed and Spark rows."))

# graphiq (FindTheBest)
gq = W("Graphiq")
A(cls("graphiq", rng="below_1b", stage="undetermined", city="Santa Barbara",
      rounds=[rnd("2010-12", "first outside round", 2000000, "Kleiner Perkins", True, gq, "press"),
              rnd("2011", "follow-on", 4000000, "Kleiner Perkins", True, gq, "press"),
              rnd("2013", "Series B", 11000000, None, True, gq, "press")],
      note="Graphiq (FindTheBest, Santa Barbara): Kleiner Perkins put in $2M in December 2010 after the founders' "
           "$750K each, then $4M in 2011, before an $11M Series B (Wikipedia); the first round is not named. Amazon "
           "bought it in 2017."))

# gravitational: the same company as the base row teleport (renamed 2022); aligned with that row
tb = cited("teleport", "valuation_citation")
A(cls("gravitational", status="private", rng="1b_plus", usd=1100000000, val_src="web_verified", val_cite=tb,
      asof="2022-05-03", stage="Series A", stage_src="first_party",
      stage_cite=POST("gravitational-pulling-us-toward"), stage_conf="high", entry_date="2019-11",
      country="US", city="Oakland", focus="Security", flags=["stale"], extra={"valuation_range_source": "web_verified"},
      rounds=[rnd("2019-11-20", "Series A", 25000000, "Kleiner Perkins", True, POST("gravitational-pulling-us-toward"), "firm")],
      note="Gravitational renamed itself Teleport, the same company as the base row teleport, aligned with it: the firm's "
           "own post (2019-11-20) says it led the $25M Series A; last priced mark the $1.1B Series C of May 2022 (the "
           "company's blog), stale."))

# greatpoint-energy
A(cls("greatpoint-energy", rng="below_1b", stage="undetermined", rounds=[], city="Cambridge",
      note="GreatPoint Energy (coal and biomass to pipeline gas, Cambridge MA on the firm's 2008-10 listing) raised about "
           "$150M from Dow, AES, Suncor, Peabody, ATV, DFJ, Kleiner Perkins, Khosla and Citi (Wikipedia); the firm's "
           "round is not named."))

# greenbio (KPCB China)
A(cls("greenbio", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
      country="CN", country_src="web_verified", country_cite=ARCH("greenbio"), city="Tianjin",
      focus="Climate & Energy", flags=["kpcb_china"],
      note="Tianjin GreenBio (PHA bioplastics; Wei Zhou) on the firm's 2009-10 China listing, located in Tianjin; its "
           "state and the round are not established."))

# groupon: KPCB Holdings bought Series G on 2011-01-11 (S-1)
gp = FTS("Groupon", "S-1")
A(cls("groupon", stage="Growth", stage_src="web_verified", stage_cite=gp, stage_conf="high", entry_date="2011-01-11",
      city="Chicago",
      rounds=[rnd("2011-01-11", "Series G", 65000026, None, True, gp, "filing")],
      note="Groupon's S-1 lists KPCB Holdings buying 2,057,614 shares for $65.0M on 2011-01-11 in the Series G "
           "(the Digital Growth Fund era, John Doerr and Mary Meeker); Growth. Chicago."))

# harmonic (Harmonic AI, Palo Alto): the prefilled public/$654.6M joins Harmonic Inc. (HLIT)
hw = W("Harmonic (company)")
hv = sibcite("harmonic", "ribbit-capital")
A(cls("harmonic", status="private", rng="1b_plus", usd=1450000000, val_src="web_verified", val_cite=hv,
      asof="2025-11-25", stage="Growth", stage_src="web_verified", stage_cite=hw, stage_conf="high",
      entry_date="2025-07", country="US", city="Palo Alto", focus="AI & Applied AI",
      flags=["model_disputes_source"], extra={"valuation_range_source": "web_verified"},
      rounds=[rnd("2024-09-23", "Series A", None, None, None, None, "company"),
              rnd("2025-07", "Series B", 100000000, "Kleiner Perkins", True, hw, "press"),
              rnd("2025-11-25", "Series C", 120000000, None, None, hv, "press")],
      note="Harmonic is the Palo Alto maths AI company (Tudor Achim, Vlad Tenev), not Harmonic Inc.: the prefilled "
           "public $654.6M float belongs to HLIT (the base row harmonic-lightwaves). Kleiner Perkins led the $100M Series "
           "B in July 2025 at $875M (Wikipedia), its entry (site 2025); the $120M Series C at $1.45B followed "
           "(SiliconANGLE, 2025-11-25). Momentum check 2026-09-30: Google News shows no later priced round."))

# hatch (hatchcard.com, renamed Nearside): the firm backed it from its seed to its Series A
hp = POST("hatch-series-a")
fin = jl.NEWS("hatch", "Hatch Raises $20 Million")
A(cls("hatch", status="private", rng="below_1b", stage="Seed", stage_src="first_party", stage_cite=hp,
      stage_conf="high", entry_date="2019-01", grad="graduated", grad_src="first_party", grad_cite=hp, grad_conf="high",
      country="US", flags=["city_unknown"], focus="Fintech & Payments",
      rounds=[rnd("2019-01", "Seed", 5000000, None, True, fin, "press"),
              rnd("2020-02", "Series A", 14000000, None, True, fin, "press"),
              rnd("2021-12", "Series B (as Nearside)", 58000000, None, None, None, "press")],
      note="The firm's own post (2021-04-13) says Hatch formed in its offices and that it supported Hatch 'from Seed to "
           "Series A'; Finovate dates the $5M seed to January 2019 and the $14M Series A to February 2020 (a California "
           "company, city not given). Hatch renamed itself Nearside and raised a $58M Series B in December 2021 (FinTech "
           "Global). Y Combinator's 'Hatch' (W19, acquired) may be this company or another; see the report."))

# health-universe: KP led the $6M seed (2026-03-20)
hu = "https://hitconsultant.net/2026/03/20/health-universe-secures-6m-for-healthcare-ai-agent-platform/"
A(cls("health-universe", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_cite=hu,
      stage_conf="high", entry_date="2025", grad="censored", country="US", flags=["city_unknown"],
      focus="Healthcare & Bio",
      extra={"valuation_range_source": "web_verified", "valuation_citation": hu, "valuation_asof": "2026-03-20"},
      rounds=[rnd("2023", "Pre-Seed", 3500000, None, False, hu, "press"),
              rnd("2026-03-20", "Seed", 6000000, "Kleiner Perkins", True, hu, "press")],
      note="Kleiner Perkins led Health Universe's $6M seed (HIT Consultant, 2026-03-20; $9.5M raised in all, after a "
           "2023 pre-seed from Susa, Twelve Below and Oncology Ventures); the site's close year is 2025. Momentum check "
           "2026-09-30: no valuation disclosed, no later round. Censored."))

# healtheon: the same company as webmd-corp-new and emdeon-corporation; aligned with webmd-corp-new
hs = cited("webmd-corp-new", "entry_stage_citation")
A(cls("healtheon", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified", stage_cite=hs,
      stage_conf="high", entry_date="1996-01-26", city="Elmwood Park", focus="Healthcare & Bio",
      rounds=[rnd("1996-01-26", "Series A", 5142500, None, True, hs, "filing"),
              rnd("1996-10-01", "Series B", 6000000, None, True, hs, "filing")],
      note="Healtheon's 1999 prospectus: Series A preferred sold on 1996-01-26 to purchasers including Kleiner Perkins "
           "Caufield & Byers VII and KPCB VII Founders Fund, which also bought the October 1996 Series B. Healtheon became "
           "WebMD Corp, Emdeon and HLTH (Elmwood Park NJ), merged into WebMD Health Corp in 2009, bought by Internet "
           "Brands in 2017. Same company as the base rows webmd-corp-new and emdeon-corporation."))

# emdeon-corporation: correction to batch 13 (aligned with webmd-corp-new, the same company)
A(cls("emdeon-corporation", stage="Series A", stage_src="web_verified", stage_cite=hs, stage_conf="high",
      entry_date="1996-01-26",
      rounds=[rnd("1996-01-26", "Series A", 5142500, None, True, hs, "filing"),
              rnd("1996-10-01", "Series B", 6000000, None, True, hs, "filing")],
      note="Emdeon Corporation is the 2005 name of Healtheon/WebMD (CIK 1009575), the same company as the base rows "
           "healtheon and webmd-corp-new: Healtheon's 1999 prospectus shows KPCB VII buying its Series A on 1996-01-26. "
           "Renamed HLTH in 2007 (Elmwood Park NJ), merged into WebMD Health Corp in 2009, bought by Internet Brands in 2017."))

# hiemile (renamed Subject)
A(cls("hiemile", status="private", rng="below_1b", stage="undetermined", rounds=[],
      country="US", city="Los Angeles", focus="SaaS",
      note="Hiemile's domain (the firm's 2021-22 consumer tile) now redirects to subject.com, Subject Technologies, a "
           "K-12 digital curriculum platform in use in 2026; Los Angeles from model knowledge. No round naming Kleiner "
           "Perkins was found."))

# hiwifi (KPCB China)
A(cls("hiwifi", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
      country="CN", country_src="web_verified", country_cite=ARCH("hiwifi"), city="Beijing",
      focus="Consumer & Marketplaces", flags=["kpcb_china"],
      note="HiWiFi, described on the firm's 2014 page (Team China, Wen Hsieh) as China's first smart Wi-Fi router "
           "maker; Beijing from model knowledge; its current state and the round are not established."))

# home-network (@Home Network; the base row at-home-corp is its duplicate)
A(cls("home-network", rng="below_1b", stage="undetermined", rounds=[], entry_date="1996", city="Redwood City",
      note="@Home Network got its start from Kleiner Perkins (Wikipedia; the firm's since-year 1996), merged with Excite "
           "in 1999 and filed for Chapter 11 in October 2001; its headquarters were in Redwood City. No round is named."))

# homie
A(cls("homie", status="unknown", rng="below_1b", stage="undetermined", rounds=[], flags=["city_unknown"],
      focus="Consumer & Marketplaces",
      note="Homie appears on the firm's 2017-18 company pages with no description or link, so which Homie it is and its "
           "city, state and round are not established."))

# houzz
A(cls("houzz", stage="undetermined", city="Palo Alto",
      rounds=[rnd("2017-06-24", "$400M round at $4B", 400000000, "Iconiq Capital", False,
                  sibcite("houzz", "iconiq-growth"), "press")],
      note="Houzz (Palo Alto). Kleiner Perkins is not named in the June 2017 $400M round at $4B (TechCrunch lists "
           "Iconiq, Sequoia, Zeev Ventures and GGV) and first appears on the firm's list in 2018; the round it entered "
           "is not on record."))

# the DoorDash post captured as a tile: the same company as the base row doordash; aligned with it
A(cls("https-www-kleinerperkins-com-perspectives-doordash-delivering-the-future-of-local",
      status="public", rng="10b_plus", usd=79530000000, val_src="web_verified",
      val_cite=cited("doordash", "valuation_citation"), asof="2026-09-30",
      stage="Growth", stage_src="first_party", stage_cite=POST("doordash-delivering-the-future-of-local"),
      stage_conf="high", entry_date="2015-03", country="US", city="San Francisco", focus="Consumer & Marketplaces",
      extra={"valuation_range_source": "web_verified"},
      rounds=[rnd("2015-03", "Series B", 40000000, "Kleiner Perkins", True, POST("doordash-delivering-the-future-of-local"), "firm")],
      note="This row is the firm's DoorDash post captured as a grid tile: the same company as the base row doordash, "
           "aligned with it. The post says Kleiner Perkins led DoorDash's Series B (2015); market cap $79.53B on "
           "2026-09-30 (stockanalysis.com)."))

# huaxun-microelectronics (KPCB China)
A(cls("huaxun-microelectronics", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
      country="CN", country_src="web_verified", country_cite=ARCH("huaxun-microelectronics"),
      flags=["kpcb_china", "city_unknown"], focus="Industrial & Robotics",
      note="Huaxun Microelectronics (GPS chips; Zuo Cao) located only as 'Shanxi, China' (a province) on the firm's "
           "2009-10 China listing; city, state and round not established."))

# huizhong (KPCB China)
A(cls("huizhong", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
      country="CN", country_src="web_verified", country_cite=ARCH("huizhong"), city="Beijing",
      focus="Media, Gaming & Advertising", flags=["kpcb_china"],
      note="Huizhong, a Beijing training school for digital entertainment (games) technology on the firm's 2009-10 China "
           "listing (Tina Ju); not one of the named TDF-era deals. State and round not established."))

jl.write("j07b", L)
