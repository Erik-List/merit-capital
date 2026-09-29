"""PRO-105 register pass (2026-09-29 ~23:00 UTC): the status of the Nordic rows still at `unknown`, from the home
registers (COLLECTION.md s5: "the registers pay off on status"; a dissolution, liquidation or bankruptcy flag in the
home register is filing-grade `defunct` evidence). scratch/nordic_status.py, answers cached under
data/filings/northzone/registers. Norway's name search covers live entities only and matched none of the nine
Norwegian rows; Sweden has no free endpoint that answers a script; Denmark (cvrapi.dk) and Finland (PRH) answered.
Mojn ApS (Aabenraa, 2007) is a namesake of Northzone's Copenhagen Mojn and changes nothing."""
import importlib.util
import json
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls = jl.cls

REPO = Path(__file__).resolve().parents[5]
CACHE = REPO / "data" / "filings" / "northzone" / "registers"


def answer(url_part):
    """The cached register answer whose request URL contains url_part (never typed from memory)."""
    for f in CACHE.glob("*.json"):
        d = json.loads(f.read_text())
        if url_part in d["url"]:
            return json.loads(d["body"])
    raise SystemExit(f"no cached register answer for {url_part}")


def cvr_page(q):
    return f"https://datacvr.virk.dk/enhed/virksomhed/{answer('search=' + q)['vat']}"


spk, itr, cry, alu = (answer("search=" + q) for q in ("Speakanet", "Interse", "Cryptico", "AllUnite"))
imb = [c for c in answer("companies?name=Imbera")["companies"] if c["businessId"]["value"] == "1635979-8"][0]
imb_url = f"https://tietopalvelu.ytj.fi/yritys/{imb['businessId']['value']}"
ge = [n for n in imb["names"] if n["name"].startswith("GE ")][0]

L = [
    cls("speakanet", status="defunct", extra={"status_citation": cvr_page("Speakanet"), "status_source": "register",
        "status_confidence": "high"},
        note=f"Danish register (CVR {spk['vat']}): {spk['name']}, the company behind GoHello, 'Speakanet A/S' its "
             f"alias, ended {spk['enddate']} in bankruptcy (creditbankrupt); a bankruptcy with no sale reads defunct"),
    cls("interse", status="defunct", extra={"status_citation": cvr_page("Interse"), "status_source": "register",
        "status_confidence": "medium"},
        note=f"Danish register (CVR {itr['vat']}): Interse A/S was renamed '{itr['name']}' (the wind-down company of "
             f"1 December 2008) and ended {itr['enddate']} in bankruptcy; Tracxn records the company as closed in 2010; "
             f"the wind-down name suggests the business may have been transferred, but no buyer is on record, so defunct at medium"),
    cls("cryptico", status="defunct", extra={"status_citation": cvr_page("Cryptico"), "status_source": "register",
        "status_confidence": "medium"},
        note=f"Danish register (CVR {cry['vat']}): {cry['name']}, founded {cry['startdate']}, dissolved "
             f"{cry['enddate']} without bankruptcy; after the firm sold its stake back to the founders in Q4 2006 (its 2010 "
             f"page); medium because the register entity is an ApS in Solrød Strand and no source ties it to the "
             f"chaos-encryption company by more than the name and the 2001 start"),
    cls("allunite", status="private", extra={"status_citation": cvr_page("AllUnite"), "status_source": "register",
        "status_confidence": "medium"},
        note=f"Danish register (CVR {alu['vat']}): {alu['name']}, founded {alu['startdate']} (the firm's page: "
             f"founded 2013), still active in {alu['city']} with {alu['employees']} employees, no end date and no "
             f"bankruptcy; operating but small, so private"),
    cls("imbera", status="acquired", extra={"status_citation": imb_url, "status_source": "register",
        "status_confidence": "high"},
        note=f"Finnish register (PRH, business ID {imb['businessId']['value']}): Imbera Electronics Oy was renamed "
             f"'{ge['name']}' on {ge['registrationDate']}, so acquired by GE; the entity ended {imb.get('endDate')}"),
]
jl.write("batch-patch6", L)
