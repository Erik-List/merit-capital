"""Judge c9, batch 18 (queue/batch-018.json): listed members, classification (plus X1 membership where the record
shows the listing is a public purchase)."""
import json

import judge_lib as jl
from judge_lib import cls, rnd, verdict

BASE = {r["slug"]: r for r in json.loads((jl.INV / "companies/base.json").read_text())}


def edgar(slug, i=0):
    return BASE[slug]["edgar_links"].split("; ")[i].strip()


CMC = "https://companiesmarketcap.com/{}/marketcap/"
WV = {"valuation_range_source": "web_verified"}
L = []

# ---- membership: X1 (PIPE into a listed company)
L.append(verdict("solta-medical", "not_member",
                 "X1/R2: the firm labels it Public/PIPES (2008); Growth Equity Opportunities Fund with NEA 12 bought "
                 "shares and warrants in a 2010 private placement (S-3 of 2010-01-29) and filed 13Gs from 2011, into "
                 "Solta (formerly Thermage), listed on Nasdaq since 2006; no NEA private round before the listing is "
                 "on record, and the firm's 2015 release places Solta in its public healthcare practice.",
                 ec="fund_filing", conf="high", cite=edgar("solta-medical")))

# ---- classification
L.append(cls("setpoint-medical", status="private", rng="below_1b", city="Valencia", city_src="formd_address",
             focus="Healthcare & Bio",
             note="Vagus nerve stimulation for rheumatoid arthritis, Valencia CA (Form D); its 2025 Form D reports "
                  "$115.5M sold with no published post-money."))
L.append(cls("shape-therapeutics", status="private", rng="below_1b", country="US", city="Seattle",
             city_src="web_verified", stage="undetermined", entry_date="2019", focus="Healthcare & Bio",
             note="RNA editing and gene therapy company; the firm's own listing places it in Seattle and San Diego "
                  "and labels the 2019 entry Early. No named round ties NEA's entry."))
L.append(cls("sierra-atlantic", status="acquired", rng="below_1b", city="Fremont", stage="undetermined",
             entry_date="1999", focus="Data Infrastructure",
             note="Enterprise application integration services, Fremont CA; Hitachi Consulting bought it in 2010 "
                  "(the firm's exit line). No round is named."))
L.append(cls("silicon-graphics", status="acquired", rng="below_1b", city="Sunnyvale", stage="undetermined",
             entry_date="1984", focus="Industrial & Robotics",
             note="The Public/PIPES label does not make it an X1 row: NEA's Richard Kramlich was a director from 1984 "
                  "(2002 proxy), before the 1986 listing. The firm's 1990 year is later than that seat, so the "
                  "entry year is read from the proxy. Status disputed from defunct: in 2009 SGI sold substantially "
                  "all its assets out of Chapter 11 to Rackable Systems, which took the Silicon Graphics name "
                  "(Wikipedia), an asset sale out of insolvency. Last headquarters Sunnyvale."))
L.append(cls("silicon-spice", status="acquired", rng="below_1b", country="US", city="Mountain View",
             stage="undetermined", entry_date="1997", focus="Industrial & Robotics",
             note="Communications processors; Broadcom bought it in 2000 (the firm's exit line). No round is named."))
L.append(cls("siliconblue-technologies", status="acquired", rng="below_1b", city="Santa Clara",
             city_src="formd_address", focus="Industrial & Robotics",
             note="Low-power FPGAs; Lattice Semiconductor bought it in 2011 (the firm's exit line)."))
L.append(cls("simple-habit", status="private", rng="below_1b", country="US", city="San Francisco",
             stage="Seed", stage_src="first_party", stage_cite=jl.SITE("simple-habit"), stage_conf="medium",
             entry_date="2017", focus="Consumer & Marketplaces",
             note="Meditation app; the firm's own listing labels the 2017 entry Seed. Graduation left for the "
                  "graduation pass."))
L.append(cls("simple-psychology", status="private", rng="below_1b", country="CN", country_src="web_verified",
             country_cite="https://www.jiandanxinli.com", city="Beijing", city_src="web_verified",
             stage="undetermined", entry_date="2016", focus="Healthcare & Bio",
             note="Jiandan Xinli, online psychotherapy marketplace operated by a Beijing company (its own site's "
                  "registration footer); Carmen Chang on the board from the firm's 2016 entry, labelled Early. No "
                  "named round."))
