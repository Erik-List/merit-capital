#!/usr/bin/env python3
"""Delta pass, tag d1, batch 1, first block (PRO-99): the graduation pass on 14 Seed rows.
Run: NQ_TAG=d1 python3 judgments-d1a.py

Skipped (JUDGE-BRIEF run notes, duplicates awaiting the merge): 3-v-biosciences, atara-bio, 360buy, alphabet-google,
entremed-inc, glori-oil, at-home-corp, delta-technology-holdings-ltd, homestore-com-inc.
Google News answered 503 all session (2026-09-30), so no headline was decoded: every non-TechCrunch URL below was
found through a publisher's own search page or a web search and read with WebFetch, unless the note says otherwise.
"""
import json

import judge_lib as jl
from judge_lib import cls, rnd, GNEWS, FORMD_CITE, GRADLINES, POST

L = []
ASOF = "2026-09-30"
_CLS = json.loads((jl.INV / "companies/classification.json").read_text())


def old(slug):
    return list((_CLS.get(slug) or {}).get("funding_rounds") or [])


def lines(slug, swap=None, extra=()):
    """GRADLINES with a surface line replaced where the default wording misreads the hits (swap: kind -> line)."""
    out = []
    for ln in GRADLINES(slug):
        k = ln.split(":", 1)[0]
        out.append((swap or {}).get(k, ln))
    return out + list(extra)


# URLs read in this pass.
BCG_AZARUS = "https://www.blockchaingamer.biz/news/28188/animoca-acquires-blockchain-streaming-platform-azarus/"
PRN_BLUEOAK = ("https://www.prnewswire.com/news-releases/blueoak-breaks-ground-on-first-us-urban-mining-refinery-to-"
               "retrieve-high-value-metals-from-e-waste-closes-35m-in-project-financing-262504051.html")
HOSPICE_MEDARRIVE = "https://hospicenews.com/2021/11/23/medarrive-gains-25-million-in-series-a-funds/"
PULSE_MINE = "https://pulse2.com/mine-14-million-series-a/"
ALLEY_PATTERN = "https://www.alleywatch.com/2019/08/pattern-equal-partners-cookware-emmitt-shine-nick-ling/"
BIOSPACE_OPHTH_D = "https://www.biospace.com/ophthonix-inc-completes-series-d-financing-at-35-1-million"
# The company's own release, cited on the GV book's Shape Security row and re-read here.
GLOBE_SHAPE = ("https://www.globenewswire.com/news-release/2012/07/02/969278/0/en/"
               "Google-Ventures-Joins-Shape-Security-Series-A-Funding-Round.html")

TC_BLUEOAK = GNEWS("blueoak", "Raises $35 Million")
TC_OFFER_SEED = GNEWS("offermatic", "Now Open To The Public")
TC_OFFER_A = GNEWS("offermatic", "Raises $4.5 Million")
TC_RETYM = GNEWS("retym", "pour another $75M")

# azarus: seed June 2019; a second, unnamed round in 2022 took the total to $5.8M; Animoca bought it in October 2023.
L.append(cls("azarus", entry_date="2019-06", grad="not_graduated", grad_src="web_verified", grad_cite=BCG_AZARUS,
             grad_conf="medium", grad_asof=ASOF,
             surfaces=lines("azarus", swap={
                 "googlenews": "googlenews: Google News, the company's name with round and exit words -> 5 headlines "
                               "naming the company, the acquisition by Animoca Brands (BlockchainGamerBiz, 2023-10-30; "
                               "games.gg) and product news; no Series A or later round"},
                 extra=["blockchaingamer: BlockchainGamer.biz's own search for Azarus -> the 2019 seed report and the "
                        "acquisition report, which says Azarus 'raised $5.8 million in two funding rounds in 2019 and "
                        "2022'; neither round is named a Series A"]),
             rounds=old("azarus") + [rnd("2022", "unnamed round", 4000000, None, None, BCG_AZARUS, "press")],
             note="S2A: not graduated. BlockchainGamer.biz (2023-10-30): Animoca Brands acquired Azarus, which had "
                  "'raised $5.8 million in two funding rounds in 2019 and 2022'; the 2022 round (about $4M after the "
                  "$1.8M seed) is unnamed and under the $5M step, and the sale ended the chance of a Series A."))

