#!/usr/bin/env python3
"""Adversarial A/B pass (COLLECTION.md s7), PRO-77 Sutter Hill Ventures: the visible slice
(every member that is public or $1B+), plus the membership questions on aac, pacific-biosciences,
avid-technology and thermawave-inc. Run: NQ_TAG=ab1 python3 judgments-ab1.py

Rows closed on agreement write no line. Every URL below was fetched by this pass (curl or WebSearch)
or is read from the row's own record."""
import json
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, ARCH, FORMD_CITE

_C = json.loads((Path(__file__).resolve().parent.parent / "companies" / "classification.json").read_text())
ASOF = "2026-09-28"
WV = {"valuation_range_source": "web_verified"}

# Quote pages fetched 2026-09-28 (each prints "... as of September 28, 2026").
CAP = {
    "nvda": "https://stockanalysis.com/stocks/nvda/market-cap/",
    "alab": "https://stockanalysis.com/stocks/alab/market-cap/",
    "cort": "https://stockanalysis.com/stocks/cort/market-cap/",
    "omcl": "https://stockanalysis.com/stocks/omcl/market-cap/",
    "pacb": "https://stockanalysis.com/stocks/pacb/market-cap/",
}

# NVIDIA's S-1/A of 1999-01-20 (the IPO registration), read from the row's own note.
NVDA_S1A = re.search(r"https://www\.sec\.gov/Archives/edgar/data/1045810/\S+?\.txt", _C["nvidia"]["note"]).group(0)
# Snowflake: SHV's own Form 3 at the IPO (reporting owner Sutter Hill Ventures, CIK 879051) and the S-1.
SNOW_F3 = "https://www.sec.gov/Archives/edgar/data/1640147/000122520820011602/0001225208-20-011602-index.htm"
SNOW_S1 = "https://www.sec.gov/Archives/edgar/data/1640147/000162828020013010/snowflakes-1.htm"
# Astera Labs: the 2023 DRS (already the row's Series B source) and SHV's Form 3 at the IPO.
ALAB_DRS = "https://www.sec.gov/Archives/edgar/data/1736297/000095012323010146/filename1.htm"
ALAB_F3 = "https://www.sec.gov/Archives/edgar/data/1736297/000141588924008694/0001415889-24-008694-index.htm"
# PacBio: the company's own release (Business Wire, 2009-08-12) and the 2010 S-1.
PACB_PR = "https://www.biospace.com/article/releases/pacific-biosciences-raises-additional-68-million-in-financing-/"
PACB_S1 = "https://www.sec.gov/Archives/edgar/data/1299130/000119312510189512/ds1.htm"
# GRAIL's 10-Q for the quarter to 2026-06-30 (filed 2026-08-06).
GRAL_10Q = "https://www.sec.gov/Archives/edgar/data/1699031/000162828026054307/gral-20260630.htm"
# IDEXX's 8-K of 1998-10-15 on the Blue Ridge Pharmaceuticals purchase.
IDXX_8K = "https://www.sec.gov/Archives/edgar/data/874716/000095013598005456/0000950135-98-005456-index.htm"
# AAC's 2005 HKEX prospectus: corporate history and substantial shareholders chapters.
AAC_HIST = "https://www1.hkexnews.hk/listedco/listconews/sehk/2005/0728/02018/ewp113.pdf"
AAC_SUBS = "https://www1.hkexnews.hk/listedco/listconews/sehk/2005/0728/02018/ewp118.pdf"

L = []

