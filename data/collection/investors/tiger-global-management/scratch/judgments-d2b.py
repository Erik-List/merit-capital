#!/usr/bin/env python3
"""PRO-167 Tiger Global, delta queue batch 2 (after the one rebuild), chunk b: Upstream to Yotpo (9 rows).
Evidence: show.py --batch 2, the evidence pack's press and SEC lines, Bing News (bq.py, NQ_TAG=d2), Wikipedia on disk
and Russian Wikipedia (WebFetch), WebFetch of press pages (VentureBeat, Yahoo Finance, Pulse 2.0, Kommersant) and of
VTEX's F-1 cover page.
Run: NQ_TAG=d2 python3 judgments-d2b.py"""
import json
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, W, NEWS

HERE = Path(__file__).resolve().parent
PKD = json.loads((HERE / "evidence-pack.json").read_text())
CLS_ON_DISK = json.loads((HERE.parent / "companies" / "classification.json").read_text())
WV = {"valuation_range_source": "web_verified"}
PINNED = ("needs_web_value", "unicorn_name_match")


def PK(slug, kind, sub):
    """The URL on the row's evidence-view line of `kind` ('sec' or 'press') that contains `sub`."""
    urls = []
    for x in (PKD.get(slug, {}).get(kind) or []):
        if sub.lower() not in x.lower():
            continue
        if kind == "sec":
            u = x.rsplit(" | ", 1)[-1].strip()
        else:
            m = re.search(r"\|\| URL (\S+)", x)
            u = m.group(1) if m else ""
        if u.startswith("http"):
            urls.append(u)
    urls = list(dict.fromkeys(urls))
    if len(urls) != 1:
        raise SystemExit(f"PK({slug!r}, {kind!r}, {sub!r}) matched {len(urls)}")
    return urls[0]


def BURL(slug, title_sub, url_sub=""):
    """The one publisher URL among the row's cached news items (news-extra*.json) whose title contains
    `title_sub` and whose URL contains `url_sub`."""
    items = []
    for f in sorted(HERE.glob("news-extra*.json")):
        items += json.loads(f.read_text()).get(slug, [])
    us = list(dict.fromkeys(i["url"] for i in items if i.get("url") and not i.get("gid")
                            and title_sub.lower() in i["title"].lower() and url_sub in i["url"]))
    if len(us) != 1:
        raise SystemExit(f"BURL({slug!r}, {title_sub!r}, {url_sub!r}) matched {len(us)}")
    return us[0]


def ONDISK(slug, key):
    """A key of this book's classification record for the row, read from disk."""
    v = (CLS_ON_DISK.get(slug) or {}).get(key)
    if not v:
        raise SystemExit(f"ONDISK({slug!r}, {key!r}) missing")
    return v


L = []

# ---------------------------------------------------------------- Upstream (wave-2 recall addition)
UP_A = PK("upstream", "press", "Business Insider")
UP_BW = BURL("upstream", "Upstream Raises $12.5M Series A", "businesswire")
L.append(verdict("upstream", "member",
    "Business Insider (2022-03-18): 'Tiger Global, which has lately been investing heavily in early stage startups, "
    "invested in Upstream's Series A'",
    ec="web", conf="high", cite=UP_A))
L.append(cls("upstream", status="unknown", rng="below_1b", stage="Series A", stage_src="web_verified",
    stage_cite=UP_A, stage_conf="high", entry_date="2022-03", country="US", city="Miami", city_src="web_verified",
    focus="Crypto & Web3",
    note="No-code platform for starting and running DAOs ('DAO-in-a-box'), founded by Alex Taub and Michael "
         "Schonfeld; its March 2022 release is datelined Miami (Business Wire). Tiger Global invested in the $12.5M "
         "Series A of 2022-03-08, led by the existing investor boldstart ventures (Business Wire; Business Insider); "
         "no earlier round on record names the firm, so the entry is the Series A. No report of the company after "
         "TechCrunch Live of November 2022 (Bing News, 2026-09-29), so its state could not be established: unknown. "
         "The sibling rows named Upstream are different companies (Coatue's UpStream, a Greensboro healthcare "
         "company; YC's Upstream, a Paris SaaS startup): name collisions, not aligned.",
    rounds=[rnd("2022-03-08", "Series A", 12_500_000, "boldstart ventures", True, UP_BW, "company")]))

# ---------------------------------------------------------------- VAST Data (wave-2 recall addition)
VD_REC = PK("vast-data", "press", "Business Insider")
VD_D = PK("vast-data", "press", "AlleyWatch")
VD_E = PK("vast-data", "press", "TechCrunch")
VD_F = BURL("vast-data", "VAST Data: $30 Billion Valuation", "pulse2.com")
L.append(verdict("vast-data", "member",
    "Business Insider (2021-05-05): VAST 'has raised $83 million in Series D funding, led by Tiger Global "
    "Management'; AlleyWatch: 'This round was led by a new investor, Tiger Global'",
    ec="web", conf="high", cite=VD_REC))
