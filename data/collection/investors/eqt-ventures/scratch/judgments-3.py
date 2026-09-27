"""PRO-163 grind, batches 003-004 (varjo .. uipath-inc), the recall addition Bluebook and the Form D
name-match rows. Same evidence and conventions as judgments-1/2.py. Rows that merge at the scheduled
rebuild (home -> buena, origin-bio -> insempra, quit-genius -> pelago, wajve -> owwn, treecard -> wildhero,
vidlab7 -> moonscale, aifloo and noomi -> nectarine-health) are not classified here: their canonical row
carries the company."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd, S, A, W, SITE, ARC = jl.cls, jl.verdict, jl.rnd, jl.S, jl.A, jl.W, jl.SITE, jl.ARC
L = []

def site_c(slug, code, **kw):
    return dict(country=code, country_src="web_verified", country_cite=SITE(slug), **kw)

def arc_c(slug, code, **kw):
    """Country from the firm's own archived eqtventures.com page (its Geography field)."""
    return dict(country=code, country_src="web_verified", country_cite=ARC(slug), **kw)

# ------------------------------------------------------------------ membership verdicts
L.append(verdict("bimobject", "not_member",
    "EQT Ventures' EUR 23.4M investment of Jul 2018 went into BIMobject AB, listed on Nasdaq First North since 2012: 'You just invested a big ticket in a public "
    "company?' (the firm's own post, 2018-07-18). A position that first appears as a purchase in a listed company is not a venture round in a private company "
    "(COLLECTION.md s1, T3; the post-RIA public-purchase rule); the firm listed it 2018-2025.", ec="site_listing", conf="high",
    cite=S("23-4m-investment-in-bimobject")))
L.append(verdict("bluebook", "member",
    "The firm's own announcement: 'Why EQT Ventures is Backing Bluebook ... Within hours of our first meeting with Bluebook, we had a term sheet signed' (2025-02-13, "
    "authors from the EQT Ventures team). Absent from the portfolio pages and the archive; a recall addition.", ec="site_listing", conf="high",
    cite=S("eqt-ventures-backs-bluebook")))
L.append(verdict("hinge-health-inc", "not_member",
    "The Form D seat (Carolina Brochado, director, 2017 and 2020) is from her Atomico years: she joined EQT Partners in Jun 2020 for EQT Growth and heads EQT Ventures "
    "only since 2025 (her EQT page). No EQT Ventures fund, listing or post names Hinge Health (T4; decisions.md D6).", ec="formd_adjudicated", conf="high",
    cite="https://eqtgroup.com/about/people/carolina-brochado"))
L.append(verdict("securityscorecard-inc", "not_member",
    "The Form D director 'Thomas Mendoza' (2016-2019) is NetApp's vice chairman, a SecurityScorecard board member, not EQT Ventures' Tom Mendoza, who was a Deal Partner "
    "in London from 2019 (the firm's team pages); no EQT listing or post names the company (T4 homonym).", ec="formd_adjudicated", conf="high"))
L.append(verdict("uipath-inc", "not_member",
    "The Form D director 'Tom Mendoza' (2018) is NetApp's vice chairman, a UiPath board member, not EQT Ventures' Tom Mendoza (who joined the fund in 2019); no EQT "
    "listing or post names UiPath (T4 homonym).", ec="formd_adjudicated", conf="high"))
L.append(verdict("algolux-inc", "not_member",
    "Name-match only: the 2021 Form D of a Montreal issuer lists 'Alistair Mitchell' as director. EQT Ventures' partner files as 'Alastair Mitchell' (Stryder, Permutive, "
    "Standard Cognition), no EQT listing, archive capture or post names Algolux, and a Canadian director of the same spelling also sits on Rank Software's Form D: no "
    "corroboration, so not a member (COLLECTION.md s1, name-match sufficiency).", ec="formd_adjudicated", conf="high"))
L.append(verdict("rank-software-inc", "not_member",
    "Name-match only: the 2019 Form D of a Toronto issuer lists 'Alistair Mitchell' as director, the same spelling as the Algolux filing and not EQT's Alastair Mitchell; "
    "no EQT listing, capture or post names the company (name-match sufficiency).", ec="formd_adjudicated", conf="high"))
