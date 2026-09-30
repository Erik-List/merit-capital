#!/usr/bin/env python3
"""Patch 1 (PRO-103): the group-1 agent revised 11x and Apron after the first
recording; both now carry a round tied to Visionaries. Writes queue/batch-patch1.out.jsonl
and the replacement notes to queue/patch1-notes.json (applied under the record lock)."""
import json
from judge_lib import line, research, write, rounds, HERE
d = research("11x"); a = research("apron")
R = [
    line("11x", entry_stage="Growth", entry_stage_source="web_verified",
         entry_stage_citation=d["entry"]["citation"], entry_stage_confidence="high",
         entry_date="2024-09-16", funding_rounds=rounds("11x")),
    line("apron", entry_stage="Seed", entry_stage_source="web_verified",
         entry_stage_citation=a["entry"]["citation"], entry_stage_confidence="medium",
         entry_date="2023-06", seed_to_a_graduation="graduated", graduation_source="web_verified",
         graduation_citation=a["graduation"]["citation"], graduation_confidence="high",
         funding_rounds=rounds("apron")),
]
NOTES = {
    "11x": "AI 'digital workers' for sales teams (San Francisco; founded 2022 in London); Visionaries joined Benchmark's $24M Series A (the company's release, GlobeNewswire 2024-09-16, absent from the 2023 pre-seed) and is among the backers of a16z's $50M Series B (2024-11-11), reported at about $350M (TechCrunch, sources), below $1B",
    "apron": "Invoice and supplier-payment automation for small businesses (London); UKTN (2023-09-28) names Bessemer's $5.5M seed of June 2023 as Apron's only earlier round and calls Visionaries Club an existing investor at the $15M Series A three months later, so the seed is the entry (medium); graduated with the Index-led Series A of 2023-09-28 (tech.eu); Series B $30M in Sept 2024 (Zinal Growth)",
}
write("batch-patch1.out.jsonl", R)
(HERE / "queue" / "patch1-notes.json").write_text(json.dumps(NOTES, indent=1, ensure_ascii=False))