L.append(cls("vast-data", status="private", rng="10b_plus", usd=30_000_000_000, val_src="web_verified",
    val_cite=VD_F, asof="2026-04-22", stage="Growth", stage_src="web_verified", stage_cite=VD_D, stage_conf="high",
    entry_date="2021-05", country="US", city="New York", city_src="web_verified", focus="Data Infrastructure",
    clear=PINNED,
    note="New York-based data storage and AI data platform (TechCrunch). Tiger Global, a new investor, led the $83M "
         "Series D of May 2021 at a $3.7B valuation (AlleyWatch; Business Insider), so the entry is Growth; it "
         "joined the $118M Series E led by Fidelity in December 2023 (TechCrunch). Mark: the $1B Series F closed in "
         "April 2026 at a $30B valuation, led by Drive Capital and Access Industries (Pulse 2.0), which is also the "
         "momentum check (data infrastructure, first seen 2021).",
    rounds=[rnd("2021-05", "Series D", 83_000_000, "Tiger Global", True, VD_D, "press"),
            rnd("2023-12-06", "Series E", 118_000_000, "Fidelity", True, VD_E, "press"),
            rnd("2026-04-22", "Series F", 1_000_000_000, "Drive Capital; Access Industries", None, VD_F, "press")],
    extra=WV))

# ---------------------------------------------------------------- Vecmocon Technologies (S2A only)
VM_SEED = ONDISK("vecmocon-technologies", "entry_stage_citation")
VM_A1 = BURL("vecmocon-technologies", "Vecmocon Pockets $10 Mn", "inc42.com")
VM_A2 = BURL("vecmocon-technologies", "Vecmocon closes $18M in Series A", "yourstory")
L.append(cls("vecmocon-technologies", grad="graduated", grad_src="web_verified", grad_cite=VM_A1, grad_conf="high",
    grad_asof="2024-11-15",
    rounds=[rnd("2022-10", "Pre-Series A", 5_200_000, "Tiger Global; Blume Ventures", True, VM_SEED, "press"),
            rnd("2024-11-15", "Series A (first close)", 10_000_000,
                "Ecosystem Integrity Fund; British International Investment", None, VM_A1, "press"),
            rnd("2025-06-09", "Series A (closed at $18M)", 18_000_000, "Ecosystem Integrity Fund; Aavishkaar Capital",
                None, VM_A2, "press")],
    note="S2A graduated: after the $5.2M round Tiger and Blume led in October 2022, Vecmocon raised $10M in the "
         "first close of its Series A in November 2024, led by Ecosystem Integrity Fund and British International "
         "Investment (Inc42), and closed the Series A at $18M in June 2025 (YourStory)."))

# ---------------------------------------------------------------- Vendr (wave-2 recall addition)
VE_A = PK("vendr", "press", "Financial Post")
VE_B = BURL("vendr", "Vendr Raises $150MM Series B", "01net")
VE_X = BURL("vendr", "Vertice acquires Vendr", "prnewswire.com")
L.append(verdict("vendr", "member",
    "Vendr's release (Business Wire via Financial Post, 2021-03-08): 'a $60 million Series A led by Tiger Global "
    "Management, with participation from existing investors Craft Ventures, Y Combinator'",
    ec="web", conf="high", cite=VE_A))
L.append(cls("vendr", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified",
    stage_cite=VE_A, stage_conf="high", entry_date="2021-03", country="US", city="Boston", city_src="web_verified",
    focus="SaaS",
    note="Boston SaaS-buying and software-pricing company (release datelines; YC Summer 2019). Tiger Global led the "
         "$60M Series A of March 2021 as a new investor beside the existing Craft Ventures, Y Combinator, Sound "
         "Ventures, Garage Capital and F-Prime (its release), so the entry is the Series A; a $150M Series B "
         "followed in June 2022. Vertice, the London AI procurement platform, announced its acquisition of Vendr "
         "on 2026-06-01 (PR Newswire; The Next Web: 'Vertice has bought Vendr'): acquired, aligned with the Y "
         "Combinator row.",
    rounds=[rnd("2021-03-08", "Series A", 60_000_000, "Tiger Global", True, VE_A, "company"),
            rnd("2022-06-16", "Series B", 150_000_000, None, None, VE_B, "company"),
            rnd("2026-06-01", "Acquisition by Vertice", None, "Vertice", False, VE_X, "company")]))

