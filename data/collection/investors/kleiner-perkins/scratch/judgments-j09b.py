"""Judge j09, batch 18 (PRO-99 Kleiner Perkins): classification of the listed members precept .. solasta. Every row
was already a member on the firm's own listing (live site or the kpcb.com archive), so each takes one classification
line. Sources read in this pass: the firm's posts on disk, Wikipedia extracts (wikifetch.py), stockanalysis.com
market-cap and profile pages (curl), company releases and press read with WebFetch, sibling books' rows (rule 10),
two web searches (Reevo; the Optic one was spent on batch 17) and Google News through nq.py (throttled: queued
queries that had not returned are named in the notes)."""
import json
import os
from pathlib import Path

import judge_lib as jl

POSTS = {p["slug"]: p["url"] for p in jl._POSTS}


def POSTX(slug):
    return POSTS[slug]


A = jl.ARCH
W = jl.W
R = jl.rnd
L = []

# ---- URLs read in this pass (WebFetch or curl; each page says what is cited)
PROFOUND_TC = ("https://techcrunch.com/2026/09/15/aeo-startup-profound-hits-unicorn-valuation-raises-180m-series-d-"
               "7-months-after-last-round/")
SAIL_PRN = ("https://www.prnewswire.com/news-releases/sail-research-raises-80-million-to-build-max-efficiency-"
            "infrastructure-for-ai-agents-302810497.html")
SARONIC_PRN = ("https://www.prnewswire.com/news-releases/saronic-closes-1-75b-series-d-at-9-25b-valuation-to-"
               "accelerate-a-new-era-of-maritime-autonomy-302729238.html")
ROGO_TR = "https://www.tipranks.com/news/private-companies/rogo-raises-160-million-series-d-at-2-billion-valuation"
SIERRA_YF = "https://finance.yahoo.com/markets/stocks/articles/sierra-raises-950m-15-8b-154125641.html"
QMCO_CAP = "https://stockanalysis.com/stocks/qmco/market-cap/"
JIANPU_CAP = "https://stockanalysis.com/quote/otc/AIJTY/market-cap/"
JIANPU_CO = "https://stockanalysis.com/quote/otc/AIJTY/company/"
PUPPET_TC = ("https://techcrunch.com/2011/11/29/cisco-google-ventures-vmware-put-8-5m-in-data-center-automation-"
             "startup-puppet-labs/")
SECRET_TC = "https://techcrunch.com/2013/12/06/secret/"
REEVO_SSM = ("https://startupstorymedia.com/khosla-ventures-leads-80-million-funding-round-for-ai-startup-reevo-"
             "valued-at-500-million/")
RMG_S1 = jl.FTS("RMG Networks", "S-1")

# ---- momentum checks through nq.py: read what came back (the queue may not have reached a row)
_HERE = Path(__file__).resolve().parent
_NX = json.loads((_HERE / "news-extra-j09.json").read_text()) if (_HERE / "news-extra-j09.json").exists() else {}


def seen(slug):
    return [i for i in _NX.get(slug, []) if i.get("names")]


def checked(slug):
    its = seen(slug)
    return (f"Google News (nq.py, 2026-09-30) returned {len(its)} headline(s) naming the company, none a $1B round"
            if slug in _NX else "the queued Google News check (nq.py) had not returned")


