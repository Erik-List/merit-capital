"""Judge j09, batch 17 (PRO-99 Kleiner Perkins): classification of the listed members novadigm .. power-computing,
and the P-Cube trap (not_member, X1). Every member here was already on the firm's own listing (live site or the
kpcb.com archive), so each takes one classification line. Sources read in this pass: the firm's posts on disk,
Wikipedia extracts (wikifetch.py), the Opower S-1 (secget.py), company pages and press releases read with WebFetch,
four web searches, and Google News through nq.py (throttled; most queued queries had not returned when this was
written, so rows they would have settled say so)."""
import judge_lib as jl

POSTS = {p["slug"]: p["url"] for p in jl._POSTS}


def POSTX(slug):
    return POSTS[slug]


A = jl.ARCH
W = jl.W
R = jl.rnd
L = []

# ---- URLs read in this pass with WebFetch (each page read and says what is cited)
OMNIFOLD_B = "https://omnifold.ai/blog/articles/series-b-investment-announcement"
PARALLEL_TC = "https://techcrunch.com/2026/04/29/parallel-web-systems-hits-2b-valuation-five-months-after-its-last-big-raise/"
PARALLEL_CAREERS = "https://parallel.ai/careers"
PACKAGD_TC = "https://techcrunch.com/2017/06/08/packagd-kpcb-forerunner-gv/"
PAIR_SEED = "https://hitconsultant.net/2020/12/09/pair-team-automate-primary-care-operations-funding/"
PAIR_A = ("https://www.prnewswire.com/news-releases/pair-team-raises-9-million-series-a-to-expand-access-to-health-care-"
          "services-for-medicaids-most-vulnerable-patients-301960920.html")
PATHLIGHT_A = ("https://www.globenewswire.com/news-release/2020/03/26/2007012/0/en/Pathlight-Aims-To-Transform-How-Teams-"
               "Are-Managed-Kleiner-Perkins-Leads-Series-A-With-7-Million.html")
ORCAN_SITE = "https://www.orcan-energy.com/"
OMNI_SITE = "http://www.omni-pharma.com"
ONELOGIN_TC = "https://techcrunch.com/2019/01/10/onelogin-snares-100m-investment-to-expand-identity-solution-into-new-markets/"
OPOWER_S1 = jl.FTS("OPOWER", "S-1")
OPTIC_SEED = "https://www.theblock.co/post/158678/nft-fraud-fighters-optic-raise-11-million-in-seed-funding-round"

# ---- X1 trap: Tina Ju's TDF Capital deal carried on the China listing
L.append(jl.verdict("p-cube", "not_member",
    "partner-carried: Tina Ju's TDF Capital deal before KPCB China (Erik 2026-09-17 partner-carried rule; "
    "decisions.md X1). P-Cube, the broadband traffic-management company Cisco bought in 2004, appears on the KPCB "
    "China listing as acquired by Cisco; no KPCB China fund round in it was found.",
    ec="site_listing", conf="high", cite=A("p-cube")))

# ---- KPCB China listing rows (X1 provisional IN, flagged)
for slug, city, focus, what in [
        ("nucom", "Beijing", "Media, Gaming & Advertising", "a Beijing sports and entertainment broadband portal"),
        ("one-wave", "Shanghai", "Media, Gaming & Advertising", "a Shanghai IPTV platform and broadband content provider"),
        ("oriental-wisdom", "Beijing", "Fintech & Payments",
         "a Beijing provider of wireless data applications for financial institutions")]:
    L.append(jl.cls(slug, status="unknown", rng="below_1b", stage="undetermined", rounds=[],
        country="CN", country_src="web_verified", country_cite=A(slug), city=city, city_src="web_verified",
        focus=focus, flags=("kpcb_china",),
        note=f"KPCB China holding (X1, provisional IN): {what}, on the firm's 2008-10 China listing (location "
             f"'{city}, China') and its 2012-14 company pages under Teams China. No source read gives its fate or the "
             "round KPCB China entered, so status unknown and stage undetermined."))