# ---------------------------------------------------------------- Vercel (wave-2 recall addition)
VC_C = BURL("vercel", "Vercel secures $102M", "venturebeat.com")
VC_D = BURL("vercel", "Vercel raises $150M Series D", "yahoo.com")
VC_E = PK("vercel", "press", "contxto")
VC_F = PK("vercel", "press", "Series F at $9.3B")
VC_S = BURL("vercel", "Vercel discloses breach", "siliconangle")
L.append(verdict("vercel", "member",
    "VentureBeat (2021-06-22) on the $102M Series C led by Bedrock Capital: 'Accel, CRV, Geodesic Capital, "
    "Greenoaks Capital, GV, 8VC, Flex Capital, GGV, Latacora, Salesforce Ventures, and Tiger Global also "
    "participated'; the Series D report (Yahoo Finance, November 2021) and contxto's Series E report (May 2024) "
    "name Tiger Global among the existing investors",
    ec="web", conf="high", cite=VC_C))
L.append(cls("vercel", status="private", rng="1b_plus", usd=9_300_000_000, val_src="web_verified",
    val_cite=VC_F, asof="2025-09-30", stage="Growth", stage_src="web_verified", stage_cite=VC_C, stage_conf="high",
    entry_date="2021-06", country="US", city="San Francisco", focus="DevTools & APIs", clear=PINNED,
    note="Frontend cloud and Next.js company, San Francisco. Tiger Global entered in the $102M Series C of June 2021 "
         "led by Bedrock Capital, at a valuation above $1B (VentureBeat), and is named an existing investor in the "
         "$150M Series D of November 2021 led by GGV at $2.5B (Yahoo Finance) and in the $250M "
         "Series E of May 2024 led by Accel (contxto, whose other sentence listing Tiger among 'new participants' "
         "repeats the Series C list); the row's first_seen of 2024 is that report, not the entry. Entry Growth. "
         "Mark: the Series F of September 2025 at $9.3B (Business Wire); momentum check (developer tools): "
         "SiliconANGLE on 2026-04-20 still cites the $9.3B and Bing News shows no later priced round. Aligned "
         "with the sibling rows on the $9.3B mark and with the 8VC, Coatue, General Catalyst, GV and IVP rows on "
         "San Francisco (Accel's Covina reads like the mailing address the company files from).",
    rounds=[rnd("2021-06-23", "Series C", 102_000_000, "Bedrock Capital", True, VC_C, "press"),
            rnd("2021-11-23", "Series D", 150_000_000, "GGV Capital", True, VC_D, "press"),
            rnd("2024-05-16", "Series E", 250_000_000, "Accel", True, VC_E, "press"),
            rnd("2025-09-30", "Series F", 300_000_000, None, None, W("Vercel"), "press")],
    extra=WV))

# ---------------------------------------------------------------- Viam (wave-2 recall addition)
VI_A = PK("viam", "press", "Robot Report")
VI_C = BURL("viam", "Viam announces a $30 Million Series C", "yahoo.com")
L.append(verdict("viam", "member",
    "The Robot Report (2022-02-11): 'Viam Robotics announced the close of a $30 million Series A round led by Tiger "
    "Global, with participation from returning investor Union Square Ventures, and Battery Ventures'",
    ec="web", conf="high", cite=VI_A))
L.append(cls("viam", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_cite=VI_A,
    stage_conf="high", entry_date="2022-02", country="US", city="New York", city_src="web_verified",
    focus="Industrial & Robotics",
    note="New York software platform for robotics and smart machines, founded by MongoDB cofounder Eliot Horowitz "
         "(its 2025 release is datelined New York). Tiger Global led the $30M Series A of February 2022 (The Robot "
         "Report), after the seed Union Square Ventures had backed, so the entry is the Series A. Latest round: the "
         "$30M Series C of March 2025 led by Union Square Ventures, at no disclosed valuation (Viam's release); no "
         "priced round at $1B or more on record (Bing News, 2026-09-29). Aligned with the Battery and USV rows.",
    rounds=[rnd("2022-02-11", "Series A", 30_000_000, "Tiger Global", True, VI_A, "press"),
            rnd("2025-03-03", "Series C", 30_000_000, "Union Square Ventures", None, VI_C, "company")]))

# ---------------------------------------------------------------- VTEX (ec=filing: re-rule; hq_country claim)
VT_F1 = PK("vtex", "sec", "VTEX")
L.append(verdict("vtex", "member",
    "VTEX's 2021 F-1 lists common shares held by Tiger Global Private Investment Partners XII, L.P. and other Tiger "
    "affiliates before the July 2021 IPO: a PIP vehicle's private position (the SC 13G filings of 2021 and 2022 are "
    "the later listed holding)",
    ec="fund_filing", conf="high", cite=VT_F1))
