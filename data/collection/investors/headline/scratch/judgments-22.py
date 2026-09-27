"""City pass on the five nameable rows the queue still asked (COLLECTION.md s6 hq_city)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write  # noqa: E402

L = [
    cls("openbucks", city="San Jose", city_src="formd_address",
        note="City: OpenBucks Corp.'s Form D business address is San Jose (EDGAR)."),
    cls("vulcun", city="San Francisco", city_src="web_verified",
        note="City: 'an American firm based in San Francisco' (SBC News, 2015-07-03)."),
    cls("mira", city="San Francisco", city_src="web_verified",
        note="City: founded in San Francisco in 2017 by Stanford programmers Jay Hack and Brandon Garcia (Very Good Light, 2020-08-14)."),
    cls("playbook", city="New York", city_src="web_verified",
        note="City: Playbook Technologies is headquartered in New York (company profiles; TechCrunch 2020-10-14 on the $9.3M round)."),
    cls("claritycare", flags=["city_unknown"],
        note="City: looked and could not place it (the site lists only an email; firstminute's post and EF's announcement name no city); Delaware-registered."),
]
if __name__ == "__main__":
    write("city-001", L, record="--dry" not in sys.argv)
