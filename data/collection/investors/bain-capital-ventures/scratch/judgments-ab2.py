"""PRO-162 A/B pass, part 2: DCG's mark moves from the unicorn list to the cited November 2021 transaction."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
L = [jl.cls("digital-currency-group", rng="10b_plus", usd=10000000000, val_src="web_verified", asof="2021-11-01",
    val_cite="https://www.cnbc.com/2021/11/01/digital-currency-group-sees-10-billion-valuation-as-softbank-google-invest.html",
    extra={"valuation_range_source": "web_verified"}, flags=["stale"])]
if __name__ == "__main__":
    jl.write("ab-2", L)
