"""Grind batch N (PRO-102): store2be and Toroleo from research-g4.json; Kyto and Loopline revised under R3."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as J  # noqa: E402
from judge_lib import cls, write, LISTING, surfaces_lines, ASOF, ec, sc, gc, RS  # noqa: E402
from judge_lib import rrounds as rounds  # noqa: E402

L = []


def cfcap(slug, key="cf_investment"):
    v = J.fields(slug, key) or J.fields(slug, "page_investment")
    return v[0][1]


L.append(cls("store2be", status="defunct", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("store2be"), entry_date="2016-07", grad="not_graduated", grad_src="web_verified",
             grad_cite="https://www.deutsche-startups.de/2020/09/09/store2be-offline/", grad_asof=ASOF,
             surfaces=surfaces_lines("store2be", "after the July 2016 seed only unnamed seven-figure rounds (2018, about EUR 2M "
                                                 "by the firm's own EUR 3M total; Feb 2020, 'siebenstellig', no figure), none "
                                                 "shown above the step-up bar (R3); operations stopped in Sept 2020"),
             country="DE", city="Berlin", country_cite=LISTING if J.live("store2be") else cfcap("store2be", "cf_location"),
             focus="Consumer & Marketplaces", extra={"status_citation": sc("store2be")},
             note="Booking marketplace for promotion, pop-up and event spaces, Berlin (founded 2015). 'Seed Funding: Project A, "
                  "GFC and Strategic Business Angels Announce Joint Investments in store2be', its first round (the firm's post, "
                  "July 2016). Later rounds were unnamed and seven-figure (2018; Feb 2020 with Signa); the company stopped "
                  "operating in Sept 2020 and went into liquidation (Deutsche Startups; North Data): defunct, not graduated (R3).",
             rounds=rounds("store2be")))
L.append(cls("toroleo", status="acquired", rng="below_1b", stage="Seed", stage_src="first_party", stage_conf="medium",
             stage_cite=LISTING, entry_date="2012", grad="not_graduated", grad_src="web_verified", grad_cite=sc("toroleo"),
             grad_asof=ASOF,
             surfaces=surfaces_lines("toroleo", "after the 2012 founding capital only Creathor's 2013 investment of unstated "
                                                "size (R3); Delticom took the business over in August 2014"),
             country="DE", city="Berlin", country_cite=LISTING, focus="Consumer & Marketplaces",
             extra={"status_citation": sc("toroleo")},
             note="Tyre and car-parts price comparison, Berlin (launched 2012), a Project A build ('der Kfz-Preisvergleich aus "
                  "dem Hause Project A', Deutsche Startups); seed by the firm's own record (CMS, Fund I). Creathor invested in 2013 "
                  "without a stated amount; Delticom took over the business in August 2014 (Deutsche Startups): acquired, not "
                  "graduated (R3).", rounds=rounds("toroleo")))
L.append({"slug": "kyto", "who": J.WHO, "entry_stage": "Seed", "entry_stage_source": "first_party",
          "entry_stage_confidence": "medium", "entry_stage_citation": cfcap("kyto"), "entry_date": "2013-09",
          "seed_to_a_graduation": "not_graduated", "graduation_source": "absence_check", "graduation_asof": ASOF,
          "graduation_surfaces": surfaces_lines("kyto", "after the 2013 seed only the Oct 2015 round with Müller Medien, "
                                                        "of unstated size (R3)")})
L.append({"slug": "loopline", "who": J.WHO, "entry_stage": "Seed", "entry_stage_source": "first_party",
          "entry_stage_confidence": "medium", "entry_stage_citation": LISTING, "entry_date": "2014",
          "seed_to_a_graduation": "not_graduated", "graduation_source": "absence_check", "graduation_asof": ASOF,
          "graduation_surfaces": surfaces_lines("loopline", "after the 2014 seed only unnamed rounds of unstated size (a "
                                                            "second round in 2016, a seven-digit round in 2018) (R3)")})

if __name__ == "__main__":
    write("batch-n", L)
