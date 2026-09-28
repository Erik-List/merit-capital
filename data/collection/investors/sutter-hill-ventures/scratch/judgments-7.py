#!/usr/bin/env python3
"""Batch 7 of the Sutter Hill Ventures grind (PRO-77): 31 Form D-only rows, membership first.

Run: NQ_TAG=b7 python3 judgments-7.py   (DRY=1 writes the .out.jsonl without recording)

Every citation comes from a helper (SEC, NEWS, ARCH, FORMD_CITE) or is a URL printed by a
tool run in this session (WebSearch results, the Spark and USV sibling rows, a Wayback
redirect header).
"""
import os
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, ARCH, NEWS, SEC

N = 7
L = []
FD = "formd_adjudicated"

# ---- URLs printed by tools in this session
TELSAR_FIERCE = "https://www.fiercebiotech.com/biotech/astellas-and-drais-partner-to-develop-astellas-compound-through-telsar"
SELDAR_GV = "https://globalventuring.com/blog/2012/06/06/astellas-seals-second-drug-deal-with-drais/"
LACEWORK_B = ("https://www.prnewswire.com/news-releases/lacework-closes-24-million-series-b-financing-with-sutter-hill-"
              "ventures-to-expand-go-to-market-for-game-changing-cloud-security-solution-300703155.html")
LACEWORK_42 = ("https://www.prnewswire.com/news-releases/lacework-closes-42-million-financing-round-and-adds-cloud-"
               "security-leader-andy-byron-as-president-300916884.html")
SIGMA_E = "https://www.sigmacomputing.com/resources/announcements/series-e"
SIGMA_D = "https://www.sigmacomputing.com/resources/announcements/sigma-raises-200-million-in-series-d-funding"
USV_QUIZLET = "https://www.usv.com/writing/2015/11/quizlet/"
NAV_B = ("https://www.prnewswire.com/news-releases/nav-increases-series-b-funding-round-to-38-million-goldman-sachs-"
         "principal-strategic-investments-leads-round-expansion-300450985.html")
SERVIZ_LABJ = "https://labusinessjournal.com/technology/serviz-fixes-125-million/"
VIGLINK = "https://web.archive.org/web/20141217125016id_/http://www.viglink.com/linksmart/"
SAVANNA_VENDOR = "https://www.crunchbase.com/organization/savanna-biotherapeutics"

# ---- news citations (decoded from the rows' Google News items)
KUMU_SE = NEWS("kumu-networks-inc", "Full Duplex on One Channel")
PROC_D = NEWS("procyrion-inc", "closes $30 million round")
LL_VB = NEWS("laserlike-inc", "Another Move to Shore Up Siri")
LUM_PR = NEWS("luminary-cloud-inc", "Emerges from Stealth, Empowering")
LUM_SA = NEWS("luminary-cloud-inc", "raises $72M")
OBS_2020 = NEWS("observe-inc", "Observe Inc Emerges From Stealth")
OBS_B = NEWS("observe-inc", "Announces $115 Million In Series B")
OBS_TC = NEWS("observe-inc", "secures $70M")
OBS_TFN = NEWS("observe-inc", "raises $145M")
LW_SA = NEWS("lacework-inc", "raises massive $525M")
LW_CRN = NEWS("lacework-inc", "Raises $1.3B On $8.3B")
SIGMA_C = NEWS("sigma-computing-inc", "Announces $300M Series C")
SIGMA_VB = NEWS("sigma-computing-inc", "raises $30 million more")
NEYE_CB = NEWS("neye-systems-inc", "citybiz")
NEYE_RT = NEWS("neye-systems-inc", "led by Alphabet")
NEYE_P2 = NEWS("neye-systems-inc", "72.5 Million Raised")

HOMONYM_TAIL = ("not SHV's James N. White of 755 Page Mill Road: a homonym. No SHV listing, SHV filing or "
                "documented round names the company.")

# =====================================================================================
# James White cluster: SHV's Jim White is James N. White (roster 2001 to 2017, Palo Alto).
# Every White below files from an unrelated address in an operating role.
# =====================================================================================
L.append(verdict("jamba-inc", "not_member",
    "James D. White on Jamba's 2009 Form D is Jamba's own chairman and chief executive (Executive Officer and "
    "Director at Jamba's Emeryville office), not SHV's James N. White of 755 Page Mill Road: a homonym. Jamba was "
    "a public company and the filing is its own 2009 private placement; no SHV listing, SHV filing or documented "
    "round names Jamba.", ec=FD, conf="high", cite=SEC("jamba-inc")))
