"""PRO-80 Bessemer, judge j06, file b: the rest of batch 11 (rows that needed a news query or a company page).
Run as NQ_TAG=j06 python3 judgments-j06b.py."""
import json

import judge_lib as jl
from judge_lib import ARCH, NEWS, POST, SITE, W, cls, rnd

SIBS = json.loads((jl.INV / "scratch" / "siblings.json").read_text())
BVP = "Bessemer Venture Partners"
CHECK = "Momentum check 2026-10-01 (Google News): "


def SIB(slug, investor):
    m = [x for x in SIBS.get(slug, []) if x["investor"] == investor and x.get("val_cite")]
    if len(m) != 1:
        raise SystemExit(f"SIB({slug!r}, {investor!r}) matched {len(m)}")
    return m[0]["val_cite"]


L = []

BAE = NEWS("silversky", "BAE Systems completes SilverSky")
L.append(cls("silversky", status="acquired", rng="below_1b", stage="undetermined", entry_date="2007-08-09",
             country="US", city="New York", city_src="web_verified", focus="Security", rounds=[],
             note="acq. by BAE Systems, 2014 ($232.5M; BAE's release places the company, legally Perimeter "
                  "Internetworking, in New York); a private group bought it back from BAE in 2020. The firm's own "
                  "investment date is 2007-08-09 (as Perimeter eSecurity); no source found names that round, so the "
                  "stage is undetermined."))

SM_SEED = NEWS("simply-measured", "rings up $750,000")
L.append(cls("simply-measured", status="acquired", rng="below_1b", stage="undetermined", entry_date="2012-10-30",
             city="Seattle", focus="SaaS",
             rounds=[rnd("2011-07-20", "seed financing", 750000, None, False, SM_SEED, "press"),
                     rnd("2012-10-30", "round with Bessemer", None, None, True, ARCH("simply-measured"), "firm"),
                     rnd("2014-03-10", "later round", 20239964, None, True, jl.FORMD_CITE("simply-measured", 1),
                         "filing")],
             note="acq. by Sprout Social, December 2017. The firm's own investment date is 2012-10-30, after the 2011 "
                  "seed financing and before the 2014 Form D the band read (so that date is replaced); no page read "
                  "names the 2012 round, so the stage is undetermined and a later pass could settle it."))

L.append(cls("siteadvisor-inc", status="acquired", rng="below_1b", stage="undetermined", entry_date="2005-03-09",
             country="US", city="Boston", focus="Security", rounds=[],
             note="acq. by McAfee, April 2006. The firm's own investment date is 2005-03-09, the company's founding "
                  "year; no source found names the round, so the stage is undetermined (as the General Catalyst book)."))

SIX = NEWS("sixfold-ai", "raises $15m")
L.append(cls("sixfold-ai", status="private", rng="below_1b",
             stage="Seed", stage_src="web_verified", stage_cite=SIX, stage_conf="high", entry_date="2023",
             grad="graduated", grad_src="web_verified", grad_cite=SIX, grad_conf="high",
             country="US", city="New York", focus="AI & Applied AI",
             rounds=[rnd("2023", "Seed", None, None, True, SIX, "press"),
                     rnd("2024-06-06", "Series A", 15000000, "Salesforce Ventures", True, SIX, "press")],
             note="FinTech Global, 2024-06-06: the $15M Series A was led by Salesforce Ventures with previous "
                  "investors Bessemer and Crystal Venture Partners, who had provided the seed funding. " + CHECK +
                  "a $30M round is reported in 2026, no $1B priced round."))

L.append(cls("skippr", status="private", rng="below_1b", stage="undetermined", entry_date="2020",
             country="GB", country_src="web_verified", country_cite="https://skippr.ai/", city="London",
             focus="AI & Applied AI", rounds=[],
             note="The listing's company site (skippr.com) now redirects to skippr.ai, an AI demo and onboarding "
                  "product made in London; the firm's Israel team (Adam Fisher, Yael Schiff) holds the position. No "
                  "round is on record in the firm's posts or the press, so the stage is undetermined; the listing's "
                  "2020 partnered year sits before its own 2022 founding year. " + CHECK + "no funding report at all."))

L.append(cls("smashfly", status="acquired", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2015-12-18", country="US", city="Concord", focus="SaaS",
             rounds=[rnd("2015-12-18", "growth round led by Bessemer", 22000000, BVP, True, None, "press")],
             note="acq. by Symphony Talent, November 2019. Bessemer led the $22M growth round announced in January "
                  "2016, after OpenView's earlier round (named from knowledge; the news query returned nothing to "
                  "cite)."))

