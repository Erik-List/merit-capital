#!/usr/bin/env python3
"""PRO-167 grind, queue batch 5, chunk c (rows 16 and 31-45). Judge b5.

Evidence: the judge view (show.py --batch 5), the evidence pack, the Bing and Google candidate caches, Bing
lookups run with NQ_TAG=b5 (bq.py), sibling books' records, and pages fetched and read in this pass (the
literal URLs below). Every citation is read from disk by a helper or is a page fetched and read here."""
import json
import os
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, W, NEWS, SEC

HERE = Path(__file__).resolve().parent
PKD = json.loads((HERE / "evidence-pack.json").read_text())
BND = json.loads((HERE / "bing-news.json").read_text())
WV = {"valuation_range_source": "web_verified"}


def PK(slug, sub, kind="press"):
    """A URL from the row's evidence-pack lines (press '|| URL', sec line tail, wiki or recall parentheses)."""
    p = PKD.get(slug, {})
    if kind == "recall":
        m = re.findall(r"\((https?://[^)\s]+)\)", p.get("recall_basis") or "")
        if not m:
            raise SystemExit(f"PK recall {slug}")
        return m[-1]
    urls = []
    for x in p.get(kind) or []:
        if sub.lower() not in x.lower():
            continue
        if kind == "press":
            m = re.search(r"\|\| URL (\S+)", x)
        elif kind == "sec":
            m = re.search(r"\| (https?://\S+)\s*$", x)
        else:
            m = re.search(r"\((https?://[^)\s]+)\)", x)
        if m:
            urls.append(m.group(1))
    urls = list(dict.fromkeys(urls))
    if len(urls) != 1:
        raise SystemExit(f"PK({slug!r}, {sub!r}, {kind}) -> {urls}")
    return urls[0]


def BN(key, sub):
    """A publisher URL from the Bing candidate cache (bing-news.json[key]) whose title contains sub."""
    urls = list(dict.fromkeys(i["url"] for i in (BND.get(key) or {}).get("items", [])
                              if sub.lower() in i["title"].lower()))
    if len(urls) != 1:
        raise SystemExit(f"BN({key!r}, {sub!r}) -> {urls}")
    return urls[0]


def SIB(slug, inv):
    """(usd, asof, citation) of a sibling book's mark for the same company, from the evidence pack."""
    for x in PKD.get(slug, {}).get("sib", []):
        if x["investor"] == inv and x.get("val_cite"):
            return int(float(x["usd"])), x["asof"], x["val_cite"]
    raise SystemExit(f"SIB({slug!r}, {inv!r}) missing")


def SIBREC(inv, slug, key):
    """A key of a sibling book's own classification record (data/collection/investors/<inv>), read from disk."""
    d = HERE.parents[1] / inv / "companies"
    rec = {**json.loads((d / "resolved.json").read_text()).get(slug, {}),
           **json.loads((d / "classification.json").read_text()).get(slug, {})}
    if not rec.get(key):
        raise SystemExit(f"SIBREC({inv!r}, {slug!r}, {key!r}) missing")
    return rec[key]


T3 = "13G/13F position in a listed company, no private round naming the firm (T3, D3)"
L = []
CHECK = "2026-09-29"

L.append(verdict("electronic-arts-inc", "not_member",
                 T3 + ": Electronic Arts has been listed on Nasdaq since 1989; Tiger's 13F lists it 2009-2010 and its "
                      "13G dates from 2010-2011", ec="fund_filing", conf="high", cite=SEC("electronic-arts-inc", "edgar")))