L.append(verdict("sitevue-ai-inc", "not_member",
    "The 2026 Form D names Leila Pirbay as director of a Tennessee issuer founded 2025. She appears on the EQT Ventures team pages only in 2022-2023 (Venture Lead, San "
    "Francisco); a 2026 seat is dated against her firm at filing time, and no EQT listing or post names SiteVue (T4, seat dating).", ec="formd_adjudicated", conf="high"))

# ------------------------------------------------------------------ classification
L.append(cls("varjo", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=S("investment-in-varjo"), entry_date="2017-09", **site_c("varjo", "FI"), city="Helsinki", focus="Industrial & Robotics",
    note="Human-eye-resolution VR/XR headsets. 'announced its $8.2M Series A, led by EQT Ventures' (the firm's post, 2017-09-29)."))

L.append(cls("vectary", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="medium",
    stage_cite="https://www.finsmes.com/2020/10/vectary-raises-7m-in-seed-funding.html", entry_date="2020-10",
    country="SK", country_src="web_verified", country_cite=SITE("vectary"), city="Bratislava", focus="SaaS", flags=["model_disputes_source"],
    note="3D and AR design platform (Slovak-founded; Form D filed by its US entity in Redwood City). EQT Ventures led the $7.3M round of Oct 2020 with BlueYard (the firm's "
         "post; UKTN), which FinSMEs calls a seed. Graduation judged in the surfaces pass."))

L.append(cls("verkor", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite="https://cleantechnica.com/2021/07/15/french-battery-startup-verkor-raises-118-million-in-funding-round/", entry_date="2021-07",
    city="Grenoble", focus="Climate & Energy",
    note="Low-carbon battery cells (gigafactory in Dunkirk, 2025). EQT Ventures co-led the EUR 100M Series B with Renault Group (Jul 2021); EUR 850M equity within the EUR 2B "
         "raise of Sep 2023 (Macquarie-led, EQT participating) with no valuation disclosed, so no $1B+ band (Rule A)."))

L.append(cls("vev", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://tech.eu/2021/05/27/oslo-based-visual-editing-platform-vev-raises-e5-million-in-seed-round-led-by-eqt-ventures/", entry_date="2021-05",
    country="NO", country_src="web_verified", country_cite=ARC("vev"), city="Oslo", focus="SaaS",
    note="Visual web-content editor. EUR 5M seed led by EQT Ventures (May 2021, Tech.eu), the fund's first Norwegian investment and Motherbrain's tenth sourced deal. "
         "Graduation judged in the surfaces pass."))

L.append(cls("viridico2", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://tech.eu/2023/03/07/viridico2-secures-ps3m-in-seed-funding-to-make-chemical-products-from-co2/", entry_date="2023-03",
    **site_c("viridico2", "GB"), city="Southampton", focus="Climate & Energy",
    note="Carbon capture and utilisation (University of Southampton spin-out). GBP 3M seed led by EQT Ventures (Mar 2023, Tech.eu). Graduation judged in the surfaces pass."))

L.append(cls("volt", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=S("investment-in-volt"), entry_date="2021-06", country="GB", country_src="web_verified", country_cite=SITE("volt"),
    city="London", focus="Fintech & Payments", flags=["model_disputes_source"],
    note="Open-banking instant payments. EQT Ventures led the $23.5M Series A (the firm's post, 2021-06-17); $60M Series B 2023. London-based; the Wikidata NO is a wrong join."))

L.append(cls("vsim", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://tech.eu/2024/09/26/vsim-founded-by-ex-nvidia-duo-raises-21-5m/", entry_date="2024-09",
    **site_c("vsim", "GB"), focus="Industrial & Robotics", flags=["city_unknown"],
    note="Physics simulation for robotics (ex-Nvidia founders). EQT Ventures led the $21.5M seed at about $100M (Sep 2024, Tech.eu; TechCrunch). The sources place it in "
         "Cambridge, Manchester or Altrincham, so the city is left unknown. Graduation judged in the surfaces pass (entry just past 24 months)."))

L.append(cls("wandelbots", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=S("investment-in-wandelbots-demonstration"), entry_date="2018-12", **site_c("wandelbots", "DE"), city="Dresden",
    focus="Industrial & Robotics",
    note="Robot programming by demonstration. 'its EUR 6M Series-A investment co-led by Paua Ventures and EQT Ventures' (the firm's post, 2018-12-13)."))

