"""Delta grind after the one rebuild (PRO-104): the four recall additions and four HQ fills."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, verdict, rnd, write  # noqa: E402

ORE = "https://impactalpha.com/ore-energy-lands-43-million-series-a-for-long-duration-battery-storage/"
FIFTH = "https://pulse2.com/fifth-dimension-raises-26-million-series-a-to-scale-ai-decision-intelligence-platform-for-real-assets/"
PEAQ = "https://techfundingnews.com/berlin-based-blockchain-startup-peaq-lands-15m-to-build-decentralised-apps-to-access-from-anywhere/"
LH_POST = ("https://web.archive.org/web/20110402172305/http://www.holtzbrinck-ventures.com:80/index.php?aktuelle-news"
           "&newsdetail=20110325-33_finanzierungsrunde-lieferheld-streicht-vier-millionen-euro-ein")
LH_DS = "https://www.deutsche-startups.de/2011/11/16/lieferheld-delivery-hero-finanzierung/"
LH_ACQ = "https://www.deutsche-startups.de/2012/02/28/delivery-hero-lieferheld-justeat/"
L = [
    verdict("ore-energy", "member", "Recall probe: 'raised $43 million in Series A financing, led by Plural Energy and "
            "Munich-based HV Capital' (impactalpha, 2026-08-07). A fund investment the firm's 2026 export predates.",
            ec="web", conf="high", cite=ORE),
    cls("ore-energy", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
        stage_cite=ORE, entry_date="2026-08", focus="Climate & Energy", country="NL", country_cite=ORE,
        city="Amsterdam",
        note="Iron-air long-duration battery storage, Amsterdam (founded 2023). HV co-led the $43M Series A with Plural "
             "Energy (impactalpha, 2026-08-07); no valuation published.",
        rounds=[rnd("2026-08-04", "Series A", 43_000_000, "Plural Energy, HV Capital", True, ORE)]),
    verdict("fifth-dimension", "member", "Recall probe: 'raised $26 million in a Series A funding round led by HV "
            "Capital' (Pulse 2.0, 2026-05-12; UKTN quotes HV partner Lina Chong).", ec="web", conf="high", cite=FIFTH),
    cls("fifth-dimension", status="private", rng="below_1b", stage="Series A", stage_src="web_verified",
        stage_conf="high", stage_cite=FIFTH, entry_date="2026-05", focus="AI & Applied AI", country="GB",
        country_cite=FIFTH, city="London",
        note="AI decision intelligence for real-asset investors, London. HV led the $26M Series A (Pulse 2.0, 2026-05-12); "
             "no valuation published.",
        rounds=[rnd("2026-05-12", "Series A", 26_000_000, "HV Capital", True, FIFTH)]),
    verdict("peaq", "member", "Recall probe: peaq 'raised $15 million in a pre-launch multi-tranche funding round led by "
            "Generative Ventures and Borderless Capital with the participation of ... HV Capital' (Tech Funding News, "
            "2024-03-27). A token position mapped to its issuing organisation, EoT Labs GmbH (COLLECTION.md s1).",
            ec="web", conf="high", cite=PEAQ),
    cls("peaq", status="private", rng="below_1b", stage="undetermined", focus="Crypto & Web3", country="DE",
        country_cite=PEAQ, city="Berlin", flags=["token_funded"],
        extra={"seed_to_a_graduation": "undetermined"},
        note="DePIN layer-1 network built by EoT Labs GmbH, Berlin. HV joined the $15M pre-launch token round led by "
             "Generative Ventures and Borderless Capital (Tech Funding News, 2024-03-27): a token-funded position, so the "
             "stage and the graduation read undetermined (COLLECTION.md s6).",
        rounds=[rnd("2024-03-27", None, 15_000_000, "Generative Ventures, Borderless Capital", True, PEAQ)]),
    verdict("lieferheld", "member", "The firm's own news post of 2011-03-25 reports Lieferheld's EUR 4M round; "
            "deutsche-startups (2011-11-16): 'Holtzbrinck Ventures und Team Europe statteten Lieferheld zuvor bereits mit "
            "einer Million Euro Startkapital aus', then EUR 4M from Tengelmann, Holtzbrinck Ventures and Team Europe. "
            "Separated from Delivery Hero (decisions.md R1).", ec="site_listing", conf="high", cite=LH_POST),
    cls("lieferheld", status="acquired", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="medium",
        stage_cite=LH_DS, entry_date="2010", grad="graduated", grad_src="first_party", grad_cite=LH_POST,
        focus="Consumer & Marketplaces", country="DE", country_cite=LH_DS, city="Berlin",
        extra={"status_citation": LH_ACQ},
        note="Online food-delivery marketplace, Berlin (founded 2010, a Team Europe company). HV and Team Europe gave it EUR 1M "
             "'Startkapital' (seed capital; deutsche-startups, 2011-11-16). The EUR 4M round of spring 2011 with Tengelmann "
             "(the firm's own post, 2011-03-25) graduates the row under the step-up test: EUR 4.0M @ ECB 2011-03-25 (EUR/USD "
             "1.4115) = $5.6M, above max(2x the seed, $5M). acq. by Delivery Hero, Feb 2012; its shareholders took Delivery "
             "Hero shares (deutsche-startups, 2012-02-28).",
        rounds=[rnd("2010", "Seed", None, "Team Europe", True, LH_DS),
                rnd("2011-03-25", None, 5_646_000, "Tengelmann", True, LH_POST, "firm")]),
    cls("milleporte", country="JP", country_cite="https://www.milleporte.com/about/company", city="Tokyo"),
    cls("namshi", country="AE", country_src="model_knowledge", city="Dubai"),
    cls("spotcap", country="DE", country_src="model_knowledge", city="Berlin"),
    cls("wind", country="DE", country_src="model_knowledge", city="Berlin"),
]
write("delta-001", L)
