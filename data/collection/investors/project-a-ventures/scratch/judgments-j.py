"""Grind batch J (PRO-102): rows from research-g*.json (every URL re-loaded by the research agents)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as J  # noqa: E402
from judge_lib import cls, write, LISTING, surfaces_lines, ASOF, ec, sc, gc, RS  # noqa: E402
from judge_lib import rrounds as rounds  # noqa: E402

L = []
L.append(cls("intelipost", status="private", rng="below_1b", stage="Seed", stage_src="first_party", stage_conf="medium",
             stage_cite=LISTING, entry_date="2014-08", grad="graduated", grad_src="web_verified", grad_cite=gc("intelipost"),
             country="BR", city="São Paulo", country_cite=LISTING, focus="SaaS", extra={"status_citation": sc("intelipost")},
             note="Freight-management software for Brazilian e-commerce, São Paulo (founded 2014; co-founded by evino's former "
                  "logistics director). Seed 2014 by the firm's own record (CMS, Fund I; the firm's round date 2014-08), the "
                  "first-year BRL 3.5M 'rodada semente' (InfoMoney); the Series A of May 2016 led by Performa graduates the row "
                  "(E-Commerce Brasil). Still independent (BRL 130M Series B, 2020); the firm's 'exited' is Project A selling "
                  "its stake.", rounds=rounds("intelipost")))
L.append(cls("restack", status="private", rng="below_1b", stage="Seed", stage_src="first_party", stage_conf="medium",
             stage_cite=LISTING, entry_date="2021-09", grad="not_graduated", grad_src="absence_check", grad_asof=ASOF,
             surfaces=surfaces_lines("restack", "no round after the 2021 seed"),
             country="DE", city="Berlin", country_cite=LISTING, focus="DevTools & APIs",
             note="Backend framework for AI agents (first a hosting layer for open-source apps), Berlin (founded 2021). Seed "
                  "2021 by the firm's own record (CMS, Fund III; archive 2021-09), the only source for the round; no later "
                  "round.", rounds=rounds("restack")))
L.append(cls("meine-erde", status="private", rng="below_1b", stage="Seed", stage_src="first_party", stage_conf="medium",
             stage_cite=J.fields("meine-erde", "cf_investment")[0][1], entry_date="2021-09", grad="not_graduated",
             grad_src="absence_check", grad_asof=ASOF,
             surfaces=surfaces_lines("meine-erde", "no round after the 2021 entry but a seed extension in November 2024"),
             country="DE", city="Berlin", country_cite=LISTING, focus="Consumer & Marketplaces",
             note="Human-composting burial provider (Circulum Vitae GmbH), Berlin (founded 2021). 'Der Berliner Geldgeber "
                  "Project A Ventures investiert ... gemeinsam mit Fußballweltmeister Mario Götze sowie zahlreichen Business "
                  "Angels' (Deutsche Startups, Sept 2021), before the company's launch; seed by the firm's own record "
                  "(archive). The only later round is a seed extension (Nov 2024), so the row did not graduate.",
             rounds=rounds("meine-erde")))
L.append(cls("scenset", status="unknown", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("scenset"), entry_date="2022-01", grad="not_graduated", grad_src="absence_check", grad_asof=ASOF,
             surfaces=surfaces_lines("scenset", "no round after the January 2022 seed (searched as Scenset; Origin collides "
                                                "with namesakes)"),
             country="NL", city="Amsterdam", country_cite=LISTING, focus="Consumer & Marketplaces",
             note="Membership luxury-travel planning (Origin until renamed), Amsterdam (founded 2020). 'The Dutch company has "
                  "raised over $5M funding in its seed round led by a German VC firm Project A' (Tech Funding News, Jan 2022). "
                  "No later round; scenset.com no longer resolves and no shutdown, dissolution or sale is on record, so the "
                  "status is unknown.", rounds=rounds("scenset")))

if __name__ == "__main__":
    write("batch-j", L)