# ---- 1. nvidia: the Series A is now cited; mark refreshed (fresher than the Sequoia sibling's).
L.append(cls(
    "nvidia", rng="100b_plus", usd=5_530_000_000_000, val_src="web_verified", val_cite=CAP["nvda"],
    asof=ASOF, extra=WV,
    stage="Series A", stage_src="web_verified", stage_cite=NVDA_S1A, stage_conf="high", entry_date="1993-06",
    rounds=[rnd("1993", "Series A", 2_151_500, None, True, NVDA_S1A, "filing"),
            rnd("1994", "Series B", 4_303_496, None, None, NVDA_S1A, "filing"),
            rnd("1995", "Series B (additional sale)", 750_001, None, None, NVDA_S1A, "filing"),
            rnd("1995", "Series C", 5_002_500, None, None, NVDA_S1A, "filing"),
            rnd("1997-08", "Series D", 7_568_151, None, None, NVDA_S1A, "filing")],
    note="A/B pass 2026-09-28: stage now cited. NVIDIA's S-1/A of 1999-01-20 says 'In 1993, the Company sold "
         "4,303,000 shares of Series A preferred stock at $0.50 per share' (about $2.15M, the $2M first round SHV and "
         "Sequoia funded), and Tench Coxe of SHV has been a director since June 1993; Series B followed in 1994, so the "
         "round SHV entered in 1993 is the Series A (web_verified, high). Mark: market cap $5.53T on 2026-09-28 "
         "(stockanalysis), fresher than the Sequoia sibling's $5.44T of 2026-08-13; band unchanged."))

# ---- 2. snowflake-inc: SHV's fund held Series Seed, so the entry is the Seed and the Series A graduates it.
_snow_rounds = [dict(r) for r in _C["snowflake-inc"]["funding_rounds"]]
for r in _snow_rounds:
    if r["round"] == "Series Seed":
        r["firm_in_round"] = True
L.append(cls(
    "snowflake-inc",
    stage="Seed", stage_src="web_verified", stage_cite=SNOW_F3, stage_conf="high", entry_date="2012-08-24",
    grad="graduated", grad_src="web_verified", grad_cite=SNOW_S1, grad_conf="high", grad_asof=ASOF,
    rounds=_snow_rounds,
    note="A/B pass 2026-09-28, open point settled: SHV's fund bought the Series Seed. Its own Form 3 at the IPO "
         "(reporting owner Sutter Hill Ventures, filed 2020-09-15) lists 2,121,351 shares of Series Seed Preferred "
         "Stock held directly, and five partners' Form 3s list Series Seed in their trusts beside it (the D2 "
         "co-investment pattern). The S-1 shows 4,410,736 Seed shares at $0.1719, so the partnership held about 48% of "
         "the round, sold from 2012-08-24 while Speiser was CEO. Entry: Seed (web_verified, high), stage still disputes "
         "the Pre-Seed band. Graduated: the S-1 names the later Series A (14,240,500 shares at $0.3476, first sale "
         "2013-03-08), with Speiser's seat elected by the Series A holders as SHV's designee."))

# ---- 3. astera-labs-inc: cap cited (gap 1); the entry is the November 2019 Series B, not the Series A.
_alab_old = {r["round"]: r for r in _C["astera-labs-inc"]["funding_rounds"]}
L.append(cls(
    "astera-labs-inc", status="public", rng="10b_plus", usd=60_950_000_000, val_src="web_verified",
    val_cite=CAP["alab"], asof=ASOF, extra=WV,
    stage="Growth", stage_src="web_verified", stage_cite=ALAB_DRS, stage_conf="medium", entry_date="2019-11",
    rounds=[rnd("2018-03-21", "Series A", 8_500_000, None, None, FORMD_CITE("astera-labs-inc", 1), "filing"),
            rnd("2019-11-08", "Series B", 26_000_003, None, True, ALAB_DRS, "filing"),
            rnd("2021-08", "Series C", 52_500_000, None, True, ALAB_DRS, "filing"),
            rnd("2022-05", "Series D", 168_600_000, None, True, _alab_old["Series D"]["source"], "filing")],
    note="A/B pass 2026-09-28. Mark: market cap $60.95B on 2026-09-28 (stockanalysis), 10b_plus, replacing the "
         "uncited 2025 float. Stage corrected Series A to Growth: SHV's Form 3 at the IPO (2024-03-19) shows the "
         "partnership holding 14,957,606 Series B shares against 9,672 Series A shares, about $967 at the Series A's "
         "$0.10 issue price, a token block and not a Series A investment; the DRS names the 'November 2019 Series B "
         "Preferred Stock Financing', lists SHV's purchases in it and in the C and D, and dates Stefan Dyckerhoff's "
         "seat to November 2019. Wikipedia's investor list, repeated for the A, B and C, does not hold against the "
         "filings. Entry: Series B, November 2019 (web_verified, medium; still disputes the Series A band). "
         "SHV Form 3: " + ALAB_F3))

