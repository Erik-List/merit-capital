"""Judge c9, batch 17 (queue/batch-017.json): listed members, classification (plus X1/D5 membership where the
record shows the listing is a public purchase or a fund)."""
import json

import judge_lib as jl
from judge_lib import cls, rnd, verdict

BASE = {r["slug"]: r for r in json.loads((jl.INV / "companies/base.json").read_text())}


def edgar(slug, i=0):
    return BASE[slug]["edgar_links"].split("; ")[i].strip()


CMC = "https://companiesmarketcap.com/{}/marketcap/"
WV = {"valuation_range_source": "web_verified"}
L = []

# ---- membership: X1 (PIPE into a listed company) and D5 (fund-shaped)
L.append(verdict("repros-therapeutics", "not_member",
                 "X1/R2: the firm labels it Public/PIPES (2009); the position is Growth Equity Opportunities Fund with "
                 "NEA 12 on a 13G of 2009-03-27 into Repros, listed on Nasdaq since the 1990s (as Zonagen), and no NEA "
                 "private round before the listing is on record, so it is a listed purchase.",
                 ec="fund_filing", conf="high", cite=edgar("repros-therapeutics")))
L.append(verdict("seattle-genetics", "not_member",
                 "X1: the firm's own listing labels it Public/PIPES with a 2009 first investment and Paul Walker's "
                 "public-equity deal team; Seattle Genetics had been listed on Nasdaq since 2001 and no NEA private "
                 "round before the listing is on record.",
                 ec="site_listing", conf="high", cite=jl.SITE("seattle-genetics")))
L.append(verdict("savara", "not_member",
                 "X1/R2: the firm labels it Public/PIPES (2021); NEA's 13D of 2021-03-16 reports a private placement "
                 "into Savara, listed since its 2017 merger with Mast Therapeutics, and no NEA private round came "
                 "before the listing.",
                 ec="fund_filing", conf="high", cite=edgar("savara")))
L.append(verdict("rigel-pharmaceuticals", "not_member",
                 "X1: the firm labels it Public/PIPES with a 2010 first investment, and its own 2015 release places "
                 "Rigel in NEA's public healthcare investment practice; Rigel had been listed on Nasdaq since 2000 and "
                 "no NEA private round before the listing is on record.",
                 ec="site_listing", conf="high", cite=jl.POST("nea-names-frank-torti-and-rick-yang")))
L.append(verdict("rock-health", "not_member",
                 "D5: Rock Health is a digital-health seed fund and accelerator (the firm's own listing: it 'funds and "
                 "supports startups'); a fund-shaped entry, not an operating company.",
                 ec="site_listing", conf="medium", cite=jl.SITE("rock-health")))

# ---- classification
L.append(cls("resilience", status="private", rng="below_1b", city="Blue Ash", focus="Healthcare & Bio",
             stage="Growth", stage_src="web_verified", stage_conf="medium",
             stage_cite=jl.NEWS("resilience", "Latham Advises RESILIENCE"), entry_date="2020-11",
             flags=("stage_disputes_band", "model_disputes_source"),
             rounds=[rnd("2020-11", "Series B", 750000000, None, True,
                         jl.NEWS("resilience", "Latham Advises RESILIENCE"), "press")],
             note="National Resilience, biomanufacturing, launched in 2020 with a Series B of about $750M naming "
                  "ARCH, 8VC, GV and NEA (Latham, 2020-11); no earlier NEA round is on record. The prefilled Seed "
                  "reads a 2015 Form D of a different Resilience (Duxbury MA, incorporated 2014), so it is disputed. "
                  "No priced post-money was published and the company has since wound down plants: below $1B, city "
                  "aligned with the GV and Lux rows."))
L.append(cls("retrieve", status="private", rng="below_1b", city="Manchester", city_src="formd_address",
             focus="SaaS",
             note="Retrieve, virtual teaching software (Manchester NH on its Form D); Form D filings run to 2022 and "
                  "nothing reports a sale or shutdown. Graduation left for the graduation pass."))
