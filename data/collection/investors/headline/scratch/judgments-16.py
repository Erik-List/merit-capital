"""Stage pass, group 5 (research agent stage-5.json; 77 quotes verified, 6 behind bot
walls). Fetch's entry moves from the November 2019 Series B (a follow-on) to the 2018
round the firm's own CMS dates."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write, note_plus  # noqa: E402
from research_lib import research, rounds_of  # noqa: E402

R = research(5)
def nt(slug, extra=""):
    return note_plus(slug, (R[slug]["notes"] + (" " + extra if extra else "")).strip())
def cited(slug, stage, conf="high", date=None, **kw):
    e = R[slug]["entry"]
    return cls(slug, stage=stage, stage_src="web_verified", stage_conf=conf, stage_cite=e["url"],
               entry_date=date or e["date"], rounds=rounds_of(R[slug]), note=nt(slug), **kw)
def modeled(slug, stage, conf="medium", date=None, add="", **kw):
    return cls(slug, stage=stage, stage_src="model", stage_conf=conf, entry_date=date or R[slug]["entry"]["date"],
               rounds=rounds_of(R[slug]), note=nt(slug, add), **kw)
def und(slug, add="", **kw):
    return cls(slug, stage="undetermined", rounds=rounds_of(R[slug]), note=nt(slug, add), **kw)
def rurl(slug, word):
    return [x["url"] for x in R[slug]["rounds"] if word.lower() in (x.get("round") or "").lower() or word in (x.get("date") or "")][0]

L = [
    cited("coya", "Seed", grad="graduated", grad_src="web_verified", grad_cite=rurl("coya", "Series A")),
    cited("klima", "Seed", grad="graduated", grad_src="web_verified", grad_cite=rurl("klima", "Series A")),
    cited("podimo", "Seed", grad="graduated", grad_src="web_verified", grad_cite=rurl("podimo", "Series A")),
    cited("procure-ai", "Seed", grad="censored"), cited("searchable", "Seed", grad="censored"), cited("vox-ai", "Seed", grad="censored"),
    modeled("natural-cycles", "Seed", grad="graduated", grad_src="web_verified", grad_cite=rurl("natural-cycles", "2016-07"), flags=["stage_uncited"]),
    modeled("payflows", "Seed", grad="graduated", grad_src="web_verified", grad_cite=rurl("payflows", "Series A")),
    cited("carbonfact", "Series A"), cited("closinglock", "Series A"), cited("deepip", "Series A"),
    cited("massive", "Series A"), cited("mithrl", "Series A"), cited("notch", "Series A"), cited("honeycomb", "Series A"),
    cited("atlys", "Growth"), cited("black-forest-labs", "Growth"),
    modeled("ag5", "Seed", date="2023-03", add="The EUR 6M round Headline led (TechCrunch 2023-03-14) was AG5's first institutional round, inside the era's seed band: Seed."),
    cls("fetch", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2018-11", rounds=rounds_of(R["fetch"]),
        flags=["cite_pending", "stage_disputes_band"],
        note="Fetch (Fetch Rewards, Madison WI; founder Wes Schroll). Entry read by sequence: the firm's CMS dates it 'Early 2018' and the only 2018 round is the unnamed $8M of November 2018 (Form D, 17 investors); the $25M round that followed (Form D September 2019, announced November 2019 as the Series B led by Greycroft and e.ventures) was a follow-on, so the 2018 round is the Series A. The Form D 'Michael Kent' is Fetch's own executive officer, not Headline's partner. " + R["fetch"]["notes"]),
    und("five-lives"), und("get-harley"), und("smartfrog-canary"), und("sqldbm"), und("thread"),
    und("allermi"), und("hades"), und("viabill"),
    und("bettercloud", status="acquired", add="Status: acquired by CoreStack, March 2026, after Vista Equity's 2022 majority stake."),
]
if __name__ == "__main__":
    write("stage-006", L, record="--dry" not in sys.argv)