# ---- KPCB China listing rows (X1 provisional IN, flagged)
for slug, city, focus, what, extra_note in [
        ("pvnext", None, "Climate & Energy", "PVNext, a Taiwanese CIGS thin-film solar cell maker",
         " The 2010 China listing's 'Solar Thin Film Company (stealth company)' row, with the same description and "
         "location, is this company under its stealth name; the two rows should merge."),
        ("solar-thin-film-company-stealth-company", None, "Climate & Energy",
         "a Taiwanese CIGS thin-film solar cell maker in stealth, listed with location 'Taiwan'",
         " It is PVNext (the pvnext row: same description, partner Wen Hsieh's China-greentech page); the two rows "
         "should merge."),
        ("rrlt", None, "Consumer & Marketplaces", "RRLT, an online recruitment platform", ""),
        ("scinor-water", "Beijing", "Climate & Energy", "Scinor Water, membrane water treatment", ""),
        ("sinoev", None, "Climate & Energy", "SinoEV, an electric-vehicle powertrain supplier", ""),
        ("sinosun", "Shenzhen", "Security",
         "SinoSun, secure ID and authentication products for Chinese banks (listing location 'Shenzhen, China')", ""),
        ("sinowel", None, "Fintech & Payments",
         "Sinowel, third-party telemarketing of insurance and wealth-management products (partners Tina Ju and Xin "
         "Tang; not one of the pre-2007 TDF deals)", "")]:
    cc = "TW" if slug in ("pvnext", "solar-thin-film-company-stealth-company") else "CN"
    kw = dict(city=city, city_src="model_knowledge") if city else {}
    L.append(jl.cls(slug, status="unknown", rng="below_1b", stage="undetermined", rounds=[],
        country=cc, country_src="web_verified", country_cite=A(slug), focus=focus,
        flags=("kpcb_china",) + (() if city else ("city_unknown",)), **kw,
        note=f"KPCB China holding (X1, provisional IN): {what}, on the firm's China listing or its 2012-14 company "
             "pages under Teams China. No source read gives its fate, its city or the round KPCB China entered, so "
             "status unknown and stage undetermined." + extra_note))

L.append(jl.cls("rong360", status="public", rng="below_1b", usd=18_420_000, val_src="web_verified",
    val_cite=JIANPU_CAP, asof="2026-09-30", stage="undetermined", rounds=[],
    country="CN", country_src="web_verified", country_cite=JIANPU_CO, city="Beijing", city_src="web_verified",
    focus="Fintech & Payments", flags=("kpcb_china",),
    note="Rong360, the Chinese loan-recommendation platform, now Jianpu Technology (Rong360 brand), headquartered in "
         "Beijing and quoted over the counter as AIJTY after its NYSE listing: market cap $18.42M on 2026-09-30 "
         "(stockanalysis). The firm's 2014 page names Wei Zhou, a KPCB China partner, so the position is read as "
         "KPCB China's (X1 flag). The round KPCB China entered is not cited."))

# ---- the rest of the batch
L.append(jl.cls("precept", status="acquired", rng="below_1b", stage="undetermined", entry_date="1995", rounds=[],
    country="US", city="Palo Alto", focus="Data Infrastructure",
    note="Precept Software, IP multicast video streaming (Palo Alto); the firm dates its entry 1995 and records the "
         "exit to Cisco (1998). The round is not on record."))

L.append(jl.cls("presto", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="Mountain View", focus="Consumer & Marketplaces", flags=("model_disputes_source",),
    note="Presto (Presto Services, Mountain View): email and photos delivered to an HP printing mailbox for people "
         "without computers. The pre-filled 'acquired' status, acquirer Foxtel and AU country belong to the "
         "Australian streaming service of the same name, disputed. No source read gives this company's fate or the "
         "round. The USV (Seed, Climate & Energy) and YC (SF SaaS) Presto rows are other companies."))

L.append(jl.cls("primus-power", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
    city="Hayward", focus="Climate & Energy",
    note="Primus Power, zinc-bromine flow batteries for grid storage (Hayward CA), on the firm's 2012-15 greentech "
         "pages (Bill Joy, David Wells). Its site did not load cleanly (certificate error, 2026-09-30) and no source "
         "read gives its present state or the round."))

