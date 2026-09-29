#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 7, chunk b (rows 16-30). Run: NQ_TAG=b7 python3 judgments-7b.py"""
import json
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, SEC, W

INV = HERE.parent


def U(slug, sub, host=None):
    """The one publisher URL on disk (news-extra*.json) whose headline contains `sub`."""
    items = []
    for f in sorted(HERE.glob("news-extra*.json")):
        items += json.loads(f.read_text()).get(slug, [])
    urls = list(dict.fromkeys(i["url"] for i in items if i.get("url") and sub.lower() in i["title"].lower()
                              and (host is None or host in i["url"])))
    if len(urls) != 1:
        raise SystemExit(f"U({slug!r}, {sub!r}, {host!r}) matched {len(urls)}: {urls[:4]}")
    return urls[0]


def LED(slug):
    v = json.loads((INV / "companies/membership-ledger.json").read_text())["tiger-global-management"]["verdicts"]
    c = (v.get(slug) or {}).get("citation")
    if not c:
        raise SystemExit(f"LED({slug!r}): no seed citation")
    return c


WV = {"valuation_range_source": "web_verified"}
CLR = ("needs_web_value", "unicorn_name_match")
L = []

# ---- inshorts
ins = LED("inshorts")
L.append(cls("inshorts", status="private", rng="below_1b", stage="undetermined",
             country="IN", country_src="web_verified", country_cite=ins, city="Noida",
             focus="Media, Gaming & Advertising",
             rounds=[rnd("2015-07-09", None, 20_000_000, "Tiger Global", True, None, "press"),
                     rnd("2017-12-07", "bridge", 5_000_000, "Tiger Global", True,
                         U("inshorts", "Content Discovery Startup Inshorts Raises $5 Mn Funding From Tiger Global"), "press"),
                     rnd("2021-07-16", None, 60_000_000, "Vy Capital", None,
                         U("inshorts", "Inshorts raises $60 million in funding led by Vy Capital"), "press")],
             note="Short-news app (Noida), formerly News in Shorts. Tiger was an investor by 2015: Techcircle's Jul 2015 "
                  "headline says it 'secures $20M more from Tiger Global', so Tiger's first round came earlier and no "
                  "source read names it (Bing, 2026-09-29: none): stage undetermined. The Dec 2017 $5M bridge came from "
                  "'existing investor Tiger Global' through its Singapore vehicle Internet Fund III Pte (inc42), a "
                  "home-desk vehicle. Vy Capital led a $60M round in 2021; no $1B mark."))

# ---- intel: a listed-stock purchase, not a private round
L.append(verdict("intel", "not_member",
                 "13G/13F position in a listed company, no private round naming the firm (T3, D3): the recall "
                 "headline reports Tiger buying listed Intel stock in 2026, and the adviser's 13F lists Intel from "
                 "2001 on; Intel has been public since 1971", ec="web", conf="high", cite=LED("intel")))

# ---- intellect
it = U("intellect", "Raises $10 Million In Funding Round Led By Tiger Global", "forbes.com")
L.append(cls("intellect", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=it, stage_conf="medium", entry_date="2022-07-11",
             country="SG", country_src="web_verified", country_cite=it, city="Singapore", focus="Healthcare & Bio",
             rounds=[rnd("2022-07-11", "Series A extension (A+)", 10_000_000, "Tiger Global", True, it, "press")],
             note="Mental-health care platform for Asia (Singapore; the pre-filled GB is a wrong join). Tiger led the "
                  "$10M extension of the Series A in Jul 2022 (Business Times: 'extended round'; 36Kr: A+ round), its "
                  "first money in the company; an extension of the A is read as Series A. Private, below $1B as in the "
                  "Headline and Y Combinator rows."))

# ---- intercept-inc (seeded ec=filing): listed-company 13G
L.append(verdict("intercept-inc", "not_member",
                 "13G/13F position in a listed company, no private round naming the firm (T3, D3): InterCept "
                 "(Norcross, Georgia) listed in 1998; the adviser's 13G filings date from 2003 and 2004",
                 ec="fund_filing", conf="high", cite=SEC("intercept-inc", "edgar")))

# ---- interviewbit
ib = U("interviewbit", "Sequoia, Tiger Global invest in InterviewBit", "livemint.com")
L.append(cls("interviewbit", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=ib, stage_conf="high", entry_date="2020-01-28",
             country="IN", country_src="web_verified", country_cite=ib, city="Bangalore",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2020-01-28", "Series A", 20_000_000, "Tiger Global and Sequoia India", True, ib, "press")],
             note="Tech upskilling (InterviewBit and Scaler), Bengaluru. Tiger and Sequoia India led the $20M Series A "
                  "of Jan 2020 (Mint; valued about $110M per ThePrint); the earlier money was Sequoia's Surge programme. "
                  "No $1B mark."))