L.append(cls("warducks", status="private", rng="below_1b", stage="undetermined", **site_c("warducks", "IE"), city="Dublin",
    focus="Media, Gaming & Advertising",
    note="AR mobile games (Motherbrain-sourced). EQT Ventures led the EUR 3.3M round of Mar 2019 (the firm's post; Tech.eu), after a EUR 0.3M seed from Suir Valley (2017); "
         "no source names the round, so undetermined. The firm's Exit 2023; no sale or closure was found."))

L.append(cls("watty", status="acquired", rng="below_1b", stage="undetermined", **site_c("watty", "SE"), city="Stockholm",
    focus="Climate & Energy",
    note="AI energy monitoring. 'EQT Ventures is happy to join Watty's EUR 3 million investment round alongside Nordic accelerator Cleantech Invest' (the firm's post, "
         "2016-07-12); no source names the round. acq. by Discovergy, 2019 (Nordic9); Watty AB was declared bankrupt in Nov 2020 (Newsworthy)."))

L.append(cls("wolt", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=S("latest-investment-in-wolt"), entry_date="2016", city="Helsinki", focus="Consumer & Marketplaces",
    note="Food and retail delivery. 'EQT Ventures ... has been an investor and close partner in Wolt's journey since the initial A round back in 2016' (the firm's post, "
         "2021-01-25; EQT's release 2021-11-09: 'EQT Ventures led the early Series-A financing round'). EQT Growth joined in Jan 2021 (another desk; the row is a member "
         "through the Ventures entry, decisions.md D2). acq. by DoorDash, 2022 (all-stock, ~EUR 7B)."))

L.append(cls("beside", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=S("beside-raises-32m"), entry_date="2025-11", **site_c("beside", "FR"), focus="AI & Applied AI",
    flags=["model_disputes_source", "city_unknown"],
    note="AI phone and receptionist for small businesses (M1 in stealth). 'We are excited ... to be a part of this journey as Series A lead investors' (the firm's post, "
         "2025-11-11; $32M with Index's seed). The firm's Key Facts say France; no source states the headquarters city. The Wikidata JP is a wrong join."))

L.append(cls("billhop", status="private", rng="below_1b", stage="undetermined", **arc_c("billhop", "SE"), city="Stockholm",
    focus="Fintech & Payments",
    note="B2B card payments for invoices. EQT Ventures led the EUR 10.5M round of Feb 2022 with Element Ventures (Tech.eu); no source names the round; a SEK 88M bridge "
         "from existing investors followed (Nordic9)."))

L.append(cls("camion", status="private", rng="below_1b", stage="Pre-Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.uktechnews.info/2024/04/24/camion-secures-2-3-million-pre-seed-investment-led-by-eqt-ventures/", entry_date="2024-04",
    **site_c("camion", "GB"), city="London", focus="Climate & Energy",
    note="EV-charging site intelligence. GBP 2.3M pre-seed led by EQT Ventures (Apr 2024, UK Tech News; site: EQT Ventures III, 2023)."))

L.append(cls("clarifeye", status="private", rng="below_1b", stage="Pre-Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.finsmes.com/2025/10/clarifeye-raises-e4m-in-pre-seed-funding.html", entry_date="2025-10",
    **site_c("clarifeye", "FR"), city="Paris", focus="AI & Applied AI",
    note="Expert-knowledge AI agents (ex-Dataiku founders). EUR 4M pre-seed led by EQT Ventures (Oct 2025, FinSMEs; Tech.eu)."))

L.append(cls("colossi-games", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.finsmes.com/2021/02/colossi-games-raises-2-5m-in-seed-funding.html", entry_date="2021-02",
    **arc_c("colossi-games", "CY"), focus="Media, Gaming & Advertising", flags=["city_unknown"],
    note="Mobile survival RPG studio. $2.5M seed led by EQT Ventures with Play Ventures (Feb 2021, FinSMEs); Cyprus-based, city not stated. Graduation judged in the surfaces pass."))

L.append(cls("curb", status="private", rng="below_1b", stage="Seed", stage_src="model", stage_conf="low", entry_date="2020-12",
    grad="graduated", grad_src="web_verified", grad_cite="https://www.finsmes.com/2021/06/dark-kitchen-startup-curb-raises-e20m-in-funding.html",
    **arc_c("curb", "SE"), city="Stockholm", focus="Consumer & Marketplaces", flags=["stage_uncited"],
    note="Delivery-first dark kitchens (founded May 2020). EQT Ventures led the EUR 3.2M first round (Dec 2020, EU-Startups), which no source names: Seed by position at low "
         "confidence. The EUR 20M round led by Point72 with EQT (Jun 2021, FinSMEs) is unnamed and clears 2x the entry and $5M, so graduated."))

