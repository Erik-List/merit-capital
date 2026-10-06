"""PRO-82: weaviate, missed in batch-007."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("gl", Path(__file__).with_name("gl.py"))
gl = importlib.util.module_from_spec(spec); spec.loader.exec_module(gl)
C, post, rnd = gl.C, gl.post, gl.rnd
u = post("yes-the-world-needs-another-database")
L = [C("weaviate", status="private", country="NL", city="Amsterdam", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=u, entry_date="2023-04", rng="below_1b",
    focus="Data Infrastructure", note="Open-source AI-native vector database (Amsterdam); 'I couldn't be more thrilled to announce our partnership with Weaviate to lead their Series B' ($50M; the firm's post, 2023-04-20), Erin Price-Wright then the Index partner; place aligned to NEA's row",
    rounds=[rnd("2023-04-20", "Series B", 50000000, "Index Ventures", True, u, "firm")])]
gl.write("patch2", L)
