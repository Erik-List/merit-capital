#!/usr/bin/env python3
"""Delta pass, tag d1, batch 1, second block (PRO-99): 7 graduation rows and the 3 rows that owed a country.
Run: NQ_TAG=d1 python3 judgments-d1b.py

Google News answered 503 all session (2026-09-30): no headline was decoded and nq.py returned an error, so no
Google News line is claimed for the two rows searched by hand (shoof-technologies, peng-peng).
"""
import json

import judge_lib as jl
from judge_lib import cls, rnd, GNEWS, GRADLINES, POST, W

L = []
ASOF = "2026-09-30"
_CLS = json.loads((jl.INV / "companies/classification.json").read_text())


def old(slug, *drop):
    rs = (_CLS.get(slug) or {}).get("funding_rounds") or []
    return [r for r in rs if not any(d.lower() in (r.get("round") or "").lower() for d in drop)]


# URLs read in this pass (WebFetch), found through a publisher's own search page or a web search.
FINSMES_BULLETIN = "https://www.finsmes.com/2019/07/bulletin-raises-7m-in-series-a-financing.html"  # index entry read; the page itself answers 403
TC_CHILL_TOTAL = "https://techcrunch.com/2012/11/29/pivot-pivot-pivot-pivot/"  # printed by TechCrunch's own search
FINOVATE_HATCH = "https://finovate.com/hatch-raises-20-million-for-small-business-banking/"  # on the hatch row
BUN_BLOG = "https://bun.com/blog/bun-joins-anthropic"
PRN_SUBJECT = ("https://www.prnewswire.com/news-releases/leading-digital-learning-platform---subject---raises-29-4-"
               "million-in-series-a-led-by-owl-ventures-301506849.html")
PRN_SHOOF = ("https://www.prnewswire.com/news-releases/shoof-technologies-announces-43-million-seed-funding-led-by-"
             "kleiner-perkins-and-movida-300584241.html")
YAHOO_SHOOF = "https://finance.yahoo.com/news/shoof-technologies-announces-funding-ntt-183500133.html"
AVCJ_PENGPENG = "https://www.avcj.com/avcj/news/57289/china-social-mobile-app-pengpeng-raises-usd17m-from-vcs"  # read on AVCJ's KPCB China listing; the item page answers 429
TECHNODE_PENGPENG = "https://technode.com/2014/07/25/former-zynga-china-gm-tencent-exec-roll-social-gaming-app-pengpeng/"

TC_STIPPLE_SEED = GNEWS("stipple", "Raises $2M")
TC_STIPPLE_A = GNEWS("stipple", "Raises $5M")
TC_NEARSIDE_B = GNEWS("nearside", "gets $58M Series B")
HATCH_POST = POST("hatch-series-a")

# bulletin: $2.2M seed in May 2017, $7M Series A in July 2019.
L.append(cls("bulletin", entry_date="2017-05-24", grad="graduated", grad_src="web_verified",
             grad_cite=FINSMES_BULLETIN, grad_conf="high",
             rounds=old("bulletin") + [rnd("2019-07-15", "Series A", 7000000, None, None, FINSMES_BULLETIN, "press")],
             note="S2A: graduated. FinSMEs (2019-07-15), 'Bulletin Raises $7M in Series A Financing': 'Bulletin, a "
                  "NYC-based retail technology company', 'closed $7m Series A funding' (headline and index entry "
                  "read; the article page refuses the fetch)."))

# chill: $1.5M seed in September 2011; by November 2012 nearly $10M in total.
L.append(cls("chill", entry_date="2011-09-06", grad="graduated", grad_src="web_verified", grad_cite=TC_CHILL_TOTAL,
             grad_conf="medium",
             rounds=old("chill") + [rnd("2012-06-27", "unnamed venture round", 8000000, None, None, TC_CHILL_TOTAL,
                                        "press")],
             note="S2A: graduated. TechCrunch (2012-11-29): 'The company's raised nearly $10 million in total from "
                  "investors like Kleiner Perkins, Redpoint Ventures, 500 Startups', linking PandoDaily's report of "
                  "June 2012 that Chill 'gets $8 million'; an unnamed $8M round after the $1.5M seed is above the "
                  "$5M step. Medium because the PandoDaily page itself no longer loads."))

