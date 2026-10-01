#!/usr/bin/env python3
"""Cross-check the research files against what the archive already proves.

A capture of the firm's own list proves the firm held the company BY that day.
So a researched "entry" dated after the first capture is not the entry: the
press named a later round the firm led or joined, and the earlier cheque is
still to find (COLLECTION.md s6: an announcement is class 1 for the round it
names; it asserts an ENTRY only where nothing earlier exists). Prints one line
per row with the mismatch class, and writes scratch/second-pass.json: the rows
that need a second look and why.
"""
import json
import re
import sys
from pathlib import Path

H = Path(__file__).resolve().parent
sys.path.insert(0, str(H))
import judge_lib as J  # noqa: E402
import pack  # noqa: E402


def ym(s):
    s = str(s or "")
    m = re.match(r"(\d{4})(?:-(\d{2}))?", s)
    return (int(m.group(1)), int(m.group(2) or 6)) if m else None


def months(a, b):
    return (b[0] - a[0]) * 12 + (b[1] - a[1])


def main():
    out = {}
    counts = {}
    for slug, r in sorted(J.RS.items()):
        if slug not in J.BASE:
            continue
        name = J.BASE[slug]["name"]
        e = pack.ev_for(slug, name)
        first = e.get("first_capture", "")[:6]
        first_ym = (int(first[:4]), int(first[4:6])) if first else None
        stages = list((e.get("stages") or {}).keys())
        ent = r.get("entry") or {}
        why = []
        if not ent or not ent.get("lakestar_named") or not str(ent.get("citation") or "").startswith("http"):
            why.append("no_cited_entry")
        else:
            d = ym(ent.get("date"))
            if d and first_ym and months(first_ym, d) > 2:
                why.append(f"entry_{ent.get('date')}_after_first_listing_{first[:4]}-{first[4:6]}")
            st = (ent.get("round") or "").lower()
            if stages and "Seed" in stages[0] and not re.search(r"seed|angel", st):
                why.append(f"site_says_Seed_research_says_{ent.get('round')}")
        if r.get("identity") == "unresolved":
            why.append("identity_unresolved")
        key = ";".join(w.split("_20")[0] if w.startswith("entry_") else w for w in why) or "ok"
        counts[key] = counts.get(key, 0) + 1
        print(f"{slug[:26]:26s} site={stages[0] if stages else '-':9s} first={first or '-':6s} "
              f"entry={str(ent.get('round'))[:18]:18s} {str(ent.get('date')):8s} | {'; '.join(why) or 'ok'}")
        if why:
            out[slug] = {"name": name, "why": why, "site_stage": stages, "first_listing": first,
                         "research_entry": {k: ent.get(k) for k in ("date", "round", "citation")} if ent else None}
    (H / "second-pass.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(counts, len(out), "rows for a second pass")


if __name__ == "__main__":
    main()