L.append(jl.cls("profound", status="private", rng="1b_plus", usd=1_800_000_000, val_src="web_verified",
    val_cite=PROFOUND_TC, asof="2026-09-15",
    stage="Series A", stage_src="first_party",
    stage_cite=POSTX("profound-brand-visibility-for-the-generative-internet"), stage_conf="high",
    entry_date="2025-06",
    rounds=[R("2025-06-18", "Series A", None, "Kleiner Perkins", True,
              POSTX("profound-brand-visibility-for-the-generative-internet"), "firm"),
            R("2026-02", "Series C", 96_000_000, None, None, PROFOUND_TC, "press"),
            R("2026-09-15", "Series D", 180_000_000, "Sequoia; Kleiner Perkins", True, PROFOUND_TC, "press")],
    country="US", city="New York", focus="AI & Applied AI", extra={"valuation_range_source": "web_verified"},
    note="Profound, AI search visibility for brands, New York. The firm's post of 2025-06-18 says it led the Series A "
         "(the since-year is 2025). TechCrunch (2026-09-15): a $180M Series D at $1.8B co-led by Sequoia and "
         "Kleiner Perkins, seven months after a $96M Series C. The Lightspeed and Sequoia rows still read below_1b; "
         "this mark is fresher (Sequoia's own stage citation) and they should align. Momentum slice: the mark is the "
         "check."))

L.append(jl.cls("proxy", status="acquired", rng="below_1b", stage="Series A", stage_src="first_party",
    stage_cite=POSTX("reinventing-digital-identity-for-the-physical-world"), stage_conf="medium",
    entry_date="2019-03",
    rounds=[R("2019-03-27", "Series A", None, None, True,
              POSTX("reinventing-digital-identity-for-the-physical-world"), "firm")],
    country="US", city="San Francisco", focus="Security",
    note="Proxy (Denis Mars, Simon Ratner), digital identity for physical access, San Francisco. The firm's post of "
         "2019-03-27 announces 'Kleiner Perkins' Series A investment in Proxy'; no earlier Kleiner Perkins round is "
         "known. Oura bought it in an all-equity deal in 2023 (aligned with the YC row)."))

L.append(jl.cls("puppet", city="Portland", rng="below_1b", stage="undetermined",
    rounds=[R("2011-11-29", "Series C", 8_500_000, "Cisco; Google Ventures; VMware", True, PUPPET_TC, "press")],
    focus="DevTools & APIs",
    note="Puppet (Puppet Labs), infrastructure automation, Portland OR; bought by Perforce in 2022. TechCrunch "
         "(2011-11-29): Kleiner Perkins was already an investor when Cisco, Google Ventures and VMware led the $8.5M "
         "Series C ($16M raised in all), so it entered at the A or the B, and no source read says which."))

L.append(jl.cls("quantum", status="public", rng="1b_plus", usd=1_250_000_000, val_src="web_verified",
    val_cite=QMCO_CAP, asof="2026-09-30", stage="undetermined", rounds=[],
    country="US", city="San Jose", focus="Data Infrastructure", flags=("model_disputes_source",),
    extra={"valuation_range_source": "web_verified"},
    note="Quantum Corporation (mass storage, founded 1980, San Jose; Wikipedia), still listed on Nasdaq as QMCO: "
         "market cap $1.25B on 2026-09-30 (stockanalysis). The pre-filled 'acquired' and DE came from a homonym "
         "join, disputed. The EDGAR hits on the row (Quantum Fuel Systems, QuantumScape) are other companies. The "
         "round the firm entered is not on record."))

L.append(jl.cls("quickturn-design-systems", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="San Jose", focus="Industrial & Robotics",
    note="Quickturn Design Systems, hardware emulation for chip design; public, then acquired by Cadence in 1999 "
         "(Wikipedia, Cadence). The round the firm entered is not on record."))

L.append(jl.cls("qume", status="acquired", rng="below_1b", stage="undetermined", entry_date="1974", rounds=[],
    country="US", city="San Jose", focus="Industrial & Robotics",
    note="Qume, daisy-wheel printers, founded 1973 by David S. Lee and Robert Schroeder; ITT bought it for $164M in "
         "1978 (Wikipedia). The firm dates its entry 1974; the round is not named. The archive tile's label "
         "'Ascend Communications' is a parse slip of the logo grid. Aligned with Sutter Hill's row."))

L.append(jl.cls("quorum-systems", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="San Diego", focus="Industrial & Robotics",
    note="Quorum Systems, multi-mode radio transceiver chips (San Diego, the firm's 2008-10 listing); bought by "
         "Spreadtrum around 2007-08 (Greylock's row, aligned). The round is not on record."))