# nearside: the renamed Hatch; the hatch row already carries the same graduation.
L.append(cls("nearside", entry_date="2019-01", grad="graduated", grad_src="first_party", grad_cite=HATCH_POST,
             grad_conf="high",
             rounds=[rnd("2019-01", "Seed", 5000000, None, True, FINOVATE_HATCH, "press"),
                     rnd("2020-02", "Series A", 14000000, None, True, FINOVATE_HATCH, "press")]
             + old("nearside", "Seed", "Series A"),
             note="S2A: graduated, as the hatch row (the same company) reads. The firm's post of 2021-04-13 says it "
                  "supported Hatch 'from Seed to Series A'; Finovate dates the $5M seed to January 2019 and the $14M "
                  "Series A to February 2020 ($20M in the two rounds, which the earlier note took for the Series A "
                  "alone)."))

# optic: $11M seed in July 2022, then the pivot to BIOPTIC; no later round anywhere.
_OPTIC = []
for ln in GRADLINES("optic"):
    k = ln.split(":", 1)[0]
    if k == "googlenews":
        ln = ("googlenews: Google News, the company's name with round and exit words -> 100 results on a common word; "
              "the only ones about this company are the seed reports of 2022-07-20 (CoinDesk, The Block); no Series A "
              "or later round")
    elif k == "googlenews_firm":
        ln = ("googlenews_firm: Google News, the company's name beside the firm's -> 7 results, the newest about the "
              "company 'NFT fraud fighters Optic raise $11 million in seed funding round' (The Block, 2022-07-20); "
              "no Series A or later round")
    elif k == "sibling":
        ln = ("sibling:y-combinator: its row for Optic -> a different company (an API tool, New York, acquired); it "
              "says nothing about this one")
    _OPTIC.append(ln)
_OPTIC += ["sibling:greylock: its row for Optic -> the same company (now BIOPTIC), stage undetermined, no later round "
           "in its note",
           "company: bioptic.io, where optic.xyz redirects (footer 'Optic, Inc.') -> a product page for pharma "
           "research; no funding round, investor or acquisition is mentioned"]
L.append(cls("optic", entry_date="2022-07-20", grad="not_graduated", grad_src="absence_check", grad_asof=ASOF,
             grad_conf="medium", surfaces=_OPTIC,
             note="S2A: not graduated; the absence test found no round after the $11M seed of July 2022 (surfaces "
                  "listed), and the company has since turned from NFT fraud detection to BIOPTIC, research software "
                  "for pharma teams."))

# oven (Bun): $7M seed led by the firm, $19M Series A led by Khosla Ventures, acquired by Anthropic in December 2025.
L.append(cls("oven", entry_date="2022-08-24", grad="graduated", grad_src="web_verified", grad_cite=BUN_BLOG,
             grad_conf="high",
             rounds=old("oven") + [rnd("2023", "Series A", 19000000, "Khosla Ventures", None, BUN_BLOG, "company")],
             note="S2A: graduated. The company's own post on joining Anthropic gives its funding as a '$7 million "
                  "seed round led by Kleiner Perkins' and a '$19 million Series A led by Khosla Ventures', $26M in "
                  "all; the Series A followed the 1.0 release of September 2023."))

# stipple: $2M seed in November 2010, $5M Series A in May 2012.
L.append(cls("stipple", entry_date="2010-11-18", grad="graduated", grad_src="web_verified", grad_cite=TC_STIPPLE_A,
             grad_conf="high",
             rounds=[rnd("2010-11-18", "Seed", 2000000, None, True, TC_STIPPLE_SEED, "press"),
                     rnd("2012-05-10", "Series A", 5000000, "Floodgate; Relevance Capital", None, TC_STIPPLE_A,
                         "press")],
             note="S2A: graduated. TechCrunch (2012-05-10): 'raised $5 million in a Series A round of funding' led "
                  "by Floodgate and Relevance Capital, after 'a $2 million seed round from Kleiner Perkins Caufield "
                  "& Byers, Mike Maples' Floodgate, Justin Timberlake, and others', which TechCrunch reported on "
                  "2010-11-18 (the entry date)."))

# subject: seed led by the firm in May 2021, $29.4M Series A in March 2022.
L.append(cls("subject", entry_date="2021-05-26", grad="graduated", grad_src="web_verified", grad_cite=PRN_SUBJECT,
             grad_conf="high",
             rounds=old("subject") + [rnd("2022-03-22", "Series A", 29400000, "Owl Ventures", True, PRN_SUBJECT,
                                          "company")],
             note="S2A: graduated, the $29.4M Series A of 2022-03-22 led by Owl Ventures with Kleiner Perkins and "
                  "SoftBank taking part (the company's release, which also gives $34.7M raised in all and a Los "
                  "Angeles base)."))