L.append(cls("darkstore", status="defunct", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite="https://techcrunch.com/2019/09/19/darkstore-raises-21-million-series-b-round/", entry_date="2019-09",
    city="San Francisco", focus="Consumer & Marketplaces",
    note="Same-day fulfilment network (FastAF). EQT Ventures led the $21M Series B (Sep 2019, TechCrunch; Laura Yao to the board). The company is closed (Crunchbase: "
         "permanently closed; no operations found); no sale was found, so defunct."))

L.append(cls("docly", status="unknown", rng="below_1b", stage="undetermined",
    country="SE", country_src="web_verified", country_cite="https://sifted.eu/articles/min-doktor-startup-failure", city="Malmö",
    focus="Healthcare & Bio", flags=["model_disputes_source"],
    note="Digital-care platform split out of Min Doktor in Aug 2018, so the fund's position arrived by demerger rather than a round (stage undetermined); 'EQT Ventures "
         "declined to make a follow-up investment in Docly' (Sifted). Headquartered in Malmö (the archive's Geography lists its markets). No closure or sale on the Swedish "
         "register or in the press: status unknown. Raised for Erik: a demerger twin of a member (report)."))

L.append(cls("dott", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://tech.eu/2018/12/14/amsterdam-based-e-scooter-startup-dott-raises-e20-million/", entry_date="2018-12",
    grad="graduated", grad_src="web_verified",
    grad_cite="https://www.eu-startups.com/2019/07/amsterdam-based-startup-dott-raises-another-e30-million-to-roll-out-its-safe-e-bikes-and-scooters/",
    **arc_c("dott", "NL"), city="Amsterdam", focus="Consumer & Marketplaces",
    note="Shared e-scooters and e-bikes. EUR 20M seed co-led by EQT Ventures and Naspers (Dec 2018, Tech.eu; Unquote); the EUR 30M Series A of Jul 2019, co-led again, "
         "graduates it (Wikipedia names it the Series A). Merged with TIER in 2024; the combined company operates as Dott."))

L.append(cls("ecoplanet", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite="https://tech.eu/2025/01/20/ecoplanet-secures-16m-series-a-led-by-eqt-ventures/", entry_date="2024-12",
    **site_c("ecoplanet", "DE"), city="Munich", focus="Climate & Energy",
    note="AI energy management for industry. EUR 16M Series A led by EQT Ventures (announced Jan 2025, Tech.eu; site Entry 2024)."))

L.append(cls("filament", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="medium",
    stage_cite="https://www.thefoundersmagazine.com/filament/", entry_date="2025-09", grad="censored",
    country="US", country_src="web_verified", country_cite=SITE("filament"), city="New York", focus="Consumer & Marketplaces",
    flags=["model_disputes_source"],
    note="Invite-only professional network (Tony Haile). $10.7M seed with EQT Ventures, Flybridge and Mozilla Ventures (Sep 2025); the page's Fund 'V3' is EQT Ventures III. "
         "The Wikidata AU is a wrong join."))

L.append(cls("hiber", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.pocketgamer.biz/news/76794/hiber-15-million-series-a/", entry_date="2021-06",
    **arc_c("hiber", "SE"), city="Stockholm", focus="Media, Gaming & Advertising",
    note="No-code 3D world creation (HiberWorld). $15M Series A led by EQT Ventures (Jun 2021, PocketGamer; the firm's post)."))

L.append(cls("ineffable-intelligence", status="private", rng="1b_plus", usd=5100000000, val_src="web_verified",
    val_cite="https://www.bloomberg.com/news/articles/2026-04-27/sequoia-and-nvidia-back-ex-deepmind-researcher-at-5-1-billion-value", asof="2026-04-27",
    stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=S("first-contact-with-superintelligence"), entry_date="2026-04", grad="censored",
    **site_c("ineffable-intelligence", "GB"), city="London", focus="AI & Applied AI",
    note="Reinforcement-learning 'superlearner' (David Silver, ex-DeepMind). 'We are proud to support Ineffable Intelligence as part of their $1.1 billion seed round' (the "
         "firm's post, 2026-04-27, authors from the EQT Ventures team; the page names no fund, and the Scaleup Europe Fund did not yet exist). The seed, co-led by Sequoia "
         "and Lightspeed, valued it at $5.1B (Bloomberg; TechCrunch). The mark was set by the entry round itself."))

