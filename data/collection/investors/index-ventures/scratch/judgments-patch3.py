"""PRO-82 momentum slice (scratch/momentum.py, 140 recent private rows below $1B, one press check each, 2026-10-06):
one row changes. Ryft was bought by Cyera in April 2026, nine months after its seed; and Build's description is corrected."""
import importlib.util, json, re
from pathlib import Path
H = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("gl", H / "gl.py")
gl = importlib.util.module_from_spec(spec); spec.loader.exec_module(gl)
jl = gl.jl
G = json.loads((H / "graduation-surfaces.json").read_text()); M = json.loads((H / "momentum.json").read_text())
def mom(slug, sub):
    hits = sorted([i for i in M[slug]["items"] if sub.lower() in i["title"].lower()], key=lambda i: (i["date"], i["source"]))
    assert hits and len({h["title"][:40].lower() for h in hits}) == 1, [h["title"][:60] for h in hits]
    u = jl._gs().decode(hits[0]["gid"]); assert u; return u
e = G["ryft"]; surfaces = ["firm: the company page on indexventures.com and the Perspectives archive (586 posts to 2026-09-30) for Ryft -> the $8M seed post of 2025-07-09 and nothing after it"]
for sn, sf in sorted(e["surfaces"].items()):
    assert sf["status"] == "ok"
    surfaces.append(f"{sn}: {sf['query']} -> {sf.get('n', len(sf.get('items', [])))} items; the seed of July 2025 and the sale to Cyera of April 2026, no round between them (other items are Ryft the UK payments company)")
u = mom("ryft", "Cyera acquires two-year-old startup Ryft")
L = [jl.cls("ryft", status="acquired", grad="not_graduated", grad_src="web_verified", grad_cite=u, grad_asof=e["asof"], surfaces=surfaces,
            note="acq. by Cyera, April 2026 ($100M to $130M; CTech, 2026-04-23), nine months after the seed: the sale ends the chance of a later round",
            extra={"status_citation": u}),
     jl.cls("build", note="correction: a British and American team building an 'agentic real estate' platform (EU-Startups, 2026-06-30), not infrastructure-project software")]
gl.write("patch3", L)