L.append(cls("vtex", country="BR", country_src="web_verified", country_cite=NEWS("vtex", "VTEX já vale US"),
    note="Country BR confirmed from the company's own evidence: the F-1 says VTEX was founded in Brazil, where it "
         "grew its business (Brazil Journal calls it the new Brazilian unicorn, September 2020); the F-1 "
         "gives its principal executive offices as 125 Kingsway, London, and the parent is registered in the Cayman "
         "Islands (a filing haven), neither of which is where the company operates."))

# ---------------------------------------------------------------- Wikimart (wave-2 recall addition)
WM_T = PK("wikimart", "press", "Tech.eu")
WM_K = PK("wikimart", "press", "Kommersant")
WM_V = PK("wikimart", "press", "vedomosti")
WM_X = PK("wikimart", "press", "Topnews")
WM_R = BURL("wikimart", "Финпромбанка", "roem.ru")
L.append(verdict("wikimart", "member",
    "Tech.eu (2017-07-11): Wikimart 'was heavily funded by Western investors, with Tiger Global Management, "
    "investing some $30 million in total in 2010, 2011 and 2012'; Kommersant (2012-03-13): Tiger put $18M into the "
    "$30M round of March 2012 after $12M of the $13.2M the company had raised before. The entry is the company's "
    "first outside round (Russian Wikipedia: about $5M, late 2009), a financing of an 18-month-old startup; Tiger "
    "held about 55% after the 2012 round, so the control question is flagged for Erik in the note",
    ec="web", conf="medium", cite=WM_T))
L.append(cls("wikimart", status="defunct", rng="below_1b", stage="undetermined", country="RU",
    country_src="web_verified", country_cite=WM_V, city="Moscow", focus="Consumer & Marketplaces",
    note="Moscow online marketplace launched in June 2008. Tiger Global was its main outside investor: about $5M in "
         "late 2009 (Russian Wikipedia), $12M of the $13.2M raised by spring 2011, and $18M of a $30M round in "
         "March 2012 (Kommersant), after which it held about 55% (founders 23%); none of these rounds is named, so "
         "the stage is undetermined. FOR ERIK: Tiger became the majority owner through these financings (the 2012 "
         "stake, and 'more than 50%' sold to Finprombank's shareholders in October 2014, roem.ru), but the first "
         "cheque was a startup's first institutional round and no record says it gave control, so the row is kept a "
         "member under T3 rather than excluded as a control position; a ruling may move it. Tiger stopped funding "
         "after the 2014 sanctions (Tech.eu); the company stopped operating in December 2016 (Topnews) and went "
         "bankrupt: defunct.",
    rounds=[rnd("2010", "First outside round (not named)", None, "Tiger Global", True, WM_T, "press"),
            rnd("2011", "Follow-on (not named); $12M of $13.2M raised came from Tiger", None, "Tiger Global", True,
                WM_K, "press"),
            rnd("2012-03", "Round of $30M (not named)", 30_000_000, "Tiger Global", True, WM_K, "press"),
            rnd("2014-10", "Controlling stake sold to Finprombank's shareholders", None, None, False, WM_R, "press")]))

# ---------------------------------------------------------------- Yotpo (wave-2 recall addition)
YO_F = PK("yotpo", "press", "calcalistech")
L.append(verdict("yotpo", "member",
    "Calcalist (2021-03-18): Yotpo's $230M Series F 'was led by Bessemer Venture Partners and Tiger Global, with "
    "participation from existing investors Claltech Investment, Coin Ventures, Hanaco, Vertex Ventures, and Vintage "
    "Investment Partners'",
    ec="web", conf="high", cite=YO_F))
L.append(cls("yotpo", status="private", rng="1b_plus", usd=1_400_000_000, val_src="web_verified", val_cite=YO_F,
    asof="2021-03-18", stage="Growth", stage_src="web_verified", stage_cite=YO_F, stage_conf="high",
    entry_date="2021-03", country="IL", country_src="web_verified", country_cite=YO_F, city="Tel Aviv",
    city_src="web_verified", focus="SaaS", flags=("stale",), clear=PINNED,
    note="E-commerce marketing software (reviews, loyalty, SMS); Calcalist calls it 'Tel Aviv-based marketing service "
         "Yotpo Inc.', which confirms the IL claim. Bessemer and Tiger Global led the $230M Series F of March "
         "2021 at $1.4B, with the existing investors named apart and after the $75M Series E of August 2020 "
         "(Calcalist), so the entry is Growth. Mark $1.4B (2021-03), stale; Shopify's strategic investment of September 2021 carried no price, "
         "and Bing News (2026-09-29) shows no later priced round or documented collapse.",
    rounds=[rnd("2020-08", "Series E", 75_000_000, None, False, YO_F, "press"),
            rnd("2021-03-18", "Series F", 230_000_000, "Bessemer Venture Partners; Tiger Global", True, YO_F, "press")],
    extra=WV))

if __name__ == "__main__":
    jl.write("delta-002b", L)