L.append(cls("revelio", status="private", rng="below_1b", country="US", stage="undetermined", entry_date="2022",
             focus="Healthcare & Bio", flags=("city_unknown",), rounds=[],
             note="Revelio Therapeutics, tumor-specific biologics (Ali Behbahani on the board, the firm's 2022 "
                  "first investment, stage label Early). Its site and the one trade item found (MM&M, 2025-03) gave "
                  "no location or named round; stage undetermined."))
L.append(cls("revelle-aesthetics", status="acquired", rng="below_1b", city="Mountain View",
             city_src="formd_address", focus="Healthcare & Bio",
             note="Cellulite device company incubated at Mountain View (its Form D address); the firm's exit line "
                  "says acquired by Tiger Aesthetics Medical."))
L.append(cls("revspring", status="private", rng="below_1b", country="US", city="Wixom", stage="Growth",
             stage_src="model", stage_conf="medium", entry_date="2024", focus="Healthcare & Bio",
             rounds=[rnd("2024-03-12", "Acquisition by Frazier Healthcare Partners", None,
                         "Frazier Healthcare Partners", None,
                         jl.NEWS("revspring", "Announces Acquisition of RevSpring"), "press")],
             note="RevSpring, patient payment and engagement platform, a mature company Frazier Healthcare Partners "
                  "bought in March 2024 (Business Wire headline; the release was not readable to confirm NEA's "
                  "name). NEA's 2024 entry, with a board seat, can only be a growth-scale minority position beside "
                  "the buyer; if the record shows NEA sharing control, R1's control test applies."))
L.append(cls("rf-monolithics", status="acquired", rng="below_1b", country="US", city="Dallas",
             stage="undetermined", entry_date="1994", focus="Industrial & Robotics",
             note="SAW radio-frequency components, Dallas; Murata bought it in 2012 (the firm's exit line). The "
                  "Public/PIPES label does not make it an X1 row: NEA general partner Cornelius Bond sat on its "
                  "board from November 1992 (2001 proxy), before its 1994 listing. No round is named."))
L.append(cls("rhythm-pharmaceuticals", status="public", rng="1b_plus", usd=6560000000, val_src="web_verified",
             val_cite=CMC.format("rhythm-pharmaceuticals"), asof="2026-09-29", city="Boston",
             city_src="formd_address", focus="Healthcare & Bio", extra=WV,
             note="Market cap $6.56B at the 2026-09-29 close (companiesmarketcap), replacing the older float."))
L.append(cls("ringcube", status="acquired", rng="below_1b", city="Mountain View", city_src="formd_address",
             stage="undetermined", entry_date="2006", focus="Data Infrastructure", rounds=[],
             note="Desktop virtualization workspaces; Citrix bought it in 2011 (the firm's exit line). The firm's "
                  "first investment is 2006; its first partner-matched Form D is 2009 and no named round was "
                  "found, so the stage is undetermined."))
L.append(cls("robinhood", status="public", rng="100b_plus", usd=104490000000, val_src="web_verified",
             val_cite=CMC.format("robinhood"), asof="2026-09-29", city="Menlo Park", city_src="formd_address",
             stage="Growth", stage_src="web_verified", stage_cite=jl.W("Robinhood Markets"), stage_conf="high",
             entry_date="2015-05", focus="Fintech & Payments", flags=("stage_disputes_band",), extra=WV,
             rounds=[rnd("2013-12", "Seed", 3000000, "Index Ventures", False, jl.W("Robinhood Markets"), "press"),
                     rnd("2014-09", "Series A", 13000000, "Index Ventures", False, jl.W("Robinhood Markets"), "press"),
                     rnd("2015-05", "Series B", 50000000, "New Enterprise Associates", True,
                         jl.W("Robinhood Markets"), "press"),
                     rnd("2017-04", "Series C", 110000000, None, None, jl.W("Robinhood Markets"), "press")],
             note="NEA led the $50M Series B of May 2015 (Wikipedia), matching the firm's 2015 first investment; the "
                  "prefilled 2019 Form D date was a later round. Market cap $104.49B at the 2026-09-29 close "
                  "(companiesmarketcap), one day fresher than the sibling rows' $104.71B; the old float is replaced."))
