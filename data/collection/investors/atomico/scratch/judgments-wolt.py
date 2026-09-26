"""PRO-79 post-close: Wolt under Erik's T2 rule of 2026-09-26 (6a7165e): a
founder's angel check stays out even where the firm lists it as its own,
unless a fund of the firm held the position."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
L = [jl.verdict("wolt", "not_member",
                "T2, Erik 2026-09-26 ('exclude as we did for Cherry'): a founder's angel check stays out even where the firm lists it, unless a fund of the firm held it. The only round press (Apr 2016, EUR 10M, EQT Ventures lead) names 'Skype founder Niklas Zennstrom' beside the individual angels Ilkka Paananen and Risto Siilasmaa, and the 2019 round names neither him nor the firm; no source shows an Atomico fund in Wolt. Supersedes decisions.md ruling 15",
                "site_listing", "medium", "https://arcticstartup.com/finnish-foodtech-startup-wolt-announces-raising-11-million-2/")]

if __name__ == "__main__":
    jl.write("wolt-001", L)