L.append(cls("simplerose", status="private", rng="below_1b", country="US", stage="undetermined", entry_date="2018",
             focus="Data Infrastructure", flags=("city_unknown",),
             note="Optimization solver software; its own site shows 2026 activity but no location, and no named "
                  "round was found (the firm's 2018 entry, labelled Early)."))
L.append(cls("simplex-healthcare", status="acquired", rng="below_1b", country="US", city="Franklin",
             city_src="formd_address", stage="Growth", stage_src="first_party",
             stage_cite=jl.SITE("simplex-healthcare"), stage_conf="medium", entry_date="2007",
             focus="Healthcare & Bio",
             note="Direct-to-patient diabetic supplies, Franklin TN (Form D); the firm labels its 2007 entry Growth, "
                  "and the 2010 Form D the band read is a later round. Acquired by Arriva Medical (the firm's exit "
                  "line)."))
L.append(cls("simsolid", status="acquired", rng="below_1b", stage="Seed", stage_src="first_party",
             stage_cite=jl.SITE("simsolid"), stage_conf="medium", entry_date="2015", focus="Industrial & Robotics",
             flags=("city_unknown",),
             note="Meshless structural simulation for design engineers; the firm's own listing labels the 2015 "
                  "entry Seed. Altair announced the acquisition on 2018-10-17 (its release, now on the Siemens "
                  "newsroom). The company is Canadian by every account seen, but no page read states its city or "
                  "country, so both are left open. Graduation left for the graduation pass."))
L.append(cls("solfocus-inc", status="unknown", rng="below_1b", city="Mountain View", city_src="formd_address",
             stage="undetermined", entry_date="2006", focus="Climate & Energy", flags=("stage_disputes_band",),
             note="Concentrator solar company, Mountain View (Form D). The prefilled Seed reads a $3.8M filing of "
                  "December 2008, but the firm's first investment is 2006, so that filing is a follow-on and the "
                  "entry round is not named. Filings stop in 2012 and Google News (2026-09-30) found nothing on "
                  "its fate."))
L.append(cls("singularity", status="private", rng="below_1b", country="US", city="El Segundo",
             stage="undetermined", entry_date="2024", focus="Industrial & Robotics",
             note="Singularity Defense, low-cost air defense interceptors; its site names NEA, Khosla, Felicis, Long "
                  "Journey, AE Industrial and YC. Felicis and Menlo record a 2026 Series A; NEA's 2024 entry "
                  "predates it but no round names NEA. The sibling rows disagree on the city (El Segundo, San "
                  "Francisco, Los Angeles); Lightspeed's Chinese 'Singularity' is a different company."))
L.append(cls("sisu", status="acquired", rng="below_1b", city="San Francisco", city_src="formd_address",
             focus="Data Infrastructure",
             note="Decision intelligence analytics; NEA's post announces its Series B investment (2019). Snowflake "
                  "took the company over in 2023; aligned with the a16z row."))
L.append(cls("sitetracker", status="private", rng="below_1b", city="Palo Alto", city_src="formd_address",
             entry_date="2017", focus="SaaS",
             note="Project and asset management for infrastructure builds. The firm's first investment is 2017 and "
                  "the same issuer (CIK 1711376) filed an $11M Form D in 2017 with NEA's Chetan Puttagunta as a "
                  "director, so the entry year is 2017, not the 2018 filing the band read. The base also carries "
                  "the old 'sitetraker' spelling as a separate row."))
L.append(cls("sitetraker", status="private", rng="below_1b", city="Palo Alto", city_src="formd_address",
             stage="Series A", stage_src="model", stage_conf="medium", entry_date="2017", focus="SaaS",
             rounds=[rnd("2017", "Form D offering (round not named)", 11000000, None, True, None, "filing")],
             note="Duplicate of sitetracker (same Form D CIK 1711376, archived under the old spelling). The 2017 "
                  "$11M offering with Chetan Puttagunta as director, the issuer's first filing, sits in the Series "
                  "A band for its year."))
L.append(cls("sitime", status="public", rng="10b_plus", usd=19580000000, val_src="web_verified",
             val_cite=CMC.format("sitime"), asof="2026-09-29", city="Santa Clara", stage="undetermined",
             entry_date="2004", focus="Industrial & Robotics", extra=WV,
             note="MEMS timing chips, Santa Clara (Wikipedia); MegaChips bought it in 2014 and spun it out in a "
                  "2019 listing. Market cap $19.58B at the 2026-09-29 close (companiesmarketcap), in line with the "
                  "Greylock row; the old float is replaced. No round is named for NEA's 2004 entry."))
