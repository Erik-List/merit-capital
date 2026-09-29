#!/usr/bin/env python3
"""PRO-167 Tiger Global, adversarial A/B pass (COLLECTION.md 7), slice 1, chunk c: a rename found late in pass B.
Surface: Bing News (bq.py storage, NQ_TAG=ab1), 2026-09-29.
Run: NQ_TAG=ab1 python3 ab1c.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import cls

L = []

# ---------------------------------------------------------------- Aleo (the operating company is now Provable)
L.append(cls("aleo",
             note="A/B 2026-09-29: the operating company Tiger backed (Aleo Systems) now trades as Provable Inc., "
                  "San Francisco, 'the company behind Shield Wallet and Aleo' (its release of 2026-08-18); still "
                  "private, and no priced equity round since the 2022 Series B, so that mark stands, stale."))

if __name__ == "__main__":
    jl.write("ab-1c", L)
