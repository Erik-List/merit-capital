"""PRO-82: two rows corrected against a sibling book's better evidence (COLLECTION.md s9: read the sibling's row).
glow: TechCrunch (2026-07-22, the row's own valuation citation, re-read in full) says 'The Palo Alto-headquartered startup ...
raised $180 million in an all-equity Series A funding round that valued it at $1.2 billion ... alongside participation from
Index Ventures'. tactic: Visionaries Club's row found the UK entity struck off on 2026-02-17 while the site stays live."""
import importlib.util, json
from pathlib import Path
H = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("gl", H / "gl.py")
gl = importlib.util.module_from_spec(spec); spec.loader.exec_module(gl)
jl = gl.jl
CL = json.loads((H.parent / "companies/classification.json").read_text())
u = CL["glow"]["valuation_citation"]; assert "techcrunch.com/2026/07/22/glow" in u
L = [jl.cls("glow", country="US", country_src="web_verified", country_cite=u, city="Palo Alto", stage="Series A", stage_src="web_verified", stage_cite=u, stage_conf="high",
            entry_date="2026-07", note="correction: 'The Palo Alto-headquartered startup' raised '$180 million in an all-equity Series A ... alongside participation from Index Ventures' (TechCrunch, 2026-07-22); founded by Israelis, headquartered in Palo Alto; the same company as Redpoint's and Sequoia's Glow rows",
            rounds=[jl.rnd("2026-07-22", "Series A", 180000000, "Sequoia Capital, Cyberstarts, Greenoaks, Redpoint Ventures", True, u, "press")]),
     jl.cls("tactic", status="unknown", note="its UK entity Quantcopy Growth AI Ltd was struck off on 2026-02-17 (Companies House, per Visionaries Club's row) while tactic.fyi stays live, so the state cannot be established")]
gl.write("patch4", L)
