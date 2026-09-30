"""The visible slice and its neighbours (PRO-102 grind; COLLECTION.md s7 A/B pass).
Sources: scratch/visible-research.json (every URL re-loaded by the research agent)."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write, LISTING, rnd  # noqa: E402

V = json.loads((Path(__file__).resolve().parent / "visible-research.json").read_text())["companies"]


def E(name):
    return V[name]["entry"]["source"]


def LP(name):
    return V[name]["latest_priced_round"]["source"]


def rounds(name):
    out = []
    for r in V[name].get("rounds") or []:
        out.append(rnd(r.get("date"), r.get("round"), r.get("amount_usd"), r.get("lead"), r.get("firm_in_round"),
                       r.get("source") or None, r.get("source_type") or "press"))
    return out


def R(name, i):
    return V[name]["rounds"][i]["source"]


L = []
geo = dict(country_cite=LISTING)

L.append(cls("trade-republic", status="private", rng="10b_plus", usd=14_652_500_000, val_src="web_verified",
             val_cite=V["Trade Republic"]["status_citation"], asof="2025-12-17",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=E("Trade Republic"),
             entry_date="2019-07", country="DE", city="Berlin", focus="Fintech & Payments", clear=["unicorn_name_match"], **geo,
             note="Mobile broker and bank, Berlin (founded 2015). Project A co-led the Series A with Creandum in July 2019 "
                  "(the firm's own post: 'invest in Trade Republic's Series A alongside our friends from Creandum'). Mark: "
                  "the EUR 1.2B secondary of Dec 2025 led by Founders Fund at EUR 12.5B, EUR 12.50B @ ECB 2025-12-17 (EUR/USD "
                  "1.1722) = $14.65B (EQS); the last primary was the EUR 250M Series C extension of June 2022 at EUR 5B "
                  "(tech.eu). Aligned with the Accel, Creandum, Sequoia, TCV and Thrive rows, which carry the same secondary.",
             rounds=rounds("Trade Republic")))

L.append(cls("sennder", status="private", rng="1b_plus", usd=1_000_000_000, val_src="web_verified", val_cite=LP("sennder"),
             asof="2021-06-01", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=E("sennder"),
             entry_date="2018", country="DE", city="Berlin", focus="Industrial & Robotics", flags=["stale"], clear=["unicorn_name_match"], **geo,
             note="Digital road-freight forwarder, Berlin (founded 2015). Project A and HV Capital provided the eight-figure "
                  "Series A of 2018 (the company's own fundraising post names HV and 'PAV'), after a 2016 angel round and a "
                  "2017 Scania investment Project A was not in. Last priced mark: the $80M Series D extension of June 2021 "
                  "'at a $1B+ valuation' (TechCrunch); no later priced round, so the mark is stale. Bought C.H. Robinson's "
                  "European surface business in 2024.", rounds=rounds("sennder")))

L.append(cls("kry", status="private", rng="1b_plus", usd=2_000_000_000, val_src="web_verified", val_cite=LP("Kry (Livi)"),
             asof="2021-04-26", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=E("Kry (Livi)"),
             entry_date="2016-08", grad="graduated", grad_src="web_verified", grad_cite=R("Kry (Livi)", 1),
             country="SE", city="Stockholm", focus="Healthcare & Bio", flags=["stale"], clear=["unicorn_name_match"], **geo,
             note="Video-based healthcare (Livi outside Sweden), Stockholm (founded 2014). Project A 'took part in this seed "
                  "round', the EUR 6.1M seed led by Index Ventures and Creandum (the firm's own release, 2016-08-17); the "
                  "EUR 20M Series A of June 2017 graduates the row. Last priced mark: the $300M Series D of April 2021 at "
                  "over $2B (the firm's post and Kry's release); no later priced round, so the mark is stale.",
             rounds=rounds("Kry (Livi)")))

L.append(cls("zepz", status="private", rng="1b_plus", usd=5_000_000_000, val_src="web_verified", val_cite=LP("Zepz (WorldRemit)"),
             asof="2021-08-24", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=E("Zepz (WorldRemit)"),
             entry_date="2014-03", country="GB", city="London", focus="Fintech & Payments", flags=["stale"], clear=["unicorn_name_match"], **geo,
             note="Digital remittances (WorldRemit, renamed Zepz in 2021), London (founded 2010). Project A was in the $40M "
                  "Series A of 2014 with Accel (the firm's own 2017 release: '$40m raised by Accel Partners and Project A in "
                  "2014'). Last priced mark: the $292M Series E of Aug 2021 at $5B; the $267M raise of Oct 2024 stated no "
                  "valuation, so the mark is stale.", rounds=rounds("Zepz (WorldRemit)")))

L.append(cls("voi", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="medium",
             stage_cite=E("Voi Technology"), entry_date="2019-03", country="SE", city="Stockholm",
             focus="Consumer & Marketplaces", flags=["model_disputes_source"], clear=["unicorn_name_match"], **geo,
             extra={"valuation_range_source": "web_verified", "valuation_source": "web_verified", "valuation_citation": LP("Voi Technology"),
                    "valuation_asof": "2026-09-30"},
             note="Shared e-scooters, Stockholm (founded 2018). Project A joined the $30M round of March 2019 as a new "
                  "investor (the firm's own release; its URL and the live CMS call it the Series A, Creandum's book calls the "
                  "same round Series B). The Dec 2021 $115M Series D put Voi 'amongst the unicorn club' without a figure; its "
                  "lead shareholder VNV Global has since carried it at $362M-$656M, so the row reads below_1b under the "
                  "collapse-evidence rule (COLLECTION.md s6, the Creandum reading), aligned with the Balderton, Creandum and "
                  "Felicis rows. A reported May 2026 Uber purchase was denied by Voi's CEO and is not in Uber's 10-Q.",
             rounds=rounds("Voi Technology")))

L.append(cls("quantum-systems", status="private", rng="1b_plus", usd=8_000_000_000, val_src="web_verified",
             val_cite=LP("Quantum Systems"), asof="2026-07-02", stage="Series A", stage_src="web_verified",
             stage_conf="medium", stage_cite=E("Quantum Systems"), entry_date="2022-10", country="DE", city="Munich",
             focus="Industrial & Robotics", **geo,
             note="Drones and multi-domain autonomy, Munich area (Gilching; the firm's CMS says Munich). Project A came in at "
                  "the October 2022 round that extended the June 2022 Series A ('The funds come from US investor Peter Thiel, "
                  "Berlin-based VC Project A, and Sanno Capital', Munich Startup). Mark: the $1.2B Series D signed July 2026 "
                  "at about $8B, aligned with the Balderton and HV Capital rows.", rounds=rounds("Quantum Systems")))

L.append(cls("catawiki", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=E("Catawiki"), entry_date="2014-09", country="NL", city="Amsterdam", focus="Consumer & Marketplaces",
             **geo, note="Online auctions, Amsterdam (founded 2008). Project A 'also participated' in the EUR 10M Series B of "
                         "Sept 2014 led by Accel (the firm's own release). Last reported valuation EUR 500M (the 2020 growth "
                         "round, as reported in 2026); below $1B.", rounds=rounds("Catawiki")))

L.append(cls("spryker", status="private", rng="below_1b", stage="Pre-Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=E("Spryker"), entry_date="2014", country="DE", city="Berlin", focus="SaaS", **geo,
             note="Composable commerce platform, Berlin (founded 2014 as a joint venture out of Project A's own e-commerce "
                  "platform). 'Project A is a pre-seed investor in Spryker since 2014 and remains the largest shareholder' "
                  "(the firm's post on the $130M Series C of Dec 2020, which valued Spryker at over $500M); an undisclosed "
                  "capital increase in Dec 2025.", rounds=rounds("Spryker")))

L.append(cls("11x", status="private", rng="below_1b", stage="Pre-Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=E("11x"), entry_date="2023-08", country="US", city="San Francisco", focus="AI & Applied AI", **geo,
             extra={"valuation_range_source": "web_verified", "valuation_citation": LP("11x"), "valuation_asof": "2026-09-30"},
             note="AI sales agents ('digital workers'), founded in London in 2022, now San Francisco. 'Project A led a $2 "
                  "million Pre-seed round into the company at incorporation' (the firm's post; announced Aug 2023, the CMS "
                  "year 2022). $24M Series A led by Benchmark (Sept 2024) and a $50M Series B led by a16z (late 2024, "
                  "reported at about $350M); no $1B figure (momentum-slice web check).", rounds=rounds("11x")))

L.append(cls("black-semiconductor", status="private", rng="below_1b", stage="Seed", stage_src="web_verified",
             stage_conf="medium", stage_cite=E("Black Semiconductor"), entry_date="2021",
             grad="graduated", grad_src="web_verified", grad_cite=R("Black Semiconductor", 1),
             country="DE", city="Aachen", focus="Industrial & Robotics", **geo,
             note="Graphene-photonics chips, Aachen (founded 2020). Project A has been 'an early supporter ... since its "
                  "seed stage' (the firm's post; CMS: Fund IV, 2021, seed), joining the seed after TechCrunch's 2020 list "
                  "of Vsquared, Cambium and Onsight. The June 2024 Series A (EUR 25.7M equity beside EUR 228.7M of IPCEI "
                  "public funding, TechCrunch) graduates the row.", rounds=rounds("Black Semiconductor")))

L.append(cls("vay", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=E("Vay"), entry_date="2021-12", country="DE", city="Berlin", focus="Industrial & Robotics", **geo,
             note="Remote-driven car delivery (teledriving), Berlin (founded 2018). Project A came in at the $95M Series B "
                  "of Dec 2021 ('In addition, Project A, Visionaries Club and signals Venture Capital participated', Vay's "
                  "release). Grab made a strategic investment in Nov 2025 (closed Jan 2026) with an option that could reach "
                  "a majority; no valuation stated and no change of control yet.", rounds=rounds("Vay")))

L.append(cls("arx-robotics", status="private", rng="below_1b", stage="Pre-Seed", stage_src="web_verified",
             stage_conf="high", stage_cite=E("ARX Robotics"), entry_date="2023-09", country="DE", city="Munich",
             focus="Industrial & Robotics", **geo,
             note="Unmanned ground robots for defence and industry, Munich (founded 2022). 'Project A leads a EUR 1.15m "
                  "pre-seed round for ARX' (the firm's post, Sept 2023); seed 2024, EUR 31M Series A April 2025 and an "
                  "extension in July 2025. No valuation figure published.", rounds=rounds("ARX Robotics")))

L.append(cls("dixa", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=E("Dixa"), entry_date="2019-02", country="DK", city="Copenhagen", focus="SaaS", **geo,
             flags=["model_disputes_source"],
             note="Customer-service platform, Copenhagen (founded 2015). 'The funding is led by Project A Ventures together "
                  "with the early investor SEED Capital', the $14M Series A of Feb 2019 (the firm's own release). Series B "
                  "2020, $105M Series C led by General Atlantic 2021; no valuation figure. The Wikidata country SE was a "
                  "wrong join and is replaced.", rounds=rounds("Dixa")))

L.append(cls("unmind", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=E("Unmind"), entry_date="2020-02", country="GB", city="London", focus="Healthcare & Bio", **geo,
             note="Workplace mental-health platform, London (founded 2016). The $10M Series A of Feb 2020 was 'led by "
                  "Berlin-based Project A' (tech.eu); $47M Series B 2021, $35M Series C 2025.", rounds=rounds("Unmind")))

L.append(cls("casavo", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=E("Casavo"), entry_date="2019-02", country="IT", city="Milan", focus="Consumer & Marketplaces", **geo,
             note="Residential real estate (instant buying, now agency), Milan (founded 2017). 'Leading the new funding round "
                  "is Project A Ventures', the $7.9M Series A of Feb 2019 (the firm's own release). A Dec 2025 balance-sheet "
                  "restructuring wiped out the old shareholders and a EUR 12M capital increase followed in April 2026; the "
                  "company operates.", rounds=rounds("Casavo")))

if __name__ == "__main__":
    write("visible", L)
