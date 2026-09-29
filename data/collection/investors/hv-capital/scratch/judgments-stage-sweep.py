"""Duty 9 class sweep (PRO-104): entry rounds the grind left undetermined, found by the stage sweep agents.
Parts 1 and 2; part 3 is appended when it lands."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, rnd, write, gn, surfaces_lines, ASOF  # noqa: E402

WA = "https://web.archive.org/web/"


def seed(slug, cite, date, conf="high", src="web_verified", **kw):
    return dict(stage="Seed", stage_src=src, stage_conf=conf, stage_cite=cite, entry_date=date, **kw)


def grad(cite, src="web_verified"):
    return dict(grad="graduated", grad_src=src, grad_cite=cite)


def no(slug, finding):
    return dict(grad="not_graduated", grad_src="absence_check", grad_asof=ASOF,
                surfaces=surfaces_lines(slug, finding))


L = []
A = lambda slug, **kw: L.append(cls(slug, **kw))  # noqa: E731

# ---- part 1 --------------------------------------------------------------------------------
ACTIO = WA + "20211026222725/https://www.eu-startups.com/2020/12/berlin-based-actio-lands-e8-5-million-to-help-users-pick-up-new-habits/"
A("actio", **seed("actio", ACTIO, "2020-12"), **no("actio", "the Dec 2020 EUR 8.5M seed only; insolvency filed Apr 2023 (a cited end)"),
  note="Habit-building app, Berlin. 'A seed funding round of EUR 8.5 million in the first close ... led by HV Capital and Cavalry "
       "Ventures' (EU-Startups, 2020-12-17). No later round; insolvency filed in Apr 2023 with no buyer reported.",
  rounds=[rnd("2020-12-17", "Seed", 10_400_000, "HV Capital, Cavalry Ventures", True, ACTIO)])
AIT = WA + "20241015163715/https://www.businessinsider.de/gruenderszene/food/series-a-aitme/"
A("aitme", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=AIT, entry_date="2021-06",
  rounds=[rnd("2021-06-15", "Series A", 9_100_000, None, True, AIT)])
CERT = "https://www.startupticker.ch/en/news/e-signing-solutions-provider-raises-5m-seed-capital"
A("certifaction", **seed("certifaction", CERT, "2022-02"),
  **no("certifaction", "the Feb 2022 EUR 5M seed led by Expa only; no later round"),
  rounds=[rnd("2022-02-21", "Seed", 5_700_000, "Expa", True, CERT)])
A("dealflo", stage="Growth", stage_src="web_verified", stage_conf="high",
  stage_cite="https://tech.eu/2017/02/27/dealflo-raises-investment/", entry_date="2017-02",
  rounds=[rnd("2017-02-27", "Series B", 12_400_000, "Holtzbrinck Ventures, Frog Capital", True,
              "https://tech.eu/2017/02/27/dealflo-raises-investment/")])
DELLI = WA + "20230205201029/https://www.eu-startups.com/2021/12/london-based-foodie-marketplace-delli-is-served-up-e2-9-million-to-launch/"
A("delli", **seed("delli", DELLI, "2021-12"), **grad("https://www.uktech.news/foodtech/delli-lands-6m-20220906"),
  note="Food marketplace from Depop's founder Simon Beckerman, London. HV's entry is the EUR 2.9M seed of Dec 2021 "
       "(EU-Startups); the GBP 6.2M round of Sept 2022 (UKTN), unnamed, graduates it under the step-up test: GBP 6.2M @ ECB "
       "2022-09-06 = $7.2M against max(2x the $3.3M seed, $5M).",
  rounds=[rnd("2021-12-17", "Seed", 3_300_000, None, True, DELLI),
          rnd("2022-09-06", None, 7_200_000, None, None, "https://www.uktech.news/foodtech/delli-lands-6m-20220906")])
DIA = WA + "20201202132642/https://www.finsmes.com/2018/02/dialogue-raises-12m-in-series-a-funding.html"
A("dialogue", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=DIA, entry_date="2018-02",
  rounds=[rnd("2018-02-23", "Series A", 12_000_000, "White Star Capital", True, DIA)])
ECO = "https://www.munich-startup.de/en/news/ecoplanet-secures-e2-6-million-in-seed-round"
A("ecoplanet", **seed("ecoplanet", ECO, "2023-04"),
  **grad("https://tech.eu/2025/01/20/ecoplanet-secures-16m-series-a-led-by-eqt-ventures/"),
  rounds=[rnd("2023-04-27", "Seed", 2_900_000, "HV Capital", True, ECO),
          rnd("2025-01-20", "Series A", None, "EQT Ventures", None,
              "https://tech.eu/2025/01/20/ecoplanet-secures-16m-series-a-led-by-eqt-ventures/")])
FELD = WA + "20250115001956/https://www.eu-startups.com/2024/11/munich-based-feld-energy-raises-e1-7-million-to-drive-agricultural-photovoltaics-in-germany/"
A("feld-energy", stage="Pre-Seed", stage_src="web_verified", stage_conf="high", stage_cite=FELD, entry_date="2024-11",
  rounds=[rnd("2024-11-13", "Pre-Seed", 1_800_000, "HV Capital", True, FELD),
          rnd("2025-09-15", "Seed", None, None, None,
              "https://tech.eu/2025/09/15/feldenergy-raises-eur10m-seed-to-accelerate-agrivoltaics-in-germany/")])
FELMO = WA + "20250430210257/https://www.businessinsider.de/gruenderszene/news/weitere-millionen-fuer-tierarzt-plattform-felmo/"
A("felmo", **seed("felmo", FELMO, "2020-07"), **grad("https://tech.eu/2021/01/14/felmo-series-a/"),
  note="Mobile vets, Berlin. 'HV Capital und 468 Capital, die bereits in der früheren Seed-Runde investierten' (Gruenderszene, "
       "2021-01-14); the seed dates to July 2020 (deutsche-startups dealmonitor). The Series A of Jan 2021 (tech.eu) "
       "graduates the row; a EUR 15M Series B followed in Aug 2021.")
FLANK = "https://tech.eu/2019/06/19/berlin-based-legal-tech-startup-legal-os-secures-2-2-million-in-seed-funding/"
INS = "https://www.insightpartners.com/ideas/flank-raises-10m-to-scale-autonomous-legal-agents-embedded-invisible-and-built-for-the-enterprise/"
A("flank", **seed("flank", FLANK, "2019-06"), **grad(INS),
  note="Legal automation (Legal OS, renamed Flank), Berlin. HV Holtzbrinck Ventures led the $2.2M seed of June 2019 (tech.eu); "
       "the $10M round of June 2025 (Insight Partners' post), unnamed, graduates it under the step-up test ($10M against "
       "max(2x $2.2M, $5M)).",
  rounds=[rnd("2019-06-19", "Seed", 2_200_000, "HV Holtzbrinck Ventures", True, FLANK),
          rnd("2025-06-05", None, 10_000_000, "Insight Partners", None, INS)])
A("funanga", status="acquired", rng="below_1b",
  extra={"status_citation": "https://www.deutsche-startups.de/2024/08/15/dealmonitor-flix-songpush/"},
  note="Cash-to-code payments (CashtoCode), Berlin. SGT German Private Equity took the majority of Funanga in Aug 2024 "
       "(deutsche-startups); Funanga AG still operates and files.")

# ---- part 2 --------------------------------------------------------------------------------
GF = "https://www.businessinsider.de/gruenderszene/business/green-fusion-macht-heizkessel-digital-und-bekommt-dafuer-12-millionen-euro-mit-diesem-pitchdeck/"
A("green-fusion", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=GF, entry_date="2025-01",
  rounds=[rnd("2025-01-21", "Series A", 12_400_000, "HV Capital, XAnge", True, GF)])
HAD = "https://www.canadianminingjournal.com/news/founders-factory-and-rio-tinto-back-six-new-mining-tech-startups/"
A("hades", **seed("hades", HAD, "2026", conf="medium"), grad="censored",
  note="Laser drilling for mining, Munich. 'Hades Mining's EUR 15 million Seed round co-led by HV Capital and Headline' "
       "(Canadian Mining Journal, 2026-03-31; tech.eu puts it in Q1 2026); HV was not in the Aug 2025 pre-seed. Inside the "
       "24-month window.",
  rounds=[rnd("2026", "Seed", 17_200_000, "HV Capital, Headline", True, HAD)])
I2X = gn("i2x", "Y5Mkx0QzBn")
A("i2x", **seed("i2x", "https://medium.com/feed/hv-holtzbrinck-ventures", "2017-02", conf="medium", src="first_party"),
  **grad(I2X),
  note="AI sales-call coaching, Berlin (Michael Brehm). The firm's own post announcing its seed programme (HV blog, "
       "2018-06-04) names i2x among its seed investments, funded 'just on the basis of a vision'; the firm dates the entry "
       "2017-02. The EUR 11M round of July 2022 (Startbase), unnamed, graduates the row under the step-up test: EUR 11.0M @ "
       "ECB 2022-07-18 = $11.1M, above the $8M bar for a 2015-18 seed of unknown size. acq. by SSF Technologies, Feb 2023.",
  rounds=[rnd("2017-02", "Seed", None, None, True, "https://medium.com/feed/hv-holtzbrinck-ventures", "firm"),
          rnd("2022-07-18", None, 11_100_000, None, True, I2X)])
INK = "https://techcrunch.com/2019/08/28/inkitt-raises-16m-led-by-kleiner-perkins-to-publish-crowdsourced-novels-in-mini-episodes/"
A("inkitt", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=INK, entry_date="2019-08",
  rounds=[rnd("2017", "Seed", 3_900_000, None, False, "https://techcrunch.com/2024/02/26/inkitt-ai-publishing-37-million/"),
          rnd("2019-08-28", "Series A", 16_000_000, "Kleiner Perkins", True, INK),
          rnd("2021-10-05", "Series B", 59_000_000, None, None,
              "https://www.techtimes.com/articles/266208/20211005/inkitt-raises-59m-for-series-b-funding-focusing-on-delivering-a-data-driven-content-house-pr.htm"),
          rnd("2024-02-26", "Series C", 37_000_000, None, None, "https://techcrunch.com/2024/02/26/inkitt-ai-publishing-37-million/")])
IC = "https://siliconcanals.com/instant-commerce-bags-5-4m/"
A("instant-commerce", **seed("instant-commerce", IC, "2022-09"),
  **no("instant-commerce", "the Sept 2022 EUR 5.4M seed led by HV only; no later round"),
  rounds=[rnd("2022-09-22", "Seed", 5_300_000, "HV Capital", True, IC)])
KY = "https://techcrunch.com/2007/12/19/kyte-takes-15-million-series-b/"
A("kyte", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=KY, entry_date="2007-05",
  note="Kyte (kyte.com), the 2006 mobile and live video platform, San Francisco. After a $2.25M first round in July 2006 "
       "(before HV), Swisscom and Holtzbrinck Ventures were announced in May 2007 in the strategic round that closed as the "
       "$15M Series B (TechCrunch, 2007-12-19, names Holtzbrinck). acq. by KIT digital, Jan 2011 (~$5.7M; KIT digital's 8-K "
       "exhibit). The old site's 'decentral.tv / kyte' row is this company. Not the 2021 car-rental startup Kyte.",
  rounds=[rnd("2007-12-19", "Series B", 15_000_000, None, True, KY)])
LK = "https://techcrunch.com/2017/06/20/lingokids/"
A("lingokids", **seed("lingokids", LK, "2017-06", conf="medium"),
  **grad("https://techcrunch.com/2018/10/02/lingokids-scores-6m-series-a-for-its-english-language-learning-platform/"),
  note="English learning for children, Madrid. Holtzbrinck Ventures co-led the $4M round of June 2017 that TechCrunch calls "
       "'seed or post-seed'; HV then led the $6M Series A of Oct 2018 (TechCrunch), which graduates the row.",
  rounds=[rnd("2017-06-20", "Seed", 4_000_000, "Holtzbrinck Ventures, JME", True, LK),
          rnd("2018-10-02", "Series A", 6_000_000, "HV Holtzbrinck Ventures", True,
              "https://techcrunch.com/2018/10/02/lingokids-scores-6m-series-a-for-its-english-language-learning-platform/")])
MID = "https://www.bitget.com/news/detail/12560603947415"
A("midas", **seed("midas", MID, "2024-03", conf="medium"),
  **grad("https://tech.eu/2026/03/30/midas-closes-50m-series-a-to-scale-onchain-investment-products/"),
  rounds=[rnd("2024-03-28", "Seed", 8_750_000, "BlockTower, Framework, HV Capital", True, MID),
          rnd("2026-03-30", "Series A", 50_000_000, "RRE Ventures, Creandum", True,
              "https://tech.eu/2026/03/30/midas-closes-50m-series-a-to-scale-onchain-investment-products/")])
PACT = "https://techfundingnews.com/cambridge-pact-16m-collagen-leather-scale/"
A("pact", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=PACT, entry_date="2025-10",
  rounds=[rnd("2025-10-31", "Series A", 21_000_000, "Forbion, HV Capital", True, PACT)])

write("stage-sweep-001", L)

# ---- part 3 (appended 2026-09-29) -----------------------------------------------------------
L.clear()
PAY = ("https://techcrunch.com/2013/02/14/as-payment-pioneer-stripe-gears-up-for-european-rollout-rocket-rival-paymill-"
       "reveals-another-5m-in-funding-from-blumberg-capital/")
A("paymill", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=PAY, entry_date="2013-01",
  rounds=[rnd("2013-01", "Series A", 13_000_000, None, True, PAY)])
PLA = "https://carbonherald.com/plan-a-secures-10m-investment-for-its-carbon-accounting-software/"
A("plan-a", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=PLA, entry_date="2021-11",
  rounds=[rnd("2021-11-03", "Series A", 10_000_000, "HV Capital, Keen Venture Partners", True, PLA),
          rnd("2023-09-19", "Series A", 27_000_000, None, None, "https://techcrunch.com/2023/09/19/plan-a-carbon-accounting/")])
PX = "https://tech.eu/2025/10/02/praxipal-lands-67m-to-build-the-ai-workforce-for-healthcare-front-desks/"
A("praxipal", **seed("praxipal", PX, "2025-10"), grad="censored",
  rounds=[rnd("2025-10-02", "Seed", 6_700_000, "HV Capital", True, PX)])
QZ = "https://cms.law/en/deu/news-information/cms-advises-digital-start-up-qualifyze-on-eur-12-million-series-a-round-of-financing"
A("qualifyze", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=QZ, entry_date="2021-11",
  rounds=[rnd("2021-11-03", "Series A", None, "HV Capital", True, QZ),
          rnd("2024-09-10", "Series B", 54_000_000, None, None,
              "https://www.prnewswire.com/news-releases/qualifyze-raises-54m-to-boost-supplier-risk-management-in-life-sciences-302241232.html")])
RV = "https://techfundingnews.com/zopa-acquires-rvvup-embedded-finance/"
A("rvvup", **seed("rvvup", RV, "2021-04", conf="medium"),
  **no("rvvup", "the GBP 5.6M seed with Lakestar only; acquired by Zopa in 2025 (a cited end)"),
  note="Payments and retail finance at checkout, London (founded 2020-21). 'Backed by HV Capital and Lakestar with GBP 5.6 "
       "million in seed funding' (Tech Funding News, 2025); the firm dates its entry 2021-04 (Fund VIII). No later round. acq. "
       "by Zopa, 2025 (share consideration; Financial IT, 2025-09-02); HV's resulting Zopa stake is not a member (D4).")
SAS = "https://techcrunch.com/2021/08/27/sastrify-snags-7m-to-help-smes-manage-saas-buying/"
A("sastrify", **seed("sastrify", SAS, "2021-08"),
  **grad("https://tech.eu/2023/05/26/saas-tool-procurement-platform-sastrify-raises-32-million/"),
  rounds=[rnd("2021-08-27", "Seed", 7_000_000, "HV Capital", True, SAS),
          rnd("2023-05-26", "Series B", 32_000_000, None, None,
              "https://tech.eu/2023/05/26/saas-tool-procurement-platform-sastrify-raises-32-million/")])
SB = "https://www.deutsche-startups.de/2018/11/05/dealmonitor-05-10-2018-2/"
A("scoutbee", **seed("scoutbee", SB, "2018-11"), **grad("https://www.deutsche-startups.de/2019/06/11/dealmonitor-11-06-2019/"),
  rounds=[rnd("2018-11-05", "Seed", 4_000_000, "Holtzbrinck Ventures, 42CAP", True, SB),
          rnd("2019-06-11", "Series A", 12_000_000, None, None, "https://www.deutsche-startups.de/2019/06/11/dealmonitor-11-06-2019/"),
          rnd("2020-01-23", "Series B", 60_000_000, None, None,
              "https://technical.ly/startups/arlington-scoutbee-60-million-series-b-funding-hiring-tech-jobs/")])
SD = "https://www.vc-magazin.de/blog/2023/02/01/sdui-edtech-start-up-erhaelt-25-mio-eur-in-series-a/"
A("sdui", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=SD, entry_date="2021-03",
  rounds=[rnd("2021-03", "Series A", None, None, True, SD),
          rnd("2023-02-01", "Series A", None, None, True, "https://www.deutsche-startups.de/2023/02/01/dealmonitor-sdui-iwoca/")])
SW = "https://techcrunch.com/2008/02/11/seatwave-wins-25m-series-c-funding-to-expand/"
A("seatwave", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=SW, entry_date="2008-02",
  rounds=[rnd("2008-02-11", "Series C", 25_000_000, "Fidelity Ventures", True, SW)])
SP = "https://tech.eu/2023/05/03/engineering-intelligence-platform-spread-butters-up-to-16-million/"
A("spread", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=SP, entry_date="2023-05")
TL = "https://www.deutsche-startups.de/2018/03/22/travel-startup-tourlane-bekommt-7-millionen/"
A("tourlane", **seed("tourlane", TL, "2016"), **grad(TL),
  note="Tailor-made travel, Berlin (founded 2016). HV's partner Christian Saller: 'bereits in der Seed-Runde investiert und "
       "unsere Beteiligung in dieser Series A ausgebaut' (deutsche-startups, 2018-03-22); the EUR 7M Series A of March 2018 "
       "graduates the row. Series B (Dec 2018) and the $47M Series C led by Sequoia and Spark (May 2019) followed.",
  rounds=[rnd("2016", "Seed", None, None, True, TL), rnd("2018-03-22", "Series A", None, None, True, TL),
          rnd("2019-05-07", "Series C", 47_000_000, "Sequoia, Spark Capital", None,
              "https://techcrunch.com/2019/05/07/tourlane-raises-a-47m-c-round-led-by-sequoia-and-spark-capital/")])
UA = "https://techcrunch.com/2018/09/18/ultimate-ai-nabs-1-3m-for-a-customer-service-ai-focused-on-non-english-markets/"
A("ultimate-ai", **seed("ultimate-ai", UA, "2018-09"),
  **grad("https://techcrunch.com/2020/12/03/ultimate-ai-scores-20m-for-a-supportive-approach-to-customer-service-automation/"),
  rounds=[rnd("2018-09-18", "Seed", 1_300_000, "Holtzbrinck Ventures, Maki.vc", True, UA),
          rnd("2020-12-03", "Series A", 20_000_000, None, None,
              "https://techcrunch.com/2020/12/03/ultimate-ai-scores-20m-for-a-supportive-approach-to-customer-service-automation/")])
VA = "https://tech.eu/2023/10/23/visionai-raises-eur5m-to-help-e-commerce-merchants-take-on-amazon/"
A("visionai", **seed("visionai", VA, "2023-10"), **no("visionai", "the Oct 2023 EUR 5M seed led by HV only; no later round"),
  note="AI search and recommendations for e-commerce, Bielefeld. HV led the EUR 5M seed of Oct 2023 (tech.eu). No later round "
       "on any surface; the entry is past the 24-month window.")
WH = "https://warehousing1.com/blog/en/weiteres-millionen-investment-fuer-warehousing1/"
A("warehousing1", **seed("warehousing1", WH, "2018-09", conf="medium"),
  **grad("https://warehousing1.com/blog/en/warehousing1-series-a-finanzierung/", src="first_party"),
  note="E-commerce warehousing network, Berlin (founded 2018). The company's own post of Aug 2019: 'strong growth since the Seed "
       "Round in September last year. The existing investors HV Holtzbrinck Ventures and Base10 Partners ... are now "
       "substantially increasing' their stake, so HV entered at the Sept 2018 seed (the firm's own list dates the Aug 2019 "
       "follow-on). The EUR 10M Series A of April 2022 (the company's post) graduates the row.")
WI = "https://techcrunch.com/2018/11/21/wind-mobility/"
A("wind", **seed("wind", WI, "2018-11"), **grad("https://techcrunch.com/2019/07/08/wind-mobility-new-hardware/"),
  note="Shared e-scooters, Berlin (founded 2018). HV Holtzbrinck Ventures joined the $22M round of Nov 2018 that TechCrunch "
       "calls seed funding; the $50M Series A of July 2019 (TechCrunch) graduates the row. WIND Mobility GmbH entered "
       "liquidation in Jan 2025 (North Data).",
  rounds=[rnd("2018-11-21", "Seed", 22_000_000, "Source Code Capital", True, WI),
          rnd("2019-07-08", "Series A", 50_000_000, None, None, "https://techcrunch.com/2019/07/08/wind-mobility-new-hardware/")])
YA = "https://techcrunch.com/2019/05/30/yapily/"
A("yapily", **seed("yapily", YA, "2019-05"), **grad("https://techcrunch.com/2020/04/05/open-banking-fintech-yapily-raises-13m-series-a/"),
  rounds=[rnd("2019-05-30", "Seed", 5_400_000, "HV Holtzbrinck Ventures, LocalGlobe", True, YA),
          rnd("2020-04-05", "Series A", 13_000_000, None, None, "https://techcrunch.com/2020/04/05/open-banking-fintech-yapily-raises-13m-series-a/"),
          rnd("2021-07-21", "Series B", 51_000_000, None, None, "https://techcrunch.com/2021/07/21/yapily-raises-51-million-for-its-open-banking-api/")])
ZG = "https://tech.eu/brief/zeitgold-funding/"
A("zeitgold", **seed("zeitgold", ZG, "2017-02"), **grad(ZG),
  note="AI bookkeeping for small businesses, Berlin (founded 2015). 'This Series A round follows its EUR 4.2 million seed round "
       "in February, also from Battery and Holtzbrinck' (tech.eu, 2017-09); the EUR 10M Series A graduates the row. A $29.2M "
       "Series B followed in May 2020. acq. by Deel, 2021 (Business Wire, 2021-08-04); HV's resulting Deel stake is not a "
       "member (D4).")
ZC = "https://techcrunch.com/2019/04/16/logistics-startup-zencargo-raises-20m-to-take-on-the-antiquated-business-of-freight-forwarding/"
A("zencargo", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=ZC, entry_date="2019-04",
  rounds=[rnd("2019-04-16", "Series A", None, "HV Holtzbrinck Ventures", True, ZC)])
# record fixes found by the sweep
A("payleven", entry_date="2012-06",
  note="Mobile card payments (a Rocket Internet company), Berlin (founded 2012). HV came in with NEA and ru-Net in the "
       "double-digit-million-euro round of June 2012 (TechCrunch, 2012-06-22), not named as a series, and was in the Jan 2013 "
       "funding too (Mobile World Live). Merged into SumUp in April 2016 (Finovate, 2016-04-28): SumUp continued and payleven's "
       "shareholders took SumUp shares, which is sale consideration (D4); payleven is the member.",
  rounds=[rnd("2012-06-22", None, None, "NEA", True, None, "press"),
          rnd("2013-01-22", None, None, None, True,
              "https://www.mobileworldlive.com/old_latest-stories/payleven-secures-new-funding-for-mobile-payment-tech/")])
A("plusdental", extra={"status_citation": "https://www.dental-tribune.com/c/straumann/news/straumann-group-to-acquire-berlin-clear-aligner-manufacturer-plusdental/"},
  note="Clear-aligner orthodontics (SunshineSmile until Oct 2019), Berlin (founded 2017). HV backed it from launch (HV entry "
       "2017, Fund VI), with no round word on record; EUR 32M in May 2020 (Ping An Global Voyager with HV and Lakestar) and "
       "EUR 35M in March 2021, neither named as a series. acq. by Straumann Group, announced 2022-05-23 (~CHF 135M; Dental "
       "Tribune).")
A("talentrun", note="TalentRun, an online karaoke community, Berlin (launched late 2007). HV and Neuhaus Partners invested in "
                    "June 2008, no round word. Merged into Mikestar in Nov 2010 (all shareholders kept stakes); the karaoke "
                    "service stopped in Nov 2011 and Mikestar GmbH went into insolvency (deleted 2014-08).")
A("platinnetz", note="Community for people over 50 (founded 2007, first in Oberhaching near Munich). HV entered 2007-08 with the "
                     "European Founders Fund, no round word. The Holtzbrinck group took control through Holtzbrinck Ventures in "
                     "Jan 2009 and moved it to Cologne (deutsche-startups, 2009-01-26). acq. by Feierabend.de, 2013-01; merged "
                     "into Feierabend Online Dienste fuer Senioren GmbH in 2019.")
write("stage-sweep-002", L)
