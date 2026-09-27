"""PRO-162 A/B pass, part 4: the four $1B+ marks that rested on the unicorn list take their rounds' own citations."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
V = {"valuation_range_source": "web_verified"}
L = [
    jl.cls("ankorstore", rng="1b_plus", usd=1980000000, val_src="web_verified", asof="2022-01",
        val_cite=jl.NEWS("ankorstore", "reaches $2 billion valuation"), extra=V, flags=["stale"]),
    jl.cls("mirakl", rng="1b_plus", usd=3500000000, val_src="web_verified", asof="2021-09",
        val_cite=jl.NEWS("mirakl", "Announces $555 Million Series E"), extra=V, flags=["stale"]),
    jl.cls("pleo", rng="1b_plus", usd=4700000000, val_src="web_verified", asof="2021-12-08",
        val_cite=jl.NEWS("pleo", "raises another $200 mln at $4.7 bln"), extra=V, flags=["stale"]),
    jl.cls("simile", rng="1b_plus", usd=2000000000, val_src="web_verified", asof="2026-07-30",
        val_cite=jl.NEWS("simile", "Synthetic-user startup Simile raises"), extra=V),
]
if __name__ == "__main__":
    jl.write("ab-4", L)
