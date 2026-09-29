#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 11, chunk b (rows 16-30). Run: NQ_TAG=b11 python3 judgments-11b.py

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

# 16. QuickNode: Tiger led the Series A.
u = PR("quicknode", "QuickNode 完成")
v = PR("quicknode", "coindesk.com/business/2023/01/24")
L.append(cls("quicknode", status="private", rng="below_1b", usd=800_000_000, val_src="web_verified", val_cite=v,
             asof="2023-01-24", extra={"valuation_range_source": "web_verified"}, flags=["stale"],
             stage="Series A", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-10",
             country="US", city="Miami", focus="DevTools & APIs",
             rounds=[rnd("2021-10", "Series A", 35_000_000, "Tiger Global", True, u),
                     rnd("2023-01", "Series B", 60_000_000, "10T Holdings", True, v)],
             note="Blockchain node and developer platform, Miami (YC's row). Tiger led the $35M Series A of October "
                  "2021 (cnyes; Business Insider on Shleifer and Curtius winning Miami deals) and joined the $60M "
                  "Series B of January 2023 at $800M led by 10T Holdings (CoinDesk). Momentum slice (developer "
                  "tools), checked on Bing News 2026-09-29: no later priced round."))

# 17. Quikr: Tiger led the September 2014 round.
u = REC("quikr")
L.append(cls("quikr", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2014-09",
             country="IN", country_src="web_verified", country_cite=W("Quikr"), city="Bangalore",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2014-09", "growth round", 60_000_000, "Tiger Global", True, u),
                     rnd("2015-04", "growth round", 150_000_000, None, True,
                         PR("quikr", "Quikr raises $150M from Tiger Global"))],
             note="Online classifieds, Bangalore. Tiger led the $60M round of September 2014 with existing "
                  "investors following (Wikipedia; Reuters via Yahoo), after Matrix, Norwest, Warburg Pincus and "
                  "Kinnevik had funded the company, so Growth; it joined the $150M round of April 2015 that neared "
                  "a $1B valuation. The unicorn list records the company as devalued (2020, about $570M): "
                  "below_1b, as Coatue's row reads; no priced mark since. The prefilled country IN is right."))

# 18. Quizizz: Tiger led the Series B.
u = REC("quizizz")
L.append(cls("quizizz", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-06",
             country="IN", country_src="web_verified", country_cite=u, city="Bangalore", focus="SaaS",
             rounds=[rnd(None, "Series A", None, "Eight Roads Ventures", False,
                         PR("quizizz", "Edtech Platform Quizizz Bags")),
                     rnd("2021-06", "Series B", 31_500_000, "Tiger Global", True, u)],
             note="Gamified quizzes and lessons sold to teachers, schools and districts (SaaS by the edtech rule). "
                  "The founders started it in Bangalore in 2015 (TechCrunch via Yahoo) and the team is there; the "
                  "Delaware parent Quizizz Inc. is the US face, so IN by the Indian-business rule (medium: no page "
                  "read states the head office). 'Tiger Global led the Series B financing round' ($31.5M, June "
                  "2021); the Series A was Eight Roads' (Inc42). No $1B mark."))

# 19. Quora: Tiger led the Series C.
u = REC("quora")
L.append(cls("quora", status="private",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2014-04",
             city="Mountain View", focus="Consumer & Marketplaces",
             rounds=[rnd("2014-04", "Series C", 80_000_000, "Tiger Global", True, u)],
             note="Q&A network (and the Poe AI app), Mountain View, as a16z's row reads. Tiger led the $80M Series "
                  "C of April 2014 at about $900M (Reuters; Wikipedia), after Benchmark's 2010 Series A and the "
                  "2012 round. Valuation left to the web pass (needs_web_value)."))

# 20. Rajasthan Royals: talks only; no completed Tiger investment on record.
L.append(verdict("rajasthan-royals", "not_member",
                 "Only talks are on record: Zee Business (2023-05-22) 'Tiger Global eyes $40 million investment', "
                 "Front Office Sports and SportsPro 'set to invest' / 'set for US$40m investment, says report'; "
                 "Google News finds no report of a completed Tiger investment, and the December 2023 reports of a "
                 "stake sale at a $650M valuation name Footpath Ventures (Economic Times, Sky News). No record ties "
                 "the firm to a completed round", ec="web", conf="medium", cite=REC("rajasthan-royals")))

