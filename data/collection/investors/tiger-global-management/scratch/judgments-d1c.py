#!/usr/bin/env python3
"""PRO-167 Tiger Global, DELTA batch 1, chunk c (rows 31-45: little-internet .. satylca-s-c-a).
Run: NQ_TAG=d1 python3 judgments-d1c.py

Every citation comes from a helper that reads a URL already on disk or builds it from a tool's response: the row's
evidence view (PR / REC), the press caches (NEWS, incl. this judge's Bing and Google items), a filing on the row
(SEC) or in the EDGAR full-text search response (FORMD_FTS), the verdict ledger (LEDGER_CITE), or a sibling book's
recorded mark (V)."""
import json
import re
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import judge_lib as jl  # noqa: E402
from judge_lib import verdict, cls, rnd, W, NEWS, SEC  # noqa: E402,F401

PK = json.loads((HERE / "evidence-pack.json").read_text())
SIBS = json.loads((HERE / "siblings.json").read_text())
INV = HERE.parent            # tiger-global-management/
ASOF = "2026-09-29"
WV = {"valuation_range_source": "web_verified"}
_VENDOR = re.compile(r"sacra\.com|pitchbook|cbinsights|tracxn|crunchbase\.com/organization|dealroom|getlatka|forgeglobal|caplight")


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


def REC(slug):
    """The citation URL at the end of the row's RECALL line."""
    b = PK.get(slug, {}).get("recall_basis") or ""
    return _one(re.findall(r"\((https?://[^\s)]+)\)\s*$", b), f"REC({slug!r})")


def band(usd):
    return "100b_plus" if usd >= 1e11 else "10b_plus" if usd >= 1e10 else "1b_plus" if usd >= 1e9 else "below_1b"


def V(slug, inv):
    """cls() keywords pinning a sibling book's cited mark for the same company (rule 10)."""
    for x in SIBS.get(slug, []):
        if x["investor"] == inv:
            if not x.get("val_cite") or _VENDOR.search(x["val_cite"]) or not x.get("usd"):
                raise SystemExit(f"V({slug!r}, {inv!r}): no usable citation")
            usd = float(x["usd"])
            return dict(rng=band(usd), usd=usd, val_src="web_verified", val_cite=x["val_cite"],
                        asof=x["asof"], extra=dict(WV))
    raise SystemExit(f"V({slug!r}, {inv!r}): no sibling row")


def LEDGER_CITE(slug):
    """The citation of a verdict already in the ledger."""
    led = json.loads((INV / "companies/membership-ledger.json").read_text())["tiger-global-management"]["verdicts"]
    v = (led.get(slug) or {}).get("citation")
    if not (isinstance(v, str) and v.startswith("http")):
        raise SystemExit(f"LEDGER_CITE({slug!r}): none")
    return v


def FORMD_FTS(q):
    """{file_date: filing index URL} for the Form Ds the EDGAR full-text search returns for "q" (built from
    the search response, never typed)."""
    import subprocess
    import urllib.parse
    url = "https://efts.sec.gov/LATEST/search-index?q=" + urllib.parse.quote(f'"{q}"') + "&forms=D"
    out = subprocess.run(["curl", "-s", "-A", "merit-capital research erik@meritcapit.al", url],
                         capture_output=True, text=True).stdout
    res = {}
    for h in json.loads(out)["hits"]["hits"]:
        s = h["_source"]
        adsh, cik = s["adsh"], str(int(s["ciks"][0]))
        res[s["file_date"]] = f"https://www.sec.gov/Archives/edgar/data/{cik}/{adsh.replace('-', '')}/{adsh}-index.htm"
    if not res:
        raise SystemExit(f"FORMD_FTS({q!r}): no filing")
    return res


FIRM = ("firm: tigerglobal.com, which publishes no portfolio, posts or announcements (five pages and a login, "
        "read 2026-09-29), and the firm's own fund filings -> no page of the firm names a later round of {}")