L.append(cls("infinit", status="private", rng="below_1b", stage="undetermined", **site_c("infinit", "FR"), focus="Fintech & Payments",
    flags=["city_unknown"],
    note="Vertical banking and AI business tools for SMEs. EQT Ventures III entered in 2022 (the firm's Key Facts); no source names the round or the city."))

L.append(cls("kitemaker", status="acquired", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://nordic9.com/news/kitemaker-raised-2-million-in-funding-from-eqt-ventures-and-sno-ventures/", entry_date="2021",
    **arc_c("kitemaker", "NO"), city="Oslo", focus="SaaS",
    note="Product management tool (YC). A $2M seed led by EQT Ventures and SNÖ Ventures (2021, Nordic9). acq. by ClickUp, 2025. Graduation judged in the surfaces pass."))

L.append(cls("luko", status="acquired", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2020-12",
    **arc_c("luko", "FR"), city="Paris", focus="Fintech & Payments", flags=["stage_uncited"],
    note="Home insurtech. EQT Ventures entered at the Series B of late 2020 with Accel, Speedinvest and Founders Fund (the archive's announcement date 2020-12-07); the round's "
         "own coverage was not read, so model at medium. Placed in receivership in Nov 2023; Allianz Direct bought the business for EUR 4.3M (court approval 2024-01-24, "
         "TechCrunch): insolvency followed by an asset sale reads acquired."))

L.append(cls("marvel-fusion", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite="https://tech.eu/2025/03/27/marvel-fusion-secures-eur50m-series-b-extension-for-fusion-energy-development/", entry_date="2025-03",
    city="Munich", focus="Climate & Energy",
    note="Laser-driven fusion energy. EQT Ventures entered with the EUR 50M extension of the Series B to EUR 113M (Mar 2025, Tech.eu; the firm's post)."))

L.append(cls("marvelx", status="private", rng="below_1b", stage="Pre-Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=S("marvelx"), entry_date="2025-05", **site_c("marvelx", "NL"), focus="AI & Applied AI", flags=["city_unknown"],
    note="AI agents for insurance operations. 'we are thrilled to lead MarvelX's $6 mn pre-seed round' (the firm's post, 2025-05-13); the city is not stated."))

L.append(cls("mental-canvas", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="medium",
    stage_cite="https://www.goodwinlaw.com/en/news-and-events/news/2018/12/12_10-mental-canvas-wins-m12-ventures", entry_date="2018-12",
    country="US", country_src="web_verified", country_cite=ARC("mental-canvas"), city="New York", focus="SaaS",
    note="3D sketching software (Julie Dorsey). Winner of the Female Founders Competition that M12 ran with EQT Ventures and SVB: $2M of funding (Dec 2018; Goodwin), "
         "the same instrument as Acerta's; Seed by instrument. Graduation judged in the surfaces pass."))

L.append(cls("meridian", status="private", rng="below_1b", stage="Seed", stage_src="model", stage_conf="low", entry_date="2025-02",
    **site_c("meridian", "NL"), focus="Fintech & Payments", flags=["model_disputes_source", "city_unknown", "stage_uncited"],
    note="Instant international payments network (Will Haering, Bradley Riss). 'Meridian Raises $15M' (EQT Ventures' own announcement, Feb 2025; site: EQT Ventures III, "
         "2024), a round deal databases call a seed and no press names: model at low. The firm's Key Facts say the Netherlands, others call it US-based; city unknown. "
         "The deterministic 'acquired / RU' pre-fill joined another Meridian. Graduation judged in the surfaces pass."))

L.append(cls("moonscale", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=S("using-ai-to-close-sales"), entry_date="2024-09", **site_c("moonscale", "DE"), focus="AI & Applied AI", flags=["city_unknown"],
    note="AI sales avatars (VidLab7, renamed Moonscale). 'EQT Ventures is invested -- leading the company's Seed financing!' (the firm's post, 2024-09-17). "
         "Graduation judged in the surfaces pass (entry just past 24 months)."))

L.append(cls("mytomorrows", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="medium",
    stage_cite=A("tomorrows-company"), entry_date="2017-01", city="Amsterdam", focus="Healthcare & Bio",
    note="Access to drugs in development. 'myTomorrows announces a EUR 10m growth funding round, co-led by EQT Ventures and Octopus Ventures, with participation from existing "
         "investors Balderton Capital and Sofinnova' (the firm's post, 2017-01-09): the firm's own round word, after Balderton's earlier round."))

