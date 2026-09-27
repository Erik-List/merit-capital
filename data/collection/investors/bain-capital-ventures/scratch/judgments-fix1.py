"""PRO-162: Onera's fate corrected (the firm's live label 'acquired by Lyniate in 2021' belongs to Datica's integration business,
which Lyniate bought in April 2021; ToolsGroup bought Onera in June 2022). Found by the batch-7 judge."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
L = [jl.cls("onera-acquired-by-lyniate-in-2021", status="acquired", rng="below_1b",
    note="Retail inventory visibility (Burlingame). 'ToolsGroup Acquires Onera to Extend Retail Platform from Planning to Execution' (Supply "
         "Chain Xchange, 2022-06-07, " + jl.NEWS("onera-acquired-by-lyniate-in-2021", "ToolsGroup Acquires Onera") + "). The firm's live "
         "list labels it 'acquired by Lyniate in 2021', which is the fate of Datica's integration business (Lyniate, April 2021), not "
         "Onera's. BCV's 2014 round (Ajay Agarwal) is not named.")]
if __name__ == "__main__":
    jl.write("fix-1", L)
