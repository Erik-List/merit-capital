#!/usr/bin/env python3
"""PRO-167 Tiger Global, DELTA batch 1, chunk a (rows 1-15: 99 .. datarobot). Run: NQ_TAG=d1 python3 judgments-d1a.py

Every citation comes from a helper that reads a URL already on disk: the row's evidence view (PR / REC),
the press caches (NEWS, incl. this judge's Bing and Google items), Wikipedia (W), a filing on the row or
in the EDGAR full-text sweep (SEC / FTSDOC), or a sibling book's recorded citation (V / SIBC)."""
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
INV = HERE.parents[1]
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


FIRM = ("firm: tigerglobal.com, which publishes no portfolio, posts or announcements (five pages and a login, "
        "read 2026-09-29), and the firm's own fund filings -> no page of the firm names a later round of {}")


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


def FORMD_NONE(q, where):
    return (f"formd: EDGAR full-text search of Form D filings for '{q}' (2026-09-29) -> none; {where}, no filing by "
            f"the company and no single-deal vehicle named after it")


L = []

# 1. 99 (99Taxis): Tiger's early-2015 investment, bought out by Didi in 2018.
u_tg = NEWS("99", "99Taxis recebe novo investimento")
u_rt = PR("99", "Reuters | China's Didi Chuxing buys control")
L.append(verdict("99", "member",
                 "Baguete (2015-02-02): 99Taxis 'recebeu esta semana um novo aporte, proveniente do fundo internacional "
                 "Tiger Global' (a new investment from Tiger Global, amount undisclosed, larger than R$5M); Exame (2017) "
                 "lists Tiger with Monashees and Qualcomm Ventures among the funds of its earlier rounds, and Didi bought "
                 "Tiger's stake when it took control in January 2018 (Reuters). A private round Tiger joined.",
                 ec="web", conf="high", cite=u_tg))
L.append(cls("99", status="acquired", rng="below_1b", stage="undetermined",
             rounds=[rnd("2015-02", "undisclosed investment (round not named)", None, "Tiger Global", True, u_tg),
                     rnd("2015-04", "undisclosed investment (round not named)", None, "Monashees; Qualcomm Ventures", None,
                         NEWS("99", "99Taxis recebe 2")),
                     rnd("2017-01", "strategic investment", 100_000_000, "Didi Chuxing", False, REC("99")),
                     rnd("2018-01", "Acquisition (Didi Chuxing, control)", None, "Didi Chuxing", None, u_rt)],
             country="BR", country_src="web_verified", country_cite=u_rt, city="São Paulo",
             focus="Consumer & Marketplaces",
             note="99 (formerly 99Taxis), ride-hailing app, São Paulo. Tiger invested in early 2015 (Baguete), after "
                  "Monashees and Qualcomm Ventures had backed the company in 2012-2013; no source names Tiger's round, so "
                  "the stage is undetermined. Didi bought control in January 2018, buying out Riverwood, Monashees, "
                  "Qualcomm Ventures, Tiger and SoftBank (Reuters): acquired."))

# 2. Appwrite: Tiger led the $27M Series A.
u = REC("appwrite")
L.append(verdict("appwrite", "member",
                 "Calcalist (2022-04-05): 'Appwrite announced on Tuesday that it has raised $27 million in its Series A "
                 "round led by Tiger Global Management' (VentureBeat reports the same round).",
                 ec="web", conf="high", cite=u))
L.append(cls("appwrite", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2022-04-05",
             rounds=[rnd("2021-09-28", "Seed", 10_000_000, None, False, NEWS("appwrite", "gets $10M seed funding")),
                     rnd("2022-04-05", "Series A", 27_000_000, "Tiger Global", True, u)],
             country="IL", country_src="web_verified", country_cite=u, city="Tel Aviv", focus="DevTools & APIs",
             note="Open-source backend-as-a-service, an Israeli company (Calcalist) with a remote team; Tel Aviv from "
                  "model knowledge. Tiger led the $27M Series A (Apr 2022, with Bessemer, Flybridge, Ibex and Seedcamp, "
                  "VentureBeat); the $10M raised across two earlier seed rounds does not name Tiger. Momentum slice "
                  "(developer tools, first seen 2022): no later priced round found (Bing News, 2026-09-29)."))

