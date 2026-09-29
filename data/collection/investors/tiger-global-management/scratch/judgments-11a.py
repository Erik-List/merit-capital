#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 11, chunk a (rows 1-15). Run: NQ_TAG=b11 python3 judgments-11a.py

Every citation comes from a helper that reads a URL already on disk: the row's evidence view
(PR / SECU / REC), the press caches (NEWS, incl. this judge's Bing items), Wikipedia (W), a
filing link on the row (SEC), or a sibling book's recorded citation (SIB)."""
import json
import re
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import judge_lib as jl  # noqa: E402
from judge_lib import verdict, cls, rnd, W, NEWS, SEC  # noqa: E402,F401

PK = json.loads((HERE / "evidence-pack.json").read_text())
INV = HERE.parents[1]


def _one(urls, what):
    urls = list(dict.fromkeys(u for u in urls if u))
    if len(urls) != 1:
        raise SystemExit(f"{what}: {len(urls)} matches {urls[:3]}")
    return urls[0]


def PR(slug, sub):
    """The URL printed on the one press line of the evidence view containing `sub`."""
    out = []
    for x in PK.get(slug, {}).get("press") or []:
        if sub.lower() in x.lower() and "|| URL " in x:
            out.append(x.split("|| URL ", 1)[1].split(" || ")[0].strip())
    return _one(out, f"PR({slug!r}, {sub!r})")


def SECU(slug, sub):
    """The filing URL printed on the one `sec` line of the evidence view containing `sub`."""
    out = [x.rsplit(" | ", 1)[1].strip() for x in PK.get(slug, {}).get("sec") or []
           if sub.lower() in x.lower()]
    return _one(out, f"SECU({slug!r}, {sub!r})")


def REC(slug):
    """The citation URL at the end of the row's RECALL line."""
    b = PK.get(slug, {}).get("recall_basis") or ""
    return _one(re.findall(r"\((https?://[^\s)]+)\)\s*$", b), f"REC({slug!r})")


def SIB(inv, slug, key):
    """A citation a sibling book recorded on its own row for the same company."""
    c = json.loads((INV / inv / "companies" / "classification.json").read_text())
    v = (c.get(slug) or {}).get(key)
    if not (isinstance(v, str) and v.startswith("http")):
        raise SystemExit(f"SIB({inv!r}, {slug!r}, {key!r}): nothing on disk")
    return v


L = []

# 1. Portside: Form D director seat (John Curtius, in tenure) + the press round.
u = NEWS("portside-inc", "Portside raises $17M for its business aviation")
L.append(verdict("portside-inc", "member",
                 "Yahoo Finance (TechCrunch, 2021-05-20): Portside 'has raised a $17 million funding round led by "
                 "Tiger Global Management'; John Curtius, a Tiger partner in tenure, is director on the company's "
                 "2021 Form D ($19.0M sold)", ec="web", conf="high", cite=u))
L.append(cls("portside-inc", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=u, stage_conf="medium",
             city="San Francisco", focus="SaaS",
             rounds=[rnd("2021-05", "Series A (the article gives no letter; the next round is named Series B)",
                         17_000_000, "Tiger Global Management", True, u),
                     rnd("2023-02", "Series B", 50_000_000, "Insight Partners", None,
                         NEWS("portside-inc", "Raises $50M in a Series B Investment")),
                     rnd("2024-05", "strategic growth investment", None, "Vista Equity Partners", None,
                         NEWS("portside-inc", "Strategic Growth Investment Led by Vista"))],
             note="Business-aviation operations software (flight departments, charter, fractional fleets), San "
                  "Francisco (the company's 2024 release is datelined there; the 2021 Form D files from Foster City). "
                  "Tiger led the $17M round of May 2021 with I2BF and SOMA as existing investors; the company named "
                  "its next round (Insight Partners, $50M, 2023) the Series B, so Tiger's round was the Series A, as "
                  "the Form D band reads. Vista Equity invested in 2024 and 2026; no priced $1B mark."))

# 2. Postmates: Uber's S-4 names the PIP IX vehicles as 27.2% holders while private.
u = SECU("postmates-inc", "Uber's S-4")
L.append(verdict("postmates-inc", "member",
                 "Uber's S-4 for Postmates (2020-08-07): entities associated with Tiger Global, among them Tiger "
                 "Global Private Investment Partners IX and Tiger Global PIP IX Holdings (which designates a "
                 "Postmates director), hold 27.2% of the private company; Tiger also led the $300M round of "
                 "September 2018 (WSJ, Bloomberg) and Lee Fixel, a Tiger partner in tenure, is director on the "
                 "2015 Form D", ec="fund_filing", conf="high", cite=u))
L.append(cls("postmates-inc", status="acquired", rng="below_1b", city="San Francisco",
             focus="Consumer & Marketplaces",
             note="On-demand delivery, San Francisco. Acquired by Uber in an all-stock deal closed December 2020 "
                  "(about $2.65B), so no standalone mark. Entry kept from the Form D band (the June 2015 round, "
                  "Growth), with Lee Fixel on that filing; Tiger later led the September 2018 $300M round."))

# 3. Prefect: Tiger led the Series B.
u = REC("prefect")
L.append(cls("prefect", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-06",
             country="US", city="Washington", focus="Data Infrastructure",
             rounds=[rnd("2021-06-10", "Series B", 32_000_000, "Tiger Global", True, u, "company")],
             note="Prefect Technologies, open-source dataflow orchestration, Washington, D.C. (TechTarget: 'based "
                  "in Washington, D.C.'). Tiger led the $32M Series B of June 2021 (the company's release), which "
                  "took total funding to $57.6M; no earlier round names Tiger. Momentum slice (data infrastructure, "
                  "first seen 2021), checked 2026-09-29 on Bing News: no later priced round or $1B mark."))

# 4. Primetrace (Kutumb's parent): Tiger led the June 2021 Series A.
u = NEWS("primetrace", "Kutumb raises $26M in Series A")
L.append(verdict("primetrace", "member",
                 "YourStory (2021-06-20): 'Community platform Kutumb raises $26M in Series A round led by Tiger "
                 "Global'; Primetrace Technologies is Kutumb's company (Moneycontrol 2026-07-29: 'Primetrace last "
                 "raised a $26 million Series A round in June 2021 from Tiger Global, Peak XV Partners')",
                 ec="web", conf="high", cite=u))
L.append(cls("primetrace", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-06",
             country="IN", country_src="web_verified", country_cite=u, city="Bangalore",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2021-06", "Series A", 26_000_000, "Tiger Global", True, u)],
             note="Primetrace Technologies runs the Kutumb community app and Crafto; Bangalore-based (YourStory). "
                  "Tiger led the $26M Series A of June 2021 (Inc42 had reported the talks in March 2021). In "
                  "talks in July 2026 to raise $50M at $500M (Moneycontrol), below $1B. The base also carries a "
                  "'kutumb' row for the same company."))

# 5. Pristyn Care: Tiger led the Series D.
u = REC("pristyn-care")
L.append(cls("pristyn-care", status="private",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-04",
             city="Gurugram", focus="Healthcare & Bio",
             rounds=[rnd("2021-04", "Series D", 53_000_000, "Tiger Global Management", True, u)],
             note="Surgical-care provider, Gurugram. Tiger led the $53M Series D of April 2021 (YourStory; "
                  "Wikipedia), its first round in the company, and joined the Series E. Valuation left to the web "
                  "pass (needs_web_value)."))

# 6. Procore: the Series I IRA defines Tiger as Tiger Global PIP 11 LLC.
u = SECU("procore-technologies-inc", "Tiger Global PIP 11 LLC")
L.append(verdict("procore-technologies-inc", "member",
                 "Procore's IPO DRS/A exhibit (2020-01-13): the Sixth Amended and Restated Investor Rights "
                 "Agreement of 2019-09-24, entered into for the Series I preferred financing, defines 'Tiger' as "
                 "Tiger Global PIP 11 LLC, a private-equity vehicle, which signs as an investor while the company "
                 "was private", ec="fund_filing", conf="high", cite=u))
L.append(cls("procore-technologies-inc",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="medium", entry_date="2019-09",
             country="US", city="Carpinteria", focus="SaaS",
             rounds=[rnd("2019-09-24", "Series I", None, None, True, u, "filing")],
             note="Construction management software, Carpinteria (Wikipedia). Tiger's PIP 11 LLC came in with the "
                  "Series I financing of September 2019: the IRA of that date gives Tiger a Major Investor clause of "
                  "its own, which the prior IRA of July 2019 did not need. NYSE listing May 2021; the adviser's 13G "
                  "and 13F filings (2021-2026) are the listed position."))

# 7. Productboard: Tiger was in the April 2021 Series C before co-leading the D.
u = NEWS("productboard", "An all-star cast of VCs")
L.append(cls("productboard", status="private",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-04",
             city="San Francisco", focus="SaaS",
             rounds=[rnd("2021-04", "Series C", 72_000_000, None, True, u),
                     rnd("2022-02", "Series D", 125_000_000, "Dragoneer Investment Group and Tiger Global", True,
                         PR("productboard", "nasdaq.com/articles/dragoneer"))],
             note="Product management software, founded in Prague, headquartered in San Francisco (the prefilled "
                  "country US; Sequoia's row keeps Prague, the engineering base). Business Insider (2021-04-22): 'An "
                  "all-star cast of VCs, including Tiger Global and Sequoia, has invested another $72 million' (the "
                  "Series C), before Tiger co-led the $125M Series D at $1.73B in February 2022, the round the "
                  "recall headline names. Valuation left to the web pass (needs_web_value)."))

# 8. Progcap: Tiger co-led the Series B.
u = PR("progcap", "Tiger Global, Sequoia lead Series B funding in Progcap")
v = NEWS("progcap", "Fintech platform Progcap raises $40 mn")
L.append(cls("progcap", status="private", rng="below_1b", usd=600_000_000, val_src="web_verified", val_cite=v,
             asof="2022-06-27", extra={"valuation_range_source": "web_verified"}, flags=["stale"],
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-06",
             country="IN", country_src="web_verified", country_cite=u, city="New Delhi", focus="Fintech & Payments",
             rounds=[rnd("2019-07", "Series A", None, "Sequoia Capital India", False, None, "press"),
                     rnd("2021-06", "Series B", 25_000_000, "Tiger Global and Sequoia Capital India", True, u),
                     rnd("2021-10", "Series C", 30_000_000, "Tiger Global and Creation Investments", True,
                         REC("progcap")),
                     rnd("2022-06", "Series C extension", 40_000_000, "Tiger Global, Creation Investments, Google",
                         True, v)],
             note="Supply-chain lending to small retailers, New Delhi. Tiger co-led the $25M Series B of June 2021 "
                  "with Sequoia India (VCCircle); the 2019 Series A was Sequoia's alone. Mark: the $40M Series C "
                  "extension of June 2022 at $600M (Business Today), stale. Momentum slice (fintech, first seen "
                  "2021), checked 2026-09-29: a planned $45M raise for FY28, no $1B round."))

# 9. Public.com: the Tiger-led February 2021 round at $1.2B.
u = REC("public-com")
L.append(cls("public-com", status="private", rng="1b_plus", usd=1_200_000_000, val_src="web_verified",
             val_cite=u, asof="2021-02-11", extra={"valuation_range_source": "web_verified"}, flags=["stale"],
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="medium", entry_date="2021-02",
             country="US", city="New York", focus="Fintech & Payments",
             rounds=[rnd("2021-02", "growth round", 220_000_000, "Tiger Global", True, u),
                     rnd("2025-03", "investment", 200_000_000, "Tiger Global", True,
                         NEWS("public-com", "Robinhood backer Tiger Global leads"))],
             note="Public (Public Holdings), commission-free investing app, New York. Business Insider "
                  "(2021-02-11): valued at about $1.2B in a round led by Tiger ($220M). Wikipedia calls Tiger an "
                  "existing investor at that round, so its first check may be the December 2020 round; Growth "
                  "either way. Tiger also led a $200M investment in March 2025 (FinTech Futures; the page refused "
                  "the fetch and no valuation was read), so the 2021 mark stands, stale. Momentum slice checked "
                  "2026-09-29 (Google and Bing News): no later stated valuation."))

# 10. Pure Storage: the Series F IRA gives PIP VII a board observer seat.
u = SECU("pure-storage-inc", "board observer")
L.append(verdict("pure-storage-inc", "member",
                 "Pure Storage's IPO DRS exhibit (2015-05-15): the Amended and Restated Investor Rights Agreement "
                 "of 2014-04-17, entered into for the Series F preferred financing, names Tiger Global Private "
                 "Investment Partners VII (a private-equity vehicle) among the investors with a board observer "
                 "seat; Tiger's Form 3 at the October 2015 IPO reports PIP VII's 4.2M Class B shares",
                 ec="fund_filing", conf="high", cite=u))
L.append(cls("pure-storage-inc",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="medium", entry_date="2014-04",
             country="US", city="Santa Clara", focus="Data Infrastructure",
             rounds=[rnd("2013-08", "Series E", 150_000_000, None, None, None, "press"),
                     rnd("2014-04-17", "Series F", 225_000_000, None, True, u, "filing")],
             note="Flash storage, Santa Clara (NYSE: PSTG; renamed Everpure, as the Sutter Hill row records). The "
                  "April 2014 Series F IRA is the earliest record naming Tiger; the August 2013 Series E IRA it "
                  "replaced is not on file and the S-1 names no Tiger purchase, so Tiger may have entered at the "
                  "Series E. Growth either way."))

# 11. Qonto: Tiger co-led the Series D with TCV.
u = PR("qonto", "Qonto levanta 486 millones en una ronda liderada por Tiger Global")
L.append(cls("qonto", status="private",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2022-01",
             country="FR", country_src="web_verified", country_cite=W("Qonto"), city="Paris",
             focus="Fintech & Payments",
             rounds=[rnd("2020-01", "Series C", None, None, False, W("Qonto"), "press"),
                     rnd("2022-01", "Series D", None, "Tiger Global and TCV", True, u)],
             note="Business accounts for SMEs and freelancers, Paris ('a French financial technology company', "
                  "Wikipedia): the prefilled FR is right. Tiger co-led the EUR 486M Series D of January 2022 with "
                  "TCV at EUR 4.4B (Capitalbolsa; the November 2021 Business Insider report of the talks is the "
                  "recall headline); the EUR 104M round of January 2020 (Alven, Valar, Tencent) did not name "
                  "Tiger. Valuation left to the web pass (needs_web_value)."))

# 12. Qualia: Tiger led the Series C.
u = REC("qualia")
L.append(cls("qualia", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2019-11",
             country="US", city="San Francisco", focus="Fintech & Payments",
             rounds=[rnd("2019-11", "Series C", 55_000_000, "Tiger Global", True, u),
                     rnd("2020-12", "Series D", 65_000_000, None, None,
                         PR("qualia", "Qualia: $65 Million Series D, Over $1 Billion Valuation"))],
             note="Real-estate closing software, San Francisco. Tiger led the $55M Series C of November 2019 "
                  "(Crunchbase News). The $65M Series D of December 2020 was reported at 'over $1 billion' (Pulse "
                  "2.0, HousingWire), a threshold with no stated post-money; kept below_1b as the 8VC and Menlo "
                  "rows read (8VC's A/B pass recorded the same check under Rule A). Second look for Erik: moving "
                  "it to 1b_plus would move all three books."))

# 13. Qualified: Tiger first came in at the Series C.
u = W("Qualified (company)")
L.append(cls("qualified", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2022-04",
             country="US", city="San Francisco", focus="SaaS",
             rounds=[rnd("2020-08", "Series A", 12_000_000, "Norwest Venture Partners", False,
                         NEWS("qualified", "Qualified.com Closes $12 Million")),
                     rnd("2021-05", "Series B", 51_000_000, "Salesforce Ventures", False,
                         NEWS("qualified", "Qualified Secures $51M In Series B")),
                     rnd("2022-04", "Series C", 95_000_000, "Sapphire Ventures", True, u)],
             note="Pipeline generation (conversational marketing, the Piper AI agent) for Salesforce users, San "
                  "Francisco (the release's dateline). Tiger's first round is the $95M Series C of April 2022: "
                  "'major investment from Tiger Global alongside existing investors Norwest, Redpoint and "
                  "Salesforce Ventures' (Business Wire), so it was new then. No valuation stated; no later $1B "
                  "round found (2026-09-29)."))

# 14. Qualio: Tiger led the Series B (membership open).
u = PR("qualio", "Irish-founded Qualio raises $50m")
L.append(verdict("qualio", "member",
                 "SiliconRepublic (2021-05-25): 'The round was led Tiger Global' (the $50M Series B), with a quote "
                 "from John Curtius, partner at Tiger Global", ec="web", conf="high", cite=u))
L.append(cls("qualio", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-05",
             country="US", country_src="web_verified", country_cite=u, city="San Francisco",
             focus="Healthcare & Bio",
             rounds=[rnd("2020", "Series A", 11_000_000, None, False,
                         NEWS("qualio", "Qualio Secures $50 Million in Series B")),
                     rnd("2021-05", "Series B", 50_000_000, "Tiger Global", True, u)],
             note="Cloud quality management software for life sciences. SiliconRepublic: 'It is now headquartered "
                  "in San Francisco but still has a base in Dublin' (founded in Dublin, 2012). Menlo's row reads "
                  "Dublin, IE with no citation: a pair to align. Tiger led the $50M Series B of May 2021; the $11M "
                  "Series A a year earlier did not name it."))

# 15. Qualtrics: only the adviser's 13G on the listed company.
L.append(verdict("qualtrics-international-inc", "not_member",
                 "13G/13F position in a listed company, no private round naming the firm (T3, D3): the adviser's "
                 "Schedule 13G filings of 2021-2023 cover Qualtrics after its January 2021 IPO; SAP owned the "
                 "company from 2019 until that listing and its earlier private rounds (Accel, Sequoia, Insight) "
                 "do not name Tiger", ec="fund_filing", conf="high",
                 cite=SEC("qualtrics-international-inc", "edgar")))

if __name__ == "__main__":
    jl.write("batch-011a", L)
