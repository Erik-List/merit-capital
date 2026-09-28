#!/usr/bin/env python3
"""Orchestrator fix after the delta (PRO-77): IEI, an unnameable listed row, still owes a country."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import cls
L = [cls("iei", country="US", country_src="model_knowledge", flags=["country_prior"],
         extra={"hq_country_confidence": "low"},
         note="IEI is listed on the firm's 2001 software page (/soft/iei.html) but no page body or other source names the "
              "company; the country is the firm's own desk (Palo Alto, US-only in 2001), inferred and flagged country_prior.")]
if __name__ == "__main__":
    jl.write("fix-002", L)