def FORMD_NONE(q, where):
    return (f"EDGAR full-text search of Form D filings for '{q}' (2026-09-29) -> none; {where}, no filing by the "
            f"company and no single-deal vehicle named after it")


L = []

# 31. Little Internet: Tiger joined the $50M first financing of Little (2015).
u = REC("little-internet")
u_fe = NEWS("little-internet", "raise $50 m for new venture Little")
u_ci = NEWS("little-internet", "Zovi raises $50 million to launch")
L.append(verdict("little-internet", "member",
                 "Entrackr (2019-04-06): 'In 2015, founders of Zovi raised $50 million from Paytm, SAIF Partners and Tiger "
                 "Global to launch a deal-centric app called Little'; Financial Express (2015-07-29) reports the same round "
                 "at the time.",
                 ec="web", conf="high", cite=u))
L.append(cls("little-internet", status="acquired", rng="below_1b", stage="undetermined",
             rounds=[rnd("2015-07", "first financing (round not named)", 50_000_000, "Paytm", True, u_fe),
                     rnd("2019-04", "Paytm takes over; SAIF and GIC exit for Paytm stock", None, "Paytm", None, u)],
             country="IN", country_src="web_verified", country_cite=u_ci, city="Bangalore",
             focus="Consumer & Marketplaces",
             note="Little (Little Internet Pvt Ltd), an app-only deals marketplace launched in 2015 by Zovi's founders "
                  "(Manish Chopra, not the former Tiger Veda head of the same name, and Satish Mani), Bangalore (CIOL's "
                  "dateline). Tiger joined its $50M first financing with Paytm and SAIF (July 2015); no source names the "
                  "round, so the stage is undetermined. Paytm took the company over in 2019, SAIF and GIC exiting for "
                  "Paytm stock (Entrackr): acquired."))

# 32. Locus: Tiger joined the $22M Series B led by Falcon Edge.
u = REC("locus")
L.append(verdict("locus", "member",
                 "Times of India (2019-05-13): 'Falcon Edge leads $22 million funding for Locus; Tiger Global joins too'; "
                 "Inc42 and the trade press report the same round, named the Series B (STAT Times, Indian Transport & "
                 "Logistics).",
                 ec="web", conf="high", cite=u))
L.append(cls("locus", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2019-05",
             rounds=[rnd("2019-05-13", "Series B", 22_000_000, "Falcon Edge Capital", True, u)],
             country="IN", country_src="web_verified", country_cite=u, city="Bangalore", focus="SaaS",
             note="Locus (locus.sh), AI-based logistics and route-optimisation software, Bangalore. Tiger joined the $22M "
                  "Series B led by Falcon Edge (May 2019) as a new investor, its first round. The pre-filled Great Britain "
                  "is a wrong Wikidata join on a one-word name. Locus Robotics (Massachusetts), which took $50M from Tiger "
                  "in 2021, is a different company and a separate row (never merged); the Y Combinator row named Locus "
                  "is a different company too."))

# 33. Magna: Tiger co-led the $15M seed; Kraken's parent bought the company in February 2026 (a cited end).
u = REC("magna")
u_s = NEWS("magna", "Magna Announces $15 Million Seed Round")
u_end = NEWS("magna", "Kraken continues acquisition streak")
MFD = FORMD_FTS("Magna Digital")
L.append(verdict("magna", "member",
                 "CoinDesk (2022-09-15): 'Token Management Platform Magna Raises $15M Seed Round at $70M Valuation ... "
                 "Investors in the round included Tiger Global, Tusk Venture Partners, Circle Ventures and Shima Capital'; "
                 "the company's release says the round was 'Led by Tiger Global and Tusk Venture Partners'.",
                 ec="web", conf="high", cite=u))
