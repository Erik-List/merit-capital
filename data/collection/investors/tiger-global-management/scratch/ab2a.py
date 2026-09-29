#!/usr/bin/env python3
"""A/B pass, slice 2, chunk a (PRO-167): public rows whose recorded figure was an SEC float or a cap
older than September 2026, refreshed to the market cap of 2026-09-29 (COLLECTION.md 6: market cap is
canonical, float is corroboration only). Caps and their page URLs are read from ab2-caps.json, written
by ab2-caps.py from stockanalysis.com; nothing is typed by hand.
Run: NQ_TAG=ab2 python3 ab2a.py"""
import json
from pathlib import Path

import judge_lib as jl
from judge_lib import cls

HERE = Path(__file__).resolve().parent
CAPS = json.loads((HERE / "ab2-caps.json").read_text())


def band(usd):
    return ("100b_plus" if usd >= 100e9 else "10b_plus" if usd >= 10e9
            else "1b_plus" if usd >= 1e9 else "below_1b")


def cap(slug, note, dispute=True):
    c = CAPS[slug]
    assert c["currency"] == "$", (slug, c)   # every cap in this chunk is quoted in USD
    usd = c["usd_native"]
    return cls(slug, rng=band(usd), usd=usd, val_src="web_verified", val_cite=c["url"], asof=c["asof"],
               val_conf="high", flags=("model_disputes_source",) if dispute else (), note=note)


L = [
    cap("freshworks-inc", dispute=False, note=(
        "A/B pass 2026-09-29: market cap refreshed to $3.26B on 2026-09-29 (stockanalysis.com, Nasdaq: FRSH), "
        "from $3.63B on 2026-08-31; same band. The Accel ($3.63B, 2026-08) and Sequoia ($3.0B, 2026-07-17) rows "
        "carry older caps.")),
    cap("mercado-libre", note=(
        "A/B pass 2026-09-29: the SEC float of $122.9B (2025-06-30) is replaced by the market cap, $86.55B on "
        "2026-09-29 (stockanalysis.com, Nasdaq: MELI; the cap fell about 31% in a year), so the band moves from "
        "100b_plus to 10b_plus. Still listed; no acquisition or de-listing found.")),
    cap("nextdoor", note=(
        "A/B pass 2026-09-29: the SEC float of $434.4M (2025-06-30) is replaced by the market cap, $930.37M on "
        "2026-09-29 (stockanalysis.com, NYSE: NXDR), still below $1B. The Benchmark and Greylock rows ($866.5M) "
        "and the Redpoint row ($434.4M) carry 2025-06-30 figures.")),
    cap("pagaya-technologies-ltd", note=(
        "A/B pass 2026-09-29: the SEC float of $1.11B (2025-06-30) is replaced by the market cap, $1.45B on "
        "2026-09-29 (stockanalysis.com, Nasdaq: PGY); same band.")),
    cap("palantir", note=(
        "A/B pass 2026-09-29: the SEC float of $299.3B (2025-06-30) is replaced by the market cap, $446.97B on "
        "2026-09-29 (stockanalysis.com, NYSE: PLTR); same band.")),
    cap("procore-technologies-inc", note=(
        "A/B pass 2026-09-29: the SEC float of $8.21B (2025-06-30) is replaced by the market cap, $7.43B on "
        "2026-09-29 (stockanalysis.com, NYSE: PCOR), in line with the ICONIQ row ($7.45B, 2026-09-28); same band.")),
    cap("pure-storage-inc", note=(
        "A/B pass 2026-09-29: the SEC float of $17.0B (2025-08-03) is replaced by the market cap of Everpure, "
        "the renamed Pure Storage (NYSE: P; the old PSTG page redirects), $43.37B on 2026-09-29 "
        "(stockanalysis.com), in line with the Sutter Hill ($43.12B) and IVP ($41.99B) rows; the Greylock and "
        "Redpoint rows still carry the 2025-08-03 figure of $33.16B.")),
    cap("roblox", note=(
        "A/B pass 2026-09-29: the SEC float of $65.5B (2025-06-30) is replaced by the market cap, $29.83B on "
        "2026-09-29 (stockanalysis.com, NYSE: RBLX; down about 68% in a year), still 10b_plus. The a16z row reads "
        "$27.52B (2026-08); the Greylock ($30.94B) and First Round ($27.52B) rows carry 2025-06-30 figures.")),
]

if __name__ == "__main__":
    jl.write("ab-2a", L)
