"""Recall additions (PRO-108, COLLECTION.md s3): companies the firm's surfaces never listed, each with a
non-vendor page naming Lakestar as an investor (scratch/recall-candidates.json, every URL re-loaded by the
recall agent; Argo from the deutsche-startups.de Lakestar tag archive). Written into the ledger's
recall_additions, which the base build injects on the next rebuild. Rejected candidates stay in
recall-candidates.json and the report: Vsim (the investor named is 'Lakestar Scout Fund', a scout cheque, T2),
Zefi.ai (Halo, the firm's angel programme, T2), Openlaw (vendor only)."""
import json, sys
from pathlib import Path
H = Path(__file__).resolve().parent
sys.path.insert(0, str(H.parents[4] / "scripts"))
from paths import Paths, write_atomic
P = Paths("lakestar")
led = json.loads(P.ledger.read_text())
b = led.setdefault("lakestar", {"verdicts": {}, "recall_additions": []})
cand = {a["name"]: a for a in json.loads((H / "recall-candidates.json").read_text())["additions"]}
ADD = []
for name, sector in (("Chamo Games", "games"), ("Cosine", "ai"), ("Juo", "saas"), ("GeneralMind", "ai"),
                     ("Antidote", "ai"), ("Pit", "ai")):
    a = cand[name]
    ADD.append({"name": name, "slug": name.lower().replace(" ", "-"), "first_seen": a["date"][:4], "on_site_now": False,
                "sector": sector,
                "basis": f"{a['what']}. {a['round']} of {a['date']} ({a['amount']}): '{a['quote']}' Never on a lakestar.com "
                         f"surface; found by the recall probe's press sweep.",
                "citation": a["citation"]})
ADD.append({"name": "Argo", "slug": "argo", "first_seen": "2017", "on_site_now": False, "sector": "fintech",
            "basis": "ARGO Trade Solutions GmbH, the trade-finance start-up of the Shoplove founders: 'Lakestar, der Fonds von "
                     "Star-Investor Klaus Hommels, investierte ... bereits in das FinTech-Unternehmen', a double-digit million "
                     "amount, and the commercial register showed Lakestar holding 23% (deutsche-startups.de, 2017-05-09, citing "
                     "Gruenderszene). Never on a lakestar.com surface; found in the German press archive tagged Lakestar.",
            "citation": "https://www.deutsche-startups.de/2017/05/09/shoplove-gruender-finanzieren-jetzt-handelsgeschaefte/"})
have = {a["slug"] for a in b.get("recall_additions", [])}
for a in ADD:
    if a["slug"] not in have:
        b.setdefault("recall_additions", []).append(a)
write_atomic(P.ledger, json.dumps(led, indent=1, ensure_ascii=False) + "\n")
print([a["slug"] for a in b["recall_additions"]])