# ---- 4. corcept-therapeutics: cap cited (gap 1); the band moves up.
L.append(cls(
    "corcept-therapeutics", status="public", rng="10b_plus", usd=12_490_000_000, val_src="web_verified",
    val_cite=CAP["cort"], asof=ASOF, extra=WV,
    note="A/B pass 2026-09-28: market cap $12.49B on 2026-09-28 (stockanalysis) replaces the 2025 float ($6.1B) as "
         "the mark, so the band moves from 1b_plus to 10b_plus. Stage (Series A, May 1999, the 2001 S-1) and HQ "
         "Redwood City (EDGAR business address) confirmed."))

# ---- 5. omnicell: mark refreshed to the quote page of the day; band unchanged.
L.append(cls(
    "omnicell", rng="1b_plus", usd=1_540_000_000, val_src="web_verified", val_cite=CAP["omcl"], asof=ASOF,
    extra=WV,
    note="A/B pass 2026-09-28: market cap $1.54B on 2026-09-28 (stockanalysis), fresher than the Sequoia sibling's "
         "$1.7B of 2026-08-11; band unchanged. HQ Fort Worth confirmed (EDGAR business address)."))

# ---- 6. grail: HQ moved to Sunnyvale.
L.append(cls(
    "grail", city="Sunnyvale", city_src="web_verified",
    note="A/B pass 2026-09-28: HQ corrected Menlo Park to Sunnyvale. GRAIL's 10-Q for the quarter to 2026-06-30 "
         "says it leased 'new corporate headquarters in Sunnyvale, California' (lease commenced June 2026); EDGAR's "
         "business address and insiders' Form 4s of 2026-09-23 give 250 S. Mathilda Avenue, Suite 100, Sunnyvale. "
         + GRAL_10Q))

# ---- 7. pacific-biosciences: pre-IPO entry found (question 5), so it stays; stage Growth.
L.append(cls(
    "pacific-biosciences", status="public", rng="below_1b", usd=531_520_000, val_src="web_verified",
    val_cite=CAP["pacb"], asof=ASOF, extra=WV,
    stage="Growth", stage_src="web_verified", stage_cite=PACB_PR, stage_conf="high", entry_date="2009",
    rounds=[rnd("2006-12", "Series D", 50_000_000, None, None, PACB_S1, "filing"),
            rnd("2008", "Series E", 119_800_000, None, None, PACB_S1, "filing"),
            rnd("2009", "Series E (2009 closings)", 68_000_000, None, True, PACB_PR, "company"),
            rnd("2010-06", "Series F", 108_847_917, None, None, PACB_S1, "filing")],
    note="A/B pass 2026-09-28, pre-IPO entry found: PacBio's own release of 2009-08-12 (Business Wire) announces "
         "an additional $68M financing and says 'Sutter Hill Ventures joins the list of the company's institutional "
         "investors'; the 2010 S-1 names that money Series E ('the net receipt of $68.0 million from our sale of "
         "Series E convertible preferred stock' in 2009, the series sold July 2008 to July 2009 at $7.00). The IPO "
         "was October 2010, so T3 does not bite. Entry: Series E, 2009, Growth (web_verified, high). Market cap "
         "$531.52M on 2026-09-28 (stockanalysis), below_1b. HQ Menlo Park confirmed (EDGAR)."))

