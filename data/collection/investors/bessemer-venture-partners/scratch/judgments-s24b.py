"""Second pass s24, file b: rows first seen 1998 to 2014 (queue/s2-4.json). Only rows that change."""
import judge_lib as jl
from judge_lib import cls, verdict, rnd, ARCH, W, FTS

FP, WV = "first_party", "web_verified"
BVP = "Bessemer Venture Partners"

# SEC documents, each read through secget (the index URLs were printed by the EDGAR listing query, the others by
# the full-text sweep or search).
REG_S1 = "https://www.sec.gov/Archives/edgar/data/1091284/000095011600001718/0000950116-00-001718-index.htm"
VALI_S1 = "https://www.sec.gov/Archives/edgar/data/1114040/000101287000003956/0001012870-00-003956-index.htm"
YODLE_S1 = "https://www.sec.gov/Archives/edgar/data/1382605/000119312514262256/d721498ds1.htm"
ARBIOS_10K = "https://www.sec.gov/Archives/edgar/data/1138862/000114420405009260/v014935_10ksb.htm"
WINC_1A = FTS("Winc", "1-A")
assert WINC_1A.endswith("tv525510_partiiandiii.htm"), WINC_1A
# TechCrunch articles found through TechCrunch's own search and read.
TC_INVOLVER = "https://techcrunch.com/2010/10/14/involver-closes-8-million-series-c-for-its-social-media-marketing-platform/"
TC_KUPIVIP = "https://techcrunch.com/2011/04/14/kupivip-secures-55m-funding-to-become-the-amazon-of-russia/"
TC_QWILT_2011 = "https://techcrunch.com/2011/10/19/accel-redpoint-put-24m-into-network-video-infrastructure-startup-qwilt/"
TC_QWILT_2014 = "https://techcrunch.com/2014/01/30/qwilt-live-video/"
TC_WANDERA = "https://techcrunch.com/2013/04/10/wandera-nabs-7m-from-bessemer-to-give-enterprises-a-way-to-control-mobile-data-use-using-saas/"
TC_CLEARSLIDE = "https://techcrunch.com/2014/02/27/clearslide-raises-50m-from-the-socialcapital-partnership-greylock-to-help-make-sales-presentations-more-effective/"
TC_SCRATCH = "https://techcrunch.com/2015/07/14/scratch-an-e-commerce-app-that-lets-you-text-requests-to-expert-shoppers-raises-3-6-million/"
TC_BILLSHRINK = "https://techcrunch.com/2010/05/28/billshrink-ceo-peter-pham-leaves-to-become-an-eir-at-trinity-ventures/"
TC_FLATWORLD = "https://techcrunch.com/2014/01/29/with-9m-from-bessemer-open-textbook-pioneer-flat-world-looks-for-new-life-in-personalized-learning/"
BILLSHRINK_ROUNDS = [rnd(None, "Series B", 8000000, "Trinity Ventures", None, TC_BILLSHRINK, "press")]

L = []

L.append(cls("register-com", stage="Series A", stage_src=WV, stage_cite=REG_S1, stage_conf="high",
             entry_date="1999-06",
             rounds=[rnd("1999-03", "Exchangeable Preferred", 2999998, "Palisade Private Partnership", False, REG_S1, "filing"),
                     rnd("1999-05", "common stock sold to Staples", 6999996, "Staples", False, REG_S1, "filing"),
                     rnd("1999-06", "Series A Convertible Preferred", 16101562, None, True, REG_S1, "filing")],
             note="Register.com's S-1 of July 2000 (Part II, recent sales) lists Bessemer Venture Partners IV L.P. and "
                  "Bessec Ventures IV L.P. among the buyers of the Series A Convertible Preferred sold in June and "
                  "July 1999 at $3.43 a share; the firm's own text says David Cowan invested in 1999. Entry at the "
                  "Series A; the date is corrected to June 1999 (the 1998 on later listings is the January 1 "
                  "placeholder rendered one year early)."))