L.append(cls("magna", status="acquired", rng="below_1b",
             stage="Seed", stage_src="web_verified", stage_cite=u_s, stage_conf="high", entry_date="2022-09-15",
             grad="not_graduated", grad_src="web_verified", grad_cite=u_end, grad_conf="high", grad_asof=ASOF,
             surfaces=[FIRM.format("Magna"),
                       "formd: EDGAR full-text search of Form D filings for 'Magna Digital' and for the founder 'Bruno "
                       "Faviero' (2026-09-29) -> Magna Digital, Inc. (CIK 1919657, New York; formerly Maple Syrup, Inc.): "
                       "one offering, first sale 2022-05-26, $17.7M sold (the seed; filed 2022-06-10, amended 2022-09-12); "
                       "no later filing",
                       "googlenews: Google News, \"Magna\" token with round and exit words (2026-09-29) -> the September "
                       "2022 seed (The Block, PR Newswire, CoinDesk, Pulse 2.0), 2024 product news and the February 2026 "
                       "Kraken purchase (Fortune, Kraken's blog, DL News); no round between them",
                       "bingnews: Bing News, \"Magna\" token management (2026-09-29) -> the 2022 seed release and the "
                       "February 2026 acquisition coverage (Yahoo Finance, CoinDesk, Bitcoin.com, Crowdfund Insider); no "
                       "later round",
                       "sibling:y-combinator: its row for Magna -> acquired, no later round in its note"],
             rounds=[rnd("2022-09-15", "Seed", 15_000_000, "Tiger Global; Tusk Venture Partners", True, u_s, "company"),
                     rnd("2022-05-26", "Form D offering (the seed, $17.7M sold)", 17_687_180, None, True,
                         MFD["2022-09-12"], "filing"),
                     rnd("2026-02-13", "Acquisition (Payward, Kraken's parent)", None, "Payward", None, u_end)],
             country="US", city="New York", city_src="formd_address", focus="Crypto & Web3",
             note="Token management platform (vesting, claims, distributions), New York (the Form D address; YC's row "
                  "agrees). Tiger co-led the $15M seed at a $70M valuation (September 2022). S2A: the seed was its last "
                  "round; Payward, Kraken's parent, bought the company in February 2026 (CoinDesk, Yahoo Finance) -> not "
                  "graduated, a cited end."))

# 34. Miferia: S2A.
L.append(cls("miferia", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=ASOF,
             surfaces=jl.GRADLINES("miferia", formd_note=FORMD_NONE("Miferia", "a Mexican company (also 'Mercanto')"),
                                   extra=["bingnews: Bing News, \"Miferia\" and \"Mercanto\" Mexico (2026-09-29) -> the "
                                          "August 2022 seed coverage only (PR Newswire, TechCrunch via Yahoo, 36Kr); no "
                                          "later round",
                                          "web: web search 'Miferia Mercanto México ronda inversión' (2026-09-29) -> the "
                                          "2022 seed coverage (Entrepreneur, El Referente) and the company's rename to "
                                          "Mercanto; no later round"]),
             note="S2A: Tiger co-led the $7M seed of August 2022 with Bain Capital Ventures, the company's first "
                  "institutional round; the business now trades as Mercanto and no later round is on any surface through "
                  "2026-09-29 -> not graduated."))

# 35. Mojo: Tiger and Thrive in the $75M Series A (2022).
u = REC("mojo")
L.append(verdict("mojo", "member",
                 "Fortune (2022-04-07): 'Mojo, which is headquartered in New York, recently raised $75 million in Series A "
                 "funding from Thrive Capital and Tiger Global'.",
                 ec="web", conf="high", cite=u))