L.append(jl.cls("omni-pharmaceuticals", status="private", rng="below_1b", stage="undetermined", rounds=[],
    country="CN", country_src="web_verified", country_cite=OMNI_SITE, city="Shanghai", city_src="web_verified",
    focus="Healthcare & Bio", flags=("kpcb_china",),
    note="KPCB China holding (X1, provisional IN): the 2013-14 company page lists it under Teams China with partner "
         "James Huang. Its own site (Omni Pharma, inhalation drug delivery) carries a Shanghai ICP filing and 2024 "
         "regulatory news, so it operates; a 2024 'potential unicorn' award is not a mark. The round is not on record."))

L.append(jl.cls("origene-technologies", status="private", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="Rockville", focus="Healthcare & Bio", flags=("kpcb_china",),
    note="OriGene (cDNA clones and research reagents, Rockville MD, founded 1996; its site still operates). The firm's "
         "2013-14 page names James Huang, KPCB China's life-sciences partner, so the position is read as a KPCB China "
         "one and flagged for the X1 count; the round is not on record."))

# ---- the rest of the batch
L.append(jl.cls("novadigm", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
    country="US", focus="Healthcare & Bio", flags=("city_unknown",),
    note="NovaDigm Therapeutics (fungal and bacterial vaccines, the NDV-3 programme), on the firm's 2012 company page "
         "under Life Sciences. Its old domain now shows an unrelated telemedicine page (read 2026-09-30); no source "
         "read gives its fate, its city or the round the firm entered."))

L.append(jl.cls("ogin", status="defunct", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="Waltham", focus="Climate & Energy",
    note="Ogin, formerly FloDesign Wind Turbine (shrouded mixer-ejector wind turbines, Massachusetts), on the firm's "
         "2014-18 pages with Bill Joy, John Doerr and Jan van Dokkum. The company wound down around 2015-16 and its "
         "fdwt.com domain is parked for sale (checked 2026-09-30); the round the firm entered is not cited, so "
         "undetermined. Confidence on the status is medium."))

L.append(jl.cls("omio-formerly-goeuro", status="private", rng="below_1b", stage="Growth", stage_src="model",
    stage_conf="medium", entry_date="2015", country="DE", country_src="web_verified", country_cite=W("Omio"),
    city="Berlin", city_src="web_verified", focus="Consumer & Marketplaces",
    note="Omio (GoEuro until 2019), multimodal travel booking, headquartered in Berlin (Wikipedia). KPCB's growth team "
         "led GoEuro's 2015 round of about $70M, after the 2013-14 seed and first institutional rounds; Wikipedia "
         "names the 2018 $150M round the Series C, so the 2015 entry is a Series B (Growth). A Digital Growth Fund "
         "position is IN (D2). No priced mark at or above $1B is cited (2022 Series E of $80M)."))

L.append(jl.cls("omnifold", status="private", rng="below_1b", stage="undetermined",
    rounds=[R("2025", "Series A", None, None, None, "https://lsvp.com/company/omnifold/", "firm"),
            R("2026-06-26", "Series B", 30_000_000, None, True, OMNIFOLD_B, "company")],
    entry_date="2025", country="US", city="San Francisco", focus="AI & Applied AI",
    extra={"valuation_range_source": "web_verified", "valuation_citation": OMNIFOLD_B, "valuation_asof": "2026-06-26"},
    note="Omnifold, AI models trained per customer for supply-chain forecasting, San Francisco. The firm dates its "
         "entry 2025 (site since-year); Lightspeed's card says Series A 2025, but no source read names the round "
         "Kleiner Perkins entered, so undetermined. Momentum check 2026-09-30: the company's own post (2026-06-26) "
         "announces a $30M Series B at a $300M valuation, $60M raised in total, backed by Kleiner Perkins and "
         "Lightspeed; no $1B round. A Google News query returned nothing."))

L.append(jl.cls("on-technology", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="Waltham", focus="Data Infrastructure",
    note="ON Technology, founded 1987 by Mitch Kapor (network and desktop systems management software, "
         "Massachusetts); public, then acquired by Symantec on 2003-10-27 (Wikipedia). The round the firm entered is "
         "not on record."))

L.append(jl.cls("one-true-media-inc", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="Redwood City", focus="Consumer & Marketplaces",
    note="One True Media, online video and slideshow creation, Redwood City (the firm's 2008-10 listing). Its site "
         "no longer answers (2026-09-30) and no source read gives its fate or the round the firm entered."))

