"""PRO-75 membership pass 5 (after rebuild 2): the Form D legal-name pairs that flip their rendering between builds
(two issuer CIKs or two filings per company). Each slug of the pair needs its own verdict, or an excluded one
resurfaces under the other name (COLLECTION.md s8). Same T4 readings as culture-amp-inc, qadium-inc and vise-inc."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
E = "formd_adjudicated"
L = [jl.verdict("culture-amp-pty-ltd", "not_member",
                "T4: Wesley Chan's seat after GV (the Australian parent's filing; same company as culture-amp-inc). His GV "
                "pages run 2012-14; Culture Amp's 2017 filings date from his years at Felicis, and GV does not list the "
                "company.", ec=E, conf="high",
                cite="https://www.sec.gov/Archives/edgar/data/1710008/000171000817000001/0001710008-17-000001-index.htm"),
     jl.verdict("expanse-inc", "not_member",
                "T4: Shaun Maguire's founder seat (Expanse is Qadium renamed in 2019, one CIK; same company as "
                "qadium-inc). He co-founded Qadium before joining GV; no GV vehicle filing and no GV list carries Qadium "
                "or Expanse.", ec=E, conf="medium",
                cite="https://www.sec.gov/Archives/edgar/data/1642992/000164299219000002/0001642992-19-000002-index.htm"),
     jl.verdict("vise-technologies-inc", "not_member",
                "T4: Shaun Maguire's seat after GV (same company as vise-inc). His GV pages run 2017-19; Vise's filings "
                "date from his years at Sequoia, and GV does not list the company.", ec=E, conf="high",
                cite="https://www.sec.gov/Archives/edgar/data/1812090/000181209021000003/0001812090-21-000003-index.htm")]
jl.write("members-5", L)
