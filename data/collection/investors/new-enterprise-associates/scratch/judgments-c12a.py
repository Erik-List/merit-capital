"""Judge c12, queue batch 23 (PRO-100 NEA): classification of listed members."""
import judge_lib as jl
from judge_lib import cls, rnd, SITE, ARCH, W, NEWS, FTS

GP = "Graduation left for the graduation pass."
L = []

# ---- Zero (Zero Financial, San Francisco); not the 20VC book's Zero (Helsinki CRM), a name collision
L.append(cls("zero", status="acquired", rng="below_1b",
             country="US", country_src="web_verified",
             country_cite=NEWS("zero", "Avant acquires San Francisco fintech"),
             city="San Francisco", city_src="web_verified",
             stage="Seed", stage_src="first_party", stage_cite=SITE("zero"), stage_conf="medium", entry_date="2016",
             grad="graduated", grad_src="web_verified", grad_conf="high",
             grad_cite=NEWS("zero", "Zero Closes $20M Series A"),
             focus="Fintech & Payments", flags=["model_disputes_source"],
             rounds=[rnd("2019-05-23", "Series A", 20000000, source=NEWS("zero", "Zero Closes $20M Series A"),
                         source_type="company")],
             note="Zero Financial (Zerocard), San Francisco; the firm lists a 2016 Seed entry, and the company closed a "
                  "$20M Series A in May 2019, which graduates the row. Avant bought Zero Financial in April 2021. "
                  "The Wikidata JP country was a one-word name match (disputed); the 20VC book's Zero is a different "
                  "company (Helsinki CRM)."))

L.append(cls("zerofox", rng="below_1b", city="Baltimore", focus="Security",
             note="ZeroFox, Baltimore; listed through a SPAC in 2022 and taken private by Haveli Investments in 2024 "
                  "for about $350M (Wikipedia), so acquired below $1B."))

z10 = FTS("ZHONE TECHNOLOGIES INC", "10-12G")
L.append(cls("zhone-technologies", status="acquired", rng="below_1b", city="Oakland",
             stage="Series A", stage_src="web_verified", stage_cite=z10, stage_conf="medium", entry_date="1999-11",
             focus="Data Infrastructure",
             rounds=[rnd("1999-11", "Series A", 500000000, lead=None, firm_in_round=True, source=z10,
                         source_type="filing")],
             note="Zhone's Form 10 (2003) says it began operations in September 1999 on a $500M commitment from its "
                  "initial investors including NEA, issued as Series A preferred in November 1999; the round is "
                  "consortium-sized (KKR, TPG) but the record names it Series A. Zhone became DASAN Zhone Solutions "
                  "(2016) then DZS, which filed Chapter 7 in March 2025; its assets went to an MSNi-owned Zhone "
                  "Technologies in June 2025 (Data Center Dynamics), so acquired out of insolvency. Same company as "
                  "the row dasan-zhone-solutions-inc."))

L.append(cls("ziarco", status="acquired", rng="below_1b",
             country="GB", country_src="web_verified",
             country_cite=NEWS("ziarco", "Novartis boosts dermatology pipeline"),
             city="Sandwich", city_src="web_verified", stage="undetermined", entry_date="2014",
             focus="Healthcare & Bio",
             rounds=[rnd("2012-11", "first financing", 6000000, firm_in_round=False,
                         source=NEWS("ziarco", "Pfizer helps fund biotech venture"), source_type="press")],
             note="Ziarco, a Sandwich (Kent) biotech of ex-Pfizer scientists, bought by Novartis in December 2016. Its "
                  "first $6M came from BVF and Pfizer Venture Investments in 2012 without NEA; the round NEA joined in "
                  "2014 is not named in any source found, so the stage is undetermined."))

