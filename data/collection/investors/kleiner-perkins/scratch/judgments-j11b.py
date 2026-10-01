"""PRO-99 Kleiner Perkins, judge j11, batch 22."""
import judge_lib as jl
from judge_lib import verdict, cls, rnd

FA = "formd_adjudicated"
L = []
DUP = ["identity_conflated", "duplicate"]


def nm(slug, basis, conf="high"):
    L.append(verdict(slug, "not_member", basis, ec=FA, conf=conf))


S1_GERON = "https://www.sec.gov/Archives/edgar/data/886744/0000891618-96-000869.txt"
FD_CROSS = "https://www.sec.gov/Archives/edgar/data/1468215/000146821509000001/0001468215-09-000001-index.htm"

# ================= not_member
nm("culture-amp-pty-ltd", "Form D name match only: Ilya Fushman's 2017 seat is his Index Ventures seat (he joined Kleiner "
   "Perkins from Index in March 2018), and no KP fund is named in a Culture Amp round. The company is the same as the "
   "cultureamp row, which the live site dates to 2016, the year of the partner's Index investment, so that listing needs the "
   "partner-carried check (D3, D5).", conf="medium")
nm("cytospar-inc", "Form D name match only: the Mark Allen on the 2022 filing sits a decade after the firm's Mark Allen "
   "appears on its roster (2010-2012); nothing names Kleiner Perkins in a round (D5 seat dating).")
nm("denbury-resources-inc", "Form D name match on a homonym: Mark Allen is an executive officer of Denbury Resources, a listed "
   "oil producer whose 2009 Form D is the company's own offering, not a venture round (T3); not a Kleiner Perkins position.")
nm("dosh-holdings-inc", "Form D name match only: Chi-Hua Chien's 2017-2018 seat is his Goodwater Capital seat (D5: Goodwater "
   "from 2014); nothing names Kleiner Perkins in a round.")
nm("earli-inc", "Form D name match only: Cyriac Roeding is Earli's co-founder and executive officer (2021), a decade after his "
   "Kleiner Perkins entrepreneur-in-residence years; no listing, KP vehicle or press names the firm in an Earli round.")
nm("egenesis-inc", "Form D name match only: Isaac Ciechanover's 2021 seat falls nine years after his Kleiner Perkins years "
   "(2010-2012); nothing names the firm in a round (D5 seat dating).")
nm("elastic-projects-inc", "Form D name match only: Aileen Lee's 2017 seat is her Cowboy Ventures seat (D5: Cowboy from 2012); "
   "nothing names Kleiner Perkins in a round.")
nm("elevian-inc", "Form D name match only: the Mark Allen on the 2020-2021 filings is the company's executive officer, years "
   "after the firm's Mark Allen appears on its roster (2010-2012); nothing names Kleiner Perkins in a round.")
nm("enachip-inc", "Form D name match only: a Mark Allen named as promoter on a 2021 filing, outside the firm's Mark Allen's "
   "roster years (2010-2012); nothing names Kleiner Perkins in a round.")
nm("endra-life-sciences-inc", "Form D name match on a homonym: David Wells is an executive officer of ENDRA Life Sciences, a "
   "listed company (placements from 2018 are public-market purchases, T3); nothing names Kleiner Perkins.")
nm("enviro-clean-group-llc", "Form D name match only: a Matt Murphy on the 2014 filing of a cleaning-services LLC; nothing shows "
   "it is the firm's partner acting for a fund and no listing, KP vehicle or press names Kleiner Perkins in a round.")
nm("eshares-inc", "Form D name match only: Matt Murphy's 2019-2021 seat on eShares (Carta) is his Menlo Ventures seat (he had "
   "left Kleiner Perkins for Menlo); nothing names Kleiner Perkins in a round (D5 seat dating).")
nm("estia-inc", "Form D name match only: a Matt Murphy named as promoter in 2019-2020, when the firm's Matt Murphy was at Menlo "
   "Ventures; nothing names Kleiner Perkins in a round (D5).")
nm("exaeris-water-innovations-llc", "Form D name match only: a Mark Allen named as promoter in 2018, outside the firm's Mark "
   "Allen's roster years (2010-2012); nothing names Kleiner Perkins in a round.")
nm("fabric-of-truth-inc", "Form D name match only: Tina Ju is named as executive officer, director and promoter of this Santa "
   "Clara company in 2024, after the KPCB China funds' investing years; no listing, KP or KPCB China vehicle or press names "
   "the firm in a round (X1, D5).", conf="medium")