L.append(jl.cls("onelogin", status="acquired", rng="below_1b", stage="undetermined", entry_date="2013",
    rounds=[R("2018-06", "Series C", 22_500_000, None, None, ONELOGIN_TC, "press"),
            R("2019-01-10", "growth round", 100_000_000, "Greenspring Associates", None, ONELOGIN_TC, "press")],
    city="San Francisco", focus="Security",
    note="OneLogin, identity and access management, founded 2009 in San Francisco; acquired by One Identity on "
         "2021-10-04 (Wikipedia; the firm's exit line). The firm dates its entry 2013; TechCrunch's 2019 report of "
         "the $100M round does not name Kleiner Perkins and no source read names the 2013 round, so undetermined."))

for slug, dup in [("onfiber-communications-inc", ""),
                  ("onfiber-xa0communications-xa0inc",
                   " This row is the same company as onfiber-communications-inc (the 2012 page's name carries "
                   "stray non-breaking-space codes); the two should merge.")]:
    L.append(jl.cls(slug, status="acquired", rng="below_1b", stage="undetermined", rounds=[],
        country="US", city="Denver", focus="Data Infrastructure",
        note="OnFiber Communications, metro fiber-optic access networks, acquired by Qwest in 2006; the firm's "
             "2008-10 listing places it in Denver, Qwest's home. The round the firm entered is not on record." + dup))

L.append(jl.cls("onyx-pharmaceuticals", city="South San Francisco", stage="undetermined", entry_date="1992",
    rng="below_1b", focus="Healthcare & Bio",
    rounds=[R("1992", "formation financing", None, None, True, W("Onyx Pharmaceuticals"), "press")],
    note="Onyx Pharmaceuticals, South San Francisco; formed in 1992 with money from Chiron and the venture firms "
         "Avalon, IVP, J. H. Whitney and Kleiner Perkins (Wikipedia); IPO 1996, acquired by Amgen in 2013. The "
         "formation round is not named, so the stage is undetermined; below_1b as an acquired row."))

L.append(jl.cls("opcom", status="acquired", rng="below_1b", stage="undetermined", entry_date="1982", rounds=[],
    country="US", focus="Data Infrastructure", flags=("city_unknown",),
    note="Opcom, voice messaging systems; the firm dates its entry 1982 and records the exit as acquired by Octel. "
         "No source read gives the round or the company's city."))

L.append(jl.cls("open-raven", status="unknown", rng="below_1b", stage="Series A", stage_src="first_party",
    stage_cite=POSTX("open-raven_series_a"), stage_conf="medium", entry_date="2020-06",
    rounds=[R("2020-06-16", "Series A", None, "Kleiner Perkins", True, POSTX("open-raven_series_a"), "firm")],
    country="US", city="Los Angeles", focus="Security",
    note="Open Raven, cloud data security, Los Angeles. The firm's post of 2020-06-16 says Kleiner Perkins led the "
         "Series A; the firm's listings begin in 2021 and no earlier Kleiner Perkins round is known, so the Series A "
         "is read as the entry. Its domain no longer resolves (2026-09-30) and no sale or shutdown was found, so "
         "status unknown."))

L.append(jl.cls("opower", stage="Growth", stage_src="web_verified", stage_cite=W("Opower"), stage_conf="high",
    entry_date="2010-11", rng="below_1b", city="Arlington", focus="Climate & Energy",
    rounds=[R("2010-11", "third round (Series C)", 50_000_000, "Accel Partners; Kleiner Perkins Caufield & Byers",
              True, W("Opower"), "press")],
    note="Opower, utility customer-engagement software for energy efficiency, Arlington VA. Wikipedia: the $50M "
         "third round of November 2010 was led by Accel and KPCB. The 2014 S-1 (" + OPOWER_S1 + ") lists the stake "
         "as held by KPCB Green Growth Fund (2,247,192 shares, the same as Accel's, bought in that round) and dates "
         "the amended investor rights agreement 2010-11-24. Growth. Acquired by Oracle in 2016."))

L.append(jl.cls("opthonix", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="San Diego", focus="Healthcare & Bio",
    note="Ophthonix (iZon high-resolution lenses), which the firm's own 2012 page calls 'a San Diego based vision "
         "correction company' (partner Joe Lacob, a seat from his Kleiner Perkins years). No source read gives its "
         "fate or the round."))