wz = W("Zoomdata")
L.append(cls("zoomdata", status="acquired", rng="below_1b", city="Reston",
             stage="Series A", stage_src="web_verified", stage_cite=wz, stage_conf="medium", entry_date="2013-07",
             focus="Data Infrastructure",
             rounds=[rnd("2012-11", "Seed", 1100000, firm_in_round=False, source=wz, source_type="press"),
                     rnd("2013-07", "Series A", 4100000, lead="Columbus Nova Technology Partners", firm_in_round=True,
                         source=wz, source_type="press"),
                     rnd("2014-10", "Series B", 17000000, lead="Accel Partners", firm_in_round=True, source=wz,
                         source_type="press"),
                     rnd("2016-02", "Series C", 25000000, lead="Goldman Sachs", firm_in_round=False, source=wz,
                         source_type="press")],
             note="The first round naming NEA is the July 2013 $4.1M Series A led by Columbus Nova; the November 2012 "
                  "seed is credited to angels. The firm's 2012 year is read as the close year, hence medium "
                  "confidence. Acquired by Logi Analytics in June 2019; the Accel book agrees on status."))

L.append(cls("zosano", rng="below_1b", city="Fremont", focus="Healthcare & Bio",
             note="Zosano Pharma, Fremont; filed Chapter 11 in 2022 and sold its assets, so acquired below $1B."))

zf = NEWS("zumper", "Foley Hoag Congratulates")
L.append(cls("zumper", status="private", rng="below_1b", country="US", city="San Francisco",
             stage="Seed", stage_src="first_party", stage_cite=SITE("zumper"), stage_conf="medium", entry_date="2012",
             grad="graduated", grad_src="web_verified", grad_cite=zf, grad_conf="high",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2014-03-04", "Series A", None, source=zf, source_type="press")],
             note="The firm lists a 2012 Seed entry; Foley Hoag's client note (2014-03-04) names Zumper's Series A "
                  "financing, which graduates the row. Private, below $1B (last reported round $60M Series D in 2020); "
                  "agrees with the a16z and Headline books."))

L.append(cls("zuoyebang", country="CN", country_src="web_verified", country_cite=SITE("zuoyebang"),
             city="Beijing", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2018",
             rng="1b_plus", usd=9600000000, val_src="web_verified",
             val_cite="https://equalocean.com/news/2020122815324", asof="2020-12-28",
             extra={"valuation_range_source": "web_verified"}, flags=["stale"],
             focus="Consumer & Marketplaces",
             rounds=[rnd("2020-12-28", "Series E+", 1600000000, firm_in_round=None,
                         source="https://equalocean.com/news/2020122815324", source_type="press")],
             note="Zuoyebang, Beijing (CN confirmed by the firm's own page). NEA's first year is 2018, when the company "
                  "was already past its 2015 Series A and later rounds (Coatue led the July 2018 $350M Series D), so "
                  "the entry is Growth. Mark aligned with the Coatue and Tiger Global books: $9.6B post-money on the "
                  "December 2020 E+ round (EqualOcean), stale and before China's 2021 tutoring rules."))

L.append(cls("zyngenia", status="unknown", rng="below_1b", city="Gaithersburg", focus="Healthcare & Bio",
             note="Zyngenia, Gaithersburg (Zybody bispecific antibodies); Form D rounds to 2012 and the firm's listing "
                  "only to 2015. No later report of a sale, shutdown or financing was found, so the state is unknown."))

L.append(cls("3jam-inc", status="unknown", rng="below_1b", country="US", stage="undetermined",
             focus="Consumer & Marketplaces", flags=["city_unknown"],
             note="3Jam, group SMS messaging, on the firm's 2008 US list only. Google News carries nothing on it; no "
                  "city, fate or round could be established."))

L.append(cls("acorn-cardiovascular-inc", status="defunct", rng="below_1b", country="US", city="Saint Paul",
             stage="undetermined", focus="Healthcare & Bio",
             note="Acorn Cardiovascular (CorCap cardiac support device), St. Paul, Minnesota; it ceased operations "
                  "after the device failed to win FDA approval (from knowledge, not re-verified). No round naming NEA "
                  "was found."))

L.append(cls("acoustic-imaging-technologies-corp", status="acquired", rng="below_1b", country="US", city="Tempe",
             stage="undetermined", focus="Healthcare & Bio",
             note="Acoustic Imaging Technologies, Tempe, Arizona, ultrasound systems; the firm's historical list gives "
                  "the exit as acquired by Dornier. No round naming NEA was found."))

L.append(cls("actelis-networks-inc", country="US", city="Fremont", stage="undetermined", focus="Data Infrastructure",
             note="Actelis Networks, carrier broadband over copper, principal office Fremont, California (R&D in "
                  "Israel); listed on Nasdaq (ASNS) since 2022. The round NEA entered is not on record."))

