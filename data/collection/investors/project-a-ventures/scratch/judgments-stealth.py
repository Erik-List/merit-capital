"""The CMS 'Stealth' card (COLLECTION.md s3/s6: an unresolvable company reads undetermined)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write, LISTING  # noqa: E402

L = [cls("stealth", status="unknown", rng="undetermined", stage="undetermined", grad="undetermined",
         country="DE", country_src="model_knowledge", flags=["identity_unresolved", "country_prior"],
         note="The live CMS carries a card titled 'Stealth' with no fund, year, round, status, HQ or website: an "
              "undisclosed company the firm lists but does not name. Membership rests on the firm's own listing; every "
              "outcome column reads undetermined and the row leaves every metric. Country is the Berlin desk prior.")]
if __name__ == "__main__":
    write("stealth", L)
