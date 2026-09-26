"""PRO-79: correction to batch-003b's the-climate-corporation stage."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)

L = [jl.cls("the-climate-corporation", stage="undetermined",
            extra={"entry_stage_source": None, "entry_stage_confidence": None},
            note="CORRECTED 2026-09-26: the Oct 2007 TechCrunch article names no round letter (only its URL slug says 'series-b'), so the Jan 2007 entry is the company's first outside round with no name on any surface -> undetermined, not a Series A by sequence; the Form D band's Growth stays overridden",
            rounds=[jl.rnd("2007-01-15", "first outside round (unnamed)", None, None, True, "https://techcrunch.com/2007/01/15/weatherbill-launches-announces-all-star-investors/"),
                    jl.rnd("2007-10-17", "unnamed", 12500000, "NEA; Index Ventures", True, "https://techcrunch.com/2007/10/17/an-interesting-bet-weatherbill-takes-125-million-series-b/")])]

if __name__ == "__main__":
    jl.write("fix-003", L)