L.append(cls("slash", city="San Francisco", stage="Seed", stage_src="web_verified",
             stage_cite=jl.W("Slash (company)"), stage_conf="medium", entry_date="2021", grad="graduated",
             grad_src="web_verified", grad_cite=jl.W("Slash (company)"), grad_conf="high",
             focus="Fintech & Payments",
             rounds=[rnd("2022", "Seed", None, "New Enterprise Associates", True, jl.W("Slash (company)"), "press"),
                     rnd("2023", "Series A", None, "New Enterprise Associates", True, jl.W("Slash (company)"),
                         "press"),
                     rnd("2025-05", "Series B", 41000000, "Goodwater Capital", True, jl.W("Slash (company)"),
                         "press")],
             note="NEA led the seed and the Series A ($19M combined, Wikipedia), and the firm's archived listing "
                  "labelled the 2021 entry Seed. Graduated: the NEA-led Series A of 2023."))
L.append(cls("slope", status="private", rng="below_1b", country="US", city="Atlanta", stage="Series A",
             stage_src="first_party", stage_cite=jl.POST("making-clinical-trials-boring"), stage_conf="high",
             entry_date="2021-10-06", focus="Healthcare & Bio",
             rounds=[rnd("2021-10-06", "Series A", None, "New Enterprise Associates", True,
                         jl.POST("making-clinical-trials-boring"), "firm")],
             note="Slope (slopeclinical.com), clinical trial biospecimen software; the firm's own post says Slope "
                  "chose NEA to lead its Series A. The USV and YC 'Slope' rows are a different company (the "
                  "payments startup)."))
L.append(cls("smartcar", status="private", rng="below_1b", country="US", city="Mountain View",
             stage="Series A", stage_src="first_party", stage_cite=jl.POST("smartcar-driving"), stage_conf="high",
             entry_date="2018-03", focus="DevTools & APIs",
             rounds=[rnd("2018-03", "Series A", 10000000, "New Enterprise Associates", True,
                         jl.POST("smartcar-driving"), "firm")],
             note="Connected-car APIs; NEA led the $10M Series A with a16z (the firm's own post, 2018-03). City "
                  "aligned with the a16z row."))
L.append(cls("smartdrive-systems", status="acquired", rng="below_1b", city="San Diego", city_src="formd_address",
             stage="undetermined", entry_date="2007", focus="Industrial & Robotics",
             note="Video-based fleet safety; Omnitracs bought it in 2020 (the firm's exit line). The firm's 2007 "
                  "entry predates the 2009 Form D and no round is named."))
L.append(cls("snagfilms", status="defunct", rng="below_1b", city="Washington", city_src="formd_address",
             stage="undetermined", entry_date="2010", focus="Media, Gaming & Advertising",
             flags=("stage_disputes_band",),
             note="SnagFilms shut its service in 2020 (Wikipedia, quoting its homepage). The prefilled Seed reads a "
                  "2012 filing, but the firm's first investment is 2010 and the issuer filed a $10M offering in "
                  "2010, so the 2012 round is a follow-on; the entry round is not named."))
L.append(cls("snap", country="US", city="Santa Monica", stage="Growth", stage_src="first_party",
             stage_cite=jl.SITE("snap"), stage_conf="medium", entry_date="2015", status="public", rng="1b_plus",
             usd=9030000000, val_src="web_verified", val_cite=CMC.format("snap"), asof="2026-09-29",
             focus="Consumer & Marketplaces", extra=WV,
             note="The firm labels its 2015 entry Growth. Market cap $9.03B at the 2026-09-29 close "
                  "(companiesmarketcap), below $10B: the $11.6B float band is replaced, in line with the sibling "
                  "rows (all 1b_plus)."))