L.append(cls("rocket", status="private", rng="below_1b", country="US", city="San Francisco",
             stage="undetermined", entry_date="2017", focus="SaaS",
             flags=("model_disputes_source",),
             extra={"valuation_source": None, "valuation_asof": None, "valuation_range_source": None,
                    "valuation_confidence": None, "is_public": False, "public_since": None},
             note="Rocket (getrocket.com), a tech recruiting firm with AI recruiting software; its site lists San "
                  "Francisco first among its offices. The prefilled public status and $14.9B float belong to "
                  "Rocket Companies, a name join, and are disputed. No round is named. Accel's 'Rocket' (Surat) is "
                  "a different company."))
L.append(cls("rocket-chat", status="private", rng="below_1b", country="BR", country_src="web_verified",
             country_cite=jl.W("Rocket.Chat"), city="Porto Alegre", city_src="web_verified", focus="SaaS",
             note="Open-source team chat created in Porto Alegre, Brazil, where engineering stays (Wikipedia); its "
                  "Form D issuer is a Cayman holding company. No priced round near $1B. Graduation left for the "
                  "graduation pass (Form D shows a $19M raise in 2021)."))
L.append(cls("roka-bioscience-inc", country="US", city="Warren", city_src="web_verified", stage="undetermined",
             entry_date="2009", rng="below_1b", focus="Healthcare & Bio",
             rounds=[rnd(None, "Series C", 20000000, None, True, jl.FTS("Roka", "S-1"), "filing"),
                     rnd("2011-12-19", "Series D", None, None, True, jl.FTS("Roka", "S-1"), "filing"),
                     rnd("2013-06", "Series E", 25000000, None, None, jl.FTS("Roka", "S-1"), "filing")],
             note="Molecular food-safety assays spun out of Gen-Probe in 2009, principal office Warren NJ (S-1). NEA "
                  "13 bought Series C and D (S-1 certain transactions), but the S-1 does not date the 2009 "
                  "formation round NEA first joined, so the stage is undetermined."))
L.append(cls("rotation-medical", status="acquired", rng="below_1b", city="Plymouth", city_src="formd_address",
             stage="undetermined", entry_date="2006", focus="Healthcare & Bio",
             note="Rotator cuff implant company; Smith & Nephew bought it in 2017 (the firm's exit line). The firm's "
                  "first investment is 2006 and no round is named."))
L.append(cls("safebase", status="acquired", rng="below_1b", country="US", city="San Francisco",
             city_src="web_verified", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://www.prnewswire.com/news-releases/safebase-inc-raises-18-million-series-a-round-to-develop-security-trust-centers-for-companies-301499643.html",
             entry_date="2022-03-10", focus="Security",
             rounds=[rnd("2022-03-10", "Series A", 18000000, "New Enterprise Associates", True,
                         "https://www.prnewswire.com/news-releases/safebase-inc-raises-18-million-series-a-round-to-develop-security-trust-centers-for-companies-301499643.html",
                         "company")],
             note="NEA led the $18M Series A (company release, San Francisco, 2022-03-10); the firm lists 2021 as "
                  "its close year. Drata bought SafeBase in 2025 (the firm's exit line and its own Zania post)."))
L.append(cls("saferide-health", status="private", rng="below_1b", country="US", city="Portland",
             stage="Seed", stage_src="first_party", stage_cite=jl.SITE("saferide-health"), stage_conf="medium",
             entry_date="2017", focus="Healthcare & Bio",
             note="Non-emergency medical transport platform; the firm's own listing labels the entry Seed (2017). "
                  "Graduation left for the graduation pass."))
