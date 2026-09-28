"""PRO-76 grind, batch-001 part C: Alloy (identity unresolved)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls = jl.cls
L = [cls("alloy", status="unknown", country="US", country_src="model_knowledge", rng="undetermined", stage="undetermined",
    grad="undetermined", focus=None,
    flags=["identity_unresolved", "country_prior", "city_unknown"],
    extra={"hq_country_confidence": "low"},
    note="The podcast site's page 'Alloy - 20VC' (posted 2022-08-03 by Kieran Hill, beside Fund I's US companies; captured 2022-2024) carries a name and nothing else, and the firm's 2026 card does not list it. At least four companies bear the name (Alloy the identity-risk platform, New York; Alloy Automation; Alloy Women's Health; Alloy Therapeutics); searched 2026-09-28 (Google News '\"Alloy\" 20VC', TechCrunch and Crunchbase News archives, the identity platform's Series B and C releases, which name no 20VC): no source ties 20VC to any of them. Stays a member on the firm's own listing; every outcome column undetermined; country is the Fund I desk prior.")]
if __name__ == "__main__":
    jl.write("batch-001c", L)