L.append(cls("nectarine-health", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=A("aifloo-raises"), entry_date="2017-09", **arc_c("nectarine-health", "SE"), city="Stockholm", focus="Healthcare & Bio",
    note="AI wristband monitoring for elderly care: Aifloo (2017), renamed Noomi (2018) and Nectarine Health (2019). 'The A round was secured from the EQT Ventures fund' "
         "(EUR 5.1M; the firm's post, 2017-09-05). acq. by Brighter AB, 2020; the subsidiary filed for bankruptcy in Oct 2022 (Brighter's release)."))

L.append(cls("odyssey", status="private", rng="1b_plus", usd=1450000000, val_src="web_verified",
    val_cite="https://techcrunch.com/2026/06/17/world-model-maker-odyssey-nabs-1-45b-valuation-backed-by-amazon-and-other-big-names/", asof="2026-06-17",
    stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.maginative.com/article/odyssey-raises-18m-to-build-ai-worlds-using-backpack-mounted-cameras/", entry_date="2024-12",
    country="US", country_src="web_verified", country_cite=SITE("odyssey"), city="Palo Alto", focus="AI & Applied AI", flags=["model_disputes_source"],
    note="AI world models (Oliver Cameron, Jeff Hawke). $18M Series A led by EQT Ventures with GV and Air Street (Maginative; site: EQT Ventures III, 2024). $310M Series B at "
         "$1.45B (TechCrunch, 2026-06-17). Headquartered in Palo Alto with teams in San Francisco and London; the Form D-era GB country pre-fill is replaced."))

L.append(cls("pactio", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=S("investment-in-pactio"), entry_date="2024-04", **arc_c("pactio", "GB"), city="London", focus="Fintech & Payments",
    note="Infrastructure for private-markets transactions. 'Today, we're thrilled to lead Pactio's $14 million Series A round' (the firm's post, 2024-04-10)."))

L.append(cls("paid", status="private", rng="below_1b", stage="Pre-Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=S("paid-s-10m-pre-seed"), entry_date="2025-03", **site_c("paid", "GB"), city="London", focus="AI & Applied AI",
    flags=["model_disputes_source"],
    note="Billing and monetisation for AI agents (Manny Medina). 'a EUR 10 million pre-seed funding round led by EQT Ventures and Sequoia Capital' (the firm's post, "
         "2025-03-25); $21M seed Sep 2025. The public-float pre-fill joined an unrelated SEC registrant: the company is private."))

L.append(cls("siilo", status="acquired", rng="below_1b", stage="Seed", stage_src="model", stage_conf="low", entry_date="2018-10",
    grad="graduated", grad_src="web_verified", grad_cite="https://techround.co.uk/news/amsterdam-based-siilo-raises-a-10-5-million-series-a/",
    **arc_c("siilo", "NL"), city="Amsterdam", focus="Healthcare & Bio", flags=["stage_uncited"],
    note="Secure messaging for healthcare professionals. EQT Ventures led a EUR 4.5M round in 2018 (the firm's post, 2018-10-04), which no source names; the named $10.5M "
         "Series A led by Heal Capital with EQT (Sep 2020, TechRound) graduates it. acq. by Doctolib, 2023."))

L.append(cls("single-earth", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://tech.eu/2021/07/07/forest-tokenisation-platform-single-earth-raises-7-9-million/", entry_date="2021-07",
    **arc_c("single-earth", "EE"), city="Tallinn", focus="Climate & Energy",
    note="Nature-backed tokens and carbon and biodiversity credits. $7.9M seed led by EQT Ventures (Jul 2021, Tech.eu). Graduation judged in the surfaces pass."))

L.append(cls("stacks", status="private", rng="below_1b", stage="Pre-Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=S("investment-in-stacks"), entry_date="2025-02", **site_c("stacks", "NL"), city="Amsterdam", focus="Fintech & Payments",
    note="AI for the financial close (Albert Malikov, ex-Plaid). 'We're excited to lead this pre-seed round' (the firm's post, 2025-02-19)."))