# 3. ARMO: Tiger led the $30M Series A.
u = REC("armo")
L.append(verdict("armo", "member",
                 "TechCrunch (2022-04-27): ARMO 'has raised a $30 million Series A funding round led by Tiger Global'; "
                 "SiliconANGLE (2025) still lists Tiger Global Management among its investors.",
                 ec="web", conf="high", cite=u))
L.append(cls("armo", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2022-04-27",
             rounds=[rnd("2022-04-27", "Series A", 30_000_000, "Tiger Global", True, u)],
             country="IL", country_src="web_verified", country_cite=u, city="Tel Aviv", focus="Security",
             note="ARMO, the Tel Aviv-based company behind the Kubescape Kubernetes security platform (TechCrunch). Tiger "
                  "led the $30M Series A (Apr 2022), its first round; still operating in 2025 (SiliconANGLE product news). "
                  "No priced round at $1B or more."))

# 4. August Schools: S2A. Two later Form D offerings, each under twice the seed; no source names a Series A.
AS_FD = FORMD_FTS("August Schools")
L.append(cls("august-schools", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=ASOF,
             surfaces=jl.GRADLINES("august-schools",
                                   formd_note="EDGAR full-text search of Form D filings for 'August Schools' (2026-09-29) "
                                              "-> August Schools, Inc. (CIK 1919986, New York): first sale 2022-03-08, $6.0M "
                                              "sold (the seed); 2024-05-28, $5.0M sold of $6.5M offered; 2025-11-07, $4.5M "
                                              "sold of $6.5M offered; no later priced round at twice the entry, and no "
                                              "single-deal vehicle named after the company",
                                   extra=["bingnews: Bing News, \"August Schools\" (2026-09-29) -> no item",
                                          "company: augustschools.com (read 2026-09-29) -> 'Built with brains in NYC'; no "
                                          "funding, press or news page",
                                          "web: web search '\"August Schools\" funding round 2024 OR 2025 Series A' "
                                          "(2026-09-29) -> no publisher report of a round; only vendor profiles, which label "
                                          "the 2024 and 2025 Form D offerings 'Series A' with no announcement behind them "
                                          "(Rule A: not evidence)"]),
             city="New York", city_src="formd_address", clear=["city_unknown"],
             rounds=[rnd("2022-04-05", "Seed", 5_000_000, "Tiger Global", True, PR("august-schools", "Business Wire")),
                     rnd("2024-05-28", "unnamed Form D offering ($5.0M sold of $6.5M)", 4_999_999, None, None,
                         AS_FD["2024-06-06"], "filing"),
                     rnd("2025-11-07", "unnamed Form D offering ($4.5M sold of $6.5M)", 4_515_122, None, None,
                         AS_FD["2025-11-17"], "filing")],
             note="S2A: Tiger led the Apr 2022 seed ($5M; $6.0M on the Form D). The company has since filed two Form Ds "
                  "(May 2024, $5.0M sold; Nov 2025, $4.5M sold), each under twice the seed, and no publisher, filing or "
                  "company page names either a Series A; vendors call them Series A without a source. Under the step-up "
                  "test for unnamed rounds the row did not graduate. Flagged for a second look. City from the Form D "
                  "address and the company's own site (New York)."))

# 5. Axis: S2A. The seed dates to late 2021 (TechCrunch: almost 18 months before the May 2023 launch).
axis_lines = [x for x in jl.GRADLINES("axis", formd_note=FORMD_NONE("Axis Pay", "an Egyptian company")[7:])
              if not x.startswith(("googlenews:", "googlenews_firm:", "sibling:"))]
