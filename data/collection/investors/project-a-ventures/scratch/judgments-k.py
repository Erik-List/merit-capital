"""Grind batch K (PRO-102): rows from research-g2/g3.json (every URL re-loaded by the research agents)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as J  # noqa: E402
from judge_lib import cls, write, LISTING, surfaces_lines, ASOF, ec, sc, gc, RS  # noqa: E402
from judge_lib import rrounds as rounds  # noqa: E402

L = []
NOVAL = {"valuation_source": None, "valuation_asof": None, "valuation_confidence": None}


def cfcap(slug, key="cf_investment"):
    v = J.fields(slug, key) or J.fields(slug, "page_investment")
    return v[0][1]


def fd(name):
    return f"formd: EDGAR company and full-text search for '{name}' (2026-09-30) -> no Form D filed by the company"


L.append(cls("adtrade", status="acquired", rng="below_1b", stage="undetermined", country="BR", city="São Paulo",
             country_cite=cfcap("adtrade", "page_location") if J.fields("adtrade", "page_location") else J.cap("adtrade"),
             focus="Media, Gaming & Advertising", extra={"status_citation": sc("adtrade")},
             note="Real-time-bidding display advertising agency for Latin America, São Paulo (founded 2013), one of Project "
                  "A's Brazilian company-builder projects on its 2013 portfolio page; no round is on record. acq. by ESV Digital, "
                  "July 2014 ('ESV Digital has acquired Adtrade', ESV's own post); Project A's ESV Digital Brazil joint venture "
                  "is its own row.", rounds=rounds("adtrade")))
L.append(cls("andercore", status="private", rng="below_1b", stage="Pre-Seed", stage_src="first_party", stage_conf="medium",
             stage_cite=LISTING, entry_date="2021", country="DE", city="Berlin", country_cite=LISTING,
             focus="Consumer & Marketplaces",
             note="AI-based B2B trade platform for construction and industrial goods, Berlin (founded 2021). Pre-seed by the "
                  "firm's own record (CMS, Fund III); 'The startup received early backing from Project A, Foundamental, and a "
                  "number of business angels' (Bau Rockstars). Series A 2023, $40M Series B Feb 2026 with Project A (tech.eu).",
             rounds=rounds("andercore")))
L.append(cls("carl-finance", status="acquired", rng="below_1b", stage="Seed", stage_src="first_party", stage_conf="medium",
             stage_cite=LISTING, entry_date="2019-06", grad="not_graduated", grad_src="web_verified", grad_cite=sc("carl-finance"),
             grad_asof=ASOF, surfaces=surfaces_lines("carl-finance", "no round after the June 2019 seed; merged into "
                                                                     "Doubledigit in January 2023"),
             country="DE", city="Berlin", country_cite=LISTING, focus="Fintech & Payments",
             extra={"status_citation": sc("carl-finance")},
             note="M&A platform for the mid-market (Carl), Berlin (founded 2016). 'The round is led by the Berlin VC Project A' "
                  "(the firm's release, June 2019), a seed by the firm's own record (CMS, Fund III). Carl became a subsidiary "
                  "of Doubledigit in January 2023, its shareholders taking parent shares and cash (FinanceFWD): acquired, "
                  "with no later round.", rounds=rounds("carl-finance")))
L.append(cls("copay", status="private", rng="below_1b", stage="Pre-Seed", stage_src="first_party", stage_conf="medium",
             stage_cite=LISTING, entry_date="2023", country="GB", city="London", country_cite=LISTING,
             focus="Fintech & Payments",
             note="Early payment between main contractors and subcontractors in UK construction (Copay Technologies Ltd), "
                  "London (founded 2023). Pre-seed 2023 by the firm's own record (CMS, Fund IV; the archive says Seed, the CMS "
                  "wins, R2); no announcement of any round.", rounds=rounds("copay")))
L.append(cls("expressgroup", status="defunct", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("expressgroup"), entry_date="2022-04", country="DE", city="Hamburg", country_cite=LISTING if J.live("expressgroup") else cfcap("expressgroup", "cf_location"),
             focus="Fintech & Payments", extra={"status_citation": sc("expressgroup")},
             note="Tax-refund app for employees (ExpressSteuer, later Express Group), Hamburg (founded 2019). The ~EUR 25M "
                  "Series A of April 2022 was led by Insight Partners and 'Project A ... also participated' (Willkie). A "
                  "provisional insolvency administrator was appointed on 2023-12-12 and the company has been in liquidation "
                  "since March 2024, with no sale (North Data): defunct.", rounds=rounds("expressgroup")))
L.append(cls("profian", status="defunct", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("profian"), entry_date="2021-09", grad="not_graduated", grad_src="web_verified",
             grad_cite=sc("profian"), grad_asof=ASOF,
             surfaces=surfaces_lines("profian", "no round after the September 2021 seed; the board closed the company in "
                                                "January 2023") + [fd("Profian")],
             country="US", city="Raleigh", country_cite=sc("profian"), focus="Security",
             extra={"status_citation": sc("profian")},
             note="Confidential-computing software (Enarx), Raleigh, NC (founded 2021). The $5M seed 'was co-led by Project A "
                  "Ventures and Illuminate Financial' (Private Equity Wire, Sept 2021), its first round. 'In mid-January 2023, "
                  "we, the board, decided to close down the company' (the CEO's post).", rounds=rounds("profian")))
L.append(cls("tabular", status="private", rng="below_1b", stage="Pre-Seed", stage_src="first_party", stage_conf="medium",
             stage_cite=LISTING, entry_date="2024", country="DE", city="Berlin", country_cite=LISTING, focus="SaaS",
             note="Accounting automation (brand Tabula; Tabula GmbH, formerly Skipper Technologies UG), Berlin (founded 2024; YC "
                  "S24). Pre-seed 2024 by the firm's own record (CMS, Fund IV); no announced round. Not Databricks' Tabular (a16z's "
                  "row).", rounds=rounds("tabular")))
L.append(cls("alvin", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("alvin"), entry_date="2022-10", grad="not_graduated", grad_src="absence_check", grad_asof=ASOF,
             surfaces=surfaces_lines("alvin", "no round after the October 2022 seed") + [fd("Alvin AI")],
             country="US", city="New York", country_cite=LISTING, focus="Data Infrastructure",
             note="Data lineage, then automated BigQuery cost optimisation (Alvin AI), New York (founded in Tallinn, 2018). "
                  "'Project A Ventures led the round', the EUR 6.1M seed announced Oct 2022 (AIN; the firm's CMS says series_a "
                  "2021, the announcement settles it). No later round.", rounds=rounds("alvin")))
L.append(cls("distil-labs", status="private", rng="below_1b", stage="Pre-Seed", stage_src="first_party", stage_conf="medium",
             stage_cite=LISTING, entry_date="2024", country="DE", city="Berlin", country_cite=LISTING, focus="AI & Applied AI",
             note="Small task-specific language models (Distil Labs GmbH), Berlin (founded 2024). Pre-seed 2024 by the firm's "
                  "own record (CMS, Fund IV), the only source for the round; a capital increase in July 2025.",
             rounds=rounds("distil-labs")))
L.append(cls("esv-digital-brazil", status="unknown", rng="below_1b", stage="undetermined", country="BR", city="São Paulo",
             country_cite=cfcap("esv-digital-brazil", "cf_location"), focus="Media, Gaming & Advertising",
             note="Performance-marketing agency, São Paulo: a joint venture the firm lists as its own ('Joint Venture', founded "
                  "01/2013) from its Brazilian company-builder period with the French group ESV Digital, which bought Project "
                  "A's Adtrade in 2014. No round (a joint-venture stake, judged as the firm's listed position like HV's "
                  "Audible.de). Listed as active through July 2024, but its domains no longer resolve and no dissolution is on "
                  "record: unknown.", rounds=rounds("esv-digital-brazil")))
L.append(cls("gigapipe", status="defunct", rng="below_1b", stage="Seed", stage_src="first_party", stage_conf="medium",
             stage_cite=cfcap("gigapipe"), entry_date="2021-05", grad="not_graduated", grad_src="web_verified",
             grad_cite=ec("gigapipe"), grad_asof=ASOF,
             surfaces=surfaces_lines("gigapipe", "no round after the May 2021 entry; the company was struck off in March 2024"),
             country="GB", city="London", country_cite=cfcap("gigapipe", "cf_location"), focus="Data Infrastructure",
             note="Observability data platform (Gigapipe Ltd), London (founded 2020). Seed by the firm's own record (archive); "
                  "Companies House shows Uwe Horstmann appointed director on 2021-05-27, the day of an allotment. The company "
                  "applied for voluntary strike-off in Dec 2023 and was dissolved on 2024-03-12 with no sale; the Gigapipe name "
                  "now belongs to the qryn project's rebrand. Defunct, not graduated.", rounds=rounds("gigapipe")))
L.append(cls("kochzauber", status="acquired", rng="below_1b", stage="Seed", stage_src="first_party", stage_conf="medium",
             stage_cite=cfcap("kochzauber"), entry_date="2012-06", grad="not_graduated", grad_src="web_verified",
             grad_cite=sc("kochzauber"), grad_asof=ASOF,
             surfaces=surfaces_lines("kochzauber", "no named round after the 2012 seed; the Otto group's myToys took a majority "
                                                   "in 2014 and Lidl bought the company in November 2015"),
             country="DE", city="Berlin", country_cite=cfcap("kochzauber", "cf_location"), focus="Consumer & Marketplaces",
             extra={"status_citation": sc("kochzauber")},
             note="Meal-kit delivery, Berlin (founded Feb 2012), a Project A company build; seed 2012 by the firm's own record "
                  "(archive, 2012-06). The Otto group's myToys took about 76% in 2014, and Lidl took over Kochzauber completely "
                  "in November 2015 (Lebensmittel Praxis).", rounds=rounds("kochzauber")))
L.append(cls("landmark-games", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("landmark-games"), entry_date="2022", grad="not_graduated", grad_src="absence_check", grad_asof=ASOF,
             surfaces=surfaces_lines("landmark-games", "no round after the 2022 seed"),
             country="GB", city="London", country_cite=LISTING if J.live("landmark-games") else cfcap("landmark-games", "cf_location"),
             focus="Media, Gaming & Advertising",
             note="Mobile games studio (Sea of Souls), London (founded 2021). The $4.6M seed 'was led by Project A Ventures and "
                  "InReach Ventures' after a pre-seed by Moonfire and Concept (tech.eu, Nov 2022; shares allotted Aug 2022, and "
                  "the firm listed the studio from Dec 2021). No later round.", rounds=rounds("landmark-games")))
L.append(cls("loopline", status="acquired", rng="below_1b", stage="undetermined", country="DE", city="Berlin",
             country_cite=LISTING, focus="SaaS", extra={"status_citation": sc("loopline")},
             note="HR performance-feedback software (Loopline Systems), Berlin: a Project A spin-off (LLS Internet GmbH, 2014). "
                  "The firm calls its first money seed, but the company then raised a 'second round of financing' in 2016 and a "
                  "seven-digit round in 2018 whose amounts are not on record, so a graduation can be neither shown nor ruled "
                  "out and the entry reads undetermined. The operating company became insolvent in August 2020 and the product "
                  "continues under a new Loopline Systems GmbH run by a co-founder (an asset transfer out of insolvency, "
                  "inferred from the register).", rounds=rounds("loopline")))
L.append(cls("popdust", status="private", rng="below_1b", stage="undetermined", country="US", city="New York",
             country_cite=J.cap("popdust"), focus="Media, Gaming & Advertising", extra={"status_citation": sc("popdust")},
             note="Music and pop-culture publisher, New York (founded 2011). Listed on the firm's May 2013 portfolio page, the "
                  "only tie to Project A; its 2012 Form D ($4.5M, eight investors) names no investor and no round names Project "
                  "A. Still publishing under Popdust, Inc.", rounds=rounds("popdust")))
L.append(cls("restabilise", status="private", rng="below_1b", stage="Pre-Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=ec("restabilise"), entry_date="2025-11", country="GB", city="London", country_cite=LISTING,
             focus="Crypto & Web3",
             note="Sterling stablecoin issuer, London (founded 2025). 'The investment round was led by Project A', the GBP 2.82M "
                  "pre-seed of Nov 2025 (Goodwin); picked for the FCA's stablecoin sandbox in Feb 2026.",
             rounds=rounds("restabilise")))
L.append(cls("shirtagram", status="unknown", rng="below_1b", stage="undetermined", country="DE", country_src="model_knowledge",
             focus="Consumer & Marketplaces", flags=["country_prior", "city_unknown"],
             note="Photo-to-merchandise gift app. Listed on the firm's May 2013 portfolio page only (gone by December 2013), "
                  "most likely one of Project A's own early app experiments; no round, register entry or news exists, and the "
                  "app's domain lapsed. Status unknown; the country is the Berlin desk prior.", rounds=[]))
L.append(cls("twig", status="private", rng="below_1b", stage="Seed", stage_src="first_party", stage_conf="medium",
             stage_cite=cfcap("twig"), entry_date="2023-09", grad="not_graduated", grad_src="absence_check", grad_asof=ASOF,
             surfaces=surfaces_lines("twig", "no round after the GBP 3M raised in September 2023"),
             country="GB", city="London", country_cite=cfcap("twig", "cf_location") if J.fields("twig", "cf_location") else LISTING,
             focus="Climate & Energy",
             note="Sustainable ingredients from synthetic biology, AI and robotics (Twig Bio Ltd), London (founded 2022). The "
                  "GBP 3M raised in Sept 2023 'came from Project A, Seedcamp, Zero Carbon Capital' and others (Tech Funding "
                  "News); seed by the firm's own record. No later round beyond small allotments.", rounds=rounds("twig")))
L.append(cls("waypoint", status="private", rng="below_1b", stage="Seed", stage_src="first_party", stage_conf="medium",
             stage_cite=LISTING, entry_date="2024-06", grad="not_graduated", grad_src="absence_check", grad_asof=ASOF,
             surfaces=surfaces_lines("waypoint", "no round after the June 2024 seed"),
             country="GB", city="London", country_cite=LISTING, focus="Consumer & Marketplaces",
             flags=["model_disputes_source"], extra=NOVAL,
             note="B2B marketplace for chemicals and fertiliser (Waypoint Commodities Ltd), London (founded 2022). Seed 2024 by "
                  "the firm's own record (CMS, Fund IV; a June 2024 allotment at Companies House); no later round. The Wikidata "
                  "join (a US company, acquired) and YC's Waypoint (an email API) are namesakes.", rounds=rounds("waypoint")))

if __name__ == "__main__":
    write("batch-k", L)