# ---------------------------------------------------------------- falconx (recall seed confirmed)
FX_BW = PK("falconx", "Business Wire | FalconX Secures $50M Investment")
FX_C = PK("falconx", "Yahoo Finance | Crypto Platform FalconX Quintuples")
fx_usd, fx_asof, fx_cite = SIB("falconx", "accel")
L.append(cls("falconx", status="private", rng="1b_plus", usd=fx_usd, val_src="web_verified", val_cite=fx_cite,
             asof="2022-06-22", extra=WV, flags=["stale"],
             stage="Growth", stage_src="web_verified", stage_cite=FX_BW, stage_conf="high", entry_date="2021-03-11",
             country="US", city="San Mateo", focus="Crypto & Web3",
             note="Institutional crypto prime brokerage, San Mateo. Tiger and B Capital put in $50M in March 2021 "
                  "(the company's release), the round after the 2019 seed and the $17M 2020 round: Growth. The $210M "
                  "round at $3.75B followed in August 2021 and the $150M Series D at $8B (GIC and B Capital) in June "
                  "2022, the last primary mark, aligned with the Accel and Lightspeed rows; older than 24 months, so "
                  "stale.",
             rounds=[rnd("2021-03-11", "unnamed ($50M)", 50_000_000, "Tiger Global, B Capital", True, FX_BW, "company"),
                     rnd("2021-08-10", "unnamed ($210M, $3.75B)", 210_000_000, None, None, FX_C, "press"),
                     rnd("2022-06-22", "Series D", 150_000_000, "GIC, B Capital", None, fx_cite, "press")]))

# ---------------------------------------------------------------- fancraze (recall seed confirmed)
FZ_SEED = SIBREC("coatue", "fancraze", "entry_stage_citation")
FZ_A = PK("fancraze", "FanCraze Raises $100 Mn Led By Insight Partners")
L.append(cls("fancraze", status="private", rng="below_1b",
             stage="Seed", stage_src="web_verified", stage_cite=FZ_SEED, stage_conf="high", entry_date="2021-11",
             grad="graduated", grad_src="web_verified", grad_cite=FZ_A, grad_conf="high",
             country="US", country_src="web_verified", country_cite=SIBREC("insight-partners", "fancraze",
                                                                            "hq_country_citation"),
             city="New York", focus="Crypto & Web3",
             note="FanCraze (Faze Technologies), cricket digital collectibles on the Flow blockchain. Tiger led the "
                  "$17.4M seed round announced in November 2021 with Coatue, Sequoia India and Dapper Labs (Business "
                  "Standard; inc42): a Seed entry. The $100M Series A led by Insight Partners in March 2022 (inc42) "
                  "graduates the row. Country and city follow the Insight row's cited portfolio page (New York); the "
                  "Coatue row reads India with no city.",
             rounds=[rnd("2021-11", "Seed", 17_400_000, "Tiger Global", True, FZ_SEED, "press"),
                     rnd("2022-03-24", "Series A", 100_000_000, "Insight Partners", None, FZ_A, "press")]))

# ---------------------------------------------------------------- favo (recall seed confirmed)
FV_TC = PK("favo", "TechCrunch | Tiger Global backs Favo")
FV_GE = PK("favo", "gestion | Startup peruana Favo capta")
FV_END = PK("favo", "Startup peruana Favo cierra")
L.append(cls("favo", status="defunct", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=FV_TC, stage_conf="high", entry_date="2021-10-06",
             country="PE", country_src="web_verified", country_cite=FV_GE, city="Lima",
             focus="Consumer & Marketplaces",
             note="Social-commerce grocery ordering through community resellers, founded in Lima and expanding to "
                  "Mexico and Brazil. Tiger led the $26.5M Series A of October 2021 (TechCrunch; Gestion calls it a "
                  "Peruvian startup raising $26M from Tiger), the firm's entry. Favo closed operations in February "
                  "2024 (Gestion, 2024-02-26): defunct.",
             rounds=[rnd("2021-10-06", "Series A", 26_500_000, "Tiger Global", True, FV_TC, "press")]))