L.append(jl.cls("rapid-robotics", status="private", rng="below_1b", stage="Growth", stage_src="first_party",
    stage_cite=POSTX("rapid-robotics"), stage_conf="high", entry_date="2021-08",
    rounds=[R("2021-08-18", "Series B", None, "Kleiner Perkins (co-lead)", True, POSTX("rapid-robotics"), "firm")],
    country="US", city="San Francisco", focus="Industrial & Robotics",
    note="Rapid Robotics, ready-to-deploy manufacturing robots, San Francisco. The firm's post of 2021-08-18 says it "
         "co-led the Series B; the $12M Series A of April 2021 was NEA's (NEA's row), and the firm's listings begin "
         "in 2022, so the entry is the B (Growth). Still operating per NEA's row."))

for slug, dup in [("recyclebank", ""),
                  ("recycle-rewards-inc", " Recycle Rewards, Inc. is RecycleBank's legal name (the 2012-18 page's "
                   "own text calls it Recyclebank); the two rows should merge.")]:
    L.append(jl.cls(slug, status="acquired", rng="below_1b", stage="undetermined", rounds=[],
        country="US", city="New York", focus="Climate & Energy",
        note="RecycleBank (Recycle Rewards, Inc.), recycling rewards for households, New York (Wikipedia; the "
             "firm's 2008-10 listing, New York City). Bought by Recycle Track Systems in 2019. On the firm's "
             "greentech list with Trae Vassallo; the round the firm entered is not cited." + dup))

L.append(jl.cls("reevo", status="private", rng="below_1b", stage="Series A", stage_src="first_party",
    stage_cite=POSTX("reevo-the-intelligent-revenue-operating-system"), stage_conf="medium", entry_date="2025-11",
    rounds=[R("2025-11-05", "Seed and Series A (combined)", 80_000_000, "Khosla Ventures; Kleiner Perkins", True,
              REEVO_SSM, "press")],
    country="US", focus="AI & Applied AI", flags=("city_unknown",),
    extra={"valuation_range_source": "web_verified", "valuation_citation": REEVO_SSM, "valuation_asof": "2025-11-06"},
    note="Reevo, an AI-native revenue operating system, incubated by Khosla Ventures. Startup Story Media "
         "(2025-11-06): $80M in combined seed and Series A led by Khosla and Kleiner Perkins at a $500M valuation; "
         "the firm's own post (2025-11-05) says it co-led the Series A, so the entry is the A. Momentum check "
         "2026-09-30 (web search and the company's release): the $500M mark is the latest; no $1B round."))

L.append(jl.cls("rgb-networks", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="Sunnyvale", focus="Data Infrastructure",
    note="RGB Networks, IP video processing and delivery (the firm's 2008-10 listing says San Mateo; later "
         "Sunnyvale, aligned with IVP's row); acquired by Imagine Communications in 2014. The round is not on "
         "record."))

L.append(jl.cls("ripcord", status="private", rng="below_1b", stage="undetermined", rounds=[],
    city="Hayward", focus="Industrial & Robotics",
    note="Ripcord, robotic digitisation of paper records, Hayward CA; on the firm's lists from 2017 and still "
         "operating (GV's row: a 2023 round and a 2026 facility release). No source read names the round Kleiner "
         "Perkins entered."))

L.append(jl.cls("rlc", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
    country="IN", country_src="web_verified", country_cite=A("rlc"), focus="Industrial & Robotics",
    flags=("city_unknown",),
    note="RLC (Reverse Logistics Company), which the firm's 2012 page calls 'India's largest technology enabled, "
         "comprehensive reverse supply chain company'. No source read gives its city, fate or the round."))

