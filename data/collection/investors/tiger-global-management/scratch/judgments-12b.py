#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 12, chunk b (rows 16-30). Run: NQ_TAG=b12 python3 judgments-12b.py

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

# 16. Selfbook: Tiger led the October 2021 Series A and its March 2022 extension.
u = REC("selfbook")
L.append(cls("selfbook", status="private", rng="below_1b", usd=300_000_000, val_src="web_verified", val_cite=u,
             asof="2022-03-08", extra={"valuation_range_source": "web_verified"}, flags=["stale"],
             stage="Series A", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-10",
             country="US", city="New York", focus="Fintech & Payments",
             rounds=[rnd("2021-10", "Series A", 25_000_000, "Tiger Global Management", True, u),
                     rnd("2022-03", "Series A extension", 15_000_000, "Tiger Global Management", True, u)],
             note="Hotel payment and booking software, New York (the company's release is datelined there). "
                  "TechCrunch (via Yahoo): 'Tiger Global Management led the extension, as well as' the company's "
                  "October 2021 Series A; the $15M extension of March 2022 took the round to $40M at a $300M "
                  "valuation. Momentum slice (fintech), checked on Bing News 2026-09-29: product and partnership "
                  "news only (PayPal, 2025), no later priced round."))

# 17. Sendbird: Tiger led the Series B extension; Series C at $1.05B.
u = REC("sendbird")
v = SIB("iconiq-growth", "sendbird", "valuation_citation")
L.append(cls("sendbird", status="private", rng="1b_plus", usd=1_050_000_000, val_src="web_verified", val_cite=v,
             asof="2021-04-06", extra={"valuation_range_source": "web_verified"}, flags=["stale"],
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2019-05",
             country="US", city="San Mateo", focus="DevTools & APIs",
             rounds=[rnd("2019-02", "Series B", 52_000_000, "ICONIQ Capital", False, None, "press"),
                     rnd("2019-05", "Series B extension", 50_000_000, "Tiger Global", True, u),
                     rnd("2021-04", "Series C", 100_000_000, "Steadfast", None, v)],
             note="Chat, voice and AI-agent APIs, San Mateo (as ICONIQ's row reads; founded in Korea). Tiger led the "
                  "$50M extension of the Series B in May 2019 (Crunchbase News), after ICONIQ's $52M Series B of "
                  "February 2019. Mark: the $100M Series C of April 2021 at $1.05B (TechCrunch, the citation on "
                  "ICONIQ's row), stale and within 5% of the band edge; ICONIQ's pass found no newer round."))

# 18. SentinelOne: PIP VII and XII bought the Series F.
u = REC("sentinelone")
L.append(cls("sentinelone",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2020-11",
             country="US", city="Mountain View", focus="Security",
             rounds=[rnd("2020-11", "Series F", 267_000_000, "Tiger Global", True, u, "filing")],
             note="Endpoint security, Mountain View (NYSE: S since June 2021); the prefilled IL, a one-word "
                  "Wikidata join to the founding country, is corrected to US, as Insight's row reads. SentinelOne's "
                  "DRS: Tiger Global Private Investment Partners VII and XII bought 12.4M Series F preferred for "
                  "about $150M (the $267M Series F of November 2020 at about $3B that Tiger led) and held more than "
                  "5% before the IPO; no earlier round names Tiger. Tiger also bought in a private placement "
                  "alongside the IPO."))

# 19. ServiceTitan: Tiger co-led the March 2021 $500M round.
u = NEWS("servicetitan", "ServiceTitan Announces $500 Million Investment Led By Tiger Global")
L.append(cls("servicetitan",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-03",
             city="Glendale", focus="SaaS",
             rounds=[rnd("2021-03-26", "Series G", 500_000_000, "Tiger Global Management and Sequoia Capital Global "
                                                                "Equities", True, u, "company")],
             note="Software for the trades, Glendale (Nasdaq: TTAN since December 2024). Tiger co-led the $500M "
                  "investment of March 2021 at $8.3B with Sequoia Capital Global Equities (the company's release); "
                  "the IPO filing's investors' rights agreement names Tiger Global PIP 14 LLC and PIP 15 LLC, "
                  "vehicles of 2021-2022 vintage, so no earlier Tiger round."))

# 20. ShareChat: Tiger co-led the April 2021 round.
u = REC("sharechat")
L.append(cls("sharechat", status="private",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-04",
             country="IN", country_src="web_verified", country_cite=W("ShareChat"), city="Bangalore",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2021-04", "Series E", 502_000_000, "Tiger Global and Lightspeed", True, u)],
             note="Mohalla Tech, maker of the ShareChat and Moj apps, headquartered in Bengaluru (Wikipedia). Tiger "
                  "co-led the $502M round of April 2021 at $2.1B (Inc42; Entrackr), its first, and added to the "
                  "Series F in July 2021. Valuation left to the web pass (needs_web_value); Lightspeed's row carries "
                  "the April 2024 financing below $2B."))

