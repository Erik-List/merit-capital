"""PRO-79 S2A pass: the open Seed rows, decided on the standard surfaces
(scripts/graduation-surfaces.py, 2026-09-26) and cited ends (COLLECTION.md 6)."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls = jl.cls
ASOF = "2026-09-26"
FIRM = "firm: atomico.com insights archive (217 posts 2011-2025 from captures, plus the firm's 2025-2026 pages found by Google News)"

L = []
L.append(cls("deeploi", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=ASOF,
             surfaces=[FIRM + " -> only the Jan 2024 seed post",
                       "googlenews: \"Deeploi\" with round words -> the Mar 2023 pre-seed and the Jan 2024 seed only (6 items)",
                       "googlenews_local: de-DE \"Deeploi\" Finanzierung/Finanzierungsrunde/Millionen -> the Jan 2024 EUR 6M round only (7 items to Apr 2025)",
                       "techcrunch: Deeploi -> the 2023 pre-seed and the 2024 seed, no later round",
                       "crunchbase_news: Deeploi -> none",
                       "formd: n/a, a German company with no US filings"],
             note="S2A: seed Jan 2024, past the 24-month window on 2026-09-26; no later round on any surface -> not graduated"))
L.append(cls("equal-media", grad="not_graduated", grad_src="web_verified", grad_conf="medium", grad_asof=ASOF,
             grad_cite="https://en.wikipedia.org/wiki/State_(website)",
             surfaces=[FIRM + " -> no Equal Media or State post",
                       "googlenews: \"Equal Media\" with round words -> 22 unrelated items (media-equality news), no round",
                       "googlenews_firm: \"Equal Media\" \"Atomico\" -> none",
                       "techcrunch: Equal Media -> unrelated items; its own State coverage (Feb 2013) reports only the same $14M",
                       "crunchbase_news: Equal Media -> unrelated items"],
             note="S2A: the May 2012 $14M seed was the last round on record; the service was inactive by 2020 and Equal Media Ltd dissolved in 2024 (Wikipedia) -> not graduated, a cited end"))
L.append(cls("farmdrop", grad="graduated", grad_src="web_verified", grad_conf="high", grad_asof=ASOF,
             grad_cite="https://techcrunch.com/2017/04/23/farmdrop/",
             note="S2A: 'Online grocery platform Farmdrop raises GBP 7M Series A led by Atomico' (TechCrunch, Apr 2017), 14 months after the Feb 2016 Series Seed -> graduated",
             rounds=[jl.rnd("2016-02-03", "Series Seed", None, "Atomico", True, "https://find-and-update.company-information.service.gov.uk/company/08111929/filing-history"),
                     jl.rnd("2017-04-23", "Series A", None, "Atomico", True, "https://techcrunch.com/2017/04/23/farmdrop/"),
                     jl.rnd("2018-06-14", "Series B", None, None, None, "https://techcrunch.com/2018/06/14/farmdrop-picks-up-10m-series-b/")]))
L.append(cls("hailo", grad="graduated", grad_src="web_verified", grad_conf="medium", grad_asof=ASOF,
             grad_cite="https://en.wikipedia.org/wiki/Hailo",
             note="S2A: 'Hailo received $3.0 million in two tranches of Seed round funding in 2011'; 'In March 2012, Hailo received $17 million in Series A round funding led by Accel Partners', with Atomico contributing (Wikipedia) -> graduated",
             rounds=[jl.rnd("2011", "Seed", 3000000, None, True, "https://en.wikipedia.org/wiki/Hailo"),
                     jl.rnd("2012-03", "Series A", 17000000, "Accel", True, "https://en.wikipedia.org/wiki/Hailo")]))
L.append(cls("heysan", grad="not_graduated", grad_src="web_verified", grad_conf="high", grad_asof=ASOF,
             grad_cite="https://www.ycombinator.com/companies/heysan",
             surfaces=[FIRM + " -> none after the 2008-2012 listings",
                       "googlenews: \"Heysan\" with round words -> none",
                       "googlenews_firm: \"Heysan\" \"Atomico\" -> none",
                       "techcrunch: Heysan -> no Heysan round (3 unrelated items)",
                       "crunchbase_news: Heysan -> none",
                       "formd: n/a, the 2007 entry predates electronic Form D filing (Sep 2008)"],
             note="S2A: the summer-2007 seed was the last round; 'Heysan was acquired by Good Technology in May 2009' (YC's company page) -> not graduated, a cited end"))
L.append(cls("opna", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=ASOF,
             surfaces=[FIRM + " -> only the Sep 2023 seed post",
                       "googlenews: \"Opna\" with round words -> the Sep 2023 $6.5M seed only (the rest is Opna Bio, a different company)",
                       "googlenews_firm: \"Opna\" \"Atomico\" -> the Sep 2023 seed and 2024 features, no later round",
                       "techcrunch: Opna -> the Sep 2023 seed only",
                       "crunchbase_news: Opna -> a Feb 2024 seed-market roundup only",
                       "companies_house: Salt Global Tech Ltd (13944072) confirmation statement of Feb 2026 still lists Atomico Venture VI's SEED 2 shares, no later preferred class"],
             note="S2A: seed Sep 2023, past the 24-month window on 2026-09-26; no later round on any surface or in the register -> not graduated"))
L.append(cls("siine", grad="not_graduated", grad_src="web_verified", grad_conf="high", grad_asof=ASOF,
             grad_cite="https://find-and-update.company-information.service.gov.uk/company/07300906",
             surfaces=[FIRM + " -> none after the 2011-2012 listings",
                       "googlenews: \"Siine\" with round words -> none",
                       "googlenews_local: en-GB \"Siine\" -> none",
                       "techcrunch: Siine -> the Feb 2011 seed and the Oct 2011 launch only",
                       "crunchbase_news: Siine -> none"],
             note="S2A: the Feb 2011 GBP 550K seed was the last round on record; Siine Ltd dissolved 2018-12-11 (register) -> not graduated, a cited end"))
L.append(cls("silk", grad="not_graduated", grad_src="web_verified", grad_conf="high", grad_asof=ASOF,
             grad_cite="https://techcrunch.com/2016/08/10/palantir-acquires-data-visualization-startup-silk/",
             surfaces=[FIRM + " -> none after the 2011-2020 listings",
                       "techcrunch: Silk -> the site search returns only unrelated items; read directly, its archive holds the May 2011 seed and the Aug 2012 '$1.6 million seed funding round' (NEA), nothing later",
                       "googlenews_local: nl-NL \"Silk\" investering/financiering -> Emerce 2012 '1,6 miljoen dollar voor Amsterdamse startup Silk' (the same seed) and NU 2016 on the Palantir purchase; no Series A",
                       "googlenews: \"Silk\" with round words -> Silk Road noise, no Silk round",
                       "crunchbase_news: Silk -> unrelated items"],
             note="S2A: after the May 2011 EUR 320K seed the next round was NAMED a seed (NEA, Aug 2012) and the Oct 2013 $1.6M unnamed round is below the $5M step-up for a pre-2015 entry; Palantir's Aug 2016 acqui-hire ended it (TechCrunch) -> not graduated, a cited end"))

if __name__ == "__main__":
    jl.write("s2a-001", L)
