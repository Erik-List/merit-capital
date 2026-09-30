"""Grind batch A (PRO-102): rows from research-g0/g3 (every URL re-loaded by the research agents)."""
import glob
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write, LISTING, rnd, surfaces_lines, firm_cite, ASOF  # noqa: E402

H = Path(__file__).resolve().parent
RS = {}
for f in glob.glob(str(H / "research-g[0-9].json")):
    RS.update(json.load(open(f)))


def rounds(slug):
    return [rnd(r.get("date"), r.get("round"), r.get("amount_usd"), r.get("lead"), r.get("firm_in_round"),
                r.get("source") if str(r.get("source") or "").startswith("http") else None, r.get("source_type") or "press")
            for r in RS[slug].get("rounds") or []]


def ec(slug):
    return RS[slug]["entry"]["citation"]


def sc(slug):
    return RS[slug]["status_citation"]


def gc(slug):
    return RS[slug]["graduation"]["citation"]


L = []

L.append(cls("42matters", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="medium",
             stage_cite=ec("42matters"), entry_date="2013", country="CH", city="Zurich", country_cite=LISTING,
             focus="Data Infrastructure", extra={"status_citation": sc("42matters")},
             note="App-store and CTV app intelligence data, Zurich (ETH spin-off, founded 2011). The firm's own post of "
                  "2014-01-28: '42matters AG has secured a 7-digit Series A round ... with Project A Ventures joining the "
                  "existing Austrian investor Gamma Capital'; the firm's 2013 page already lists it and its CMS says seed "
                  "2012, a firm-field disagreement the post settles. acq. by Similarweb, 2024 (Similarweb's announcement).",
             rounds=rounds("42matters")))

L.append(cls("comtravo", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("comtravo"), entry_date="2017-07", country="DE", city="Berlin", country_cite=LISTING, focus="SaaS",
             extra={"status_citation": sc("comtravo")},
             note="AI business-travel booking for SMEs, Berlin (founded 2015). 'Comtravo closed an EUR 8.5 million Series A "
                  "financing round co-led by Berlin-based VC Project A and Swedish VC fund Creandum' (the firm's own release, "
                  "2017); Series B 2019-20 with Project A. acq. by TripActions (now Navan), 2022 (Crunchbase News); Project A's "
                  "Navan shares are sale consideration (the navan row, not_member).", rounds=rounds("comtravo")))

L.append(cls("architect", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("architect"), entry_date="2025-09", grad="censored", country="GB", city="London",
             country_cite=LISTING, focus="AI & Applied AI",
             extra={"valuation_range_source": "web_verified", "valuation_citation": sc("architect"), "valuation_asof": ASOF},
             note="Agentic website platform (Architect AI), London (founded 2024). 'That's why we led Architect AI's $4.75M "
                  "seed round' (the firm's post, 2025-09-09); inside the 24-month window, so censored. Momentum-slice check "
                  "2026-09-30: no later round, no valuation figure.", rounds=rounds("architect")))

L.append(cls("enapi", status="private", rng="below_1b", stage="Pre-Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("enapi"), entry_date="2024-03", country="DE", city="Berlin", country_cite=LISTING,
             focus="Climate & Energy",
             note="EV-charging roaming and payments infrastructure, Berlin (founded 2023, out of the Project A Studio). The "
                  "EUR 2.5M pre-seed of March 2024 was 'provided by Project A Ventures, Seedcamp, and HelloWorld' (Mercom); a "
                  "EUR 7.5M seed led by Voyager Ventures followed in Jan 2025.", rounds=rounds("enapi")))

L.append(cls("gabi", status="acquired", rng="below_1b", stage="Pre-Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("gabi"), entry_date="2016", country="US", city="San Francisco", country_cite=LISTING,
             focus="Fintech & Payments", flags=["model_disputes_source"], extra={"status_citation": sc("gabi")},
             note="Insurance comparison (insurtech), San Francisco (founded 2016). 'Project A successfully exits the insurtech "
                  "company after having first invested at pre-seed stage five years ago' (the firm's post, 2021-11-22; the "
                  "CMS says seed 2017). acq. by Experian for $320M, 2021. The Wikidata join (a Czech company, defunct, 1997) "
                  "was a namesake and is replaced.", rounds=rounds("gabi")))

L.append(cls("anyline", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("anyline"), entry_date="2020-01", country="AT", city="Vienna", country_cite=LISTING,
             focus="AI & Applied AI",
             note="Mobile OCR and data capture, Vienna (founded 2013). The $12M Series A of Jan 2020 was 'led by Berlin-based "
                  "Project A' (tech.eu), its first round in the company; $20M growth round July 2021.", rounds=rounds("anyline")))

L.append(cls("aula", status="acquired", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("aula"), entry_date="2018-04", grad="not_graduated", grad_src="absence_check", grad_asof=ASOF,
             surfaces=surfaces_lines("aula", "no round after the April 2018 seed; the platform was sold to Coventry "
                                             "University Group in January 2022"),
             country="GB", city="London", country_cite=LISTING, focus="SaaS", extra={"status_citation": sc("aula")},
             note="Communication platform for universities, London (founded 2016). Project A co-led the $4.2M seed of April "
                  "2018 with Brighteye and Sunstone, 'with participation from existing investors such as Nordic Makers' (the "
                  "firm's own release). No later round; the platform went to Coventry University Group in January 2022 and "
                  "the old company was renamed and solvently wound up (an asset sale: acquired).", rounds=rounds("aula")))

L.append(cls("cosmic-lounge", status="private", rng="below_1b", stage="Seed", stage_src="model", stage_conf="low",
             entry_date="2023-04", grad="not_graduated", grad_src="absence_check", grad_asof=ASOF,
             surfaces=surfaces_lines("cosmic-lounge", "no round after the EUR 4M seed of April 2023"),
             country="FI", city="Helsinki", country_cite=LISTING, focus="Media, Gaming & Advertising", flags=["stage_uncited"],
             note="Mobile games studio, Helsinki (founded 2022). The EUR 4M seed of April 2023 was led by Transcend after a 2022 "
                  "pre-seed by Sisu (gamesindustry.biz); no press names Project A, whose logo was added to the company's "
                  "investor wall in April 2023 beside Transcend's (the firm's CMS: Fund IV, 2023, pre_seed; archive: Seed). The "
                  "stage rests on that match and is uncited; the no rests on the dated search.", rounds=rounds("cosmic-lounge")))

if __name__ == "__main__":
    write("batch-a", L)