# blueoak: the Form D layer's no stands; the 2014 money was project financing for the Arkansas plant.
L.append(cls("blueoak", entry_date="2011-09-14", grad="not_graduated", grad_src="formd",
             grad_cite=FORMD_CITE("blueoak", 0), grad_conf="medium", grad_asof=ASOF,
             surfaces=lines("blueoak", swap={
                 "techcrunch": "techcrunch: TechCrunch's own search -> 1 headline naming the company, 'BlueOak Raises "
                               "$35 Million For Its Factory That Mines Electronics' (2014-06-10): project financing "
                               "for the Arkansas plant, not a priced round of the company; no Series A or later round"},
                 extra=["prnewswire: the company's own release of 2014-06-10 -> '$35M in project financing' towards "
                        "the Osceola facility from a state pension fund, a state development authority, tax-credit "
                        "lenders and an unnamed investor consortium; no round of the company is named"]),
             rounds=[rnd("2011-09-14", "Seed", 5224544, None, True, FORMD_CITE("blueoak", 0), "filing"),
                     rnd("2014-06-10", "project financing (Arkansas plant)", 35000000, None, None, TC_BLUEOAK, "press")],
             note="S2A: not graduated, as the Form D layer reads. The one later raise is the $35M of June 2014, which "
                  "TechCrunch and the company's release call project financing for the Osceola plant (pension fund, "
                  "state development authority, tax-credit lenders), not a priced round of BlueOak Resources; the "
                  "plant was reported shutting in November 2018 (Resource Recycling). TechCrunch puts the initial "
                  "raise from Kleiner Perkins and Terawatt at $7.5M."))

# convoke: a bare 2024 entry is read at 2024-12-31, inside the window.
L.append(cls("convoke", entry_date="2024", grad="censored",
             note="S2A: censored. The entry year 2024 is read at its last day, under 24 months before 2026-09-30, "
                  "and the seed was only announced in August 2025."))

# genentech: 1976 seed; the firm's own case study gives the October 1980 IPO, $35M.
GEN = POST("genentech")
L.append(cls("genentech", entry_date="1976", grad="graduated", grad_src="first_party", grad_cite=GEN,
             grad_conf="high",
             rounds=old("genentech") + [rnd("1980-10", "IPO", 35000000, "Hambrecht & Quist (underwriter)", None, GEN,
                                            "firm")],
             note="S2A: graduated. The firm's own case study says the 1980 IPO 'raised $35 million', a later priced "
                  "financing far above the $5M step for a 1976 seed; no earlier venture round is cited."))

# medarrive: seed December 2020, Series A November 2021.
L.append(cls("medarrive", entry_date="2020-12-03", grad="graduated", grad_src="web_verified",
             grad_cite=HOSPICE_MEDARRIVE, grad_conf="high",
             rounds=old("medarrive") + [
                 rnd("2021-11", "Series A", 25000000, "Section 32", True, HOSPICE_MEDARRIVE, "press"),
                 rnd("2022-01-28", "unnamed (Form D)", 32846769, None, None,
                     FORMD_CITE("medarrive", 1), "filing"),
                 rnd("2023-03-31", "unnamed (Form D)", 10000000, None, None, FORMD_CITE("medarrive", 0), "filing")],
             note="S2A: graduated, the $25M Series A of November 2021 led by Section 32, with Kleiner Perkins among "
                  "the existing investors taking part (Hospice News, 2021-11-23)."))

