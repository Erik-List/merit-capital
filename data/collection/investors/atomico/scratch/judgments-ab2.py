"""PRO-79 A/B pass, part 2: MasterClass, whose value rested on the unicorn-list
pre-fill (Rule A: a floor, never a mark) and was missed by the first slice
listing, which read only the grind's own lines."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
CNBC = "https://www.cnbc.com/2021/05/13/masterclass-more-than-triples-valuation-in-one-year.html"
L = [jl.cls("masterclass", status="private", rng="1b_plus", usd=2750000000, val_src="web_verified", asof="2021-05-13",
            val_cite=CNBC, val_conf="high", flags=["stale"], clear=["unicorn_name_match"],
            note="A/B: the $225M Series F of May 2021 at a $2.75B valuation (CNBC: 'MasterClass more than triples valuation in one year') is the last priced mark; the unicorn-list pre-fill it replaces is a floor, never a mark (Rule A); no later priced round found",
            rounds=[jl.rnd("2021-05-13", "Series F", 225000000, None, None, CNBC)])]

if __name__ == "__main__":
    jl.write("ab-002", L)