L.append(verdict("medtest-holdings-inc", "not_member",
    "James White on MedTest Holdings' 2011 and 2012 Form Ds is the company's own executive officer and director at "
    "99 Derby Street, Hingham, Massachusetts, " + HOMONYM_TAIL, ec=FD, conf="high", cite=SEC("medtest-holdings-inc")))
L.append(verdict("newcomlink-inc", "not_member",
    "James S. White on Newcomlink's 2011 to 2013 Form Ds is the company's own executive officer and director in "
    "Austin, Texas, " + HOMONYM_TAIL, ec=FD, conf="high", cite=SEC("newcomlink-inc")))
L.append(verdict("osmetech-plc", "not_member",
    "James Nicholas Gerald White on Osmetech's 2008 and 2009 Form Ds is the company's own executive officer and "
    "director, filing c/o Ashurst in London, not SHV's James N. White of 755 Page Mill Road: a homonym. Osmetech "
    "was an AIM-listed UK diagnostics company; no SHV listing, SHV filing (CIK 879051) or documented round names it.",
    ec=FD, conf="high", cite=SEC("osmetech-plc")))
L.append(verdict("panera-holdings-corp", "not_member",
    "The James White (initial J., G. or none across the filings) on Panera Holdings' 2017 to 2020 Form Ds is a "
    "Panera Bread director at the St. Louis head office, not SHV's James N. White of 755 Page Mill Road: a homonym. "
    "Panera Holdings is Panera's holding company after JAB Holding's 2017 take-private (industry: Restaurants), a "
    "buyout rather than a venture round; no SHV listing, SHV filing or documented round names it.",
    ec=FD, conf="high", cite=SEC("panera-holdings-corp")))
L.append(verdict("realitycheck-technology-llc", "not_member",
    "James Byron White on the 2013 Form D (a $180,000 offering by a St. Louis LLC) is its own executive officer and "
    "director at a Louisville, Kentucky address, " + HOMONYM_TAIL, ec=FD, conf="high",
    cite=SEC("realitycheck-technology-llc")))
L.append(verdict("triage-inc", "not_member",
    "James Thomas White on Triage's 2014 Form D is an executive officer at a Cohasset, Massachusetts address, beside "
    "the founder R. Charles White, " + HOMONYM_TAIL, ec=FD, conf="high", cite=SEC("triage-inc")))
L.append(verdict("unit-of-work-inc", "not_member",
    "James White on Unit of Work's 2020 Form D is the company's sole officer and director (its founder), at 288 "
    "Norfolk Street, Cambridge, Massachusetts, " + HOMONYM_TAIL, ec=FD, conf="high", cite=SEC("unit-of-work-inc")))
L.append(verdict("wicked-tango-llc", "not_member",
    "James William White on Wicked Tango's 2015 Form Ds is a director of a Las Vegas LLC at a Walnut Shade, "
    "Missouri address, " + HOMONYM_TAIL, ec=FD, conf="high", cite=SEC("wicked-tango-llc")))

# =====================================================================================
# Greg Sands: SHV to 2012, then his own Costanoa (D1 external, D5 seat dating).
# =====================================================================================
L.append(verdict("quizlet-inc", "not_member",
    "Greg Sands on Quizlet's 2015 Form D sat for Costanoa, the firm he founded in 2012 (D5): USV's own post on the "
    "$12M Series A says 'we joined our friends at Costanoa, Altos, and Owl'. No SHV listing, SHV filing or "
    "documented round names Quizlet.", ec=FD, conf="high", cite=USV_QUIZLET))
L.append(verdict("risk-io-inc", "not_member",
    "Gregory Sands files c/o Costanoa Venture Capital, 160 Forest Avenue, on Risk I/O's 2014 Form D: Costanoa's "
    "seat, the firm he founded in 2012 (D5). No SHV listing, SHV filing or documented round names the company.",
    ec=FD, conf="high", cite=SEC("risk-io-inc")))