# mine (formerly Fizz): the January 2026 round is named a Series A.
L.append(cls("mine", entry_date="2021", grad="graduated", grad_src="web_verified", grad_cite=PULSE_MINE,
             grad_conf="medium",
             rounds=old("mine") + [rnd("2026-01-26", "Series A", 14000000, "359 Capital", True, PULSE_MINE, "press")],
             note="S2A: graduated. Pulse 2.0 (2026-01-26): 'Mine, formerly known as Fizz, raised a $14 million "
                  "Series A' led by 359 Capital with Kleiner Perkins taking part, total raised $28M; medium because "
                  "FinSMEs reports the same round without a round name."))

# nexus-dx: the Form D layer's no; both September 2009 filings carry one sale date.
L.append(cls("nexus-dx", entry_date="2009-09-16", grad="not_graduated", grad_src="formd",
             grad_cite=FORMD_CITE("nexus-dx", 0), grad_conf="high", grad_asof=ASOF, surfaces=lines("nexus-dx"),
             note="S2A: not graduated, as the Form D layer reads. The two filings share the sale date 2009-09-16 "
                  "(one round), no later round is on file or in the press surfaces, and the company went into ITC "
                  "Nexus Holding in 2010."))

# offermatic: the firm was in the $750K seed of December 2010 and led the Series A of March 2011.
L.append(cls("offermatic", stage="Seed", stage_src="web_verified", stage_cite=TC_OFFER_SEED, stage_conf="high",
             entry_date="2010-12-08", grad="graduated", grad_src="web_verified", grad_cite=TC_OFFER_A,
             grad_conf="high", flags=["model_disputes_source"],
             rounds=[rnd("2010-12-08", "Seed", 750000, None, True, TC_OFFER_SEED, "press"),
                     rnd("2011-03-09", "Series A", 4500000, "Kleiner Perkins Caufield & Byers", True, TC_OFFER_A,
                         "press")],
             note="S2A: graduated, disputing the Form D layer, which anchored the entry on the Series A filing. "
                  "TechCrunch (2010-12-08): 'closed a $750,000 seed round with participation from Kleiner Perkins, "
                  "Bessemer, and angel investors'; TechCrunch (2011-03-09): '$4.5 million in funding in a Series A "
                  "round led by early backer Kleiner Perkins'. The founder launched another company in September "
                  "2012."))

# ophthonix-inc: not a seed. The firm was an existing investor at the Series D of December 2006.
L.append(cls("ophthonix-inc", stage="undetermined", flags=["stage_disputes_band"],
             rounds=[rnd("2006-12-14", "Series D", 35100000, "DAG Ventures", True, BIOSPACE_OPHTH_D, "company"),
                     rnd("2010-03-05", "unnamed (Form D)", 4906297, None, None, FORMD_CITE("ophthonix-inc", 0), "filing"),
                     rnd("2010-09-16", "unnamed (Form D)", 12137189, None, None, FORMD_CITE("ophthonix-inc", 1), "filing")],
             extra={"entry_stage_source": None, "entry_date": None},
             note="Stage disputes the Form D seed band: the company's Series D release (2006-12-14, $35.1M led by "
                  "DAG Ventures) names Kleiner Perkins Caufield & Byers among the existing investors that joined, so "
                  "the entry predates the filings and the 2010 round is a follow-on. The entry round itself is not "
                  "named in any source read, so the stage is undetermined and the row carries no S2A, as its "
                  "duplicates izon-formerly-ophthonix and opthonix read."))

# opstrace: one seed filing, then GitLab bought it in December 2021.
L.append(cls("opstrace", entry_date="2020-04-22", grad="not_graduated", grad_src="formd",
             grad_cite=FORMD_CITE("opstrace", 0), grad_conf="high", grad_asof=ASOF, surfaces=lines("opstrace"),
             note="S2A: not graduated, as the Form D layer reads: the $6.5M seed filing of April 2020 is the only "
                  "round on file or in the press surfaces before GitLab's acquisition in December 2021."))

