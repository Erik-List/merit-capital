"""Grind batch F (PRO-102): rows from research-g*.json (every URL re-loaded by the research agents)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write, LISTING, surfaces_lines, ASOF, ec, sc, gc, RS  # noqa: E402
from judge_lib import rrounds as rounds  # noqa: E402

L = []
L.append(cls("nexcade", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("nexcade"), entry_date="2026-07", grad="censored", country="GB", city="London",
             country_cite=LISTING, focus="AI & Applied AI",
             extra={"valuation_range_source": "web_verified", "valuation_citation": sc("nexcade"), "valuation_asof": ASOF},
             note="AI agents for freight forwarders, London (founded 2025). 'Nexcade has raised a $6 million Seed round led by "
                  "Project A Ventures' (the company, July 2026), after a $2.5M pre-seed led by Connect Ventures without Project "
                  "A; censored. Momentum-slice check 2026-09-30: no valuation figure.", rounds=rounds("nexcade")))
L.append(cls("priceloop", status="defunct", rng="below_1b", stage="undetermined", country="DE", city="Berlin",
             country_cite=LISTING, focus="SaaS", extra={"status_citation": sc("priceloop")},
             note="AI pricing-optimisation software, Berlin (founded 2020 by Contorion's founder). 'Der Berliner Kapitalgeber "
                  "Project A Ventures investiert in Priceloop' (Deutsche Startups, June 2021), a round no source names (the "
                  "firm's archive: seed); Accel followed in Dec 2021 without a stated amount, so neither the entry round nor a "
                  "graduation can be established. Liquidation filed 2024-05-15, deleted from the register 2025-10-29 (North "
                  "Data): defunct.", rounds=rounds("priceloop")))
L.append(cls("wine-in-black", status="acquired", rng="below_1b", stage="undetermined", country="DE", city="Berlin",
             country_cite=LISTING, focus="Consumer & Marketplaces", extra={"status_citation": sc("wine-in-black")},
             note="Curated premium-wine online shop, Berlin (founded 2011 by others, backed by e.ventures and Passion "
                  "Capital). Deutsche Startups reported in Jan 2012 that Project A planned to take the shop over, 'ob durch "
                  "Übernahme, Teilverkauf oder Beteiligungstausch' still unclear; the firm's 2014 post lists Project A as one "
                  "of five investors (with Bright Capital, e.ventures, Passion Capital, b-to-v), so no control is shown. The "
                  "2012 round is not named and the firm's labels disagree (CMS seed, archive Series A): undetermined. Owned by "
                  "Viva Group since January 2019 (Deutsche Startups).", rounds=rounds("wine-in-black")))
L.append(cls("netspeak-games", status="private", rng="below_1b", stage="Series A", stage_src="web_verified",
             stage_conf="high", stage_cite=ec("netspeak-games"), entry_date="2022-09", country="GB", city="London",
             country_cite=LISTING, focus="Media, Gaming & Advertising",
             note="Remote-first games studio (Sunshine Days), London (founded 2019). The $12M Series A of Sept 2022: 'The round "
                  "was led by venture capital firms LakeStar and Project A' (GamesIndustry.biz). Layoffs in Jan 2024; the "
                  "company is active at Companies House (accounts to March 2026).", rounds=rounds("netspeak-games")))
L.append(cls("resourcly", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("resourcly"), entry_date="2025-10", grad="censored", country="DE", city="Mannheim",
             country_cite=LISTING, focus="AI & Applied AI",
             extra={"valuation_range_source": "web_verified", "valuation_citation": ec("resourcly"), "valuation_asof": ASOF},
             note="AI platform for manufacturers' spare-parts inventory, Mannheim (Techstars-backed). The EUR 2.7M seed of Oct "
                  "2025: 'The round was led by Project A' (tech.eu); censored. Momentum-slice check 2026-09-30: no later round "
                  "or valuation.", rounds=rounds("resourcly")))
L.append(cls("root-global", status="private", rng="below_1b", stage="Pre-Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("root-global"), entry_date="2022-07", country="DE", city="Berlin", country_cite=LISTING,
             focus="Climate & Energy",
             note="Carbon accounting and decarbonisation for food supply chains, Berlin (founded 2022). 'The pre-seed financing "
                  "round was led by Project A' (EUR 2.5M, tech.eu, July 2022); an EUR 8M seed led by Point Nine followed in "
                  "Aug 2024.", rounds=rounds("root-global")))
L.append(cls("vestigas", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("vestigas"), entry_date="2025-04", grad="censored", country="DE", city="Munich",
             country_cite=LISTING, focus="SaaS",
             note="Construction supply-chain software (digital delivery notes, invoice checks), Munich (registered in "
                  "Eggenfelden). The EUR 8M seed of April 2025 with Project A and b2venture (Munich Startup; FinSMEs: 'led by "
                  "Project A and b2venture'); censored.", rounds=rounds("vestigas")))

if __name__ == "__main__":
    write("batch-f", L)
