"""E1 delta, duty 1: Rappi's unicorn-list pre-fill flags come off; its mark is the cited July
2021 Series F at $5.25B (LatamList)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write  # noqa: E402

L = [cls("rappi", clear=["needs_web_value", "unicorn_name_match"])]
if __name__ == "__main__":
    write("e1-duties", L, record="--dry" not in sys.argv)
