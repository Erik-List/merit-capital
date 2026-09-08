#!/usr/bin/env python3
"""Compact one-line-per-row view of a queue batch, for judging in chat."""
import json, sys
from pathlib import Path
Q = Path(__file__).resolve().parents[1] / "scratch" / "queue"
for n in sys.argv[1:]:
    f = Q / f"batch-{int(n):03d}.json"
    rows = json.load(open(f))
    print(f"===== {f.name}  ({len(rows)} rows)")
    for r in rows:
        ev = r.get("evidence_class", "")
        wb = r.get("wayback_years", "") or ""
        wb = wb[:4] + ".." + wb[-4:] if len(wb) > 12 else wb
        bits = [f"t{r.get('tier','')}", ev]
        if r.get("site_url"): bits.append("site")
        if r.get("partners_formd"): bits.append("P:" + r["partners_formd"][:34])
        if r.get("partners_site"): bits.append("ps:" + r["partners_site"][:24])
        if wb: bits.append("wb" + wb)
        if r.get("site_invest_year"): bits.append("iy" + str(r["site_invest_year"]))
        if r.get("formd_span"): bits.append("fd" + r["formd_span"])
        if r.get("formd_max_round_usd"): bits.append(f"${r['formd_max_round_usd']/1e6:.1f}M")
        if r.get("rounds"): bits.append(f"r{len(r['rounds'])}")
        if r.get("issuer_city"): bits.append((r["issuer_city"] or "").title()[:14])
        if r.get("year_inc"): bits.append("inc" + str(r["year_inc"]))
        if r.get("former_unicorn"): bits.append("UNICORN")
        if r.get("sector"): bits.append("s:" + r["sector"][:18])
        k = r.get("known") or {}
        if k: bits.append("known=" + ",".join(f"{a}:{b}" for a, b in k.items())[:46])
        print(f"  {r['slug'][:34]:34s} | {r['name'][:30]:30s} | {'+'.join(r['need']):46s} | {' '.join(bits)}")
