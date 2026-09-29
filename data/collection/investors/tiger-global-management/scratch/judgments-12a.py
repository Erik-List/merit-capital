#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 12, chunk a (rows 1-15). Run: NQ_TAG=b12 python3 judgments-12a.py

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

# 1. Ruangguru: Tiger led the April 2021 round (after the 2019 Series C).
u = REC("ruangguru")
L.append(cls("ruangguru", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-04",
             country="ID", country_src="web_verified", country_cite=W("Ruangguru"), city="Jakarta",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2019-12", "Series C", 150_000_000, "General Atlantic", False, None, "press"),
                     rnd("2021-04", "growth round", 55_000_000, "Tiger Global Management", True, u)],
             note="Indonesian learning app, Jakarta (Wikipedia confirms the prefilled ID). Tiger led the $55M round "
                  "of April 2021 (the company's release; Wikipedia), which came after the December 2019 Series C, "
                  "so Growth. Reported near a $1B valuation (Tempo, 2021) but no priced $1B round; layoffs in "
                  "November 2022 (Bloomberg)."))

# 2. RummyCircle: Games24x7's rummy app (the company is also the 'games24x7' row).
u = NEWS("rummycircle", "Play Games24x7 discloses investment by Tiger Global")
L.append(cls("rummycircle", status="private", rng="below_1b",
             stage="undetermined",
             country="IN", country_src="web_verified",
             country_cite=NEWS("rummycircle", "India's Games24x7 valued at $2.5 billion in new funding"),
             city="Mumbai", focus="Media, Gaming & Advertising",
             rounds=[rnd("2012-08", "unnamed round", None, None, True, u),
                     rnd("2022-03", "growth round", 75_000_000, "Malabar Investments", True,
                         NEWS("rummycircle", "Games24x7 becomes unicorn, with a $75-million funding round"))],
             note="RummyCircle is the rummy app of Play Games24x7, a 'Mumbai-headquartered' company (TechCrunch via "
                  "Yahoo) that is also the base's 'games24x7' row: one company, two rows. Tiger's money went in by "
                  "2012 (VCCircle: 'Play Games24x7 discloses investment by Tiger Global'); the round is unnamed, so "
                  "the stage is undetermined. Tiger joined the March 2022 $75M round at $2.5B. Collapse evidence: "
                  "India's August 2025 law banning real-money online games shut the company's core business, and "
                  "Games24x7 cut about 70% of staff (500 people, Inc42 and MSN, September 2025), so the 2022 mark "
                  "no longer stands; below_1b, a second look for the A/B pass.",
             extra={"valuation_range_source": "web_verified",
                    "valuation_citation": NEWS("rummycircle", "Games24X7 to lay off 70% employees")}))

# 3. Run:ai: Tiger co-led the Series C (membership open).
u = PR("run-ai", "techcrunch.com/2022/03/15/runai")
L.append(verdict("run-ai", "member",
                 "TechCrunch (2022-03-15): Tel Aviv-based Run:ai 'raised a $75 million Series C funding round led by "
                 "Tiger Global Management and Insight Partners'", ec="web", conf="high", cite=u))
L.append(cls("run-ai", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2022-03",
             country="IL", country_src="web_verified", country_cite=u, city="Tel Aviv", focus="AI & Applied AI",
             rounds=[rnd("2021-01", "Series B", 30_000_000, "Insight Partners", False, None, "press"),
                     rnd("2022-03", "Series C", 75_000_000, "Tiger Global Management and Insight Partners", True, u)],
             note="GPU orchestration for AI workloads, Tel Aviv. Tiger co-led the $75M Series C of March 2022 with "
                  "Insight, which had led the $30M Series B of January 2021 (Insight's row). Acquired by Nvidia, "
                  "closed December 2024."))

# 4. Rupifi: Tiger co-led the Series A.
u = REC("rupifi")
c = NEWS("rupifi", "Fintech Platform Rupifi raises $4.1 Million Led by Quona")
L.append(cls("rupifi", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2022-01",
             country="IN", country_src="web_verified", country_cite=c, city="Bangalore", focus="Fintech & Payments",
             rounds=[rnd("2021-03", "pre-Series A", 4_100_000, "Quona Capital", False, c),
                     rnd("2022-01", "Series A", 25_000_000, "Bessemer Venture Partners and Tiger Global", True, u)],
             note="B2B buy-now-pay-later and payments for small businesses, Bengaluru-based (SiliconIndia). Tiger "
                  "co-led the $25M Series A of January 2022 with Bessemer (CIOL; Moneycontrol); the 2020 pre-seed "
                  "and the $4.1M pre-Series A of March 2021 (Quona) did not name it. Momentum slice (fintech), "
                  "checked 2026-09-29: only a small 2025 rights issue from existing investors; no $1B round."))