L.append(cls("axis", entry_date="2021",
             grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=ASOF,
             surfaces=axis_lines + [
                 "googlenews: Google News, \"Axis\" with round and exit words -> 85 headlines about other companies called "
                 "Axis (Axis Bank, Axis Security, Axis Robotics and others), none a round of the Egyptian fintech",
                 "googlenews_firm: Google News, \"Axis\" \"Tiger Global\" -> the May-June 2023 launch and licence coverage "
                 "that recalls the $8.25M seed (TechCrunch, EnterpriseAM, waya.media, BitKE); no later round",
                 "bingnews: Bing News, \"Axis Pay\" and \"Axis\" Egypt fintech (2026-09-29) -> the 2023 launch coverage, an "
                 "October 2023 interview (The Africa Report), a June 2026 lending partnership (Zawya) and an August 2026 "
                 "CEO interview (Ahram); no funding round after the seed",
                 "web: web search 'Axis Pay Egypt fintech raises funding round Series A' (2026-09-29) -> no publisher report "
                 "of a later round; one vendor profile lists a 2026 'Series A' with no amount or announcement behind it "
                 "(Rule A: not evidence)"],
             note="S2A: TechCrunch (2023-05-17) says Axis raised its $8.25M seed, co-led by Tiger Global, Sawari Ventures "
                  "and Raba, almost 18 months before its May 2023 launch, so the entry is late 2021: entry_date corrected "
                  "from 2023 to 2021. The company still operates (2026 partnerships and a CEO interview) but no later "
                  "round is on any publisher surface -> not graduated. A vendor's unannounced 2026 'Series A' is flagged "
                  "for a second look. The two Y Combinator rows named Axis are different companies."))

# 6. Buf Technologies: Tiger co-led the $68M fourth financing with Lux.
u = REC("buf-technologies")
L.append(verdict("buf-technologies", "member",
                 "The Globe and Mail (2021-12-12): Buf raised US$93.4M in four financings 'including a US$68-million "
                 "funding last month co-led by New York funds Lux Capital and Tiger Global'.",
                 ec="web", conf="high", cite=u))
L.append(cls("buf-technologies", status="private", rng="below_1b",
             stage="Growth", stage_src="model", stage_conf="medium", entry_date="2021-11",
             rounds=[rnd("2020-09", "Seed", 3_700_000, "Lightspeed Venture Partners", False, u),
                     rnd("2021-11", "fourth financing (the Series B in the Lux book)", 68_000_000,
                         "Lux Capital; Tiger Global", True, u)],
             country="CA", country_src="web_verified", country_cite=u, city="Toronto", focus="DevTools & APIs",
             note="Protocol Buffers tooling, Toronto (aligned with the Lux book). Tiger co-led the $68M round of November "
                  "2021, the fourth financing in 22 months after a Lightspeed-led $3.7M seed (Globe and Mail), which the Lux "
                  "book records as the Series B: Growth, from the named deal. Momentum slice (developer tools, first seen "
                  "2021): no later priced round found (Bing News, 2026-09-29)."))

# 7. BukuKas (Lummo): Tiger co-led the Series C; the company ceased operating in 2023.
u = REC("bukukas")
u_c = PR("bukukas", "The Jakarta Post")
L.append(verdict("bukukas", "member",
                 "CNBC Indonesia (2023-05-15): BukuKas's parent Lummo 'pada Januari 2022 mengumumkan pendanaan seri C "
                 "senilai Rp 1,14 triliun dari investor startup raksasa Tiger Global dan Sequoia Capital India' (a Series C "
                 "from Tiger Global and Sequoia India); The Jakarta Post: the $80M Series C was 'led by Tiger Global and "
                 "Sequoia Capital India'.",
                 ec="web", conf="high", cite=u))
