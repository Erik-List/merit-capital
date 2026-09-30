"""Grind batch B (PRO-102): rows from research-g*.json (every URL re-loaded by the research agents)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write, LISTING, surfaces_lines, ASOF, ec, sc, gc  # noqa: E402
from judge_lib import rrounds as rounds  # noqa: E402

L = []

L.append(cls("homeday", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("homeday"), entry_date="2016-05", country="DE", city="Berlin", country_cite=LISTING,
             focus="Consumer & Marketplaces", extra={"status_citation": sc("homeday")},
             note="Digital estate agency, founded in Cologne in 2014, now Berlin. 'Successful Series A Financing Round: Homeday "
                  "Wins Project A and Paua Ventures as Investors' (the firm's own post, 2016-06-15: Project A committed in May "
                  "2016). Axel Springer took 100% in 2023 (Gruenderszene).", rounds=rounds("homeday")))
L.append(cls("linexa", status="private", rng="below_1b", stage="Pre-Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("linexa"), entry_date="2026-04", country="DE", city="Munich", country_cite=LISTING,
             focus="Industrial & Robotics",
             note="AI layer over legacy factory-automation logic, Munich (founded 2025). 'Linexa ... has raised EUR 2 million in "
                  "pre-seed funding, led by Project A' (tech.eu, 2026-04-22), its first round.", rounds=rounds("linexa")))
L.append(cls("hades", status="private", rng="below_1b", stage="Pre-Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("hades"), entry_date="2025-08", country="DE", city="Munich", country_cite=LISTING,
             focus="Climate & Energy",
             note="Geothermal and critical-mineral drilling (Hades Mining, now Hades Resources GmbH), Munich (founded 2024). "
                  "'Hades Mining ... has raised a EUR 5.5 million pre-seed round led by Project A' (tech.eu, 2025-08-20); a EUR "
                  "15M round named seed followed in Q1 2026.", rounds=rounds("hades")))
L.append(cls("klara", status="acquired", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("klara"), entry_date="2016-09", grad="graduated", grad_src="web_verified", grad_cite=gc("klara"),
             country="US", city="New York", country_cite=LISTING, focus="Healthcare & Bio",
             extra={"status_citation": sc("klara")},
             note="Patient-communication platform, New York (founded 2013 in Berlin). 'Project A first invested in 2016 in "
                  "Klara's seed funding round' (the firm's exit post), the $3M seed co-led with Lerer Hippeau; the $11.5M "
                  "Series A of Aug 2018 led by FirstMark, with Project A, graduates the row. acq. by ModMed, 2022 (the firm's "
                  "post); Project A's ModMed shares are sale consideration (the modernizing-medicine row).",
             rounds=rounds("klara")))
L.append(cls("labrys", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("labrys"), entry_date="2023-12", grad="graduated", grad_src="web_verified", grad_cite=gc("labrys"),
             country="GB", city="London", country_cite=LISTING, focus="Security", flags=["model_disputes_source"],
             note="Secure command-and-control and verification platform for defence and humanitarian teams, London (founded "
                  "2022). The $5.5M seed of Dec 2023 was 'led by Germany's Project A Ventures' (TechCrunch), its first round; "
                  "the $20M Series A of June 2025 led by Plural graduates the row. The Wikidata country IT was a namesake.",
             rounds=rounds("labrys")))
L.append(cls("metycle", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("metycle"), entry_date="2023-12", grad="graduated", grad_src="web_verified", grad_cite=gc("metycle"),
             country="DE", city="Cologne", country_cite=LISTING, focus="Consumer & Marketplaces",
             note="B2B marketplace for secondary metals, Cologne (founded 2022). 'Project A led Metycle's Seed funding round "
                  "with Partech' (tech.eu, Dec 2023); the EUR 1.5M pre-seed before it was Market One's and DFF's. The EUR 14.1M "
                  "Series A of Feb 2025 led by 2150 graduates the row (FinSMEs, archived capture); a $150M credit facility in "
                  "Sept 2026.", rounds=rounds("metycle")))
L.append(cls("heyflow", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("heyflow"), entry_date="2021-10", grad="graduated", grad_src="web_verified", grad_cite=gc("heyflow"),
             country="DE", city="Hamburg", country_cite=LISTING, focus="SaaS",
             note="No-code interactive-form builder, Hamburg (founded 2020). The $6M seed of Oct 2021 was 'led by Project A "
                  "Ventures in Berlin' after Atlantic Labs and Possible Ventures (Hamburg Business); the EUR 14.7M Series A of "
                  "Feb 2024 graduates the row (EU-Startups).", rounds=rounds("heyflow")))
L.append(cls("immersive-gamebox", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified",
             stage_conf="medium", stage_cite=ec("immersive-gamebox"), entry_date="2019-12", country="GB", city="London",
             country_cite=LISTING, focus="Media, Gaming & Advertising", extra={"status_citation": sc("immersive-gamebox")},
             note="Immersive group-gaming venues (Electric Playbox, Electric Gamebox, Immersive Gamebox), London (founded "
                  "2018). Project A was in the GBP 8.5M Series A of Dec 2019 (the firm's archive: Series A, 2020-01; the June "
                  "2021 Series A follow-on lists it among the 'existing investors', UKTN). The operating company entered "
                  "administration on 2024-12-10 and the business was sold to funds of Harlan Capital Partners in Feb 2025 "
                  "(insolvency followed by a sale: acquired).", rounds=rounds("immersive-gamebox")))
L.append(cls("micropsi", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("micropsi"), entry_date="2018-10", country="DE", city="Berlin", country_cite=LISTING,
             focus="Industrial & Robotics",
             note="AI software for industrial robots (micropsi industries), Berlin (founded 2014). 'Closed $6.08 million (5.28 "
                  "million euros) in Series A funding led by Project A', with previous investors Coparion and Vito Ventures (the "
                  "firm's own release, Oct 2018); a EUR 30M round in Feb 2022 (VentureBeat).", rounds=rounds("micropsi")))

if __name__ == "__main__":
    write("batch-b", L)