L.append(cls("mojo", status="unknown", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=u, stage_conf="medium", entry_date="2022",
             rounds=[rnd("2022", "Series A", 75_000_000, None, True, u)],
             country="US", city="New York", focus="Media, Gaming & Advertising",
             note="Sports-betting app co-founded by Marc Lore and Alex Rodriguez, headquartered in New York (Fortune). "
                  "Tiger and Thrive backed its $75M Series A in early 2022, the first round naming Tiger; the investors of "
                  "any earlier seed are not on record. It cut 20% of staff (Business Insider, November 2023), agreed in "
                  "December 2023 to sell its pricing and trading technology and closed its New Jersey sportsbook while "
                  "saying the company would continue (Covers), and sold its app technology in February 2024 (Yahoo "
                  "Sports); nothing later shows it operating, so the status is unknown. The pre-filled Australia is a "
                  "wrong Wikidata join; the Y Combinator row named Mojo (Paris, acquired) is a different company."))

# 36. Moss: Tiger led the EUR 75M Series B; the 2026 Series C marks it at $1.16B.
u = REC("moss")
u_eu = PR("moss", "EU-Startups")
L.append(verdict("moss", "member",
                 "FinTech Global (2022-01-25): 'Tiger Global and A-Star joined the Series B round'; Startbase: 'Das "
                 "amerikanische Venture Capital-Unternehmen Tiger Global Management hat die Runde angeführt' (Tiger led the "
                 "EUR 75M round).",
                 ec="web", conf="high", cite=u))
L.append(cls("moss", status="private", **V("moss", "cherry"),
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2022-01",
             rounds=[rnd("2022-01-19", "Series B", 86_000_000, "Tiger Global", True, u_eu)],
             country="DE", country_src="web_verified", country_cite=u, city="Berlin", focus="Fintech & Payments",
             note="Spend management for European companies, Berlin. Tiger led the EUR 75M (about $86M) Series B of January "
                  "2022 at $573M (FinTech Global) as a new investor (FinanzBusiness), after Cherry's 2019 seed and Valar's "
                  "Series A, so the Series B is its entry. Momentum slice (fintech, first seen 2022): the 2026 Series C at "
                  "$1.16B (Sifted, as in the Cherry book) is the current mark. The Y Combinator row named Moss (San "
                  "Francisco, developer tools) carries this company's mark, which looks like a name collision in that "
                  "book."))

# 37. New York Life Insurance & Annuity Corp: a homonym director.
L.append(verdict("new-york-life-insurance-annuity-corp", "not_member",
                 "Homonym (D7): the ALEXANDER COOK on this issuer's 2023 and 2024 Form Ds is a director of New York Life "
                 "Insurance and Annuity Corporation (New York), whose filings cover the insurer's own separate-account "
                 "offerings with billions sold, not Tiger's Alex Cook; no Tiger round exists in an insurer's product "
                 "offerings.",
                 ec="formd_adjudicated", conf="high", cite=SEC("new-york-life-insurance-annuity-corp", "formd", 0)))

# 38. Oico: S2A.
L.append(cls("oico", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=ASOF,
             surfaces=jl.GRADLINES("oico", formd_note=FORMD_NONE("Oico", "a Brazilian company"),
                                   extra=["bingnews: Bing News, \"Oico\" construção (2026-09-29) -> the January 2022 R$30M "
                                          "seed coverage (Globo, Baguete) and the May 2023 pause (Terra); no later round",
                                          "web: web search 'Oico marketplace materiais de construção 2024 rodada "
                                          "investimento' (2026-09-29) -> the 2020 pre-seed and seed, the January 2022 seed "
                                          "and the 2023 pause; no later round"]),
             note="S2A: Tiger joined the R$30M seed Valor led (January 2022); in May 2023 Oico paused operations, cut staff "
                  "and looked for a new model (Terra), and no later round is on any surface -> not graduated."))

# 39. Opto Investments: Tiger led the $145M Series A at $475M.
u = REC("opto-investments")
u_a = PR("opto-investments", "RIABiz")
L.append(verdict("opto-investments", "member",
                 "Bloomberg Law (2022-09-21): 'The financing was led by Tiger Global Management LLC with participation from "
                 "venture capital firms including 8VC, Fin Capital and HOF Capital', valuing Opto at $475M; RIABiz: Tiger "
                 "'will invest at least $50 million as part of the Series A funding round'.",
                 ec="web", conf="high", cite=u))