nm("feals-inc", "Form D name match only: Matt Murphy's 2020 seat falls in his Menlo Ventures years; nothing names Kleiner "
   "Perkins in a round (D5 seat dating).")
nm("firehydrant-inc", "Form D name match only: Matt Murphy's 2021 seat is his Menlo Ventures seat (the Menlo sibling row holds "
   "FireHydrant's Series A); nothing names Kleiner Perkins in a round (D5).")
nm("fleetsmith-inc", "Form D name match only: Ilya Fushman's 2016 seat is his Index Ventures seat (he joined Kleiner Perkins in "
   "March 2018); nothing names Kleiner Perkins in a round (D5 seat dating).")
nm("flyte-center-inc", "Form D name match on a homonym: the Mark Allen on the 2014 filing is the company's executive officer; "
   "nothing names Kleiner Perkins in a round.")
nm("fms-ena-home-llc", "Form D name match on a homonym: a Fresenius Medical Care dialysis-clinic LLC whose director David Wells "
   "is a Fresenius officer; not a venture company and not a Kleiner Perkins position.")
nm("fog-pharmaceuticals-inc", "Form D name match only: the related person is Weiqing Zhou, the company's executive officer, not "
   "the roster's Wei Zhou; no listing, KP or KPCB China vehicle or press names the firm in a round.")
nm("fresenius-medical-care-morrisville-llc", "Form D name match on a homonym: a Fresenius Medical Care dialysis-clinic LLC whose "
   "director David Wells is a Fresenius officer; not a venture company and not a Kleiner Perkins position.")
nm("fresenius-medical-care-rock-quarry-llc", "Form D name match on a homonym: a Fresenius Medical Care dialysis-clinic LLC whose "
   "director David Wells is a Fresenius officer; not a venture company and not a Kleiner Perkins position.")
nm("fresenius-medical-care-white-oak-llc", "Form D name match on a homonym: a Fresenius Medical Care dialysis-clinic LLC whose "
   "director David Wells is a Fresenius officer; not a venture company and not a Kleiner Perkins position.")
nm("gather-wholesale-inc", "Form D name match only: Ilya Fushman is a director on the 2020 filing ($12.2M, a virtual-mailbox "
   "address in Walnut, CA), inside his Kleiner Perkins years, but the company could not be identified and no firm listing, "
   "KP vehicle or press names Kleiner Perkins in its round; missing corroboration is not_member.", conf="medium")
nm("genies-inc", "D2 Bond: Mary Meeker on the 2021 Form D ($65M Series C) is a Bond partner, and after September 2018 a Bond "
   "partner locates Bond, not Kleiner Perkins; nothing names a Kleiner Perkins or Digital Growth fund.")
nm("gpudb-inc", "Form D name match only: Ray Lane's 2016 seat is his GreatPoint Ventures seat (Wikipedia: 'existing backer Ray "
   "Lane of GreatPoint Ventures'); nothing names a Kleiner Perkins fund. GPUdb is Kinetica, the same registrant (CIK 1671223) "
   "as kinetica-db-inc.")
nm("grail-inc", "Form D name match only: Brook Byers sits on GRAIL's board from 2017 at the company's address; press coverage of "
   "his appointment (CNBC, 2017-04-26) describes him joining on his own rather than for Kleiner Perkins, and GRAIL's Series A "
   "and B releases (cited on the GV and Sutter Hill rows) name no Kleiner Perkins fund.", conf="medium")
nm("heap-inc", "Form D name match only: Matt Murphy's 2021 seat is his Menlo Ventures seat (the Menlo sibling row holds Heap); "
   "nothing names Kleiner Perkins in a round (D5).")
nm("heart-test-laboratories-inc", "Form D name match on a homonym: David Wells is an officer of Heart Test Laboratories, listed "
   "since 2022 (the 2023 placements are public-market purchases, T3); nothing names Kleiner Perkins.")
nm("hello-soju-inc", "Form D name match only: Ted E. Schlein's 2024 seat falls in his Ballistic Ventures years (D5: Ballistic "
   "from 2022); no listing, KP vehicle or press names a Kleiner Perkins fund in a round.", conf="medium")