L.append(cls("sagimet-biosciences", city="San Mateo", city_src="formd_address", stage="undetermined",
             entry_date="2009", focus="Healthcare & Bio",
             note="Sagimet is 3-V Biosciences renamed (same CIK 1400118); the base carries both rows. NEA 13 and NEA "
                  "Ventures 2009 held it from 2009 (S-1 investor rights agreement), but no round is named."))
L.append(cls("sakana-ai", status="private", rng="1b_plus", usd=2537940155, val_src="web_verified",
             val_cite=jl.NEWS("sakana-ai", "Series B at $2.65B"), asof="2025-11-20", city="Tokyo",
             city_src="web_verified", stage="Series A", stage_src="first_party",
             stage_cite=jl.POST("our-investment-in-sakana"), stage_conf="high", entry_date="2024-09-04",
             focus="AI & Applied AI", extra=WV,
             rounds=[rnd("2024-01", "Seed", 30000000, "Lux Capital, Khosla Ventures", False,
                         jl.POST("our-investment-in-sakana"), "firm"),
                     rnd("2024-09-04", "Series A", None, "NEA, Khosla Ventures, Lux Capital", True,
                         jl.POST("our-investment-in-sakana"), "firm"),
                     rnd("2025-11-17", "Series B", 135000000, None, None,
                         jl.NEWS("sakana-ai", "Series B at $2.65B"), "press")],
             note="The firm's own post: NEA co-led the Series A with existing investors Khosla and Lux (Tokyo, "
                  "2024-09-04). Momentum check 2026-09-30 (Google News): the $135M Series B of 2025-11-17 at about "
                  "JPY 400B post-money (reported as $2.65B); JPY 400.00B @ ECB 2025-11-20 = $2.54B, aligned with "
                  "the Lux row."))
L.append(cls("salesforce-com", status="public", rng="100b_plus", usd=185430000000, val_src="web_verified",
             val_cite=CMC.format("salesforce"), asof="2026-09-29", city="San Francisco", city_src="formd_address",
             stage="Growth", stage_src="first_party", stage_cite=jl.SITE("salesforce-com"), stage_conf="medium",
             entry_date="2002", focus="SaaS", flags=("stage_disputes_band",), extra=WV,
             note="The firm lists a 2002 Growth investment, before the 2004 listing, and its 2012 post says NEA "
                  "invested 'just under a decade ago'; the prefilled 2013 Form D date is not NEA's entry. Market "
                  "cap $185.43B at the 2026-09-29 close (companiesmarketcap)."))
L.append(cls("salix", country="US", city="Gaithersburg", stage="undetermined", entry_date="1998",
             rng="below_1b", focus="Data Infrastructure",
             note="Salix Technologies, class-independent telecom switching (Gaithersburg MD); Tellabs bought it in "
                  "1999 (the firm's exit line). No round is named."))
L.append(cls("samaya-ai", status="private", rng="below_1b", country="US", stage="undetermined",
             entry_date="2025-05-14", focus="AI & Applied AI", flags=("city_unknown",),
             extra={**WV, "valuation_citation": jl.NEWS("samaya-ai", "Announces $43.5m in Funding Led by NEA")},
             rounds=[rnd("2025-05-14", "Financing (round not named)", 43500000, "New Enterprise Associates", True,
                         jl.NEWS("samaya-ai", "Announces $43.5m in Funding Led by NEA"), "company")],
             note="NEA led a $43.5M financing (company release and the firm's post, 2025-05-14); neither names the "
                  "round and vendors disagree on how many rounds it spans, so the stage is undetermined. Momentum "
                  "check 2026-09-30 (Google News and one web search): a further 2026 round is reported but no "
                  "priced $1B+ round; vendor estimates near $157M are not marks."))
