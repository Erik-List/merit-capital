"""Second pass s24, file c: rows first seen 2015 to 2026 (queue/s2-4.json). Only rows that change."""
import judge_lib as jl
from judge_lib import cls, verdict, rnd, ARCH, W, NEWS, POST

WV = "web_verified"
BVP = "Bessemer Venture Partners"

# Pages found through TechCrunch's own search or the session's web search, and read.
TC_RABBIT = "https://techcrunch.com/2013/02/28/rabbit-raises-3-3m-seed-round/"
TC_FRIDAY = "https://techcrunch.com/2020/11/23/friday-app-a-remote-work-tool-raises-2-1-million-led-by-bessemer/"
MAINEBIZ = "https://mainebiz.biz/article/portland-remote-work-startup-raises-21m-to-fund-further-growth"
FRIDAY_NOTICE = "https://friday.app/p/shutting-down"
# Headlines from the row's news queries, decoded to the publisher's URL; each page was read.
TECHCIRCLE_WYDR = NEWS("wydr", "VC-backed B2B marketplace Wydr shuts down")
VCC_INNOVITI = NEWS("innovati", "Trifecta Capital, NBFCs invest")
EVENTHUBS_TSM = NEWS("team-solomid-tsm", "NBA stars Stephen Curry and Andre Iguodala")
TC_VERTICE_B = NEWS("vertice", "Vertice raises $25M for AI-based tools")
TC_VERTICE_C = NEWS("vertice", "Vertice bags $50M")
TC_SPOT = NEWS("spot-ai", "emerges from stealth")
BOXED_PR = NEWS("boxed", "Boxed Announces Nationwide Launch")
ENTRACKR_VETIC_C = NEWS("vetic", "Exclusive: Petcare startup Vetic to raise $26 Mn")
VETIC_POST = POST("building-premier-pet-healthcare-with-vetic")

L = []

L.append(cls("rabbit", status="acquired", city="Redwood City",
             rounds=[rnd("2013-02-28", "Seed", 3300000, None, False, TC_RABBIT, "press")],
             note="Status aligned to the GV row: Rabbit shut down in July 2019 after a failed round and on 2019-07-31 "
                  "its remaining assets (intellectual property, software stack and patents) were acquired by Kast "
                  "(Wikipedia, Rabb.it), which GV's book reads as acquired with Kast as successor. Redwood City is "
                  "from the GV row (the company's 2015 Form D address). TechCrunch (2013-02-28) reports the $3.3M "
                  "seed from Google Ventures and others, without Bessemer; the firm's own date is 2015-05-21, the "
                  "time of the unnamed 2015 round the GV row records, so the stage stays undetermined."))

L.append(cls("wydr", stage="Series A", stage_src=WV, stage_cite=TECHCIRCLE_WYDR, stage_conf="high",
             city="Gurugram", city_src="web_verified",
             rounds=[rnd("2015-10", "angel round", None, "Sandeep Aggarwal", False, TECHCIRCLE_WYDR, "press"),
                     rnd("2017-01", "Series A", None, None, True, TECHCIRCLE_WYDR, "press")],
             note="Techcircle (2018-11-05): in January 2017 Wydr raised its Series A from Bessemer Venture Partners, "
                  "Stellaris Venture Partners, Axis Capital and Jungle Ventures, after an angel round in October "
                  "2015; the firm's own date is 2016-12-19. The same article calls the company "
                  "Gurugram-headquartered."))

L.append(cls("innovati", stage="Growth", stage_src=WV, stage_cite=VCC_INNOVITI, stage_conf="high",
             rounds=[rnd("2015-07", "Series A", 5000000, "Catamaran Ventures", False, VCC_INNOVITI, "press"),
                     rnd("2017-07", "Series B", 18000000, None, True, VCC_INNOVITI, "press")],
             note="The firm's Innovati is Innoviti Payment Solutions of Bangalore: same business and 2017 date as "
                  "the innoviti row, which is this company under its correct spelling. VCCircle (2019-03-15): "
                  "Innoviti last raised $18M in July 2017 in a Series B from the SBI-FMO Fund, Bessemer Venture "
                  "Partners and existing investor Catamaran Ventures, after a $5M Series A in July 2015 without "
                  "Bessemer. Entry at the Series B, so Growth."))

L.append(cls("team-solomid-tsm", stage="Series A", stage_src=WV, stage_cite=EVENTHUBS_TSM, stage_conf="high",
             rounds=[rnd("2018-07-24", "Series A", 37000000, BVP, True, EVENTHUBS_TSM, "press")],
             note="EventHubs (2018-07-26, following Forbes): the $37M raised for TSM's parent company Swift was "
                  "Series A funding led by Bessemer Venture Partners, which put in $25M of it; that is the $25M "
                  "investment reported in January 2018 and matches the firm's own date of 2018-02-12."))