L.append(cls("starcloud", status="private", rng="1b_plus", usd=1100000000, val_src="web_verified", val_cite=W("Starcloud"), asof="2026-03-30",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=W("Starcloud"), entry_date="2026-03",
    city="Redmond", focus="Data Infrastructure",
    note="Data centres in orbit (YC). 'On March 30, 2026, Starcloud announced that it had raised a $170M Series A at a $1.1bn valuation led by Benchmark and EQT Ventures' "
         "(Wikipedia); the fund's first check (site Entry 2026; the page names no fund). A later round reported at $3.3B with Nvidia, Cisco and Benchmark is not dated "
         "on disk, so the Series A mark stands; the A/B pass re-checks."))

L.append(cls("strawberry", status="private", rng="below_1b", stage="Pre-Seed", stage_src="web_verified", stage_conf="medium",
    stage_cite="https://nordic9.com/news/strawberry-browser-raised-6-million-in-a-pre-seed-deal-backed-by-general-catalyst-eqt-ventures-and-angel-investors/",
    entry_date="2025-10", country="SE", country_src="web_verified", country_cite="https://siliconcanals.com/strawberry-raises-e5-1m/", city="Stockholm",
    focus="AI & Applied AI", flags=["model_disputes_source"],
    note="AI agent browser. $6M led by General Catalyst and EQT Ventures (Oct 2025, Tech.eu), a pre-seed in Nordic9. Stockholm-founded; the Wikidata DK is a wrong join."))

L.append(cls("verto-analytics", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=A("verto-analytics"), entry_date="2016-05", **arc_c("verto-analytics", "FI"), city="Helsinki", focus="Data Infrastructure",
    note="Cross-device audience measurement. EQT Ventures led the $16.1M Series B (the firm's post, 2016-06-01). acq. by DISQO, 2021 (DISQO's release, 2021-06-15)."))

L.append(cls("voila", status="private", rng="below_1b", stage="undetermined", **arc_c("voila", "DE"), city="Berlin",
    focus="Consumer & Marketplaces",
    note="Restaurant meals delivered nationwide (getvoila). EQT Ventures led the EUR 8.8M round of Feb 2022 with FoodLabs and Shio (EU-Startups; the firm's 2022 review); no "
         "source names the round."))

L.append(cls("wildhero", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=S("on-eqt-ventures-investment-in-treecard"), entry_date="2021-02", **site_c("wildhero", "GB"), city="London",
    focus="Fintech & Payments",
    note="Wooden debit card that plants trees (TreeCard, now Wildhero: the page links treecard.org). The firm's post of 2021-02-25 announces its $5.12M seed, led by EQT "
         "Ventures. The firm's Exit 2025. Graduation judged in the surfaces pass."))

L.append(cls("willa-pay", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.finsmes.com/2020/06/willa-raises-3m-in-seed-funding.html", entry_date="2020-06",
    **arc_c("willa-pay", "SE"), city="Stockholm", focus="Fintech & Payments",
    note="Instant payment for freelancers (Willa Pay). $3M seed led by EQT Ventures (Jun 2020, FinSMEs); co-headquartered in Stockholm and Venice, California. "
         "Graduation judged in the surfaces pass."))

L.append(cls("wonder", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.finsmes.com/2020/12/wonder-raises-11m-in-seed-funding.html", entry_date="2020-12",
    country="DE", country_src="web_verified", country_cite=ARC("wonder"), city="Berlin", focus="SaaS", flags=["model_disputes_source"],
    note="Spatial video rooms for online events (wonder.me, founded as Yotribe). $11M seed led by EQT Ventures with BlueYard (Dec 2020, FinSMEs; TechCrunch). The US country "
         "pre-fill is a wrong join. Graduation judged in the surfaces pass."))

L.append(cls("ylookup", status="private", rng="below_1b", stage="Pre-Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://nordic9.com/news/ylookup-closed-a-3-million-pre-seed-round-led-by-eqt-ventures/", entry_date="2026-01",
    **site_c("ylookup", "GB"), city="London", focus="AI & Applied AI",
    note="Agentic workflow engine for tax, audit and advisory. $3M pre-seed led by EQT Ventures (Jan 2026, Nordic9; EQT Ventures' own announcement)."))

L.append(cls("bluebook", status="private", rng="below_1b", stage="undetermined",
    country="SE", country_src="web_verified", country_cite=S("eqt-ventures-backs-bluebook"), city="Stockholm", focus="AI & Applied AI",
    note="AI co-pilot for accountants (20+ pilots with 8 of Sweden's top 10 firms at announcement). EQT Ventures signed a term sheet 'within hours of our first meeting' "
         "(the firm's post, 2025-02-13); the round is not named."))

jl.write("batch-003", L)
