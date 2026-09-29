"""PRO-105 register pass, UK side (2026-09-29 ~23:20 UTC): the UK rows still at `unknown`, from Companies House
(scratch/companies_house.py, the public register website; COLLECTION.md s5: free structured status). Also carries
Ocapo's cited facts onto eProspects, the row it was merged into after this pass showed they are one company
(identity-merges.json; the third rebuild). Artfinder and One2 1Two (8 Bars) have no register entity under those
names and stay unknown. The register answers are copied to sources/registers/register-status.json as evidence."""
import importlib.util
import json
import sys
from pathlib import Path

H = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("jl", H / "judge_lib.py")
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls = jl.cls
sys.path.insert(0, str(H))
import companies_house as ch  # noqa: E402

C = json.load(open(H.parent / "companies" / "classification.json")); C = C.get("northzone", C)
L_ADD = json.load(open(H.parent / "companies" / "membership-ledger.json"))["northzone"]["recall_additions"]
ocapo = [a for a in L_ADD if a["slug"] == "ocapo"][0]

bnt, col, ore, oca, epl = (ch.company(n) for n in ("06623962", "05436421", "04595626", "08350690", "11883531"))
oca_off = ch.officers("08350690")
zink = [o for o in oca_off if "ZINK" in o["name"]][0]
METASWITCH_PR = "https://www.metaswitch.com/about/press-releases/metaswitch-acquires-colibria"  # WebSearch result, 2026-09-29

L = [
    cls("bravenewtalent", status="defunct", extra={"status_citation": bnt["url"], "status_source": "register",
        "status_confidence": "high"},
        note=f"Companies House {bnt['number']}: {bnt['name']}, incorporated {bnt['incorporated']}, dissolved "
             f"{bnt['dissolved']} with its office care of an insolvency practice; no sale on record, so defunct"),
    cls("orecon", status="defunct", extra={"status_citation": ore["url"], "status_source": "register",
        "status_confidence": "high"},
        note=f"Companies House {ore['number']}: {ore['name']} (wave energy R&D), incorporated {ore['incorporated']}, "
             f"dissolved {ore['dissolved']}; no sale on record, so defunct"),
    cls("colibria", status="acquired", extra={"status_citation": METASWITCH_PR, "status_source": "web_verified",
        "status_confidence": "high"},
        note=f"Acquired by Metaswitch Networks, announced 2011-04-06 (Metaswitch's release); Companies House "
             f"{col['number']} shows {col['name']} dissolved {col['dissolved']} with its office at Metaswitch Networks"),
    cls("eprospects", status="private", country="GB", country_src="web_verified", country_cite=oca["url"],
        city="London", city_src="web_verified", focus="Media, Gaming & Advertising", entry_date="2013-07",
        clear=["city_unknown"],
        extra={"status_citation": oca["url"], "status_source": "register", "status_confidence": "medium",
               "hq_city_citation": oca["url"]},
        rounds=[{"amount_usd": None, "date": "2013-07", "firm_in_round": True, "lead": "Northzone",
                 "round": "undisclosed (GBP 9.5m investment with BOOST&Co)", "source": ocapo["citation"],
                 "source_type": "press"}],
        note=f"eProspects is the trading name of Ocapo Limited (Companies House {oca['number']}, incorporated "
             f"{oca['incorporated']}; {zink['name'].title()} of Northzone a director {zink['appointed']} to "
             f"{zink['resigned']}), in which Northzone led a GBP 9.5m investment in July 2013 (FinSMEs; the firm's "
             f"post); the Ocapo row is merged here. Ocapo Limited is active in London and EPROSPECTS LIMITED "
             f"({epl['number']}, {epl['incorporated']}) shares its director, so private (medium: a small operating "
             f"company with no recent round); round not named, so the entry stage stays undetermined"),
]
out = H.parent / "sources" / "registers" / "register-status.json"
reg = {"_readme": "Home-register answers behind the status pass of 2026-09-29 (scratch/judgments-patch6.py, "
                  "scratch/judgments-patch7.py): Companies House profiles read through the public website "
                  "(scratch/companies_house.py); the CVR and PRH answers are cached under data/filings/northzone/registers.",
       "companies_house": {c["number"]: c for c in (bnt, col, ore, oca, epl)},
       "companies_house_officers": {"08350690": oca_off}}
out.write_text(json.dumps(reg, indent=1, ensure_ascii=False) + "\n")
jl.write("batch-patch7", L)
