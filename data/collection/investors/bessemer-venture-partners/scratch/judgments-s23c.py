"""PRO-80 Bessemer, second pass s23, file c: rilla, vega-health, and three rows settled from SEC filings found
after files a and b were recorded (wavesmith-networks upgraded to a filing citation, cecure-gaming,
advanced-recognition-technologies). Run as NQ_TAG=s23 python3 judgments-s23c.py."""
import judge_lib as jl
from judge_lib import NEWS, cls, rnd

BVP = "Bessemer Venture Partners"

L = []

SACRA = "https://sacra.com/c/rilla"
L.append(cls("rilla",
             rounds=[rnd("2022-12", "Series A", 3700000, "Crew Capital", None, SACRA, "vendor"),
                     rnd("2023-12", "Series A1", None, None, None, SACRA, "vendor"),
                     rnd("2025-06", "Series B", None, "GV", True, SACRA, "vendor")],
             note="A vendor profile lists a $3.7M Series A led by Crew Capital (December 2022), an undisclosed Series A1 (December 2023) and the GV-led Series B of June 2025 with Bessemer taking part. The firm's 2023 year points at the Series A1, but no firm, company or press page names Bessemer in it (web search and two news queries, 2026-10-06), so the stage stays undetermined."))

PU = NEWS("vega-health", "$4 Million Seed")
AX = NEWS("vega-health", "Axios")
L.append(cls("vega-health", stage="Seed", stage_src="web_verified", stage_cite=PU, stage_conf="high", entry_date="2025-10",
             grad="censored", city="Durham", city_src="web_verified",
             rounds=[rnd("2025-10-16", "Seed", 4000000, BVP, True, PU, "press")],
             note="Pulse 2.0 (2025-10-23): Vega Health 'announced its official launch with $4 million in seed funding from Bessemer Venture Partners' (launch of 2025-10-16). The entry is inside the 24 month window, so censored. Axios calls it 'a new Durham startup' (" + AX + "), North Carolina."))

S4 = "https://www.sec.gov/Archives/edgar/data/936395/000095013303001530/w85521sv4.htm"
L.append(cls("wavesmith-networks", stage="Series A", stage_src="web_verified", stage_cite=S4, stage_conf="high",
             entry_date="2000-04-13",
             rounds=[rnd("2000-04-13", "Series A (series A-1 preferred)", None, None, True, S4, "filing")],
             note="Ciena's 2003 merger registration statement lists the entities affiliated with Bessemer as holders of 14,066,678 shares of WaveSmith's series A-1 preferred (43.86% of that series), plus series B-1 and series C, and calls Bessemer 'one of WaveSmith's lead investors'. "
                  "That confirms the firm's own sentence ('BVP invested in every round'): the entry was the Series A, dated by the firm 2000-04-13."))

ANTE = "https://www.sec.gov/Archives/edgar/data/1490161/000104746910005866/a2199105zex-99_1.htm"
WPT = "https://www.sec.gov/Archives/edgar/data/1283843/000110465909015104/a09-1606_110k.htm"
WPT07 = "https://www.sec.gov/Archives/edgar/data/1283843/000110465907019390/a07-7654_110k.htm"
L.append(cls("cecure-gaming", status="defunct", entry_date="2006-07-31",
             country="GB", country_src="web_verified", country_cite=ANTE, clear=("country_unknown",),
             rounds=[rnd("2006-07-31", "unnamed round with WPT Enterprises", None, None, True, WPT07, "filing")],
             note="WPT Enterprises' annual reports: a Subscription and Shareholders' Agreement of 2006-07-31 between WPT, Cecure Gaming (f/k/a 3G Scene Limited) and Bessemer Venture Partners VI, in which WPT paid $2.9M for 10%; in 2008 Cecure could not raise working capital and cut most of its staff (" + WPT + "). "
                  "Its successor's 2010 information statement says the business 'is currently in receivership in the British equivalent of a bankruptcy proceeding', so defunct, United Kingdom. The filings do not name the 2006 round, and the city was not found."))

ART = "https://www.sec.gov/Archives/edgar/data/1002517/000095013505001961/b54513ssexv99w1.htm"
L.append(cls("advanced-recognition-technologies", stage="Growth", stage_src="web_verified", stage_cite=ART,
             stage_conf="medium", entry_date="2004-01-06",
             rounds=[rnd("2003-09", "Series C", 1856000, None, None, ART, "filing"),
                     rnd("2004-01", "Series D", 4333000, None, True, ART, "filing")],
             note="ART's audited statements, filed by ScanSoft after the purchase: 'In January 2004, the Company issued to certain investors 5,935,153 New Series D Preferred stock ... for a total gross consideration of $4,333' thousand, after Series A, B and C. "
                  "The firm's own investment date is 2004-01-06, so the entry was the Series D (Growth); the statements do not name the investors. The city in Israel was not found."))

jl.write("s23c", L)