nm("hippo-enterprises-inc", "D2 Bond: Noah Knauf joined Hippo's board in July 2019 and the 2021 S-1 names 'Bond Capital Fund, LP "
   "and affiliate' as the holder, with no Kleiner Perkins or Digital Growth fund; a Bond-only position is external (D2).")


TC_ERIDU = "https://techcrunch.com/2026/03/10/ai-network-startup-eridu-emerges-from-stealth-with-hefty-200m-series-a/"
TC_FEMTO = "https://techcrunch.com/2022/09/28/femtosense-raises-capital-to-power-the-ai-inside-of-consumer-electronics/"
GNW_GALY = "https://www.globenewswire.com/news-release/2024/09/03/2939864/0/en/galy-raises-33-million-in-oversubscribed-series-b-financing-to-advance-its-cellular-agriculture-platform.html"
L.append(verdict("eridu-corp", "not_member", "Form D name match only: Wen Hsieh's 2026 seat is his Matter Venture Partners seat "
                 "(TechCrunch, 2026-03-10: the $200M Series A was led by Socratic Partners, John Doerr personally and Matter "
                 "Venture Partners, whose founding managing partner Hsieh is); no Kleiner Perkins fund is named, and a partner's "
                 "personal check is not the firm's (D3, D5).", ec=FA, conf="high", cite=TC_ERIDU))
L.append(verdict("femtosense-inc", "not_member", "Form D name match only: Wen Hsieh is a director on the 2018 seed filing "
                 "($1.1M), but no Kleiner Perkins fund is named anywhere; TechCrunch's account of the 2022 $8M Series A lists "
                 "Fine Structures Ventures, J2 Ventures, SV Pacific, Quest, Amino Capital, Sand Hill Angels and Gaingels, and "
                 "the firm never listed the company (missing corroboration).", ec=FA, conf="medium", cite=TC_FEMTO))
L.append(verdict("galy-co", "not_member", "R4, a partner's family office is not the firm: GALY's Series B release (2024-09-03) "
                 "names Eighty Eighty Group, 'John Doerr's family office', among its existing investors and Ryan Panchadsaram "
                 "(on the board since 2021) as Doerr's technical advisor at Kleiner Perkins; no Kleiner Perkins fund is named "
                 "(decisions.md R4, D3).", ec=FA, conf="high", cite=GNW_GALY))

S1_HEARTFLOW = "https://www.sec.gov/Archives/edgar/data/1464521/0001628280-25-035242.txt"
L.append(verdict("heartflow-inc", "not_member", "Form D name match only: Dana Mead is HeartFlow's President and CEO on the 2019 "
                 "filing, an operating role after his Kleiner Perkins years, and HeartFlow's 2025 S-1 names no Kleiner Perkins or "
                 "KPCB fund anywhere (holder tables included); no listing or press names the firm in a round (D5).", ec=FA,
                 conf="high", cite=S1_HEARTFLOW))
nm("gruns-nutrition-inc", "Form D name match only: Nancy Xiao's 2025 seat falls years after her Kleiner Perkins roster years "
   "(2019-2020); Wikipedia's account of Gruns' rounds (pre-seed and seed 2023-2024, a $35M Series B led by Headline in 2025) "
   "names no Kleiner Perkins fund (D5 seat dating).")

nm("epiodyne-inc", "Form D name match only: Brook Byers is a director on the 2017-2019 filings at the company's own address; "
   "the Menlo row cites Menlo's own page for the Series A, and no firm listing, KP vehicle or press source (Google News "
   "search 2026-09-30) names a Kleiner Perkins fund in an Epiodyne round (missing corroboration).", conf="medium")

# ================= members held by KP vehicles' own filings (classification only)
L.append(cls("digital-generation-systems-inc", rng="below_1b", stage="undetermined", rounds=[], country="US", city="Irving",
             focus="Media, Gaming & Advertising",
             note="Ad-distribution network (DG Systems, San Francisco, later DG FastChannel in Irving, TX); Kevin Compton of "
                  "Kleiner Perkins sat on its board (Corsair's 1997 S-1). Sizmek spun off and the rest sold to Extreme Reach "
                  "in 2014 (Wikipedia): acquired, aligned with the TCV row. EDGAR holds no IPO prospectus naming the "
                  "firm's round."))
