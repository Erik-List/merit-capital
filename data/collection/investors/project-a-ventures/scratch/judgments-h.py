"""Batch H (PRO-102): the firm's own stage fields, promoted at medium (decisions.md R2), label the rows
no documented round covers; rows recorded earlier with an uncited stage are upgraded (note-free patches)."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as J  # noqa: E402
from judge_lib import cls, write, LISTING, surfaces_lines, ASOF, sc, RS, WHO  # noqa: E402
from judge_lib import rrounds as rounds  # noqa: E402

V = json.loads((J.H / "visible-research.json").read_text())["companies"]


def cf_cite(slug, key="cf_investment"):
    """The earliest archived capture stating the firm's round word."""
    vals = J.fields(slug, key) or J.fields(slug, "page_investment")
    return vals[0][1]


L = []


def upgrade(slug, stage, cite, drop_grad=False):
    r = {"slug": slug, "who": WHO, "entry_stage": stage, "entry_stage_source": "first_party",
         "entry_stage_confidence": "medium", "entry_stage_citation": cite, "clear_flags": ["stage_uncited"]}
    if drop_grad:
        r.update({"seed_to_a_graduation": None, "graduation_source": None, "graduation_asof": None,
                  "graduation_surfaces": None, "graduation_citation": None})
    L.append(r)


upgrade("tirendo", "Seed", LISTING)
upgrade("tictail", "Seed", LISTING)
upgrade("ello", "Seed", LISTING)
upgrade("mimo", "Seed", LISTING)
upgrade("pets-deli", "Seed", cf_cite("pets-deli"))
upgrade("amazd", "Seed", cf_cite("amazd"))
upgrade("cosmic-lounge", "Pre-Seed", LISTING, drop_grad=True)

L.append(cls("coureon", status="acquired", rng="below_1b", stage="Seed", stage_src="first_party", stage_conf="medium",
             stage_cite=cf_cite("coureon"), entry_date="2015-01", grad="not_graduated", grad_src="web_verified",
             grad_cite=sc("coureon"), grad_asof=ASOF,
             surfaces=surfaces_lines("coureon", "no round after Project A's 2015 founding capital; sold to UB Tech in 2018"),
             country="DE", city="Berlin", country_cite=cf_cite("coureon", "cf_location"), focus="SaaS",
             extra={"status_citation": sc("coureon")},
             note="Multi-carrier shipping software for online merchants, Berlin: a Project A company build (founded January "
                  "2015; Project A held about 71%, Deutsche Startups 2015), seed by the firm's own record (archive: Seed, "
                  "2015-01; an incubation, D6). acq. by UB Tech (United Broker), June 2018 (the firm's release), with no later "
                  "round.", rounds=rounds("coureon")))
L.append(cls("kyrall", status="private", rng="below_1b", stage="Pre-Seed", stage_src="first_party", stage_conf="medium",
             stage_cite=LISTING, entry_date="2025", country="DE", city="Munich", country_cite=LISTING,
             focus="AI & Applied AI", extra={"status_citation": sc("kyrall")},
             note="AI automation of functional 3D part design (CAD), Munich (Kyrall GmbH, registered April 2025). Pre-seed "
                  "2025 from Fund IV by the firm's own record, the only source for the round; launched its AI CAD modeller in "
                  "July 2026 (Develop3D).", rounds=rounds("kyrall")))
L.append(cls("scipio", status="private", rng="below_1b", stage="Pre-Seed", stage_src="first_party", stage_conf="medium",
             stage_cite=LISTING, entry_date="2025", country="DE", city="Berlin", country_cite=sc("scipio"),
             focus="Industrial & Robotics", extra={"status_citation": sc("scipio")},
             note="Defence logistics software (resupply planning for armed forces; Scipio Networks GmbH), Berlin, registered "
                  "at Project A's own address. Pre-seed 2025 from Fund IV by the firm's own record, the only source for the "
                  "round; a Thales partnership in June 2026.", rounds=rounds("scipio")))

U = V["Uberall"]
L.append(cls("uberall", status="private", rng="below_1b", stage="Seed", stage_src="first_party", stage_conf="medium",
             stage_cite=LISTING, entry_date="2012", grad="graduated", grad_src="web_verified", grad_cite=U["rounds"][1]["source"],
             country="DE", city="Berlin", country_cite=LISTING, focus="SaaS", flags=["model_disputes_source"],
             note="Location and review marketing platform, Berlin (founded 2012). Seed 2012 from Fund I by the firm's own "
                  "record (CMS; the firm's 2013 gallery lists it), no release of that round found; the $25M Series B of Feb "
                  "2018 with Project A graduates the row (tech.eu). $115M Series C in 2021 at about $500M (TechCrunch). The "
                  "Wikidata join confirmed DE.",
             rounds=[J.rnd(r.get("date"), r.get("round"), r.get("amount_usd"), r.get("lead"), r.get("firm_in_round"),
                           r.get("source") or None) for r in U["rounds"]]))
K = V["Knowunity"]
L.append(cls("knowunity", status="private", rng="below_1b", stage="Seed", stage_src="first_party", stage_conf="medium",
             stage_cite=LISTING, entry_date="2021-04", grad="graduated", grad_src="web_verified", grad_cite=K["rounds"][1]["source"],
             country="DE", city="Berlin", country_cite=LISTING, focus="Consumer & Marketplaces",
             note="Student learning app, Berlin (founded 2020). Seed 2021 by the firm's own record (CMS: Fund III, 2021; the "
                  "firm's post 'Our investment in Knowunity', April 2021, names no round); the EUR 10M Series A of May 2022, "
                  "with Project A, graduates the row (tech.eu). Series B 2025.",
             rounds=[J.rnd(r.get("date"), r.get("round"), r.get("amount_usd"), r.get("lead"), r.get("firm_in_round"),
                           r.get("source") or None) for r in K["rounds"]]))

if __name__ == "__main__":
    write("batch-h", L)
