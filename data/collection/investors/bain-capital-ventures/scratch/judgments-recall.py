"""PRO-162 recall probe follow-up: the EDGAR full-text triage (scratch/recall/fts-triage.json) found Signify Health's
stake to be sale consideration for Remedy Partners (COLLECTION.md s1, Erik 2026-09-22)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
L = [jl.verdict("signify-health", "not_member",
    "Sale consideration: Remedy Partners, a BCV company from 2015 (its own row, remedy-partners), combined with Signify Health in 2019, "
    "and Signify's IPO registration files the investor rights agreement with Bain Capital Venture Fund 2014, L.P. signing beside Remedy "
    "Founders LLC among the former Remedy holders. The firm's 2022 listing reflects that stock; no source shows new BCV money in "
    "Signify. Stock received because a company bought a portfolio company is not membership, and the acquirer leaves the base "
    "(COLLECTION.md s1, Erik 2026-09-22).",
    ec="fund_filing", conf="high", cite="https://www.sec.gov/Archives/edgar/data/1828182/000095012320012946/filename22.htm")]
if __name__ == "__main__":
    jl.write("recall", L)