L.append(cls("actional-corporation", status="acquired", rng="below_1b", country="US", city="Mountain View",
             stage="undetermined", focus="Data Infrastructure",
             note="Actional, web services management software, Mountain View; acquired by Progress Software in 2006 "
                  "(the firm's historical list agrees). No round naming NEA was found."))

L.append(cls("adaptec-inc", rng="below_1b", country="US", city="Milpitas", stage="undetermined",
             focus="Industrial & Robotics",
             note="Adaptec, Milpitas, storage controllers; listed 1986, its business sold to PMC-Sierra in 2010 (the "
                  "Lightspeed book agrees). The 1980s round NEA entered is not on record."))

tca = NEWS("aetherflux", "Space solar startup Aetherflux raises $50M")
pay = NEWS("aetherflux", "Aetherflux Rebrands, Pivots Business")
L.append(cls("aetherflux", status="private", rng="1b_plus", usd=2000000000, val_src="web_verified", val_cite=pay,
             asof="2026-05-11", extra={"valuation_range_source": "web_verified"},
             country="US", city="San Carlos", city_src="web_verified",
             stage="Series A", stage_src="web_verified", stage_cite=tca, stage_conf="high", entry_date="2025-04-02",
             focus="Climate & Energy",
             rounds=[rnd("2025-04-02", "Series A", 50000000, lead="Index Ventures, Interlagos", firm_in_round=True,
                         source=tca, source_type="press"),
                     rnd("2026-05-11", "Series B", 275000000, lead="Index Ventures", firm_in_round=None, source=pay,
                         source_type="press")],
             note="NEA joined the $50M Series A led by Index and Interlagos (TechCrunch, April 2025); the founder's own "
                  "$10M preceded it and there was no outside seed. In May 2026 the company rebranded as Cowboy Space "
                  "Corporation (in-orbit compute and launch) and raised a $275M Series B at a $2B valuation (Payload), "
                  "fresher than the a16z book's below-$1B reading. Same company as the row cowboy-space."))

L.append(cls("agami-systems-inc", status="defunct", rng="below_1b", country="US", city="Sunnyvale",
             stage="undetermined", focus="Data Infrastructure",
             note="Agami Systems (formerly Zambeel), Sunnyvale, NAS storage; it shut down (Mercury News, 2008-08-20, "
                  "'What went wrong at start-up Agami Systems?'). No round naming NEA was found."))

L.append(cls("agility-design-solutions", status="acquired", rng="below_1b", country="US", city="Palo Alto",
             stage="undetermined", focus="DevTools & APIs",
             note="Agility Design Solutions, formed in 2008 from Catalytic Inc. and Celoxica's ESL tools business, "
                  "DSP design software; its product lines went to Mentor Graphics in 2009 (from knowledge). No round "
                  "naming NEA was found."))

L.append(cls("agitar-software-inc", status="defunct", rng="below_1b", country="US", city="Mountain View",
             stage="undetermined", focus="DevTools & APIs",
             note="Agitar Software, Mountain View, Java developer testing; wound down around 2008. Aligned with the "
                  "Sequoia book."))

L.append(cls("akashic-memories-corporation", status="acquired", rng="below_1b", country="US", city="San Jose",
             stage="undetermined", focus="Industrial & Robotics",
             note="Akashic Memories, San Jose, sputtered thin-film disk media; the firm's historical list gives the "
                  "exit as acquired by Kubota. No round naming NEA was found."))

L.append(cls("alkermes-inc", rng="below_1b", country="US", city="Waltham", stage="undetermined",
             focus="Healthcare & Bio",
             note="Alkermes, Inc. (Waltham, Massachusetts) combined with Elan Drug Technologies in 2011 and became a "
                  "subsidiary of Alkermes plc (Dublin, Nasdaq ALKS); kept acquired under the successor-entity rule. "
                  "The 1980s round NEA entered is not on record."))

