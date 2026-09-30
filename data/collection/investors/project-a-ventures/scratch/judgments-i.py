"""Grind batch I (PRO-102): rows from research-g*.json (every URL re-loaded by the research agents)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as J  # noqa: E402
from judge_lib import cls, write, LISTING, surfaces_lines, ASOF, ec, sc, gc, RS  # noqa: E402
from judge_lib import rrounds as rounds  # noqa: E402

L = []
NOVAL = {"valuation_source": None, "valuation_asof": None, "valuation_confidence": None}
fs = surfaces_lines("flowrite", "no round after the November 2021 seed (searched as Flowrite)")
fs += surfaces_lines("flow-ai", "no round after the November 2021 seed (searched as Flow AI)")[1:]
L.append(cls("flow-ai", status="acquired", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("flow-ai"), entry_date="2021-11", grad="not_graduated", grad_src="absence_check", grad_asof=ASOF,
             surfaces=fs, country="FI", city="Helsinki", country_cite=LISTING, focus="AI & Applied AI",
             extra={"status_citation": sc("flowrite")},
             note="AI writing assistant Flowrite, renamed Flow AI (AI agents), Helsinki (founded 2020). 'The seed is led by "
                  "Project A' ($4.4M, TechCrunch, Nov 2021), after money from Lifeline and Seedcamp. No later round; the "
                  "Flowrite product went to Maestro Labs in Jan 2025 and Aiven acquired the company in July 2026.",
             rounds=rounds("flowrite")))
L.append(cls("liqid", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("liqid"), entry_date="2015-08", grad="graduated", grad_src="web_verified", grad_cite=gc("liqid"),
             country="DE", city="Berlin", country_cite=LISTING, focus="Fintech & Payments",
             note="Digital wealth manager, Berlin (founded 2015). 'Project A Ventures is supporting the company's seed round "
                  "with a seven-figure investment' (the firm's post, Aug 2015); the EUR 33M 'Series C' of Sept 2018 led by "
                  "Toscafund graduates the row (the firm's release). LGT took a significant minority in the EUR 88M Series D, "
                  "2021.", rounds=rounds("liqid")))
L.append(cls("minodes", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("minodes"), entry_date="2013-08", country="DE", city="Berlin", country_cite=LISTING, focus="SaaS",
             extra={"status_citation": sc("minodes")},
             note="In-store visitor analytics for retailers, Berlin (founded July 2013). 'Completion of an undisclosed 7-digit "
                  "Series A round of financing led by Project A Ventures and Berlin Technologie Holding' (the firm's post, "
                  "2014; the firm's CMS says seed, the post settles it). acq. by Telefónica Germany NEXT for a low eight-figure "
                  "euro sum, May 2017 (the firm's post).", rounds=rounds("minodes")))
L.append(cls("opinary", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("opinary"), entry_date="2018-01", country="DE", city="Berlin", country_cite=LISTING,
             focus="Media, Gaming & Advertising", extra={"status_citation": sc("opinary")},
             note="Opinion polls and engagement widgets for publishers, Berlin (founded 2014). The EUR 3M Series A of Jan 2018 "
                  "was 'led by Project A', with previous backers GFC and Motu (tech.eu). acq. by Affinity Global, 2023; the GmbH "
                  "was renamed Affinity Global GmbH in 2024.", rounds=rounds("opinary")))
L.append(cls("semasio", status="acquired", rng="below_1b", stage="Seed", stage_src="first_party", stage_conf="medium",
             stage_cite=LISTING, entry_date="2012-08", grad="not_graduated", grad_src="absence_check", grad_asof=ASOF,
             surfaces=surfaces_lines("semasio", "no named round after Project A's August 2012 entry; bought by Fyllo in "
                                                "2022 and by Samba TV in 2024"),
             country="DE", city="Hamburg", country_cite=LISTING, focus="Media, Gaming & Advertising",
             extra={"status_citation": sc("semasio")},
             note="Semantic audience targeting for advertisers, Hamburg (founded 2010). 'Holtzbrinck Ventures and the incubator "
                  "Project A have joined the High-Tech Gründerfonds in investing a seven-digit sum into Semasio GmbH' (HTGF, "
                  "Aug 2012), a round the release does not name; the firm's own record calls it seed (CMS, Fund I). No named "
                  "later round; acq. by Fyllo, 2022, then by Samba TV, 2024.", rounds=rounds("semasio")))
L.append(cls("treatwell", status="acquired", rng="below_1b", stage="Series A", stage_src="first_party", stage_conf="medium",
             stage_cite=LISTING, entry_date="2014-10", country="NL", city="Amsterdam", country_cite=LISTING,
             focus="Consumer & Marketplaces", flags=["model_disputes_source"], extra=dict(NOVAL, status_citation=sc("treatwell")),
             note="Hair and beauty booking marketplace, Amsterdam (the Dutch Treatwell, founded 2012). Series A 2014 by the "
                  "firm's own record (CMS, archive and 2016-19 pages); Recruit's disclosure lists Project A with EUR 2.1M. acq. "
                  "by Wahanda (a Recruit company) for EUR 34M, June 2015, which then took the Treatwell name (the firm's own "
                  "post). The Wikidata country DE was the later group's.", rounds=rounds("treatwell")))
L.append(cls("eyeota", status="acquired", rng="below_1b", stage="Seed", stage_src="first_party", stage_conf="medium",
             stage_cite=LISTING, entry_date="2013-04", grad="graduated", grad_src="web_verified", grad_cite=gc("eyeota"),
             country="SG", city="Singapore", country_cite=LISTING, focus="Media, Gaming & Advertising",
             extra={"status_citation": sc("eyeota")},
             note="Audience data for digital advertising, Singapore (founded 2010; European base in Berlin). Seed 2013 by the "
                  "firm's own record (CMS, Fund I; the archive dates it 2013-04 and calls it Series A, the CMS wins, R2); the "
                  "$7M Series A of Jan 2016, with Project A, graduates the row (the firm's release). acq. by Dun & Bradstreet, "
                  "2021.", rounds=rounds("eyeota")))
L.append(cls("nettle", status="private", rng="below_1b", stage="Pre-Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("nettle"), entry_date="2025-04", country="GB", city="London", country_cite=LISTING,
             focus="AI & Applied AI",
             extra={"valuation_range_source": "web_verified", "valuation_citation": ec("nettle"), "valuation_asof": ASOF},
             note="AI risk assessment for commercial insurers, London (founded 2024). The GBP 1.45M pre-seed of April 2025: "
                  "'The funding round was led by Project A' (tech.eu), with angels. Momentum-slice check 2026-09-30: no later "
                  "round or valuation.", rounds=rounds("nettle")))

if __name__ == "__main__":
    write("batch-i", L)
