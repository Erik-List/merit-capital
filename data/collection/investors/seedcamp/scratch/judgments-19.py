"""PRO-83 rule 6: a non-US country on a $1B+ row carries a citation (Pleo, Sorare, Grover)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
c, loc = jl.c, jl.loc
L = [
    c("pleo", **loc("DK", "Copenhagen", "https://www.reuters.com/markets/europe/danish-fintech-firm-pleo-raises-another-200-mln-47-bln-valuation-2021-12-09/")),
    c("sorare", **loc("FR", "Paris", "https://www.prnewswire.com/news-releases/sorare-raises-680m-series-b-to-create-the-next-sports-entertainment-giant-leveraging-nfts-301380764.html")),
    c("grover", **loc("DE", "Berlin", "https://tech.eu/2022/04/07/berlins-grover-hits-super-grover-status-with-unicorn-valuation-but/")),
]
if __name__ == "__main__":
    jl.write("fixups-04", L)