# ---------------------------------------------------------------- fazz (recall seed confirmed)
FA_C = PK("fazz", "TechCrunch | Southeast Asian fintech Fazz raises $100M")
FA_B = NEWS("fazz", "Payfazz gets $53 million")
L.append(cls("fazz", status="private", rng="below_1b",
             extra={"valuation_range_source": "web_verified", "valuation_citation": FA_C, "valuation_asof": CHECK},
             stage="undetermined",
             country="ID", country_src="web_verified", country_cite=FA_B, city="Jakarta", focus="Fintech & Payments",
             note="Fazz (Payfazz merged with Singapore's Xfers in 2021), agent-network and business payments, "
                  "Jakarta. Tiger was already an investor when it returned for Payfazz's $53M Series B of July 2020, "
                  "led by B Capital and Insignia (Yahoo Finance: 'Previous investors, including Tiger Global, Y "
                  "Combinator and ACE & Company, also returned'), and it led Fazz's $100M Series C in September 2022 "
                  "(TechCrunch). Its first round, the 2017 seed or the $21M 2018 Series A, is not named on record, so "
                  "the stage is undetermined. Momentum check " + CHECK + ": no priced round at $1B or more found.",
             rounds=[rnd("2020-07-06", "Series B", 53_000_000, "B Capital, Insignia Ventures", True, FA_B, "press"),
                     rnd("2022-09-13", "Series C", 100_000_000, "Tiger Global", True, FA_C, "press")]))

# ---------------------------------------------------------------- fiat chrysler (listed stock; seeds replaced)
L.append(verdict("fiat-chrysler-automobiles-n-v", "not_member",
                 T3 + ": Fiat Chrysler was listed in New York and Milan; Tiger's 13G filings (2018-2020) and "
                      "Bloomberg's 2018 report of a $1B holding describe a public-market position",
                 ec="fund_filing", conf="high", cite=SEC("fiat-chrysler-automobiles-n-v", "edgar")))

# ---------------------------------------------------------------- flatfile (recall seed confirmed)
FF_CB = PK("flatfile", "", "recall")
FF_PR = PK("flatfile", "irblog.prnewswire.com | Flatfile Raises $50 Million Series B")
L.append(cls("flatfile", status="private", rng="below_1b",
             extra={"valuation_range_source": "web_verified", "valuation_citation": FF_PR, "valuation_asof": CHECK},
             stage="Growth", stage_src="web_verified", stage_cite=FF_CB, stage_conf="high", entry_date="2022-09-27",
             country="US", city="Denver", focus="DevTools & APIs",
             note="Embeddable data import and onboarding platform, Denver. Tiger led the $50M Series B of September "
                  "2022 (Crunchbase News), after the 2020 $7.6M round and the 2021 Series A without Tiger: Growth. "
                  "Momentum check " + CHECK + ": the Bing search for its later rounds found none after the Series B.",
             rounds=[rnd("2022-09-27", "Series B", 50_000_000, "Tiger Global", True, FF_CB, "press")]))

# ---------------------------------------------------------------- float (recall seed confirmed)
FL_A = PK("float", "BetaKit | Tiger Global the latest suitor")
FL_B = NEWS("float", "Float raises $70-million Series B CAD")
L.append(cls("float", status="private", rng="below_1b",
             extra={"valuation_range_source": "web_verified", "valuation_citation": FL_B, "valuation_asof": CHECK},
             stage="Series A", stage_src="web_verified", stage_cite=FL_A, stage_conf="high", entry_date="2021-11-03",
             country="CA", country_src="web_verified", country_cite=FL_B, city="Toronto", focus="Fintech & Payments",
             note="Float Financial, corporate cards and spend management, Toronto. Tiger led the C$37M Series A of "
                  "November 2021 (BetaKit; the Globe and Mail): the firm's entry. Goldman Sachs led the C$70M Series "
                  "B in January 2025 (BetaKit) at an undisclosed valuation; momentum check " + CHECK + ": no priced "
                  "round at $1B or more. The Point Nine and Y Combinator rows named Float are other companies.",
             rounds=[rnd("2021-11-03", "Series A", None, "Tiger Global", True, FL_A, "press"),
                     rnd("2025-01-13", "Series B", None, "Goldman Sachs", None, FL_B, "press")]))