# 21. Shein: Tiger-linked entities are pre-IPO holders (membership open); listed in Hong Kong, 2026.
u = NEWS("shein", "Shein to pay up to $4.4b to selected pre-IPO investors")
v = NEWS("shein", "Shein Ends Flat After Plunging As Much As 10%")
L.append(verdict("shein", "member",
                 "The Straits Times (2026-08-24), from Shein's Hong Kong IPO filings: the pre-IPO investors entitled "
                 "to compensation for the valuation slide 'include entities linked to Boyu Capital, Tiger Global, "
                 "General Atlantic, Thrive Capital, Mubadala and Brookfield', so Tiger bought into the company "
                 "while it was private", ec="web", conf="medium", cite=u))
L.append(cls("shein", status="public", rng="10b_plus", usd=24_000_000_000, val_src="web_verified", val_cite=v,
             asof="2026-09-01", extra={"valuation_range_source": "web_verified"},
             stage="Growth", stage_src="model", stage_conf="medium",
             country="SG", country_src="web_verified", country_cite=v, city="Singapore",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2022-04", "growth round", 1_000_000_000, None, None, None, "press")],
             note="Online fast-fashion retailer, 'Singapore-headquartered' (Forbes); listed in Hong Kong on "
                  "2026-09-01 at a market cap of about $24B (Forbes, debut day), down from the ~$100B private mark "
                  "of 2022; the shares have fallen since (record low 2026-09-29), still 10b_plus. Tiger-linked "
                  "entities are among the pre-IPO investors the company compensates for buying in at higher "
                  "valuations (Straits Times), i.e. in one of the 2020-2023 private rounds; which round Tiger "
                  "entered is not on record, but every candidate is a late round of a company founded in 2008: "
                  "Growth, model, medium."))

# 22. Shippit: Tiger led the Series B.
u = REC("shippit")
L.append(cls("shippit", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2020-12",
             country="AU", country_src="web_verified", country_cite=PR("shippit", "techinasia.com"), city="Sydney",
             focus="SaaS",
             rounds=[rnd("2020-12", "Series B", 22_200_000, "Tiger Global", True, u),
                     rnd("2022-05", "Series B2", None, "Tiger Global and Tidal Ventures", True, None, "press")],
             note="E-commerce shipping and fulfilment software, Sydney ('Australian logistics startup', Tech in "
                  "Asia). Tiger led the A$30M (US$22.2M) Series B of December 2020 (Business Times; Yahoo) and "
                  "co-led the A$65M Series B2 of May 2022 (AFR); no earlier round names it. No $1B mark."))

# 23. ShopClues: Tiger led the January 2015 Series D; sold to Qoo10 in 2019.
u = REC("shopclues")
L.append(cls("shopclues", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2015-01",
             country="IN", country_src="web_verified", country_cite=W("ShopClues"), city="Gurugram",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2015-01", "Series D", 100_000_000, "Tiger Global", True, u),
                     rnd("2016-01", "growth round", None, "GIC", True, None, "press")],
             note="Online marketplace, Gurgaon (Gurugram); run by Clues Network Pvt Ltd under a US parent, an "
                  "Indian business (the prefilled IN is right). Tiger led the $100M Series D of January 2015 at "
                  "about $500M with existing investors Helion and Nexus following (VCCircle; MediaNama; WSJ), its "
                  "first round; the company then reached $1.1B in the GIC-led round of 2016. Sold to Qoo10 in "
                  "November 2019 for a fraction of that (Scroll)."))

# 24. Shopflo: Tiger led the seed; bought by Pine Labs in 2026.
u = REC("shopflo")
L.append(cls("shopflo", status="acquired", rng="below_1b",
             stage="Seed", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2022-05",
             country="IN", country_src="web_verified",
             country_cite=PR("shopflo", "vccircle.com/shopflo-becomes-first-startup"), city="Bangalore",
             focus="SaaS",
             rounds=[rnd("2022-05", "Seed", 2_600_000, "Tiger Global and TQ Ventures", True, u)],
             note="Checkout software for D2C brands, Shopflo Technologies Pvt Ltd (Bengaluru). Tiger led the $2.6M "
                  "seed of May 2022 with TQ Ventures at a pre-product stage, its first seed cheque (VCCircle; "
                  "Financial Express). Pine Labs acquired it in April 2026 for Rs 88 crore (Inc42). Graduation left "
                  "for the graduation pass."))

