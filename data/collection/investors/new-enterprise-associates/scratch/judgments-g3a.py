#!/usr/bin/env python3
"""PRO-100 NEA delta judge g3a: queue batch 3, 22 rows (DELTA-BRIEF.md).

Graduation pass on the Seed rows (choosy, cruisewise, fantasy-shopper, koozoo, paysa, qbotix, reachify, reznext, silk,
tract, umami, viavia, wedding-party), the four recall additions (avivo-corporation, blacktag, boisson,
camp-family-experience-retailer) and the leftovers (future-retail, aquila, aveo, cardima, censtor).

Every citation was read on 2026-09-30: SEC documents through secget.py (the sec-cache check below refuses one that was
never fetched), news headlines through nq.py / graduation-surfaces.json decoded by NEWS / GNEWS, and the other pages
with WebFetch or curl (READ below). WebSearch: 3 calls.

Run: NQ_TAG=g3a python3 judgments-g3a.py"""
import hashlib
import json
from pathlib import Path

import judge_lib as jl

cls, verdict, rnd, NEWS, GNEWS, POST = jl.cls, jl.verdict, jl.rnd, jl.NEWS, jl.GNEWS, jl.POST
HERE = Path(__file__).resolve().parent
CHECK = "2026-09-30"
KNOWN = json.loads((jl.INV / "companies/classification.json").read_text())


def SEC(url):
    """An SEC document read this session through secget.py (present in sec-cache)."""
    if not (HERE / "sec-cache" / (hashlib.sha1(url.encode()).hexdigest() + ".txt")).exists():
        raise SystemExit(f"SEC({url!r}): never fetched")
    return url


