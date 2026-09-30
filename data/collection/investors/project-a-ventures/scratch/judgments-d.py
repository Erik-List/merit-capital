"""Grind batch D (PRO-102): rows from research-g*.json (every URL re-loaded by the research agents)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write, LISTING, surfaces_lines, ASOF, ec, sc, gc, RS  # noqa: E402
from judge_lib import rrounds as rounds  # noqa: E402

L = []
NOVAL = {"valuation_source": None, "valuation_asof": None, "valuation_confidence": None}

L.append(cls("stark", status="private", rng="1b_plus", usd=3_987_200_000, val_src="web_verified",
             val_cite=RS["stark"]["valuation"]["citation"], asof="2026-06-23", stage="undetermined",
             country="DE", city="Berlin", country_cite=LISTING, focus="Industrial & Robotics",
             note="Loitering munitions and drones (STARK Defence, stark-defence.com), Berlin (founded 2024). Press names "
                  "Project A among the investors in the $62M round of Aug 2025 led by Sequoia at a $500M valuation (UAS "
                  "Vision) and in the EUR 500M Series C of June 2026 (invest-in.berlin); the entry round is not named, so the "
                  "stage is undetermined. The CMS gives no fund or year; Project A co-founder Uwe Horstmann became STARK's CEO "
                  "in October 2025. Mark: 'more than three and a half billion euros' (TNW), EUR 3.50B @ ECB 2026-06-23 "
                  "(EUR/USD 1.1392) = $3.99B, a floor; aligned in band with Sequoia's row ($4.1B).", rounds=rounds("stark")))
L.append(cls("tirendo", status="acquired", rng="below_1b", stage="Seed", stage_src="model", stage_conf="low",
             entry_date="2012-02", grad="not_graduated", grad_src="web_verified", grad_cite=sc("tirendo"), grad_asof=ASOF,
             surfaces=surfaces_lines("tirendo", "no round after Project A's February 2012 entry; sold to Delticom in September 2013"),
             country="DE", city="Berlin", country_cite=LISTING, focus="Consumer & Marketplaces",
             flags=["stage_uncited"], extra={"status_citation": sc("tirendo")},
             note="Online tyre retailer, Berlin (founded Oct 2011). 'Im Februar dieses Jahres stieg der Inkubator Project A "
                  "Ventures bei Tirendo ein' (Deutsche Startups, 2012); the firm files it as seed (CMS, archive), a round no "
                  "source names. acq. by Delticom for about EUR 50M, Sept 2013, with no later round: the sale ends the row "
                  "not graduated.", rounds=rounds("tirendo")))
L.append(cls("rematiq", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("rematiq"), entry_date="2025-04", grad="censored", country="DE", city="Berlin",
             country_cite=LISTING, focus="Healthcare & Bio",
             note="AI regulatory compliance for MedTech (REMATIQ), Berlin (founded 2023). 'We're proud to be leading "
                  "REMATIQ's EUR 5.4 million Seed round, alongside renowned business angels' (the firm's post, 2025-04-10); "
                  "inside the 24-month window, censored.", rounds=rounds("rematiq")))
L.append(cls("riva", status="private", rng="below_1b", stage="Pre-Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("riva"), entry_date="2025-08", country="GB", city="London", country_cite=LISTING,
             focus="Fintech & Payments", flags=["model_disputes_source"], extra=NOVAL,
             note="Cross-border B2B payments on stablecoin rails (Riva Money), London (founded 2025 by ex-Wise and Revolut "
                  "founders). The $3M pre-seed of Aug 2025 was 'led by Project A' (Financial IT). The Wikidata country IT was "
                  "a namesake.", rounds=rounds("riva")))
L.append(cls("yababa", status="defunct", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("yababa"), entry_date="2021-11", grad="not_graduated", grad_src="web_verified",
             grad_cite="https://tech.eu/2023/02/06/berlins-yababa/", grad_asof=ASOF,
             surfaces=surfaces_lines("yababa", "no round after the November 2021 seed; insolvent in February 2023"), country="DE", city="Berlin", country_cite=LISTING,
             focus="Consumer & Marketplaces", extra={"status_citation": sc("yababa")},
             note="Quick-commerce grocery delivery, Berlin (founded 2021). 'Yababa's seed round is led by Creandum and Project "
                  "A, with existing investor FoodLabs' ($15.5M, TechCrunch, Nov 2021). Insolvency opened by the Charlottenburg "
                  "court on 2023-02-03 and the company has been in liquidation since April 2023 (North Data; tech.eu "
                  "'Berlin's Yababa is insolvent'); no sale of the business, so defunct and not graduated.",
             rounds=rounds("yababa")))
L.append(cls("saatchi-art", status="acquired", rng="below_1b", stage="undetermined", country="US", city="Los Angeles",
             country_src="formd_address", focus="Consumer & Marketplaces", extra={"status_citation": sc("saatchi-art")},
             note="Online art marketplace (Saatchi Online, then Saatchi Art), Los Angeles (Santa Monica on its Form D; founded "
                  "2006). 'Project A has been involved with Saatchi Online since January 2013 as both an investor and a source "
                  "of operational expertise', beside Balderton (the firm's post, Dec 2013); the 2013 round (Form D, $6.15M "
                  "sold, first sale 2013-04-02) is not named by any source and the firm's own labels disagree (CMS series_a, "
                  "archive Series B), so the stage is undetermined. acq. by Demand Media for about $17M in cash and stock, Aug "
                  "2014 (the firm's post; Demand Media's S-3 lists the selling holders); Project A's Demand Media shares are "
                  "sale consideration.", rounds=rounds("saatchi-art")))
L.append(cls("tictail", status="acquired", rng="below_1b", stage="Seed", stage_src="model", stage_conf="low",
             entry_date="2013-11", grad="graduated", grad_src="web_verified", grad_cite=gc("tictail"),
             country="SE", city="Stockholm", country_cite=LISTING, focus="Consumer & Marketplaces",
             flags=["stage_uncited", "model_disputes_source"], extra={"status_citation": sc("tictail")},
             note="DIY e-commerce shops and marketplace, Stockholm (founded 2011). 'Project A Ventures ... invests 600,000 euros "
                  "in the Swedish start-up, Tictail' (the firm's post, Nov 2013), joining the Oct 2012 seed investors Balderton "
                  "and Klaus Hommels before any Series A: a seed-stage cheque no source names. The $8M Series A led by Thrive, "
                  "Feb 2014, graduates the row (Balderton's post). acq. by Shopify, 2018. The Wikidata country US was the New "
                  "York office.", rounds=rounds("tictail")))
L.append(cls("zenguard", status="acquired", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("zenguard"), entry_date="2013-10", grad="graduated", grad_src="web_verified", grad_cite=gc("zenguard"),
             country="DE", city="Berlin", country_cite=LISTING, focus="Security", extra={"status_citation": sc("zenguard")},
             note="ZenMate browser VPN (ZenGuard GmbH), Berlin (founded 2013). Project A 'provides a mid six-figure amount as "
                  "seed investment' (the firm's post, Oct 2013); the $3.2M Series A led by Holtzbrinck Ventures, Oct 2014, "
                  "graduates the row. acq. by Kape Technologies for EUR 4.8M, 2018 (ProPrivacy).", rounds=rounds("zenguard")))

if __name__ == "__main__":
    write("batch-d", L)