L.append(verdict("victorops-inc", "not_member",
    "Gregory P. Sands on VictorOps' 2013 to 2016 Form Ds (Boulder) sat for Costanoa, the firm he founded in 2012 "
    "(D5); LinkSmart's own board page, archived May 2013, already lists him as Costanoa Venture Capital's director. "
    "No SHV listing, SHV filing or documented round names VictorOps.", ec=FD, conf="high", cite=SEC("victorops-inc")))

# Mandelbrot Project is LinkSmart's incorporation name (same CIK), and SHV listed LinkSmart.
L.append(verdict("mandelbrot-project-inc", "member",
    "Same company as the listed LinkSmart: Mandelbrot Project, Inc. renamed itself LinkSmart, Inc. in 2010 (SEC "
    "former name of CIK 1476100), and SHV's own archived portfolio lists LinkSmart from 2013 to 2016. Greg Sands, "
    "then an SHV managing director, joined the board at this 2010 round. Duplicate of the linksmart row: merge.",
    ec="site_listing", conf="high", cite=ARCH("linksmart")))
L.append(cls("mandelbrot-project-inc", status="acquired", rng="below_1b",
    stage="Series A", stage_src="formd_structural", stage_conf="medium", stage_cite=SEC("mandelbrot-project-inc"),
    entry_date="2010-06-30", city="Boulder", city_src="formd_address", focus="Media, Gaming & Advertising",
    note="LinkSmart (Boulder): in-text link monetization and content distribution for web publishers. VigLink "
         "acquired it on 25 November 2014 (VigLink's own page, archived December 2014: " + VIGLINK + "), so "
         "acquired, below_1b. Entry: the 2010 round of $4.1M from 25 investors, when Greg Sands, then at SHV, joined "
         "Foundry Group's Seth Levine on the board; one earlier filing ($500,000 from one investor, October 2009) "
         "makes it a Series A by the structural rule (one earlier filing, inside the 2010 Series A band). The "
         "linksmart row's 2013 filing is not SHV's entry: by then Sands sat for Costanoa (LinkSmart's own board "
         "page, May 2013). Same CIK as linksmart; the merged row should carry this entry.",
    rounds=[rnd("2010-06-30", "unnamed ($4.1M from 25 investors)", 4_100_000, None, True,
                SEC("mandelbrot-project-inc"), "filing")]))

# =====================================================================================
# Ron Bernal: at NEA from February 2010 (Sequel from May 2006).
# =====================================================================================
L.append(verdict("kumu-networks-inc", "not_member",
    "Ron Bernal on Kumu's 2012 Form D (c/o Kumu, Palo Alto) sat for NEA: he left SHV for Sequel Venture Partners "
    "(May 2006) and NEA (February 2010), so the seat is not SHV's (D5). Kumu's own staff: 'We were originally "
    "funded by NEA and Khosla' (Semiconductor Engineering, 2019). No SHV listing, SHV filing or documented round "
    "names Kumu.", ec=FD, conf="high", cite=KUMU_SE))

# =====================================================================================
# Stefan Dyckerhoff: Juniper to December 2012, SHV from October 2012.
# =====================================================================================
L.append(verdict("juniper-networks-inc", "not_member",
    "Stefan R. Dyckerhoff appears as an Executive Officer of Juniper Networks (c/o Juniper, Sunnyvale) on Juniper's "
    "own December 2012 Form D: he was a Juniper executive from October 2009 to December 2012 before SHV (D5; EDGAR "
    "full-text, Astera Labs' registration statement). Juniper was public from 1999 and the filing is its own "
    "offering, not an SHV position; the membership trap named in config.", ec=FD, conf="high",
    cite=SEC("juniper-networks-inc")))
L.append(verdict("rf-pixels-inc", "not_member",
    "Stefan Dyckerhoff (SHV managing director from October 2012) is a director on RF Pixels' 2016 and 2018 Form Ds, "
    "filing c/o the company in Fremont rather than from 755 Page Mill Road, beside Walden's Lip-Bu Tan. No SHV "
    "listing, SHV filing or documented round names the company and Google News carries nothing on it; vendor "
    "profiles list SHV, which cannot carry membership. A name-match without corroboration is not_member "
    "(COLLECTION.md s1); worth a second look if a round announcement surfaces.", ec=FD, conf="medium",
    cite=SEC("rf-pixels-inc")))
