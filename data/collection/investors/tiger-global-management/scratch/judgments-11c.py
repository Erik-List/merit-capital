#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 11, chunk c (rows 31-45). Run: NQ_TAG=b11 python3 judgments-11c.py

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

# 31. ResQ: Tiger co-led the Series A (membership open).
u = PR("resq", "techcrunch.com/2021/10/12/resq")
L.append(verdict("resq", "member",
                 "TechCrunch (2021-10-12): ResQ 'has raised a $39 million Series A co-led by Tiger Global and Canvas "
                 "Ventures'; the company's release quotes Griffin Schroeder, partner at Tiger Global Management",
                 ec="web", conf="high", cite=u))
L.append(cls("resq", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-10",
             country="CA", country_src="web_verified", country_cite=PR("resq", "betakit.com"), city="Toronto",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2021-10", "Series A", 39_000_000, "Tiger Global and Canvas Ventures", True, u)],
             note="Restaurant repair and maintenance platform (a marketplace of technicians with its own software), "
                  "Toronto (BetaKit reports the round in CAD). Tiger co-led the $39M Series A of October 2021 with "
                  "Canvas Ventures, its first round in the company. No $1B mark."))

# 32. Restoration Hardware: adviser 13G on a listed company only.
L.append(verdict("restoration-hardware-holdings-inc", "not_member",
                 "13G/13F position in a listed company, no private round naming the firm (T3, D3): the adviser's "
                 "2014 Schedule 13G covers RH (Restoration Hardware), listed on the NYSE since November 2012; its "
                 "private owners before the listing (Catterton, Tower Three) are not Tiger and no round names it",
                 ec="fund_filing", conf="high", cite=SEC("restoration-hardware-holdings-inc", "edgar")))

# 33. Revolut: Tiger co-led the Series E.
u = REC("revolut")
L.append(cls("revolut", status="private",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-07",
             country="GB", country_src="web_verified", country_cite=W("Revolut"), city="London",
             focus="Fintech & Payments",
             rounds=[rnd("2021-07", "Series E", 800_000_000, "SoftBank Vision Fund 2 and Tiger Global", True, u)],
             note="Digital bank headquartered in London (Wikipedia); the prefilled LT is its Lithuanian banking "
                  "entity, as the sibling rows found. Tiger co-led the $800M Series E of July 2021 at $33B with "
                  "SoftBank Vision Fund 2 (Revolut's own post; Business Insider), its first round in the company, "
                  "and joined the Coatue-led secondary of August 2024 (Coatue's row). Valuation left to the web "
                  "pass (needs_web_value); the sibling rows carry the July 2026 secondary at $115B (and two still "
                  "$75B)."))

# 34. Rhino: Tiger led the January 2021 'pre-IPO' round.
u = REC("rhino")
L.append(cls("rhino", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-01",
             country="US", city="New York", focus="Fintech & Payments",
             rounds=[rnd("2017-09", "Seed", 1_940_000, "ff Venture Capital", False,
                         NEWS("rhino", "Rhino Raises $1.94 Million")),
                     rnd("2021-01", "pre-IPO round", 95_000_000, "Tiger Global", True, u)],
             note="Security-deposit insurance for renters, New York. Tiger led the $95M round of January 2021 that "
                  "the company called pre-IPO, valuing it at just under $500M (Business Insider; TechCrunch), "
                  "after a 2017 seed and a Series A that did not name Tiger. Rhino and Jetty merged in February "
                  "2025 (the companies' release; terms undisclosed) and the combined business trades as a private "
                  "company. Momentum slice (fintech), checked 2026-09-29: no later priced $1B round."))

# 35. RingCentral: adviser 13G/13F on a listed company only.
L.append(verdict("ringcentral-inc", "not_member",
                 "13G/13F position in a listed company, no private round naming the firm (T3, D3): the adviser's "
                 "Schedule 13G filings of 2021-2023 and 13F lines of 2019-2022 cover RingCentral, listed on the "
                 "NYSE since 2013; its private rounds (Sequoia, Khosla, DAG and others) do not name Tiger",
                 ec="fund_filing", conf="high", cite=SEC("ringcentral-inc", "edgar")))

# 36. Ringier: the Swiss publisher bought jobs.ch FROM Tiger; not a Tiger investment.
L.append(verdict("ringier", "not_member",
                 "The recall sentence reports a sale by Tiger, not an investment: 'Ringier acquired jobs.ch Holding "
                 "AG from the private equity firm Tiger Global Management in the fall of 2012' (Wikipedia, Ringier). "
                 "Ringier is the buyer of a Tiger holding; no record ties the firm to a round of Ringier",
                 ec="web", conf="high", cite=W("Ringier")))

