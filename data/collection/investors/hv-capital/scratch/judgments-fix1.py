import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write  # noqa
L=[cls("onlinetours", status="private",
       note="Online travel agency onlinetours.ru, Moscow (founded 2012). HV entered 2014-03; still on the 2022-25 lists as a "
            "growth holding, and Headline's book holds it as private. The round is not named.")]
write("fix-001", L)