# ---- 8. aac: no post-IPO purchase on record (question 4); stays a member, stage undetermined.
L.append(cls(
    "aac",
    rounds=[rnd("2004-03", "Series A Preferred (subscribed by Chengwei AAC)", None, "Chengwei AAC", None,
                AAC_HIST, "filing"),
            rnd("2004-11", "Series B Preferred (November and December 2004 closings)", None, None, None,
                AAC_HIST, "filing")],
    note="A/B pass 2026-09-28 (the T3 question): no post-IPO purchase is on record, so the row stays. AAC's 2005 "
         "HKEX prospectus names no Sutter Hill entity: the outside money before the August 2005 listing was Chengwei "
         "AAC (Series A Preferred, March 2004; owned 54.76% by Chengwei Ventures Fund I and 45.24% by 26 unnamed "
         "holders) and Series B Preferred sold to financial investors in November and December 2004. SHV was an LP of "
         "Chengwei and its regular co-investor (Yoqoo 2005: SHV, Farallon and Chengwei), and the firm's AAC page "
         "describes the company as it stood before the listing (operations in China, the US and Germany; the "
         "prospectus has Taiwan and Sweden still being set up), which reads as a pre-IPO co-investment beside "
         "Chengwei, route and round unnamed, so the stage stays undetermined. If SHV held AAC only through its "
         "Chengwei fund interest, D6 would take the row out; flagged for Erik. " + AAC_SUBS))

# ---- 9. idexx-laboratories-inc: sale consideration for Blue Ridge Pharmaceuticals (a Pass B finding).
L.append(verdict(
    "idexx-laboratories-inc", "not_member",
    "Sale consideration (COLLECTION.md s1, Erik 2026-09-22): IDEXX bought Blue Ridge Pharmaceuticals on "
    "1998-10-01 for cash, notes, warrants on 805,519 IDEXX shares allocated among the Blue Ridge stockholders, and "
    "up to 1,240,875 contingent IDEXX shares, and its 8-K's stock purchase agreement names Sutter Hill Ventures, a "
    "California Limited Partnership, and Sutter Hill Associates as Blue Ridge stockholders. The firm's 1999 table "
    "lists Blue Ridge ('Acquired by IDEXX') beside IDEXX ('Public company'); IDEXX is one of only two acquirers the "
    "table also lists as holdings (Avid is the other). No record ties SHV to IDEXX's own financing: its 1997 10-K "
    "and proxy do not name Sutter Hill, and press on IDEXX's founding names Venrock. The investment is Blue Ridge "
    "Pharmaceuticals (its own row, blue-ridge-pharmaceuticals). Medium: an early IDEXX round before its 1991 IPO "
    "cannot be excluded from the filings on EDGAR.",
    ec="web", conf="medium", cite=IDXX_8K))

# ---- 10. avid-technology: sale consideration for Digidesign (question 6).
L.append(verdict(
    "avid-technology", "not_member",
    "Sale consideration (COLLECTION.md s1, Erik 2026-09-22): the firm's 1999 table lists Digidesign ('Acquired by "
    "Avid') and Avid ('Public company'); Avid bought Digidesign, public since December 1993, in an all-stock merger "
    "in January 1995 (about $200M), so SHV's Digidesign shares became Avid shares. The same table's only other "
    "acquirer listed as a holding, IDEXX, is proven consideration (IDEXX's 1998 8-K names SHV as a Blue Ridge "
    "stockholder paid in IDEXX warrants and shares), so the table's acquirer rows record consideration, not "
    "investments. No record ties SHV to an Avid financing: Avid's 1996 10-K and 1997 proxy do not name Sutter Hill, "
    "and its 1993 IPO prospectus predates EDGAR. The investment is Digidesign (its own row, digidesign). Medium: a "
    "pre-IPO Avid round cannot be excluded without that prospectus.",
    ec="site_listing", conf="medium", cite=ARCH("avid-technology", 1999)))

if __name__ == "__main__":
    jl.write("ab-001", L)
