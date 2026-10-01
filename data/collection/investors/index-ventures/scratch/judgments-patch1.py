"""PRO-82 patch 1: an uncited stage on a decided row reads confidence low (PRO-131 b); Seedcamp is an LP-class stake (D4)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("gl", Path(__file__).with_name("gl.py"))
gl = importlib.util.module_from_spec(spec); spec.loader.exec_module(gl)
L = [gl.jl.cls(s, extra={"entry_stage_confidence": "low"}) for s in ("big-health", "adaptive-ml")]
L.append(gl.verdict("seedcamp", "not_member", "fund-shaped entry (decisions.md D4, T5): Seedcamp is an investor (accelerator funds of which Index was a founding backer and LP, Saul Klein a co-founder), not an operating company; on the firm's 2012-2016 list under its Seed stage filter",
                    ec="site_listing", conf="high", cite=gl.arch("seedcamp", "stage_filter", "Seed stage")))
gl.write("patch1", L)
