"""PRO-161 A/B pass, part 2: Figure and Policy Bazaar crossed $1B on their 2026-09-28 caps, so their Growth / Series A
entries need class-1 evidence (verify rule 4). Both readings stand; the citations are the ones their notes already name."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls = jl.cls
FIG = "https://fintech.global/2018/05/02/figure-said-to-raise-50m-led-by-dst-ribbit/"
PB = "https://www.medianama.com/2015/04/223-policybazaar-raises-40m-from-premjiinvest-focus-on-paisabazaar/"
L = [cls("figure", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=FIG, entry_date="2018-05"),
     cls("policy-bazaar", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=PB)]
jl.write("ab-2", L)
