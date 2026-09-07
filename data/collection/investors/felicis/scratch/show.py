#!/usr/bin/env python3
"""Compact batch view for the judge: only what a decision actually turns on."""
import json
import sys
from pathlib import Path

QUEUE = Path(__file__).resolve().parents[1] / "scratch" / "queue"
SHORT = {"status": "S", "hq_country": "C", "entry_stage": "E",
         "valuation_range": "V", "membership": "M"}


def main():
    for b in [int(a) for a in sys.argv[1:]]:
        rows = json.loads((QUEUE / f"batch-{b:03d}.json").read_text())
        print(f"===== batch {b:03d} ({len(rows)} rows)")
        for x in rows:
            need = "".join(SHORT.get(n, "?") for n in x["need"])
            k = x.get("known") or {}
            bits = [f"{x['slug']}", f"[{need}]"]
            if x.get("site_entry_stage"):
                bits.append(f"st={x['site_entry_stage']}")
            if x.get("first_seen"):
                bits.append(f"fs={x['first_seen']}")
            if k.get("hq_country"):
                bits.append(f"PRE_C={k['hq_country']}")
            if k.get("status"):
                bits.append(f"PRE_S={k['status']}")
            if k.get("valuation_range"):
                bits.append(f"PRE_V={k['valuation_range']}")
            if k.get("entry_stage"):
                bits.append(f"PRE_E={k['entry_stage']}")
            if x.get("former_unicorn"):
                bits.append("UNICORN")
            if x.get("partners_formd"):
                bits.append(f"pd={x['partners_formd']}")
            if x.get("formd_max_round_usd"):
                bits.append(f"max=${int(x['formd_max_round_usd']):,}")
            if x.get("issuer_city"):
                bits.append(f"@{x['issuer_city']}")
            if x.get("name") and x["name"].lower() != x["slug"].replace("-", " "):
                bits.append(f"'{x['name']}'")
            print("  " + " ".join(bits))


main()