L.append(cls("opto-investments", status="private", rng="below_1b", usd=475_000_000, val_src="web_verified",
             val_cite=u, asof="2022-09-21", extra=dict(WV), flags=["stale"],
             stage="Series A", stage_src="web_verified", stage_cite=u_a, stage_conf="high", entry_date="2022-09-20",
             rounds=[rnd("2022-09-20", "Series A", 145_000_000, "Tiger Global", True, u_a)],
             country="US", city="New York", focus="Fintech & Payments",
             note="Private-markets platform for investment advisers, New York (its releases' dateline). Tiger led the "
                  "$145M Series A at $475M when the company left stealth (September 2022), its first round. Momentum "
                  "slice (fintech, first seen 2022): no later priced round (Bing News 2026-09-29: partnerships, advisory "
                  "appointments and a May 2026 AI fund close only), so the 2022 mark stands, stale."))

# 40. Path Robotics: Tiger led the $100M Series C.
u = PR("path-robotics", "TechCrunch")
L.append(verdict("path-robotics", "member",
                 "TechCrunch (2021-07-20): Path Robotics 'has raised $100 million, led by Tiger Global and featuring "
                 "participation from Silicon Valley Bank, an existing investor', a pre-emptive Series C; Tiger also joined "
                 "the 2024 round (The Robot Report).",
                 ec="web", conf="high", cite=u))
L.append(cls("path-robotics", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-07-20",
             rounds=[rnd("2021-05", "Series B", 56_000_000, None, False, u),
                     rnd("2021-07-20", "Series C", 100_000_000, "Tiger Global", True, u),
                     rnd("2024-10-28", "unnamed round", 100_000_000, "Matter Venture Partners; Drive Capital", True,
                         REC("path-robotics"))],
             country="US", city="Columbus", focus="Industrial & Robotics",
             note="AI welding robots, Columbus, Ohio (TechCrunch). Tiger led the pre-emptive $100M Series C of July 2021, "
                  "two and a half months after the $56M Series B, and joined the $100M round of October 2024 led by "
                  "Matter Venture Partners and Drive Capital. No round states a valuation, so below $1B (Rule A)."))

# 41. PAX Labs: Tiger an existing investor by the 2019 $420M round at $1.7B; its entry is not on record.
u = REC("pax")
u_v = PR("pax", "Confirmed: Pax Labs raises")
L.append(verdict("pax", "member",
                 "Crunchbase News (2019-04-16, updated): PAX's $420M round 'Investors included Tiger Global Management, Tao "
                 "Capital Partners, and Prescott General Partners'; TechCrunch (2019-04-22): the round came 'from existing "
                 "investors Tiger Global Management and Tao Capital Partners' and new investors.",
                 ec="web", conf="high", cite=u))
L.append(cls("pax", status="private", rng="1b_plus", usd=1_700_000_000, val_src="web_verified", val_cite=u_v,
             asof="2019-04-22", extra=dict(WV), flags=["stale"], clear=["needs_web_value"],
             stage="undetermined",
             rounds=[rnd("2018-10", "unnamed round", 20_000_000, None, None, u),
                     rnd("2019-04-22", "unnamed round at $1.7B", 420_000_000, None, True, u_v)],
             country="US", city="San Francisco", focus="Consumer & Marketplaces",
             note="PAX Labs, vaporizer maker (founded 2007 as Ploom), San Francisco. Tiger was already an investor when "
                  "PAX raised $420M at $1.7B in April 2019 (TechCrunch); the round in which Tiger first came in is not on "
                  "record (Bing and Google News searched 2026-09-29), so the stage is undetermined. The $1.7B is the last "
                  "priced round, stale; PAX cut a quarter of its staff in October 2019 (MJBizDaily), which is not a priced "
                  "event. The unicorn-list flag is replaced by the cited figure. The Y Combinator row named Pax (San "
                  "Francisco, SaaS) is a different company; the Khosla row named Pax is itself flagged unresolved."))