# ---------------------------------------------------------------- flock-safety (recall seed confirmed)
FS_E = PK("flock-safety", "", "recall")
fs_usd, fs_asof, fs_cite = SIB("flock-safety", "coatue")
L.append(cls("flock-safety", status="private", rng="1b_plus", usd=fs_usd, val_src="web_verified", val_cite=fs_cite,
             asof="2025-03", extra=WV,
             stage="Growth", stage_src="web_verified", stage_cite=FS_E, stage_conf="high", entry_date="2022-02-15",
             country="US", city="Atlanta", focus="Security",
             note="Licence-plate cameras and public-safety software, Atlanta. Tiger led the $150M Series E of "
                  "February 2022 (the company's post): Growth. Last priced round: $275M led by a16z at $7.5B "
                  "(March 2025), aligned with the Coatue, Spark and Y Combinator rows; Fortune's 2026 '$8 billion' "
                  "is not a priced round, and a possible sale was only reported (Semafor, 2026-09).",
             rounds=[rnd("2022-02-15", "Series E", 150_000_000, "Tiger Global", True, FS_E, "company")]))

# ---------------------------------------------------------------- flutterwave (recall seed confirmed)
FW_C = SIBREC("insight-partners", "flutterwave", "entry_stage_citation")
fw_usd, fw_asof, fw_cite = SIB("flutterwave", "headline")
L.append(cls("flutterwave", status="private", rng="1b_plus", usd=fw_usd, val_src="web_verified", val_cite=fw_cite,
             asof=fw_asof, extra=WV, clear=["needs_web_value"],
             stage="Growth", stage_src="web_verified", stage_cite=FW_C, stage_conf="high", entry_date="2021-03-09",
             country="US", city="San Francisco", focus="Fintech & Payments",
             note="African payments infrastructure, San Francisco and Lagos. Avenir Growth and Tiger Global led the "
                  "$170M Series C of March 2021 at over $1B (TechCrunch): Tiger's entry, Growth. B Capital led the "
                  "$250M Series D at over $3B (February 2022); the Series E of June 2026 at $3.2B (FinTech Futures) "
                  "is the mark the sibling rows carry. HQ San Francisco as the General Catalyst, Headline and Insight "
                  "rows read (the Lux and Y Combinator rows read Lagos).",
             rounds=[rnd("2021-03-09", "Series C", 170_000_000, "Avenir Growth, Tiger Global", True, FW_C, "press"),
                     rnd("2026-06-17", "Series E", None, None, None, fw_cite, "press")]))

L.append(verdict("focus-media-holding-ltd", "not_member",
                 T3 + ": Focus Media listed on Nasdaq in July 2005 and Tiger's 13G filings date from 2006-2007; no "
                      "prospectus names a Tiger vehicle", ec="fund_filing", conf="high",
                 cite=SEC("focus-media-holding-ltd", "edgar")))

# ---------------------------------------------------------------- fort-robotics (recall seed confirmed)
FR_8K = PK("fort-robotics", "Newbury Street II merger", "sec")
FR_SPAC = NEWS("fort-robotics", "To Go Public At $556.6 Million Enterprise Value")
L.append(cls("fort-robotics", status="private", rng="below_1b",
             stage="undetermined",
             country="US", city="Philadelphia", focus="Industrial & Robotics",
             note="Safety and control platform for robots and autonomous machines, Philadelphia. Tiger took part in "
                  "the $25M Series B of July 2022 with Prologis (Inquirer, The Robot Report headlines) and is named "
                  "an existing investor in the August 2026 SPAC merger filing, where it also commits to the PIPE "
                  "(not a venture entry, D6). Whether Tiger entered at that Series B or earlier is not on record, so "
                  "the stage is undetermined. The signed merger with Newbury Street II (implied pro forma enterprise "
                  "value $556.6M, Pulse 2.0) has not closed: private, below $1B.",
             rounds=[rnd("2022-07-12", "Series B", 25_000_000, None, True, None, "press"),
                     rnd("2026-08-18", "SPAC merger agreement (PIPE commitment)", None, None, True, FR_8K, "filing")]))

