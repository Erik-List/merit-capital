"""PRO-162, corrective rebuild 2: 'Risk Management Software' (the firm's 2003 rendering of RMS) resurfaced once risk-management-solutions
was excluded, and the rename step moved DealTime's verdict onto it (restored by hand). It takes RMS's own ruling."""
import importlib.util, json
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
V = json.load(open(Path(__file__).parents[1] / "companies/membership-ledger.json"))["bain-capital-ventures"]["verdicts"]
v = V["risk-management-solutions"]
L = [jl.verdict("risk-management-software", "not_member", "The firm's 2003 rendering 'Risk Management Software', the same company as the "
     "row 'risk-management-solutions' (RMS), which is ruled out; the ruling is the same: " + v["basis"],
     ec=v["evidence_class"], conf=v["confidence"], cite=v.get("citation"))]
if __name__ == "__main__":
    jl.write("rebuild-2", L)