L.append(jl.cls("optic", status="private", rng="below_1b", stage="Seed", stage_src="web_verified",
    stage_cite=OPTIC_SEED, stage_conf="high", entry_date="2022-07-20",
    rounds=[R("2022-07-20", "Seed", 11_000_000, "Kleiner Perkins; Pantera Capital", True, OPTIC_SEED, "press")],
    country="US", city="San Francisco", focus="Healthcare & Bio",
    note="Optic, Inc. (Andrey Doronichev), founded 2022 on AI content recognition for NFTs. The Block (2022-07-20): "
         "an $11M seed led by Kleiner Perkins and Pantera Capital, with Greylock among the others. optic.xyz now "
         "redirects to BIOPTIC, AI research for pharma teams, whose 2026 footer still reads 'Optic, Inc.' (read "
         "2026-09-30): the same company as Greylock's Optic row (San Francisco, Healthcare & Bio, aligned); not the "
         "YC Optic (New York, acquired). Graduation left for the graduation pass."))

L.append(jl.cls("optilink", status="acquired", rng="below_1b", stage="undetermined", entry_date="1987", rounds=[],
    country="US", city="Petaluma", focus="Data Infrastructure",
    note="Optilink, fiber-optic loop transmission equipment, Petaluma CA; the firm dates its entry 1987 and records "
         "the exit to Digital Switch (DSC Communications). The round is not on record."))

L.append(jl.cls("orcan-energy", status="private", rng="below_1b", stage="undetermined", rounds=[],
    country="DE", country_src="web_verified", country_cite=ORCAN_SITE, city="Munich", city_src="web_verified",
    focus="Climate & Energy",
    note="Orcan Energy AG, waste-heat-to-power ORC modules; its own site (read 2026-09-30) says headquartered in "
         "Munich with production in Kiel, and it operates. On the firm's 2013-18 greentech pages (Brook Porter, Jan "
         "van Dokkum); the round is not on record."))

L.append(jl.cls("otismed", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="Alameda", focus="Healthcare & Bio",
    note="OtisMed, patient-specific knee-surgery instrumentation (Alameda CA); the firm's own 2012-14 page calls it "
         "a business unit of Stryker Orthopaedics (acquired 2009). Partner Dana Mead. The round is not on record."))

L.append(jl.cls("ouya", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="Santa Monica", focus="Media, Gaming & Advertising",
    note="OUYA (Boxer8, Santa Monica), the Android game console; its software assets and team were sold to Razer in "
         "July 2015 (Wikipedia), an asset sale read as acquired with Razer the successor. Partner Bing Gordon; the "
         "Kleiner Perkins round is not cited (the queued Google News check had not returned), so undetermined."))

L.append(jl.cls("oven", status="acquired", rng="below_1b", stage="Seed", stage_src="first_party",
    stage_cite=POSTX("celebrating-bun"), stage_conf="high", entry_date="2022-08-24",
    rounds=[R("2022-08-24", "Seed", 7_000_000, "Kleiner Perkins", True, W("Bun (software)"), "press")],
    country="US", city="San Francisco", focus="DevTools & APIs",
    note="Oven, the company behind the Bun JavaScript runtime (Jarred Sumner). The firm's post of 2025-12-02 says "
         "'we proudly led Bun (then called Oven's) Seed'; Wikipedia dates the $7M seed led by Kleiner Perkins to "
         "2022-08-24. Anthropic acquired Bun on 2025-12-02 (Wikipedia). Graduation left for the graduation pass."))

L.append(jl.cls("packagd", status="acquired", rng="below_1b", stage="Seed", stage_src="web_verified",
    stage_cite=PACKAGD_TC, stage_conf="medium", entry_date="2017",
    grad="graduated", grad_src="web_verified", grad_cite=PACKAGD_TC, grad_conf="high",
    rounds=[R("2017", "initial seed funding", 1_500_000, "Kleiner Perkins", True, PACKAGD_TC, "press"),
            R("2017-06-08", "Series A", 6_000_000, "Forerunner Ventures; GV", None, PACKAGD_TC, "press")],
    country="US", focus="Consumer & Marketplaces", flags=("city_unknown",),
    note="Packagd (shoppable unboxing video), incubated at Kleiner Perkins by partner Eric Feng. TechCrunch "
         "(2017-06-08): Kleiner Perkins put up the initial $1.5M, then Forerunner and GV led a $6M Series A, which "
         "graduates the row. The seed is dated only as before that article, so the entry year is 2017 at the "
         "latest. Facebook bought it in 2019 (GV's row, aligned). No source read gives the city."))

