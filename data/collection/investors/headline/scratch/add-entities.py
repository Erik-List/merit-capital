"""Re-add the own vehicles that edgar-entities.py cannot see (a unique EDGAR
company-search match returns a company page the seed step does not parse) and
confirm the home desk. Run after every edgar-entities.py run (run-log.md)."""
import json
from pathlib import Path

P = Path(__file__).resolve().parents[1] / "entities.json"
ADD = [("1931045", "Headline US VII, L.P.", "fund"),
       ("1931106", "Headline Global Growth IV, L.P.", "fund"),
       ("2002335", "Headline Global Growth Lux IV SCSP", "fund"),
       ("2040786", "Headline Lion SPV, L.P.", "fund"),
       ("2036016", "Headline Wombat SPV, L.P.", "fund"),
       ("1533898", "BV Capital Fund II, L.P.", "fund"),
       ("1533899", "BV Capital Fund II-A, L.P.", "fund"),
       ("1510113", "BV Capital Fund IV (Asia), L.P.", "fund"),
       ("1533897", "BV Capital Gmbh & Co Beteiligungs KG No. 1", "fund"),
       ("1534591", "BV Capital Management, LLC", "management")]
rows = json.loads(P.read_text())
have = {str(r["cik"]) for r in rows}
n = 0
for cik, name, role in ADD:
    if cik in have:
        continue
    rows.append({"cik": cik, "name": name, "desk": "headline", "vehicle_role": role,
                 "sources": ["company-search-single-match"], "confirmed": True})
    n += 1
for r in rows:
    if r["desk"] == "headline":
        r["confirmed"] = True
rows.sort(key=lambda r: (r["desk"], r["name"].lower()))
P.write_text(json.dumps(rows, indent=1) + "\n")
print(f"added {n}; {len(rows)} entities, {sum(r['desk'] == 'headline' for r in rows)} home")