L.append(verdict("neye-systems-inc", "member",
    "A documented round names SHV: nEye's $80M Series C of April 2026 'was led by Palo Alto's Sutter Hill Ventures', "
    "and Stefan Dyckerhoff, SHV managing director, joined the board (citybiz); he is a director on the round's Form "
    "D. Fund money through a primary round.", ec="web", conf="high", cite=NEYE_CB))
L.append(cls("neye-systems-inc", status="private", rng="below_1b",
    city="Santa Clara", city_src="web_verified", focus="Industrial & Robotics",
    extra={"valuation_range_source": "web_verified", "valuation_asof": "2026-04-15", "valuation_citation": NEYE_CB},
    note="Wafer-scale optical circuit switches for AI data centres, out of Ming Wu's UC Berkeley lab; Santa Clara "
         "(citybiz). SHV's entry is the Series C it led in April 2026, a Growth entry, which the prefilled band "
         "agrees with. Momentum check 2026-09-28: no valuation was disclosed for the Series C or for the $58M "
         "Series B of April 2025 led by CapitalG (Reuters), so below_1b. Chips and optical hardware read Industrial "
         "& Robotics, as the sibling books class Ayar Labs, Lightmatter and Enfabrica.",
    rounds=[rnd("2023", "Series A (unannounced, led by TEDA Holdings)", None, "TEDA Holdings", None, NEYE_P2, "press"),
            rnd("2025-04-10", "Series B", 58_000_000, "CapitalG", None, NEYE_RT, "press"),
            rnd("2026-04-15", "Series C", 80_000_000, "Sutter Hill Ventures", True, NEYE_CB, "press")]))

# =====================================================================================
# Andy Sheehan: on SHV's team page through May 2016.
# =====================================================================================
L.append(verdict("nav-technologies-inc", "not_member",
    "Andy Sheehan (on SHV's team page through May 2016) is a director on Nav's 2016 to 2018 Form Ds, filing from "
    "Nav's San Mateo and Draper offices, not 755 Page Mill Road. Nav's own release names its rounds without SHV: "
    "Experian led the $25M Series B with Crosslink Capital, Tencent and other existing investors, Kleiner Perkins "
    "led the $6.5M Series A, Goldman Sachs PSI led the 2017 expansion. No SHV listing, SHV filing or documented "
    "round names Nav; a seat alone is not a fund position (COLLECTION.md s1).", ec=FD, conf="medium", cite=NAV_B))
L.append(verdict("serviz-inc", "uncertain",
    "Andy Sheehan (SHV managing director, in tenure) joined the board at the February 2014 Series A, which Groupon "
    "led with other investors (socaltech); the December 2014 Series B coverage lists 'existing investors Andy "
    "Sheehan of Sutter Hill Ventures, Jeff Stibel of Stibel Investments' and the founders (Los Angeles Business "
    "Journal), naming the person beside his firm, as it names Stibel beside his own vehicle, rather than the firm. "
    "Whether the money was the partnership's or Sheehan's own (D2) is open; no SHV listing or filing settles it. "
    "Porch acquired Serviz in 2018.", ec="web", conf="low", cite=SERVIZ_LABJ))

# =====================================================================================
# Jeff Bird: SHV to 2019, then his own Bluebird Ventures (D1 external).
# =====================================================================================
L.append(verdict("procyrion-inc", "not_member",
    "Jeff Bird's seat on Procyrion is Bluebird Ventures', his own vehicle formed in 2019 (external under D1): the "
    "2019 $30M Series D 'was lead by Bluebird Ventures' and 'Jeff Bird, managing director of Bluebird Ventures, "
    "will join the company's board' (InnovationMap); the 2024 Series E release names Bluebird as a returning "
    "investor. No SHV listing, SHV filing or documented round names Procyrion.", ec=FD, conf="high", cite=PROC_D))
L.append(verdict("theracos-inc", "not_member",
    "Jeff Bird (SHV managing director, in tenure) is a director on Theracos' 2013 and 2016 Form Ds, filing from the "
    "company's Marlborough, Massachusetts office, not 755 Page Mill Road. SHV's own 2013 to 2016 portfolio pages "
    "list his other companies (Portola, AkaRx, Drais, Forty Seven) but never Theracos; no SHV filing or documented "
    "round names it, and a vendor profile's listing of SHV cannot carry membership. A name-match without "
    "corroboration is not_member (COLLECTION.md s1).", ec=FD, conf="medium", cite=SEC("theracos-inc")))