L.append(cls("sana", status="acquired", rng="below_1b", country="SE", country_src="web_verified",
             country_cite="https://eqtgroup.com/about/current-portfolio/sana-labs", city="Stockholm",
             stage="Growth", stage_src="first_party", stage_cite=jl.POST("our-investment-in-sana-labs"),
             stage_conf="high", entry_date="2023-06-01", focus="AI & Applied AI",
             rounds=[rnd("2022-12", "Series B", 34000000, "Menlo Ventures", False, None, "firm"),
                     rnd("2023-06-01", "Investment after the Series B", None, None, True,
                         jl.POST("our-investment-in-sana-labs"), "firm")],
             note="Sana Labs (Stockholm). The firm's own post: NEA met the company just after it agreed its Series "
                  "B and invested about six months later, so the entry is after the B. Workday completed the "
                  "acquisition on 2025-11-04 (PR Newswire headline); aligned with the EQT and Menlo rows."))
L.append(cls("sasken-communications", status="public", rng="below_1b", country="IN", country_src="web_verified",
             country_cite="https://www.sasken.com/", city="Bengaluru", city_src="web_verified", stage="Growth",
             stage_src="first_party", stage_cite=jl.SITE("sasken-communications"), stage_conf="medium",
             entry_date="2005", focus="Data Infrastructure",
             note="Embedded software and R&D services, corporate office Domlur, Bengaluru (its own site); listed on "
                  "NSE. The firm labels the 2005 entry Growth, before the September 2005 listing. Its market cap is "
                  "a few hundred million dollars, well below $1B."))
L.append(cls("satori-pharmaceuticals", status="unknown", rng="below_1b", city="Cambridge",
             city_src="formd_address", focus="Healthcare & Bio",
             note="Alzheimer's drug developer, Cambridge MA (Form D); filings stop in 2012, the firm dropped it "
                  "from the live list and Google News (2026-09-30) found nothing on its fate."))
L.append(cls("say-media", status="acquired", rng="below_1b", city="San Francisco", stage="Growth",
             stage_src="first_party", stage_cite=jl.SITE("say-media"), stage_conf="high", entry_date="2012-07-19",
             focus="Media, Gaming & Advertising",
             rounds=[rnd("2012-07-19", "Growth round", 27000000, "New Enterprise Associates", True,
                         jl.POST("investing-in-the-digital-media-revolution"), "firm")],
             note="SAY Media (formerly VideoEgg, founded 2005). The firm's own post: NEA led a $27M round on "
                  "2012-07-19, labelled Growth on its listing. Maven took over SAY Media in 2018 (Business Insider, "
                  "2018-08-28); aligned with the First Round row."))
L.append(cls("sbc", status="private", rng="below_1b", country="US", stage="undetermined", entry_date="2024",
             focus="Crypto & Web3", flags=("city_unknown",), rounds=[],
             note="Stablecoin.xyz, operator of the SBC stablecoin (The Stable Coin Company); its site names no "
                  "location or round. Momentum check 2026-09-30 (Google News): no item, so no priced round found."))
L.append(cls("sci-solutions", status="acquired", rng="below_1b", country="US", city="Seattle",
             stage="undetermined", entry_date="1998", focus="Healthcare & Bio",
             note="Hosted patient-access software for providers, Seattle; R1 RCM bought it in 2020 (the firm's exit "
                  "line). No round is named."))
L.append(cls("sciencelogic", status="private", rng="below_1b", city="Reston", city_src="formd_address",
             focus="Data Infrastructure",
             note="IT operations monitoring, Reston VA (Form D); NEA's $15M Series A of 2010 (Wikipedia). Later "
                  "rounds were raised without a published post-money."))
L.append(cls("scopely", status="acquired", rng="below_1b", city="Culver City", city_src="web_verified",
             stage="Seed", stage_src="web_verified", stage_cite=jl.W("Scopely"), stage_conf="high",
             entry_date="2013", grad="graduated", grad_src="web_verified", grad_cite=jl.W("Scopely"),
             grad_conf="high", focus="Media, Gaming & Advertising",
             rounds=[rnd("2013", "Seed", 8500000, "Anthem Venture Partners", True, jl.W("Scopely"), "press"),
                     rnd("2014", "Series A", 35000000, "Evolution Media", None, jl.W("Scopely"), "press"),
                     rnd("2016", "Series B", 55000000, None, None, jl.W("Scopely"), "press")],
             note="NEA joined the $8.5M seed led by Anthem (Wikipedia, 2013; the firm's listing says Seed, 2011). "
                  "Graduated: $35M Series A of 2014. Savvy Games Group bought Scopely for $4.9B, closed July 2023; "
                  "aligned with the Battery, Felicis and Headline rows."))
