"""PRO-75 grind, pilot (and the template for the parallel judges): one fully researched row.
Ahana: GV led the $2.25M seed (GlobeNewswire, 2020-06-02); Third Point Ventures led the $20M Series A with GV
following on (GlobeNewswire, 2021-08-03); IBM acquired it (the firm's own exit line, 'Acquired by IBM, 2023')."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, verdict, rnd, POST, SITE, ARCH, W, NEWS, FTS = (jl.cls, jl.verdict, jl.rnd, jl.POST, jl.SITE, jl.ARCH, jl.W,
                                                      jl.NEWS, jl.FTS)
L = []

SEED = "https://www.globenewswire.com/news-release/2020/06/02/2042090/0/en/Ahana-Raises-2-25-Million-Seed-Funding-Led-by-GV-and-Joins-Linux-Foundation-s-Presto-Foundation.html"
SERIES_A = "https://www.globenewswire.com/news-release/2021/08/03/2273643/0/en/Presto-Company-Ahana-Raises-20M-Series-A-Led-By-Third-Point-Ventures-To-Redefine-Open-Data-Lake-Analytics.html"
L.append(cls("ahana", status="acquired", rng="below_1b", country="US", country_src="model_knowledge",
             city="San Mateo", focus="Data Infrastructure",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=SEED, entry_date="2020-06",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=SERIES_A,
             note="Managed PrestoDB for cloud data lakes (San Mateo). GV led the $2.25M seed in June 2020 (Ahana's release); "
                  "Lux Capital led a $2.3M seed extension in September 2020 with GV following; Third Point Ventures led the "
                  "$20M Series A in August 2021. Acquired by IBM in April 2023 (the firm's own exit line).",
             rounds=[rnd("2020-06-02", "Seed", 2250000, "GV", True, SEED, "company"),
                     rnd("2021-08-03", "Series A", 20000000, "Third Point Ventures", True, SERIES_A, "company")]))

jl.write("pilot", L)