pra = NEWS("allyalign-health", "AllyAlign Health Partners with NEA")
L.append(cls("allyalign-health", status="acquired", rng="below_1b", country="US", city="Richmond",
             city_src="web_verified",
             stage="Growth", stage_src="first_party", stage_cite=ARCH("allyalign-health"), stage_conf="medium",
             entry_date="2021-06-10", focus="Healthcare & Bio",
             rounds=[rnd("2021-06-10", "growth investment", 300000000, lead="New Enterprise Associates",
                         firm_in_round=True, source=pra, source_type="company")],
             note="AllyAlign Health, Richmond, Virginia, Medicare Advantage plans for senior living. NEA led a new "
                  "investment with Oak HC/FT, Town Hall Ventures and existing investors Heritage Group and Ziegler "
                  "(company release, 2021-06-10; $300M per Fierce Healthcare), a syndicated financing rather than a "
                  "control purchase; the firm's own archived page labels it Growth. The firm's May 2022 post says "
                  "AllyAlign was combined with Elite Patient Care and Provider Health Services into Curana Health (row "
                  "curana-health), so acquired by merger."))

sv = "https://www.sec.gov/Archives/edgar/data/1179079/000089256906000579/a19030orsv1.htm"
L.append(cls("alsius-corporation", status="acquired", rng="below_1b", country="US", city="Irvine",
             stage="undetermined", focus="Healthcare & Bio",
             rounds=[rnd(None, "Series C-D (exchanged from C-1, C-2 and D)", None, firm_in_round=True, source=sv,
                         source_type="filing"),
                     rnd(None, "Series E", None, firm_in_round=True, source=sv, source_type="filing"),
                     rnd(None, "Series F", None, firm_in_round=True, source=sv, source_type="filing")],
             note="Alsius, Irvine, intravascular temperature management; went public through a SPAC merger in 2007 "
                  "and sold its assets to ZOLL Medical in 2009. Its 2006 S-1 shows NEA VII holding Series C-D, E and F "
                  "preferred, but a recapitalisation left the earlier series near zero, so NEA's first round is not "
                  "established."))

L.append(cls("alta-devices-inc", status="acquired", rng="below_1b", country="US", city="Sunnyvale",
             stage="undetermined", focus="Climate & Energy",
             note="Alta Devices, Sunnyvale, thin-film GaAs solar; acquired by Hanergy in 2014. No round naming NEA "
                  "was found."))

L.append(cls("amplica-inc", status="unknown", rng="below_1b", country="US", city="Newbury Park",
             stage="undetermined", focus="Industrial & Robotics",
             note="Amplica, microwave amplifiers, on the firm's historical list as NASDAQ: AMPI; its later fate could "
                  "not be established from the sources available (pre-web era)."))

L.append(cls("anadys-pharmaceuticals-inc", rng="below_1b", country="US", city="San Diego", stage="undetermined",
             focus="Healthcare & Bio",
             note="Anadys Pharmaceuticals, San Diego; listed 2004, acquired by Roche in 2011 for about $230M. The round "
                  "NEA entered is not on record."))

L.append(cls("aprius-inc", status="defunct", rng="below_1b", country="US", city="Sunnyvale",
             stage="undetermined", focus="Data Infrastructure",
             note="Aprius, Sunnyvale, PCIe I/O virtualization; wound down around 2012. Aligned with the Lightspeed and "
                  "Menlo books."))

ap = "https://siebelschool.illinois.edu/news/kumar-s-startup-apropose-receives-1875m-seed-funding-round"
L.append(cls("apropose", status="defunct", rng="below_1b", country="US", city="Mountain View",
             city_src="web_verified", stage="Seed", stage_src="web_verified", stage_cite=ap, stage_conf="high",
             entry_date="2016-07-21", focus="SaaS",
             rounds=[rnd("2016-07-21", "Seed", 1875000, lead="New Enterprise Associates, Andreessen Horowitz",
                         firm_in_round=True, source=ap, source_type="press")],
             note="Mountain View design-analytics startup of Ranjitha Kumar; the $1.875M seed was led by NEA and a16z "
                  "(University of Illinois news, 2016-07-21), while the firm's archived page gives 2014 as the year. "
                  "Defunct, aligned with the a16z book. " + GP))

L.append(cls("arch-rock-corporation", status="acquired", rng="below_1b", country="US", city="San Francisco",
             stage="undetermined", focus="Data Infrastructure",
             note="Arch Rock, San Francisco, IP-based wireless sensor networks; acquired by Cisco in 2010 (from "
                  "knowledge). No round naming NEA was found."))