L.append(jl.cls("rmg-networks", city="Dallas", rng="below_1b", stage="undetermined", focus="Media, Gaming & Advertising",
    rounds=[R("2006", "founding financing (as Danoo)", None, None, True, W("RMG Networks"), "press")],
    note="RMG Networks (Reach Media Group, founded 2006 as Danoo with backing from Kleiner Perkins, DAG, National "
         "CineMedia and Tennenbaum; Wikipedia, now Korbyt, Dallas). The firm's 'Merged' status is RMG's 2013 merger "
         "into the SCG Financial SPAC, in which KPCB Holdings took stock as a former RMG stockholder (2014 S-1, "
         + RMG_S1 + "): RMG is the company the fund held (R5), not an acquirer. Taken private by Virgo and Sachs "
         "Capital in 2018. The round is not named."))

L.append(jl.cls("roadrunner", status="private", rng="below_1b", stage="Seed", stage_src="first_party",
    stage_cite=POSTX("roadrunner-the-new-revenue-infrastructure"), stage_conf="high", entry_date="2025",
    grad="graduated", grad_src="first_party", grad_cite=POSTX("roadrunner-the-new-revenue-infrastructure"),
    grad_conf="high",
    rounds=[R("2025", "Seed", None, "Kleiner Perkins", True, POSTX("roadrunner-the-new-revenue-infrastructure"), "firm"),
            R("2026-05", "Series A", None, "Founders Fund", True, POSTX("roadrunner-the-new-revenue-infrastructure"),
              "firm")],
    country="US", focus="AI & Applied AI", flags=("city_unknown",),
    note="Roadrunner (Joubin Mirzadegan), AI revenue infrastructure. The firm's post of 2026-05-12: 'we incubated "
         "the company and led the seed', and Founders Fund led the Series A, which graduates the row; the seed is "
         "dated by the firm's since-year, 2025. Momentum check: " + checked("roadrunner") + "; the company's site "
         "(2026-09-30) names Founders Fund and Kleiner Perkins and no valuation. Headline's Roadrunner (Pittsburgh, "
         "climate) is another company."))

L.append(jl.cls("rogo", status="private", rng="1b_plus", usd=2_000_000_000, val_src="web_verified",
    val_cite=ROGO_TR, asof="2026-04-29", stage="Growth", stage_src="web_verified", stage_cite=ROGO_TR,
    stage_conf="high", entry_date="2026-04-29",
    rounds=[R("2026-04-29", "Series D", 160_000_000, "Kleiner Perkins", True, ROGO_TR, "press")],
    country="US", city="New York", focus="AI & Applied AI", extra={"valuation_range_source": "web_verified"},
    note="Rogo, AI agents for investment banks, New York. TipRanks (2026-04-29): a $160M Series D at $2B led by "
         "Kleiner Perkins with Sequoia, Thrive, J.P. Morgan and Khosla; the firm's own post says it led the Series D "
         "and its since-year is 2026, so the D is the entry (Growth). Aligned with Tiger Global's mark; the Sequoia "
         "and Thrive rows still read below_1b. Momentum slice: the mark is the check."))

L.append(jl.cls("sail-research", status="private", rng="below_1b", stage="Series A", stage_src="web_verified",
    stage_cite=SAIL_PRN, stage_conf="high", entry_date="2026-06-25",
    rounds=[R("2026-06-25", "Seed", None, "Sequoia", None, SAIL_PRN, "company"),
            R("2026-06-25", "Series A", None, "Kleiner Perkins", True, SAIL_PRN, "company")],
    country="US", city="San Francisco", city_src="web_verified", focus="AI & Applied AI",
    extra={"valuation_range_source": "web_verified", "valuation_citation": SAIL_PRN, "valuation_asof": "2026-06-25"},
    note="Sail Research, serving and sandboxes for long-horizon AI agents, San Francisco. The company's release of "
         "2026-06-25: $80M in seed and Series A at a $450M valuation, the Series A led by Kleiner Perkins and the "
         "seed by Sequoia, so the firm entered at the A. Momentum check 2026-09-30: the $450M mark is the latest; "
         "no $1B round."))