L.append(cls("scout-rfp", status="acquired", rng="below_1b", city="San Francisco", city_src="formd_address",
             stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite="https://techcrunch.com/2015/01/27/automating-the-rfp-process-nets-scout-rfp-2-75-million/",
             entry_date="2015-01-27", grad="graduated", grad_src="web_verified", grad_conf="high",
             grad_cite="https://techcrunch.com/2017/06/07/scout-rfp-raises-15-5-million-to-help-companies-manage-purchases/",
             focus="SaaS",
             rounds=[rnd("2015-01-27", "Seed", 2750000, "New Enterprise Associates", True,
                         "https://techcrunch.com/2015/01/27/automating-the-rfp-process-nets-scout-rfp-2-75-million/",
                         "press"),
                     rnd("2016-07", "Series A", 9000000, None, None, None, "press"),
                     rnd("2017-06-07", "Series B", 15500000, "Menlo Ventures", True,
                         "https://techcrunch.com/2017/06/07/scout-rfp-raises-15-5-million-to-help-companies-manage-purchases/",
                         "press"),
                     rnd("2019-01-15", "Series C", 33000000, "Scale Venture Partners", None, None, "press")],
             note="NEA led the $2.75M seed (TechCrunch, 2015-01-27; the firm's listing says Seed). Graduated: a $9M "
                  "Series A in July 2016 (FinSMEs headline) and the cited $15.5M Series B of 2017-06-07 led by "
                  "Menlo. Workday completed the $540M purchase in December 2019; aligned with the GV and Menlo rows."))
L.append(cls("scratch-music-group", status="private", rng="below_1b", country="US", city="New York",
             stage="Seed", stage_src="first_party", stage_cite=jl.SITE("scratch-music-group"), stage_conf="medium",
             entry_date="2013", focus="Media, Gaming & Advertising",
             note="Scratch (DJ academy and event DJs), whose event business rebranded in 2023 (PR Newswire); the "
                  "firm's own listing labels the entry Seed (2013). Graduation left for the graduation pass."))
L.append(cls("semiconductor-manufacturing-international-corporation-smic", status="public", rng="10b_plus",
             usd=66180000000, val_src="web_verified", val_cite=CMC.format("smic"), asof="2026-09",
             country="CN", country_src="web_verified",
             country_cite=jl.W("Semiconductor Manufacturing International Corporation"), city="Shanghai",
             city_src="web_verified", stage="Growth", stage_src="first_party",
             stage_cite=jl.SITE("semiconductor-manufacturing-international-corporation-smic"), stage_conf="medium",
             entry_date="2003", focus="Industrial & Robotics", extra=WV,
             note="Shanghai foundry (Wikipedia). The firm labels its 2003 entry Growth, before the 2004 listing; "
                  "Richard Kramlich joined the board in 2003 (F-1). Market cap $66.18B as of September 2026 "
                  "(companiesmarketcap)."))
L.append(cls("sengled", status="unknown", rng="below_1b", country="CN", country_src="web_verified",
             country_cite=jl.SITE("sengled"), city="Shanghai", stage="Growth", stage_src="first_party",
             stage_cite=jl.SITE("sengled"), stage_conf="medium", entry_date="2010", focus="Climate & Energy",
             note="Smart LED lighting; the firm's own listing calls it a green lighting company in China and labels "
                  "the 2010 entry Growth. Its cloud service collapsed in 2025 and Amazon ended its Alexa skill (The "
                  "Verge, 2025-08-04); no shutdown or sale is documented, so the state is unknown."))
