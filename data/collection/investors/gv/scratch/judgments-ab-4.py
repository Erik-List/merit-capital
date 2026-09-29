#!/usr/bin/env python3
"""A/B pass (COLLECTION.md s6 'the web pass pins it or kills it'; PRO-75, 2026-09-29): the two needs_web_value rows.
Neither Inertia's $450M Series A nor Treeline's raises or its pending reverse merger carries a published valuation,
so under Rule A both stay below_1b and the flag is cleared; the report lists both as likely understatements."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl  # noqa: E402

cls = json.loads((jl.INV / "companies/classification.json").read_text())


def plus(slug, extra):
    return (cls.get(slug, {}).get("note") or "").rstrip() + " " + extra


L = [jl.cls("inertia", clear=["needs_web_value"],
            note=plus("inertia", "Web pass 2026-09-29: Crunchbase News and TechCrunch (2026-04-14) name no valuation "
                      "and Google News carries none, so the row stays below_1b under Rule A, a likely understatement.")),
     jl.cls("treeline-biosciences", clear=["needs_web_value"],
            note=plus("treeline-biosciences", "Web pass 2026-09-29: no priced round or deal figure names a "
                      "valuation (the reverse merger gives Standard holders 16% but states no price), so the row "
                      "stays below_1b under Rule A, a likely understatement until the merger closes."))]
jl.write("ab-4", L)
