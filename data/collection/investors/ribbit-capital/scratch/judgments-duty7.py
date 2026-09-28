"""PRO-161 standing duty 7 (2026-09-28): the blind 5% sample (9 rows, scratch/blind-sample.json, a second judge with
no access to the record: scratch/blind-results.json) disagreed on 2 of 54 cells. Both rows take the flag `unstable`
and are adjudicated here; the notes are rewritten by set-notes.py from notes-duty7.json."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls = jl.cls

BLOCK = ("https://www.theblock.co/news/deals/2025-03-19-privy-raises-15-million-usd-round-led-by-ribbit-capital-"
         "investment-in-web3-wallet-infrastructure-heats-up-347110")
SIFTED = "https://sifted.eu/articles/inside-saltpay"

L = [
    cls("privy", stage="Growth", stage_src="model", stage_conf="medium", stage_cite=BLOCK, entry_date="2025-03",
        flags=["unstable"]),
    cls("teya", rng="1b_plus", usd=1000000000, val_src="web_verified", val_cite=SIFTED, asof="2021-05",
        flags=["stale", "unstable"], extra={"valuation_range_source": "web_verified"}),
]
jl.write("duty7-1", L)