L.append(cls("senseonics", country="US", city="Germantown", stage="undetermined", entry_date="1997",
             focus="Healthcare & Bio",
             note="Implantable glucose sensors (formerly Sensors for Medicine and Science), Germantown MD; NEA 9 "
                  "signed the 2015 registration rights agreement, but no entry round is named."))
L.append(cls("senti-biosciences", city="South San Francisco", city_src="formd_address", focus="Healthcare & Bio"))
L.append(cls("sentons", status="private", rng="below_1b", city="Sunnyvale", city_src="formd_address",
             focus="Industrial & Robotics",
             note="Ultrasound touch and force sensing chips; Google News (2026-09-30) reports no sale or shutdown. "
                  "Graduation left for the graduation pass."))
L.append(cls("sentry", status="private", rng="1b_plus", usd=3000000000, val_src="web_verified",
             val_cite="https://www.helpnetsecurity.com/2022/05/06/sentry-funding/", asof="2022-05",
             country="US", city="San Francisco", stage="Series A", stage_src="first_party",
             stage_cite=jl.POST("continued-partnership-with-sentry"), stage_conf="high", entry_date="2016",
             focus="DevTools & APIs", flags=("stale",), extra=WV,
             rounds=[rnd("2016", "Series A", 9000000, "New Enterprise Associates", True,
                         jl.POST("continued-partnership-with-sentry"), "firm"),
                     rnd("2022-05", "Series E", 90000000, "BOND, Accel", True,
                         "https://www.helpnetsecurity.com/2022/05/06/sentry-funding/", "press")],
             note="The firm's own post: NEA led the 2016 Series A (Accel's seed came first). The $90M Series E of "
                  "May 2022 valued Sentry at more than $3B (Help Net Security), older than 24 months so flagged "
                  "stale; the Accel row still reads below $1B without this cited mark."))
L.append(cls("sepracor", status="acquired", rng="below_1b", country="US", city="Marlborough",
             stage="undetermined", entry_date="1985", focus="Healthcare & Bio",
             note="Founded 1984, listed 1991; Dainippon Sumitomo bought it for $2.6B and renamed it Sunovion "
                  "(Wikipedia). No round is named."))
L.append(cls("serious-energy", status="unknown", rng="below_1b", city="Sunnyvale", city_src="formd_address",
             focus="Climate & Energy",
             note="Serious Energy is Serious Materials renamed (same Form D CIK 1418835; the base carries both "
                  "rows). It hit a spate of troubles in 2012 (SFGATE), sold Kensington Windows back in 2013 and its "
                  "fiberglass window division later; no final sale or shutdown is documented."))
L.append(cls("serious-materials-inc", status="unknown", rng="below_1b", city="Sunnyvale", city_src="formd_address",
             stage="Growth", stage_src="first_party", stage_cite=jl.SITE("serious-energy"), stage_conf="medium",
             entry_date="2007", focus="Climate & Energy",
             note="Duplicate of serious-energy (same Form D CIK 1418835, renamed Serious Energy in 2011); stage and "
                  "year from the firm's own listing of the renamed company (Growth, 2007)."))

L.append(cls("second-front", status="private", rng="below_1b", usd=750000000, val_src="web_verified",
             val_cite=jl.NEWS("second-front", "$750 Million Valuation"), asof="2024-09-13", city="Arlington",
             focus="DevTools & APIs", flags=("stale",), extra=WV,
             rounds=[rnd("2023-11-28", "Series B", None, "New Enterprise Associates", True,
                         jl.POST("our-investment-in-second-front"), "firm"),
                     rnd("2024-09-13", "Series C", 70000000, "Salesforce Ventures", None,
                         jl.NEWS("second-front", "$750 Million Valuation"), "press")],
             note="The firm's own post: NEA led the Series B (2023-11-28). Momentum check 2026-09-30 (Google News): "
                  "the $70M Series C of 2024-09-13 priced it at $750M (Forbes), below $1B and older than 24 months; "
                  "no later priced round. City aligned with the Battery row."))

jl.write("c9a", L)
