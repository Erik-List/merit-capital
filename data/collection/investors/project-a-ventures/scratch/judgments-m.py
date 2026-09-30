"""Grind batch M (PRO-102): rows from research-g4.json (every URL re-loaded by the research agent)."""
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


def rsrc(slug, i):
    return RS[slug]["rounds"][i]["source"]


L.append(cls("mindfuel", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("mindfuel"), entry_date="2024-03", grad="not_graduated", grad_src="absence_check", grad_asof=ASOF,
             surfaces=surfaces_lines("mindfuel", "no round after the March 2024 seed"),
             country="DE", city="Munich", country_cite=LISTING, focus="SaaS",
             note="Data and AI use-case management software (Delight), Munich (founded 2020). 'Mindfuel announces the closing of "
                  "a EUR 3.75m seed funding round led by Project A Ventures' (the company, March 2024), with business angels. No "
                  "later round; the consulting unit was sold in 2025 (a unit sale, not the company).", rounds=rounds("mindfuel")))
L.append(cls("natue", status="acquired", rng="below_1b", stage="Seed", stage_src="first_party", stage_conf="medium",
             stage_cite=cfcap("natue"), entry_date="2012", grad="graduated", grad_src="web_verified", grad_cite=rsrc("natue", 1),
             country="BR", city="São Paulo", country_cite=cfcap("natue", "cf_location"), focus="Consumer & Marketplaces",
             extra={"status_citation": sc("natue")},
             note="Online shop for natural and wellness products, São Paulo, a Project A company build: 'O primeiro aporte da "
                  "Natue veio da Project A Ventures' (Exame, 2013); seed 2012 by the firm's own record. The unnamed BRL 16M round "
                  "of June 2013 (about $7.5M, Exame) clears the $5M step-up bar for a 2012 seed of unknown size and graduates "
                  "the row. acq. by Mundo Verde, Oct 2018, buying out Project A (ImpactAlpha).", rounds=rounds("natue")))
L.append(cls("nu3", status="acquired", rng="below_1b", stage="Seed", stage_src="first_party", stage_conf="medium",
             stage_cite=LISTING, entry_date="2012-03", grad="graduated", grad_src="web_verified", grad_cite=rsrc("nu3", 4),
             country="DE", city="Berlin", country_cite=LISTING, focus="Consumer & Marketplaces",
             extra={"status_citation": sc("nu3")},
             note="Online shop and own brands for supplements and functional food, Berlin (founded 2011). Project A took about "
                  "39% in spring 2012 (Deutsche Startups), a seed by the firm's own record (CMS, Fund I); the unnamed EUR 8M round "
                  "of Nov 2016 (about $8.8M, Deutsche Startups) clears the $5M step-up bar and graduates the row. acq. by Shop "
                  "Apotheke Europe (now Redcare Pharmacy) for shares and cash, July 2018.", rounds=rounds("nu3")))
L.append(cls("peergrade", status="acquired", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("peergrade"), entry_date="2017-12", grad="not_graduated", grad_src="web_verified",
             grad_cite=sc("peergrade"), grad_asof=ASOF,
             surfaces=surfaces_lines("peergrade", "no round after the December 2017 seed; the product became Eduflow, bought by "
                                                  "Multiverse in 2023"),
             country="DK", city="Copenhagen", country_cite=cfcap("peergrade", "cf_location"), focus="SaaS",
             extra={"status_citation": sc("peergrade")},
             note="Peer-feedback software for teachers (later Eduflow), Copenhagen (DTU spin-out, 2015; YC S17). The $1.5M seed "
                  "'from Y Combinator, byFounders, Project A, Nordic Makers' (EdSurge, Dec 2017). No later round; the team "
                  "replaced Peergrade with Eduflow in 2020 and Multiverse acquired Eduflow in May 2023 (UKTN).",
             rounds=rounds("peergrade")))
L.append(cls("procompra", status="defunct", rng="below_1b", stage="Seed", stage_src="first_party", stage_conf="medium",
             stage_cite=cfcap("procompra"), entry_date="2014-10", grad="not_graduated", grad_src="web_verified",
             grad_cite=sc("procompra"), grad_asof=ASOF,
             surfaces=surfaces_lines("procompra", "no round after the October 2014 seed; the company was wound up in December "
                                                  "2016"),
             country="BR", city="São Paulo", country_cite=cfcap("procompra", "cf_location"), focus="Consumer & Marketplaces",
             extra={"status_citation": sc("procompra")},
             note="B2B marketplace matching small businesses with suppliers for quotes, São Paulo (founded 2014), a Project A "
                  "company build: its majority shareholders 'Project-A Ventures e Costa Family Office' made 'um aporte inicial de "
                  "1 milhão de euros' (Projeto Draft, 2015); seed by the firm's own record. The company's registration was closed "
                  "by voluntary winding-up on 2016-12-20 (Brazilian CNPJ register): defunct.", rounds=rounds("procompra")))
L.append(cls("qunomedical", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("qunomedical"), entry_date="2016-03", grad="graduated", grad_src="web_verified",
             grad_cite=gc("qunomedical"), country="DE", city="Berlin", country_cite=cfcap("qunomedical", "cf_location"),
             focus="Healthcare & Bio",
             note="Medical-travel platform turned patient-relationship software (Junomedical until 2017), Berlin (founded 2015). "
                  "'Junomedical has received its seed funding from Berlin-based Project A' (the firm's post, April 2016); the "
                  "EUR 10M Series A of Nov 2022 graduates the row (DvH Ventures).", rounds=rounds("qunomedical")))
L.append(cls("resi", status="private", rng="below_1b", stage="Series A", stage_src="first_party", stage_conf="medium",
             stage_cite=LISTING, entry_date="2019-12", country="GB", city="London", country_cite=LISTING,
             focus="Consumer & Marketplaces", flags=["model_disputes_source"],
             note="Online architecture service for UK home extensions (Resi Design Ltd), London (founded 2016 by the Hassle.com "
                  "founders). Series A 2019 by the firm's own record (CMS, Fund III); Companies House shows the Dec 2019 allotment "
                  "of 5,106 shares at GBP 926.03 (about GBP 4.7M) that the round consisted of. Media-for-equity from ITV 2023, a "
                  "round at a GBP 20M valuation in 2024. The Wikidata join confirmed GB.", rounds=rounds("resi")))

if __name__ == "__main__":
    write("batch-m", L)