L.append(cls("bukukas", status="defunct", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=u_c, stage_conf="high", entry_date="2022-01",
             rounds=[rnd("2021-01", "Series A", 10_000_000, "Sequoia Capital India", False,
                         NEWS("bukukas", "BukuKas gets $50M")),
                     rnd("2021-05", "Series B", 50_000_000, None, False, NEWS("bukukas", "series B round")),
                     rnd("2022-01", "Series C", 80_000_000, "Tiger Global; Sequoia Capital India", True, u_c)],
             country="ID", country_src="web_verified", country_cite=u, city="Jakarta", focus="Fintech & Payments",
             note="BukuKas (renamed Lummo in January 2022), bookkeeping and payments app for Indonesian merchants, "
                  "Jakarta. Tiger co-led the $80M Series C with Sequoia India (Jan 2022); it is not named in the $10M "
                  "Series A (Sequoia India) or the $50M Series B (TechCrunch, May 2021), so the Series C is its entry. The "
                  "BukuKas app stopped working after 26 May 2023 and former staff say Lummo no longer operates (CNBC "
                  "Indonesia): defunct."))

# 8. Catch of the Day: a minority investment in 2011; the founders kept control.
u = REC("catch-of-the-day")
L.append(verdict("catch-of-the-day", "member",
                 "delimiter (2011-05-23): Catch of the Day 'said the list of investors included Packer's Consolidated "
                 "Press Holdings, Seek co-founder and chief executive Andrew Bassat, Glenn Poswell ... and hedge fund Tiger "
                 "Global Management', investment capital into the private company at a reported $200M valuation, with the "
                 "founders keeping a controlling stake (so not a control position).",
                 ec="web", conf="medium", cite=u))
L.append(cls("catch-of-the-day", status="acquired", rng="below_1b", stage="undetermined",
             rounds=[rnd("2011-05", "minority investment by a consortium (round not named)", None, None, True, u)],
             country="AU", country_src="web_verified", country_cite=u, city="Melbourne",
             focus="Consumer & Marketplaces",
             note="Daily-deals e-commerce site (later Catch Group), Melbourne. In May 2011 a consortium of Consolidated "
                  "Press Holdings, Andrew Bassat, Glenn Poswell and Tiger Global invested at a reported $200M valuation "
                  "while the founders, Gabby and Hezi Leibovich, kept control (delimiter); the deal is not named as a "
                  "round, so the stage is undetermined. Wesfarmers bought Catch Group in 2019 (model knowledge): "
                  "acquired."))

# 9. Cedar: Tiger led the $200M Series D at $3.2B.
u = REC("cedar")
u_v = PR("cedar", "Bloomberg")
L.append(verdict("cedar", "member",
                 "newswire.com release (2021-03-09): 'Cedar Closes $200M in Series D Funding ... Led by Tiger Global "
                 "Management'.",
                 ec="web", conf="high", cite=u))
L.append(cls("cedar", status="private", rng="1b_plus", usd=3_200_000_000, val_src="web_verified", val_cite=u_v,
             asof="2021-03-09", extra=dict(WV), flags=["stale"],
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-03-09",
             rounds=[rnd("2021-03-09", "Series D", 200_000_000, "Tiger Global", True, u)],
             country="US", city="New York", focus="Healthcare & Bio",
             note="Patient billing and payments platform, New York (as in the Thrive book; the Felicis book's Seattle is "
                  "wrong). Tiger led the $200M Series D at $3.2B (Mar 2021; Bloomberg); Thrive incubated the company in 2016 "
                  "and the earlier rounds were Founders Fund-, Thrive- and a16z-led, so the Series D is Tiger's entry. No "
                  "later priced round: the mark is stale. The pre-filled Japan is a wrong Wikidata join on a one-word "
                  "name. The a16z and Y Combinator rows named Cedar are different companies (program entries in San "
                  "Francisco)."))

# 10. Cockroach Labs: Tiger co-led the Series C.
u = REC("cockroach-labs")
L.append(verdict("cockroach-labs", "member",
                 "Crunchbase News (2019-08-06): 'Cockroach Labs announced it raised $55 million in a Series C round co-led "
                 "by a trio of firms: Altimeter Capital, Tiger Global, and existing investor GV'.",
                 ec="web", conf="high", cite=u))