# 21. Rapyd: Tiger is on the Series C release.
u = PR("rapyd", "finanznachrichten.de/nachrichten-2019-10")
L.append(cls("rapyd", status="private",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="medium", entry_date="2019-10",
             country="GB", country_src="web_verified", country_cite=PR("rapyd", "Rapyd raises $100 million for mobile"),
             city="London", focus="Fintech & Payments",
             rounds=[rnd("2019-02", "Series B", 40_000_000, "General Catalyst and Stripe", None,
                         NEWS("rapyd", "Stripe joins Rapyd's $40m Series B")),
                     rnd("2019-10", "Series C", 100_000_000, "Oak HC/FT", True, u),
                     rnd("2021-01", "Series D", 300_000_000, "Coatue", True, REC("rapyd"))],
             note="Fintech-as-a-service payments, London (VentureBeat: 'a London-based company'; founded in Tel "
                  "Aviv), as the Coatue, General Catalyst and Spark rows read. Tiger is listed on the $100M Series "
                  "C release of October 2019 ('Investors include Oak HC/FT, Tiger Global, Coatue, Stripe, General "
                  "Catalyst, Target Global and Entree Capital'); the $40M Series B of February 2019 does not name "
                  "it. It joined the Coatue-led $300M Series D (January 2021). Valuation left to the web pass "
                  "(needs_web_value): the latest priced round, $500M at about $4.5B (March 2025), is in the Coatue "
                  "and General Catalyst rows; Spark's still reads $15B."))

# 22. Razorpay: Tiger led the Series A (membership open; Form D seat is Lee Fixel's, in tenure).
u = PR("razorpay-inc", "Indian fintech firm Razorpay nabs US$11.5M")
L.append(verdict("razorpay-inc", "member",
                 "Yahoo News Singapore (Tech in Asia, 2015-10-27): 'Indian fintech firm Razorpay nabs US$11.5M led "
                 "by Tiger Global' (YourStory: the $9M Series A led by Tiger Global); Lee Fixel, a Tiger partner "
                 "in tenure, is director on the company's 2018 Form Ds", ec="web", conf="high", cite=u))
L.append(cls("razorpay-inc", status="private", country="IN", country_src="web_verified", country_cite=u,
             city="Bangalore", focus="Fintech & Payments", flags=["model_disputes_source"],
             note="Payments, Bangalore (the Lightspeed, Ribbit and YC rows agree). The prefilled US is the Delaware "
                  "parent's Form D address (Palo Alto) and is disputed: Razorpay is an Indian business, and it "
                  "redomiciled to India in 2025 (Lightspeed's row). Tiger led the Series A of October 2015, as the "
                  "Form D band reads, and the 2017-2018 Series B. Valuation left to the web pass (needs_web_value)."))

# 23. RDC Concrete: bought by Tiger-backed Infra.Market; not a Tiger investment.
L.append(verdict("rdc-concrete", "not_member",
                 "The recall headline reports an acquisition by a portfolio company, not an investment: 'Tiger "
                 "Global-backed Infra.Market buys RDC Concrete for Rs 730 crore' (Economic Times, 2021-09-20). "
                 "Tiger's investment is Infra.Market (its own row); no record ties the firm to a round of RDC "
                 "Concrete, which Infra.Market bought from True North", ec="web", conf="high", cite=REC("rdc-concrete")))

# 24. Rebill: Tiger led the seed.
u = PR("rebill", "Startup latina Rebill recibe US$3.6M")
L.append(cls("rebill", status="private", rng="below_1b",
             stage="Seed", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2022-08",
             country="AR", country_src="web_verified", country_cite=REC("rebill"), city="Buenos Aires",
             focus="Fintech & Payments",
             rounds=[rnd("2022-08", "Seed", 3_000_000, "Tiger Global", True, u)],
             note="Subscription billing and payment collection for Latin America, 'an Argentina-based startup' "
                  "(TechCrunch via Yahoo), YC. Tiger led the $3M seed of August 2022 (US$3.6M across two rounds; "
                  "La Cronica de Hoy: 'inversion liderada por Tiger Global'). No later round found on Bing News "
                  "(2026-09-29). Graduation left for the graduation pass. Momentum slice (fintech): no $1B round."))

# 25. Redfin: the S-1/A lists PIP VII's Series F, tender and Series G purchases.
u = SECU("redfin-corp", "S-1/A")
L.append(verdict("redfin-corp", "member",
                 "Redfin's IPO S-1/A (2017-07-17): Tiger Global Private Investment Partners VII bought $25.65M of "
                 "the Series F preferred (closings November 2013 and February 2014) and 513,341 shares in the "
                 "tender offer that closed January 2014; PIP VII and IX held 10.5% before the listing",
                 ec="fund_filing", conf="high", cite=u))
