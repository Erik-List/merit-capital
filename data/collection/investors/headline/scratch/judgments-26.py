"""E1 delta: the three Asia-desk rows whose company cannot be named carry the same shape as the
book's earlier unnameable rows: S2A undetermined, and a country inferred from the desk partner who
lists them (flag country_prior)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write  # noqa: E402

L = [
    cls("cardmon", country="TW", flags=["country_prior"], extra={"seed_to_a_graduation": "undetermined"}),
    cls("undone", country="TW", flags=["country_prior"], extra={"seed_to_a_graduation": "undetermined"}),
    cls("openhome", country="JP", flags=["country_prior"], extra={"seed_to_a_graduation": "undetermined"}),
]
if __name__ == "__main__":
    write("e1-unnamed", L, record="--dry" not in sys.argv)