# ---- invideo
iv = U("invideo", "InVideo raises $15 million from Sequoia, Tiger Global")
L.append(cls("invideo", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=iv, stage_conf="high", entry_date="2020-10-27",
             country="IN", country_src="web_verified",
             country_cite=U("invideo", "Video creation and editing platform InVideo raises $15 million"),
             city="Mumbai", focus="AI & Applied AI",
             rounds=[rnd("2020-10-27", "Series A", 15_000_000, "Sequoia Capital India", True, iv, "press")],
             note="Video creation, now generative-AI video (Mumbai-founded, TechCrunch 2020; it also runs a US office). "
                  "Tiger joined the $15M Series A of Oct 2020 led by Sequoia India (Moneycontrol: 'from Sequoia, Tiger "
                  "Global and others'); the earlier $2.5M round was Sequoia Surge's. No $1B mark found."))

# ---- invisionapp-inc: Form D director of record in Lee Fixel's Tiger years
L.append(verdict("invisionapp-inc", "member",
                 "Lee Fixel, Tiger partner until early 2019, is director of InVisionApp Inc. (New York) on its Form Ds "
                 "from 2013q4 to 2017q3, inside his Tiger years (D7), and the identity resolves to the design-"
                 "collaboration company InVision; the 2013q4 filing ($11.6M sold) is the round his seat dates from "
                 "(director-of-record pattern)", ec="formd_adjudicated", conf="medium", cite=SEC("invisionapp-inc")))
L.append(cls("invisionapp-inc", status="defunct", rng="below_1b", city="New York", focus="SaaS",
             note="InVision (design prototyping and collaboration, New York). Entry kept at the Form D band's Series A "
                  "(2013q4, $11.6M sold, Lee Fixel's seat from that filing). The company announced in Jan 2024 that "
                  "it would end its services at the end of 2024 and closed: defunct, as in Spark's row."))

# ---- irokotv
L.append(cls("irokotv", status="private", rng="below_1b", stage="undetermined",
             country="NG", country_src="web_verified", country_cite=W("IROKO Partners"), city="Lagos",
             focus="Media, Gaming & Advertising",
             rounds=[rnd("2011", None, None, "Tiger Global", True, W("Irokotv"), "press"),
                     rnd("2012", None, None, "Tiger Global", True, W("Irokotv"), "press"),
                     rnd("2012-07", None, 2_000_000, "Kinnevik", None, W("Irokotv"), "press")],
             note="iROKOtv, Nollywood streaming by iROKO Partners (Lagos, with a London office). Wikipedia: Tiger "
                  "Global 'led a two-round investment totalling US$8 million' in 2011 and 2012, the company's first "
                  "outside money; neither round is named, so the stage is undetermined. Kinnevik led later rounds. No "
                  "shutdown or sale of the company found (Canal+ bought the ROK studio unit in 2019): private."))

# ---- iru (formerly Kandji)
ir = W("Iru (company)")
L.append(cls("iru", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=ir, stage_conf="high", entry_date="2021",
             city="San Diego", focus="Security",
             rounds=[rnd("2021", "Series B", 60_000_000, None, None, ir, "press"),
                     rnd("2021", "Series C", 100_000_000, "Tiger Global", True, ir, "press")],
             note="Iru, formerly Kandji (Apple device management and security, San Diego). Wikipedia: a $60M Series B, "
                  "then a $100M Series C led by Tiger Global in late 2021, Tiger's entry. Private, below $1B as in the "
                  "Felicis, First Round and General Catalyst rows."))

# ---- itilite
il = U("itilite", "Series C to accelerate digital adoption", "prnewswire.com")
L.append(cls("itilite", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=il, stage_conf="high", entry_date="2022-04-13",
             country="IN", country_src="web_verified", country_cite=U("itilite", "India-Based T&E Startup Itilite"),
             city="Bangalore", focus="SaaS",
             rounds=[rnd("2022-04-13", "Series C", 29_000_000, "Tiger Global and Dharana Capital", True, il, "company")],
             note="Business travel and expense software (Bengaluru, with a US office). Tiger co-led the $29M Series C "
                  "of Apr 2022 with Dharana, its first round in the company. No $1B mark."))

