"""PRO-105 patch 2026-09-29 ~21:00 UTC: CuspAI's $450M Series B at $2.6B (July 2026), found through the
firm's own post 'Four AI unicorns minted this year' after batch 1 had recorded it below $1B (the momentum
class, COLLECTION.md s6): the priced round is cited to the press, not to the firm's post (Rule A)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, rnd = jl.cls, jl.rnd
U = "https://pulse2.com/cuspai-raises-450-million-series-b-at-2-6-billion-valuation-to-discover-new-materials/"
L = [cls("cusp-ai", rng="1b_plus", usd=2600000000, val_src="web_verified", val_cite=U, asof="2026-07-20", val_conf="high",
     note="Generative AI for materials design (Cambridge, UK); Northzone participated in the $30M seed with Hoxton, BasisSet, LocalGlobe and Lightspeed (the firm's post, 2024-06-18); $100M Series A Sept 2025 at about $520M; $450M Series B at $2.6B, July 2026, co-led by Bezos Expeditions (Pulse 2.0; Reuters 2026-07-20; the firm's post 'Four AI unicorns minted this year')",
     rounds=[rnd("2024-06-18", "Seed", 30000000, None, True, jl.post("our-investment-in-cuspai-pioneering-ai-designed-materials-to-combat-climate-change"), "firm"),
             rnd("2025-09", "Series A", 100000000, None, None, jl.post("material-revolution-a-portrait-of-cuspais-chad-edwards"), "firm"),
             rnd("2026-07-20", "Series B", 450000000, "Bezos Expeditions (co-lead)", None, U, "press")])]
jl.write("batch-patch3", L)