L.append(cls("redfin-corp", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2013-11",
             country="US", city="Seattle", focus="Consumer & Marketplaces",
             rounds=[rnd("2013-11", "Series F", 50_500_000, None, True, u, "filing"),
                     rnd("2014-01", "tender offer (secondary)", None, None, True, u, "filing"),
                     rnd("2014-12", "Series G", 71_000_000, None, True, u, "filing"),
                     rnd("2015-08", "tender offer (secondary)", None, None, True, u, "filing")],
             note="Online real-estate brokerage, Seattle. Per the S-1/A, PIP VII bought $25.65M of the $50.5M "
                  "Series F (closings November 2013 and February 2014; Tiger may have come in at the second "
                  "closing, after its January 2014 tender purchase), $6.1M of the $71M Series G (December 2014), "
                  "and PIP IX bought in the August 2015 tender. Listed July 2017; acquired by Rocket Companies in "
                  "July 2025, so no standalone mark (Greylock's row still reads public: a pair to align)."))

# 26. Redis: Tiger led the Series G.
u = REC("redis")
L.append(cls("redis", status="private",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-04",
             city="Mountain View", focus="Data Infrastructure",
             rounds=[rnd("2021-04", "Series G", 110_000_000, "Tiger Global", True, u)],
             note="In-memory database company (Redis Labs), Mountain View, as Bain Capital Ventures' row reads. "
                  "Tiger led the $110M Series G of April 2021 at over $2B (dbta; Reuters; Wikipedia), its first "
                  "round; in April 2024 Tiger and Viola sold $200-300M of shares at over $2B (Calcalist). "
                  "Valuation left to the web pass (needs_web_value)."))

# 27. Refyne: Tiger led the Series B.
u = REC("refyne")
L.append(cls("refyne", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2022-01",
             country="IN", country_src="web_verified",
             country_cite=NEWS("refyne", "Refyne Raises $16 Mn To Help Employees"), city="Bangalore",
             focus="Fintech & Payments",
             rounds=[rnd("2021-06", "Series A", 16_000_000, "RTP Global and partners of DST Global", False,
                         NEWS("refyne", "Refyne raises $16 million in Series A funding from RTP Global")),
                     rnd("2022-01", "Series B", 82_000_000, "Tiger Global", True, u)],
             note="Earned-wage-access platform, Bangalore ('Bengaluru-based', Inc42). Tiger led the $82M Series B "
                  "of January 2022 (VCCircle; TechCrunch); the $16M Series A of June 2021 was led by RTP Global "
                  "and DST Global partners. Momentum slice (fintech), checked 2026-09-29: Moneycontrol "
                  "(2026-09-21) reports Refyne looking to raise about $50M at a $1B valuation, talks rather than a "
                  "priced round, so below_1b stands."))

# 28. Relativity Space: Tiger led the Series D.
u = SIB("general-catalyst", "relativity-space", "entry_stage_citation")
L.append(cls("relativity-space", status="private",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2020-11",
             city="Long Beach", focus="Industrial & Robotics",
             rounds=[rnd("2020-11-23", "Series D", 500_000_000, "Tiger Global", True, u, "company")],
             note="3D-printed rockets, Long Beach. Tiger led the $500M Series D of November 2020 at about $2.3B "
                  "(CNBC; the company's release, as cited on General Catalyst's row); no earlier round names it. "
                  "Eric Schmidt took a controlling stake and became CEO in March 2025 (Coatue's row); the company "
                  "remains private. Valuation left to the web pass (needs_web_value): the June 2021 $4.2B mark in "
                  "the sibling rows is likely too high after the 2025 recapitalisation."))

# 29. Relay Payments: Lee Fixel's seat is Addition's (D7).
L.append(verdict("relay-payments-inc", "not_member",
                 "Lee Fixel's director seat on the 2020-2021 Form Ds is after his 2019 departure from Tiger to "
                 "found Addition (D7); the company's release (cited on Ribbit's row) says Addition led the Series A "
                 "and Series B with Ribbit and Spark participating; no Tiger round of Relay Payments is on record",
                 ec="formd_adjudicated", conf="high", cite=SEC("relay-payments-inc")))

# 30. RenoRun: Tiger led the Series B; creditor protection and shutdown in 2023.
u = NEWS("renorun", "Montreal-based RenoRun raises US$142 million")
L.append(cls("renorun", status="defunct", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2022-02",
             country="CA", country_src="web_verified", country_cite=u, city="Montreal",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2019-11", "Series A", None, "Inovia Capital and Obvious Ventures", False,
                         NEWS("renorun", "RenoRun scores Series A")),
                     rnd("2022-02", "Series B", 142_000_000, "Tiger Global Management", True, u)],
             note="Construction-materials delivery marketplace, Montreal. Tiger led the US$142M Series B of "
                  "February 2022 (Financial Post; TechCrunch); the C$22.5M Series A of November 2019 was led by "
                  "Inovia and Obvious. RenoRun filed for creditor protection in Quebec on 2023-03-28 after Tiger "
                  "and government funds declined further financing (Globe and Mail) and shut down operations on "
                  "2023-05-01 while pursuing an asset sale (BetaKit); no completed sale found, so defunct under the "
                  "bankruptcy rule."))

if __name__ == "__main__":
    jl.write("batch-011b", L)
