"""Graduation on the delta's Seed rows (graduation-surfaces.py 2026-09-27, 39 lookups,
none failed; Form D layer for Housecall Pro and Nom Nom)."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write, note_plus  # noqa: E402

ASOF = "2026-09-27"
G = json.loads((Path(__file__).resolve().parent / "graduation-surfaces.json").read_text())
FIRM = "firm: Headline CMS, posts, Substack archive and the e.ventures logo wall -> no later round named"
def lines(slug, formd=None, showed=None):
    showed = showed or {}
    s = [FIRM] + [f"{svc}: {v['query']} -> {showed.get(svc, str(v['n']) + ' items, none naming a later round of this company')}" for svc, v in G[slug]["surfaces"].items()]
    if formd:
        s.append("formd: " + formd)
    return s
def no(slug, src="absence_check", cite=None, formd=None, showed=None, text=""):
    return cls(slug, grad="not_graduated", grad_src=src, grad_cite=cite, grad_asof=ASOF, surfaces=lines(slug, formd, showed),
               note=note_plus(slug, text) if text else None)

L = [
    cls("housecall-pro", grad="graduated", grad_src="formd", entry_date="2013-07-26",
        note=note_plus("housecall-pro", "Graduation from its own Form D sequence (Codefied Inc.): $1.5M entry (2013-07-26), then $8.2M (2015q3).")),
    cls("nom-nom", grad="graduated", grad_src="formd", entry_date="2016-08-01",
        note=note_plus("nom-nom", "Graduation from its own Form D sequence (NomNomNow Inc.): $3.29M entry (first sale 2016-08-01), then $10.0M (2017-12). Mars bought it in 2022 (reported near $1B).")),
    no("mira", src="web_verified", cite="https://cosmeticsbusiness.com/birchbox-acquired-by-beauty-and-healthcare-start-up-femtec-health-for-45m--180281", formd="Mira Beauty: no Form D filer found -> no later US offering on file",
       text="Graduation: the only later round, $9.0M of growth funding (September 2020), is unnamed and just under twice the $4.53M seed ($9.06M), so the step-up fails; FemTec Health bought Mira in October 2021, ending the chance to raise."),
    no("asap54", src="web_verified", cite="https://find-and-update.company-information.service.gov.uk/company/08411914",
       text="Graduation: no later round than the 2014 raise (about $3.8M in all); ASAP54.COM LIMITED was dissolved (Companies House)."),
    cls("cuponation", grad="graduated", grad_src="web_verified", grad_cite="https://www.deutsche-startups.de/2015/12/10/rockets-cuponation-holt-sich-10-mill",
        note=note_plus("cuponation", "Graduation: CupoNation's EUR 10M round of December 2015 (Rocket Internet, Holtzbrinck, NEA, e.ventures and others) clears the step-up on an unknown seed (era ceiling $2.5M, so $5M).")),
    cls("admoment", stage="undetermined",
        note=note_plus("admoment", "Stage: e.ventures backed AdMoment 'from its creation' (rb.ru) and joined Prostor Capital's $3M round of November 2013, but the founding round's date and amount are not on record, so the entry cannot be staged or its graduation decided.")),
    no("fight-my-monster", showed={"googlenews": "the $2.1M seed (Silicon Republic 2012-02-16); nothing later", "googlenews_local": "the same 2012 seed; nothing later"}),
    no("mapia", showed={"techcrunch": "'German funds target Ukraine with new investments' (2009-07-14), the entry; nothing later"}),
    no("ahara", formd="Ahara: no Form D filer found -> no later US offering on file",
       showed={"googlenews": "the $10M+ seed (PR Newswire, Athletech News, June 2023; LA Business Journal July 2023); nothing later",
               "googlenews_firm": "the same seed coverage; nothing later"}),
    no("soldsie", formd="Soldsie: no Form D filer found -> no later US offering on file",
       showed={"googlenews": "the $1M seed (March 2013) and the $425K crowdfunded round (January 2013); nothing later",
               "techcrunch": "'Soldsie Raises $425K' (2013-01-09) before the seed; nothing later"}),
]
if __name__ == "__main__":
    write("grad-002", L, record="--dry" not in sys.argv)