L.append(jl.cls("pair-team", status="private", rng="below_1b", stage="Seed", stage_src="web_verified",
    stage_cite=PAIR_SEED, stage_conf="high", entry_date="2020-12-09",
    grad="graduated", grad_src="web_verified", grad_cite=PAIR_A, grad_conf="high",
    rounds=[R("2020-12-09", "Seed", 2_700_000, None, True, PAIR_SEED, "press"),
            R("2023-10-19", "Series A", 9_000_000, "NEXT Ventures", True, PAIR_A, "company")],
    country="US", city="San Francisco", focus="Healthcare & Bio",
    note="Pair Team, primary care for Medicaid patients, San Francisco. HIT Consultant (2020-12-09): out of stealth "
         "with a $2.7M seed from Kleiner Perkins, Craft Ventures and Y Combinator. The company's release of "
         "2023-10-19 names a $9M Series A led by NEXT Ventures with Kleiner Perkins participating: graduated."))

L.append(jl.cls("parallel", status="private", rng="1b_plus", usd=2_000_000_000, val_src="web_verified",
    val_cite=PARALLEL_TC, asof="2026-04-29", stage="Series A", stage_src="web_verified", stage_cite=PARALLEL_TC,
    stage_conf="high", entry_date="2025-11",
    rounds=[R("2025-11", "Series A", 100_000_000, "Kleiner Perkins; Index Ventures", True, PARALLEL_TC, "press"),
            R("2026-04-29", "Series B", 100_000_000, "Sequoia", None, PARALLEL_TC, "press")],
    country="US", city="Palo Alto", city_src="web_verified", focus="AI & Applied AI",
    flags=("model_disputes_source",), extra={"valuation_range_source": "web_verified"},
    note="Parallel Web Systems (Parag Agrawal), web infrastructure for AI agents; the AU claim is a Wikidata homonym, "
         "disputed: a US company. TechCrunch (2026-04-29): $100M Series B at $2B led by Sequoia, after a $100M "
         "Series A at $740M led by Kleiner and Index (the firm's own post of 2025-11-12 says it co-led the Series A; "
         "its since-year is 2025, and the January 2024 seed was Khosla, Index and First Round). Mark aligned with "
         "Spark and First Round. The careers page lists Palo Alto first among its offices (Spark's city; First "
         "Round reads San Francisco). Momentum slice: the mark itself is the check."))

L.append(jl.cls("pathlight", status="private", rng="below_1b", stage="Series A", stage_src="web_verified",
    stage_cite=PATHLIGHT_A, stage_conf="high", entry_date="2020-03-26",
    rounds=[R("2020-03-26", "Series A", 7_000_000, "Kleiner Perkins", True, PATHLIGHT_A, "company")],
    country="US", city="San Francisco", focus="SaaS",
    note="Pathlight (Alex Kvamme, Trey Doig), team performance management for customer-facing teams, San Francisco. "
         "Its release of 2020-03-26: Kleiner Perkins led the $7M Series A ($10M raised to date). Momentum check "
         "2026-09-30 (web search): the latest round found is the $25M April 2021 round led by Insight Partners with "
         "Kleiner Perkins; no $1B round, and no sale or shutdown found."))

L.append(jl.cls("pavilion-data", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="San Jose", focus="Data Infrastructure",
    note="Pavilion Data Systems, NVMe-over-fabrics storage arrays (San Jose), on the firm's 2018-25 enterprise and "
         "hardtech lists. Its domain is now for sale (2026-09-30) and no sale or shutdown was cited, so status "
         "unknown; the round Kleiner Perkins entered is not on record."))

L.append(jl.cls("paymate", status="private", rng="below_1b", stage="undetermined", rounds=[],
    country="IN", country_src="web_verified", country_cite=W("PayMate"), city="Mumbai", city_src="web_verified",
    focus="Fintech & Payments", flags=("model_disputes_source",),
    note="PayMate, the Indian mobile and B2B payments company (Mumbai, Wikipedia); the Wikidata NO claim is a "
         "homonym, disputed. An iFund position (2008-14 listings). It filed a DRHP in May 2022 but has not listed. "
         "The round is not on record."))