DRAIS = ("a virtual company run by Drais Pharmaceuticals (Bridgewater, New Jersey; itself an SHV and InterWest "
         "company)")
L.append(verdict("telsar-pharma-inc", "member",
    "A documented round names SHV: 'InterWest Partners and Sutter Hill Ventures' plus Astellas Venture Management "
    "'will invest a total of $14 million into Telsar' (Fierce Biotech, April 2012); Jeff Bird, SHV managing "
    "director, files c/o Sutter Hill Ventures, 755 Page Mill Road on the Form D.", ec="web", conf="high",
    cite=TELSAR_FIERCE))
L.append(cls("telsar-pharma-inc", status="unknown", rng="below_1b", city="Bridgewater", city_src="formd_address",
    focus="Healthcare & Bio",
    note="Telsar is " + DRAIS + " to develop Astellas' ASP3291 for ulcerative colitis. Its Phase 2 study "
         "(NCT01612039) completed in April 2014; no later filing, trial or news traces the company, so status "
         "unknown (a later pass could settle it). Entry: the $14M formation round of April 2012; the prefilled "
         "Series A band stands, since the record gives no round word.",
    rounds=[rnd("2012-04", "formation financing (unnamed)", 14_000_000, None, True, TELSAR_FIERCE, "press")]))
L.append(verdict("seldar-pharma-inc", "member",
    "A documented round names SHV: Seldar and Telsar share the same investors, Astellas Venture Management, "
    "InterWest Partners and Sutter Hill Ventures, which 'have invested $13m into Seldar' (Global Venturing, June "
    "2012); Jeff Bird, SHV managing director, files c/o Sutter Hill Ventures, 755 Page Mill Road on the Form D.",
    ec="web", conf="high", cite=SELDAR_GV))
L.append(cls("seldar-pharma-inc", status="unknown", rng="below_1b", city="Bridgewater", city_src="formd_address",
    focus="Healthcare & Bio",
    note="Seldar is " + DRAIS + " to develop Astellas' ASP7147 for diarrhoea-predominant IBS. Its Phase 2 pilot "
         "(NCT01896583) completed in July 2014; no later filing, trial or news traces the company, and Astellas' "
         "option to acquire is not reported exercised, so status unknown (a later pass could settle it). Entry: the "
         "$13M formation round of May to June 2012; the prefilled Series A band stands, since the record gives no "
         "round word.",
    rounds=[rnd("2012-06", "formation financing (unnamed)", 13_000_000, None, True, SELDAR_GV, "press")]))

# NovoGlia and Savanna Biotherapeutics: one company (CIK 1873404, renamed 2025).
NOVO_NOTE = ("Savanna Biotherapeutics (NovoGlia, Inc. until 2025, same CIK 1873404): iPSC-derived microglia cell "
             "therapy, lead program SB-101 for ALSP, IND planned for the first half of 2027 (BIO 2026 listing, HQ "
             "Aliso Viejo): private, no priced round disclosed, below_1b. Entry: the first filing, $24.3M sold of "
             "$54.3M offered from 2022-11-03; the Growth band reads the $54.3M offering. A vendor profile calls the "
             "funding a $37.3M Series A-II (the two filings' $24.3M and $13.0M together), which points to a tranched "
             "Series A; vendors cannot cite (Rule A), so the band stands until a company or firm announcement names "
             "the round. Bluebird Ventures (Jeff Bird's own vehicle, external under D1) co-invests. Duplicate pair: "
             "novoglia-inc and savanna-biotherapeutics-inc.")
NOVO_ROUNDS = [rnd("2022-11-03", "first filed round (unnamed)", 24_304_480, None, True, jl.FORMD_CITE("novoglia-inc", 0), "filing"),
               rnd("2025-06-12", "second filed round (unnamed)", 12_999_997, None, True, jl.FORMD_CITE("novoglia-inc", 1), "filing"),
               rnd("2025", "Series A-II, $37.3M in total (vendor profile)", 37_300_000, None, None, SAVANNA_VENDOR, "vendor")]