L.append(jl.cls("saronic-technologies", status="private", rng="1b_plus", usd=9_250_000_000, val_src="web_verified",
    val_cite=SARONIC_PRN, asof="2026-03-31", stage="Growth", stage_src="web_verified", stage_cite=SARONIC_PRN,
    stage_conf="high", entry_date="2026-03-31",
    rounds=[R("2026-03-31", "Series D", 1_750_000_000, "Kleiner Perkins", True, SARONIC_PRN, "company")],
    country="US", city="Austin", city_src="web_verified", focus="Industrial & Robotics",
    extra={"valuation_range_source": "web_verified"},
    note="Saronic Technologies, autonomous surface vessels, Austin TX. The company's release of 2026-03-31: a $1.75B "
         "Series D at a $9.25B valuation led by Kleiner Perkins; the firm's since-year is 2026, so the D is the "
         "entry (Growth). Mark aligned with the 8VC, a16z, General Catalyst and Lightspeed rows."))

L.append(jl.cls("scintera-networks", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="San Jose", focus="Industrial & Robotics",
    note="Scintera Networks, CMOS signal-processing chips for communications (San Jose); acquired by Maxim "
         "Integrated in 2014. Listed with Doug Mackenzie; the round is not on record."))

L.append(jl.cls("scs", status="acquired", rng="below_1b", stage="undetermined", entry_date="1982", rounds=[],
    country="US", city="San Jose", focus="Industrial & Robotics",
    note="SCS (Silicon Compiler Systems), logic synthesis and chip-design tools; the firm dates its entry 1982 and "
         "records the exit to Mentor Graphics. The round is not on record."))

L.append(jl.cls("secret", status="defunct", rng="below_1b", stage="Seed", stage_src="web_verified",
    stage_cite=SECRET_TC, stage_conf="high", entry_date="2013-12-06",
    grad="graduated", grad_src="web_verified", grad_cite=W("Secret (app)"), grad_conf="high",
    rounds=[R("2013-12-06", "Seed", 1_200_000, None, True, SECRET_TC, "press"),
            R("2014-03", "Series A", 8_600_000, None, None, W("Secret (app)"), "press"),
            R("2014-07-14", "Series B", 25_000_000, None, None, W("Secret (app)"), "press")],
    country="US", city="San Francisco", focus="Consumer & Marketplaces",
    note="Secret, the anonymous sharing app (David Byttow, Chrys Bader-Wechseler), San Francisco. TechCrunch "
         "(2013-12-06): the $1.2M seed from the Form D included KPCB, Google Ventures and Alexis Ohanian (Megan Quinn "
         "carried it at the firm). Wikipedia: an $8.6M Series A in March 2014 (graduated) and a $25M Series B in "
         "July 2014; Byttow shut the company down on 2015-04-29. Aligned with GV and Redpoint."))

L.append(jl.cls("secured", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
    country="GB", city="London", focus="Consumer & Marketplaces",
    note="Secured (formerly BUMP), tools for sneaker and NFT collectors: the firm's 2025-26 consumer tile links "
         "secured.community, the domain of YC's W18 company of that name (London, marked Inactive in YC's "
         "directory). The domain has expired (2026-09-30). Country and city aligned with the YC row from its "
         "directory record; the round Kleiner Perkins entered is not on record."))

L.append(jl.cls("sequent-computer-systems", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="Beaverton", focus="Data Infrastructure", flags=("model_disputes_source",),
    note="Sequent Computer Systems, multiprocessor servers, Beaverton OR; IBM bought it in 1999 for $810M "
         "(Wikipedia). The pre-filled 'defunct' read that purchase as a dissolution, disputed (COLLECTION.md s6; "
         "aligned with IVP). The round is not on record."))

L.append(jl.cls("settle", status="private", rng="below_1b", stage="Series A", stage_src="first_party",
    stage_cite=POSTX("settle-series-a"), stage_conf="medium", entry_date="2021-05",
    rounds=[R("2021-05-18", "Series A", None, "Kleiner Perkins", True, POSTX("settle-series-a"), "firm")],
    country="US", city="San Francisco", focus="Fintech & Payments",
    note="Settle, payables and financing for consumer brands, San Francisco. The firm's post of 2021-05-18 says it "
         "led the Series A; its listings begin in 2021 and no earlier Kleiner Perkins round is known. Momentum "
         "check: " + checked("settle") + "; Ribbit's row records an August 2021 round at about $600M and no $1B "
         "round (news sweep 2026-09-28)."))