L.append(cls("edmark-corp", status="acquired", rng="below_1b", stage="undetermined", rounds=[], country="US", city="Redmond",
             focus="Consumer & Marketplaces",
             note="Children's educational software (Redmond, WA); acquired by IBM in November 1996 for $102.3M (Wikipedia, "
                  + jl.W("Edmark") + "). Kleiner Perkins filed a 13G in February 1996; no source names the firm's round."))
L.append(cls("genemedicine-inc", status="acquired", rng="below_1b", stage="undetermined", rounds=[], country="US",
             city="The Woodlands", focus="Healthcare & Bio",
             note="Gene medicine developer (The Woodlands, TX); merged with Megabios in March 1999 to form Valentis, so "
                  "acquired, aligned with the NEA row. EDGAR holds no IPO prospectus naming the firm's round."))
L.append(cls("geron-corporation", stage="Series A", stage_src="web_verified", stage_cite=S1_GERON, stage_conf="high",
             entry_date="1992", country="US", city="Foster City", focus="Healthcare & Bio",
             rounds=[rnd("1992", "Series A", 7600000, None, True, S1_GERON, "filing")],
             note="Telomerase and oncology biotech (Foster City). The 1996 S-1 lists Kleiner Perkins Caufield & Byers VI and "
                  "its founders fund holding 366,176 Series A shares; Series A ($3.40 a share, $7.6M) closed 757,353 shares "
                  "by the end of 1992 and 1,477,919 in March 1993, with KP partner Alexander Barkas a director and CEO from "
                  "March 1992, so the entry is the 1992 Series A (Wikipedia: initial venture capital from Kleiner Perkins and "
                  "Venrock)."))

# ================= duplicates of listed rows
PR_ERG = "https://www.prnewswire.com/news-releases/erecycling-group-secures-105-million-in-series-c-funding-229536621.html"
L.append(verdict("erecycling-group-inc", "member",
                 "eRecycling Group, Inc. (Irving, TX) is the parent of eRecyclingCorps, the erecyclingcorps row on the firm's "
                 "archived company pages (2012-2014, Green Growth Fund, Michael Linse and Maritza Liaw); its 2013 release says "
                 "KPCB's Green Growth Fund made its initial investment in December 2011 and KPCB led the $105M Series C. Merge "
                 "into erecyclingcorps.", ec="site_listing", cite=jl.ARCH("erecyclingcorps")))
L.append(cls("erecycling-group-inc", status="acquired", rng="below_1b", stage="undetermined", entry_date="2011-12",
             city="Irving", focus="Climate & Energy", flags=DUP + ["stage_disputes_band"],
             rounds=[rnd("2011-12", "round (unnamed)", None, None, True, PR_ERG, "company"),
                     rnd("2013-10-28", "Series C", 105000000, "Kleiner Perkins Caufield & Byers", True, PR_ERG, "company")],
             note="Wireless device trade-in and reuse (Irving, TX), later renamed HYLA Mobile and bought by Assurant in "
                  "2020, so acquired. The company's release of 2013-10-28 says the firm's Green Growth Fund first invested "
                  "in December 2011 (the round is not named; a Series C followed in 2013), so the pre-filled Series A band, "
                  "read off the January 2013 filing, is not the entry: undetermined with the date. Duplicate of "
                  "erecyclingcorps."))

L.append(verdict("cross-platform-corp", "member",
                 "Cross-Platform Corp is Shopkick's first legal name (CIK 1468215, the registrant on the shopkick row): its "
                 "2009 Form D names Aileen Lee, Matt Murphy and Cyriac Roeding, then all at Kleiner Perkins, and the firm's "
                 "own list carries Shopkick from 2009 (iFund). Merge into shopkick.", ec="site_listing",
                 cite=jl.SITE("shopkick")))
L.append(cls("cross-platform-corp", status="acquired", rng="below_1b", stage="undetermined", entry_date="2009",
             country="US", city="Redwood City", focus="Consumer & Marketplaces", flags=DUP,
             rounds=[rnd("2009", "round (unnamed)", 5020000, None, True, FD_CROSS, "filing")],
             note="Shopkick, shopping rewards app, conceived while Cyriac Roeding was an entrepreneur-in-residence at the "
                  "firm; acquired by SK Planet in 2014 and sold to Trax in 2019 (Wikipedia, which now places it in Denver; "
                  "city aligned with the Greylock and Menlo rows). The firm's partners are on the first, 2009 filing, so the "
                  "firm entered at the first round, which no source names. Duplicate of shopkick."))

jl.write("j11b", L)
