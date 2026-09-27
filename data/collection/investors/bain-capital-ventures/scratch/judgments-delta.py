"""PRO-162 delta after the rebuild: the recall addition Cogsy, the home-health Adaptive split from Adaptive Security, and
Bluestem's stage. Evidence read 2026-09-27: the firm's post on Cogsy, Tech.eu on the seed round, Wikipedia (Adii Pienaar),
Companies House (COGSY LIMITED 12973044), Home Health Care News on Adaptive Innovations' Series A."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd, POST, SITE, W, NEWS = jl.cls, jl.verdict, jl.rnd, jl.POST, jl.SITE, jl.W, jl.NEWS
L = []
COGSY_POST = POST("our-seed-investment-in-cogsy")
TECHEU = "https://tech.eu/2021/12/22/e-commerce-veteran-adii-pienaar-goes-for-the-hattrick-with-new-venture-cogsy-reels-in-5-million-in-accel-led-seed-round/"
CH = "https://find-and-update.company-information.service.gov.uk/company/12973044"
L.append(verdict("cogsy", "member",
    "The firm's own post 'The Next Generation Of Inventory Management: Our Seed Investment In Cogsy' (2021-12-22): 'BCV is a supporting "
    "investor in Cogsy's $6 million seed round'; Tech.eu: 'Cogsy's $5 million seed round was led by Accel and saw Bain Capital Ventures "
    "... participating'. Not on the live list (a sub-10% stake, decisions.md R3); added by the recall probe.",
    ec="web", conf="high", cite=COGSY_POST))
L.append(cls("cogsy", status="acquired", rng="below_1b", country="GB", country_src="web_verified", country_cite=CH,
    flags=["city_unknown"], focus="SaaS", stage="Seed", stage_src="first_party", stage_conf="high", stage_cite=COGSY_POST,
    entry_date="2021-12", grad="not_graduated", grad_src="web_verified", grad_cite=W("Adii Pienaar"), grad_asof="2026-09-27",
    surfaces=jl.GRADLINES("cogsy", name="Cogsy",
        formd_note="the company is UK-registered (COGSY LIMITED, Companies House 12973044) and files no Form D -> not applicable",
        extra=["googlenews: Google News, the company's name -> 3 result(s); the only funding report is the December 2021 seed "
               "('WooCommerce founder raises £4.5m for Cogsy', BusinessCloud, 2021-12-22); no later round",
               "wikipedia: the founder's article (Adii Pienaar) -> 'co-founded Cogsy in 2020, which was acquired by Mayple in 2023'; "
               "no later round",
               "company: Companies House, COGSY LIMITED -> incorporated 2020, dissolved 13 April 2026",
               "sibling:accel: its row for Cogsy -> no later round in its note (reads it wound down)"]),
    note="Inventory and commerce-operations software for small online sellers, founded in 2020 by Adii Pienaar (WooCommerce's "
         "co-founder); UK-registered (COGSY LIMITED, dissolved April 2026). BCV joined the Accel-led seed of December 2021 (the firm's "
         "post; Tech.eu). 'Cogsy was acquired by Mayple in 2023' (Wikipedia, Adii Pienaar) with no later round, which ends the S2A "
         "window: not graduated. Sibling Accel reads defunct and US without a citation."))
HHCN = NEWS("adaptive-adaptive-co", "Lands $50M Series A")
L.append(cls("adaptive-adaptive-co", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="New York",
    city_src="web_verified", focus="Healthcare & Bio", stage="Seed", stage_src="first_party", stage_conf="medium",
    stage_cite=SITE("adaptive-adaptive-co"), entry_date="2025",
    grad="graduated", grad_src="web_verified", grad_cite=HHCN, grad_conf="high",
    rounds=[rnd("2026-06", "Series A", 50000000, "Felicis", True, HHCN, "press")],
    note="Adaptive Innovations, an AI-native home-health provider (New York City and Dallas, per Home Health Care News). BCV's "
         "listing: 2025, Seed (Christina Melas-Kyriazi, Ryan Kim), at the $10M seed the company disclosed with its Series A. 'The "
         "Series A round was led by Felicis, with significant participation from Bain Capital Ventures' ($50M, June 2026), which "
         "graduates it. Not the Adaptive Security row ('adaptive'), which the firm's CMS also titles 'Adaptive'."))
L.append(cls("bluestem-brands", stage="undetermined",
    note="Online retailer (Eden Prairie; formerly Fingerhut Direct Marketing). 'Bain Capital' in its 2011 S-1 means Bain Capital "
         "Venture Fund, L.P. and affiliates; the company was sold to Capmark Financial in 2014 and later to Chinese investors. The "
         "firm's position dates from the February 2004 recapitalisation of Fingerhut (Wikipedia lists 'Bain Capital Ventures (2004)' "
         "among its owners); no source read names the round or the stake, so the stage is undetermined. OPEN for Erik: whether the "
         "2004 investor group took control of Fingerhut (D4)."))
if __name__ == "__main__":
    jl.write("delta-1", L)