L.append(cls("smilebox", status="acquired", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2007-12-05", country="US", city="Redmond", focus="Consumer & Marketplaces",
             rounds=[rnd("2007-12", "Series B", 7000000, BVP, True, None, "press"),
                     rnd("2009-09-01", "insider round", 399999, None, True, jl.FORMD_CITE("smilebox", 0), "filing")],
             note="acq. by IncrediMail (Perion), 2011. Bessemer led the $7M Series B of December 2007, after Frazier's "
                  "Series A (named from knowledge); the firm's own investment date 2007-12-05 replaces the 2009 Form D "
                  "date, which is a small insider round."))

L.append(cls("smule", status="private", rng="below_1b", stage="undetermined", entry_date="2008-06-25",
             city="Salt Lake City", city_src="formd_address", focus="Consumer & Marketplaces",
             rounds=[rnd("2008-06-25", "first round with Bessemer", None, None, True, ARCH("smule"), "firm"),
                     rnd("2009-12-15", "later round", 8000000, None, None, None, "filing"),
                     rnd("2014-04-10", "later round", 16600000, None, None, NEWS("smule", "Raises $16.6M"), "press"),
                     rnd("2017-05-08", "round led by Tencent", 54000000, "Tencent", None,
                         NEWS("smule", "Tencent leads $54m"), "press")],
             note="The firm's own investment date is 2008-06-25, the founding year, three years before the Form D the "
                  "band read; no page names that 2008 round, so the stage is undetermined. HQ Salt Lake City (the "
                  "2022 Form D and Wikipedia; formerly San Francisco). The 2017 Tencent round carried no $1B mark."))

SOL = NEWS("solomon", "raises $6.8 mn")
L.append(cls("solomon", status="private", rng="below_1b", city="New York", city_src="formd_address",
             focus="AI & Applied AI",
             rounds=[rnd("2024", "earlier round", 3000000, "Crew Capital", None, SOL, "press"),
                     rnd("2025-07-23", "round from Bessemer", 6800000, BVP, True, SOL, "press")],
             note="Solomon Labs, a Korean-founded tax AI startup filing from New York. Maeil Business, 2025-07-23: "
                  "$6.8M from Bessemer, about $10M raised in all including $3M in 2024 from Crew Capital and Base "
                  "Ventures; the round is not named, so the Form D band stands. " + CHECK + "no $1B priced round."))

SOUF = NEWS("souffl-therapeutics", "Fierce Biotech")
L.append(cls("souffl-therapeutics", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=SOUF, stage_conf="high", entry_date="2024",
             country="US", city="Watertown", city_src="web_verified", focus="Healthcare & Bio",
             rounds=[rnd("2025-10-07", "Series A", 200000000, None, True, SOUF, "press")],
             note="Fierce Biotech, 2025-10-07: the company launched with a $200M series A whose investors include "
                  "Bessemer, Arch, Vida and Polaris; the entry year is the listing's partnered year 2024. HQ Watertown, "
                  "Massachusetts (the company's own site)."))

SPR = NEWS("spruce", "raises $4.5M")
L.append(cls("spruce", status="acquired", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=SPR, stage_conf="high", entry_date="2017-04-19",
             city="New York", focus="Fintech & Payments", flags=["stage_disputes_band"],
             rounds=[rnd("2017-05-26", "Series A", 4500000, None, True, SPR, "press"),
                     rnd("2021-06-02", "Series C", 60000000, "Zigg Capital", None,
                         NEWS("spruce", "Series C Funding Led by Zigg"), "press")],
             note="acq. by Zillow Group, September 2023 (the firm's listing). The Real Deal, 2017-05-26: $4.5M in a "
                  "Series A funding round from Bessemer, Omidyar Network and Third Prime; the firm's own investment "
                  "date is 2017-04-19, so the band's Growth label, read off the 2021 Series C filing, is disputed. The "
                  "a16z book's Spruce is another company (Spruce Systems)."))

L.append(cls("staircase", status="private", rng="below_1b", city="Philadelphia", city_src="formd_address",
             focus="Fintech & Payments",
             note="Mortgage API company; its site still serves the platform and no sale or shutdown is reported. " +
                  CHECK + "no round after the $18M of March 2021, no $1B priced round."))