L.append(cls("autoimmune-inc", status="unknown", rng="below_1b", country="US", city="Pasadena",
             stage="undetermined", focus="Healthcare & Bio",
             note="AutoImmune Inc. (oral tolerance therapies, Nasdaq AIMM), founded in Lexington, Massachusetts and "
                  "later run from Pasadena after its trials failed in the late 1990s; its final fate could not be "
                  "established."))

fa = NEWS("avos", "AVOS Systems Closes Series A")
L.append(cls("avos", status="unknown", rng="below_1b", country="US", city="San Mateo",
             stage="Series A", stage_src="model", stage_cite=fa, stage_conf="low", entry_date="2012-04",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2012-04", "Series A", None, firm_in_round=None, source=fa, source_type="press")],
             note="AVOS Systems, the Chad Hurley and Steve Chen company (Delicious, MixBit); FinSMEs reported its "
                  "Series A in April 2012, the year the firm gives, but the page could not be read to confirm NEA in "
                  "it, hence low confidence. Delicious was sold in 2014; the company's later state is unknown."))

L.append(cls("axys-pharmaceuticals-inc", status="acquired", rng="below_1b", country="US",
             city="South San Francisco", stage="undetermined", focus="Healthcare & Bio",
             note="AXYS Pharmaceuticals (Arris and Sequana merged in 1998), South San Francisco; acquired by Celera "
                  "Genomics in 2001. The round NEA entered is not on record."))

L.append(cls("bandgap-engineering", status="unknown", rng="below_1b", country="US", city="Woburn",
             stage="undetermined", entry_date="2007", focus="Climate & Energy",
             note="Bandgap Engineering, Woburn, Massachusetts, nanostructured silicon for PV and Li-ion anodes; the "
                  "firm's page ran to 2021 as private. No report of its later state or of the round NEA entered was "
                  "found (Google News returns only the physics term)."))

L.append(cls("banjo", status="private", rng="below_1b", city="Park City", stage="undetermined", entry_date="2015",
             focus="AI & Applied AI",
             note="Banjo, real-time event detection from social and public data, Park City, Utah; renamed SafeXai in "
                  "2020 after its founder's resignation and still reported operating in 2021 (Salt Lake Tribune). The "
                  "round NEA entered in 2015 is not named in any source found."))

L.append(cls("bariatric-partners-inc", status="unknown", rng="below_1b", country="US", stage="undetermined",
             focus="Healthcare & Bio", flags=["city_unknown"],
             note="Bariatric Partners (Journey Lite surgery centers), on the firm's 2008 list only; Google News has "
                  "nothing on it, and no city, fate or round could be established."))

L.append(cls("be", country="US", country_src="web_verified", country_cite=W("Be Inc."), city="Menlo Park",
             city_src="web_verified", rng="below_1b", stage="undetermined", entry_date="1996",
             focus="Industrial & Robotics", flags=["model_disputes_source"],
             note="Be Inc. (BeBox and BeOS), Menlo Park; listed 1999, its assets bought by Palm in 2001 and the company "
                  "dissolved. The Wikidata IL country was a one-word name match (disputed). The round NEA entered in "
                  "1996 is not on record."))

wo = W("Onshape")
L.append(cls("belmont-technology", status="acquired", rng="below_1b", country="US", city="Cambridge",
             stage="undetermined", entry_date="2013", focus="SaaS",
             rounds=[rnd("2012-11", "first round", 9000000, lead="North Bridge Venture Partners, Commonwealth Capital",
                         firm_in_round=False, source=wo, source_type="press")],
             note="Belmont Technology was the placeholder name of Onshape (Wikipedia): the same company as the row "
                  "onshape. Cloud CAD, Cambridge, Massachusetts; acquired by PTC in November 2019 for $470M. Its first "
                  "$9M came from North Bridge and Commonwealth without NEA; the round NEA joined in 2013 is not named."))

L.append(cls("benu-inc", status="unknown", rng="below_1b", country="US", stage="undetermined", entry_date="2000",
             focus="Healthcare & Bio", flags=["city_unknown"],
             note="BENU, integrated health benefits for mid-size employers, first invested 2000. Not the Spark book's "
                  "Benu (Benu Networks, broadband software, Billerica): a name collision. No city, fate or round could "
                  "be established."))