L.append(jl.cls("shiva", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="Bedford", focus="Data Infrastructure",
    note="Shiva Corporation, remote-access equipment (founded 1985 in Cambridge MA, later Bedford); acquired by "
         "Intel in October 1998 (Wikipedia). Aligned with Greylock's row. The round is not on record."))

L.append(jl.cls("shoof-technologies", status="unknown", rng="undetermined", stage="undetermined", grad="undetermined",
    flags=("identity_unresolved",),
    note="Shoof Technologies, on the firm's 2018-21 enterprise tiles only; shooftech.com now carries an unrelated "
         "casino-review page (2026-09-30) and no source read says what the company did or where it was."))

L.append(jl.cls("siara-systems", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="Mountain View", focus="Data Infrastructure",
    note="Siara Systems, metro optical and IP networking equipment (Mountain View), acquired by Redback Networks in "
         "1999; Redback later went to Ericsson, which is why the firm's tile links ericsson.com. The round is not on "
         "record."))

L.append(jl.cls("sierra", status="private", rng="10b_plus", usd=15_800_000_000, val_src="web_verified",
    val_cite=SIERRA_YF, asof="2026-05-04", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2025",
    rounds=[R("2026-05-04", "Series E", 950_000_000, "Tiger Global; GV", None, SIERRA_YF, "press")],
    country="US", city="San Francisco", focus="AI & Applied AI", extra={"valuation_range_source": "web_verified"},
    note="Sierra (Bret Taylor, Clay Bavor), customer-service AI agents, San Francisco. The firm dates its entry 2025; "
         "every Sierra round from late 2024 on was a later-stage round (the September 2025 $350M at $10B led by "
         "Greenoaks), so a 2025 entry is Growth, but no source read names Kleiner Perkins in a round. Yahoo Finance "
         "(2026-05-04): $950M led by Tiger Global and GV at $15.8B; aligned with the GV, ICONIQ, Sequoia, Thrive "
         "and Tiger rows. Momentum slice: the mark is the check."))

L.append(jl.cls("signal", status="acquired", rng="below_1b", stage="undetermined", entry_date="1993", rounds=[],
    country="US", city="San Diego", focus="Healthcare & Bio",
    note="Signal Pharmaceuticals, cancer drug discovery (San Diego); the firm dates its entry 1993 and records the "
         "exit to Celgene (2000). Lightspeed's 'Signal' row (Seed) is another company."))

L.append(jl.cls("silecs-inc", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="Mountain View", focus="Industrial & Robotics",
    note="Silecs, dielectric materials for chips and flat-panel displays, Mountain View (the firm's 2008-10 "
         "listing), with Vinod Khosla (a seat from his Kleiner Perkins years). No source read gives its fate or the "
         "round."))

L.append(jl.cls("silicon-spice", status="acquired", rng="below_1b", stage="undetermined", entry_date="1998",
    rounds=[], country="US", city="Mountain View", focus="Industrial & Robotics",
    note="Silicon Spice, DSP chips for broadband communications (Mountain View); the firm dates its entry 1998 and "
         "records the exit to Broadcom (2000). Aligned with NEA's row. The round is not on record."))

L.append(jl.cls("singularity-network", status="unknown", rng="undetermined", stage="undetermined",
    grad="undetermined", flags=("identity_unresolved",),
    note="'Singularity Network' on the firm's 2020-26 alumni tiles links singularitynet.io (the SingularityNET AI "
         "token project), but no source ties Kleiner Perkins to that project and nothing else names the company, so "
         "the row cannot be identified."))

L.append(jl.cls("solasta", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="Newton", focus="Climate & Energy",
    note="Solasta, nano-structured solar cells (Newton MA), on the firm's 2013-18 greentech pages with Bill Joy. No "
         "source read gives its fate or the round."))

jl.write("j09b", L)
