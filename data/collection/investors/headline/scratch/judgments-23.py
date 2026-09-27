"""Standing duties 4, 5 and 8 (COLLECTION.md s8): the float sweep's name-collision class.
Three rows carried is_public from a registrant that is not the company (Pronto Networks'
2017 float, Flux and Pulse's wrong joins); none of the three ever listed. Shopping.com's
note keeps only its corrected half."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write  # noqa: E402

C = json.loads((Path(__file__).resolve().parents[1] / "companies" / "classification.json").read_text())
NOPUB = {"is_public": False, "public_since": None}
L = [
    cls("pronto-networks", flags=["model_disputes_source"],
        extra={**NOPUB, "valuation_source": "model_knowledge", "valuation_range_source": "model_knowledge", "valuation_asof": None},
        note="Duty 8: the 2013 listing and 2017 SEC float came from another registrant named Pronto; Pronto Networks never listed (quarantined)."),
    cls("flux", flags=["model_disputes_source"], extra=NOPUB,
        note="Duty 8: the listing flag came with the wrong CZ join; Flux never listed."),
    cls("pulse", flags=["model_disputes_source"], extra=NOPUB,
        note="Duty 8: the listing flag came with the wrong BG join; Pulse was private until LinkedIn bought it."),
    cls("shopping-com", note=C["shopping-com"]["note"].split(" | ")[1]),
]
if __name__ == "__main__":
    write("duties-001", L, record="--dry" not in sys.argv)
