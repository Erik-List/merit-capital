"""PRO-75 membership pass 4 (after rebuild 1): Oxford Sciences Innovation resurfaced as its own row once its
name-variant canonical, Oxford Science Enterprises, was excluded (the build applies exclusions before merging;
COLLECTION.md s8, the 2tor-inc case). Same company, same D10 reading."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
L = [jl.verdict("oxford-sciences-innovation", "not_member",
                "decisions.md D10 (T5, fund-shaped position): Oxford Sciences Innovation (renamed Oxford Science "
                "Enterprises in 2021, excluded under the same ruling) is an investment company; the firm's own 2015 "
                "listing called it 'a fund that provides capital and business expertise to companies developed in "
                "Oxford University'. GV holds an interest in the vehicle, the LP-stake class.",
                ec="site_listing", conf="high", cite=jl.ARCH("oxford-sciences-innovation"))]
jl.write("members-4", L)
