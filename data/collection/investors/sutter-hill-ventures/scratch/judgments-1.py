#!/usr/bin/env python3
"""PRO-77 Sutter Hill Ventures, queue batch 1 (45 rows, all members already: listed or filing).
Run: NQ_TAG=b1 python3 judgments-1.py

Every citation comes from a helper (ARCH, W, NEWS, SEC, FORMD_CITE) or is a URL printed by a
tool run in this session (EDGAR submissions listings, WebSearch results, the Sequoia sibling's
classification row)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, W, NEWS, SEC

N = 1
L = []


def FDC(slug, date):
    """The EDGAR index of the one Form D of `slug` whose first sale is `date`."""
    idx = [i for i, r in enumerate(jl.FORMD_ROUNDS(slug)) if r.get("sale_date") == date]
    if len(idx) != 1:
        raise SystemExit(f"FDC({slug!r}, {date!r}) matched {len(idx)}")
    return jl.FORMD_CITE(slug, idx[0])


def FDR(slug, firm_dates=(), label="Form D, round not named"):
    """The company's Form D sequence as funding_rounds; firm_in_round True on the filings
    that list a Sutter Hill person in tenure."""
    out = []
    for i, r in enumerate(jl.FORMD_ROUNDS(slug)):
        d = r.get("sale_date")
        out.append(rnd(d, label, r.get("offering_usd"), None, True if d in firm_dates else None,
                       jl.FORMD_CITE(slug, i), "filing"))
    return sorted(out, key=lambda x: x["date"] or "")


# ---- URLs printed by tools run in this session (EDGAR listings, WebSearch, sibling rows)
AKSYS_S1 = "https://www.sec.gov/Archives/edgar/data/902600/000095013196002339/0000950131-96-002339.txt"
BV_S1 = "https://www.sec.gov/Archives/edgar/data/920448/000091205796011007/0000912057-96-011007.txt"
CORCEPT_S1 = "https://www.sec.gov/Archives/edgar/data/1088856/000101287001503256/ds1.txt"
HEARME_S1 = "https://www.sec.gov/Archives/edgar/data/1078693/000101287099000539/0001012870-99-000539.txt"
HORIZON_S1 = "https://www.sec.gov/Archives/edgar/data/1492426/000119312510175302/ds1.htm"
ELOY_8K = "https://www.sec.gov/Archives/edgar/data/1094348/000095013701503724/c65139e8-k.txt"
ASTERA_DRS = "https://www.sec.gov/Archives/edgar/data/1736297/000095012323010146/filename1.htm"
ASTERA_424B4 = "https://www.sec.gov/Archives/edgar/data/1736297/000119312524073873/d285484d424b4.htm"
ARTISAN_S1 = "https://www.sec.gov/Archives/edgar/data/1517302/000119312511089694/ds1.htm"
INFOADV_S1 = "https://www.sec.gov/Archives/edgar/data/1047118/000104746997000465/0001047469-97-000465.txt"
OMNICELL_S1 = "https://www.sec.gov/Archives/edgar/data/926326/000091205700019006/0000912057-00-019006.txt"
CARDICA_S1 = "https://www.sec.gov/Archives/edgar/data/1178104/000116923205005200/d65698_s-1.htm"
NVDA_S1A = "https://www.sec.gov/Archives/edgar/data/1045810/000089843099000180/0000898430-99-000180.txt"
EXOGEN_8K = "https://www.sec.gov/Archives/edgar/data/934094/000095013199004510/0000950131-99-004510.txt"
OACIS_14D1 = "https://www.sec.gov/Archives/edgar/data/1011671/000095010399000186/0000950103-99-000186.txt"
NETMOVES_8K = "https://www.sec.gov/Archives/edgar/data/1010677/000095012300001078/0000950123-00-001078.txt"
CLARUS_S1 = "https://www.sec.gov/Archives/edgar/data/913277/000093176398000890/0000931763-98-000890.txt"
APAM_CAP = "https://stockanalysis.com/stocks/apam/market-cap/"
NVDA_CAP = "https://stockanalysis.com/stocks/nvda/market-cap/"
OMCL_CAP = "https://stockanalysis.com/stocks/omcl/market-cap/"
TC_GLASSDOOR = "https://techcrunch.com/2008/10/28/glassdoor-raises-another-65-million-for-company-and-salary-review-community/"
PRN_GLASSDOOR_C = "https://www.prnewswire.com/news-releases/glassdoor-secures-12-million-series-c-round-led-by-battery-ventures-115719744.html"
GV_PLATFORA = "https://globalventuring.com/blog/2011/11/02/platfora-processes-7-2m/"
TC_PLATFORA = "https://techcrunch.com/2011/09/08/andreessen-horowitz-leads-5-7m-round-in-analytics-platform-for-hadoop-data-platfora"
GV_PLATFORA_D = "https://globalventuring.com/blog/2015/12/10/platfora-finds-30m-series-d-answer/"
BW_MERGANSER = ("https://www.businesswire.com/news/home/20150219005154/en/Merganser-Biotech-Inc.-Raises-28-Million"
                "-in-a-Series-A-Financing-to-Develop-Hepcidin-Mimetic-Peptides")
ACQ_NVDA = "https://www.acquiredbriefing.com/p/nvidia-i"
DCV_PINC = "https://www.dcvelocity.com/articles/46325-yard-management-tech-vendor-pinc-lands-significant-private-equity-investment"
KALERIS = "https://kaleris.com/news/kaleris-announces-merge-of-best-in-class-companies-pinc-shipxpress-and-railcarrx/"
PEPRO_RN = "https://peprofessional.com/blog/2015/03/19/court-square-completes-buy-of-research-now/"
GLMX_Q4 = "https://glmx.com/news/2026/glmx-reports-fourth-quarter-2025-activity.html"
BATTERY_GD = "https://www.battery.com/blog/glassdoor-case-study/"

GRAD_LEFT = "Graduation left for the graduation pass."
PRO157 = ("Under the PRO-157 rule (a company incorporated or first listed 3+ years before its first e-filed round "
          "raised earlier) the early band is withheld; prepare missed it because the filing answers "
          "'over five years' instead of giving a year.")

# 1. Aksys
L.append(cls(
    "aksys", status="defunct", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=AKSYS_S1, stage_conf="high", entry_date="1993-04-02",
    country="US", city="Lincolnshire", focus="Healthcare & Bio",
    rounds=[rnd("1993-04-02", "Series A", 1_500_000, None, True, AKSYS_S1, "filing"),
            rnd("1994-04-15", "Series B", 2_400_000, None, True, AKSYS_S1, "filing"),
            rnd("1995-03-07", "Series C", 3_000_000, None, True, AKSYS_S1, "filing"),
            rnd("1995-09-22", "Series D", 4_506_761, None, True, AKSYS_S1, "filing")],
    note="Aksys, home haemodialysis machines (PHD system), Two Marriott Drive, Lincolnshire, Illinois (its 2003 "
         "prospectus); IPO 1996, the firm's 1999 table says public company. The company shut down in February "
         "2007 (Modern Healthcare, 'Dialysis machine firm Aksys shuts down'), with no sale of the business found, "
         "so defunct. The 1996 S-1/A's recent-sales list names 'Sutter Hill Ventures, a California Limited "
         "Partnership' among the buyers of the April 2, 1993 Series A ($1.5M, with Coral Partners and Sand Hill "
         "Financial) and of every later series through the September 1995 Series D, so SHV entered at the Series A."))

# 2. Artisan Partners
L.append(cls(
    "artisan-partners-limited-partnership", status="public", rng="1b_plus", usd=2_900_000_000,
    val_src="web_verified", val_cite=APAM_CAP, asof="2026-09-28",
    stage="undetermined", city="Milwaukee",
    flags=("model_disputes_source",),
    extra={"valuation_range_source": "web_verified", "focus": None},
    rounds=[rnd("1995-01", "Class A limited partnership interests (the initial outside investors)", None, None,
                True, ARTISAN_S1, "filing")],
    note="DISPUTE of the prefilled status 'acquired' (the float layer's reading of a filer whose 2024 float is its "
         "last on disk): Artisan Partners Asset Management trades on the NYSE as APAM, market cap $2.9B on "
         "2026-09-28 (stockanalysis.com), so public, 1b_plus. Membership stands on the evidence D6 asks for: the "
         "firm filed it under Investment Partnerships from 2008, but the 2011 S-1 says the Class A investors, "
         "the initial outside investors in Artisan Partners Holdings, included 'a venture capital fund managed by "
         "Sutter Hill Ventures', so the position is equity in the operating asset manager, not a fund interest. "
         "Tench Coxe sat on the advisory committee from January 1995. The record calls the entry Class A limited "
         "partnership interests and names no round, so the stage is undetermined. Focus is null: a traditional "
         "asset manager fits none of the twelve (outside taxonomy)."))

# 3. Astera Labs
L.append(cls(
    "astera-labs-inc", city="San Jose", city_src="web_verified",
    stage="Series A", stage_src="web_verified", stage_cite=W("Astera Labs"), stage_conf="medium",
    entry_date="2018-03", flags=("stage_disputes_band",), focus="Industrial & Robotics",
    rounds=[rnd("2018-03", "Series A", 8_500_000, None, True, W("Astera Labs"), "press"),
            rnd("2019-11", "Series B", 26_000_003, None, True, ASTERA_DRS, "filing"),
            rnd("2021-08", "Series C", 52_500_000, None, True, ASTERA_424B4, "filing"),
            rnd("2022-05", "Series D", 168_600_000, None, True, ASTERA_424B4, "filing")],
    note="Band check on a public 10b_plus row. The band read the $26M Form D (first sale 2019-11-08) as a Series A, "
         "but the record names that round the Series B: the 2023 DRS calls it the 'November 2019 Series B "
         "Preferred Stock Financing' and shows SHV entities buying Series B in its February 2020 closing, and "
         "Stefan Dyckerhoff joined the board in November 2019 (424B4). Wikipedia's funding history names Sutter "
         "Hill Ventures among the investors of the March 2018 $8.5M Series A, the earliest round a source ties to "
         "SHV, so the label stays Series A on that citation with the entry dated 2018-03. Medium, not high: the "
         "article repeats one investor list verbatim for the A, B and C rounds, and no SHV person is on the March "
         "2018 Form D (directors Mohan, Gajendra, Jankov, Alba); if SHV's first money was the November 2019 Series "
         "B the stage reads Growth. HQ San Jose since June 2025 (Wikipedia; EDGAR business address 2345 North "
         "First Street, San Jose)."))

# 4. Authentic Response
L.append(cls(
    "authentic-response", status="unknown", rng="below_1b",
    stage="undetermined", flags=("stage_disputes_band",), city="New York", city_src="formd_address",
    focus="Media, Gaming & Advertising",
    extra={"entry_date": None},
    rounds=FDR("authentic-response", {"2009-09-02", "2010-08-04"}),
    note="Online market research sample panels. DISPUTE of the Seed band: the firm's own company page says "
         "'Since 1998, Authentic Response has led the market research industry', and a 2008 merger with "
         "PostMasterDirect explains the 2008 incorporation year on the September 2009 Form D, so the $2.1M 2009 "
         "round is not a seed of an 11-year-old business. " + PRO157.replace("prepare missed it because the filing "
         "answers 'over five years' instead of giving a year.", "Here the Form D's 2008 year is the merged "
         "entity's.") + " Greg Sands (SHV, in tenure) is a director on the 2009 and 2010 Form Ds filing from 755 "
         "Page Mill Road; the round SHV entered is not on record. Fate: no source reports a sale or shutdown after "
         "2010 (New York office on the filings), so status unknown."))

# 5. Benu Networks
L.append(cls(
    "benu-networks-inc", status="acquired", rng="below_1b",
    stage="undetermined", city="Burlington", city_src="web_verified", focus="Data Infrastructure",
    rounds=FDR("benu-networks-inc", {"2013-08-05", "2014-10-06", "2015-10-19", "2017-06-19", "2018-07-12"}),
    note="Carrier broadband software (virtual service edge). Ciena announced on 2022-11-22 that it had acquired "
         "Benu Networks, 'headquartered in Burlington, Massachusetts' (WilmerHale's deal note, "
         + NEWS("benu-networks-inc", "WilmerHale Advises Benu") + "), so acquired. Stefan Dyckerhoff (SHV from "
         "October 2012) is a director on every Form D from August 2013 ($5.0M) on; the firm's page says Benu was "
         "founded in 2010, so the 2013 filing is not the company's first round and the band was rightly withheld. "
         "No source names the round SHV entered: undetermined."))

# 6. BroadVision
L.append(cls(
    "broadvision", country="US", city="Redwood City", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=BV_S1, stage_conf="high", entry_date="1993",
    focus="SaaS",
    rounds=[rnd("1993", "Series A", 2_560_000, "Mayfield VII and Sutter Hill Ventures", True, BV_S1, "filing"),
            rnd(None, "Series B", 1_666_666, None, True, BV_S1, "filing"),
            rnd(None, "Series C", 6_007_200, None, True, BV_S1, "filing")],
    note="E-commerce and portal software, Redwood City (Wikipedia; EDGAR address 460 Seaport Court). Acquired "
         "(the prefill; ESW Capital took it private in 2020), so below_1b with no figure. The 1996 S-1/A's Certain "
         "Transactions table shows 'Sutter Hill Ventures, a California Limited Partnership' buying 1,941,974 "
         "Series A shares at $0.60 (the Series A sold from the May 1993 inception, with Mayfield VII), then Series "
         "B and C; David Anderson a director since November 1993. SHV entered at the Series A."))

# 7. Cardica
L.append(cls(
    "cardica-inc", country="US", city="Redwood City", rng="below_1b", stage="undetermined",
    focus="Healthcare & Bio",
    rounds=[rnd("2002-06", "Series D (Guidant Investment Corporation bought 2,590,673 shares)", 10_000_000, None, None, CARDICA_S1, "filing"),
            rnd("2003-08", "Series E (Guidant Investment Corporation bought 851,064 shares)", 4_000_000, None, None, CARDICA_S1, "filing")],
    note="Cardiac surgery staplers (renamed Dextera Surgical in 2016); Chapter 11 in December 2017 and its assets "
         "sold to Aesculap in 2018, so acquired out of insolvency (the prefill). Last address 900 Saginaw Drive, "
         "Redwood City (EDGAR, now Dex Liquidating Co.). The 2005 S-1 shows William Younger (SHV) a director "
         "since August 2000 and SHV entities holding 2,935,561 shares, but names only the Guidant-bought Series D "
         "and E; the series SHV first bought is not on record: undetermined."))

# 8. Celeritek
L.append(cls(
    "celeritek", status="acquired", rng="below_1b", stage="undetermined",
    rounds=[],
    country="US", city="Santa Clara", focus="Industrial & Robotics",
    note="GaAs RF chips and subsystems, Santa Clara; IPO 1995 (before EDGAR prospectuses, so no preferred history "
         "on file). It sold its operating businesses in 2004 and 2005 (defense subsystems to Teledyne, the "
         "semiconductor line to Mimix Broadband) and wound down; its listed shell (CIK 919583) later became "
         "Strasbaugh. An asset sale out of a wind-down reads acquired, which agrees with the Greylock sibling. "
         "Focus Industrial & Robotics (chips), not the sibling's SaaS. The round SHV entered is not on record."))

# 9. ChoiceStream
L.append(cls(
    "choicestream", status="unknown", rng="below_1b", stage="undetermined",
    city="Boston", city_src="formd_address", focus="Media, Gaming & Advertising",
    rounds=FDR("choicestream", {"2011-11-10"}) + [
        rnd("2015-08", "Series C", 14_000_000, None, None,
            NEWS("choicestream", "DSP ChoiceStream Raises $14 Million"), "press")],
    note="Personalisation software that became a demand-side ad platform; Cambridge, later Boston (2015 Form D). "
         "SHV listed it from 2008 and Greg Sands is a director on the November 2011 Form D ($12.2M); the 2015 "
         "$14M round (MediaPost: Series C) lists no SHV person. SHV's entry predates the e-filed rounds and is not "
         "named: undetermined. No source gives the company's fate after 2017, so unknown, as the General "
         "Catalyst sibling also reads."))

# 10. Clarus
L.append(cls(
    "clarus", status="acquired", rng="below_1b", stage="undetermined",
    rounds=[],
    country="US", city="Suwanee", focus="SaaS", flags=("model_disputes_source",),
    note="DISPUTE of the prefilled 'public, $110M' (a float join on CIK 913277, which today files as Clarus Corp, "
         "the Salt Lake City outdoor-gear company). SHV's Clarus is the e-procurement software maker (formerly SQL "
         "Financials, 3950 Johns Creek Court, Suwanee, Georgia in its 1998 S-1/A); it sold that business to Epicor "
         "in 2002 and the cash shell later bought Black Diamond, a different business. Successor-entity ambiguity "
         "reads acquired with no figure, as the Greylock sibling carries. Tench Coxe a director from September "
         "1993; the S-1/A shows SHV holding common stock and names no round for it: undetermined. The Y "
         "Combinator row named Clarus is a different company."))

# 11. Clover
L.append(cls(
    "clover", status="acquired", rng="below_1b", stage="undetermined",
    city="Sunnyvale", focus="Fintech & Payments", flags=("model_disputes_source", "stage_disputes_band"),
    rounds=[rnd("2010-11-01", "first round, not named", 5_500_000, "Sutter Hill Ventures", True,
                W("Clover Network"), "press"),
            rnd("2012-04", "convertible note", 3_000_000, "Sutter Hill Ventures", True, W("Clover Network"),
                "press")],
    note="DISPUTE of the prefilled 'defunct', a name join to another Clover (the Accel and Y Combinator rows "
         "named Clover are different companies): Clover Network, the payments and point-of-sale company, was "
         "acquired by First Data on 2012-12-28 (Wikipedia: Clover Network), HQ Sunnyvale. An SHV incubation (D3): "
         "Mike and Leonard Speiser are directors and executive officers on the first Form D. SHV led the $5.5M "
         "first round on 2010-11-01 with Andreessen Horowitz and angels, then a $3M convertible note in April "
         "2012. D3 labels an incubation's first round as the record names it and reads undetermined where it "
         "does not; no source names the $5.5M round, so the Seed band is replaced by undetermined and the row "
         "leaves the S2A cohort."))

# 12. Connection Engine
L.append(cls(
    "connection-engine", status="unknown", rng="below_1b", entry_date="2010-06-25",
    city="Boulder", city_src="formd_address", focus="SaaS",
    rounds=FDR("connection-engine", {"2010-06-25", "2011-06-24"}),
    note="Consumer-data marketing platform, Boulder. Entry date moved to 2010-06-25: Greg Sands (SHV, in tenure) "
         "is a director on the first Form D ($1.2M, June 2010) as well as on the June 2011 one the layer read, "
         "and the company was incorporated in 2010, so the Seed band stands on the first round. No source gives "
         "its fate and its domain no longer resolves: status unknown. " + GRAD_LEFT))

# 13. Corcept Therapeutics
L.append(cls(
    "corcept-therapeutics", city="Redwood City", city_src="web_verified",
    stage="Series A", stage_src="web_verified", stage_cite=CORCEPT_S1, stage_conf="high", entry_date="1999-05",
    focus="Healthcare & Bio",
    rounds=[rnd("1999-05", "Series A", 656_382, None, True, CORCEPT_S1, "filing"),
            rnd("2000-01", "Series B", 1_199_997, None, True, CORCEPT_S1, "filing"),
            rnd("2001-05", "Series BB", None, None, True, CORCEPT_S1, "filing"),
            rnd("2001-06", "Series C", None, None, True, CORCEPT_S1, "filing")],
    note="Band check on a public 1b_plus row (no band was set). The 2001 S-1's preferred-financing table shows "
         "'Sutter Hill Ventures and affiliates' buying Series A (dated May 1999), Series B (January 2000), Series "
         "BB (May 2001) and Series C (June 2001); Leonard Baker a director since 1999. Entry: the May 1999 Series "
         "A, as the firm's 1999 table ('Private Company') agrees. HQ Redwood City (EDGAR business address 101 "
         "Redwood Shores Parkway)."))

# 14. Data Domain
L.append(cls(
    "data-domain", status="acquired", rng="below_1b", city="Santa Clara",
    stage="Growth", stage_src="web_verified", stage_cite=W("Dell EMC Data Domain"), stage_conf="high",
    entry_date="2003", focus="Data Infrastructure",
    rounds=[rnd("2002", "Series A", 9_300_000, "NEA and Greylock", None, W("Dell EMC Data Domain"), "press"),
            rnd("2003", "Series B", 17_000_000, "Sutter Hill Ventures", True, W("Dell EMC Data Domain"), "press")],
    note="Deduplicating backup storage, Santa Clara; IPO 2007, bought by EMC for $2.4B in 2009, so acquired "
         "(agrees with the Greylock and IVP siblings). Wikipedia: NEA and Greylock led the 2002 $9.3M Series A and "
         "'Sutter Hill Ventures led its $17 million Series B funding round in 2003'; Ron Bernal (then an SHV "
         "venture partner) joined the board in December 2003 (2007 S-1). A Series B entry is Growth."))

# 15. Drobo (Data Robotics)
L.append(cls(
    "data-robotics", status="defunct", rng="below_1b", stage="undetermined",
    city="San Jose", focus="Data Infrastructure",
    rounds=FDR("data-robotics", {"2009-10-15"}),
    note="Drobo storage appliances (Data Robotics until 2011), founded in San Jose in 2005; merged with Connected "
         "Data in 2013, placed under StorCentric in 2018; StorCentric filed Chapter 11 in June 2022 and moved to "
         "Chapter 7 in April 2023 with no buyer, and Drobo support ended in January 2023 (Wikipedia: Drobo). A "
         "bankruptcy with no sale reads defunct, aligned with the Greylock sibling. Ron Bernal (c/o SHV, 755 Page "
         "Mill Road) is a director on the October 2009 $10M Form D, four years after founding; the round SHV "
         "entered is not named: undetermined. Storage is Data Infrastructure."))

# 16. Demandbase
L.append(cls(
    "demandbase", status="private", rng="below_1b", city="San Francisco", city_src="formd_address",
    stage="undetermined", flags=("stage_disputes_band",), focus="SaaS",
    extra={"entry_date": None},
    rounds=FDR("demandbase", {"2013-03-22", "2014-03-20"}) + [
        rnd("2023-02", "financing (not named)", 175_000_000, None, None,
            NEWS("demandbase", "Demandbase to power product development"), "press")],
    note="B2B account-based marketing software, San Francisco. DISPUTE of the Series A band: the 2013 and 2014 "
         "Form Ds say the company was incorporated over five years before (Demandbase dates from 2006), and SHV "
         "listed it from 2012. " + PRO157 + " Greg Sands is on the 2013 and 2014 filings after his 2012 move to "
         "Costanoa, so those seats date SHV's entry no better; the round SHV entered is not on record. Private; "
         "the February 2023 $175M financing disclosed no valuation and no priced round at $1B or more was found, "
         "so below_1b (vendor ARR and valuation estimates not used, Rule A)."))

# 17. Drais Pharmaceuticals
L.append(cls(
    "drais-pharmaceuticals-inc", status="unknown", rng="below_1b", stage="undetermined",
    country="US", country_src="formd_address", city="Bridgewater", city_src="formd_address",
    focus="Healthcare & Bio",
    rounds=FDR("drais-pharmaceuticals-inc", {"2007-12-14"}),
    note="Specialty pharmaceutical company, Bridgewater, New Jersey, incorporated 2007; Jeff Bird (SHV) is a "
         "director on its December 2007 Form D (amount not stated) and Horizon's 2010 S-1 lists Drais among his "
         "boards. No source names the round or gives the company's fate: stage undetermined, status unknown."))

# 18. e-Rewards
L.append(cls(
    "e-rewards", status="acquired", rng="below_1b", stage="undetermined", city="Plano",
    focus="Media, Gaming & Advertising",
    rounds=FDR("e-rewards"),
    note="Online research panels, Plano, Texas; after buying Research Now plc it took the Research Now name "
         "worldwide in 2010 (MrWeb); Court Square Capital completed a buyout of Research Now Group in March 2015 "
         "and merged it with SSI in 2017 (now Dynata), so acquired. SHV's 1999 table lists e-Rewards as a private "
         "company; a David Anderson is a director on its 2009 to 2013 Form Ds but files c/o the company, so those "
         "filings do not by themselves place SHV (buyout: " + PEPRO_RN + "). The 1999 entry round is not named: "
         "undetermined."))

# 19. Exogen
L.append(cls(
    "exogen", status="acquired", rng="below_1b", stage="undetermined",
    rounds=[],
    country="US", city="Piscataway", focus="Healthcare & Bio",
    note="Ultrasound bone-healing stimulator (SAFHS), Piscataway, New Jersey; IPO 1995. Smith & Nephew agreed to "
         "buy it on 1999-07-25 (Exogen 8-K, " + EXOGEN_8K + ") and completed a tender offer that summer, so "
         "acquired; the firm's 1999 table still said public company. No EDGAR prospectus names SHV's round: "
         "undetermined."))

# 20. FaxSav
L.append(cls(
    "faxsav", status="acquired", rng="below_1b", stage="undetermined",
    rounds=[],
    country="US", city="Edison", focus="Data Infrastructure",
    note="Internet fax delivery, Edison, New Jersey (renamed NetMoves); Mail.com's merger subsidiary merged into "
         "NetMoves on 2000-02-08 (NetMoves 8-K), so acquired, as the Battery and Menlo siblings read. SHV held "
         "shares at the 1996 IPO but the S-1 names no round for it: undetermined."))

# 21. Forty Seven
L.append(cls(
    "forty-seven-inc", rng="below_1b", city="Menlo Park",
    stage="Series A", stage_src="web_verified",
    stage_cite=NEWS("forty-seven-inc", "Completes $75M Series A"), stage_conf="high", entry_date="2015-11-23",
    flags=("stage_disputes_band",), focus="Healthcare & Bio",
    rounds=[rnd("2016-02-24", "Series A", 75_000_000, "Lightspeed Venture Partners and Sutter Hill Ventures", True,
                NEWS("forty-seven-inc", "Completes $75M Series A"), "company"),
            rnd("2017-10-17", "Series B", 75_000_000, None, None,
                NEWS("forty-seven-inc", "Completes $75 Million Series B"), "company")],
    note="DISPUTE of the Growth band (it read the $74.8M size): the company's release of 2016-02-24 says 'The "
         "Series A financing was led by Lightspeed Venture Partners and Sutter Hill Ventures with participation "
         "from Clarus Ventures and GV'; the Form D's first sale 2015-11-23 dates that round. SHV entered at the "
         "Series A (Lightspeed's own earlier 2015 seed card is Lightspeed's entry, not SHV's). Gilead bought the "
         "company for $4.9B in 2020, so acquired, below_1b. HQ Menlo Park (1490 O'Brien Drive on the later "
         "filings), as the Lightspeed sibling reads."))

# 22. Glassdoor
L.append(cls(
    "glassdoor", status="acquired", rng="below_1b", city="San Francisco", city_src="web_verified",
    stage="Growth", stage_src="web_verified", stage_cite=TC_GLASSDOOR, stage_conf="high", entry_date="2008-10",
    flags=("stage_disputes_band",), focus="Consumer & Marketplaces",
    rounds=[rnd("2008-03", "Series A (Benchmark Capital participated)", None, None, None, TC_GLASSDOOR, "press"),
            rnd("2008-10", "Series B", 6_500_000, "Sutter Hill Ventures", True, TC_GLASSDOOR, "press"),
            rnd("2011-01", "Series C", 12_000_000, "Battery Ventures", None, PRN_GLASSDOOR_C, "company")],
    note="DISPUTE of the Seed band: TechCrunch (2008-10-28) reports the $6.5M round as a Series B led by Sutter "
         "Hill Ventures, Jim White joining the board, after Benchmark's Series A that March; Battery's own case "
         "study (" + BATTERY_GD + ") and the company's release call the 2011 $12M round the Series C. SHV's "
         "entry is the October 2008 Series B, Growth. Recruit bought Glassdoor for $1.2B in 2018 and it merged "
         "into Indeed on 2026-07-01, so acquired. City: the headquarters moved from Mill Valley to San Francisco "
         "in 2019 (San Francisco Chronicle, 2019-05-24 and 2022-04-28), fresher than the Battery sibling's "
         "Sausalito, the 2008 filing address."))

# 23. Global Liquid Markets (GLMX)
L.append(cls(
    "global-liquid-markets", status="private", rng="below_1b", stage="undetermined",
    city="Palo Alto", city_src="formd_address", focus="Fintech & Payments",
    extra={"entry_date": None},
    rounds=FDR("global-liquid-markets", {"2017-04-27"}),
    note="GLMX, an electronic trading platform for securities financing (repo and securities lending), founded "
         "2010, Palo Alto, CEO Glenn Havlicek; still operating (quarterly activity reports into 2026, " + GLMX_Q4 +
         "). SHV listed it from 2013; Andy Sheehan is a director on the April 2017 $5.3M Form D, which says the "
         "company was incorporated over five years earlier, so that filing is not SHV's entry (John Pasquesi on "
         "the same filing is Otter Capital, external under D1). The round SHV entered is not on record. Private, "
         "no priced round at $1B or more found: below_1b."))

# 24. Guardian Analytics
L.append(cls(
    "guardian-analytics", status="acquired", rng="below_1b", city="Mountain View", city_src="web_verified",
    stage="undetermined", flags=("stage_disputes_band",), focus="Security",
    extra={"entry_date": None},
    rounds=FDR("guardian-analytics", {"2011-02-11"}),
    note="Fraud prevention for banks and credit unions, 'based in Mountain View, CA' (its 2017 release, "
         + NEWS("guardian-analytics", "Appoints Prashanth Shetty") + "). NICE Actimize bought it in 2020 and "
         "renamed the product Xceed; guardiananalytics.com now redirects to NICE Actimize's Xceed page: acquired. "
         "DISPUTE of the Series A band: the February 2011 Form D ($14.1M, Greg Sands a director) says the company "
         "was incorporated over five years before. " + PRO157 + " The round SHV entered is not on record."))

# 25. HearMe
L.append(cls(
    "hearme", status="defunct", rng="below_1b", country="US", city="Mountain View",
    stage="Growth", stage_src="web_verified", stage_cite=HEARME_S1, stage_conf="high", entry_date="1995-08",
    focus="Media, Gaming & Advertising",
    rounds=[rnd("1995-01", "Series A", 1_400_000, None, None, HEARME_S1, "filing"),
            rnd("1995-08", "Series B", 4_535_043, None, True, HEARME_S1, "filing"),
            rnd("1996-04", "Series C", 11_869_082, None, True, HEARME_S1, "filing"),
            rnd("1997-07", "Series D", 16_799_994, None, True, HEARME_S1, "filing"),
            rnd("1999-01", "Series E", 20_033_020, None, True, HEARME_S1, "filing")],
    note="HearMe (Mpath Interactive), internet voice and game communities, Mountain View; IPO 1999, wound down and "
         "liquidated in 2001, so defunct as the Accel and IVP siblings read. The 1999 S-1 sold the January 1995 "
         "Series A to IVP and Accel only, and the Series B (August 1995 and January 1996, $2.07 a share) to 'IVP, "
         "Accel Partners, Sutter Hill Ventures and its affiliates'; SHV also bought C, D and E. Entry: the Series "
         "B, Growth."))

# 26. Helix
L.append(cls(
    "helix", status="private", rng="below_1b", city="San Mateo", city_src="web_verified",
    focus="Healthcare & Bio",
    rounds=[rnd("2015-07-15", "formation round, not named", 185_000_000, None, True,
                NEWS("helix", "Mayo Clinic joins Illumina"), "press"),
            rnd("2018-03", "Series B (first close of a planned $200M)", None, None, None,
                NEWS("helix", "first close of planned $200M series B"), "press"),
            rnd("2021-06-03", "Series C", 50_000_000,
                "Warburg Pincus, DFJ Growth, Kleiner Perkins, Mayo Clinic and Temasek", None,
                NEWS("helix", "Helix Announces $50 Million Series C"), "company")],
    note="Population genomics and clinical testing, San Mateo (the 2021 Series C release is datelined San Mateo; "
         "Inside Precision Medicine: 'Based in San Mateo, CA'). Illumina, Warburg Pincus and SHV formed Helix in "
         "2015 (Mayo Clinic News Network), Jeff Bird a director. Still private; the June 2021 $50M Series C "
         "disclosed no valuation and no priced round at $1B or more was found: below_1b. Stage left as banded "
         "(Growth, read off the $185M formation Form D); the later rounds are named Series B (2018) and Series C "
         "(2021), which points to the formation round being the Series A, but no source I could read names it. "
         "The a16z row named Helix is an unresolved, likely different company."))

# 27. Horizon Pharma
L.append(cls(
    "horizon-pharma-inc", city="Deerfield", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=HORIZON_S1, stage_conf="high", entry_date="2005-10",
    focus="Healthcare & Bio",
    rounds=[rnd("2005-10", "Series A", 6_000_000, None, True, HORIZON_S1, "filing"),
            rnd("2006-11", "Series B", 14_900_000, None, True, HORIZON_S1, "filing"),
            rnd("2007-07", "Series C", 29_900_000, None, True, HORIZON_S1, "filing"),
            rnd("2009-12", "Series D", 25_800_000, None, True, HORIZON_S1, "filing")],
    note="Horizon Pharma USA (founded 2005 as Horizon Therapeutics, Inc.), later Horizon Therapeutics plc, bought "
         "by Amgen in 2023: acquired, below_1b. The 2010 S-1 lists the preferred rounds (Series A October 2005 "
         "$6.0M, B November 2006, C July 2007, D December 2009) and a related-party table in which 'Sutter Hill "
         "Ventures, L.P.' holds shares of Series A, B, C and D (and no Special Preferred), so SHV bought into the "
         "October 2005 Series A; Jeff Bird joined the board in July 2007. City: the plc was domiciled in Dublin, "
         "Ireland, but its operating base was Deerfield, Illinois (520 Lake Cook Road on the Form Ds), consistent "
         "with the US country the entry-time filing gives."))

# 28. Inflection
L.append(cls(
    "inflection", status="acquired", rng="below_1b", city="San Francisco", city_src="web_verified",
    focus="Consumer & Marketplaces",
    note="Inflection, public-records and background-check company (Archives.com, sold to Ancestry in 2012; "
         "PeopleSmart; GoodHire). Checkr bought it for about $400M in April 2022 (" +
         NEWS("inflection", "Checkr scoops up background check") + "), so acquired. inflection.com now shows "
         "Inflection Risk Solutions, LLC at 1 Montgomery Street, San Francisco; its 2010 Form D gave Palo Alto. "
         "Stage left as banded (Growth, the July 2010 $30.3M round with Greg Sands). The Greylock row named "
         "Inflection is Inflection AI, a different company."))

# 29. Information Advantage
L.append(cls(
    "information-advantage", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Eden Prairie", focus="Data Infrastructure",
    rounds=[rnd("1994", "Series A", 2_500_000, None, None, INFOADV_S1, "filing"),
            rnd("1995-06", "Series B", 7_165_026, None, True, INFOADV_S1, "filing"),
            rnd("1996-03", "Series C", 4_923_220, None, True, INFOADV_S1, "filing"),
            rnd("1997-02", "Series D", 6_999_960, None, True, INFOADV_S1, "filing")],
    note="OLAP and data-warehouse software, Eden Prairie, Minnesota; IPO 1997, acquired by Sterling Software in "
         "1999 (the firm's own 1999 outcome line), as the Lightspeed and Menlo siblings read. The 1997 S-1 shows "
         "SHV entities buying 863,469 shares of the June 1995 Series B (with Menlo the largest buyers) and more "
         "in C and D, but its table covers purchases only since September 1994 and the Series A (fiscal 1995, "
         "$2.5M) is not attributed, so whether SHV entered at the A or the B is not on record: undetermined."))

# 30. Intacct
L.append(cls(
    "intacct", status="acquired", rng="below_1b", city="San Jose",
    stage="undetermined", flags=("stage_disputes_band",), focus="SaaS",
    extra={"entry_date": None},
    rounds=FDR("intacct", {"2010-06-18"}),
    note="Cloud financial management software, San Jose; Sage bought it for $850M in 2017: acquired, as the "
         "Battery sibling reads. DISPUTE of the Seed band: the June 2010 Form D ($3.0M, Gregory Sands filing c/o "
         "SHV) says Intacct was incorporated over five years before (it dates from 1999), and SHV listed it from "
         "2008. " + PRO157 + " SHV's entry round is not on record; the row is no Seed entry, so no graduation."))

# 31. Kineto Wireless
L.append(cls(
    "kineto-wireless-inc", status="acquired", rng="below_1b", city="Milpitas", city_src="formd_address",
    stage="undetermined", flags=("stage_disputes_band",), focus="Data Infrastructure",
    extra={"entry_date": None},
    rounds=FDR("kineto-wireless-inc", {"2010-02-11", "2010-11-04", "2011-04-26"}),
    note="Wi-Fi calling (UMA) software for mobile carriers, Milpitas; Taqua acquired Kineto in September 2014 (" +
         NEWS("kineto-wireless-inc", "Taqua Acquires Kineto") + "): acquired. DISPUTE of the Series A band: the "
         "February 2010 Form D (Tench Coxe filing c/o SHV) says the company was incorporated over five years "
         "before; Wikipedia names SHV among its venture backers with Venrock, Oak and SeaPoint. " + PRO157 +
         " The round SHV entered is not on record."))

# 32. LifeSize
L.append(cls(
    "lifesize-communications", status="acquired", rng="below_1b", stage="undetermined",
    city="Austin", city_src="formd_address", focus="SaaS",
    rounds=FDR("lifesize-communications", {"2015-12-28"}),
    note="HD video conferencing, Austin. SHV's company page existed by the 2008-2009 crawl, before Logitech bought "
         "LifeSize in December 2009; Logitech spun Lifesize out in January 2016 with $17.5M, Andy Sheehan (SHV) "
         "a director on that Form D, a re-entry after the 2009 exit. Lifesize filed for bankruptcy in May 2023 "
         "and Enghouse Systems bought its assets (" + NEWS("lifesize-communications",
         "Lifesize Files for Bankruptcy") + "): acquired either way. Neither SHV round is named in a source I "
         "could read: undetermined."))

# 33. LinkSmart
L.append(cls(
    "linksmart", status="unknown", rng="below_1b",
    stage="Series A", stage_src="formd_structural", stage_cite=FDC("linksmart", "2010-06-30"),
    stage_conf="medium", entry_date="2010-06-30",
    city="Boulder", city_src="formd_address", focus="Media, Gaming & Advertising",
    rounds=FDR("linksmart", {"2010-06-30", "2013-04-25"}),
    note="Text-link analytics and monetisation for web publishers, Boulder. SHV's entry is the June 2010 $4.1M "
         "round, not the 2013 filing the layer read: Greg Sands (SHV managing director until his 2012 move to "
         "Costanoa) first appears on the June 2010 Form D, one filing after a $0.5M October 2009 round with "
         "Foundry Group's Seth Levine; one earlier filing and an amount inside the Series A band read Series A "
         "(COLLECTION.md s6 structural rule), and the 2013 seat post-dates Sands's SHV tenure. No source gives "
         "LinkSmart's fate and its domain no longer resolves: status unknown."))

# 34. Mattersight (eLoyalty)
L.append(cls(
    "mattersight", city="Chicago", city_src="formd_address", rng="below_1b",
    stage="Growth", stage_src="web_verified", stage_cite=ELOY_8K, stage_conf="high", entry_date="2001-12",
    focus="SaaS",
    rounds=[rnd("2001-12", "Series B convertible preferred (private placement)", 25_000_000,
                "Technology Crossover Ventures and Sutter Hill Ventures", True, ELOY_8K, "filing")],
    note="Mattersight is eLoyalty renamed in 2011; NICE bought it in 2018 (the prefill's acquired), below_1b. "
         "SHV's first money: eLoyalty's 8-K of 2001-09-24 announces a share purchase agreement with funds managed "
         "by Technology Crossover Ventures and by Sutter Hill Ventures to buy up to $25.0M of Series B "
         "convertible preferred in a private placement, closed in December 2001 after the stockholder vote; "
         "Tench Coxe then joined the board. A Series B entry is Growth. The base carries this company twice: the "
         "eloyalty row is the same company."))

# 35. Merganser Biotech
L.append(cls(
    "merganser-biotech", status="unknown", rng="below_1b", city="King of Prussia", city_src="formd_address",
    focus="Healthcare & Bio",
    rounds=[rnd("2015-02", "Series A", 28_000_000, "Novartis Venture Fund", True, BW_MERGANSER, "company")],
    note="Hepcidin mimetic peptides for iron-overload disease. Its February 2015 release: a $28M Series A led by "
         "the Novartis Venture Fund with Frazier Healthcare, Sutter Hill Ventures and Osage University Partners, "
         "which agrees with the Series A band (entry 2015-02-13). It began its first clinical trial in February "
         "2016; no later source gives its fate and its domain now redirects to an unrelated site, so status "
         "unknown."))

# 36. Molecular Devices
L.append(cls(
    "molecular-devices", status="acquired", rng="below_1b", stage="undetermined",
    rounds=[],
    city="San Jose", focus="Healthcare & Bio",
    note="Microplate readers and life-science instruments, founded 1983; IPO 1995; MDS bought it in March 2007 and "
         "Danaher took it over in 2010 (Wikipedia: Molecular Devices), so acquired; it operates as a Danaher "
         "business headquartered in San Jose. David Anderson (SHV) a director; the round SHV entered is not on "
         "record (its IPO predates EDGAR prospectuses): undetermined."))

# 37. Nexxo Financial
L.append(cls(
    "nexxo-financial-corporation", status="defunct", rng="below_1b", city="San Bruno", city_src="formd_address",
    stage="undetermined", flags=("stage_disputes_band",), focus="Fintech & Payments",
    extra={"entry_date": None},
    rounds=FDR("nexxo-financial-corporation", {"2010-03-29"}),
    note="Self-service financial kiosks and remittances for the unbanked, San Bruno; wound down, as the Menlo "
         "sibling reads (Form Ds stop in 2012). DISPUTE of the Series A band: the March 2010 Form D ($10.7M, Greg "
         "Sands a director) says the company was incorporated over five years before (Menlo lists it from "
         "2005). " + PRO157 + " The round SHV entered is not on record."))

# 38. NuGEN
L.append(cls(
    "nugen", city="San Carlos", city_src="formd_address", rng="below_1b",
    stage="undetermined", flags=("stage_disputes_band",), focus="Healthcare & Bio",
    extra={"entry_date": None},
    rounds=FDR("nugen", {"2010-03-22", "2011-08-09", "2014-09-12"}),
    note="Nucleic acid amplification and library preparation kits, San Carlos (the firm's page and the Form Ds); "
         "Tecan bought it in 2018 (the prefill's acquired), below_1b. DISPUTE of the Seed band: the firm's own "
         "page says 'Founded in 2000' and the March 2010 Form D ($1.5M, Jeff Bird filing c/o SHV) says the "
         "company was incorporated over five years before; SHV listed it from 2008. " + PRO157 + " SHV's entry "
         "round is not on record; no Seed entry, so no graduation."))

# 39. NVIDIA
L.append(cls(
    "nvidia", country="US", city="Santa Clara",
    stage="Series A", stage_src="model", stage_conf="medium", entry_date="1993-06",
    rng="100b_plus", usd=5_440_000_000_000, val_src="web_verified", val_cite=NVDA_CAP, asof="2026-08-13",
    extra={"valuation_range_source": "web_verified"}, focus="Industrial & Robotics",
    rounds=[rnd("1993", "first venture round (name not given in the source)", 2_000_000,
                "Sequoia Capital and Sutter Hill Ventures", True, ACQ_NVDA, "press")],
    note="Model stage on a named deal: SHV and Sequoia put $2M into NVIDIA's first venture round in 1993 at a $6M "
         "post-money valuation (Acquired Briefing), the company's first venture round, recorded as its Series A in "
         "the Sequoia book too; Tench Coxe a director since June 1993 (1999 prospectus, " + NVDA_S1A + "). No "
         "filing names the series, hence model at medium. Mark aligned to the Sequoia sibling's cited cap "
         "($5.44T on 2026-08-13), fresher than the 2025 float. HQ Santa Clara."))

# 40. Oacis Healthcare
L.append(cls(
    "oacis-healthcare-systems", status="acquired", rng="below_1b", stage="undetermined",
    rounds=[],
    country="US", city="Greenbrae", focus="Healthcare & Bio",
    note="Clinical information software, Greenbrae, California (EDGAR address 100 Drakes Landing Road); SAIC "
         "bought it through a tender offer by its Oscar Acquisition Corporation in March 1999 (SC 14D-1, " +
         OACIS_14D1 + "), matching the firm's 1999 outcome line 'Acquired by SAIC'. The round SHV entered is not "
         "on record: undetermined."))

# 41. Omnicell
L.append(cls(
    "omnicell", city="Fort Worth", city_src="web_verified", stage="undetermined",
    rng="1b_plus", usd=1_700_000_000, val_src="web_verified", val_cite=OMCL_CAP, asof="2026-08-11",
    extra={"valuation_range_source": "web_verified"}, focus="Healthcare & Bio",
    rounds=[rnd(None, "Series A", 120_000, None, None, OMNICELL_S1, "filing"),
            rnd(None, "Series B", 120_000, None, None, OMNICELL_S1, "filing"),
            rnd(None, "Series C", 1_014_000, None, None, OMNICELL_S1, "filing"),
            rnd(None, "Series D", 1_412_000, None, None, OMNICELL_S1, "filing"),
            rnd(None, "Series H", 13_203_000, None, None, OMNICELL_S1, "filing")],
    note="Band check on a public 1b_plus row (no band was set). William Younger (SHV) a director since the "
         "September 1992 founding; the 2000 S-1 lists preferred Series A to H (Series A only $120K, B $120K, C "
         "$1.0M, D $1.4M, H $13.2M) and SHV as a holder, but not which series SHV first bought, so undetermined "
         "(the filing gives no dates for the series). HQ Fort Worth "
         "(Wikipedia; EDGAR address 4220 North Freeway), as the Sequoia sibling reads. Mark aligned to the "
         "Sequoia sibling's cited cap ($1.7B on 2026-08-11), fresher than the 2025 float."))

# 42. OpenDNS
L.append(cls(
    "opendns", city="San Francisco", city_src="formd_address", rng="below_1b",
    stage="Growth", stage_src="web_verified", stage_cite=W("OpenDNS"), stage_conf="medium", entry_date="2013-02-22",
    focus="Security",
    rounds=[rnd("2013-02", "Series B", 9_267_710, None, True, W("OpenDNS"), "press"),
            rnd("2014-05", "Series C", 35_000_000, None, True, W("OpenDNS"), "press")],
    note="DNS-layer security, San Francisco; Cisco bought it for $635M in 2015: acquired, below_1b. Stefan "
         "Dyckerhoff (SHV from October 2012) is a director on the $9.3M Form D whose first sale is 2013-02-22; "
         "Wikipedia dates a Series B to February 2013 and names SHV among the 'previous backers' in the May 2014 "
         "$35M Series C. The band was withheld (founded 2005, first filing 2010); SHV's entry is that 2013 Series "
         "B, Growth. Medium: the article dates the Series B without naming its investors."))

# 43. PINC
L.append(cls(
    "pinc", status="acquired", rng="below_1b", city="Alameda", city_src="formd_address",
    stage="undetermined", flags=("stage_disputes_band",), focus="SaaS",
    extra={"entry_date": None},
    rounds=FDR("pinc", {"2009-09-29", "2013-04-08"}) + [
        rnd("2020-06", "private equity investment (Accel-KKR)", None, "Accel-KKR", None, DCV_PINC, "press")],
    note="Sensor and RFID yard management for logistics, Alameda. Accel-KKR made a significant private equity "
         "investment in June 2020 (DC Velocity), added Wabtec's shipper TMS and RailcarRx, and merged the three "
         "into Kaleris in March 2021 (" + KALERIS + "): acquired. DISPUTE of the Seed band: the September 2009 "
         "Form D ($5.8M, Tench Coxe a director) says PINC was incorporated over five years before, and SHV listed "
         "it from 2008. " + PRO157 + " SHV's entry round is not on record; no Seed entry, so no graduation."))

# 44. Platfora
L.append(cls(
    "platfora", status="acquired", rng="below_1b", city="San Mateo", city_src="formd_address",
    stage="Series A", stage_src="web_verified", stage_cite=GV_PLATFORA, stage_conf="high", entry_date="2011-08-25",
    flags=("stage_disputes_band",), focus="Data Infrastructure",
    rounds=[rnd("2011-09", "Series A", 7_200_000, "Andreessen Horowitz", True, GV_PLATFORA, "press"),
            rnd("2012-10-31", "Form D, round not named", 19_999_998, None, None,
                FDC("platfora", "2012-10-31"), "filing"),
            rnd("2015-12", "Series D", 30_000_000, "HSBC and Harmony Partners", None, GV_PLATFORA_D, "press")],
    note="DISPUTE of the Seed band: Global Venturing (2011-11-02) calls the $5.7M September 2011 round, closed at "
         "$7.2M, a Series A (Andreessen Horowitz led, In-Q-Tel joined; TechCrunch 2011-09-08 reports the a16z-led "
         "$5.7M round) and notes the amended filing was signed by SHV's Mike Speiser, who is a director on that "
         "Form D (first sale 2011-08-25). SHV entered at the Series A, not a seed, so no graduation. Workday "
         "bought Platfora in 2016: acquired, below_1b. San Mateo."))

# 45. Portola
L.append(cls(
    "portola", city="South San Francisco", rng="below_1b", focus="Healthcare & Bio",
    note="Cardiovascular and haematology drugs, South San Francisco; Alexion bought it in 2020 (about $1.4B), so "
         "acquired, below_1b. Stage left as banded (Growth, the July 2008 $60.1M round with Jeff Bird filing c/o "
         "SHV); the 2013 S-1 lists Series A to C preferred but not which series SHV bought first."))

if __name__ == "__main__":
    assert len({x["slug"] for x in L}) == 45, len({x["slug"] for x in L})
    jl.write(f"batch-{N:03d}", L)
