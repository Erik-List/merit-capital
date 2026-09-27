"""Stage pass, group 4 (research agent stage-4.json; 74 of 81 quotes verified on the
page, 7 behind bot walls or SEC)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write, note_plus  # noqa: E402
from research_lib import research, rounds_of  # noqa: E402

R = research(4)
def nt(slug, extra=""):
    return note_plus(slug, (R[slug]["notes"] + (" " + extra if extra else "")).strip())
def cited(slug, stage, conf="high", date=None, **kw):
    e = R[slug]["entry"]
    return cls(slug, stage=stage, stage_src="web_verified", stage_conf=conf, stage_cite=e["url"],
               entry_date=date or e["date"], rounds=rounds_of(R[slug]), note=nt(slug), **kw)
def modeled(slug, stage, conf="medium", date=None, **kw):
    return cls(slug, stage=stage, stage_src="model", stage_conf=conf, entry_date=date or R[slug]["entry"]["date"],
               rounds=rounds_of(R[slug]), note=nt(slug), **kw)
def rurl(slug, word):
    return [x["url"] for x in R[slug]["rounds"] if word.lower() in (x.get("round") or "").lower() or word in (x.get("date") or "")][0]
def und(slug, **kw):
    return cls(slug, stage="undetermined", rounds=rounds_of(R[slug]), note=nt(slug), **kw)

L = [
    cited("adapt", "Seed", date="2026-01", grad="censored"),
    cited("asana-rebel", "Series A"), cited("copa90", "Series A"),
    cited("automaited", "Seed"),
    cited("claap", "Pre-Seed"),
    cited("deblock", "Seed", conf="medium", grad="graduated", grad_src="web_verified", grad_cite=rurl("deblock", "Series A")),
    cited("first-aml", "Growth"), cited("gorilla", "Growth"),
    cited("homa", "Seed", grad="graduated", grad_src="web_verified", grad_cite=rurl("homa", "Series A")),
    cited("kili-technology", "Seed", grad="graduated", grad_src="web_verified", grad_cite=rurl("kili-technology", "Series A")),
    cited("mistral", "Seed", grad="graduated", grad_src="web_verified", grad_cite=rurl("mistral", "Series A")),
    cited("motion", "Seed", grad="graduated", grad_src="web_verified", grad_cite=rurl("motion", "Series A")),
    cited("tabnine", "Series A"),
    cited("voicea", "Series A", conf="medium"),
    cited("zive", "Pre-Seed"),
    cited("skalar", "Seed", conf="medium", date="2026-07", grad="censored"),
    modeled("brumbrum", "Series A"),
    modeled("primo", "Seed", date="2023-04", grad="graduated", grad_src="web_verified", grad_cite=rurl("primo", "2026-09"),
            country="DK", country_src="model_knowledge", flags=["model_disputes_source"]),
    modeled("sparetech", "Seed", date="2021-10", grad="graduated", grad_src="web_verified", grad_cite=rurl("sparetech", "Series A")),
    und("friendsurance", status="acquired"),
    und("air"), und("bitwarden"), und("linc"), und("palmstreet"), und("plumery"), und("robco"), und("verse-medical"),
    cls("nom-nom", rounds=rounds_of(R["nom-nom"]), note=nt("nom-nom", "Stage from the merged NomNomNow Form D sequence at the rebuild.")),
]
if __name__ == "__main__":
    write("stage-004", L, record="--dry" not in sys.argv)