# 5. Saavn: Tiger was an existing investor at the 2015 Series C; merged into JioSaavn.
u = NEWS("saavn", "Music streaming firm Saavn raises $100M from Tiger Global")
L.append(cls("saavn", status="acquired", rng="below_1b", stage="undetermined",
             country="IN", country_src="web_verified", country_cite=W("JioSaavn"), city="Mumbai",
             focus="Media, Gaming & Advertising",
             rounds=[rnd("2015-07", "Series C", 100_000_000, "Tiger Global Management", True, u)],
             note="Music streaming; a US-based company until Reliance bought control in March 2018 and merged it "
                  "with JioMusic as JioSaavn (Mumbai, Wikipedia), the last known seat. Tiger led the $100M Series C "
                  "of July 2015 as an 'existing investor' (VCCircle), so its first round was earlier and is not on "
                  "record here: stage undetermined."))

# 6. SafeNet: adviser 13G on a listed company only.
L.append(verdict("safenet-inc", "not_member",
                 "13G/13F position in a listed company, no private round naming the firm (T3, D3): the adviser's "
                 "Schedule 13G filings of 2003-2004 cover SafeNet, a Nasdaq-listed company since long before; no "
                 "private round names Tiger", ec="fund_filing", conf="high", cite=SEC("safenet-inc", "edgar")))

# 7. SafetyCulture: Tiger joined the 2018 round.
u = REC("safetyculture")
L.append(cls("safetyculture", status="private",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="medium", entry_date="2018-05",
             country="AU", country_src="web_verified", country_cite=u, city="Sydney", focus="SaaS",
             rounds=[rnd("2018-05", "Series C", None, None, True, u)],
             note="Workplace inspection and safety software, Sydney (founded in Townsville). AFR (May 2018): "
                  "'SafetyCulture raises $60m as Tiger Global, Blackbird and Scott Farquhar pile in', the A$60M "
                  "round after the company's earlier venture rounds, so Growth; no earlier round names Tiger. "
                  "Valuation left to the web pass (needs_web_value); The Australian put it at $2.1B in 2022."))

# 8. Samsara: PIP XI and Tiger Global Investments are Series F holders under the IRA.
u = REC("samsara")
L.append(cls("samsara",
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="medium", entry_date="2019-09",
             country="US", country_src="web_verified", country_cite=W("Samsara (company)"), city="San Francisco",
             focus="Industrial & Robotics",
             rounds=[rnd("2019-09", "Series F", 300_000_000, None, True, u, "filing"),
                     rnd("2020-05-15", "Series F extension", None, None, None, u, "filing")],
             note="Connected-operations (industrial IoT) platform, San Francisco (NYSE: IOT); the prefilled MT was "
                  "a one-word Wikidata join and is corrected to US. The S-1's investors' rights agreement treats "
                  "Tiger Global Private Investment Partners XI, Tiger Global Investments and John Curtius as one "
                  "Major Investor among the Series F holders; Wikipedia names Tiger among the backers of the rounds "
                  "that took the valuation to $6.3B by September 2019, the $300M Series F, read as the entry "
                  "(medium: the May 2020 Series F extension is the other candidate). Growth either way; a PIP "
                  "vehicle is named, so the home desk."))

# 9. SBA Communications: adviser 13G on a listed company only.
L.append(verdict("sba-communications-corp", "not_member",
                 "13G/13F position in a listed company, no private round naming the firm (T3, D3): the adviser's "
                 "Schedule 13G filings of 2008-2009 and 13F lines of 2006-2008 cover SBA Communications, "
                 "Nasdaq-listed since 1999; no private round names Tiger", ec="fund_filing", conf="high",
                 cite=SEC("sba-communications-corp", "edgar")))

# 10. Scalapay: Tiger led the Series A; unicorn Series B.
u = REC("scalapay")
v = PR("scalapay", "prnewswire.co.uk")
L.append(cls("scalapay", status="private", rng="1b_plus", usd=1_000_000_000, val_src="web_verified", val_cite=v,
             asof="2022-02-23", extra={"valuation_range_source": "web_verified"}, flags=["stale"],
             stage="Series A", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2021-09",
             country="IT", country_src="web_verified", country_cite=PR("scalapay", "milanofinanza.it"), city="Milan",
             focus="Fintech & Payments",
             rounds=[rnd("2021-01", "Seed", 48_000_000, "Fasanara Capital", False, W("Scalapay")),
                     rnd("2021-09", "Series A", 155_000_000, "Tiger Global", True, u, "company"),
                     rnd("2022-02", "Series B", 497_000_000, "Tencent and Willoughby Capital", None, v, "company")],
             note="Buy-now-pay-later, operating from Milan (MilanoFinanza: 'startup con sede a Milano'; its "
                  "registered head office is in Dublin, Independent.ie): the prefilled IT is right. Tiger led the "
                  "$155M Series A of September 2021 at $700M; the $48M seed (Fasanara) did not name it. Mark: the "
                  "$497M Series B of February 2022, which the company announced as making it a unicorn, 'a "
                  "valuation that exceeded one billion post-money' (Il Sole 24 Ore): recorded at the $1B floor, at "
                  "the band edge, stale. Still described as a unicorn in 2025-2026 (EIB loan, December 2025)."))