L.append(cls("valicert", stage="Growth", stage_src="model", stage_conf="medium",
             rounds=[rnd("1998-05-06", "Series B", 6204001, None, None, VALI_S1, "filing"),
                     rnd("1999-07-21", "Series C", 22965659, None, None, VALI_S1, "filing")],
             note="Model, medium: the firm's own investment date is 1998-05-04 and ValiCert's S-1 of 2000 records the "
                  "Series B financing on 1998-05-06 (3.28M shares at $1.89), after the junior and senior Series A "
                  "classes, so the entry is read as the Series B of May 1998 (Growth). The filing does not name "
                  "Bessemer, which held under 5% and had no director."))

L.append(cls("circe-biomedical", status="defunct",
             note="Status settled: Arbios Systems' 10-KSB for 2004 says Circe Biomedical ceased its operations in "
                  "2003 and that Arbios bought most of its remaining bioartificial liver assets in April 2004 ("
                  + ARBIOS_10K + "). The business ended before the asset purchase, so defunct."))

L.append(cls("octave-communications", city="Nashua",
             note="City added: Nashua, New Hampshire, where Octave Communications was based before Voyant bought it "
                  "(from memory)."))

L.append(cls("mobilian", city="Hillsboro",
             note="City corrected to Hillsboro, Oregon, where Mobilian was based when Intel bought it in 2003 (from "
                  "memory); the earlier Research Triangle Park was a mistake."))

L.append(verdict("argnor", "not_member",
                 "Fund-shaped entry: the firm's own description says Argnor is a specialized early-stage investment "
                 "fund focused on wireless opportunities in Scandinavia, so it is another manager's fund, not an "
                 "operating company (decisions.md D7).", cite=ARCH("argnor")))

L.append(cls("trinet", entry_date="2000",
             note="Entry date added: the firm's 2000 site gives 2000 as its investment year (David Cowan's deal). No "
                  "source read names the round, so the stage stays undetermined."))

L.append(cls("buyerzone-com", city="Waltham",
             note="City added: Waltham, Massachusetts, BuyerZone's base when Reed Business Information bought it in "
                  "2007 (from memory)."))

L.append(cls("kajeet",
             rounds=[rnd("2007-09", "Series B", 36800000, None, None, W("Kajeet"), "press")],
             note="Second pass: Wikipedia records a $36.8M Series B in September 2007 and a new investment from MWP "
                  "Growth Capital in October 2024 (still private). The firm's 2005 entry (as Integrated Mobile) came "
                  "in an earlier round that no source read names, so the stage stays undetermined."))

L.append(cls("yodle", stage="Series A", stage_src=WV, stage_cite=YODLE_S1, stage_conf="medium",
             rounds=[rnd("2006-11", "Series A", 3098000, None, True, YODLE_S1, "filing")],
             note="Yodle's S-1 of July 2014 dates its Series A preferred November 2006 ($3.1M at $0.1444 a share) and "
                  "says Rob Stavis of Bessemer first joined the board in November 2006; the firm's own investment "
                  "date is 2006-10-04. The company was incorporated in March 2005 as Natpal and the Series A is its "
                  "first preferred series, so the entry is read as the Series A."))

L.append(cls("shriram-epc", status="public",
             note="Status settled: the company renamed itself SEPC Limited in March 2022 and trades on the NSE "
                  "(stockanalysis.com company profile). Market cap INR 9.94B on 2026-10-06; INR 9.94B @ ECB "
                  "2026-10-06 (INR/EUR 108.6615, EUR/USD 1.1269) = $103.1M, so below $1B."))

L.append(cls("billshrink", status="acquired", country="US", city="Redwood City", clear=["country_unknown"],
             rounds=BILLSHRINK_ROUNDS,
             note="Same company as the truaxis row: BillShrink renamed itself Truaxis and MasterCard bought it in "
                  "September 2012 (TechCrunch, 2012-09-06; the firm's own Truaxis listing). Redwood City, California "
                  "from memory. TechCrunch (2010-05-28) says Trinity Ventures led the $8M Series B, and in 2012 that "
                  "the company raised $9M in all from Trinity and Bessemer; the round Bessemer entered in 2007 is "
                  "not named, so the stage stays undetermined."))

