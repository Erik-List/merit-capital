"""PRO-75 membership pass 2: listed rows whose membership a derivation decides against the listing (decisions.md D10)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
L = [jl.verdict("oxford-science-enterprises", "not_member",
                "decisions.md D10 (T5, fund-shaped position): an investment company, not an operating company. The firm's "
                "own 2015 listing described Oxford Sciences Innovation (renamed Oxford Science Enterprises in 2021) as "
                "'a fund that provides capital and business expertise to companies developed in Oxford University'; GV "
                "holds an interest in the vehicle, the LP-stake class (the Sutter Hill D6 reading).",
                ec="site_listing", conf="high", cite=jl.ARCH("oxford-science-enterprises"))]
jl.write("members-2", L)
