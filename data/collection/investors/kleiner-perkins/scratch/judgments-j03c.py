"""PRO-99 Kleiner Perkins, judge j03, follow-up to batch 6 (judgments-j03b.py): the momentum-slice checks for
mirage, maxima, nooks, mine and multiply, which were queued on Google News when batch 6 was recorded, plus the
entry rounds those searches found for mine (Fizz) and multiply."""
import sys
import judge_lib as jl
from judge_lib import cls, rnd, POST

GL = "Graduation left for the graduation pass."
TODAY = "2026-09-30"
TC_MIRAGE = ("https://techcrunch.com/2026/03/24/mirage-raises-75m-to-continue-building-models-for-its-ai-video-editing-"
             "app-captions/")
TC_FIZZ = ("https://techcrunch.com/2024/06/06/kleiner-perkins-leads-14-4m-seed-round-into-fizz-a-credit-building-debit-"
           "card-aimed-at-gen-z-college-students/")
TC_MULTIPLY = ("https://techcrunch.com/2025/03/19/mortgage-as-an-employee-benefit-kleiner-perkins-leads-23-5m-series-a-"
               "for-multiply-mortgage/")
RP_MAXIMA = "https://www.redpoint.com/companies/maxima/"
KP_MAXIMA_A = [p["url"] for p in jl._POSTS
               if p["slug"] == "maxima-bringing-ai-agents-to-the-heart-of-enterprise-accounting"][0]
NOOKS_B = jl.NEWS("nooks", "announces $43M Series B")
MAXIMA_BW = jl.NEWS("maxima", "Seed and Series A to Transform")


def mom(cite):
    return {"valuation_range_source": "web_verified", "valuation_citation": cite, "valuation_asof": TODAY}


L = []

L.append(cls("mirage", status="private", rng="below_1b", country="US", city="New York",
             flags=["model_disputes_source"], stage="Growth", stage_src="model", stage_conf="medium",
             stage_cite=POST("captions-series-b"), entry_date="2023-06-22", focus="AI & Applied AI", extra=mom(TC_MIRAGE),
             rounds=[rnd("2023-06-22", "Series B", None, "Kleiner Perkins", True, POST("captions-series-b"), "firm"),
                     rnd("2026-03-24", "growth financing", 75000000, "General Catalyst Customer Value Fund", None,
                         TC_MIRAGE, "press")],
             note="AI video app Captions, renamed Mirage in September 2025, New York; private, so the public status and "
                  "$26M value came from a different listed company of the same name. The firm's first post on it "
                  "(2023-06-22, 'captions-series-b') marks the Series B, its 2023 entry. Momentum check 2026-09-30 "
                  "(Google News): TechCrunch put the valuation at $500M at the September 2025 rebrand, and the $75M of "
                  "growth financing from General Catalyst's CVF in March 2026 came with no valuation disclosed, so no "
                  "$1B+ round."))

L.append(cls("maxima", status="private", country="US", city="San Mateo", flags=["model_disputes_source"],
             stage="Seed", stage_src="first_party", stage_cite=KP_MAXIMA_A, stage_conf="high", entry_date="2024",
             grad="graduated", grad_src="first_party", grad_cite=KP_MAXIMA_A, grad_conf="high", grad_asof="2025-12-04",
             rng="below_1b", focus="AI & Applied AI", extra=mom(MAXIMA_BW),
             rounds=[rnd("2024", "Seed", None, "Kleiner Perkins", True, KP_MAXIMA_A, "firm"),
                     rnd("2025-11-18", "Seed and Series A (combined announcement)", 41000000, None, True, MAXIMA_BW,
                         "company"),
                     rnd("2025", "Series A", None, "Redpoint Ventures", True, RP_MAXIMA, "firm")],
             note="AI agents for enterprise accounting (maxima.ai), San Mateo per Redpoint's page; still private, so "
                  "the acquired status and the Israeli country from a one-word name match are wrong. The firm's post "
                  "of 2025-12-04 says it led the Seed and joins the Series A; the company announced $41M across both "
                  "on 2025-11-18 (Business Wire). Momentum check 2026-09-30 (Google News): no priced valuation and "
                  "no $1B+ round."))

L.append(cls("nooks", status="private", rng="below_1b", country="US", city="San Francisco",
             stage="Growth", stage_src="first_party", stage_cite=POST("nooks-bringing"), stage_conf="high",
             entry_date="2024-10-23", focus="AI & Applied AI", extra=mom(NOOKS_B),
             rounds=[rnd("2024-04-24", "Series A", 22000000, None, None, None, "press"),
                     rnd("2024-10-24", "Series B", 43000000, "Kleiner Perkins", True, NOOKS_B, "company")],
             note="AI sales dialer, San Francisco. The firm's post of 2024-10-23 says it leads the Series B, its 2024 "
                  "entry, after the $22M Series A of April 2024. Momentum check 2026-09-30 (Google News): the $43M "
                  "Series B (PR Newswire) is the latest round found, no $1B+ round."))

L.append(cls("mine", status="private", rng="below_1b", country="US", city="New York",
             stage="Seed", stage_src="web_verified", stage_cite=TC_FIZZ, stage_conf="high", entry_date="2021",
             focus="Fintech & Payments", extra=mom(TC_FIZZ),
             rounds=[rnd("2021", "Seed (first check, during YC Summer 2021)", None, None, True, TC_FIZZ, "press"),
                     rnd("2024-06-06", "Seed (total announced)", 14400000, "Kleiner Perkins", True, TC_FIZZ, "press")],
             note="Credit-building debit card for college students, New York (Fizz, joinfizz.com; the firm now lists "
                  "it as Mine). TechCrunch (2024-06-06): Kleiner Perkins led the $14.4M seed and first invested when "
                  "the company was in YC's Summer 2021 batch, the firm's 2021 entry. Momentum check 2026-09-30 "
                  "(Google News): no later round and no $1B+ mark. The Battery and Headline 'Mine' rows are MineOS "
                  "of Tel Aviv, a different company. " + GL))

L.append(cls("multiply", status="private", rng="below_1b", country="US", city="Denver",
             stage="Seed", stage_src="model", stage_conf="medium", stage_cite=TC_MULTIPLY, entry_date="2022",
             grad="graduated", grad_src="web_verified", grad_cite=TC_MULTIPLY, grad_conf="high",
             grad_asof="2025-03-19", focus="Fintech & Payments", extra=mom(TC_MULTIPLY),
             rounds=[rnd("2022", "Seed", 3500000, "A*", None, TC_MULTIPLY, "press"),
                     rnd("2025-03-19", "Series A", 23500000, "Kleiner Perkins", True, TC_MULTIPLY, "press")],
             note="Mortgage as an employee benefit (Multiply Mortgage), Denver. The firm's since-year is 2022, when "
                  "A* led the company's $3.5M seed, and Kleiner Perkins led the $23.5M Series A of March 2025 "
                  "(TechCrunch), which graduates the seed. Momentum check 2026-09-30 (Google News): the Series A "
                  "price was not disclosed and no $1B+ round was found. The Lux and YC 'Multiply' rows are Multiply "
                  "Labs, a robotics company."))

jl.write("j03c", L)
