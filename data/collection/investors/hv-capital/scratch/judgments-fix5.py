import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write  # noqa: E402
write("fix-005", [cls("musicplayr", clear=["stage_uncited"])])