# 37. Rivery: Tiger led the Series B; acquired by Boomi.
u = REC("rivery")
L.append(cls("rivery", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2022-05",
             country="IL", country_src="web_verified", country_cite=u, city="Tel Aviv", focus="Data Infrastructure",
             rounds=[rnd("2021", "Series A", None, None, False, u),
                     rnd("2022-05-24", "Series B", 30_000_000, "Tiger Global", True, u, "company")],
             note="SaaS data integration (ELT) platform; the release gives offices in 'New York and Tel Aviv HQ' "
                  "(founded in Israel, as Israel Hayom reports it). Tiger led the $30M Series B of May 2022; the "
                  "previous year's Series A was State of Mind Ventures' and Entree Capital's (total raised $48M). "
                  "Acquired by Boomi, announced December 2024 (Carlsquare advised Boomi)."))

# 38. RoadSync: Tiger led the Series B.
u = REC("roadsync")
L.append(cls("roadsync", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-06",
             country="US", city="Atlanta", focus="Fintech & Payments",
             rounds=[rnd("2020-04", "Series A", 5_700_000, None, False,
                         NEWS("roadsync", "RoadSync Raises $5.7 Million in Series A")),
                     rnd("2021-06", "Series B", 30_000_000, "Tiger Global", True, u, "company")],
             note="Payments platform for freight and logistics, Atlanta. Tiger led the $30M Series B of June 2021 "
                  "(Business Wire); the $5.7M Series A of April 2020 did not name it. Momentum slice (fintech), "
                  "checked on Bing News 2026-09-29: no later round or $1B mark."))

# 39. Roblox: PIP X bought Series F and Series G preferred.
u = REC("roblox")
L.append(cls("roblox",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2018",
             country="US", city="San Mateo", focus="Media, Gaming & Advertising",
             rounds=[rnd("2018", "Series F", 150_000_000, None, True, u, "filing"),
                     rnd("2020-02", "Series G", 150_000_000, None, True, u, "filing")],
             note="Online game platform, San Mateo (NYSE: RBLX, direct listing March 2021). Roblox's DRS: Tiger "
                  "Global Private Investment Partners X bought $75.7M of the Series F (whose investors' rights "
                  "agreement is dated June 2018; the $150M round was announced September 2018) and Series G "
                  "preferred, and signs the investors' rights agreement. No earlier round names Tiger."))

# 40. Robust Intelligence: Tiger led the Series B; acquired by Cisco.
u = REC("robust-intelligence")
L.append(cls("robust-intelligence", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-12",
             country="US", city="San Francisco", focus="Security",
             rounds=[rnd("2021-12", "Series B", 30_000_000, "Tiger Global", True, u)],
             note="AI model security and validation, San Francisco. Tiger led the $30M round of December 2021 "
                  "(SiliconANGLE), the Series B after Sequoia's 2020 Series A (Sequoia's row). Acquired by Cisco in "
                  "2024."))

# 41. Rogo: Tiger joined the Thrive-led Series B; Series D at $2B.
u = REC("rogo")
v = "https://www.tipranks.com/news/private-companies/rogo-raises-160-million-series-d-at-2-billion-valuation"
L.append(cls("rogo", status="private", rng="1b_plus", usd=2_000_000_000, val_src="web_verified", val_cite=v,
             asof="2026-04-29", extra={"valuation_range_source": "web_verified"},
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2025-05",
             country="US", city="New York", focus="AI & Applied AI",
             rounds=[rnd("2024-10", "Series A", 18_500_000, "Khosla Ventures", False,
                         NEWS("rogo", "Rogo Announces $18M Series A")),
                     rnd("2025-05", "Series B", 50_000_000, "Thrive Capital", True, u),
                     rnd("2026-04-29", "Series D", 160_000_000, "Kleiner Perkins", None,
                         NEWS("rogo", "Rogo Raises $160M Series D to Scale"), "company")],
             note="AI analyst platform for investment banks, New York. Tiger joined the $50M Series B of spring 2025 "
                  "led by Thrive (Financial IT names Thrive, J.P. Morgan and Tiger Global); the $18.5M Series A of "
                  "October 2024 was Khosla's. Momentum slice (AI), checked 2026-09-29: the $160M Series D of April "
                  "2026 led by Kleiner Perkins was reported at a $2B valuation (TipRanks), up from $750M at the "
                  "Series C. The Sequoia and Thrive rows still read below_1b: a pair to align."))

