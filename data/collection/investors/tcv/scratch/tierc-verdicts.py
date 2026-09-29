#!/usr/bin/env python3
"""Membership verdicts for the Form D name-match rows (PRO-169, decisions.md D9).

Every tier-C row (no listing on any TCV surface, in any year) whose only
evidence is a Form D naming a roster person is judged against the firm's
compliance list: TCV publishes "All investments (listed alphabetically)" and
the run holds every version from 2017 to 2026-07-15 plus the earlier sites'
lists, so a company on none of them is not a TCV position; the match locates
the person (T4), not the firm. Rows whose last Form D is dated after the live
list (2026-07-15) are left for the judge, since a deal that new cannot yet be
on the list. Writes scratch/queue/tierc.out.jsonl for `run.py record`.
"""
import json
import re
from pathlib import Path

INV = Path(__file__).resolve().parents[1]
Q = json.load(open(INV / "scratch/queue/queue.json"))
b = json.load(open(INV / "companies/base.json"))
BASE = {r["slug"]: r for r in (b if isinstance(b, list) else b.values())}
LIST_ASOF = "2026-07-15"
out, held = [], []
for it in Q:
    r = BASE.get(it["slug"])
    if not r or r.get("tier") != "C" or "membership" not in it["need"]:
        continue
    if r.get("site_url") or r.get("wayback_years"):
        continue
    span = r.get("formd_span") or ""
    first = span.split("-")[0] if span else ""
    # the span is in years: a company FIRST matched in the list's own year may be a deal made
    # after the list's date; one matched earlier was already a relationship when the list was
    # written, so its absence from the list decides it
    if first and first >= LIST_ASOF[:4]:
        held.append((it["slug"], r["name"], span, r.get("partners_formd")))
        continue
    who = r.get("partners_formd") or "a roster name"
    ev = "Form D" if r.get("formd_accessions") or r.get("formd_links") else "EDGAR"
    basis = (f"{ev} related-person name-match on {who}" + (f" ({span})" if span else "") +
             "; the company is on no version of TCV's compliance list (live 2026-07-15, archived 2017-2026) "
             "or earlier site list, which names every investment of the firm, so the match locates the person, "
             "not a TCV fund position (decisions.md D9; T4).")
    if r.get("edgar_forms"):
        basis = (f"Schedule 13D/G by a TCV fund ({r.get('edgar_span')}) on a listed company that is on no version "
                 "of the firm's compliance list: a TCV I-III public holding, which the list excludes by its own note "
                 "(decisions.md D4, D9; T3).")
    out.append({"slug": it["slug"], "verdict": "not_member", "who": "agent",
                "evidence_class": "formd_adjudicated" if not r.get("edgar_forms") else "fund_filing",
                "confidence": "high", "basis": basis})
dest = INV / "scratch/queue/tierc.out.jsonl"
dest.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in out))
print(f"{len(out)} not_member verdicts written to {dest.name}; {len(held)} held for the judge:")
for h in held:
    print("  ", *h)