L.append(jl.cls("peakstream", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="Redwood City", focus="DevTools & APIs",
    note="PeakStream, a software platform for GPU and multicore computing (Redwood City, Matt Murphy); acquired by "
         "Google in 2007. The Kleiner Perkins round is not cited, so undetermined."))

L.append(jl.cls("pelago-inc", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified",
    stage_cite=W("Whrrl"), stage_conf="high", entry_date="2006-11",
    rounds=[R("2006-11", "Series A", None, None, True, W("Whrrl"), "press"),
            R("2008-05", "second round", 15_000_000, "Deutsche Telekom", None, W("Whrrl"), "press")],
    country="US", city="Seattle", focus="Consumer & Marketplaces",
    note="Pelago, Inc. (the Whrrl location app), Seattle. Wikipedia: its November 2006 Series A was backed by "
         "Kleiner Perkins, Trilogy Equity Partners and Bezos Expeditions; Groupon bought it in April 2011. The "
         "Pelago rows in the a16z, Atomico, EQT Ventures and YC books are a different company (New York health)."))

L.append(jl.cls("peng-peng", status="unknown", rng="undetermined", stage="undetermined", grad="undetermined",
    flags=("identity_unresolved",),
    note="Peng Peng (pengpeng.la), on the firm's 2021-24 logo grid only. The domain no longer resolves and no "
         "source read says what the company is or where it is, so the row cannot be identified."))

L.append(jl.cls("pernixdata", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified",
    stage_cite=W("PernixData"), stage_conf="medium", entry_date="2013-05",
    rounds=[R("2013-05", "second round (Series B)", None, None, True, W("PernixData"), "press")],
    city="San Jose", focus="Data Infrastructure",
    note="PernixData (flash virtualization), San Jose. Wikipedia: its second round, in May 2013, came from Kleiner "
         "Perkins and the original investors, so the firm entered at the B (Growth). Nutanix bought it in 2016."))

L.append(jl.cls("picloud", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="San Francisco", focus="DevTools & APIs",
    note="PiCloud, Python cloud computing (San Francisco, Matt Murphy); Dropbox took it over in November 2013 "
         "(aligned with a16z's row). The round is not on record."))

L.append(jl.cls("pillar", status="unknown", rng="below_1b", stage="undetermined", entry_date="2019-05",
    rounds=[R("2019-05-30", "undisclosed", None, None, True, POSTX("welcome-pillar"), "firm")],
    country="US", focus="Fintech & Payments", flags=("city_unknown", "model_disputes_source"),
    note="Pillar, a student-loan repayment app (founders Michael and Gilad); the JP claim is a Wikidata homonym, "
         "disputed. The firm's post of 2019-05-30 announces its investment without naming the round; the firm now "
         "lists it among alumni and pillar.app is parked for sale (2026-09-30). Fate and city not found."))

L.append(jl.cls("pinger", status="private", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="San Jose", focus="Consumer & Marketplaces",
    note="Pinger (Textfree, Sideline), founded 2005 by Greg Woock and Joe Sipher, headquartered in San Jose "
         "(Wikipedia); an iFund-era listing with Randy Komisar, still operating. The round is not on record."))

L.append(jl.cls("plastiq", status="acquired", rng="below_1b", stage="Growth", stage_src="first_party",
    stage_cite=POSTX("plastiq-empowering-smbs-with-better-bill-payment"), stage_conf="medium", entry_date="2018-11",
    rounds=[R("2018-11-19", "Series C", 27_000_000, "Kleiner Perkins", True,
              POSTX("plastiq-empowering-smbs-with-better-bill-payment"), "firm")],
    country="US", city="San Francisco", focus="Fintech & Payments",
    note="Plastiq, card-funded bill payment for SMBs, San Francisco. The firm's post of 2018-11-19 says it led the "
         "$27M Series C; its listings begin in 2018 and no earlier Kleiner Perkins round is known (Growth). Chapter "
         "11 in May 2023 with the business sold to Priority Technology: acquired with a successor, as Khosla's row."))