L.append(verdict("novoglia-inc", "member",
    "SHV principals sit on both of the company's Form Ds: Mike Speiser (SHV managing director) is a director on this "
    "2022 filing, and Keith Loebner (an SHV principal on the adviser's Schedule A) files from 755 Page Mill Road on "
    "the 2025 filing, beside Jeff Bird; the issuer resolves to a real company (Savanna Biotherapeutics, microglia "
    "cell therapy, Aliso Viejo; CIRM funded Novoglia, Inc. in 2023). Director-of-record pattern at the firm's "
    "address, in tenure: member at medium, flagged for the A/B pass. Same company as savanna-biotherapeutics-inc "
    "(CIK 1873404): merge.", ec=FD, conf="medium", cite=SEC("novoglia-inc")))
L.append(cls("novoglia-inc", status="private", rng="below_1b", city="Aliso Viejo", city_src="web_verified",
    focus="Healthcare & Bio", note=NOVO_NOTE, rounds=NOVO_ROUNDS))
L.append(verdict("savanna-biotherapeutics-inc", "member",
    "Keith Loebner (an SHV principal on the adviser's Schedule A) and Jeff Bird file from 755 Page Mill Road, Suite "
    "A-200 on the company's 2025 Form D, and Mike Speiser (SHV managing director) sat on its 2022 filing as "
    "NovoGlia; the issuer resolves to a real company (microglia cell therapy, Aliso Viejo). Director-of-record "
    "pattern at the firm's address, in tenure: member at medium, flagged for the A/B pass. Same company as "
    "novoglia-inc (CIK 1873404, renamed 2025): merge.", ec=FD, conf="medium", cite=SEC("savanna-biotherapeutics-inc")))
L.append(cls("savanna-biotherapeutics-inc", status="private", rng="below_1b",
    stage="Growth", stage_src="formd_band", entry_date="2022-11-03",
    city="Aliso Viejo", city_src="web_verified", focus="Healthcare & Bio",
    note=NOVO_NOTE + " This row mirrors novoglia-inc's entry: the band is the company's first filing, made under the "
                     "NovoGlia name.",
    rounds=NOVO_ROUNDS))

# =====================================================================================
# Mike Speiser: SHV incubations and partner seats.
# =====================================================================================
L.append(verdict("laserlike-inc", "member",
    "SHV incubation (D3): Mike Speiser, SHV managing director, is executive officer and director on the 2015 Form D, "
    "filing from 755 Page Mill Road with the founders; 'Laserlike had raised $24 million in two rounds led by Sutter "
    "Hill Ventures and Redpoint' (Voicebot, citing TechCrunch, 2019). Fund money through a documented round.",
    ec="web", conf="high", cite=LL_VB))
L.append(cls("laserlike-inc", status="acquired", rng="below_1b",
    grad="graduated", grad_src="web_verified", grad_cite=LL_VB, grad_conf="high",
    city="Mountain View", city_src="formd_address", focus="AI & Applied AI",
    note="Personalised content discovery built by three former Google search engineers, Mountain View (the 2016 "
         "Form D). Apple bought it and confirmed the acquisition in March 2019 (iPhone in Canada), so acquired, "
         "below_1b. Entry: the first round of September 2015, $4.18M sold, which SHV led; the prefilled Seed band "
         "stands, and Redpoint's own row bands the later round a Series A. Graduated: the second of the 'two rounds "
         "led by Sutter Hill Ventures and Redpoint' is the $19.97M round of November 2016 on the company's Form D, "
         "more than four times the entry and over $5M, the step-up test for an unnamed round.",
    rounds=[rnd("2015-09-09", "first round (unnamed)", 4_175_000, "Sutter Hill Ventures", True, LL_VB, "press"),
            rnd("2016-11-23", "second round (unnamed)", 19_974_984, "Redpoint", None, LL_VB, "press")]))

L.append(verdict("luminary-cloud-inc", "member",
    "SHV incubation (D3): 'Luminary was incubated by Sutter Hill Ventures beginning in 2019' and is backed by SHV, "
    "'which led its $115 million funding' (the company's release, March 2024); Mike Speiser and Jason Lango file "
    "from 755 Page Mill Road on the 2020 Form D. Fund money through documented rounds.",
    ec="web", conf="high", cite=LUM_PR))
