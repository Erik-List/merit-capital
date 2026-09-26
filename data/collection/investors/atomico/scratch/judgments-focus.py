"""PRO-79: sector focus for the ten nameable rows the grind left without one."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
F = {"hinge-health": "Healthcare & Bio", "masterclass": "Consumer & Marketplaces",
     "mews": "SaaS", "onna": "SaaS", "pactum": "AI & Applied AI",
     "psiquantum": "Industrial & Robotics", "stripe": "Fintech & Payments",
     "teatime-games": "Media, Gaming & Advertising", "the-climate-corporation": "Climate & Energy",
     "wolt": "Consumer & Marketplaces"}
L = [jl.cls(s, focus=f) for s, f in F.items()]

if __name__ == "__main__":
    jl.write("focus-001", L)