L.append(jl.cls("platial", status="defunct", rng="below_1b", stage="undetermined", rounds=[],
    city="Portland", focus="Consumer & Marketplaces",
    note="Platial, collaborative map-making website, Portland OR; it announced its closure on 2010-02-27 "
         "(Wikipedia). The round the firm entered is not on record."))

L.append(jl.cls("plum-district", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified",
    stage_cite=W("Plum District"), stage_conf="medium", entry_date="2010",
    rounds=[R("2010", "Series A (angels)", 2_100_000, None, False, W("Plum District"), "press"),
            R("2010", "Series A", 8_500_000, None, True, W("Plum District"), "press"),
            R("2011-12", "Series C", 20_000_000, None, True, W("Plum District"), "press")],
    country="US", city="San Francisco", focus="Consumer & Marketplaces",
    note="Plum District, daily deals for mothers, San Francisco; an sFund position (Aileen Lee). Wikipedia: $8.5M "
         "Series A from Kleiner Perkins and General Catalyst after a $2.1M angel Series A, and a $20M Series C in "
         "December 2011; the year of the $8.5M is not given there and is read as 2010, the sFund's launch year. "
         "Acquired by Coupon Lawn in July 2020 (Wikipedia), fresher than General Catalyst's 'unknown'."))

L.append(jl.cls("podshow", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified",
    stage_cite=W("Mevio"), stage_conf="medium", entry_date="2005-08",
    rounds=[R("2005-08", "first venture round", 8_850_000, None, True, W("Mevio"), "press"),
            R("2006-09-29", "second round", 15_000_000, "DAG Ventures", True, W("Mevio"), "press"),
            R("2008-07", "Series C", 15_000_000, "Crosslink Capital", True, W("Mevio"), "press")],
    country="US", city="Los Angeles", focus="Media, Gaming & Advertising",
    note="PodShow (Mevio from 2008), podcast network founded 2004 in San Francisco. Wikipedia: Kleiner Perkins, "
         "Sequoia and Sherpalo put in about $8.85M in August 2005, its first venture round; the 2006 round is the "
         "second and the 2008 one is named Series C, so the entry is the Series A. The company moved to Hollywood "
         "as Bitesize (2012), closed the Mevio service in April 2014, and Bitesize was bought by Media General: "
         "acquired, last city Los Angeles."))

L.append(jl.cls("poetic", status="private", rng="below_1b", stage="Seed", stage_src="first_party",
    stage_cite=POSTX("poetic-turning-enterprise-procedures-into-evolving-software"), stage_conf="medium",
    entry_date="2026", grad="graduated", grad_src="first_party",
    grad_cite=POSTX("poetic-turning-enterprise-procedures-into-evolving-software"), grad_conf="high",
    rounds=[R("2026", "Seed", None, None, True,
              POSTX("poetic-turning-enterprise-procedures-into-evolving-software"), "firm"),
            R("2026-06-10", "Series A", 50_000_000, "Kleiner Perkins", True,
              POSTX("poetic-turning-enterprise-procedures-into-evolving-software"), "firm")],
    country="US", focus="AI & Applied AI", flags=("city_unknown",),
    note="Poetic (runbooks written in plain language, run by AI; founder Markie Wagner). The firm's post of "
         "2026-06-10: its partner backed Poetic at the seed stage, then Kleiner Perkins led the $50M Series A, which "
         "graduates the row; the seed is dated only by the firm's since-year, 2026. Momentum check 2026-09-30 "
         "(Google News, nq.py): the headlines of 2026-06-10 (Benzinga, Pulse 2.0) put the Series A at a $500M "
         "valuation; no $1B round. The publisher links were not yet decoded, so the check is recorded here only."))

L.append(jl.cls("power-computing", status="acquired", rng="below_1b", stage="undetermined", entry_date="1995",
    rounds=[], country="US", city="Round Rock", focus="Consumer & Marketplaces",
    note="Power Computing, the Mac-clone maker founded 1993 in Milpitas and later based across I-35 from Dell's "
         "Round Rock campus; Apple bought its Mac OS license and core assets in 1997 (Wikipedia), which ended the "
         "business: read as acquired, as the firm's exit line. The firm dates its entry 1995; the round is not on "
         "record."))

jl.write("j09a", L)
