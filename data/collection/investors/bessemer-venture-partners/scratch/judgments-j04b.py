"""PRO-80 Bessemer, judge j04, file b: batch 7 rows mashlogic .. myheritage (22 rows) and one citation fix (mambu)."""
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


def SIBROUND(investor, slug, sub):
    """A funding-round source URL a sibling book already holds for the same company (read from its classification)."""
    d = json.loads((jl.INV.parent / investor / "companies" / "classification.json").read_text())
    m = {r["source"] for r in (d.get(slug) or {}).get("funding_rounds") or [] if r.get("source") and sub in r["source"]}
    if len(m) != 1:
        raise SystemExit(f"SIBROUND({investor!r}, {slug!r}, {sub!r}) matched {len(m)}")
    return m.pop()


def WIKI(title):
    """jl.W, falling back to the article URL when the cached extract was fetched today but is short."""
    try:
        return W(title)
    except SystemExit:
        raw = jl.WIKI_CACHE / (title.replace(" ", "_") + ".txt")
        if raw.exists() and raw.stat().st_size > 800:
            return "https://en.wikipedia.org/wiki/" + title.replace(" ", "_")
        raise


# market-cap pages read with curl on 2026-10-01 (stockanalysis.com, the pattern the brief names)
SA_MATRIMONY = "https://stockanalysis.com/quote/nse/MATRIMONY/market-cap/"
SA_MOTILAL = "https://stockanalysis.com/quote/nse/MOTILALOFS/market-cap/"
# read with WebFetch on 2026-10-01; the URL is the one the Bain Capital Ventures book cites for the same round
OCBJ_MIND = "https://www.ocbj.com/automobiles/rivian-backed-mind-robotics-startup-raises-500-million/"

mash_tc = SIBROUND("new-enterprise-associates", "mashlogic-inc", "techcrunch.com/2009/06/01")
mcp_acq = NEWS("mcp-manager", "Usercentrics Acquires MCP Manager - FinSMEs")
mealpal_a = NEWS("mealpal", "Series A led by Comcast Ventures")
docsapp_a = NEWS("medibuddy-fka-docsapp", "DocsApp raises $7.2 mn Series A funding")
docsapp_lm = NEWS("medibuddy-fka-docsapp", "DocsApp raises $7.2 million from Bessemer")
medisage_r = NEWS("medisage", "first round of institutional fundraise")
mind_val = SIB("mind-robotics", "bain-capital-ventures")
mind_a = NEWS("mind-robotics", "for industrial AI-powered robots")
miter_b = NEWS("miter", "Miter, the AI Platform for Construction, Raises $40 Million")
modelcode_hq = NEWS("modelcode", "Modelcode.ai founder Michael Fertik expands")
moon_hq = NEWS("moonvalley", "Joins $84 Million Round for Toronto")
mn_shut = NEWS("mothernature-com", "Plans to Shut Down")
motilal_pe = NEWS("motilal-oswal", "Advisor to Motilal Oswal in raising private equity")
mindbody_s1 = FTSURL("d879972ds1.htm")