# 11. Scaler (InterviewBit): Tiger co-led the January 2020 Series A.
u = PR("interviewbit", "livemint.com/companies/news/interviewbit-raises-20-million-in-series-a")
L.append(cls("scaler", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2020-01",
             country="IN", country_src="web_verified", country_cite=u, city="Bangalore",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2020-01", "Series A", 20_000_000, "Tiger Global and Sequoia India", True, u),
                     rnd("2022-02", "Series B", 55_000_000, "Lightrock India", True,
                         NEWS("scaler", "Scaler raises $55 million Series B from Lightrock"))],
             note="Tech upskilling, Bengaluru. Scaler is InterviewBit Technologies' brand, so this row and the "
                  "base's 'interviewbit' row are one company. Tiger co-led the $20M Series A of January 2020 with "
                  "Sequoia India (Mint; Entrackr), after a Surge seed, and joined the $55M Series B of February 2022 "
                  "led by Lightrock. No $1B mark."))

# 12. Scribe: Tiger is an existing investor at the Series C (membership open).
u = PR("scribe", "techcrunch.com/2025/11/10")
L.append(verdict("scribe", "member",
                 "TechCrunch (2025-11-10): 'The all-equity Series C round was led by StepStone, with participation "
                 "from existing investors Amplify Partners, Redpoint Ventures, Tiger Global, Morado Ventures, and "
                 "New York Life Ventures'; Tiger held shares before the round", ec="web", conf="high", cite=u))
L.append(cls("scribe", status="private", rng="1b_plus", usd=1_300_000_000, val_src="web_verified", val_cite=u,
             asof="2025-11-10", extra={"valuation_range_source": "web_verified"},
             stage="undetermined", country="US", city="San Francisco", focus="SaaS",
             rounds=[rnd("2025-11", "Series C", 75_000_000, "StepStone", True, u)],
             note="Workflow documentation and AI process mapping (Scribe, scribehow.com), San Francisco; not the "
                  "YC row's Bangalore 'Scribe', a different company of the same name. Mark: the $75M Series C of "
                  "November 2025 at $1.3B post-money (TechCrunch). Tiger is named as an existing investor in that "
                  "round; the round it entered is not on record (Redpoint's first round was the 2024 Series B), so "
                  "the stage is undetermined."))

# 13. Sea Ltd: adviser 13G/13F on a listed company only.
L.append(verdict("sea-ltd", "not_member",
                 "13G/13F position in a listed company, no private round naming the firm (T3, D3): the adviser's "
                 "13F lines run from 2018-03-31 and its 13G from 2019, after Sea's NYSE listing of October 2017; "
                 "no private round of Sea (Garena) names Tiger, and the one press line is about Wati in Southeast "
                 "Asia", ec="fund_filing", conf="high", cite=SEC("sea-ltd", "edgar")))

# 14. Securden: Tiger led the Series A.
u = REC("securden")
L.append(cls("securden", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2022-04",
             country="US", city="Newark", focus="Security",
             rounds=[rnd("2020-07", "Seed", 1_200_000, "Accel", False, None, "press"),
                     rnd("2022-04", "Series A", 10_500_000, "Tiger Global Management", True, u)],
             note="Privileged access and password management, Newark, Delaware, with engineering in Chennai (as "
                  "Accel's row reads). Tiger led the $10.5M Series A of April 2022 (Zee Business; VCCircle); the "
                  "$1.2M seed of 2020 was Accel's. No $1B mark."))

# 15. SeekOut: Tiger led the March 2021 round, then the Series C at $1.2B.
u = PR("seekout", "www.yahoo.com/entertainment/seekout")
v = PR("seekout", "pulse2.com/seekout-115-million")
L.append(cls("seekout", status="private", rng="1b_plus", usd=1_200_000_000, val_src="web_verified", val_cite=v,
             asof="2022-01-12", extra={"valuation_range_source": "web_verified"}, flags=["stale"],
             stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="medium", entry_date="2021-03",
             country="US", city="Bellevue", focus="SaaS",
             rounds=[rnd("2021-03", "Series B", 65_000_000, "Tiger Global", True, u),
                     rnd("2022-01", "Series C", 115_000_000, "Tiger Global", True, v)],
             note="Talent search and recruiting software, Bellevue, Washington. Tiger backed the $65M round of March "
                  "2021 (TechCrunch via Yahoo), then led the $115M Series C of January 2022 at $1.2B ('Tiger doubles "
                  "down on SeekOut', TechCrunch; Pulse 2.0). Layoffs in 2024 (GeekWire) but no priced round below "
                  "the mark: 1b_plus, stale."))

if __name__ == "__main__":
    jl.write("batch-012a", L)
