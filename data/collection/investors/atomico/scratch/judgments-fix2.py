"""PRO-79 grind: correction to batch-001's andercore line (found by the recall
probe's press sweep, 2026-09-26)."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)

L = [jl.cls("andercore", stage="undetermined",
            extra={"entry_stage_source": None, "entry_stage_confidence": None, "entry_stage_citation": None},
            note="CORRECTED 2026-09-26: the Feb 2026 $40M Series B was NOT Atomico's first round. Tech.eu: 'The round includes participation from existing investors Atomico and Project A', and the firm's own post is titled 'Continuing our partnership with Andercore' - the entry predates the B and its round is unnamed on every surface -> undetermined (the ankar reading)",
            rounds=[jl.rnd("2026-02-11", "Series B", 40000000, "Atomico; Project A", True,
                           "https://tech.eu/2026/02/11/andercore-is-expanding-its-ai-based-industrial-trade-platform-following-a-40m-series-b-raise/")])]

if __name__ == "__main__":
    jl.write("fix-002", L)