# 42. PetLove Cayman: entry stage only.
PFD = SEC("petlove-cayman-ltd", "formd", 0)
L.append(cls("petlove-cayman-ltd", stage="undetermined",
             rounds=[rnd("2013-01", "Form D offering of PetLove Cayman, Ltd. (Lee Fixel a director)", 9_808_256, None, None,
                         PFD, "filing")],
             note="Entry stage: Lee Fixel sat on PetLove Cayman's January 2013 Form D ($9.8M sold, no earlier filing), but "
                  "the Brazilian business predates the Form D band's company-age test (model knowledge: Petlove dates from "
                  "1999) and no source names the round Tiger bought (Bing and Google News searched 2026-09-29, no item), "
                  "so the stage is undetermined rather than the band's Series A."))

# 43. Rebill: S2A.
L.append(cls("rebill", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=ASOF,
             surfaces=jl.GRADLINES("rebill", formd_note=FORMD_NONE("Rebill", "an Argentine company"),
                                   extra=["bingnews: Bing News, \"Rebill\" fintech (2026-09-29) -> the August-September 2022 "
                                          "seed and Mexico expansion coverage (TechCrunch, La Crónica, El Economista) and a "
                                          "September 2026 interview in Portafolio; no later round",
                                          "web: web search 'Rebill fintech Latin America raises Series A 2023 OR 2024 OR "
                                          "2025' (2026-09-29) -> no report of a Series A or any later round"]),
             note="S2A: Tiger led the August 2022 seed (US$3.6M across two rounds); the company still operates (Portafolio, "
                  "2026-09-24) but no later round is on any surface -> not graduated."))

# 44. Restaurant365: ICONIQ led the $88M round in 2019, joined by Tiger.
u = REC("restaurant365")
L.append(verdict("restaurant365", "member",
                 "PR Newswire (2019-06-27): 'ICONIQ Capital leads this round of funding and is joined by Tiger Global "
                 "Management and Bessemer Venture Partners (BVP led Restaurant365's Series A and Series B funding)'.",
                 ec="web", conf="high", cite=u))
L.append(cls("restaurant365", status="private", **V("restaurant365", "iconiq-growth"), flags=["stale"],
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2019-06-27",
             rounds=[rnd("2019-06-27", "Series C", 88_000_000, "ICONIQ Capital", True, u, "company")],
             country="US", city="Irvine", focus="SaaS",
             note="Restaurant accounting and operations software, Irvine. Tiger joined the $88M round ICONIQ led in June "
                  "2019, after Bessemer's Series A and B (the release), so the Series C is its entry. The $135M round of "
                  "May 2023 put it at $1B (Orange County Business Journal, as in the ICONIQ book); ICONIQ's May 2024 round "
                  "gave no valuation, so the 2023 mark stands, stale."))

# 45. Satylca S.C.A: a Despegar group entity; the group is out as a control position.
DESP = LEDGER_CITE("despegar-com-corp")
L.append(verdict("satylca-s-c-a", "not_member",
                 "Control position (T3 addendum), the Despegar group ruling: Satylca S.C.A (Buenos Aires) is a Despegar "
                 "group entity whose 2012 Form Ds list Charles Coleman and Scott Shleifer (Tiger) as directors. The IPO "
                 "registration statement shows Tiger's funds (PIP IV, Tiger Global Investments and affiliates) holding 57.3% "
                 "of Despegar before the 2017 IPO, a majority stake; same basis as despegar-com-corp.",
                 ec="fund_filing", conf="medium", cite=DESP, exclusion="control_position"))

if __name__ == "__main__":
    jl.write("delta-001c", L)