# 42. Rokt: Tiger led the Series E; company-run secondary at $3.5B.
u = PR("rokt", "retailtouchpoints.com")
v = NEWS("rokt", "Rokt Announces Secondary Transaction, Increasing Valuation")
L.append(cls("rokt", status="private", rng="1b_plus", usd=3_500_000_000, val_src="web_verified", val_cite=v,
             asof="2025-01-16", extra={"valuation_range_source": "web_verified"},
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-12",
             country="US", city="New York", focus="Media, Gaming & Advertising",
             rounds=[rnd("2021-12", "Series E", 325_000_000, "Tiger Global", True, u),
                     rnd("2022-12", "secondary", None, "Square Peg and Wellington Management", None,
                         PR("rokt", "nasdaq.com/articles/e-commerce-tech-startup-rokt")),
                     rnd("2025-01-16", "secondary", None, None, None, v, "company")],
             note="E-commerce transaction marketing (the Rokt ad network), 'headquartered in New York City' "
                  "(Wikipedia), founded in Sydney. Tiger led the $325M Series E of December 2021 at $1.95B (Retail "
                  "TouchPoints; WSJ), its first round. Mark: the company-announced secondary of January 2025 at "
                  "$3.5B; an MA Financial fund's offering priced shares at about $7.9B in November 2025 (Courier-"
                  "Mail), a secondary sale kept in this note. 1b_plus either way."))

# 43. Roku: adviser 13G/13F after the IPO only.
L.append(verdict("roku-inc", "not_member",
                 "13G/13F position in a listed company, no private round naming the firm (T3, D3): the adviser's "
                 "Schedule 13G filings of 2017-2018 and a single 13F quarter (2017-09-30) follow Roku's Nasdaq IPO "
                 "of September 2017; its private rounds (Menlo, Globespan, Netflix, Fox, Hearst and others) do not "
                 "name Tiger", ec="fund_filing", conf="high", cite=SEC("roku-inc", "edgar")))

# 44. Root: Tiger's tender offer of January 2019, then the Series E.
u = REC("root-insurance")
L.append(cls("root-insurance", status="public", rng="below_1b", usd=730_510_000, val_src="web_verified",
             val_cite="https://stockanalysis.com/stocks/root/market-cap/", asof="2026-09-29",
             extra={"valuation_range_source": "web_verified"},
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2019-01",
             country="US", city="Columbus", focus="Fintech & Payments",
             rounds=[rnd("2019-01", "tender offer (secondary)", 16_000_000, "Tiger Global", True, u, "filing"),
                     rnd("2019-08", "Series E", 350_000_000, None, True, u, "filing")],
             note="Car insurance, Columbus (Nasdaq: ROOT since October 2020). Root's DRS: in January 2019 the "
                  "company signed a participation agreement with Tiger Global Private Investment Partners XI, LFX "
                  "Capital and Alex Cook for a tender offer they ran (about 2.1M shares, $16.0M), and PIP XI and "
                  "Alex Cook bought $10M of the Series E; the tender is Tiger's entry, Growth by the policy "
                  "constant. Market cap $730.51M on 2026-09-29 (stockanalysis.com), below $1B as Redpoint's row "
                  "reads."))

# 45. Roposo: Tiger led the Series A; acquired by InMobi's Glance.
u = NEWS("roposo", "Binny Bansal backed Roposo raises")
L.append(cls("roposo", status="acquired", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2015-03",
             country="IN", country_src="web_verified", country_cite=REC("roposo"), city="Gurugram",
             focus="Media, Gaming & Advertising",
             rounds=[rnd("2015-03", "Series A", 5_000_000, "Tiger Global", True, u),
                     rnd("2015-08", "follow-on", 15_000_000, "Tiger Global", True,
                         PR("roposo", "Roposo gets $15 mn from Tiger Global"))],
             note="Fashion-discovery social network turned short-video app, Gurugram. Tiger led the $5M Series A of "
                  "March 2015 after an angel round (YourStory: 'Binny Bansal backed Roposo raises a $5 million "
                  "series A funding round from Tiger Global') and added $15M in August 2015. Acquired by InMobi's "
                  "Glance in December 2019."))

if __name__ == "__main__":
    jl.write("batch-011c", L)