# ---- ivalua
iva = U("ivalua", "raises $60 million at a $1 billion valuation")
L.append(cls("ivalua", status="private",
             rng="1b_plus", usd=1_000_000_000, val_src="web_verified", val_cite=iva, asof="2019-05-20",
             stage="Growth", stage_src="web_verified", stage_cite=U("ivalua", "Tiger joins KKR and Ardian"),
             stage_conf="high", entry_date="2019-05-20",
             country="FR", country_src="web_verified", country_cite=U("ivalua", "licornes françaises", "frenchweb"),
             city="Orsay", focus="SaaS", flags=("stale",), clear=CLR, extra=WV,
             rounds=[rnd("2019-05-20", None, 60_000_000, "Tiger Global", True, iva, "press")],
             note="Spend-management software (Orsay, France). Tiger joined KKR and Ardian in the $60M round of May 2019 "
                  "at a $1B valuation (VentureBeat; Le Monde Informatique put it near EUR 900M), its entry, a late round "
                  "into a company KKR had backed in 2017. The mark sits exactly on the band edge and is stale; no later "
                  "priced round found (the company calls itself a profitable unicorn, 2023)."))

# ---- ivi
L.append(cls("ivi", status="private", rng="below_1b", stage="undetermined",
             country="RU", country_src="web_verified", country_cite=W("Ivi.ru"), city="Moscow",
             focus="Media, Gaming & Advertising",
             rounds=[rnd("2011", None, None, "Tiger Global", True, W("Ivi.ru"), "press"),
                     rnd("2012", None, 40_000_000, "Baring Vostok", True, W("Ivi.ru"), "press"),
                     rnd("2021", None, 250_000_000, None, None, W("Ivi.ru"), "press")],
             note="ivi, Russian video-streaming service (Moscow). Wikipedia: 'In 2011, ivi.ru secured additional "
                  "funding from ... Tiger Global Management', a round it does not name (stage undetermined); Tiger was "
                  "still a holder in Baring Vostok's $40M round of 2012 and in 2022 (Business Insider). The 2021 $250M "
                  "round's valuation was not found, so no $1B mark."))

# ---- jabu
jb = LED("jabu")
L.append(cls("jabu", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=jb, stage_conf="high", entry_date="2022-05-25",
             country="ZA", country_src="web_verified",
             country_cite=U("jabu", "South Africa’s JABU Gets $3.2M"), city="Cape Town",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2021", "Seed", 3_200_000, None, None,
                         U("jabu", "YC-backed Namibian startup JABU gets $3.2M", "techcrunch.com"), "press"),
                     rnd("2022-05-25", "Series A", 15_000_000, "Tiger Global", True, jb, "press")],
             note="B2B e-commerce and distribution for small retailers in Namibia and South Africa. The $3.2M seed "
                  "(2021) had no Tiger; Tiger led the $15M Series A of May 2022. Country and city aligned with the Y "
                  "Combinator row (Cape Town, ZA; PYMNTS calls it South African), though ITWeb in 2022 put the head "
                  "office in Windhoek, Namibia."))

# ---- jambo
jm = U("jambo", "Paradigm Enters Africa With $30M Round", "finance.yahoo.com")
L.append(cls("jambo", status="private", rng="below_1b", stage="undetermined",
             country="CD", country_src="web_verified", country_cite=jm, flags=("city_unknown",),
             focus="Crypto & Web3",
             rounds=[rnd("2022-05-10", "Series A", 30_000_000, "Paradigm", None, jm, "press")],
             note="Jambo, web3 super-app for Africa ('a Congo-based startup', CoinDesk). Membership rests on the "
                  "Sharps Technology 8-K bio naming Tiger among the investors of its $40M+; the $30M Series A of May "
                  "2022 was Paradigm-led with Pantera, Delphi, Kingsway and Gemini named, Tiger not, and the seed's "
                  "investors were not found: Tiger's round is not established, stage undetermined. No city found."))

# ---- jar
jr = LED("jar")
L.append(cls("jar", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=jr, stage_conf="high", entry_date="2022-02-03",
             country="IN", country_src="web_verified",
             country_cite=U("jar", "Digital gold savings app Jar registers 9X rise"), city="Bangalore",
             focus="Fintech & Payments",
             rounds=[rnd("2022-02-03", "Series A", 32_000_000, "Tiger Global", True, jr, "press"),
                     rnd("2022-08-18", "Series B", 22_600_000, "Tiger Global", True,
                         U("jar", "Tiger Global leads Series B funding round in fintech startup Jar"), "press")],
             note="Gold savings app (Bengaluru). Tiger led the $32M Series A of Feb 2022 at about $200M and the $22.6M "
                  "Series B of Aug 2022 at $300M. Momentum check 2026-09-29 (Bing): no later priced round found, the "
                  "newest item being the FY25 results (YourStory, Sep 2025)."))

if __name__ == "__main__":
    jl.write("batch-007b", L)
