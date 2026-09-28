"""PRO-76, the post-rebuild delta: the three recall additions of the recall
probe (companies/membership-ledger.json), judged and classified. Citations read
2026-09-28 (verify-url.py). Rulings cited: decisions.md D1, R1."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd = jl.cls, jl.verdict, jl.rnd
W = "web_verified"
U = "undetermined"
NOSTAGE = {"entry_stage_source": None, "entry_stage_confidence": None, "entry_stage_citation": None}
BOILER = "https://www.uktechnews.info/2025/03/17/fyxer-ai-secures-7-7-million-investment-led-by-20vc/"
TFN = "https://techfundingnews.com/factory-ai-150m-series-c-unicorn-ai-agents-developers/"
L = [
 verdict("perplexity", "member", "The firm's own boilerplate in its 2025 releases: '20VC has backed companies such as Perplexity, Linear, 11x, Deblock and Captions' (the 'About 20VC' text, UK Tech Investment News, 2025-03-17): the firm names the company as its own.", ec="web", conf="high", cite=BOILER),
 verdict("captions", "member", "The firm's own boilerplate in its 2025 releases: '20VC has backed companies such as Perplexity, Linear, 11x, Deblock and Captions' (the 'About 20VC' text, UK Tech Investment News, 2025-03-17): the firm names the company as its own.", ec="web", conf="high", cite=BOILER),
 verdict("factory", "member", "Factory's $150M Series C led by Khosla Ventures at a $1.5B valuation: 'Other investors include Sequoia Capital, Insight Partners, Blackstone, Evantic Capital, Abstract Ventures, 20VC, NEA, and Mantis VC' (Tech Funding News, 2026-04-17).", ec="web", conf="high", cite=TFN),

 cls("perplexity", status="private", country="US", city="San Francisco", focus="AI & Applied AI", rng="10b_plus", usd=20000000000, val_src=W,
     asof="2025-09", val_cite="https://finance.yahoo.com/news/perplexity-finalizes-20-billion-valuation-232758524.html",
     stage=U, extra=NOSTAGE,
     note="AI answer engine (Perplexity, San Francisco). A company the firm names as backed in its own 2025 boilerplate; no source names 20VC's round, and rounds from the 2022 seed through the 2025 growth rounds all fall inside the funds' life: undetermined. Mark: 'commitments from investors for $200 million in new funding at a $20 billion valuation' (Reuters via Yahoo Finance, September 2025), as in the Accel and IVP rows (a January 2026 tranche at about $23B is vendor-reported only).",
     rounds=[rnd("2024-01", "Series B", 73600000, "IVP", None, None),
             rnd("2025-09", "growth", 200000000, None, None, "https://finance.yahoo.com/news/perplexity-finalizes-20-billion-valuation-232758524.html")]),
 cls("captions", status="private", country="US", city="New York", focus="AI & Applied AI", rng="below_1b",
     stage=U, extra=NOSTAGE,
     note="AI video creation app (Captions, New York). A company the firm names as backed in its own 2025 boilerplate; no source names 20VC's round: undetermined. Below $1B, as in the a16z and Sequoia rows (about $500M in 2024)."),
 cls("factory", status="private", country="US", city="San Francisco", focus="AI & Applied AI", rng="1b_plus", usd=1500000000, val_src=W,
     asof="2026-04-17", val_cite=TFN,
     stage="Growth", stage_src=W, stage_conf="medium", entry_date="2026-04", stage_cite=TFN,
     note="AI software-development agents ('Droids'; Factory, San Francisco). The $150M Series C led by Khosla Ventures at a $1.5B valuation: 'Other investors include Sequoia Capital, Insight Partners, Blackstone, Evantic Capital, Abstract Ventures, 20VC, NEA, and Mantis VC' (Tech Funding News, 2026-04-17): the first round naming 20VC, so Growth (medium: the article does not say whether 20VC was new). The $5M seed of November 2023 (Sequoia and Lux) and the 2024 Series A name no 20VC. Mark: that Series C at $1.5B; a round at $3.5B with Blackstone was reported only as 'set to' (City AM, 2026-08-03). The Khosla, Lux and Sequoia rows still read below_1b, the stale side.",
     rounds=[rnd("2023-11", "seed", 5000000, "Sequoia Capital, Lux Capital", None, None),
             rnd("2026-04", "Series C", 150000000, "Khosla Ventures", True, TFN)]),
]
if __name__ == "__main__":
    jl.write("batch-delta", L)