STS = NEWS("statespace", "Series C funding")
L.append(cls("statespace", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=STS, stage_conf="high", entry_date="2021-09-15",
             country="US", city="New York", focus="Media, Gaming & Advertising",
             rounds=[rnd("2021-09-15", "Series C", 50000000, "Khosla Ventures", True, STS, "press")],
             note="GamesIndustry.biz, 2021-09-16: $50M Series C, with Bessemer named among the new investors joining "
                  "the round. Maker of Aim Lab; city and band as the Khosla and Lux books."))

STL = NEWS("streamloots", "Caspar Lee")
L.append(cls("streamloots", status="private", rng="below_1b", stage="Series A", stage_src="model",
             stage_conf="medium", entry_date="2020", country="ES", country_src="web_verified", country_cite=STL,
             city="Valencia", focus="Media, Gaming & Advertising",
             rounds=[rnd("2020-10", "Series A", 4200000, BVP, True, None, "press"),
                     rnd("2020-11-04", "creator fund investment", None, None, False, STL, "press")],
             note="Bessemer led the Series A of October 2020 (named from knowledge; Tubefilter, 2020-11-04, confirms "
                  "a prior $5.6M investment from Bessemer in the Spanish startup without naming the round). No later "
                  "round found."))

L.append(cls("strella", status="private", rng="below_1b",
             stage="Series A", stage_src="first_party", stage_cite=POST("meet-the-founders-of-strella"),
             stage_conf="high", entry_date="2025-10-16", country="US", city="New York", focus="AI & Applied AI",
             rounds=[rnd("2024-10-15", "Seed", 4000000, "Decibel Partners", False, NEWS("strella", "raises $4M"), "press"),
                     rnd("2025-10-16", "Series A", 14000000, BVP, True, POST("meet-the-founders-of-strella"), "firm")],
             note="The firm's own post announces it leading the $14M Series A as a new investor; the 2024 seed was "
                  "Decibel's. " + CHECK + "no $1B priced round."))

L.append(cls("stromedix", status="acquired", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2008-04-18", city="Cambridge", focus="Healthcare & Bio",
             rounds=[rnd("2008-04", "Series B", 25000000, None, True, None, "press"),
                     rnd("2011-01-24", "later round", 15500000, None, True, jl.FORMD_CITE("stromedix", 0), "filing")],
             note="acq. by Biogen Idec, 2012. Bessemer joined the $25M Series B of April 2008, after the Atlas and "
                  "Frazier Series A (named from knowledge); the firm's own investment date 2008-04-18 replaces the "
                  "2011 Form D date."))

STW = NEWS("stuffthatworks", "Seed Funding")
STW_IL = NEWS("stuffthatworks", "launches in the U.S.")
L.append(cls("stuffthatworks", status="private", rng="below_1b",
             stage="Seed", stage_src="web_verified", stage_cite=STW, stage_conf="high", entry_date="2018",
             country="IL", country_src="web_verified", country_cite=STW_IL, city="Tel Aviv", focus="Healthcare & Bio",
             rounds=[rnd("2020-07-23", "Seed", 9000000, BVP, True, STW, "press")],
             note="Mercom, 2020-07-24: $9M in seed funding led by Bessemer, 83North and Ofek Ventures; Calcalist calls "
                  "it a Tel Aviv-based startup. The entry year is the listing's partnered year 2018, the founding "
                  "year. Graduation left for the graduation pass."))

SUB = NEWS("subtle-medical", "Morgan Stanley Expansion Capital Leads")
L.append(cls("subtle-medical", status="private", rng="below_1b",
             stage="Seed", stage_src="first_party", stage_cite=POST("our-deep-health-seed-program"), stage_conf="high",
             entry_date="2018-05-17", grad="graduated", grad_src="web_verified", grad_cite=SUB, grad_conf="high",
             country="US", city="Menlo Park", focus="Healthcare & Bio",
             rounds=[rnd("2018-05-17", "Seed", None, BVP, True, POST("our-deep-health-seed-program"), "firm"),
                     rnd("2026-06-02", "growth financing", 33000000, "Morgan Stanley Expansion Capital", None, SUB,
                         "press")],
             note="The firm's own post names Subtle Medical as the first company backed by its Deep Health Seed "
                  "Program. The $33M growth financing led by Morgan Stanley Expansion Capital (2026-06-02) is a later "
                  "priced round well above twice any seed."))

