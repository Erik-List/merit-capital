"""PRO-162, after the one scheduled rebuild. The build applies ledger exclusions before the identity overlay, so a merge group whose
canonical is not_member never runs and its other renderings resurface as their own rows (COLLECTION.md s8: every slug of such a
group needs its own verdict). And the rename step moved 17 verdicts from excluded rows onto those renderings; two landed on a
different company (Ameritrade's on the 2006 Shopping.com row, Stream International's on the Stream Global Services Form D row).
Each line below gives the row the ruling of the company it actually is."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
V = __import__("json").load(open(Path(__file__).parents[1] / "companies/membership-ledger.json"))["bain-capital-ventures"]["verdicts"]
L = []


def same_as(slug, canonical, what):
    v = V[canonical]
    L.append(jl.verdict(slug, "not_member", f"{what}, the same company as the row '{canonical}' (identity-merges.json), which is ruled "
                        "out; the ruling is the same: " + v["basis"], ec=v["evidence_class"], conf=v["confidence"], cite=v.get("citation"))
             | ({"exclusion": v["exclusion"]} if v.get("exclusion") else {}))


same_as("shopping-com-formerly-dealtime-com", "shopping-com", "The firm's 2006 rendering 'Shopping.com (formerly Dealtime.com)'")
same_as("dealtime", "shopping-com", "The firm's 2003 rendering 'DealTime'")
same_as("stream-international", "stream", "The firm's 2006 rendering 'Stream International'")
same_as("the-princeton-review", "education-holdings-1-the-princeton-review", "The Princeton Review")
same_as("interpath-usinternetworking", "usinternetworking", "The firm's 2006 rendering 'Interpath / USInternetworking'")
same_as("wharton-econometrics", "wefa-associates", "Wharton Econometric Forecasting Associates")
same_as("edata-resources", "environmental-data-resources-inc", "The firm's 2003 rendering 'EData Resources'")
L.append(jl.verdict("stream-global-services-inc", "not_member",
    "Stream Global Services, Inc. (Wellesley, MA), the Form D-only row of a 2009 $185M offering naming a 'Jeffrey Schwartz' as director: "
    "a company listed on NYSE Amex since its 2008 formation (the former Global BPO Services Corp.), so the filing is a placement into a "
    "listed company, not a venture round (COLLECTION.md s1 T3); nothing ties it to a BCV fund, and it is not the Stream International "
    "the firm listed (ruled on its own row).",
    ec="formd_adjudicated", conf="medium",
    cite="https://www.sec.gov/Archives/edgar/data/1405287/000140528709000001/0001405287-09-000001-index.htm"))
if __name__ == "__main__":
    jl.write("rebuild-1", L)
