"""PRO-162: the 2012 listing's navigation link captured as a company row (T5, not a company)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
L = [jl.verdict("bain-capital-ventures-investments", "not_member",
    "Not a company: the row is the 2012 listing's navigation link '| Bain Capital Ventures Investments |' to "
    "/portfolio/company/all-bain-capital-ventures-investments/, captured as a company page (COLLECTION.md s1 T5). "
    "Added to config wayback.non_company_slugs and the identity-merges rejects so the rebuild drops it.",
    ec="site_listing", conf="high")]
if __name__ == "__main__":
    jl.write("nav", L)