L.append(cls("snowplow", status="private", rng="below_1b", country="GB", country_src="web_verified",
             country_cite="https://snowplow.io/", city="London", city_src="web_verified", stage="Growth",
             stage_src="first_party", stage_cite=jl.POST("snowplow"), stage_conf="high", entry_date="2022-06-30",
             focus="Data Infrastructure",
             extra={**WV, "valuation_citation": jl.NEWS("snowplow", "Closes $40M in Series B")},
             rounds=[rnd("2022-06-30", "Series B", 40000000, "New Enterprise Associates", True,
                         jl.POST("snowplow"), "firm")],
             note="Behavioral data platform, London (its own site lists London then Boston). The firm's own post: "
                  "NEA led the $40M Series B. Momentum check 2026-09-30 (Google News): only the 2022 Series B, no "
                  "later priced round."))
L.append(cls("socialradar", status="acquired", rng="below_1b", city="Washington", city_src="formd_address",
             focus="Consumer & Marketplaces",
             note="Location-aware social app, Washington DC (Form D); Verizon bought it (the firm's exit line)."))
L.append(cls("sol", status="private", rng="below_1b", country="US", stage="Seed", stage_src="first_party",
             stage_cite=jl.SITE("sol"), stage_conf="medium", entry_date="2026", grad="censored",
             focus="AI & Applied AI", flags=("model_disputes_source", "city_unknown"),
             note="Sol (meetsol.com), an agentic core HR system 'backed by Sutter Hill Ventures and NEA' (its own "
                  "site, no location given). The prefilled JP is a one-word Wikidata match and is disputed; US on "
                  "the investors' footprint. The firm labels the 2026 entry Seed, so graduation is censored. YC's "
                  "'sol' row is an unidentified different company. Momentum check 2026-09-30 (Google News): no "
                  "item reports a round or a price."))
L.append(cls("solace-therapeutics", status="private", rng="below_1b", city="Framingham", city_src="formd_address",
             stage="undetermined", entry_date="2012", focus="Healthcare & Bio",
             note="Bladder device company, Framingham MA (Form D, filings to 2021). The firm's first investment is "
                  "2012; its partner-matched Form D starts in 2016, and no round is named."))
L.append(cls("solar-junction", status="acquired", rng="below_1b", country="US", city="San Jose",
             stage="undetermined", entry_date="2007", focus="Climate & Energy",
             note="Multi-junction solar cells; the firm's exit line says acquired by the IRRADIANCE Group. No round "
                  "is named."))
L.append(cls("solidfire", status="acquired", rng="below_1b", city="Boulder", city_src="formd_address",
             focus="Data Infrastructure",
             note="All-flash storage, Boulder CO (Form D); NetApp bought it in 2016 (the firm's exit line)."))
L.append(cls("some-spider-studios", status="acquired", rng="below_1b", country="US", city="New York",
             stage="undetermined", entry_date="2017", focus="Media, Gaming & Advertising",
             note="Scary Mommy and sister brands; the firm's exit line says acquired by BDG Media. No round is named."))
L.append(cls("sonatype", status="acquired", rng="below_1b", city="Fulton", stage="undetermined",
             focus="Security",
             note="Software supply chain management; Vista Equity Partners bought control in 2019 (the firm's exit "
                  "line). The 2012 $25M offering followed a 2010 filing and is not named. City aligned with the "
                  "Accel row."))
L.append(cls("sonic-innovations", status="acquired", rng="below_1b", country="US", city="Salt Lake City",
             stage="undetermined", entry_date="1997", focus="Healthcare & Bio",
             note="Digital hearing aids, listed in 2000 after NEA's 1997 private entry; William Demant bought it "
                  "(the firm's exit line). No round is named."))
L.append(cls("soraa", status="acquired", rng="below_1b", city="Fremont", city_src="formd_address",
             focus="Climate & Energy",
             note="GaN-on-GaN LEDs; Ecosense Lighting bought the business (the firm's exit line); aligned with the "
                  "Khosla row."))
L.append(cls("sorriso-pharmaceuticals", status="private", rng="below_1b", city="Sandy", city_src="formd_address",
             focus="Healthcare & Bio",
             note="Oral antibodies for inflammatory bowel disease, Sandy UT (Form D); no priced mark published."))
L.append(cls("sourcefire", city="Columbia", stage="Growth", stage_src="web_verified",
             stage_cite=jl.FTS("SOURCEFIRE", "S-1"), stage_conf="medium", entry_date="2003", rng="below_1b",
             focus="Security",
             note="The S-1's voting agreement gives NEA 10 the Series B director seat, and the firm's first "
                  "investment is 2003: NEA entered at the Series B. Cisco bought Sourcefire in 2013."))
