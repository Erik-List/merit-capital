"""Grind batch E (PRO-102): rows from research-g*.json (every URL re-loaded by the research agents)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write, LISTING, surfaces_lines, ASOF, ec, sc, gc, RS  # noqa: E402
from judge_lib import rrounds as rounds  # noqa: E402

L = []
L.append(cls("avoltra", status="private", rng="below_1b", stage="Pre-Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("avoltra"), entry_date="2025-07", country="DE", city="Munich", country_cite=LISTING,
             focus="Climate & Energy",
             note="AI energy-procurement intelligence for industry, Munich (the CMS; the GmbH is registered in Nuremberg). The "
                  "EUR 2.3M pre-seed of July 2025: 'The round was led by Project A', which had followed the founders through "
                  "the Project A Studio (tech.eu).", rounds=rounds("avoltra")))
L.append(cls("amazd", status="unknown", rng="below_1b", stage="Seed", stage_src="model", stage_conf="low",
             entry_date="2021-03", grad="not_graduated", grad_src="absence_check", grad_asof=ASOF,
             surfaces=surfaces_lines("amazd", "no round after the March 2021 investment"),
             country="DE", city="Munich", country_cite=LISTING, focus="SaaS", flags=["stage_uncited"],
             note="Conversational commerce (shop advisers chatting with shoppers), Munich (founded Oct 2020). 'Project A "
                  "Ventures und Global Founders Capital (GFC) investieren in amazd' (Deutsche Startups, March 2021), its only "
                  "reported round and unnamed; the firm's archive calls it seed. The GmbH is still registered (last annual "
                  "report 2023, filed Jan 2025) but the website no longer serves and the firm dropped it from its list: dark, "
                  "so unknown.", rounds=rounds("amazd")))
L.append(cls("ello", status="private", rng="below_1b", stage="Seed", stage_src="model", stage_conf="low",
             entry_date="2020", grad="graduated", grad_src="web_verified", grad_cite=gc("ello"),
             country="US", city="San Francisco", country_cite=LISTING, focus="Consumer & Marketplaces", flags=["stage_uncited"],
             note="AI reading coach for children, San Francisco (YC W20). Project A led Ello's funding before its Series A "
                  "('existing funding led by Project A', TechCrunch 2023); the firm's CMS files it as a 2020 seed, a round no "
                  "source names. The $15M Series A of Sept 2023 graduates the row.", rounds=rounds("ello")))
L.append(cls("evernest", status="private", rng="below_1b", stage="undetermined", country="DE", city="Hamburg",
             country_cite=LISTING, focus="Consumer & Marketplaces",
             note="Tech-enabled real-estate brokerage, Hamburg (founded Nov 2019). Project A invested with business angels in "
                  "March 2020 and held 19.7% (Deutsche Startups, 2020-05-01), a round no source names; the firm's CMS says seed "
                  "2019, but the company's named seed (EUR 6M, March 2021, Project A in it) came a year later, so the entry "
                  "round is not established. EUR 13M Series A Jan 2022.", rounds=rounds("evernest")))
L.append(cls("atmen", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("atmen"), entry_date="2025-06", grad="censored", country="DE", city="Munich",
             country_cite=LISTING, focus="Climate & Energy", flags=["model_disputes_source"],
             note="Certification and compliance software for green hydrogen and industrial energy (Atmen Solutions GmbH, "
                  "formerly Point Twelve Energy), Munich area (Eching). 'Atmen closed a EUR 5M seed funding round, led by "
                  "Project A' with existing investors Revent and Vireo (Tech Funding News, June 2025); censored. The Wikidata "
                  "country CZ was a namesake.", rounds=rounds("atmen")))
L.append(cls("bene-bono", status="acquired", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("bene-bono"), entry_date="2022-07", grad="not_graduated", grad_src="absence_check",
             grad_asof=ASOF, surfaces=surfaces_lines("bene-bono", "no named later round; an unnamed EUR 10M round in March "
                                                                  "2024 below the step-up bar; receivership in 2025"),
             country="FR", city="Paris", country_cite=LISTING, focus="Consumer & Marketplaces",
             extra={"status_citation": sc("bene-bono")},
             note="Anti-waste organic grocery delivery (Hors Normes until 2023), Paris (founded 2020). Project A came in at the "
                  "EUR 7M seed of July 2022 beside Stride VC, which had funded the first EUR 1.55M alone (Reussir; Journal du "
                  "Net). An unnamed EUR 10M round in March 2024 (about $10.8M) is below the step-up bar of twice the $7.1M "
                  "seed, so the row did not graduate. Receivership in summer 2025; the Paris commercial court chose Quitoque's "
                  "takeover offer in Oct 2025 (Maddyness): insolvency followed by a sale, acquired.",
             rounds=rounds("bene-bono")))

if __name__ == "__main__":
    write("batch-e", L)