# peng-peng: identified. Pengpeng is the social gaming app of Asia Innovations (pengpeng.la); KPCB China was in its
# $17M Series B of April 2015.
WIKI_ASIG = W("Asia Innovations Group")
L.append(cls("peng-peng", status="private", rng="below_1b", stage="Growth", stage_src="web_verified",
             stage_cite=AVCJ_PENGPENG, stage_conf="medium", entry_date="2015-04-09",
             country="SG", country_src="web_verified", country_cite=WIKI_ASIG,
             city="Singapore", city_src="web_verified", focus="Consumer & Marketplaces",
             flags=["kpcb_china"], clear=["identity_unresolved"],
             rounds=[rnd("2015-04-09", "Series B", 17000000, None, True, AVCJ_PENGPENG, "press")],
             extra={"seed_to_a_graduation": None},
             note="Identified: TechNode (2014-07-25) describes Pengpeng, a social gaming app at pengpeng.la (the "
                  "tile's domain) developed by Asia Innovations of Andy Tian and Ouyang Yun, and AVCJ (2015-04-09) "
                  "reports it 'raised $17 million in a Series B round of funding from KPCB China, Ventech Capital "
                  "and Magic Stone Alternative Investments', the only round on record naming the firm (medium: an "
                  "earlier entry is not ruled out). A KPCB China position (decisions.md X1). Asia Innovations Group "
                  "is now 'a mobile social company based in Singapore' running Uplive (Wikipedia); the SPAC merger "
                  "it announced in September 2022 is not on record as completed, so the row reads private with no "
                  "mark."))

# shoof-technologies: identified. $4.3M seed led by the firm in January 2018.
_SHOOF = ["firm: the firm's own posts and listings for Shoof Technologies -> on the enterprise tiles for 2018-21 only; "
          "no post names the company",
          "formd: EDGAR's company search and full-text search for 'Shoof' -> no filer of that name and no Form D",
          "techcrunch: TechCrunch's own search for 'Shoof Technologies' -> 0 results",
          "crunchbase_news: Crunchbase News's own search for 'Shoof Technologies' -> 0 results",
          "prnewswire: the company's own releases -> the $4.3M seed (2018-01-18) and an investment of undisclosed size "
          "by NTT DoCoMo Ventures (2019-02-19, carried by Yahoo Finance); no named or sized later round",
          "company: shooftech.com -> now an unrelated casino-review page (the row's earlier note, 2026-09-30); no "
          "newsroom left to read"]
L.append(cls("shoof-technologies", rng="below_1b", stage="Seed", stage_src="web_verified", stage_cite=PRN_SHOOF,
             stage_conf="high", entry_date="2018-01-18", grad="not_graduated", grad_src="absence_check",
             grad_asof=ASOF, grad_conf="medium", surfaces=_SHOOF,
             country="US", city="Sunnyvale", city_src="web_verified", focus="Industrial & Robotics",
             clear=["identity_unresolved"],
             rounds=[rnd("2018-01-18", "Seed", 4300000, "Kleiner Perkins; Movida Japan", True, PRN_SHOOF, "company"),
                     rnd("2019-02-19", "unnamed strategic investment", None, "NTT DoCoMo Ventures", None, YAHOO_SHOOF,
                         "company")],
             note="Identified: the company's release of 2018-01-18 (Sunnyvale) announces '$4.3 million seed funding "
                  "led by Kleiner Perkins and Movida Japan' for wireless asset tracking in industrial IoT (founders "
                  "George Flammer and Elad Gottlib). S2A: not graduated; the only later money on record is an "
                  "investment of undisclosed size by NTT DoCoMo Ventures in February 2019, neither named a Series A "
                  "nor sized, and the absence test found nothing after it (surfaces listed; Google News was "
                  "unavailable on the day). Its fate is not on record, so the status stays unknown."))

# singularity-network: still not identified; the country is the desk's, flagged as inferred.
L.append(cls("singularity-network", country="US", flags=["country_prior"],
             extra={"hq_country_confidence": "low"},
             note="Country inferred from the firm's US desk (flag country_prior), not read off a source: the company "
                  "behind the tile still cannot be named."))

if __name__ == "__main__":
    jl.write("d1b", L)
