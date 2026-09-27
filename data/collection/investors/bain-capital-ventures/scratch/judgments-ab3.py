"""PRO-162 A/B pass, part 3: Etched's $21B mark moves from the unicorn list to the round's own release."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
L = [jl.cls("etched", rng="10b_plus", usd=21000000000, val_src="web_verified", asof="2026-08-18",
    val_cite=jl.NEWS("etched", "Etched Raises $700M at a $21B Valuation"), extra={"valuation_range_source": "web_verified"})]
if __name__ == "__main__":
    jl.write("ab-3", L)