SWP = NEWS("sweep", "raises $28M - techcrunch")
L.append(cls("sweep", status="private", rng="below_1b",
             stage="Seed", stage_src="web_verified", stage_cite=SWP, stage_conf="high", entry_date="2021",
             grad="graduated", grad_src="web_verified", grad_cite=SWP, grad_conf="high",
             country="US", city="New York", focus="SaaS",
             rounds=[rnd("2021", "Seed", None, BVP, True, SWP, "press"),
                     rnd("2022-12-15", "Series A", None, "Insight Partners", True, SWP, "press"),
                     rnd("2025-05-20", "Series B", 22500000, "Insight Partners", True,
                         NEWS("sweep", "Raises $22.5M in Series B Funding Led by Insight"), "press")],
             note="TechCrunch, 2022-12-15: $28M in equity from Bessemer, which seeded Sweep, and Insight, which led "
                  "the Series A. Calcalist reported on 2026-09-03 that ServiceNow has bought the company; neither "
                  "party has announced it and no closing is on record, so the row stays private (as the Insight "
                  "book, whose New York city it shares). The Balderton, Coatue and YC rows named Sweep are other "
                  "companies. " + CHECK + "no $1B priced round."))

SWG = NEWS("swiggy", "raises $15 mn from Bessemer")
L.append(cls("swiggy", status="public", rng="1b_plus", usd=6438796971, val_src="web_verified",
             val_cite=SIB("swiggy", "coatue"), asof="2026-10-01",
             stage="Growth", stage_src="web_verified", stage_cite=SWG, stage_conf="high", entry_date="2016-09-07",
             country="IN", country_src="web_verified", country_cite=SITE("swiggy"), city="Bangalore",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2016-09-19", "Series D", 15000000, BVP, True, SWG, "press")],
             note="Listed on the NSE since November 2024; market cap INR 620.24B @ ECB 2026-10-01 (INR/EUR 108.832, "
                  "EUR/USD 1.1298) = $6.44B (stockanalysis). Times of India, 2016-09-19: $15 million in a Series D "
                  "funding led by Bessemer, with most existing investors participating. India confirmed by the "
                  "firm's own listing."))

L.append(cls("taxiforsure", status="acquired", rng="below_1b", stage="Growth", stage_src="model",
             stage_conf="medium", entry_date="2014-05-09", country="IN", country_src="web_verified",
             country_cite=SITE("taxiforsure"), city="Bangalore", focus="Consumer & Marketplaces",
             rounds=[rnd("2014-05", "Series B", 10000000, BVP, True, None, "press"),
                     rnd("2014-08-21", "Series C", 30000000, "Accel", True,
                         NEWS("taxiforsure", "Series C From Accel"), "press")],
             note="acq. by Ola, 2015 ($200M). Bessemer led the $10M Series B of spring 2014 with Accel, Helion and "
                  "Blume, which had funded the earlier rounds (named from knowledge; the firm's own investment date is "
                  "2014-05-09, three months before the cited Series C)."))

L.append(cls("teachable", status="acquired", rng="below_1b", stage="undetermined", entry_date="2018",
             country="US", city="New York", focus="SaaS", rounds=[],
             note="acq. by Hotmart, 2020. The firm's roadmap post says it invested in Teachable in 2017 and the "
                  "listing says 2018; the company raised six small rounds and no page ties Bessemer to a named one, "
                  "so the stage is undetermined."))

L.append(cls("teleradiology-solutions", status="private", rng="below_1b", stage="undetermined", entry_date="2024",
             country="IN", country_src="web_verified", country_cite=SITE("teleradiology-solutions"),
             city="Bangalore", focus="Healthcare & Bio", rounds=[],
             note="A Bangalore teleradiology provider founded in 2002, on the firm's India list from 2024. Neither the "
                  "firm's posts nor the press report the transaction, so the round and its nature (a growth round or "
                  "a larger stake in a 22-year-old company) are open; a later pass should name it."))

TLR = NEWS("teller-finance", "raises $6.9 million")
L.append(cls("teller-finance", status="private", rng="below_1b", stage="undetermined", entry_date="2021",
             country="US", focus="Crypto & Web3", flags=["city_unknown"],
             rounds=[rnd("2022-02-24", "round led by Blockchain Capital", 6900000, "Blockchain Capital", True, TLR,
                         "press")],
             note="ZDNET, 2022-02-24: $6.9M led by Blockchain Capital with Bessemer among the investors; the article "
                  "names no round and the listing's partnered year is 2021, so the stage is undetermined. A "
                  "decentralised lending protocol with no stated office, hence no city."))

assert len(L) == 24, len(L)
jl.write("j06b", L)
