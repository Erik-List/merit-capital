"""PRO-161 standing duty 9 (2026-09-28): the duty 7 disagreement on Privy (an unnamed round after documented earlier
rounds) swept as a class. Rows where the firm's documented first money is a priced round with no series name are
staged by the structural rule (COLLECTION.md s6: two prior rounds read Growth; one prior reads Series A or Growth by
the era band, Series A ceiling $40M from 2022). Lighter is the one other row in that position; NYDIG, Futureswap,
RHI Group and OnePay stay undetermined because the entry itself or the instrument is unknown."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls = jl.cls

FORTUNE = "https://fortune.com/2025/11/11/lighter-fundraise-founders-fund-ribbit-capital-haun-ventures-robinhood-vladimir-novakovski/"
L = [cls("lighter", stage="Growth", stage_src="model", stage_conf="medium", stage_cite=FORTUNE, entry_date="2025-11-11")]
jl.write("duty9-1", L)
