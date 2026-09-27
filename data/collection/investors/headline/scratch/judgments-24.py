"""Duties 1 and 3 (COLLECTION.md s8), close-out: the unicorn pre-fill's two flags on the nine
rows whose mark the valuation pass replaced with a cited round (valuation_source web_verified)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write  # noqa: E402

SLUGS = ["acorns", "creditas", "flutterwave", "gopuff", "icertis", "lightricks", "sorare", "staffbase", "swile"]
L = [cls(s, clear=["needs_web_value", "unicorn_name_match"]) for s in SLUGS]
if __name__ == "__main__":
    write("duties-002", L, record="--dry" not in sys.argv)
