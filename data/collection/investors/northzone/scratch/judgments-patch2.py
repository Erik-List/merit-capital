"""PRO-105 patch after the graduation pass (2026-09-29 ~20:55 UTC): the SEC float layer joined 'Era' and
'Tier' to other listed companies (public since 2013 and 2011); the rows are private and the float is
quarantined (COLLECTION.md s8 duty 8). Flink and Hopin graduate on cited later rounds while their seed
entry is uncited: PRO-131 b, flag stage_uncited at low confidence."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls = jl.cls
L = [cls("era", flags=["model_disputes_source"], extra={"is_public": False}),
     cls("tier", flags=["model_disputes_source"], extra={"is_public": False}),
     cls("flink", stage_conf="low", stage="Seed", stage_src="model", flags=["stage_uncited"]),
     cls("hopin", stage_conf="low", stage="Seed", stage_src="model", flags=["stage_uncited"])]
jl.write("batch-patch2", L)
