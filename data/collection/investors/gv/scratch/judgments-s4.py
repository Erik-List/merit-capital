#!/usr/bin/env python3
"""Sweep judge s4 (PRO-75, COLLECTION.md s8 duty 9, 2026-09-29): the undetermined-stage and unknown-status class,
49 rows. Settled here: 18 entry stages (5 Seed rows decided for S2A). Rows no source settles get no line (26 stages,
all 9 statuses). The firm's listing capture is used only as a bound (GV was in by that date), never as a label
(lead's clarification of SWEEP-BRIEF). Notes carry only the new sentences (record appends)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl  # noqa: E402

N = "Stage sweep 2026-09-29: "
ASOF = "2026-09-29"
UNC = ["stage_uncited"]

# ---- citations printed by the tools run for this sweep (TechCrunch's own search, EDGAR, nq.py via jl.NEWS)
TC_BUGSNAG_SEED = "https://techcrunch.com/2013/09/20/bugsnag-the-error-reporting-platform-used-by-linkedin-and-others-raises-1-2m-seed-round/"
TC_BUGSNAG_A = "https://techcrunch.com/2015/07/07/bugsnag-nabs-7-2-million-in-series-a-funding-from-benchmark/"
TC_BUGSNAG_B = "https://techcrunch.com/2018/01/10/bugsnag-snares-9-million-series-b-now-gives-you-a-software-stability-score/"
PRN_RESOLUTION_B = "https://www.prnewswire.com/news-releases/resolution-games-closes-7-5-million-series-b-funding-round-300734705.html"
TC_AMBITION = "https://techcrunch.com/2014/02/21/ambition-launch/"
SEC_AMBITION_2018 = "https://www.sec.gov/Archives/edgar/data/1743326/000174332618000001/0001743326-18-000001-index.htm"
SEC_AUTOLUS_F1 = "https://www.sec.gov/Archives/edgar/data/1730463/000119312518154573/d531832df1.htm"
TC_BLUEBOTTLE_2012 = "https://techcrunch.com/2012/10/15/hipster-coffee-lovers-rejoice-blue-bottle-coffee-raises-20m/"
TC_BLUEBOTTLE_2014 = "https://techcrunch.com/2014/01/29/coffee/"
TC_MIXBIT_2014 = ("https://techcrunch.com/2014/06/06/youtube-co-founders-break-up-as-chad-hurley-spins-out-his-own-company"
                  "-and-steve-chen-joins-google-ventures/")
TC_NEST = "https://techcrunch.com/2014/01/13/nest-investors-strike-it-rich/"
SEC_VVEHICLE_2009_06 = "https://www.sec.gov/Archives/edgar/data/1398503/000139850309000003/0001398503-09-000003-index.htm"
SEC_VVEHICLE_2009_07 = "https://www.sec.gov/Archives/edgar/data/1398503/000139850309000004/0001398503-09-000004-index.htm"
TC_SIGNPOST_2010 = "https://techcrunch.com/2010/10/20/signpost-local-deals/"
TC_SIGNPOST_B = "https://techcrunch.com/2013/11/19/signpost-series-b/"
TC_SIGNPOST_C = "https://techcrunch.com/2015/04/28/signpost-series-c/"
TC_SIGNPOST_2019 = "https://techcrunch.com/2019/07/09/signpost-nabs-52m-to-help-smbs-collect-reviews-and-marketing-collateral-like-bigger-rivals/"
SEC_SIGNPOST_2010 = "https://www.sec.gov/Archives/edgar/data/1484639/000148463910000001/0001484639-10-000001-index.htm"
SEC_SIGNPOST_2012 = "https://www.sec.gov/Archives/edgar/data/1484639/000148463912000004/0001484639-12-000004-index.htm"
TC_SCOUT_SEED = "https://techcrunch.com/2015/01/27/automating-the-rfp-process-nets-scout-rfp-2-75-million/"
TC_SCOUT_B = "https://techcrunch.com/2017/06/07/scout-rfp-raises-15-5-million-to-help-companies-manage-purchases/"
SEC_OC_2013 = "https://www.sec.gov/Archives/edgar/data/1592389/000159238913000001/0001592389-13-000001-index.htm"
SEC_OC_2014 = "https://www.sec.gov/Archives/edgar/data/1592389/000159238914000002/0001592389-14-000002-index.htm"
SEC_OC_2015 = "https://www.sec.gov/Archives/edgar/data/1592389/000159238915000001/0001592389-15-000001-index.htm"
TC_STAMPED_2011 = "https://techcrunch.com/2011/11/21/stamped-approval/"
TC_STAMPED_YAHOO = "https://techcrunch.com/2012/10/25/yahoo-bought-stamped/"
GVC_STAMPED = "https://globalventuring.com/blog/2012/07/25/google-ventures-backs-stamped/"
SEC_LEDGER_2014 = "https://www.sec.gov/Archives/edgar/data/1596252/000159625214000002/0001596252-14-000002-index.htm"
SEC_LEDGER_2018 = "https://www.sec.gov/Archives/edgar/data/1596252/000159625218000003/0001596252-18-000003-index.htm"
SEC_MPARTICLE_2013 = "https://www.sec.gov/Archives/edgar/data/1582826/000158282613000002/0001582826-13-000002-index.htm"
TC_MPARTICLE_SEED2 = "https://techcrunch.com/2014/10/09/mparticle-seed-funding/"
TC_MPARTICLE_A = "https://techcrunch.com/2016/01/13/mparticle-series-a/"
TC_MPARTICLE_B = "https://techcrunch.com/2016/10/13/mparticle-series-b/"
TC_POYNT_A = "https://techcrunch.com/2014/10/29/former-google-wallet-head-launches-poynt-a-future-proofed-payment-terminal/"
TC_POYNT_C = "https://techcrunch.com/2018/11/13/poynt-raises-100m-for-its-smart-payment-terminal/"
VB_POYNT_B = "https://venturebeat.com/business/former-google-exec-raises-28m-to-start-shipping-his-smart-payment-terminals"
GNW_TOME = ("https://www.globenewswire.com/news-release/2023/12/12/2794660/0/en/tome-biosciences-launches-with-over-200-million"
            "-in-funding-to-advance-programmable-genomic-integration-platform.html")
FINSMES_SCOUT_A = "https://www.finsmes.com/2016/07/scout-rfp-raises-9m-in-series-a-funding.html"
PRN_SCOUT_C = ("https://www.prnewswire.com/news-releases/scout-rfp-raises-33m-to-define-the-future-of-strategic-sourcing-and"
               "-procurement-including-investments-from-scale-venture-partners-and-workday-ventures-300778193.html")
PULSE_SCOUT_WORKDAY = "https://pulse2.com/workday-buying-scout-rfp-540-million/"
BB_FORMD = "https://www.sec.gov/Archives/edgar/data/1560324/{}/primary_doc.xml"
FASTCO_NEST = "https://www.fastcompany.com/3005231/tony-fadells-nest-thermostat-company-hits-800-million-valuation"

# ---- Google News headlines (decoded to the publisher URL by jl.NEWS, cached in news-decoded-s4.json)
BI_RESOLUTION = jl.NEWS("resolution-games", "first investment in mainland Europe")
BI_AMBITION = jl.NEWS("ambition", "Fantasy Football Meets Sales")
BJ_AMBITION_B = jl.NEWS("ambition", "stoked with Series B")
TFP_AMBITION = jl.NEWS("ambition", "Chattanooga-based digital sales software provider")
DEALBOOK_BB = jl.NEWS("blue-bottle-coffee", "Blue Bottle Raises $25.75")
LABIOTECH_EVOX = jl.NEWS("evox-therapeutics", "Oxford Biotech Raises")
BIOINFORMANT_EVOX = jl.NEWS("evox-therapeutics", "Richly Funded Exosome")
BI_AVOS = jl.NEWS("mixbit", "Steve Chen Explains What He")
FINSMES_AVOS = jl.NEWS("mixbit", "AVOS Systems Closes Series A")
BGR_NEST = jl.NEWS("nest", "Why Google Bought Nest")
FORTUNE_VVEHICLE = jl.NEWS("next-autoworks", "Kleiner trial suggests")
STAT_TOME = jl.NEWS("tome-biosciences", "New CRISPR startup, drawing big-name backers")
BIOSPACE_TOME = jl.NEWS("tome-biosciences", "Tome Biosciences Launches with $213M")
USAT_OC = jl.NEWS("the-orange-chef-co", "Orange Chef sees its future")
PRN_OC = jl.NEWS("the-orange-chef-co", "Perfect Company Acquires")
BI_STAMPED = jl.NEWS("stamped", "Ex-Googlers Relaunch")

L = [
 # ---- Growth
 jl.cls("bugsnag", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=TC_BUGSNAG_B,
        entry_date="2018-01-10",
        rounds=[jl.rnd("2013-09-20", "Seed", 1400000, None, False, TC_BUGSNAG_SEED),
                jl.rnd("2015-07-07", "Series A", 7200000, "Benchmark", False, TC_BUGSNAG_A),
                jl.rnd("2018-01-10", "Series B", 9000000, None, True, TC_BUGSNAG_B)],
        note=N + "TechCrunch (2018-01-10) reports the $9M Series B with 'first-timer GV (formerly Google Ventures) joining "
                 "existing investors Matrix Partners and Benchmark Capital', after a $1.4M seed (2013) and the $7.2M "
                 "Series A led by Benchmark (2015): GV entered at the Series B, Growth."),
 jl.cls("autolus", stage="Growth", stage_src="model", stage_conf="medium", stage_cite=SEC_AUTOLUS_F1,
        entry_date="2017-09-25",
        rounds=[jl.rnd("2014-09-25", "series A preferred (initial)", None, "Syncona", False, SEC_AUTOLUS_F1, "filing"),
                jl.rnd("2016-03-02", "series A preferred (GBP 23.3M; Syncona, Woodford, Arix only)", None, None, False,
                       SEC_AUTOLUS_F1, "filing"),
                jl.rnd("2017-04-03", "series A preferred (GBP 36.7M in two tranches; Syncona, Woodford, Arix only)", None,
                       None, False, SEC_AUTOLUS_F1, "filing"),
                jl.rnd("2017-09-25", "series A preferred (press: Series C; eleven investors)", 80000000, None, True,
                       SEC_AUTOLUS_F1, "filing")],
        note=N + "the F-1's own issuance history gives every private round before September 2017 to Syncona, Woodford and "
                 "Arix alone (its related-party tables account for all 18,547,008 shares of March 2016 and both 2017 "
                 "tranches), while the $80.0M round of 2017-09-25 went to eleven investors; the F-1 names Google "
                 "Ventures among its backers, so GV entered in that round, which the press calls the Series C: Growth "
                 "(model, medium)."),
 jl.cls("evox-therapeutics", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=LABIOTECH_EVOX,
        entry_date="2018-09-03",
        rounds=[jl.rnd("2016-05-11", "Series A (GBP 10M)", None, "Oxford Sciences Innovation", False, BIOINFORMANT_EVOX),
                jl.rnd("2018-09-03", "Series B (GBP 35.5M)", 46500000, "Redmile Group", True, LABIOTECH_EVOX),
                jl.rnd("2021-02-18", "Series C", None, None, None, BIOINFORMANT_EVOX)],
        note=N + "Labiotech (2018-09-03) reports the GBP 35.5M Series B backed, among others, by the venture arm of "
                 "Google's parent, and BioInformant (2018-10-01) names Redmile its lead 'with significant new investments "
                 "from GV (formerly Google Ventures)', after a GBP 10M Series A from Oxford Sciences Innovation (2016); "
                 "the firm lists Evox from its December 2018 capture: GV entered at the Series B, Growth."),
 jl.cls("nest", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=TC_NEST, entry_date="2011-08",
        rounds=[jl.rnd("2010-09", "Series A", None, "Kleiner Perkins, Shasta Ventures", False, TC_NEST),
                jl.rnd("2011-08", "Series B", None, "Google Ventures", True, TC_NEST),
                jl.rnd("2013-01-30", "Unnamed round ($800M valuation reported)", None, None, None, FASTCO_NEST)],
        note=N + "TechCrunch (2014-01-13): 'Shasta and KPCB funded all of Nest's Series A round back in September 2010', "
                 "and the August 2011 Series B 'also included Google Ventures', which led Nest's Series B and C rounds; "
                 "BGR (2014-01-14) also says Google Ventures helped lead the 2011 Series B. GV entered at the Series B, "
                 "Growth."),
 jl.cls("next-autoworks", stage="Growth", stage_src="model", stage_conf="medium", stage_cite=SEC_VVEHICLE_2009_07,
        entry_date="2009-07",
        rounds=[jl.rnd("2009-06-10", "debt bridge ($3.4M sold)", 3400000, None, None, SEC_VVEHICLE_2009_06, "filing"),
                jl.rnd("2009-07-20", "equity ($62.3M sold to 13 investors)", 62256674, None, True, SEC_VVEHICLE_2009_07,
                       "filing")],
        note=N + "Fortune (2015-03-12) reports that Ellen Pao connected V-Vehicle with Google Ventures and T. Boone "
                 "Pickens 'for further investment' after Kleiner Perkins' own; the company's filings (V Vehicle Co, CIK "
                 "1398503) show a 2007 paper Form D, a $3.4M debt bridge from June 2009 and a $62.3M equity round from "
                 "2009-07-20 on which Google's David Drummond joins the board, so GV entered in the July 2009 round, "
                 "after the 2007 round and the bridge: Growth (model, medium)."),
 jl.cls("tome-biosciences", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2023-12",
        rounds=[jl.rnd("2022-09", "Series A (closed; backers ARCH, Andreessen Horowitz, Longwood Fund)", None, None, False,
                       STAT_TOME),
                jl.rnd("2023-12-12", "Series A and Series B (combined $213M)", 213000000, None, True, GNW_TOME, "company")],
        note=N + "STAT (2022-09-20) describes Tome, still in stealth, as backed by ARCH, Andreessen Horowitz and the "
                 "Longwood Fund, 'which have closed a Series A round'; GV first appears in the December 2023 launch list "
                 "for the combined $213M Series A and B (BioSpace, 2023-12-12, " + BIOSPACE_TOME + "), and the firm lists "
                 "Tome from its early 2024 capture, so GV entered at the Series B: Growth (model, medium)."),
 # ---- Series A
 jl.cls("resolution-games", stage="Series A", stage_src="model", stage_conf="medium", stage_cite=BI_RESOLUTION,
        entry_date="2015-08-26",
        rounds=[jl.rnd("2015-08-26", "unnamed $6M (the Series A by the company's naming of its next round)", 6000000,
                       "Google Ventures", True, BI_RESOLUTION),
                jl.rnd("2018-10-23", "Series B", 7500000, "MizMaa Ventures", True, PRN_RESOLUTION_B, "company"),
                jl.rnd("2021-07-14", "Series C", 25000000, None, None, None)],
        note=N + "Business Insider (2015-08-26) reports a $6M round led by Google Ventures with Creandum, Bonnier, "
                 "Partech and Initial Capital; the company's own release names its $7.5M October 2018 round the Series "
                 "B and puts total funding at $13.5M, so the $6M round was the only one before it and is its Series A "
                 "(model, medium). Creandum's row calls the same round a seed, uncited."),
 jl.cls("blue-bottle-coffee", stage="Series A", stage_src="model", stage_conf="medium", stage_cite=TC_BLUEBOTTLE_2014,
        entry_date="2012-10",
        rounds=[jl.rnd("2012-10-01", "equity $19.7M (the Series A by the company's naming of the 2014 round)", 19672975,
                       "True Ventures", True, BB_FORMD.format("000156032412000001"), "filing"),
                jl.rnd("2014-01-24", "Series B", 25750039, "Morgan Stanley Investment Management", True,
                       TC_BLUEBOTTLE_2014),
                jl.rnd("2015-05-29", "equity (unnamed)", 74958801, None, None, BB_FORMD.format("000156032415000001"),
                       "filing")],
        note=N + "TechCrunch (2014-01-29) calls the $25.7M round of January 2014 the company's series B and lists Google "
                 "Ventures among the 'former investors' who joined it (DealBook the same day also names Google Ventures); "
                 "the only earlier institutional round is the $19.7M raised from October 2012, its first Form D, led by "
                 "True Ventures (TechCrunch, 2012-10-15), and the firm listed Blue Bottle from its May 2013 capture, so GV "
                 "entered in the 2012 round, the Series A by the company's own later naming (model, medium)."),
 jl.cls("mixbit", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=BI_AVOS,
        entry_date="2012-04-27",
        rounds=[jl.rnd("2012-04-27", "Series A (Avos Systems' first outside round)", None, None, True, BI_AVOS)],
        note=N + "MixBit is the renamed Avos Systems (TechCrunch, 2014-06-06, and Wikipedia: in 2014 Avos turned into a "
                 "single company working only on MixBit). Business Insider (2012-04-27) reports Avos's first round of "
                 "outside funding with Google Ventures, NEA and Madrone Partners, and FinSMEs headlined it the same day "
                 "as Avos's Series A (" + FINSMES_AVOS + "): GV entered at the Series A. The base also carries "
                 "avos-systems as a separate row for the same company."),
 jl.cls("poynt", stage="Series A", stage_src="model", stage_conf="low", entry_date="2014-10",
        rounds=[jl.rnd("2014-10-29", "Series A", None, "Matrix Partners", True, TC_POYNT_A),
                jl.rnd("2015-10-22", "Series B", 28000000, "Oak HC/FT", None, VB_POYNT_B),
                jl.rnd("2018-11-13", "Series C", 100000000, None, None, TC_POYNT_C)],
        note=N + "the firm listed Poynt from its late 2014 capture, so GV was in by then; the only round on record before "
                 "that capture is the launch Series A led by Matrix Partners (TechCrunch, 2014-10-29), and the $133M "
                 "raised by 2018 leaves about $5M before the $28M Series B and the $100M Series C; TechCrunch "
                 "(2018-11-13) names Google Ventures among its backers, so GV entered at the Series A (the firm's "
                 "listing as a bound, model, low)."),
 # ---- Seed, decided for S2A
 jl.cls("ambition", stage="Seed", stage_src="model", stage_conf="low", entry_date="2014", flags=UNC,
        grad="graduated", grad_src="web_verified", grad_cite=BJ_AMBITION_B, grad_conf="medium",
        rounds=[jl.rnd("2014-02", "Seed", None, None, False, TC_AMBITION),
                jl.rnd("2014", "post-YC funding (Google Ventures, SV Angel, Redpoint Ventures)", None, None, True,
                       BI_AMBITION),
                jl.rnd("2018-06-01", "equity ($5.86M sold to 36 investors)", 5858089, None, None, SEC_AMBITION_2018,
                       "filing"),
                jl.rnd("2021-10", "Series B ($15.5M)", 15500000, "Primus Capital", None, BJ_AMBITION_B)],
        note=N + "Business Insider (2014-09-20) says the company, just out of Y Combinator, had raised from Google "
                 "Ventures, SV Angel and Redpoint Ventures; that 2014 money came after the YC-era seed (TechCrunch, "
                 "2014-02-21) and before the $5.86M equity round of June 2018 (its only Form D) and the Series B from "
                 "Primus Capital (Business Journals headline, October 2021; $15.5M per the Times Free Press), so GV "
                 "entered at the seed stage (model, low: no page names GV's round). S2A: the named Series B graduates "
                 "it."),
 jl.cls("signpost", stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=TC_SIGNPOST_2010,
        entry_date="2010-10",
        grad="graduated", grad_src="web_verified", grad_cite=TC_SIGNPOST_B, grad_conf="high",
        rounds=[jl.rnd("2010-02-22", "Seed ($1.05M sold)", 1049999, "Spark Capital", False, SEC_SIGNPOST_2010, "filing"),
                jl.rnd("2010-10", "seed follow-on", None, None, True, TC_SIGNPOST_2010),
                jl.rnd("2012-04-25", "Series A ($3.8M sold)", 3804622, "Spark Capital", None, SEC_SIGNPOST_2012, "filing"),
                jl.rnd("2013-11-19", "Series B", 10000000, "OpenView Venture Partners", None, TC_SIGNPOST_B),
                jl.rnd("2015-04-28", "Series C", 20500000, None, None, TC_SIGNPOST_C),
                jl.rnd("2019-07-09", "late-stage financing", 52000000, "HighBar Partners", None, TC_SIGNPOST_2019)],
        note=N + "TechCrunch (2010-10-20) reports Google Ventures 'taking a stake' in Signpost as 'a follow-on to a $1 "
                 "million seed round' that Spark Capital provided earlier that year (Form D, $1.05M from 2010-02-22); the "
                 "next round is the Series A of April 2012 (Form D, $3.8M; TechCrunch in 2013 refers to 'its Series A "
                 "last year'), so GV's entry is a seed extension: Seed. S2A: the named $10M Series B of November 2013 "
                 "led by OpenView (TechCrunch, 2013-11-19) graduates it, as Spark's row reads."),
 jl.cls("scoutrfp", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TC_SCOUT_SEED,
        entry_date="2015-01-27",
        grad="graduated", grad_src="web_verified", grad_cite=TC_SCOUT_B, grad_conf="high",
        rounds=[jl.rnd("2015-01-27", "Seed", 2750000, "New Enterprise Associates", True, TC_SCOUT_SEED),
                jl.rnd("2016-07-27", "Series A", 9000000, None, None, FINSMES_SCOUT_A),
                jl.rnd("2017-06-07", "Series B", 15500000, "Menlo Ventures", None, TC_SCOUT_B),
                jl.rnd("2019-01-15", "Series C", 33000000, "Scale Venture Partners", None, PRN_SCOUT_C, "company"),
                jl.rnd("2019-11", "Acquisition", 540000000, "Workday", None, PULSE_SCOUT_WORKDAY)],
        note=N + "TechCrunch (2015-01-27): 'The company has raised $2.75 million in seed financing from New Enterprise "
                 "Associates, with participation from Google Ventures and Zapis Capital': GV entered at the seed. S2A: "
                 "the $9M Series A of July 2016 (FinSMEs headline) and the $15.5M Series B led by Menlo (TechCrunch, "
                 "2017-06-07, which says the company 'previously raised about $12 million from NEA and Google Ventures "
                 "(GV)') graduate it."),
 jl.cls("the-orange-chef-co", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=USAT_OC,
        entry_date="2013-11",
        grad="not_graduated", grad_src="web_verified", grad_cite=PRN_OC, grad_conf="high", grad_asof=ASOF,
        surfaces=["firm: the firm's own listing and posts for The Orange Chef Co. -> listed 2014 and 2015 (Andy "
                  "Wheeler); no post names a later round",
                  "formd: EDGAR for Orange Chef Co (CIK 1592389) -> equity from 2013-11-26 ($1.97M sold by 2014-01-23), "
                  "then debt only: $935K from 2014-10-29 and $500K from 2015-06-03; no later priced round",
                  "techcrunch: TechCrunch's own search (Orange Chef) -> the Prep Pad launch (2013-09-11) and a feature "
                  "(2014-10-31); no later round",
                  "googlenews: Google News (Orange Chef with raises, seed, funding, Google Ventures, acquired) -> USA "
                  "Today (2014-03-03) on the seed and PR Newswire (2016-12-22) on Perfect Company buying the Prep Pad IP "
                  "after Yummly acquired the company in 2015; no later round"],
        rounds=[jl.rnd("2013-11", "Seed ($1.2M, co-led by SparkLabs Global Capital and Google Ventures)", 1200000,
                       "SparkLabs Global Capital, Google Ventures", True, USAT_OC),
                jl.rnd("2013-11-26", "Seed (Form D: $1.97M sold of $3.0M by 2014-01-23)", 1971355, None, True,
                       SEC_OC_2013, "filing"),
                jl.rnd("2014-10-29", "debt ($935K sold)", 935000, None, None, SEC_OC_2014, "filing"),
                jl.rnd("2015-06-03", "debt ($500K sold)", 500000, None, None, SEC_OC_2015, "filing"),
                jl.rnd("2015", "Acquisition by Yummly", None, "Yummly", None, PRN_OC, "company")],
        note=N + "USA Today (2014-03-02) says SparkLabs Global Capital 'co-led a $1.2 million seed investment in Orange "
                 "Chef with Google Ventures last November' (the company's Form D shows the equity offering from "
                 "2013-11-26): GV entered at the seed. S2A: not graduated on a cited end. After the seed the company "
                 "filed only debt ($935K from October 2014, $500K from June 2015), and 'Yummly acquired The Orange Chef "
                 "Company in 2015' (Perfect Company's release, 2016-12-22), so the seed was its last priced round."),
 jl.cls("stamped", stage="Seed", stage_src="model", stage_conf="low", entry_date="2011", flags=UNC,
        grad="not_graduated", grad_src="web_verified", grad_cite=TC_STAMPED_YAHOO, grad_conf="high", grad_asof=ASOF,
        surfaces=["firm: the firm's own listing for Stamped -> carried from the 2012 capture with the exit line "
                  "'Acquired by Yahoo!, 2012'; no post names a later round",
                  "formd: EDGAR company search for Stamped -> no Form D by the company",
                  "techcrunch: TechCrunch's own search (Stamped) -> the launch (2011-11-21) and the Yahoo purchase "
                  "(2012-10-25); no later round",
                  "googlenews: Google News (Stamped with raises, seed, funding, Google Ventures) -> Business Insider "
                  "(2012-07-25, the relaunch with celebrity investors, $3M raised to date) and Business Insider "
                  "(2012-10-25, Yahoo's purchase); no Series A or later round",
                  "sibling:bain-capital-ventures: its row for Stamped -> Seed (model), S2A not_graduated"],
        rounds=[jl.rnd("2011", "launch financing (seed-sized)", None, "Bain Capital Ventures, Google Ventures", True,
                       TC_STAMPED_2011),
                jl.rnd("2012-07-25", "unnamed (celebrity investors; $3M raised in total)", None, None, True, GVC_STAMPED),
                jl.rnd("2012-10-25", "Acquisition by Yahoo", None, "Yahoo", None, TC_STAMPED_YAHOO)],
        note=N + "GV was in the launch financing of this 2011 company with Bain Capital Ventures (TechCrunch, 2011-11-21), "
                 "and Global Venturing (2012-07-25) reports GV and Bain backing it again as the July 2012 relaunch took "
                 "it to $3M raised in total (Business Insider the same day); all of its money is seed-sized, so GV "
                 "entered at the seed (model, low: no page names the round), as Bain's row reads. S2A: not graduated on "
                 "a cited end: Yahoo bought Stamped in October 2012 (TechCrunch, 2012-10-25) with no round of $5M or "
                 "more after the seed."),
 jl.cls("ledgerx", stage="Seed", stage_src="model", stage_conf="low", entry_date="2014", flags=UNC,
        grad="graduated", grad_src="web_verified", grad_cite=SEC_LEDGER_2018, grad_conf="medium",
        rounds=[jl.rnd("2013-12-31", "Seed (offering amended to $2M debt; $185K sold by 2014-01-28)", 185000, None, True,
                       SEC_LEDGER_2014, "filing"),
                jl.rnd("2015-08-04", "equity ($20.77M sold to 19 investors by the 2018-04-17 amendment)", 20765154, None,
                       None, SEC_LEDGER_2018, "filing")],
        note=N + "the firm listed LedgerX from its late 2014 capture, so GV was in by then; before that capture the parent "
                 "Ledger Holdings Inc. (CIK 1596252) has one financing on record, the offering begun 2013-12-31 and "
                 "amended in January 2014 to a $2M debt offering, the 2014 round Lightspeed's own card calls the Seed, "
                 "so GV entered at the seed (the firm's listing as a bound, model, low). S2A: graduated; the equity "
                 "offering from 2015-08-04 had sold $20.77M to 19 investors by its April 2018 amendment, above the $5M "
                 "an unnamed later round needs for a 2014 entry. Lightspeed's row reads not graduated without that "
                 "filing."),
 jl.cls("mparticle", stage="Seed", stage_src="model", stage_conf="low", entry_date="2013", flags=UNC,
        grad="graduated", grad_src="web_verified", grad_cite=TC_MPARTICLE_A, grad_conf="high",
        rounds=[jl.rnd("2013-07-19", "Seed (equity; $2.55M sold to 43 investors by 2013-11-01)", 2551063, None, True,
                       SEC_MPARTICLE_2013, "filing"),
                jl.rnd("2014-10-09", "Seed (additional)", 1500000, None, False, TC_MPARTICLE_SEED2),
                jl.rnd("2016-01-13", "Series A", 15000000, "Social Capital", False, TC_MPARTICLE_A),
                jl.rnd("2016-10-13", "Series B", 17500000, "Bain Capital Ventures", None, TC_MPARTICLE_B)],
        note=N + "the firm listed mParticle from its late 2013 capture, so GV was in by then; the company's Form D record "
                 "(CIK 1582826) holds one round before it, the equity round from 2013-07-19 ($2.55M sold to 43 investors "
                 "by 2013-11-01), which TechCrunch's 'additional round of seed funding' (2014-10-09) makes the seed, "
                 "before the named Series A (2016) and Series B (2016): GV entered at the seed (the firm's listing as a "
                 "bound, model, low; AlleyWatch names Google Ventures among its backers). S2A: the $15M Series A led "
                 "by Social Capital (TechCrunch, 2016-01-13) graduates it."),
]
jl.write("s4", L)