lines = [
    cls("mambu", country="NL", country_src="web_verified", country_cite=WIKI("Mambu (company)")),

    cls("mashlogic", status="acquired", rng="below_1b",
        stage="Seed", stage_src="web_verified", stage_cite=mash_tc, stage_conf="high", entry_date="2006-09-27",
        country="US", city="Menlo Park", focus="Consumer & Marketplaces",
        rounds=[rnd("2006-09-27", "seed (incubation)", 900000, "Bessemer Venture Partners", True, mash_tc, "press"),
                rnd("2009-06-01", "second seed", 500000, None, None, mash_tc, "press"),
                rnd("2009-08-19", "unnamed (Form D)", 2548800, None, True, jl.FORMD_CITE("mashlogic", 0), "filing")],
        note="MashLogic, browser extension, Menlo Park. TechCrunch (2009-06-01): 'Bessemer Venture Partners is incubating the "
             "startup and put in most of the original $900,000 in seed money'; the firm's archive dates the investment to "
             "September 2006, which replaces the 2009 Form D date. Acquired by Groupon as the New Enterprise Associates book "
             "reads it (the firm's exit year is 2013). Graduation left for the graduation pass."),

    cls("matrimony-com", status="public", rng="below_1b", usd=112427723, val_src="web_verified", val_cite=SA_MATRIMONY,
        asof="2026-10-01",
        stage="undetermined", entry_date="2011-09-28",
        city="Chennai", focus="Consumer & Marketplaces", rounds=[],
        note="Matrimony.com (formerly Consim Info, BharatMatrimony), Chennai; listed on the NSE since September 2017. "
             "INR 10.83B @ ECB 2026-10-01 (INR/EUR 108.832, EUR/USD 1.1298) = $112.4M (stockanalysis.com). The firm's archive "
             "dates its investment to September 2011, six years before the listing; no source read names that round. The "
             "base row bharat-matrimony is the same company."),

    cls("mcp-manager", status="acquired", rng="below_1b",
        stage="undetermined", entry_date="2021",
        country="US", city="New York", city_src="web_verified", focus="SaaS", rounds=[],
        note="MCP Manager, a governance platform for the Model Context Protocol from a New York company founded by Michael "
             "Yaroshefsky that earlier built spreadsheet-style workbooks; acq. by Usercentrics, January 2026 (FinSMEs, the "
             "firm's listing). The firm's year is 2021; no source read names the round."),

    cls("mealpal", status="private", rng="below_1b",
        stage="Series A", stage_src="web_verified", stage_cite=mealpal_a, stage_conf="high", entry_date="2016-09-27",
        country="US", city="New York", focus="Consumer & Marketplaces",
        rounds=[rnd("2017-03-03", "Series A", 15000000, "Comcast Ventures", True, mealpal_a, "press")],
        note="MealPal, lunch subscription, New York. Comcast Ventures' post (2017-03-03): 'excited to lead MealPal's Series A "
             "round of financing, joined by Bessemer'; the entry date is the firm's own investment date, the announcement "
             "came in 2017. The Menlo book reads defunct, but mealpal.com still took sign-ups for New York City on 2026-10-01, "
             "so private."),

    cls("medibuddy-fka-docsapp", status="private", rng="below_1b",
        stage="Series A", stage_src="web_verified", stage_cite=docsapp_a, stage_conf="medium", entry_date="2017-10-27",
        country="IN", country_src="web_verified", country_cite=SITE("medibuddy-fka-docsapp"), city="Bangalore",
        focus="Healthcare & Bio",
        rounds=[rnd("2017-12-12", "Series A", 7200000, "Bessemer Venture Partners", True, docsapp_a, "press"),
                rnd("2017-12-12", "Series A", 7200000, "Bessemer Venture Partners", True, docsapp_lm, "press")],
        note="MediBuddy (DocsApp merged with Medi Assist's MediBuddy unit in 2020), online doctor consultations, Bangalore. "
             "DocsApp's $7.2M Series A of December 2017 (VCCircle) came from Bessemer and others (Livemint headline); the "
             "firm's archive dates the DocsApp investment to 2017-10-27. This row's archive match (2011, NSE: MEDIASSIST) "
             "belongs to Medi Assist, a separate row, and is not used; the base row docsapp is this company."),

    cls("medisage", status="private", rng="below_1b",
        stage="undetermined", entry_date="2022-04-13",
        country="IN", country_src="web_verified", country_cite=SITE("medisage"), city="Mumbai", focus="Healthcare & Bio",
        rounds=[rnd("2022-04-13", "first institutional round (unnamed)", 7000000, None, None, medisage_r, "press")],
        note="MediSage, online community for doctors, Mumbai (the firm's listing: 'an India-based online community of "
             "doctors'). YourStory (2022-04-13) reports $7M 'in first round of institutional fundraise' without a round "
             "name, so the stage is undetermined."),

    cls("melio-payments", status="acquired", rng="below_1b",
        stage="undetermined", entry_date="2018",
        country="US", city="New York", focus="Fintech & Payments", rounds=[],
        note="Melio, B2B payments for small businesses, New York with its engineering in Tel Aviv; acq. by Xero, agreed June "
             "2025 (the firm's listing, Calcalist). The firm's year is 2018, the founding year; its 2020 post reports $144M "
             "'in several rounds' without naming the one it entered, so undetermined."),

    cls("meltplan", status="private", rng="below_1b", city="Berkeley", city_src="formd_address",
        focus="AI & Applied AI",
        stage="Seed", stage_src="first_party", stage_cite=POST("optimizing-pre-construction-workflows"), stage_conf="high",
        entry_date="2026-02-18", flags=["stage_disputes_band"], grad="censored",
        rounds=[rnd("2026-02-25", "Seed", 10000000, "Bessemer Venture Partners", True,
                    POST("optimizing-pre-construction-workflows"), "firm")],
        note="MeltPlan, AI preconstruction planning for contractors, Berkeley per its Form D. The firm's own post: 'Bessemer "
             "Venture Partners leads MeltPlan's $10 million Seed round' (2026-02-25), which disputes the Series A band read "
             "off the size of the February 2026 filing. Entry inside the 24-month window: censored. Momentum check 2026-10-01: "
             "no round beyond the seed."),

    cls("metalogix", status="acquired", rng="below_1b",
        stage="undetermined", entry_date="2008-09-30",
        country="US", city="Washington", focus="SaaS", rounds=[],
        note="Metalogix, content management tools for SharePoint and Exchange, Washington DC; acq. by Permira, 2014, when "
             "Insight and Bessemer 'fully exit their stakes' (Private Equity Wire). Bessemer invested beside Insight in "
             "September 2008; no source read names the round or says whether the two took control, which is flagged for a "
             "ruling."),

    cls("millennial-media", rng="below_1b", city="Baltimore", focus="Media, Gaming & Advertising",
        stage="Series A", stage_src="model", stage_conf="medium", entry_date="2006-07-24",
        rounds=[rnd("2006-07-24", "Series A", None, None, True, None, "press"),
                rnd("2009-11-13", "Series C", 16000000, "New Enterprise Associates", None,
                    jl.FORMD_CITE("millennial-media", 0), "filing")],
        note="Millennial Media, mobile advertising, Baltimore; IPO 2012, acq. by AOL, 2015. The firm's archive dates its "
             "investment to July 2006, two months after the founding and the month the Columbia Capital and Acta Wireless "
             "directors joined the board (S-1): the Series A, named from knowledge. The 2009 Form D is the Series C that "
             "New Enterprise Associates led, not the entry."),

    cls("milo", rng="below_1b", country="US", city="Palo Alto", focus="Consumer & Marketplaces",
        stage="Series A", stage_src="model", stage_conf="medium", entry_date="2009-11-10",
        rounds=[rnd("2009-11", "Series A", 4000000, "True Ventures", True, None, "press")],
        note="Milo.com, local shopping search, Palo Alto; acq. by eBay, 2010. The firm's archive dates its investment to "
             "2009-11-10, the month of the $4M Series A that True Ventures led (named from knowledge; the Felicis book "
             "reads Series A from its own listing). The Y Combinator row named Milo is a different company."),

    cls("mind-robotics", status="private", rng="1b_plus", usd=3400000000, val_src="web_verified", val_cite=mind_val,
        asof="2026-05-13",
        stage="Seed", stage_src="web_verified", stage_cite=OCBJ_MIND, stage_conf="high", entry_date="2025-11",
        grad="graduated", grad_src="web_verified", grad_cite=mind_a, grad_conf="high",
        country="US", city="Palo Alto", focus="Industrial & Robotics",
        rounds=[rnd("2025-11", "Seed", 115000000, "Eclipse", True, OCBJ_MIND, "press"),
                rnd("2026-03-11", "Series A", 500000000, "Accel and Andreessen Horowitz", None, mind_a, "press"),
                rnd("2026-05-13", "unnamed", 400000000, "Kleiner Perkins", None, mind_val, "press")],
        note="Mind Robotics, industrial AI robotics spun out of Rivian, Palo Alto. Orange County Business Journal: 'In late "
             "2025, Mind Robotics raised $115 million in seed funding led by Eclipse', with Bessemer among the other "
             "investors (the a16z book dates the seed to November 2025). The $500M Series A of March 2026 graduates the row "
             "(TechCrunch), and the $400M round of May 2026 valued it at $3.4 billion (Reuters via CNA), as in the sibling "
             "books."),

    cls("mindbody", rng="below_1b", city="San Luis Obispo", focus="SaaS",
        stage="Growth", stage_src="web_verified", stage_cite=mindbody_s1, stage_conf="high",
        flags=["stage_disputes_band"],
        rounds=[rnd("2010-08-12", "Series D", 11000000, "Bessemer Venture Partners", True, mindbody_s1, "filing")],
        note="Mindbody, software for fitness studios and spas, San Luis Obispo; IPO 2015, taken private by Vista in 2019. The "
             "S-1 names Jeremy Levine the designee of the Series D preferred holders and the firm's memo of July 2010 "
             "describes an $11M preferred round, so Bessemer entered at the Series D of August 2010; the Series A band "
             "counted only the filings since 2009 and is disputed."),

    cls("miter", status="private", rng="below_1b", city="San Francisco", focus="SaaS",
        stage="Series A", stage_src="web_verified", stage_cite=miter_b, stage_conf="high", entry_date="2025-05-19",
        flags=["stage_disputes_band"],
        rounds=[rnd("2021-04-09", "seed", 3500000, None, False, jl.FORMD_CITE("miter", 0), "filing"),
                rnd("2025-05-19", "Series A", 38000000, "Bessemer Venture Partners and Coatue", True,
                    POST("backing-miter-building"), "firm"),
                rnd("2026-09-30", "Series B", 40000000, "Battery Ventures", True, miter_b, "company")],
        note="Miter, payroll and workforce software for construction, San Francisco. The firm's post: 'Bessemer Venture "
             "Partners co-leads Miter's $38M financing' (2025-05-19); the company's Series B release of 2026-09-30 calls "
             "that 'Miter's Series A fundraising round in May 2025' and lists Bessemer as participating again. The 2021 "
             "Form D names Connor Watumull as the company's own executive, not a Bessemer seat, so the Seed band is "
             "disputed; the firm's listing year is 2025."),

    cls("mitigata", status="private", rng="below_1b",
        stage="Growth", stage_src="first_party", stage_cite=POST("securing-indias-digital-economy-with-mitigata"),
        stage_conf="high", entry_date="2026-06-23",
        country="IN", country_src="web_verified", country_cite=POST("securing-indias-digital-economy-with-mitigata"),
        city="Bangalore", focus="Security",
        rounds=[rnd("2026-06-23", "Series B", 14500000, "Bessemer Venture Partners", True,
                    POST("securing-indias-digital-economy-with-mitigata"), "firm")],
        note="Mitigata, cyber risk and insurance platform for Indian enterprises, Bangalore. The firm's own post: 'Bessemer "
             "Venture Partners leads Mitigata's $15M Series B' (2026-06-23)."),

    cls("modelcode", status="private", rng="below_1b",
        stage="undetermined", entry_date="2024",
        country="US", city="New York", city_src="web_verified", focus="DevTools & APIs", rounds=[],
        note="Modelcode.ai, generative AI for modernising legacy code, founded by Michael Fertik; 'Headquartered in New "
             "York' (Calcalist, 2025-04-02). The firm's year is 2024; no funding announcement was found, so the round is "
             "not named. Momentum check 2026-10-01 (Google News): no priced round at $1B or more."),

    cls("moonvalley", status="acquired", rng="below_1b",
        stage="Seed", stage_src="first_party", stage_cite=POST("moonvalley-revolutionizing"), stage_conf="high",
        entry_date="2024-11-18", grad="censored",
        country="CA", country_src="web_verified", country_cite=moon_hq, city="Toronto", focus="AI & Applied AI",
        rounds=[rnd("2024-11-18", "Seed", 70000000, "General Catalyst, Khosla Ventures and Bessemer", True,
                    POST("moonvalley-revolutionizing"), "firm"),
                rnd("2025-07-14", "unnamed (additional)", 84000000, "General Catalyst", None,
                    NEWS("moonvalley", "raises additional $84 million USD"), "press")],
        note="Moonvalley, licensed AI video models, Toronto (citybiz: 'Toronto's Moonvalley') and Los Angeles. The firm's own "
             "post: 'thrilled to co-lead Moonvalley's seed round' (2024-11-18). The later $43M and $84M raises of 2025 carry "
             "no round name and do not double the $70M seed; the entry is inside the 24-month window, censored. Reka took "
             "over the company in June 2026 (the firm's listing reads acquired, as does the General Catalyst book; Reka's "
             "release says the two 'joined forces')."),

    cls("mothernature-com", status="defunct", rng="below_1b",
        stage="undetermined", entry_date="1998",
        country="US", city="Concord", focus="Consumer & Marketplaces", rounds=[],
        note="MotherNature.com, online retailer of vitamins and natural products, Concord MA; IPO December 1999, then wound "
             "up ('MotherNature.com Plans to Shut Down', SupplySide Supplement Journal, on the liquidation of late 2000). "
             "The firm's list gives 1998 and Bessemer funds filed 13Gs in 2000 and 2001; the round is not named."),

    cls("motilal-oswal", status="public", rng="1b_plus", usd=6215291072, val_src="web_verified", val_cite=SA_MOTILAL,
        asof="2026-10-01",
        stage="Growth", stage_src="web_verified", stage_cite=motilal_pe, stage_conf="medium", entry_date="2006",
        country="IN", country_src="web_verified", country_cite=W("Motilal Oswal Financial Services"), city="Mumbai",
        focus="Fintech & Payments",
        rounds=[rnd("2006", "private equity round (pre-IPO)", None, "New Vernon Private Equity and Bessemer", True,
                    motilal_pe, "press")],
        note="Motilal Oswal Financial Services, brokerage and asset manager, Mumbai; listed in September 2007. Avendus records "
             "itself as 'Advisor to Motilal Oswal in raising private equity funding from New Vernon Private Equity and "
             "Bessemer Venture Partners', and the firm's year is 2006: a private round a year before the listing, so a "
             "member under D5 and a pre-IPO entry, Growth. INR 598.71B @ ECB 2026-10-01 (INR/EUR 108.832, EUR/USD 1.1298) "
             "= $6.22B (stockanalysis.com)."),

    cls("moveinsync", status="private", rng="below_1b",
        stage="Growth", stage_src="first_party", stage_cite=POST("making-the-daily-commute"), stage_conf="high",
        entry_date="2024-01-25",
        country="IN", country_src="web_verified", country_cite=POST("350-million-for-our-next-india-fund"),
        city="Bangalore", focus="SaaS",
        rounds=[rnd("2024-01-25", "Series C", None, "Bessemer Venture Partners", True,
                    POST("making-the-daily-commute"), "firm")],
        note="MoveInSync, employee commute software, Bangalore; the firm's India fund post counts it among its startups in "
             "India. The firm's own post: 'Bessemer leads MoveInSync's Series C fundraise' (2024-01-25)."),

    cls("mural-health", status="private", rng="below_1b", city="Berwyn", city_src="formd_address",
        focus="Healthcare & Bio",
        note="Mural Health, participant payments and engagement for clinical trials, Berwyn PA (Form D; Technical.ly calls "
             "it Berwyn-based). The firm's listing year is 2022, the year of the company's first $7.5M filing, while the "
             "band dates the entry to the 2024 filing that first names Steve Kraus; no source read names either round, so "
             "the band is left as it is and the date question is reported."),

    cls("myheritage", status="acquired", rng="below_1b", city="Or Yehuda", focus="Consumer & Marketplaces",
        note="MyHeritage, online genealogy, Or Yehuda; acq. by Francisco Partners, 2021 (reported $600M). Bessemer led the "
             "$25M round of November 2012 (Wikipedia), which agrees with the Growth band."),
]

jl.write("j04b", lines)
