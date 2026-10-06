"""PRO-82 label pass (decisions.md D8). The firm's two stage claims, scored by scratch/label-score.py against this book's
own cited rows before any row was labelled:
  (a) live listing 'backed at Seed' (data-backed seed / all-seed): 31 of 36 cited rows agree -> first_party at MEDIUM.
      The row's own cited round wins where it disagrees (auxmoney, cowboy-space, deliveroo, notion, revolut, pilot).
  (b) 2009-2013 'Seed stage' filter ALONE: 1 of 1 cited, 7 unjudged -> eligible by semantics, first_party at LOW.
  (b2) filed under BOTH 'Seed stage' and 'Early stage': 0 of 5 -> refused; an anchor, not a label.
Patch lines carry no note (the grind's note stays)."""
import importlib.util, json
from pathlib import Path
spec = importlib.util.spec_from_file_location("gl", Path(__file__).with_name("gl.py"))
gl = importlib.util.module_from_spec(spec); spec.loader.exec_module(gl)
jl = gl.jl
C, post, arch, rnd = gl.C, gl.post, gl.arch, gl.rnd
LISTING = "https://www.indexventures.com/companies/"
A = """adzuna argent atlantic-money cartesia catch citymapper common-room cowboy creative-juice double duffel duna eisen goody
lightning-ai humanloop hutch-games immersive-gamebox lever linear nacelle newfront nuvo peanut lithic roli scoop second-home
stytch supersolid tactic tiney wise twelve-labs wetravel""".split()
B = "abe-s-market cruisewise fontself geckoboard rjdj the-gifts-project".split()
B2 = "erply go-try-it-on innovative-silicon mind-candy mobissimo peopleperhour songkick".split()
L = []
for s in A:
    L.append(jl.cls(s, stage="Seed", stage_src="first_party", stage_cite=LISTING, stage_conf="medium"))
for s in B:
    L.append(jl.cls(s, stage="Seed", stage_src="first_party", stage_cite=arch(s, "stage_filter", "Seed stage"), stage_conf="low"))
for s in B2:
    L.append(jl.cls(s, stage="undetermined", rounds=[]))
u = post("its-time-to-turn-on-autopilot")
L.append(jl.cls("pilot", stage="Series A", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2018-03",
                rounds=[rnd("2018-03", "Series A", 15000000, "Index Ventures", True, u, "firm"), rnd("2019-04-17", "Series B", 40000000, "Index Ventures", True, u, "firm")]))
L.append(jl.cls("harmonic", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2024-09"))
L.append(jl.cls("netvibes", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2006"))
gl.write("label-pass", L)