L.append(cls("cockroach-labs", status="private", **V("cockroach-labs", "coatue"), flags=["stale"],
             clear=["needs_web_value"],
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2019-08-06",
             rounds=[rnd("2019-08-06", "Series C", 55_000_000, "Altimeter Capital; Tiger Global; GV", True, u)],
             city="New York", focus="Data Infrastructure",
             note="Distributed SQL database (CockroachDB), New York. Tiger co-led the $55M Series C (Aug 2019) as a new "
                  "investor beside existing investor GV, its first round. The last priced round is the $278M Series F of "
                  "December 2021 at $5B (PR Newswire, as in the Coatue, GV and Sequoia books), older than 24 months: "
                  "stale. The unicorn-list flag is replaced by the cited figure."))

# 11. Commonwealth Fusion Systems: Tiger led the $1.8B Series B; no stated valuation (Rule A).
u = REC("commonwealth-fusion-systems")
w = W("Commonwealth Fusion Systems")
L.append(verdict("commonwealth-fusion-systems", "member",
                 "Canary Media (2021-12-02): 'Tiger Global Management led this funding round for Commonwealth Fusion "
                 "Systems' ($1.8B); Capital Brief (2025) repeats that Google joined 'a funding round led by Tiger Global "
                 "Management'.",
                 ec="web", conf="high", cite=u))
L.append(cls("commonwealth-fusion-systems", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-12",
             rounds=[rnd("2018", "initial funding", 50_000_000, "Eni", False, w),
                     rnd("2019", "Series A", 115_000_000, None, False, w),
                     rnd("2020", "Series A2", 84_000_000, None, False, w),
                     rnd("2021-12", "Series B", 1_800_000_000, "Tiger Global", True, u),
                     rnd("2025-08", "Series B2", 863_000_000, None, None, w)],
             city="Devens", focus="Climate & Energy",
             note="Fusion power company spun out of MIT, headquartered at its Devens, Massachusetts campus. Tiger led the "
                  "$1.8B Series B (Dec 2021) after the Eni seed funding and the Series A and A2 (Wikipedia), so the Series "
                  "B is its entry. No page states a valuation for any round, so under Rule A the row reads below $1B, "
                  "aligned with the Coatue and Khosla books; Coatue lists it among its open rulings as almost certainly "
                  "too low."))

# 12. Contractbook: Tiger led the $30M Series B; Scrive bought the company in 2025.
u = REC("contractbook")
u_x = NEWS("contractbook", "Svenskere overtager")
L.append(verdict("contractbook", "member",
                 "Legal IT Insider (2021-05-11): 'The $30 Million Series B round is led by Tiger Global with participation "
                 "from existing investors Bessemer Venture Partners, byFounders and Gradient Ventures'.",
                 ec="web", conf="high", cite=u))
L.append(cls("contractbook", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-05",
             rounds=[rnd("2020-12-09", "Series A", 9_400_000, "Bessemer Venture Partners", False,
                         NEWS("contractbook", "Contractbook Raises $9.4 Million in Series A")),
                     rnd("2021-05-11", "Series B", 30_000_000, "Tiger Global", True, u),
                     rnd("2025-06", "Acquisition (Scrive)", None, "Scrive", None, u_x)],
             country="DK", country_src="web_verified", country_cite=u_x, city="Copenhagen", focus="SaaS",
             note="Contract management platform, Copenhagen. Tiger led the $30M Series B (May 2021) after the Bessemer-led "
                  "$9.4M Series A (Dec 2020), so the Series B is its entry. Sweden's Scrive, owned by Vitruvian Partners, "
                  "took over the company in June 2025 (Borsen: 'Den kobenhavnske tech-virksomhed Contractbook ... overtages "
                  "nu af svenske Scrive'): acquired."))