L.append(cls("bethesda-research-laboratories", status="acquired", rng="below_1b", country="US",
             city="Gaithersburg", stage="undetermined", focus="Healthcare & Bio",
             note="Bethesda Research Laboratories, Gaithersburg, Maryland; combined with GIBCO in 1983 to form Life "
                  "Technologies (row life-technologies), as the firm's historical list says. No round naming NEA was "
                  "found."))

bb = "https://pulse2.com/blackbird-raises-10-million/"
L.append(cls("blackbird", status="unknown", rng="below_1b", stage="Series A", stage_src="web_verified",
             stage_cite=bb, stage_conf="high", entry_date="2019-03", focus="Consumer & Marketplaces",
             flags=["city_unknown"],
             rounds=[rnd("2019-03-12", "Series A", 10000000, lead="New Enterprise Associates", firm_in_round=True,
                         source=bb, source_type="press")],
             note="BlackBird, a California flight-sharing marketplace founded by Rudd Davis in 2016; NEA led its $10M "
                  "Series A (announced March 2019; the firm's 2018 year is the close year). Not the a16z and USV "
                  "books' Blackbird (Blackbird Labs, New York restaurant loyalty): a name collision. Its current state "
                  "and exact city could not be established."))

L.append(cls("blispay", status="acquired", rng="below_1b", country="US", city="Baltimore",
             stage="Seed", stage_src="first_party", stage_cite=ARCH("blispay"), stage_conf="medium", entry_date="2014",
             focus="Fintech & Payments",
             note="Blispay, Baltimore consumer point-of-sale credit; the firm's archived page labels the 2014 "
                  "investment seed. Acquired by Alliance Data in May 2019 (Baltimore Business Journal). " + GP))

wb = W("Bridge International Academies")
L.append(cls("bridge-international-academies", status="private", rng="below_1b", city="Nairobi",
             stage="undetermined", entry_date="2012", focus="Consumer & Marketplaces",
             flags=["model_disputes_source"],
             note="Bridge International Academies, low-cost school chain founded in Nairobi in 2008; Wikipedia lists "
                  "NEA among its investors and names NewGlobe Schools, Inc. as its parent. NewGlobe is the company's "
                  "own restructured parent, not an acquirer, so the prefilled acquired is disputed: private. Same "
                  "company as the row newglobe. The round NEA entered in 2012 is not named."))

L.append(cls("british-bio-technology-limited", status="acquired", rng="below_1b",
             country="GB", country_src="web_verified", country_cite=W("British Biotech"), city="Oxford",
             stage="undetermined", focus="Healthcare & Bio",
             note="British Biotechnology (British Biotech plc from its 1992 listing), Oxford; merged with RiboTargets "
                  "into Vernalis in 2003 (Wikipedia). The round NEA entered is not on record."))

cm = ("https://www.globenewswire.com/news-release/2026/09/09/3358756/0/en/camara-launches-with-broad-institute-"
      "collaboration-to-develop-novel-cardiometabolic-and-renal-medicines.html")
L.append(cls("camara", status="private", rng="below_1b", country="DK", country_src="web_verified", country_cite=cm,
             city="Copenhagen", city_src="web_verified",
             stage="Seed", stage_src="web_verified", stage_cite=cm, stage_conf="high", entry_date="2026-09-09",
             grad="censored", focus="Healthcare & Bio",
             rounds=[rnd("2026-09-09", "Seed", None, lead=None, firm_in_round=True, source=cm, source_type="company")],
             note="CaMaRa launched from Copenhagen on 2026-09-09 with a seed financing from Forbion, Novo Holdings, NEA "
                  "and RA Capital (company release); inside the censoring window."))

L.append(cls("cape", status="unknown", rng="below_1b", country="US", stage="undetermined", entry_date="2014",
             focus="Industrial & Robotics", flags=["city_unknown"],
             note="Cape Productions, an end-to-end drone video service the firm first backed in 2014. Not the a16z, "
                  "Bain Capital Ventures and IVP books' Cape (privacy mobile carrier, Washington): a name collision. "
                  "Its fate, city and the round NEA entered could not be established."))

jl.write("c12a", L)