# 25. Sidecar Health: Tiger joined the Series C at $1B.
u = NEWS("sidecar-health", "reaches unicorn status after fresh investment")
L.append(cls("sidecar-health", status="private", rng="1b_plus", usd=1_000_000_000, val_src="web_verified",
             val_cite=u, asof="2021-01-26", extra={"valuation_range_source": "web_verified"}, flags=["stale"],
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-01",
             country="US", city="El Segundo", focus="Healthcare & Bio",
             rounds=[rnd("2021-01-26", "Series C", 125_000_000, "Drive Capital", True,
                         NEWS("sidecar-health", "Cash Price"), "company")],
             note="Cash-price health insurance, El Segundo. FinTech Global (2021-02-01): the $125M Series C was led "
                  "by Drive Capital 'with participation also coming from BOND, Tiger Global and Menlo Ventures', at "
                  "a $1bn valuation (the unicorn mark, at the band edge, stale). Layoffs in July 2022 (Business "
                  "Insider) but no priced round below the mark. Menlo's row reads below_1b with no figure: a pair "
                  "to align."))

# 26. Sierra: Tiger co-led the May 2026 round at $15.8B.
u = REC("sierra")
L.append(cls("sierra", status="private", rng="10b_plus", usd=15_800_000_000, val_src="web_verified", val_cite=u,
             asof="2026-05-04", extra={"valuation_range_source": "web_verified"},
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2026-05",
             country="US", city="San Francisco", focus="AI & Applied AI",
             rounds=[rnd("2026-05-04", "Series E", 950_000_000, "Tiger Global and GV", True, u)],
             note="Customer-service AI agents (Bret Taylor, Clay Bavor), San Francisco. Tiger co-led the $950M round "
                  "of May 2026 at $15.8B with GV (Yahoo Finance; GV's row names it the Series E); no earlier round "
                  "names Tiger. Mark aligned with the GV, ICONIQ, Sequoia and Thrive rows."))

# 27. Sightfull: Tiger participated in the Series A (membership open).
u = PR("sightfull", "techcrunch.com/2022/09/13")
L.append(verdict("sightfull", "member",
                 "TechCrunch (2022-09-13): Sightfull 'closed an $18 million Series A round led by Dell Technologies "
                 "Capital with participation from Norwest Venture Partners and Tiger Global'", ec="web", conf="high",
                 cite=u))
L.append(cls("sightfull", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2022-09",
             country="IL", country_src="web_verified", country_cite=u, city="Tel Aviv", focus="SaaS",
             rounds=[rnd("2022-09", "Series A", 18_000_000, "Dell Technologies Capital", True, u)],
             note="Revenue and business-metrics analytics for SaaS companies; 'Sightfull is Tel Aviv-based' "
                  "(TechCrunch), opening a New York office. Tiger joined the $18M Series A of September 2022; no "
                  "earlier round names it. No $1B mark."))

# 28. SignalFx: Tiger led the Series E; bought by Splunk.
u = W("SignalFx")
L.append(cls("signalfx", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2019-06",
             country="US", city="San Mateo", focus="DevTools & APIs",
             rounds=[rnd("2019-06", "Series E", 75_000_000, "Tiger Global Management", True, u)],
             note="Cloud monitoring, San Mateo. Tiger led the $75M Series E of June 2019 (Wikipedia; VentureBeat), "
                  "after General Catalyst's 2018 Series D; Splunk bought the company for $1.05B two months later "
                  "(closed October 2019)."))

# 29. Sina: adviser 13G/13F on a listed company only.
L.append(verdict("sina-corp", "not_member",
                 "13G/13F position in a listed company, no private round naming the firm (T3, D3): the adviser's "
                 "Schedule 13G filings of 2008-2009 and 13F lines of 2007-2018 cover Sina, Nasdaq-listed since "
                 "2000; no private round names Tiger", ec="fund_filing", conf="high", cite=SEC("sina-corp", "edgar")))

# 30. SirionLabs: Tiger co-led the Series C.
u = PR("sirionlabs", "vccircle.com/tiger-global-avatar-growth-lead-series-c")
L.append(cls("sirionlabs", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2020-05",
             country="US", city="Seattle", focus="SaaS",
             rounds=[rnd("2020-05", "Series C", 44_000_000, "Tiger Global and Avatar Growth Capital", True, u)],
             note="AI contract lifecycle management, 'founded in New Delhi and now US-headquartered' (SiliconIndia), "
                  "with its main US office in Seattle (GeekWire, 2020). Tiger co-led the $44M Series C of May 2020 "
                  "with Avatar (VCCircle; Mint); Mint had reported Tiger in talks for a stake in May 2019, not "
                  "confirmed. TechCrunch (June 2024) called it 'now valued around $1B' without a priced round, and "
                  "Haveli agreed to take a majority stake in January 2026 (Reuters) at an undisclosed price: "
                  "below_1b pending a stated figure, a second look for the A/B pass."))

if __name__ == "__main__":
    jl.write("batch-012b", L)
