"""PRO-83: the Form D name-match rows, judged cluster-first (COLLECTION.md §3), plus two rule-6 citations.

The roster sweep matched only the common names Tom/Thomas Wilson and Will/William/Bill Bennett
outside Seedcamp V L.P. itself. Seedcamp takes no board seats (FAQs; decisions.md D8) and
none of these issuers is on any Seedcamp surface: each is a namesake's seat (US real
estate SPVs, Canadian miners, an Ohio spirits maker, US health and tech companies)."""
import importlib.util, json
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
ROOT = Path(__file__).resolve().parents[5]
base = json.loads((ROOT / "data/collection/investors/seedcamp/companies/base.json").read_text())
L = []
for r in base:
    if r.get("tier") != "C":
        continue
    who = r.get("partners_formd") or ""
    L.append(jl.verdict(r["slug"], "not_member",
        f"Form D name-match only ({who or 'roster namesake'}); a namesake of a Seedcamp person, the issuer is on no Seedcamp surface and the firm takes no board seats (decisions.md D8, cluster ruling)",
        ec="formd_adjudicated", conf="high"))
CH = "https://find-and-update.company-information.service.gov.uk/company/"
L.append(jl.cls("9fin", country="GB", country_src="web_verified", country_cite=CH + "10451957"))
L.append(jl.cls("fluidstack", country="GB", country_src="web_verified", country_cite=CH + "10985545"))
if __name__ == "__main__":
    jl.write("batch-formd", L)