# 13. CreditBook: S2A.
L.append(cls("creditbook", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=ASOF,
             surfaces=jl.GRADLINES("creditbook", formd_note=FORMD_NONE("CreditBook", "a Pakistani company")[7:],
                                   extra=["bingnews: Bing News, \"CreditBook\" Pakistan (2026-09-29) -> the May 2021 seed "
                                          "and the December 2021 pre-Series A coverage only (a Business Recorder item "
                                          "dated 2026 reprints the 2021 seed story); no later round",
                                          "web: web search 'CreditBook Pakistan fintech funding round 2023 OR 2024 Series A' "
                                          "(2026-09-29) -> the two 2021 rounds and a 2024 Rest of World interview with a "
                                          "co-founder; no later round"]),
             note="S2A: entry the $11M pre-Series A of December 2021 (read Seed); no Series A or later round on any "
                  "surface through 2026-09-29 -> not graduated."))

# 14. Cube26: S2A, a cited end (Paytm bought it in 2018 after the 2015 seed).
u_end = PR("cube26", "moneycontrol")
L.append(cls("cube26", grad="not_graduated", grad_src="web_verified", grad_cite=u_end, grad_conf="high",
             grad_asof=ASOF,
             surfaces=jl.GRADLINES("cube26", formd_note=FORMD_NONE("Cube26", "an Indian company")[7:],
                                   extra=["bingnews: Bing News, \"Cube26\" (2026-09-29) -> the October 2015 Rs 50 crore "
                                          "seed led by Tiger with Flipkart (Financial Express, Economic Times), the 2017 "
                                          "IoT shutdown (VCCircle) and the June 2018 Paytm purchase (inc42: 'backed by "
                                          "Tiger Global and Flipkart with $7.7 Mn Seed funding in 2015'); no later round"]),
             note="S2A: the October 2015 seed (Rs 50 crore, about $7.7M, led by Tiger with Flipkart) was its last round; "
                  "Paytm bought the company in June 2018 in a fire sale (Moneycontrol, Entrackr) -> not graduated, a cited "
                  "end."))

# 15. DataRobot: Tiger first appears in the $270M Series F (Nov 2020); co-led the Series G.
u = REC("datarobot")
u_f = PR("datarobot", "Pulse 2.0")
L.append(verdict("datarobot", "member",
                 "DataRobot release (2021-07-27): the $300M Series G 'was led by return investors Altimeter Capital and "
                 "Tiger Global'; Pulse 2.0 (2020-11-18) lists Tiger Global among the investors in the $270M round led by "
                 "Altimeter.",
                 ec="web", conf="high", cite=u))
L.append(cls("datarobot", status="private", **V("datarobot", "sutter-hill-ventures"), flags=["stale"],
             clear=["needs_web_value"],
             stage="Growth", stage_src="web_verified", stage_cite=u_f, stage_conf="high", entry_date="2020-11",
             rounds=[rnd("2019-09-17", "Series E", 206_000_000, "Sapphire Ventures", None,
                         NEWS("datarobot", "platform secures $206m in Series E")),
                     rnd("2020-11-17", "Series F (pre-IPO round)", 270_000_000, "Altimeter Capital", True, u_f),
                     rnd("2021-07-27", "Series G", 300_000_000, "Altimeter Capital; Tiger Global", True, u, "company")],
             country="US", city="Boston", focus="AI & Applied AI",
             note="Enterprise AI platform, Boston. Tiger first appears among the investors of the $270M pre-IPO round led "
                  "by Altimeter (the Series F, Nov 2020; Pulse 2.0), is not named in the Sapphire-led $206M Series E "
                  "(Sept 2019), and co-led the $300M Series G at $6.3B as a return investor (Jul 2021). The $6.3B (Reuters, "
                  "as in the Sutter Hill book) is the last priced primary, stale; secondary-market prices far under it are "
                  "platform estimates (Rule A). Momentum slice (AI, first seen 2021): no later priced round (Bing News, "
                  "2026-09-29)."))

if __name__ == "__main__":
    jl.write("delta-001a", L)