L.append(cls("luminary-cloud-inc", status="private", rng="below_1b",
    city="San Mateo", city_src="web_verified", focus="AI & Applied AI",
    note="GPU cloud engineering simulation that now sells itself as a physics AI platform, San Mateo (SiliconANGLE, "
         "September 2025). Private: its $72M Series B of September 2025 was led by N47 with SHV and NVentures "
         "(SiliconANGLE), no price disclosed, so below_1b; checked 2026-09-28 for a $1B+ priced round, none found. "
         "The prefilled Series A (the $15M first filing of December 2020) agrees with the record: SHV led the $115M "
         "the company raised before that Series B.",
    rounds=[rnd("2020-12-11", "first filed round (unnamed; the Series A by the later Series B)", 14_999_999, None, True,
                SEC("luminary-cloud-inc"), "filing"),
            rnd("2024-03-13", "$115M raised to date, led by SHV (unnamed)", 115_000_000, "Sutter Hill Ventures", True,
                LUM_PR, "company"),
            rnd("2025-09-15", "Series B", 72_000_000, "N47", True, LUM_SA, "press")]))

L.append(verdict("observe-inc", "member",
    "SHV incubation (D3): 'Observe was founded in 2017 by SHV' and has raised $35M 'in Series A and debt-financing "
    "from Sutter Hill Ventures' (the company's release, October 2020); SHV led its $115M Series B of March 2024; "
    "Mike Speiser files from 755 Page Mill Road on the 2024 and 2025 Form Ds. Fund money through documented rounds.",
    ec="web", conf="high", cite=OBS_2020))
L.append(cls("observe-inc", status="acquired", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=OBS_2020, stage_conf="high", entry_date="2020",
    flags=["stage_disputes_band"], city="San Mateo", city_src="web_verified", focus="Data Infrastructure",
    note="Observability built on Snowflake, San Mateo. Snowflake agreed to buy it in January 2026 (terms "
         "undisclosed, reported near $1B) and closed on 2026-02-02 (Snowflake's own post), so acquired, below_1b. "
         "Stage disputes the band: the prefilled Growth reads the first Form D under the new CIK (February 2024), "
         "but SHV formed the company in 2017 and funded it alone through its Series A (the October 2020 release), "
         "which the Series B release of March 2024 dates 'four years ago'; entry 2020, Series A. SHV also led the "
         "Series B and joined the $70M debt round of May 2022 (TechCrunch).",
    rounds=[rnd("2020", "Series A (with debt financing, $35M together)", 35_000_000, "Sutter Hill Ventures", True,
                OBS_2020, "company"),
            rnd("2022-05-11", "debt round", 70_000_000, None, True, OBS_TC, "press"),
            rnd("2024-03-27", "Series B", 115_000_000, "Sutter Hill Ventures", True, OBS_B, "company"),
            rnd("2025-05-22", "$145M round (Tech Funding News calls it a Series B)", 144_999_986,
                "Evolution Equity Partners and Madrona", None, OBS_TFN, "press")]))

L.append(verdict("lacework-inc", "member",
    "SHV incubation (D3; Crunchbase News, 2021: Lacework and Snowflake 'were incubated by Sutter Hill'). The "
    "company's own release of 2018-08-28 announces a $24M Series B 'led by Sutter Hill Ventures' and calls Lacework "
    "a company 'funded by Sutter Hill Ventures'; Mike Speiser and Stefan Dyckerhoff, SHV managing directors in "
    "tenure, sit on its 2017 to 2021 Form Ds. Fund money through documented rounds.",
    ec="web", conf="high", cite=LACEWORK_B))
L.append(cls("lacework-inc", status="acquired", rng="below_1b",
    stage="Series A", stage_src="model", stage_conf="medium", stage_cite=LACEWORK_B, entry_date="2015",
    city="San Jose", city_src="web_verified", focus="Security",
    note="Cloud security, San Jose. SHV formed Lacework (founded 2015) and was its only funder until 2018: the "
         "release of 2018-08-28 announces the $24M Series B led by SHV and puts total funding at $32.7M, so the "
         "$8.7M raised before it was SHV's Series A, the entry (model, medium; a vendor dates it May 2015). SHV "
         "also funded the $42M 2019 round and co-led the $525M round of January 2021 with Altimeter (SiliconANGLE "
         "calls it the Series D); the $1.3B round of November 2021 priced it at $8.3B (CRN). Fortinet completed "
         "the acquisition on 2024-08-02, terms undisclosed (CRN), so acquired, below_1b. HQ San Jose (Crunchbase "
         "News, January 2021; the 2021 Form Ds), moved from Mountain View; Coatue's sibling row reads Mountain "
         "View, the HQ until 2020, General Catalyst's reads San Jose, and this row holds the later cited address.",
    rounds=[rnd("2015", "financing before the Series B (unnamed; $8.7M by the release's totals)", 8_700_000,
                "Sutter Hill Ventures", True, LACEWORK_B, "company"),
            rnd("2018-08-28", "Series B", 24_000_000, "Sutter Hill Ventures", True, LACEWORK_B, "company"),
            rnd("2019-09", "$42M financing (unnamed)", 42_000_000, None, True, LACEWORK_42, "company"),
            rnd("2021-01-07", "Series D", 525_000_000, "Sutter Hill Ventures and Altimeter Capital", True, LW_SA, "press"),
            rnd("2021-11-18", "$1.3B round at an $8.3B valuation", 1_300_000_000, None, None, LW_CRN, "press")]))