L.append(cls("spectrian", status="acquired", rng="below_1b", country="US", city="Sunnyvale",
             stage="undetermined", entry_date="1991", focus="Industrial & Robotics",
             note="RF power amplifiers for wireless infrastructure; REMEC bought it in 2002 (the firm's exit line). "
                  "No round is named."))
L.append(cls("spektr", status="private", rng="below_1b", country="DK", country_src="web_verified",
             country_cite=jl.POST("how-spektr"), city="Copenhagen", city_src="web_verified", stage="Series A",
             stage_src="first_party", stage_cite=jl.POST("how-spektr"), stage_conf="high", entry_date="2026-04",
             focus="Fintech & Payments",
             extra={**WV, "valuation_citation": jl.NEWS("spektr", "In NEA-Led Series A")},
             rounds=[rnd("2026-04-15", "Series A", 20000000, "New Enterprise Associates", True,
                         jl.NEWS("spektr", "In NEA-Led Series A"), "press")],
             note="The firm's own post announces its Series A lead in spektr (Copenhagen). Momentum check "
                  "2026-09-30 (Google News): the $20M Series A of April 2026 is the latest round, no $1B price. "
                  "Aligned with the Northzone row."))
L.append(cls("spine-wave", status="private", rng="below_1b", city="Shelton", city_src="formd_address",
             stage="undetermined", entry_date="2000", focus="Healthcare & Bio",
             note="Spinal device company, Shelton CT (Form D). The firm's first investment is 2000; the Form D "
                  "layer starts in 2011, and no round is named."))
L.append(cls("spiras-health", status="private", rng="below_1b", country="US", city="Brentwood",
             city_src="web_verified", stage="Growth", stage_src="first_party",
             stage_cite=jl.POST("spiras-health-personalized"), stage_conf="high", entry_date="2021-06-22",
             focus="Healthcare & Bio",
             rounds=[rnd("2021-06-22", "Series B", None, None, True, jl.POST("spiras-health-personalized"),
                         "firm")],
             note="In-home care management for chronic disease, Brentwood TN (its own site). The firm's own post: "
                  "NEA partnered at the Series B announced 2021-06-22."))
L.append(cls("spiration", status="acquired", rng="below_1b", country="US", city="Redmond", stage="undetermined",
             entry_date="1999", focus="Healthcare & Bio",
             note="Bronchoscopic emphysema valves; Olympus bought it in 2010 (the firm's exit line). No round is "
                  "named."))
L.append(cls("splashtop", city="Cupertino", stage="undetermined", entry_date="2008", focus="SaaS",
             note="Remote access software, founded 2006 as DeviceVM (Wikipedia). The firm's 2008 entry carries no "
                  "named round."))
L.append(cls("splicebio", status="private", rng="below_1b", country="ES", country_src="web_verified",
             country_cite="https://splice.bio", city="Barcelona", stage="undetermined", entry_date="2021",
             focus="Healthcare & Bio",
             rounds=[rnd("2025", "Series B", 135000000, "EQT Life Sciences, Sanofi Ventures", True,
                         "https://splice.bio", "company")],
             note="Protein-splicing gene therapy company from Barcelona (its own site; the CEO's 2025 Diari ARA "
                  "interview). Its $135M Series B was co-led by EQT Life Sciences and Sanofi Ventures with NEA among "
                  "existing investors (its own site); the round NEA entered in 2021 is not named."))
L.append(cls("spokn", status="private", rng="below_1b", country="US", city="New York", stage="Seed",
             stage_src="first_party", stage_cite=jl.SITE("spokn"), stage_conf="medium", entry_date="2021",
             focus="SaaS",
             note="Employee video and audio stories; the firm's own listing labels the 2021 entry Seed. City aligned "
                  "with the YC row. Graduation left for the graduation pass."))
L.append(cls("spreadtrum-communications", status="acquired", rng="below_1b", country="CN",
             country_src="web_verified", country_cite=jl.W("Spreadtrum"), city="Shanghai", city_src="web_verified",
             stage="undetermined", entry_date="2004-04", focus="Industrial & Robotics",
             note="Fabless wireless chip company, Shanghai (Wikipedia); Scott Sandell joined its board in April 2004 "
                  "(F-1), before the 2007 listing; Tsinghua Unigroup bought it in 2013 for about $1.78B. No round "
                  "is named."))

jl.write("c9b", L)
