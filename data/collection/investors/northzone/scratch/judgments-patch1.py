"""PRO-105 patch after verify --in-flight, 2026-09-29 ~20:40 UTC: Klarna's entry citation (the firm's own
post names its 2015 investment); Stream and Sona carry a pre-filled status from one-word Wikidata joins
that their classification lines disputed in the note but did not override."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, rnd, post = jl.cls, jl.rnd, jl.post
K = post("klarna-europe-fountain-entrepreneurship")
L = [
 cls("klarna", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=K, entry_date="2015",
     note="Buy-now-pay-later and digital bank (Stockholm, founded 2005); 'Hans Otterling, a former General Partner at Northzone who led our 2015 investment in Klarna' (the firm's post, 2025-10-16): a 2015 entry ten years and several rounds after Sequoia's 2010 entry is a growth round under any reading; NYSE since Sept 2025; market cap aligned to IVP's and Atomico's cited figure of 2026-09-25; Wikidata SE confirmed",
     rounds=[rnd("2015", "growth round", None, "Northzone (Hans Otterling)", True, K, "firm")]),
 cls("stream", status="private"),
 cls("sona", status="private"),
]
jl.write("batch-patch1", L)
