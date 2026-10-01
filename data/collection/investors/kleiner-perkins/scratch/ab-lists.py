#!/usr/bin/env python3
"""Work lists for the A/B pass and the stage/R7 pass, from the MERGED view (resolved + classification over the live
base, members only; skip-list duplicates of identity-merges.json left out). Writes queue/ab1.json (private $1B+),
ab2.json (momentum slice), ab3.json (public rows), st.json (stage citations for $1B+ rows without class 1/2 evidence,
plus the R7 sweep: site rows since 2010 with no round naming the firm)."""
import json, re
from pathlib import Path
HERE = Path(__file__).resolve().parent; INV = HERE.parent
base = {r["slug"]: r for r in json.loads((INV / "companies/base.json").read_text())}
led = json.loads((INV / "companies/membership-ledger.json").read_text())["kleiner-perkins"]["verdicts"]
C = json.loads((INV / "companies/classification.json").read_text()); C = C.get("kleiner-perkins", C)
R = json.loads((INV / "companies/resolved.json").read_text()); R = R.get("kleiner-perkins", R)
dups = {d for m in json.loads((INV / "companies/identity-merges.json").read_text())["kleiner-perkins"]["merges"] for d in m["duplicates"]}
site = {r["url"]: r for r in json.loads((INV / "sources/site/company-list.json").read_text())["rows"]}
HOT = {"AI & Applied AI", "Fintech & Payments", "Data Infrastructure", "DevTools & APIs"}
ab1, ab2, ab3, st = [], [], [], []
for s, r in base.items():
    if s in dups or led.get(s, {}).get("verdict") != "member":
        continue
    m = {**R.get(s, {}), **C.get(s, {})}
    rng, stt, src = m.get("valuation_range"), m.get("status"), m.get("entry_stage_source")
    big = rng in ("1b_plus", "10b_plus", "100b_plus")
    fs = int(str(r.get("first_seen") or "0")[:4] or 0)
    iy = int((site.get(r.get("site_url") or "", {}).get("invest_year") or "0")[:4] or 0)
    if stt == "private" and big:
        ab1.append(s)
    if stt == "private" and not big and max(fs, iy) >= 2021 and m.get("focus") in HOT:
        ab2.append(s)
    if stt == "public":
        ab3.append(s)
    if big and src not in ("web_verified", "first_party", "formd_structural", "program_terms"):
        st.append((s, "rule 4: $1B+ without class 1/2 stage evidence"))
    elif iy >= 2010 and r.get("site_url") and not any(x.get("firm_in_round") for x in (m.get("funding_rounds") or [])) \
            and src not in ("web_verified", "first_party", "formd_structural", "formd_band"):
        st.append((s, "R7 sweep: no round on record names the firm"))
Q = HERE / "queue"
for n, l in (("ab1", ab1), ("ab2", ab2), ("ab3", ab3)):
    (Q / f"{n}.json").write_text(json.dumps(sorted(l), indent=1))
(Q / "st.json").write_text(json.dumps([{"slug": s, "why": w} for s, w in sorted(st)], indent=1))
print({"ab1": len(ab1), "ab2": len(ab2), "ab3": len(ab3), "st": len(st),
       "st_rule4": sum(1 for _, w in st if w.startswith("rule 4"))})
