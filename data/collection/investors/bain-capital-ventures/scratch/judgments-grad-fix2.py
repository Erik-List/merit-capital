"""PRO-162 graduation pass follow-ups (list B judge): Noteable's and Tracelytics' entries were Series A rounds, not seeds, so their
S2A column does not apply (Tracelytics' recorded not_graduated is withdrawn with the stage)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
NP = jl.POST("noteables-pierre-brunelle")
TC_SEED = "https://techcrunch.com/2011/11/03/web-app-performance-solution-tracelytics-raises-600k-from-google-ventures-battery-flybridge/"
L = [
    jl.cls("noteable", stage="Series A", stage_src="first_party", stage_conf="high", stage_cite=NP, entry_date="2021-11",
        flags=["stage_disputes_band"],
        note="'BCV announced its first investment in the company in November 2021, leading Noteable's $21 million Series A round' "
             "(the firm's post, 2022-01-12). The June 2020 Form D the band read is Wing's seed, filed while Aaref Hilaly sat on the "
             "board before he joined BCV in August 2020."),
    jl.cls("tracelytics", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2012-03-08",
        flags=["stage_disputes_band"],
        extra={"seed_to_a_graduation": None, "graduation_source": None, "graduation_asof": None,
               "graduation_surfaces": None, "graduation_citation": None, "graduation_confidence": None},
        note="BCV's $5.2M round of March 2012 (Ben Holzman, the Form D) followed the company's $600K seed from Google Ventures, "
             "Battery and Flybridge ('Tracelytics Raises $600K', TechCrunch, 2011-11-03, " + TC_SEED + "): the first institutional round "
             "after a seed, read as its Series A, so the S2A column does not apply."),
]
if __name__ == "__main__":
    jl.write("grad-fix-2", L)
