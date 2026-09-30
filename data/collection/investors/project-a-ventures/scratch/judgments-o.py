"""Grind batch O (PRO-102): the last rows from research-g4.json."""
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


L.append(cls("valve", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("valve"), entry_date="2022-09", grad="not_graduated", grad_src="absence_check", grad_asof=ASOF,
             surfaces=surfaces_lines("valve", "no round after the September 2022 seed; no allotment in the register since May 2022"),
             country="GB", city="London", country_cite=LISTING, focus="SaaS",
             note="Sales and distribution software for flexible-workspace operators (Valve Space Ltd), London (founded 2018). 'A "
                  "$4.5M seed funding round led by Project A with participation from Discovery Ventures' (the company's release, "
                  "Sept 2022). No later round; Companies House shows no allotment since.", rounds=rounds("valve")))
L.append(cls("wonderbly", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("wonderbly"), entry_date="2016-06", country="GB", city="London", country_cite=LISTING,
             focus="Consumer & Marketplaces", extra={"status_citation": sc("wonderbly")},
             note="Personalised children's books (Lost My Name until 2017), London (founded 2012). 'With this extension of the "
                  "Series A round, Project A joins the circle of renowned international investors, including lead investor "
                  "Google Ventures' (the firm's post, June 2016; EUR 4M). Sold to Graphite Capital in July 2021 and to Penguin "
                  "Random House in June 2025 (PRH's announcement).", rounds=rounds("wonderbly")))
L.append(cls("keatz", status="defunct", rng="below_1b", stage="Seed", stage_src="first_party", stage_conf="medium",
             stage_cite=cfcap("keatz"), entry_date="2016-09", grad="graduated", grad_src="web_verified",
             grad_cite=RS["keatz"]["rounds"][2]["source"], country="DE", city="Berlin", country_cite=LISTING if J.live("keatz") else cfcap("keatz", "cf_location"),
             focus="Consumer & Marketplaces", extra={"status_citation": sc("keatz")},
             note="Salad delivery GreenGurus turned ghost-kitchen chain Keatz, Berlin (founded 2015). 'Ende 2016 investierte "
                  "Project A in das Startup' (Deutsche Startups, 2018), a seed by the firm's own record. The unnamed EUR 12M "
                  "round of March 2019 (about $13.5M, TechCrunch) clears the $8M step-up bar for a 2016 seed of unknown size "
                  "and graduates the row. In liquidation since 2022-10-06 (North Data): defunct.", rounds=rounds("keatz")))

if __name__ == "__main__":
    write("batch-o", L)