# pattern (Pattern Brands): the May 2019 round is the Series A.
L.append(cls("pattern", entry_date="2018-11-19", grad="graduated", grad_src="web_verified", grad_cite=ALLEY_PATTERN,
             grad_conf="medium", flags=["model_disputes_source"],
             rounds=[rnd("2018-11-19", "Seed (Form D)", 5203456, None, True, FORMD_CITE("pattern", 0), "filing"),
                     rnd("2019-05-15", "Series A", 8775900, "Kleiner Perkins; Primary Venture Partners; RRE", True,
                         ALLEY_PATTERN, "press")],
             note="S2A: graduated, disputing the Form D layer, whose step-up test cannot see a round's name. "
                  "AlleyWatch (2019-08-20): 'In 2019 Pattern raised a total of $14M in a Series A round led by "
                  "Kleiner Perkins, Primary Ventures, and RRE'; the filings split that $14M into a $5.2M round first "
                  "sold 2018-11-19 (the firm's 2018 entry) and an $8.8M round first sold 2019-05-15, the named "
                  "Series A. Medium because the article does not separate the two closes; later raises of $60M "
                  "(2021) and $25M (2022) are in the Google News headlines."))

# retym: the firm led the 2021 seed; Series D in March 2025.
L.append(cls("retym", entry_date="2021", grad="graduated", grad_src="web_verified", grad_cite=TC_RETYM,
             grad_conf="high",
             rounds=old("retym") + [
                 rnd("2023-05-17", "unnamed (Form D)", 59999959, None, None, FORMD_CITE("retym", 0), "filing"),
                 rnd("2025-03-31", "Series D", 75000000, "Spark Capital", True, TC_RETYM, "press")],
             note="S2A: graduated. TechCrunch (2025-03-31): 'a fresh $75 million series D led by James Kuklinski of "
                  "Spark Capital', total raised $180M, with Kleiner Perkins taking part again; a $60M round is on "
                  "Form D in May 2023."))

# shape-security: the April 2012 round the firm led is the Series A, not a seed.
L.append(cls("shape-security", stage="Series A", stage_src="web_verified", stage_cite=GLOBE_SHAPE, stage_conf="high",
             entry_date="2012-04-09", flags=["stage_disputes_band"],
             rounds=[rnd("2012-04-09", "Series A", 5784998, "Kleiner Perkins Caufield & Byers; TomorrowVentures", True,
                         GLOBE_SHAPE, "company"),
                     rnd("2012-12-21", "unnamed (Form D)", 20000001, None, None, FORMD_CITE("shape-security", 1), "filing"),
                     rnd("2014-02-21", "unnamed (Form D)", 40000163, None, None, FORMD_CITE("shape-security", 2), "filing")],
             note="Stage disputes the Form D seed band: the company's release of 2012-07-02 says 'Shape's Series A "
                  "round was led by Kleiner Perkins Caufield & Byers and Google Executive Chairman Eric Schmidt's "
                  "TomorrowVentures', the round the April 2012 Form D ($5.8M) records, as the GV book reads. A "
                  "Series A entry carries no S2A."))

# siluria-technologies: the Form D layer's yes.
L.append(cls("siluria-technologies", entry_date="2009-06-05", grad="graduated", grad_src="formd",
             grad_cite=FORMD_CITE("siluria-technologies", 1), grad_conf="high",
             rounds=[rnd("2009-06-05", "Seed (Form D)", 3268293, None, True, FORMD_CITE("siluria-technologies", 0), "filing"),
                     rnd("2011-06-15", "unnamed (Form D)", 21990592, None, None, FORMD_CITE("siluria-technologies", 1), "filing")],
             note="S2A: graduated, as the Form D layer reads: the $3.3M entry round of June 2009 was followed by a "
                  "$22M round first sold in June 2011, and three larger ones after it."))

if __name__ == "__main__":
    jl.write("d1a", L)
