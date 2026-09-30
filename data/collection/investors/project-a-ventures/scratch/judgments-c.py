"""Grind batch C (PRO-102): rows from research-g*.json (every URL re-loaded by the research agents)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write, LISTING, surfaces_lines, ASOF, ec, sc, gc, RS  # noqa: E402
from judge_lib import rrounds as rounds  # noqa: E402

L = []
NOVAL = {"valuation_source": None, "valuation_asof": None, "valuation_confidence": None}

L.append(cls("pactum", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("pactum"), entry_date="2020-06", grad="graduated", grad_src="web_verified", grad_cite=gc("pactum"),
             country="US", city="Mountain View", country_src="formd_address", focus="AI & Applied AI",
             flags=["stage_disputes_band"],
             note="Autonomous contract negotiation for procurement, Mountain View (founded in Estonia, 2019). Project A led the "
                  "$3M seed of June 2020 (tech.eu; the firm's 'why we invested' post the next day); the $11M Series A of May "
                  "2021 led by Atomico graduates the row. The Form D band read the 2021 filing (the Series A) as the entry; the "
                  "seed never filed. $54M Series C led by Insight, June 2025.", rounds=rounds("pactum")))
L.append(cls("mimo", status="private", rng="below_1b", stage="Seed", stage_src="model", stage_conf="medium",
             entry_date="2025-03", grad="censored", country="GB", city="London", country_cite=ec("mimo"),
             focus="Fintech & Payments",
             note="SME payments and embedded credit (Omim Technology Ltd), London, founded 2023 by Swedish founders. 'The round "
                  "was led by new investor Project A' (UKTN, March 2025): a GBP 6.6M round eleven months after the seed "
                  "Northzone led, unnamed in the press; the firm's CMS files it as seed, so the entry reads as the seed's "
                  "extension. Inside the 24-month window: censored. The CMS HQ Stockholm is the founders' origin.",
             rounds=rounds("mimo")))
L.append(cls("quix", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("quix"), entry_date="2021-05", grad="graduated", grad_src="web_verified", grad_cite=gc("quix"),
             country="GB", city="London", country_cite=LISTING, focus="Data Infrastructure",
             note="Python stream-processing platform, London (founded 2020 by ex-McLaren engineers). The GBP 2.3M seed of May "
                  "2021 was 'led by Project A Ventures' (TechCrunch); the $12.9M Series A led by MMC Ventures, Nov 2022, "
                  "graduates the row.", rounds=rounds("quix")))
L.append(cls("montamo", status="private", rng="below_1b", stage="Pre-Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("montamo"), entry_date="2023-12", country="DE", city="Berlin", country_cite=LISTING,
             focus="Climate & Energy",
             note="Trains and employs heat-pump and green-energy installers, Berlin (founded Nov 2023 out of the Project A "
                  "Studio). 'A EUR 2.1 million pre-seed round, led by Project A Ventures' (TechCrunch, Dec 2023); a EUR 6M seed "
                  "led by firstminute followed in April 2025.", rounds=rounds("montamo")))
L.append(cls("pets-deli", status="acquired", rng="below_1b", stage="Seed", stage_src="model", stage_conf="low",
             entry_date="2015", grad="graduated", grad_src="web_verified", grad_cite=ec("pets-deli"),
             country="DE", city="Berlin", country_cite=LISTING, focus="Consumer & Marketplaces", flags=["stage_uncited"],
             extra={"status_citation": sc("pets-deli")},
             note="Fresh pet food, Berlin (founded 2014). Project A invested in 2015 (the firm's archive: Seed, 2015-08); its "
                  "own post of Feb 2016 has Global Founders Capital joining 'existing investors Index Ventures and Project A', "
                  "so Project A predates the eight-figure Series A (tech.eu), which graduates the row. The 2015 round itself is "
                  "not cited. acq. by VAFO Group, 2026.", rounds=rounds("pets-deli")))
L.append(cls("re-cap", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("re-cap"), entry_date="2021-12", grad="graduated", grad_src="web_verified", grad_cite=gc("re-cap"),
             country="DE", city="Berlin", country_cite=LISTING, focus="Fintech & Payments",
             note="Revenue-based financing and treasury platform, Berlin (founded 2021). The Dec 2021 seed ($111.5M headline, "
                  "mostly debt) took its growth capital 'from pan-European VCs Felix Capital and Project A Ventures' after a "
                  "May 2021 pre-seed by Entree (TechCrunch); the $14.6M Series A of June 2024, with Project A, graduates the "
                  "row.", rounds=rounds("re-cap")))
L.append(cls("mister-b-b", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("mister-b-b"), entry_date="2017-06", country="FR", city="Paris", country_cite=ec("mister-b-b"),
             focus="Consumer & Marketplaces", flags=["model_disputes_source"],
             note="LGBTQ+ travel and accommodation platform (misterb&b), Paris (founded 2014). 'Has closed a $8.5 million Series "
                  "A funding round led by Berlin-based VC Project A and primarily France based VC Ventech' (the firm's own "
                  "release, June 2017). Its US entity (CIK 1759313, later SFO84, Inc.) filed Form Ds in San Francisco in "
                  "2019-2020 with Anton Waitz as director; that filing address is the US subsidiary's, not the HQ.",
             rounds=rounds("mister-b-b")))
L.append(cls("q", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("q"), entry_date="2025-07", grad="graduated", grad_src="web_verified", grad_cite=gc("q"),
             country="DE", city="Berlin", country_cite=LISTING, focus="Industrial & Robotics", flags=["model_disputes_source"],
             extra=dict(NOVAL, is_public=False, public_since=None),
             note="Defence software integrating drones and sensors (Project Q, project-q.ai), Berlin (founded 2024). 'The "
                  "funding round was led by early-stage investor Project A' (the EUR 7.5M seed, Dronelife, July 2025); the EUR "
                  "15M Series A led by Expeditions, July 2026, graduates the row. The Wikidata and SEC-float joins (a Norwegian "
                  "company listed in 2011) were namesakes of the one-letter CMS name.", rounds=rounds("q")))
L.append(cls("relay", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("relay"), entry_date="2023-11", grad="graduated", grad_src="web_verified", grad_cite=gc("relay"),
             country="GB", city="London", country_cite=LISTING, focus="Consumer & Marketplaces", flags=["model_disputes_source"],
             extra=NOVAL,
             note="Tech-enabled e-commerce parcel delivery, London (founded 2022). 'We lead the $10m seed funding round for "
                  "Relay' (the firm's post, Nov 2023, co-led with Prologis Ventures); the $35M Series A led by Plural, Feb "
                  "2025, graduates the row. The Wikidata join (a South African company, acquired) and the other books' Relay "
                  "rows (a16z, Spark) are namesakes.", rounds=rounds("relay")))

if __name__ == "__main__":
    write("batch-c", L)
