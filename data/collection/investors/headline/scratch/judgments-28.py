"""E1 delta, A/B pass (s7) on the new visible rows: one headline sweep per $1B+ row for events
after its mark. No band moved."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write  # noqa: E402

L = [
    cls("rappi", note="A/B pass: Amazon's September 2025 money was a $25M convertible note with warrants for up to 12%, no valuation stated (ColombiaOne, 2026-09-19); the July 2021 $5.25B round stays the last priced mark, stale, as in the a16z and General Catalyst rows."),
    cls("genki-robotics", note="A/B pass: Axios (2026-04-21, 'Humanoid robotics startup gets $1 billion valuation') and Crunchbase News (2026-05-06) both report the Series A at $1B; no later round."),
    cls("olist", note="A/B pass: no priced round after the December 2021 $186M at $1.5B (Bloomberg Linea); Olist bought Flip in August 2025. Stale."),
    cls("wellhub", note="A/B pass: no priced round after the August 2023 Series F at $2.4B, as in the Atomico row. Stale."),
]
if __name__ == "__main__":
    write("e1-ab", L, record="--dry" not in sys.argv)