L.append(verdict("sigma-computing-inc", "member",
    "SHV incubation (D3): Bitmoon Computing, Sigma's incorporation name, files in 2014 with Mike Speiser and Sam "
    "Pullara as directors c/o Sutter Hill Ventures, 755 Page Mill Road; documented rounds name the partnership, "
    "the December 2021 Series C release among 'Existing Investors Sutter Hill Ventures and Altimeter Capital'.",
    ec="web", conf="high", cite=SIGMA_C))
L.append(cls("sigma-computing-inc", status="private", rng="1b_plus", usd=3_000_000_000, val_src="web_verified",
    val_cite=SIGMA_E, asof="2026-05-18", val_conf="high", extra={"valuation_range_source": "web_verified"},
    city="San Francisco", city_src="web_verified", focus="Data Infrastructure",
    note="Cloud analytics and BI on the data warehouse, San Francisco. Mark: the $80M Series E closed 2026-05-18 at a "
         "$3B valuation, led by Princeville Capital with SHV participating (the company's announcement), aligned "
         "with Spark Capital's row ($3B, May 2026). Stage check on a $1B+ row: the prefilled Series A (the $8.0M "
         "first filing of April 2014, as Bitmoon Computing) agrees with the record. VentureBeat (November 2019) "
         "calls the $30M then raised an extension of the Series B with about $60M raised in total, which the "
         "filings split as $8.0M (2014), $20.0M (2017) and $30M (2019), so the 2014 round SHV funded at formation "
         "is the Series A.",
    rounds=[rnd("2014-04-15", "first round (unnamed; the Series A by the later Series B)", 8_000_301, None, True,
                SEC("sigma-computing-inc"), "filing"),
            rnd("2017-12-20", "second round (unnamed; the Series B by the 2019 extension)", 19_999_997, None, None,
                SEC("sigma-computing-inc", "formd", 1), "filing"),
            rnd("2019-11", "Series B extension", 30_000_000, None, True, SIGMA_VB, "press"),
            rnd("2021-12-16", "Series C", 300_000_000, "D1 Capital Partners and XN", True, SIGMA_C, "company"),
            rnd("2024-05", "Series D", 200_000_000, "Spark Capital and Avenir", None, SIGMA_D, "company"),
            rnd("2026-05-18", "Series E", 80_000_000, "Princeville Capital", True, SIGMA_E, "company")]))

L.append(verdict("stride-software-inc", "not_member",
    "Mike Speiser (SHV managing director, in tenure) is a director on Stride Software's June 2017 Form D (StrideSpark, "
    "Inc. until 2017), filing from the company's 433 Hamilton Avenue office, not 755 Page Mill Road; the founders "
    "are its executive officers from the first 2016 filing, which names no SHV person, so this is not the "
    "incubation pattern. No SHV listing, SHV filing or documented round names the company and Google News has "
    "nothing on it; vendor profiles list SHV and a 2019 sale to Snowflake, neither citable. A name-match without "
    "corroboration is not_member (COLLECTION.md s1); worth a second look.", ec=FD, conf="medium",
    cite=SEC("stride-software-inc")))


if __name__ == "__main__":
    b = __import__("json").loads((Path(__file__).resolve().parent / "queue" / f"batch-{N:03d}.json").read_text())
    want = {i["slug"] for i in b}
    got = {x["slug"] for x in L if "verdict" in x}
    assert want == got, (sorted(want - got), sorted(got - want))
    jl.write(f"batch-{N:03d}", L, record=not os.environ.get("DRY"))