L.append(cls("truaxis", city="Redwood City", rounds=BILLSHRINK_ROUNDS,
             note="City corrected to Redwood City, California, where BillShrink was based (from memory). TechCrunch "
                  "(2010-05-28) says Trinity Ventures led the $8M Series B, and (2012-09-06) that the company raised "
                  "$9M in all from Trinity and Bessemer; the 2007 round Bessemer entered is not named. The billshrink "
                  "row is the same company under its earlier name."))

L.append(cls("ganesh-housing",
             note="Second pass: the company was incorporated as a public limited company in 1991 and its shares "
                  "trade on the BSE and NSE (IIFL and stockanalysis.com profiles), but a web search and Google News "
                  "found no report of the June 2008 Bessemer transaction, so whether it was an allotment in the "
                  "listed company (T3) or a stake in a project subsidiary is still open. Kept as listed."))

L.append(cls("powergenix", status="acquired",
             note="Status settled: PowerGenix merged with EnSite Power in 2016 to form ZincFive (Wikipedia, "
                  "ZincFive), which still operates and raised a Series F in December 2025; a merger into a successor "
                  "reads acquired. No source read names the round Bessemer entered in 2008."))

L.append(cls("activ-financial-services", status="acquired",
             note="Status settled: Options Technology of Belfast paid an undisclosed sum to acquire Activ Financial "
                  "(The Irish News, 2021-10-20). No source read names the round behind the firm's 2009-12-31 date."))

L.append(cls("ind-barath-power-infra",
             note="Second pass, headlines only: Livemint (2014-12-01) has the company reviving IPO plans, so it "
                  "never listed; later coverage is of an insolvency sale of a plant unit (Business Standard, "
                  "2019-07-01) and a CBI loan-fraud case (2020 to 2022). No source read says whether the holding "
                  "company itself is in liquidation, so the status stays unknown."))

L.append(cls("involver", stage="Growth", stage_src=WV, stage_cite=TC_INVOLVER, stage_conf="high",
             rounds=[rnd("2010-10-14", "Series C", 8000000, BVP, True, TC_INVOLVER, "press")],
             note="TechCrunch (2010-10-14): Involver closed an $8M Series C led by Bessemer Venture Partners, with "
                  "existing investors Western Technology Investment and Cervin Ventures also in; Bessemer was the new "
                  "investor, so its entry is the Series C (Growth). The firm's own date is 2010-09-22."))

L.append(cls("sagence", stage="Growth", stage_src="model", stage_conf="medium", city="Washington",
             rounds=[rnd("2011-01", "second round ($15M)", 15000000, None, None, W("FlatWorld"), "press"),
                     rnd("2014-01-29", "$9.5M round", 9500000, BVP, True, TC_FLATWORLD, "press")],
             note="Inferred identity: Sagence is the competency-based education business of Flat World Education "
                  "under the name it took after the textbook business was sold in late 2016; the firm gives it the "
                  "same investment date (2010-12-21) as its flat-world-knowledge row, and TechCrunch (2014-01-29) "
                  "has Bessemer leading Flat World's $9.5M round for that platform. So this row and "
                  "flat-world-knowledge look like one company. Model, medium: Bessemer entered at Flat World's $15M "
                  "round of January 2011 (Wikipedia), its second after the $8M first round and announced as a "
                  "Series B, so Growth. Washington is where Flat World was based from 2013 (from memory). What "
                  "became of Sagence was not found, so the status stays unknown."))

L.append(cls("kupivip", stage="Growth", stage_src=WV, stage_cite=TC_KUPIVIP, stage_conf="high",
             rounds=[rnd("2011-04-14", "third round", 55000000, None, True, TC_KUPIVIP, "press")],
             note="TechCrunch (2011-04-14): KupiVIP landed $55M in third-round funding with three new investors, "
                  "Balderton Capital, Bessemer Venture Partners and Russia Partners, joining Accel and Mangrove. A "
                  "third round reads Growth, as the Accel and Balderton rows do."))

