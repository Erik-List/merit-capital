"""Grind batch G (PRO-102): rows from research-g*.json (every URL re-loaded by the research agents)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write, LISTING, surfaces_lines, ASOF, ec, sc, gc, RS  # noqa: E402
from judge_lib import rrounds as rounds  # noqa: E402

L = []
NOVAL = {"valuation_source": None, "valuation_asof": None, "valuation_confidence": None}
L.append(cls("laserhub", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("laserhub"), entry_date="2019-04", grad="graduated", grad_src="web_verified", grad_cite=gc("laserhub"),
             country="DE", city="Stuttgart", country_cite=LISTING, focus="Industrial & Robotics",
             note="Online procurement for custom sheet-metal and turned parts, Stuttgart (founded 2017). The April 2019 round "
                  "was 'led by the Berlin Operational VC Project A' (the firm's own release), its seed round ('Wir unterstützen "
                  "Laserhub seit der Seed-Runde', Stuttgart Startups); the Series A of July 2020 led by Acton, with Project A "
                  "and Point Nine, graduates the row (tech.eu).", rounds=rounds("laserhub")))
L.append(cls("vaeridion", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("vaeridion"), entry_date="2022-06", grad="graduated", grad_src="web_verified",
             grad_cite=gc("vaeridion"), country="DE", city="Munich", country_cite=LISTING, focus="Climate & Energy",
             note="Battery-electric nine-seat regional aircraft (Microliner), Munich (founded 2021). The EUR 3.2M seed of June "
                  "2022 was led by Vsquared with 'Project A and Andreas Kupke' (Startbase), its first round; the EUR 14M Series "
                  "A of Dec 2024 graduates the row (the company's release).", rounds=rounds("vaeridion")))
L.append(cls("bucket", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("bucket"), entry_date="2023-06", grad="not_graduated", grad_src="absence_check", grad_asof=ASOF,
             surfaces=surfaces_lines("bucket", "no round after the June 2023 seed; the founders bought the company back "
                                               "from its investors in January 2026"),
             country="DK", city="Copenhagen", country_cite=LISTING, focus="DevTools & APIs",
             note="Feature flags for B2B SaaS teams (Bucket, renamed Reflag), Copenhagen (founded 2021 by the Opbeat founders). "
                  "'With a fresh Seed round from Project A, including participation from existing investor Creandum' (the "
                  "company's post, June 2023). No later round; in January 2026 the founders bought the company back from its "
                  "investors to run it for profit (Reflag's post), an exit for Project A, not a sale of the company.",
             rounds=rounds("bucket")))
L.append(cls("baobab", status="private", rng="below_1b", stage="Pre-Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("baobab"), entry_date="2022-01", country="DE", city="Berlin", country_cite=sc("baobab"),
             focus="Fintech & Payments", flags=["model_disputes_source"], extra=NOVAL,
             note="Cyber-insurance MGA for SMEs (Baobab Insurance, now Baobab Risk Solutions), Berlin (founded 2021 in Cologne; "
                  "the register seat moved to Berlin in Sept 2025). 'Baobab's financing round was led by Project A Ventures' "
                  "(the EUR 3.5M pre-seed, PYMNTS, Jan 2022), its first; a EUR 12M Series A led by Viola Fintech in June 2025. "
                  "The Wikidata country CZ was a namesake.", rounds=rounds("baobab")))
L.append(cls("dalma", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("dalma"), entry_date="2022-06", country="FR", city="Paris", country_cite=LISTING,
             focus="Fintech & Payments",
             note="Pet insurance, Paris (founded 2021). Northzone: 'We are leading Dalma's $15m Series A alongside our friends "
                  "from Project A and Anterra, as well as existing investors GFC, Frst and Kima' (June 2022), so Project A came "
                  "in at the A. EUR 20M Series B led by Breega, March 2025.", rounds=rounds("dalma")))
L.append(cls("claimer", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("claimer"), entry_date="2022-09", grad="not_graduated", grad_src="absence_check", grad_asof=ASOF,
             surfaces=surfaces_lines("claimer", "no round after the September 2022 seed"),
             country="GB", city="London", country_cite=LISTING, focus="Fintech & Payments",
             note="R&D tax-credit claims software, London (founded 2018). The GBP 3.6M seed announced Sept 2022: 'The round was "
                  "led by Project A Ventures' (UKTN), after a GBP 300k angel seed in 2020 without it (the firm's CMS year 2021 "
                  "is the close). No later round.", rounds=rounds("claimer")))

if __name__ == "__main__":
    write("batch-g", L)
