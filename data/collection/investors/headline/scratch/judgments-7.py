"""Leftovers of pass 1: team-page docs with no CMS details (identified by search where
possible), the hidden Roadrunner doc, Zippia's stage and city. Merged: helcium -> helcim.
A company that cannot be named stays a member on the firm's own listing and reads
undetermined (COLLECTION.md s3, s6)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, verdict, write, rnd  # noqa: E402

AMI = "https://techcrunch.com/2026/03/09/yann-lecuns-ami-labs-raises-1-03-billion-to-build-world-models/"
FETCH = "https://madison.com/business/shopping-app-fetch-rewards-to-double-staff-after-raising-25-million/article_56c3ebd1-e889-5e37-9261-7868220dda80.html"
GOF = "https://www.prnewswire.com/news-releases/gofreight-raises-23m-to-automate-freight-forwarding-workflows-and-expand-its-team-301684587.html"
RR = "https://www.businesswire.com/news/home/20200317005064/en/RoadRunner-Recycling-Raises-%2428.6-Million-in-Series-C-Funding-to-Continue-US-Expansion-Double-Team-Size-and-Elevate-Recycling-in-a-World-Dominated-by-Waste"
ZIP = "https://www.prnewswire.com/news-releases/career-resource-site-zippia-raises-8-5-million-in-series-a-funding-to-expand-product-development-and-reach-new-job-seekers-300835403.html"
CLAR = "https://www.firstminute.capital/news-announcements/clarity-care-hermine-tranie"


def unresolved(slug, who, why, country="US"):
    return cls(slug, status="unknown", country=country, rng="undetermined", stage="undetermined",
               grad="undetermined", flags=["identity_unresolved", "country_prior"],
               note=f"A title-only CMS doc on {who}'s team page (created August 2026, no location, website or date). {why} The company cannot be named; country is the listing partner's desk, inferred.")


L = [
    cls("ami-labs", status="private", country="FR", city="Paris", rng="1b_plus", usd=4530000000, val_src="web_verified",
        val_cite=AMI, asof="2026-03-09", val_conf="high", stage="Seed", stage_src="model", stage_conf="medium",
        entry_date="2026-03", grad="censored",
        note="AMI Labs (Advanced Machine Intelligence; Yann LeCun, Alexandre LeBrun and others), Paris. Its only round: $1.03B at a $3.5B pre-money valuation ($4.53B post), March 2026, co-led by Cathay Innovation, Greycroft, Hiro Capital, HV Capital and Bezos Expeditions, reported as Europe's largest seed. The press does not name Headline; the firm's CMS lists AMI Labs on the EU fund page under three of its investors, so the entry is this round.",
        rounds=[rnd("2026-03-09", "Seed", 1030000000, "Cathay Innovation; Greycroft; Hiro Capital; HV Capital; Bezos Expeditions", None, AMI, "press")]),
    cls("fetch", status="private", country="US", city="Madison", stage="Growth", stage_src="web_verified",
        stage_conf="high", stage_cite=FETCH, entry_date="2019-11",
        note="Fetch (Fetch Rewards; founder Wes Schroll), Madison, Wisconsin; on the CMS's US and Global Growth fund pages. Greycroft and e.ventures led the $25M Series B (November 2019). Mark goes to the valuation pass.",
        rounds=[rnd("2019-11", "Series B", 25000000, "Greycroft; e.ventures", True, FETCH, "press")]),
    cls("gofreight", status="private", country="US", city="Los Angeles", rng="below_1b", stage="Series A",
        stage_src="web_verified", stage_conf="high", stage_cite=GOF, entry_date="2022-11",
        note="GoFreight (freight-forwarding software): $23M Series A co-led by Flex Capital and Headline (November 2022). Listed by Thomas Gieselmann.",
        rounds=[rnd("2022-11", "Series A", 23000000, "Flex Capital; Headline", True, GOF, "press")]),
    cls("claritycare", status="private", country="US", rng="below_1b", stage="undetermined", flags=["city_unknown"],
        note="ClarityCare AI (prior authorisation and utilisation management agents; CEO Hermine Tranié, CTO Alexandru Andrei, via Entrepreneurs First), Delaware-registered; $3.5M seed (2025) with Maverick, firstminute and Top Harvest, no Headline named. Listed by Mathias Schilling and Astrid Moullé-Berteaux in 2026; the round Headline entered is not on record. City not placeable (Dover is the registered agent's)."),
    unresolved("indigo", "Jerry Fung", "Indigo, the medical-liability insurer (Series B $50M, February 2026, led by Rubicon Founders), is one candidate but no Headline round ties to it; the Wikidata country join is not evidence."),
    unresolved("journey", "Matt Brown", "No company named Journey with a Headline round was found."),
    cls("root", flags=["model_disputes_source"], note="placeholder"),
    unresolved("keeper", "Mathias Schilling and Kate Liu (Asia desk)", "Keeper the AI matchmaking app (pre-seed $4M led by Lightbank) shows no Headline round."),
    unresolved("nouri", "Mathias Schilling", "No company named Nouri with a Headline round was found."),
    verdict("roadrunner", "member",
            "Hidden CMS doc referenced to the Global Growth fund page, corroborated: RoadRunner Recycling's $28.6M Series C was co-led by e.ventures and Greycroft, and King Goh of e.ventures Growth joined the board (Business Wire 2020-03-17).",
            ec="web", conf="high", cite=RR),
    cls("roadrunner", status="private", country="US", city="Pittsburgh", rng="below_1b", stage="Growth",
        stage_src="web_verified", stage_conf="high", stage_cite=RR, entry_date="2020-03",
        note="RoadRunner Recycling (Pittsburgh): Series C $28.6M co-led by e.ventures and Greycroft with Franklin Templeton (2020-03-17), from the growth fund; Series D 2022 ($70M, BeyondNetZero) and a Fifth Wall extension.",
        rounds=[rnd("2020-03-17", "Series C", 28600000, "e.ventures; Greycroft", True, RR, "press")]),
    cls("zippia", city="San Mateo", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=ZIP,
        entry_date="2019-04",
        note="Zippia, the careers site, San Mateo: E.ventures led the $8.5M Series A and Thomas Gieselmann joined the board (release 2019-04-22).",
        rounds=[rnd("2019-04-22", "Series A", 8500000, "e.ventures", True, ZIP, "company")]),
]
# Root: the Wikidata join gave JP; Matt Brown is on the US desk.
L[6] = unresolved("root", "Matt Brown", "The Wikidata country join (JP) matched another Root and is disputed.")
L[6]["flags"] = sorted(set(L[6]["flags"]) | {"model_disputes_source"})
if __name__ == "__main__":
    write("batch-007", L, record="--dry" not in sys.argv)