L.append(cls("clearslide", stage="Growth", stage_src="model", stage_conf="medium",
             rounds=[rnd("2012-08", "Series B", 28000000, None, None, W("ClearSlide"), "press"),
                     rnd("2014-02-27", "Series C", 50000000, "The Social+Capital Partnership", True, TC_CLEARSLIDE, "press")],
             note="Model, medium: the firm's own investment date is 2012-08-10, the month ClearSlide raised its $28M "
                  "Series B (Wikipedia), and TechCrunch (2014-02-27) lists Bessemer among the current investors "
                  "joining the $50M Series C. No page read names Bessemer in the Series B itself; the entry is read "
                  "as that round, so Growth."))

L.append(cls("wandera", status="acquired", stage="Series A", stage_src=WV, stage_cite=TC_WANDERA, stage_conf="high",
             flags=["stage_disputes_band"],
             rounds=[rnd("2012", "Seed (angels)", None, None, False, TC_WANDERA, "press"),
                     rnd("2013-04-10", "Series A", 7000000, BVP, True, TC_WANDERA, "press")],
             note="TechCrunch (2013-04-10): Wandera closed $7M, a Series A that came entirely from Bessemer Venture "
                  "Partners, after a seed from angels the year before. That is the $7.05M Form D of March 2013, so "
                  "the entry is the Series A and the Form D layer's Seed reading is disputed. Status filled: "
                  "acquired by Jamf in 2021 (the firm's listing)."))

L.append(cls("qwilt", stage="Growth", stage_src=WV, stage_cite=TC_QWILT_2014, stage_conf="medium",
             rounds=[rnd("2011-10-19", "first two rounds, announced together", 24000000, None, False, TC_QWILT_2011, "press"),
                     rnd("2013", "third round (total reaches $40M)", None, None, True, TC_QWILT_2014, "press")],
             note="TechCrunch (2011-10-19): Qwilt had raised $24M in two rounds from Accel, Redpoint, Crescent Point "
                  "and others, without Bessemer; TechCrunch (2014-01-30): $40M raised from investors that include "
                  "Bessemer Venture Partners, Accel, Redpoint and Marker. The firm's own date is 2013-05-31, so "
                  "Bessemer entered in the round after the first two, which reads Growth; neither page names the "
                  "round (recalled as a $16M Series C)."))

L.append(cls("winc", stage="Series A", stage_src=WV, stage_cite=WINC_1A, stage_conf="high",
             rounds=[rnd("2013", "Series Seed", 3218995, None, False, WINC_1A, "filing"),
                     rnd("2014", "Series A", 8372863, None, True, WINC_1A, "filing")],
             note="Winc's 2019 offering circular: Series Seed preferred was sold in 2013 (CrossCut the largest "
                  "holder, the Bessemer funds not among the 5% holders) and Series A preferred in 2014 for $8.4M, of "
                  "which the Bessemer funds hold 72% and whose board seat Kent Bennett fills; the firm's own "
                  "investment date is 2014-04-25. Entry at the Series A. The club-w row is the same company (a "
                  "merge is already on file)."))

L.append(cls("scratch", stage="Seed", stage_src=WV, stage_cite=TC_SCRATCH, stage_conf="high", city="Boston",
             city_src="web_verified",
             rounds=[rnd("2015-07-14", "Seed", 3600000, BVP, True, TC_SCRATCH, "press")],
             note="TechCrunch (2015-07-14): Scratch raised $3.6M in seed funding in a round led by Bessemer Venture "
                  "Partners, with NextView, Red Swan and Aspiration Growth, announced at launch; the firm's own "
                  "investment date is 2014-09-11, a month after the founding. The same article puts the 14-person "
                  "team in Boston, so the city is corrected from New York. No report of a later round, a sale or a "
                  "shutdown was found, so the status stays unknown. Graduation left for the graduation pass."))

jl.write("s24b", L)