L.append(verdict("homelight", "not_member",
                 "Sale consideration, the firm's Eave position (decisions.md R6): the firm lists this entry as "
                 "'HomeLight (fka Eave)' and describes 'HomeLight Home Loans (formerly Eave)'; HomeLight acquired "
                 "Eave, a digital mortgage startup, in July 2019 (Wikipedia, HomeLight). Eave is the row in this "
                 "base, on the firm's own 2016 investment, and no Bessemer round in HomeLight itself is on record.",
                 ec="site_listing", cite=ARCH("homelight"), conf="medium"))

L.append(cls("friday", status="defunct", stage="Seed", stage_src=WV, stage_cite=TC_FRIDAY, stage_conf="high",
             entry_date="2020-11-23", country="US", city="Portland", city_src="web_verified",
             clear=["country_unknown"],
             rounds=[rnd("2020", "earlier round ($450,000)", 450000, "Underscore VC", False, MAINEBIZ, "press"),
                     rnd("2020-11-23", "Seed", 2100000, BVP, True, TC_FRIDAY, "press")],
             note="TechCrunch (2020-11-23): Friday closed a $2.1M seed round led by Bessemer Venture Partners. "
                  "Mainebiz the same day calls it a Portland, Maine startup and says Underscore led a $450,000 round "
                  "earlier that year. The company's own notice (" + FRIDAY_NOTICE + ") says it was shutting down "
                  "and turning the app off on 2022-06-03, so defunct. Graduation left for the graduation pass."))

L.append(cls("vertice", stage="Series A", stage_src=WV, stage_cite=TC_VERTICE_B, stage_conf="medium",
             rounds=[rnd("2022-05", "Series A", 26000000, "83North and Bessemer Venture Partners", True, TC_VERTICE_B, "press"),
                     rnd("2024-01-17", "Series B", 25000000, "83North and Bessemer Venture Partners", True, TC_VERTICE_B, "press"),
                     rnd("2025-01-21", "Series C", 50000000, "Lakestar", True, TC_VERTICE_C, "press")],
             note="TechCrunch (2024-01-17): the $25M Series B was co-led by 83North and Bessemer, which also co-led "
                  "the London startup's previous round of $26M; Business Insider's May 2022 piece on that round "
                  "files it as a Series A, and TechCrunch (2025-01-21) puts total funding near $100M, which those "
                  "three rounds account for. Entry at the $26M Series A; the firm's partnered year is 2021 and the "
                  "announcement came in May 2022. London (GB) confirmed."))

L.append(cls("spot-ai", stage="Series A", stage_src=WV, stage_cite=TC_SPOT, stage_conf="high",
             entry_date="2021-10-15",
             rounds=[rnd(None, "Seed", 2000000, None, False, TC_SPOT, "press"),
                     rnd("2021-10-15", "Series A", 20000000, "Redpoint Ventures", True, TC_SPOT, "press")],
             note="TechCrunch (2021-10-15): Spot AI came out of stealth with $22M, a $20M Series A led by Redpoint "
                  "Ventures with Bessemer Venture Partners also participating, and an earlier $2M seed from angels, "
                  "Village Global and Stanford StartX. Entry at the Series A, as the Redpoint row reads."))

L.append(cls("boxed", stage="Seed", stage_src=WV, stage_cite=BOXED_PR, stage_conf="high", entry_date="2013-08",
             rounds=[rnd("2013-08", "Seed", 1100000, None, True, BOXED_PR, "company")],
             note="Boxed's own release of 2013-11-14 says it announced a $1.1M seed round from Social Starts, ENIAC "
                  "Ventures and Bessemer Venture Partners in August 2013, so the entry is the seed, eight years "
                  "before the 2021 listing (no public-purchase question). Graduation left for the graduation pass."))

L.append(cls("vetic",
             rounds=[rnd("2022-11-30", "Seed", 3700000, "Lachy Groom", None, NEWS("vetic", "Lachy Groom leads $3.7 Mn"), "press"),
                     rnd("2025-05", "Series C", 26000000, BVP, True, ENTRACKR_VETIC_C, "press"),
                     rnd("2026-06-18", "$40M round", 40000000, BVP, True, VETIC_POST, "firm")],
             note="Stage still undetermined. Entrackr (2025-05-09): Bessemer led the Rs 224 crore Series C and was "
                  "already the second-largest outside shareholder before it; the firm's own post (2026-06-18) says "
                  "it had invested in multiple rounds before the $40M round it led. The firm's partnered year is "
                  "2024, so the entry was a round before the Series C; Google News searches for a 2024 round naming "
                  "Bessemer found none."))

jl.write("s24c", L)
