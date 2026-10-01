import json, judge_lib as jl
led = json.loads((jl.INV / "companies/membership-ledger.json").read_text())["kleiner-perkins"]["verdicts"]
c = led["casi"]
jl.write("lead1", [jl.verdict("entremed-inc", "not_member",
    c["basis"] + " (EntreMed is CASI's former name; the same row under its earlier name, which resurfaced at the rebuild)",
    ec=c.get("evidence_class", "web"), conf=c.get("confidence", "medium"), cite=c.get("citation"))])
