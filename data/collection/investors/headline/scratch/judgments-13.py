"""Stage pass, group 3 (research agent stage-3.json; 87 of 92 quotes verified on the
page, 5 behind publisher bot walls). Named round + firm on one page -> web_verified;
a round named by sequence or across two pages -> model with the deal named."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write, note_plus  # noqa: E402
from research_lib import research, rounds_of  # noqa: E402

R = research(3)
def cited(slug, stage, conf="high", date=None, **kw):
    e = R[slug]["entry"]
    return cls(slug, stage=stage, stage_src="web_verified", stage_conf=conf, stage_cite=e["url"],
               entry_date=date or e["date"], rounds=rounds_of(R[slug]),
               note=note_plus(slug, R[slug]["notes"]), **kw)
def modeled(slug, stage, conf="medium", date=None, **kw):
    return cls(slug, stage=stage, stage_src="model", stage_conf=conf, entry_date=date or R[slug]["entry"]["date"],
               rounds=rounds_of(R[slug]), note=note_plus(slug, R[slug]["notes"]), **kw)
def rurl(slug, word):
    return [x["url"] for x in R[slug]["rounds"] if word.lower() in (x.get("round") or "").lower() or word in (x.get("date") or "")][0]

L = [
    cited("jow", "Seed", grad="graduated", grad_src="web_verified", grad_cite=rurl("jow", "Series A")),
    cited("aiprise", "Series A"), cited("apiax", "Series A"),
    cited("attio", "Seed", grad="graduated", grad_src="web_verified", grad_cite=rurl("attio", "Series A")),
    cited("bioptimus", "Seed"), cited("blossom-health", "Series A"), cited("codesignal", "Series A"),
    cited("dbeaver", "Seed"), cited("helcim", "Growth"), cited("mine", "Series A"), cited("monta", "Series A"),
    cited("netbox-labs", "Growth"),
    cited("numa", "Seed", grad="graduated", grad_src="web_verified", grad_cite=rurl("numa", "2021-03")),
    cited("planradar", "Series A"), cited("shopmonkey", "Series A"), cited("upheal", "Series A"),
    cited("gopuff", "Growth", conf="medium"),
    cited("leapwork", "Series A", conf="medium", date="2019"),
    modeled("flockjay", "Series A"),
    modeled("karma", "Seed", date="2018-02", grad="graduated", grad_src="web_verified", grad_cite=rurl("karma", "Series A")),
    modeled("sorare", "Seed", grad="graduated", grad_src="web_verified", grad_cite=rurl("sorare", "Series A")),
    modeled("staffbase", "Growth"),
    modeled("vizzia", "Series A", date="2025-09"),
    modeled("weavr", "Seed", conf="low", date="2021", flags=["stage_uncited"],
            grad="graduated", grad_src="web_verified", grad_cite=rurl("weavr", "Series A")),
    cls("powerus", rounds=rounds_of(R["powerus"]), note=note_plus("powerus", R["powerus"]["notes"])),
    cls("recursive", rounds=rounds_of(R["recursive"]), note=note_plus("recursive", "Entry round: " + R["recursive"]["notes"])),
    cls("circadia", rounds=rounds_of(R["circadia"]), note=note_plus("circadia", R["circadia"]["notes"])),
    cls("fancy", rounds=rounds_of(R["fancy"]), note=note_plus("fancy", R["fancy"]["notes"])),
]
if __name__ == "__main__":
    write("stage-003", L, record="--dry" not in sys.argv)