def FDX(cik, acc):
    """A Form D's EDGAR index URL, only for a filing whose primary document was read."""
    SEC(f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-', '')}/primary_doc.xml")
    return f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-', '')}/{acc}-index.htm"


# Pages read this session with WebFetch or curl (each says what it is cited for).
READ = {
    "qbotix_b": "https://globalventuring.com/blog/2014/05/16/qbotix-follows-the-sun-for-12m-series-b/",
    "boisson_bi": "https://www.businessinsider.com/boisson-ceo-raises-12-million-dominate-non-alcoholic-retail-sector-2022-8",
    "camp_bi": "https://www.businessinsider.com/vcs-funding-startups-disrupt-future-entertainment-generative-ai-tech-2024-1",
}
# The Atomico book's citation for Silk's end (read with curl this session: 'Palantir acquires data visualization
# startup Silk', TechCrunch 2016-08-10, 'appears to be an acqui-hire').
SILK_END = json.loads((jl.INV.parent / "atomico/companies/classification.json").read_text())["silk"]["graduation_citation"]
assert SILK_END.startswith("https://techcrunch.com/2016/08/10/palantir-acquires")


def SURF(slug, firm, formd, over=None, drop=(), extra=()):
    """GRADLINES with the firm and Form D lines given, noisy default publisher lines replaced by what was read."""
    out = []
    for line in jl.GRADLINES(slug, firm_note=firm, formd_note=formd):
        k = line.split(":", 1)[0]
        if k in drop:
            continue
        out.append((over or {}).get(k, line))
    return out + list(extra)


L = []

# ================================================================ choosy
WWD_CHOOSY = GNEWS("choosy", "Choosy Secures $5.4 Million Seed")
L.append(cls("choosy", grad="not_graduated", grad_src="absence_check", grad_conf="high", grad_asof=CHECK,
    surfaces=SURF("choosy",
        "the firm's own listings for Choosy (captured 2018 to 2021: 'yr 2018, stage Seed', Current, private) -> no post names the company",
        "EDGAR company search and full-text search of Form Ds (Choosy; Jessie Zeng) -> no filing by the company",
        over={"googlenews": "googlenews: Google News ('Choosy' with round and exit words; with fashion; with Jessie Zeng) -> WWD "
                            "2018-05-15 'Choosy Secures $5.4 Million Seed Round', then launch, hiring and founder profiles to "
                            "Forbes 2020-04-24; the rest is the common word; no later round"},
        extra=["sibling:coatue: its row for Choosy -> defunct ('ceased trading in 2019'), the $5.4M seed of May 2018 the only "
               "round in its note"]),
    rounds=[rnd("2018-05-15", "Seed", 5400000, None, None, WWD_CHOOSY, "press")],
    note="S2A: not graduated; the absence test found no round after the $5.4M seed of May 2018 (WWD), and the company is "
         "defunct as in the Coatue book."))

# ================================================================ cruisewise
TC_CW = GNEWS("cruisewise", "CruiseWise Launches")
L.append(cls("cruisewise", grad="not_graduated", grad_src="absence_check", grad_conf="high", grad_asof=CHECK,
    surfaces=SURF("cruisewise",
        "the firm's own listings for CruiseWise (2013 to 2020: 'yr 2011, stage seed', exit 'acquired (by Trip Advisor)') -> no post names the company",
        "EDGAR company search and full-text search of Form Ds (CruiseWise) -> no filing by the company",
        over={"techcrunch": "techcrunch: TechCrunch's own search (CruiseWise) -> the 2012-02-13 launch piece ('$1.6 million in "
                            "seed funding from SV Angel, NEA, Index Ventures, PROfounders Capital'); nothing later on the company",
              "googlenews": "googlenews: Google News ('CruiseWise' with round and exit words; with TripAdvisor; alone) -> one "
                            "2012 Business Insider piece on its founder's visa; no later round"}),
    rounds=[rnd("2012-02-13", "Seed", 1600000, None, True, TC_CW, "press")],
    note="S2A: not graduated; the absence test found no round after the $1.6M seed from SV Angel, NEA, Index Ventures and "
         "PROfounders (TechCrunch, 2012-02-13), and the firm's own page gives the exit as acquired by TripAdvisor."))

# ================================================================ fantasy-shopper
L.append(cls("fantasy-shopper", grad="not_graduated", grad_src="absence_check", grad_conf="high", grad_asof=CHECK,
    surfaces=SURF("fantasy-shopper",
        "the firm's own 2013 listing for Fantasy Shopper (Current) -> no post names the company",
        "a UK company (Fantasy Shopper Limited, Exeter); EDGAR holds no filing by it",
        over={"techcrunch": "techcrunch: TechCrunch's own search (Fantasy Shopper) -> the October 2011 launch pieces and the two "
                            "2012-01-23 reports of the $3.3M first money from Accel and NEA; nothing later on the company"}),
    note="S2A: not graduated; the absence test (English and UK editions) found no round after the $3.3M first round of "
         "January 2012, and the company entered members' voluntary liquidation in March 2014."))

# ================================================================ koozoo
TC_KZ = GNEWS("koozoo", "Koozoo Raises")
L.append(cls("koozoo", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=CHECK,
    surfaces=SURF("koozoo",
        "the firm's own 2013 listing for Koozoo (Current) -> no post names the company",
        "EDGAR company search and full-text search of Form Ds (Koozoo) -> no filing by the company",
        over={"googlenews": "googlenews: Google News ('Koozoo' with round and exit words; 'Koozoo'; with video) -> no result"}),
    rounds=[rnd("2012-12-12", "Seed", 2500000, "NEA and Tugboat Ventures", True, TC_KZ, "press")],
    note="S2A: not graduated; the absence test found nothing after the $2.5M seed led by NEA and Tugboat (TechCrunch, "
         "2012-12-12) and the February 2013 launch; coverage of the company stops there."))

# ================================================================ paysa
SB_PAYSA = GNEWS("paysa", "Paysa launches")
L.append(cls("paysa", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=CHECK,
    surfaces=SURF("paysa",
        "the firm's own listings for Paysa (2017 to 2020: 'yr 2015, stage Seed', Current) -> no post names the company",
        "EDGAR company search (Paysa) and full-text search of Form Ds (Paysa; Chris Bolte) -> no filing by the company",
        over={"googlenews": "googlenews: Google News ('Paysa' with round and exit words; with salary; with raises) -> StartUp Beat "
                            "2016-02-24, the launch 'with $4 million in seed funding from NEA, Milliway Ventures and others', "
                            "then salary-survey citations to 2017; the other hits are Pakistan's PaySa and unrelated; no later round"}),
    rounds=[rnd("2016-02-24", "Seed", 4000000, None, True, SB_PAYSA, "press")],
    note="S2A: not graduated; the absence test found no round after the $4M seed from NEA, Milliway Ventures and others "
         "announced at launch (StartUp Beat, 2016-02-24)."))

# ================================================================ qbotix
GV_QB = READ["qbotix_b"]
L.append(cls("qbotix", grad="graduated", grad_src="web_verified", grad_cite=GV_QB, grad_conf="high",
    rounds=[rnd("2012", "unnamed", 5000000, None, None, GV_QB, "press"),
            rnd("2013", "unnamed", 6500000, None, None, GV_QB, "press"),
            rnd("2014-05-16", "Series B", 12000000, "E.ON and Iberdrola", True, GV_QB, "press")],
    note="S2A: graduated; Global Venturing (2014-05-16) reports a $12M Series B with E.ON and Iberdrola, joined by existing "
         "backers NEA, Firelake and Draper Nexus, after a $5M round in 2012 and $6.5M in 2013; a named later round decides "
         "it. This corrects the earlier note that none of the money was named by series; Fortune (2015-09-22) has it shut "
         "down in August 2015."))

# ================================================================ reachify
FD_RF17 = FDX(1645055, "0001231919-18-000012")
L.append(cls("reachify", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=CHECK,
    surfaces=SURF("reachify",
        "the firm's own listings for Reachify (2017 to 2020: 'yr 2017, stage Seed', Historic by 2020) -> no post names the company",
        "Reachify, Inc. (formerly Shopster, Inc., CIK 1645055) -> 2015-05-26 $250,000 as Shopster; first sale 2017-01-23, "
        "$3,366,640 sold to 13 investors (amended 2018-03-06); no later filing",
        over={"googlenews": "googlenews: Google News ('Reachify' with round and exit words; 'Reachify') -> one PR Newswire release "
                            "of 2023-06-20 (a new chief revenue officer); no round"}),
    rounds=[rnd("2017-01-23", "unnamed (Form D)", 3366640, None, None, FD_RF17, "filing")],
    note="S2A: not graduated; the absence test found no round after the 2017 financing ($3.37M on its Form D, the year the "
         "firm labels Seed), and a June 2023 release shows the company still operating."))

# ================================================================ reznext
L.append(cls("reznext", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=CHECK,
    surfaces=SURF("reznext", None,
        "an Indian company (Bangalore); EDGAR holds no filing by it",
        over={"googlenews": "googlenews: Google News ('RezNext' with round and exit words; 'RezNext'; with acquired) -> Hospitality "
                            "Net 2013-09-17 (a new CEO); no later round and no exit"}),
    note="S2A: not graduated; the absence test (English and Indian editions) found no round after the $5M seed of "
         "December 2014."))

# ================================================================ silk
SILK_SEED = KNOWN["silk"]["entry_stage_citation"]
L.append(cls("silk", grad="not_graduated", grad_src="web_verified", grad_cite=SILK_END, grad_conf="high", grad_asof=CHECK,
    surfaces=SURF("silk",
        "the firm's own listings for Silk (2014 to 2022: 'yr 2012, stage early') -> no post names the company (the one "
        "post matching the name is about the Silk Road)",
        "a Dutch company (Amsterdam); EDGAR holds no filing by it",
        over={"googlenews": "googlenews: Google News ('Silk' with round and exit words) -> Silk Road and other noise; on this "
                            "company only the 2016-08-10 reports of Palantir's purchase (Business Insider, GeekWire, Fortune); no later round",
              "googlenews_firm": "googlenews_firm: Google News ('Silk' beside NEA) -> GeekWire 2016-08-10 on the Palantir "
                                 "purchase; no later round",
              "googlenews_local": "googlenews_local: Google News, Dutch edition -> NU 2016-08-11 'Dataverwerker Palantir koopt "
                                  "Nederlandse startup Silk'; no later round",
              "crunchbase_news": "crunchbase_news: Crunchbase News's own search (Silk) -> other companies named Silk; nothing on this one",
              "techcrunch": "techcrunch: TechCrunch's own search (Silk) -> unrelated items; read directly, TechCrunch holds the "
                            "2012-08-01 seed and the 2016-08-10 Palantir acquisition, nothing between",
              "sibling:atomico": "sibling:atomico: its row for Silk -> not graduated: NEA's August 2012 round was also named a "
                                 "seed, the October 2013 $1.6M unnamed round is below the $5M step-up, and Palantir's 2016 "
                                 "acqui-hire ended it (TechCrunch)"},
        drop=("sibling:insight-partners",)),
    rounds=[rnd("2012-08-01", "Seed", 1600000, "NEA", True, SILK_SEED, "press")],
    note="S2A: not graduated, aligned with the Atomico book; after NEA's $1.6M seed of August 2012 the only later money on "
         "record is a $1.6M unnamed round in October 2013 (Atomico's note), below the $5M step-up, and Palantir's "
         "August 2016 acqui-hire ended the company (TechCrunch). The insight-partners 'Silk' is Silk Security, another company."))

# ================================================================ tract
CB_TRACT = GNEWS("tract", "Esther Wojcicki’s Tract Raises")
L.append(cls("tract", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=CHECK,
    surfaces=SURF("tract",
        "the firm's own post of 2022-09-16 ('Building for the Next Generation of Young Creators', on the seed) and its 2023 "
        "listing ('yr 2022, stage Seed') -> nothing later names the company",
        "EDGAR company search (Tract) and full-text search of Form Ds (Tract; Wojcicki) -> no filing by the company",
        over={"googlenews": "googlenews: Google News ('Tract' with round and exit words; with Wojcicki; with kids learning funding) "
                            "-> a 2021 founder interview, citybiz 2022-09-15 and Business Insider 2022-09-19 on the $7M seed; "
                            "the other hits are land tracts, urinary tracts and the Tract data-center company; no later round",
              "crunchbase_news": "crunchbase_news: Crunchbase News's own search (Tract) -> 30 results, none on this company"}),
    rounds=[rnd("2022-09-15", "Seed", 7000000, "NEA", True, CB_TRACT, "press")],
    note="S2A: not graduated; the absence test found no round after NEA's $7M seed of September 2022, 48 months before "
         "the check."))

# ================================================================ umami
FD_UM11 = FDX(1515780, "0001515780-11-000004")
FD_UM12 = FDX(1515780, "0001515780-12-000002")
L.append(cls("umami", city="New York", city_src="formd_address", flags=["model_disputes_source"],
    grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=CHECK,
    surfaces=SURF("umami",
        "the firm's own 2013 listing for Umami (Current) -> no post names the company",
        "Umami Co. (formerly ABB TV, Inc., CIK 1515780; officers Scott Rosenberg and Bryan Slavin) -> first sale "
        "2011-03-07, $1,650,000 sold of $1,750,000 (the seed); first sale 2012-03-23, $125,000 sold of $325,000; no later "
        "filing, nothing near the $5M step-up",
        over={"googlenews": "googlenews: Google News ('Umami' with round and exit words; with Fox; with second screen) -> Umami "
                            "Burger, umami flavour and other companies named Umami; nothing on this company after the 2011 seed",
              "techcrunch": "techcrunch: TechCrunch's own search (Umami) -> unrelated results; read directly, TechCrunch holds "
                            "the 2011-08-16 seed ('$1.65 million in seed funding from Battery Ventures, NEA and other "
                            "angels'); nothing later"}),
    rounds=[rnd("2011-03-07", "Seed", 1650000, None, True, FD_UM11, "filing"),
            rnd("2012-03-23", "unnamed (Form D)", 125000, None, None, FD_UM12, "filing")],
    note="S2A: not graduated, aligned with the Battery book; Umami Co.'s Form Ds show the $1.65M seed and a $125,000 sale "
         "in March 2012, nothing later before FOX bought it in 2013. City disputed: the founders TechCrunch names (Scott "
         "Rosenberg, Bryan Slavin) file as Umami Co. at 347 West 36th Street, New York (Montclair, New Jersey at the first "
         "filing), not San Francisco; Battery's row reads San Francisco from model knowledge."))

# ================================================================ viavia
FD_VV25 = FDX(1929563, "0001929563-25-000001")
FD_VV26 = FDX(1929563, "0001929563-26-000001")
PR_VV = GNEWS("viavia", "VIAVIA announces seed")
L.append(cls("viavia", grad="graduated", grad_src="web_verified", grad_cite=FD_VV26, grad_conf="high",
    rounds=[rnd("2022-08-25", "Seed", 8000000, "NEA and Basis Set Ventures", True, PR_VV, "company"),
            rnd("2025-01-07", "unnamed (Form D)", 10000000, None, None, FD_VV25, "filing"),
            rnd("2026-03-13", "unnamed (Form D)", 22431991, None, None, FD_VV26, "filing")],
    note="S2A: graduated; after the $8M seed NEA and Basis Set co-led (the company's release, 2022-08-25), ViaVia Corp's "
         "Form D of March 2026 sold $22.4M of a $30.1M preferred offering ($17.3M new money beside $5.1M of converted "
         "SAFEs), above the $16M step-up; the $10M sale of January 2025 does not reach it. Headline's Clarey Zhu is on the "
         "2026 filing, as in the Headline book."))

# ================================================================ wedding-party
FI_WP = KNOWN["wedding-party"]["entry_stage_citation"]
L.append(cls("wedding-party", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=CHECK,
    surfaces=SURF("wedding-party",
        "the firm's own listings for Wedding Party (2014 to 2020: 'yr 2012, stage seed', Current, private) -> no post names the company",
        "EDGAR company search and full-text search of Form Ds ('Wedding Party'; 'Wedding Party, Inc.') -> no filing by the company",
        over={"googlenews": "googlenews: Google News ('Wedding Party' with round and exit words; with app acquired; with photo "
                            "app) -> celebrity and news wedding parties; the only item near the company is Business Journals "
                            "2016-07-21, WedPics's founder on buying his top competitor to shut it down (body not readable, "
                            "the headline does not name the company); no later round"}),
    rounds=[rnd("2013-02-21", "Seed", 1000000, "NEA and Felicis", True, FI_WP, "press")],
    note="S2A: not graduated, aligned with the Felicis book; the absence test found no round after the $1M seed of "
         "February 2013."))

# ================================================================ avivo-corporation (recall addition)
AVIVO_RRA = SEC("https://www.sec.gov/Archives/edgar/data/1091158/000095013405002504/a05563exv10w3.txt")
AVIVO_8K = SEC("https://www.sec.gov/Archives/edgar/data/1091158/000095013705005390/a08744e8vk.htm")
SEC("https://www.sec.gov/Archives/edgar/data/1091158/000095013405002504/a05563exv2w1.txt")
L.append(verdict("avivo-corporation", "member",
    "Schedule B ('Avivo Investors') of the registration rights agreement WebSideStory filed with its February 2005 merger "
    "agreement lists New Enterprise Associates 10, L.P. and NEA Ventures 2000, L.P. among Avivo Corporation's holders, "
    "beside Sofinnova; NEA's Charles Linehan was the Avivo holders' representative. A private California company held by "
    "an NEA fund. Its WebSideStory stock is the sale consideration (websidestory-inc is not_member under D8).",
    ec="fund_filing", conf="high", cite=AVIVO_RRA))
L.append(cls("avivo-corporation", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="San Bruno", city_src="web_verified", focus="SaaS",
    note="Avivo Corporation of San Bruno, California (the merger agreement's notice address), 'a leading provider of "
         "on-demand digital marketing applications' with hosted site search and web content management; WebSideStory "
         "bought it on 2005-05-04 for 3,123,149 shares and options plus $4.2M in cash (8-K, 2005-05-05): acquired, "
         "below_1b. Avivo had Series A, B and C preferred and no source says which NEA 10 bought, so the stage is "
         "undetermined."))

# ================================================================ blacktag (recall addition)
WWD_BT = NEWS("blacktag", "Secures $3.75 Million Seed")
FD_BT = FDX(1835731, "0001835731-20-000002")
L.append(verdict("blacktag", "member",
    "WWD (2020-11-18): Blacktag 'revealed a $3.75 million seed round led by Connect Ventures, a newly formed investment "
    "partnership between Creative Artists Agency (CAA) and New Enterprise Associates (NEA)'; The Hollywood Reporter the "
    "same day. Connect Ventures I is a fund of NEA's adviser (decisions.md), and its Michael Blank is a director on "
    "Blacktag's Form D.", ec="web", conf="high", cite=WWD_BT))
L.append(cls("blacktag", status="private", rng="below_1b",
    stage="Seed", stage_src="web_verified", stage_cite=WWD_BT, stage_conf="high", entry_date="2020-11-18",
    country="US", city="New York", city_src="formd_address", focus="Media, Gaming & Advertising",
    grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=CHECK,
    surfaces=SURF("blacktag",
        "the firm's own posts and listings -> no NEA post names Blacktag; Connect Ventures' own site (connectventures.com, "
        "read 2026-09-30) shows only TMRW Sports, Moises and Sekai",
        "Blacktag, Inc. (CIK 1835731, New York) -> one Form D, first sale 2020-08-14, $3,875,001 sold to 13 investors (the "
        "seed; Connect Ventures' Michael Blank a director); no later filing",
        over={"googlenews": "googlenews: Google News ('Blacktag') -> the 2020-11-18 seed reports (WWD, The Hollywood Reporter, "
                            "Deadline), the 2021 short film and launch, The New York Times 2021-10-20 'Blacktag Has Big Plans', "
                            "PCMag 2022-02-03; no later round"},
        extra=["company: blacktag.com, read 2026-09-30 -> the live creator network ('988 creators and counting', copyright "
               "2025, CAA and Splashlight as partners); no financing news"]),
    rounds=[rnd("2020-11-18", "Seed", 3750000, "Connect Ventures", True, WWD_BT, "press")],
    note="Blacktag, a New York platform and studio for Black creators (Akin Adebowale and Ousman Sahko); Connect Ventures "
         "led its $3.75M seed (WWD, 2020-11-18; Form D first sale 2020-08-14, $3.9M, 6 St. Johns Lane, New York). Its site "
         "is live with a 2025 copyright: private, below_1b. S2A: not graduated; the absence test found no round after the "
         "seed."))

# ================================================================ boisson (recall addition)
BI_BOI = READ["boisson_bi"]
FD_BOI = FDX(1963889, "0001963889-23-000001")
VINE_BOI = NEWS("boisson", "Is Non-Alcoholic Retailer Boisson Shutting Down")
BW_BOI = NEWS("boisson", "Receives New Funding From")
L.append(verdict("boisson", "member",
    "Business Insider (August 2022), read 2026-09-30: Boisson's '$12 million in seed funding': 'Connect Ventures, a "
    "partnership between Creative Artists Agency and VC firm New Enterprise Associates, and Blue Scorpion Investments ... "
    "co-led the round.' Connect's Michael Blank is a director on Boisson's Form D, Connect funded it again in September "
    "2023 (Business Wire), and the firm's own 2022 gift guide of 'the NEA and Connect Ventures portfolios' features it.",
    ec="web", conf="high", cite=BI_BOI))
L.append(cls("boisson", status="private", rng="below_1b",
    stage="Seed", stage_src="web_verified", stage_cite=BI_BOI, stage_conf="high", entry_date="2022-08-03",
    country="US", city="New York", city_src="formd_address", focus="Consumer & Marketplaces",
    grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=CHECK,
    surfaces=SURF("boisson",
        "the firm's own posts -> the gift guide of 2022-12-22 ('the NEA and Connect Ventures portfolios') features Boisson; "
        "no post names a round",
        "Boisson Inc. (CIK 1963889, 177 Court Street, Brooklyn) -> one Form D, first sale 2022-04-05, $17,627,363 sold to "
        "27 investors (the seed; Connect Ventures' Michael Blank a director); no later filing",
        over={"googlenews": "googlenews: Google News ('Boisson' with non-alcoholic, funding, raises, '$12 million', Nick Bodkins) "
                            "-> the 2022 seed coverage, Business Wire 2023-09-27 (new funding from Convivialité Ventures and "
                            "Connect Ventures), the April 2024 Chapter 11 reorganization (Brewbound) and 2025-26 releases of the "
                            "operating company; no Series A and no round near the $24M step-up (the tennis player Loïs Boisson "
                            "fills the rest)"},
        extra=["vinepair: VinePair 2024-03-29, read -> '$12 million in seed funding' in August 2022 and '$5 million in "
               "additional funding' from Convivialité Ventures and Connect Ventures in September 2023; no other round"]),
    rounds=[rnd("2022-08-03", "Seed", 12000000, "Connect Ventures and Blue Scorpion Investments", True, BI_BOI, "press"),
            rnd("2023-09-27", "unnamed", 5000000, None, True, BW_BOI, "press")],
    note="Boisson, the non-alcoholic drinks retailer founded in Brooklyn (Nick Bodkins), with stores in New York; Connect "
         "Ventures co-led its $12M seed announced 2022-08-03 (Business Insider). It filed Chapter 11 in April 2024 to "
         "reorganize around e-commerce and wholesale, and a July 2025 release names new leadership of the operating "
         "company: private, below_1b. S2A: not graduated; the only later money is the $5M of September 2023 (VinePair), "
         "unnamed and below the $24M step-up."))

# ================================================================ camp-family-experience-retailer (recall addition)
GG22 = POST("nea-holiday-gift-guide-2022")
POST("nea-holiday-gift-guide-2021")
POST("international-womens-day-2022")
CAMP_FD = {a: FDX(1754583, a) for a in ("0001754583-21-000001", "0001754583-21-000002", "0001754583-22-000001",
                                         "0001754583-23-000001")}
L.append(verdict("camp-family-experience-retailer", "member",
    "The firm's own posts list CAMP among its portfolio companies: the first NEA gift guide (2021-12-10, 'our favorite "
    "portfolio company offerings'), the International Women's Day 2022 post ('our female-founded and women-led portfolio "
    "companies': 'Camp: A family experience company') and the 2022 gift guide of 'the NEA and Connect Ventures "
    "portfolios'. Business Insider (2024-01-12, read) quotes Connect Ventures' head and says Connect 'has also backed ... "
    "the toy retailer Camp'. Camp NYC, Inc. of New York (Ben Kaufman).", ec="site_listing", conf="high", cite=GG22))
L.append(cls("camp-family-experience-retailer", status="private", rng="below_1b", stage="undetermined",
    country="US", city="New York", city_src="formd_address", focus="Consumer & Marketplaces",
    rounds=[rnd("2021-10-28", "convertible notes (Form D)", 1500000, None, None, CAMP_FD["0001754583-21-000001"], "filing"),
            rnd("2021-12-17", "SAFEs (Form D)", 7000000, None, None, CAMP_FD["0001754583-21-000002"], "filing"),
            rnd("2022-03-25", "unnamed equity (Form D)", 42432938, None, None, CAMP_FD["0001754583-22-000001"], "filing"),
            rnd("2023-05-30", "unnamed equity (Form D)", 17898646, None, None, CAMP_FD["0001754583-23-000001"], "filing")],
    note="CAMP, the New York family experience store and toy retailer founded by Ben Kaufman (Camp NYC, Inc., 91 Fifth "
         "Avenue on its Form Ds), still opening branded experiences in 2025-26: private, below_1b. The firm's posts carry "
         "it from December 2021, but no source names the round NEA or Connect Ventures bought (the Form Ds show notes and "
         "SAFEs in late 2021, $42.4M of equity in March 2022 and $17.9M in May 2023, with no NEA or Connect director), so "
         "the stage is undetermined and no entry date is given."))

# ================================================================ future-retail (membership stays uncertain)
NIE_FR = NEWS("future-retail", "Future retail ordered into liquidation by NCLT Mumbai")
L.append(cls("future-retail", status="defunct", rng="below_1b", stage="undetermined",
    country="IN", country_src="web_verified", country_cite=NIE_FR, city="Mumbai", focus="Consumer & Marketplaces",
    note="Future Retail Ltd, the Mumbai-listed retailer of Kishore Biyani's Future Group (Big Bazaar); the Mumbai bench of "
         "the NCLT ordered its liquidation after every resolution bid failed (New Indian Express, "
         "2024-07-30), and its brands went to auction in 2025: defunct, below_1b. The firm's 2014-15 page gives no year "
         "and only the label 'early', and no source dates or names NEA's purchase, so the stage is undetermined; the "
         "membership question (X1 or a pre-merger private stake) is still open."))

# ================================================================ aquila-biopharmaceuticals-inc
AQ_PROXY = SEC("https://www.sec.gov/Archives/edgar/data/704292/000100547700007211/0001005477-00-007211.txt")
SEC("https://www.sec.gov/Archives/edgar/data/704292/000104746999005798/0001047469-99-005798.txt")
L.append(cls("aquila-biopharmaceuticals-inc", status="acquired", rng="below_1b", country="US", city="Framingham",
    city_src="web_verified", focus="Healthcare & Bio",
    note="Aquila Biopharmaceuticals (Cambridge Biotech until 1996), vaccine adjuvants, 175 Crossing Boulevard, Framingham, "
         "Massachusetts (NEA VI's 13G, Item 1(b)). Its stockholders met on 2000-11-15 to adopt a merger agreement with "
         "Antigenics (proxy letter, 2000-10-20) and it deregistered on 2000-11-17: acquired, below_1b."))

# ================================================================ aveo-pharmaceuticals-inc
L.append(verdict("aveo-pharmaceuticals-inc", "not_member",
    "X1 and R2: NEA's first position is the May 2016 PIPE it led into AVEO (8-K of 2016-05-13, bought through Growth "
    "Equity Opportunities Fund IV), a company listed on Nasdaq since its March 2010 IPO; R2 names AVEO among the Growth "
    "Equity Opportunities vehicles' listed issuers. EDGAR full-text search finds no filing naming New Enterprise "
    "Associates in AVEO before 2016, so no NEA private round came first.",
    ec="fund_filing", conf="high", cite=KNOWN["aveo-pharmaceuticals-inc"]["entry_stage_citation"]))

# ================================================================ cardima-inc
CARD_8K = SEC("https://www.sec.gov/Archives/edgar/data/1022570/000101376210003075/form8k.htm")
L.append(cls("cardima-inc", status="defunct", rng="below_1b", country="US", city="Fremont", city_src="web_verified",
    focus="Healthcare & Bio",
    note="Cardima, a Fremont, California maker of catheters for atrial fibrillation (47266 Benicia Street on EDGAR). Its "
         "board approved a Chapter 11 petition on 2010-10-26, to be filed by 2010-12-17 (8-K, 2010-12-17); it filed nothing "
         "after and the SEC revoked its registration in 2013. A bankruptcy with no sale on record: defunct, below_1b."))

# ================================================================ censtor-corp-ca
SEC("https://www.sec.gov/Archives/edgar/data/932094/0000891618-96-002187.txt")
L.append(cls("censtor-corp-ca", rng="below_1b", country="US", city="San Jose", city_src="web_verified",
    focus="Industrial & Robotics",
    note="Censtor, a developer of disk-drive head technology at 530 Race Street, San Jose (its 1996 10-K); after the 1996 sale "
         "of its operations to Read-Rite it kept only patent licensing from Los Gatos. Defunct, so below_1b."))

jl.write("g3a", L)