# ---------------------------------------------------------------- forter (membership open)
FO_SA = PK("forter", "SiliconANGLE | E-commerce fraud prevention startup Forter raises")
FO_R = PK("forter", "Reuters | Forter valued at $3 bln")
L.append(verdict("forter", "member",
                 "SiliconANGLE (2021-05-25): 'The Series F round was led by Tiger Global Management', the $300M "
                 "private round at $3B; Retail Dive quotes Tiger partner John Curtius", ec="web", conf="high",
                 cite=FO_SA))
L.append(cls("forter", status="private", rng="1b_plus", usd=3_000_000_000, val_src="web_verified", val_cite=FO_R,
             asof="2021-05-25", extra=WV, flags=["stale"], clear=["needs_web_value"],
             stage="Growth", stage_src="web_verified", stage_cite=FO_SA, stage_conf="high", entry_date="2021-05-25",
             city="New York", focus="Security",
             note="E-commerce fraud prevention, New York. Tiger led the $300M Series F at $3B (May 2021, Reuters); "
                  "the $125M Series E of November 2020 at $1.3B was not Tiger's: Growth. No later priced round found; "
                  "the 2021 mark stands, stale.",
             rounds=[rnd("2021-05-25", "Series F", 300_000_000, "Tiger Global Management", True, FO_SA, "press")]))

# ---------------------------------------------------------------- freight-tiger (recall seed replaced)
L.append(verdict("freight-tiger", "not_member",
                 "The recall headline is Business Standard's report that Tata Motors will buy 26.79% of Freight Tiger "
                 "for Rs 150 crore (2023-10-19); 'Tiger' is the company's own name, and no record ties Tiger Global "
                 "to a round of the company", ec="web", conf="high", cite=PK("freight-tiger", "", "recall")))

# ---------------------------------------------------------------- freshworks-inc (membership open)
FW_IRA = PK("freshworks-inc", "PIP VI Holdings", "sec")
FW_B = BN("freshdesk", "Freshdesk Raises $5M In Second Round")
fr_usd, fr_asof, fr_cite = SIB("freshworks-inc", "accel")
L.append(verdict("freshworks-inc", "member",
                 "Freshworks' IPO draft registration exhibit: Tiger Global PIP VI Holdings and Internet Fund II and "
                 "III sign the Series H investors' rights agreement; VCCircle (2012-04-26): 'Freshdesk Raises $5M In "
                 "Second Round Of Funding Led By Tiger Global'; Lee Fixel sits as director on the Form Ds 2013-2018",
                 ec="fund_filing", conf="high", cite=FW_IRA))
L.append(cls("freshworks-inc", rng="1b_plus", usd=fr_usd, val_src="web_verified", val_cite=fr_cite,
             asof="2026-08-31", extra=WV, flags=["model_disputes_source"],
             stage="Growth", stage_src="web_verified", stage_cite=FW_B, stage_conf="high", entry_date="2012-04",
             city="San Mateo", focus="SaaS",
             note="Customer service and IT software (Freshdesk until 2017), San Mateo with its product organisation "
                  "in Chennai; Nasdaq: FRSH since September 2021. Tiger led the $5M second round of April 2012, six "
                  "months after Accel's $1M Series A (VCCircle), i.e. the Series B: Growth; the pre-filled entry date "
                  "2013-11-14 was the Form D anchor of the later $7M Series C, corrected to 2012-04. Tiger led the $50M "
                  "Series E of 2015. Market cap replaces the SEC float: $3.63B (2026-08-31), as the Accel row reads.",
             rounds=[rnd("2012-04-26", "Series B (second round)", 5_000_000, "Tiger Global", True, FW_B, "press")]))

if __name__ == "__main__":
    jl.write("batch-005c", L, record=os.environ.get("DRY") != "1")
