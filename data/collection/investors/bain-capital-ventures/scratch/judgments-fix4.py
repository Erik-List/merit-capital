"""PRO-162 final verify fixes: Stamped's seed rests on its own evidence (a 2011 launch financing), so it carries stage_uncited at
low confidence (COLLECTION.md s6, PRO-131 b)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
L = [jl.cls("stamped", stage="Seed", stage_src="model", stage_conf="low", flags=["stage_uncited"])]
if __name__ == "__main__":
    jl.write("fix-4", L)
