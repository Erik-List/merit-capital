#!/usr/bin/env python3
"""PRO-77 Sutter Hill Ventures, queue batch 3 (45 rows). Run: NQ_TAG=b3 python3 judgments-3.py

Every citation comes from a helper (ARCH, W, NEWS) or is a URL a tool printed in this
session (EDGAR indexes listed by the submissions API or the full-text sweep, WebSearch
results, the stockanalysis page read by WebFetch)."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, ARCH, W, NEWS

N = 3
L = []
INV = Path(__file__).resolve().parents[1]


def ARCH_PATH(slug, year, path):
    """The row's capture in a listing year on a given page path (read from disk)."""
    for r in json.loads((INV / "sources/wayback/parsed" / f"{year}.json").read_text()):
        if r["slug"] == slug and r.get("path") == path:
            return r["capture_url"]
    raise SystemExit(f"ARCH_PATH({slug!r}, {year}, {path!r}): not on disk")


# EDGAR indexes printed by this session's tools (submissions API / full-text sweep)
ALTEON_424B4 = "https://www.sec.gov/Archives/edgar/data/1089925/000101287099003357/0001012870-99-003357-index.htm"
CM_424B4 = "https://www.sec.gov/Archives/edgar/data/1031951/000089843099002024/0000898430-99-002024-index.htm"
AGP_S1A = "https://www.sec.gov/Archives/edgar/data/1064863/000095013301500056/0000950133-01-500056-index.htm"
ASPM_S1A = "https://www.sec.gov/Archives/edgar/data/886235/000095013599005700/0000950135-99-005700-index.htm"
C3_S1 = "https://www.sec.gov/Archives/edgar/data/1577526/000162828020016443/0001628280-20-016443-index.htm"
BOXER_D = "https://www.sec.gov/Archives/edgar/data/1589031/000158903113000002/0001589031-13-000002-index.htm"
CORIXA_8K = "https://www.sec.gov/Archives/edgar/data/1042561/000089102002001171/0000891020-02-001171-index.htm"
# WebSearch / WebFetch results
CLAIMCARD_PC = "https://www.propertyandcasualty.com/doc/claimcard-secures-33-million-in-second-round-0001"
C3_CAP = "https://stockanalysis.com/stocks/ai/market-cap/"

# ---------------------------------------------------------------- not members (D6, T3, sale consideration)
L.append(verdict(
    "biovest", "not_member",
    "decisions.md D6 (T5, the LP-stake class): the firm's 1999 table lists 'Biovest Partners, Medical investment "
    "partnership, Distributed', and its 2008 and 2012 pages file 'Biovest' under the firm's own 'Investment "
    "Partnerships' category (/investment/biovest.html), so the position is a partnership interest. The 2008 to "
    "2013 pages attach a description and link of Biovest International, Inc. (OTCQB: BVTI), an unrelated operating "
    "company; no SEC filing from 2001 on puts Sutter Hill Ventures in Biovest International's filings, so the "
    "description reads as the web page's mix-up, not an identification of an SHV equity holding.",
    ec="site_listing", conf="medium", cite=ARCH("biovest", 2008)))
L.append(verdict(
    "chengwei-capital", "not_member",
    "decisions.md D6 (T5, the LP-stake class): the firm's 2008 and 2012 pages file Chengwei Capital under its own "
    "'Investment Partnerships' category (/investment/chengwei.html: 'Chengwei Ventures invests in early-stage "
    "technology companies in greater China'), and the 2013 page describes a fund whose portfolio 'includes over 20 "
    "companies'. SHV's position is an interest in a venture fund, not equity in an operating company; Len Baker is "
    "named beside it as the firm's contact.",
    ec="site_listing", conf="high", cite=ARCH("chengwei-capital", 2008)))
L.append(verdict(
    "costanoa-venture-capital", "not_member",
    "decisions.md D6 and D1 (T5, the LP-stake class): Costanoa Venture Capital is Greg Sands's own venture firm "
    "from 2012 (external under D1). The firm's 2013 to 2016 lists carry it beside its companies, and the 2013 page "
    "describes it as an early stage investor in cloud-based services, linking costanoavc.com; the position is an "
    "interest in its fund, not an operating company.",
    ec="site_listing", conf="high", cite=ARCH_PATH("costanoa-venture-capital", 2013, "/portfolio-full")))
L.append(verdict(
    "curis", "not_member",
    "Sale consideration (COLLECTION.md s1, Erik 2026-09-22; the Point Nine share-swap ruling of 2026-09-26): the "
    "firm's 2008 and 2012 pages list Curis with the merger text 'Curis, Inc. will be formed by leveraging the "
    "combined strengths of Creative BioMolecules, Ontogeny and Reprogenesis'. The firm's 1999 table (every "
    "investment since 1970) lists Ontogeny and neither of the other two, so SHV's Curis shares are the "
    "consideration for its Ontogeny shares in the July 2000 merger; no SEC filing from 2001 on names Sutter Hill "
    "Ventures in Curis's filings, so no new money followed. The investment is Ontogeny (its own row, ontogeny).",
    ec="site_listing", conf="medium", cite=ARCH("curis", 2008)))
L.append(verdict(
    "corixa", "not_member",
    "T3 and decisions.md D4 (a post-IPO position with no pre-IPO round): SHV's only Corixa position is the August "
    "2002 private placement of Corixa common stock (7,332,562 shares at $6.13, led by InterWest Partners); "
    "Corixa's 8-K of 2002-08-13 carries the purchase agreement signed for Sutter Hill Ventures, A California "
    "Limited Partnership by Tench Coxe. Corixa had been public since its 1997 IPO, and the firm's own 1999 table "
    "of every investment since 1970 does not list it, so there was no venture round in a private company: a "
    "purchase of a public company's stock. The firm's 2008 to 2016 listing does not change the instrument.",
    ec="fund_filing", conf="medium", cite=CORIXA_8K))

# ---------------------------------------------------------------- members: classification only
L.append(cls(
    "alteon-websystems", status="acquired", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=ALTEON_424B4, stage_conf="high", entry_date="1996-05",
    rounds=[rnd("1996-05", "Series A", None, None, True, ALTEON_424B4, "filing"),
            rnd("1997-05", "Series B", None, None, True, ALTEON_424B4, "filing"),
            rnd("1998-06", "Series C", None, None, True, ALTEON_424B4, "filing"),
            rnd("1999-06", "Series D", None, None, True, ALTEON_424B4, "filing")],
    country="US", city="San Jose", focus="Data Infrastructure",
    note="Gigabit Ethernet switches, San Jose (EDGAR registrant address). Acquired by Nortel Networks on "
         "2000-10-04 (Wikipedia; the firm's 2010 page: 'acquired by Nortel Networks'). Entry: the IPO prospectus "
         "(424B4, 1999-09-24), Related Party Transactions, shows Sutter Hill Ventures buying Series A preferred in "
         "5/96 (3,896,103 shares as converted at $0.51, the same block as Matrix Partners), then Series B (5/97, "
         "$3.33), C (6/98, $4.67) and D (6/99, $5.67); Tench Coxe has been a director since May 1996. Wikipedia "
         "agrees: the initial venture investors were Matrix Partners and Sutter Hill Ventures."))
L.append(cls(
    "alventive", status="defunct", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="Santa Clara", focus="SaaS",
    note="Collaborative product-design software, Santa Clara (EDGAR registrant address). Listed by the firm only "
         "in 2004 (Software). Status aligned with sibling Benchmark (defunct, ceased operations after the 2001 "
         "bust); EDGAR shows a paper Form D as late as 2002-05-14 and nothing after, and Google News finds nothing. "
         "The round SHV joined is not on record."))
L.append(cls(
    "amberpoint-inc", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="Oakland", focus="DevTools & APIs",
    note="Web services (SOA) management software, Oakland (EDGAR registrant address; paper Form Ds 2002 to 2008). "
         "Acquired by Oracle in 2010 (the firm's 2013 page: 'was acquired by Oracle'). The firm's 2004 page quotes "
         "the company as founded in 2001 with significant venture backing from Sutter Hill and Norwest, which puts "
         "SHV in at founding but names no round; no press or filing names it, so the stage is undetermined."))
L.append(cls(
    "american-medical-systems", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Minnetonka", focus="Healthcare & Bio",
    note="Urology implants, Minnetonka, Minnesota. The firm's 1999 table: 'Acquired by Pfizer' (sibling Greylock "
         "dates the sale 1985 from its own listing); aligned with Greylock on status and city. This is the "
         "original AMS, not the AMS Holdings later bought out of Pfizer. The round SHV joined is not on record "
         "(before EDGAR)."))
L.append(cls(
    "amerigroup", rng="below_1b", stage="undetermined",
    rounds=[rnd(None, "Series A convertible preferred", None, None, None, AGP_S1A, "filing"),
            rnd(None, "Series B convertible preferred", None, None, None, AGP_S1A, "filing"),
            rnd(None, "Series C convertible preferred", None, None, None, AGP_S1A, "filing"),
            rnd("1998-07", "Series E redeemable preferred", 5_000_000, None, None, AGP_S1A, "filing"),
            rnd("1999-01-20", "Series E redeemable preferred", 5_000_000, None, None, AGP_S1A, "filing")],
    country="US", city="Virginia Beach", focus="Healthcare & Bio",
    note="Medicaid managed care, Virginia Beach. Acquired by WellPoint (now Elevance Health) in 2012 for $4.9B "
         "(Wikipedia). Fund position confirmed by the 2001 S-1/A: the principal stockholders footnote 'Represents "
         "securities owned by Sutter Hill Ventures, a California Limited Partnership' and its Entrepreneurs Funds. "
         "The prospectus lists Series A, B and C convertible preferred (8,000,000, 7,025,000 and 6,480,000 "
         "shares), Series D issued to Prudential for its Medicaid business (1999) and Series E redeemable "
         "preferred ($5.0M each in July 1998 and January 1999), but it does not say which series SHV bought, so "
         "the stage is undetermined (sibling Accel's Series A is a model label)."))
L.append(cls(
    "ameritox", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
    city="Baltimore", focus="Healthcare & Bio",
    note="Urine drug monitoring for pain medication, Baltimore, with its lab in Greensboro, NC. Wikipedia "
         f"({W('Ameritox')}): in 2018 it sold its book of business, auctioned its equipment and other assets and "
         "ceased to operate; an asset sale out of a wind-down reads acquired (COLLECTION.md s6). Aligned with "
         "sibling Bain Capital Ventures (acquired); sibling Sequoia still reads private, and the cited 2018 sale is "
         "fresher. The firm listed it 2008 to 2016 with Jeff Bird as managing director; no source names the round "
         "SHV joined."))
L.append(cls(
    "amira-medical", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Scotts Valley", focus="Healthcare & Bio",
    note="Glucose self-testing devices, Scotts Valley, California (model knowledge). The firm's 1999 table lists it "
         "as private; its 2008 and 2013 pages: 'was acquired by Roche Diagnostics'. The round SHV joined is not on "
         "record."))
L.append(cls(
    "amylin-pharmaceuticals-inc", rng="below_1b", stage="undetermined",
    country="US", city="San Diego", focus="Healthcare & Bio",
    note="Diabetes drugs (Symlin, Byetta), San Diego; founded 1987, IPO 1992 (Wikipedia). Acquired by "
         "Bristol-Myers Squibb in 2012 (tender offer filings on EDGAR from July 2012; the firm's 2013 page says "
         "so). The firm's 1999 table lists it as public; the round SHV joined is not on record (before EDGAR)."))
L.append(cls(
    "apollo-computer", rng="below_1b", stage="undetermined", city="Chelmsford", focus="Industrial & Robotics",
    note="Engineering workstations, founded 1980 in Chelmsford, Massachusetts; acquired by Hewlett-Packard in 1989 "
         "for $476M (Wikipedia; the firm's own pages say the same). Aligned with sibling Greylock (acquired, US, "
         "Industrial & Robotics). The founding-era round SHV joined is not on record."))
L.append(cls(
    "aptia", status="unknown", rng="below_1b", stage="undetermined",
    country="US", focus="Data Infrastructure", flags=("city_unknown",),
    note="Network monitoring and consulting; the firm's 1999 table lists it as private and no later page carries "
         "it. Google News, EDGAR and the firm's archive give no fate and no location (the name now belongs to an "
         "unrelated UK pensions administrator), so status is unknown and the city unplaced; US is inferred from "
         "the firm's 1999 portfolio, which is US companies. The round SHV joined is not on record."))
L.append(cls(
    "aspect-medical-systems", status="acquired", rng="below_1b", stage="undetermined",
    rounds=[rnd("1997-02/1997-10", "Series C", 12_900_000, None, None, ASPM_S1A, "filing"),
            rnd("1998-02-13", "Series D", None, None, None, ASPM_S1A, "filing"),
            rnd("1998-12-17", "Series E", None, None, None, ASPM_S1A, "filing")],
    country="US", city="Norwood", focus="Healthcare & Bio", flags=("model_disputes_source",),
    note="BIS anesthesia-depth monitors. Acquired by Covidien in 2009 for $210M (Wikipedia). Country disputed: "
         "the Wikidata IE reflects the later owners (Covidien, then Medtronic, both Irish-domiciled); Aspect was a "
         "Massachusetts company (Natick at its 1999 S-1, Norwood in its later EDGAR filings), hence US and "
         "Norwood. The S-1/A lists Series C (1997, $3.75 a share, about $12.9M), D (February 1998, $7.00) and E "
         "(December 1998, $10.00) but names no SHV purchase and SHV is not a 5% holder, so the round SHV joined "
         "is undetermined; the firm's 1999 table lists Aspect as private."))
L.append(cls(
    "avant", status="acquired", rng="below_1b", stage="undetermined", city="Fremont",
    focus="Industrial & Robotics", flags=("model_disputes_source",), clear=("unicorn_name_match",),
    extra={"valuation_source": None, "valuation_range_source": None, "valuation_asof": None,
           "valuation_confidence": None},
    note="Avant! Corporation, IC design (EDA) software, Fremont (EDGAR registrant address). Merged into Synopsys "
         "on 2002-06-06 (Wikipedia, Synopsys; the firm's 2013 page: 'has been acquired by Synopsys'), so acquired "
         "and below_1b. Disputed prefill: the private 1b_plus mark ($1.98B, 2015, unicorn list) belongs to Avant, "
         "the Chicago online lender, a name match; sibling ribbit-capital's avant is that lender (a collision, not "
         "aligned). EDA reads Industrial & Robotics, as on the other books' EDA rows. The round SHV joined is not "
         "on record."))
L.append(cls(
    "avid-technology", status="acquired", rng="below_1b", stage="undetermined", city="Burlington",
    focus="Media, Gaming & Advertising",
    note="Digital video and audio editing, Burlington, Massachusetts. Taken private by an STG affiliate in "
         "November 2023 for $1.4B (Wikipedia), so acquired; aligned with siblings Greylock and Sequoia. The firm's "
         "1999 table lists Avid (public) and, separately, Digidesign ('Acquired by Avid', 1995); the firm does not "
         "list its other stock-paying acquirers (Genzyme, EndoSonics, Nortel), which reads as a direct Avid "
         "position rather than Digidesign consideration, though no filing confirms either. The round SHV joined "
         "is not on record (IPO 1993, before EDGAR)."))
L.append(cls(
    "banyan-systems", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Westborough", focus="Data Infrastructure",
    note="VINES network operating system, Westborough, Massachusetts (EDGAR registrant, renamed ePresence). "
         f"Wikipedia ({W('Banyan VINES')}): the company dropped the Banyan name for ePresence in 1999, sold its "
         "services division to Unisys in late 2003 and liquidated its Switchboard holdings; an asset sale out of a "
         "wind-down reads acquired. Aligned with sibling Battery (acquired); sibling Greylock reads defunct on the "
         "liquidation. IPO 1992; the round SHV joined is not on record."))
L.append(cls(
    "barrx-medical", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="Sunnyvale", focus="Healthcare & Bio",
    note="BÂRRX Medical, ablation therapy for Barrett's esophagus, Sunnyvale (EDGAR registrant address; paper "
         "Form Ds 2003 and 2004, an electronic one in 2010). Acquired by Covidien in January 2012 (the firm's 2013 "
         "page). No source found names the round SHV joined."))
L.append(cls(
    "biosurface-technology", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Cambridge", focus="Healthcare & Bio",
    note="Skin and connective tissue repair, Cambridge, Massachusetts. The firm's 1999 table: 'Merged with "
         "Genzyme' (sibling Greylock's listing dates it 1995); aligned with Greylock (acquired, Cambridge). The "
         "round SHV joined is not on record."))
L.append(cls(
    "bix", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="Palo Alto", focus="Media, Gaming & Advertising",
    note="User-generated talent-contest site (Bix.com Inc., earlier 900 Seconds Inc., Palo Alto per its EDGAR "
         "registration; paper Form Ds 2006 and 2007). Acquired by Yahoo in February 2007 (the firm's 2013 page). "
         "No source found names the round SHV joined."))
L.append(cls(
    "blue-ridge-pharmaceuticals", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Greensboro", focus="Healthcare & Bio",
    note="Veterinary drugs, headquartered in Greensboro, NC; acquired by IDEXX Laboratories in October 1998 (the "
         "firm's own 2008 and 2013 pages; its 1999 table: 'Acquired by IDEXX'). The round SHV joined is not on "
         "record."))
L.append(cls(
    "bonafide", status="unknown", rng="undetermined", stage="undetermined", grad="undetermined",
    country="US", flags=("identity_unresolved", "city_unknown", "model_disputes_source"),
    note="Company not identified. The firm listed 'Bonafide' in 2015 and 2016 with a logo only (no description or "
         "link), and its 2015 team page files it under Mike Speiser beside Pure Storage, Snowflake, Sumo Logic and "
         "Sila Nanotechnologies, so it reads as a stealth company of his. Tried: EDGAR (no issuer of that name "
         "with an SHV person; Bonafide Provisions LLC of Oceanside is a bone-broth maker whose Form D names no SHV "
         "person), Google News and web search (nothing). Country disputed: the Wikidata AR is Bonafide, an "
         "Argentine coffee brand, a wrong join on a one-word name; US is inferred from the Speiser listing. Stage, "
         "band and graduation read undetermined for an unnamed company."))
L.append(cls(
    "boxer", stage="Seed", stage_src="web_verified", stage_cite=NEWS("boxer", "Boxer Snags"), stage_conf="high",
    entry_date="2013-10", rng="below_1b",
    rounds=[rnd(None, "angel round (as TaskBox)", 600_000, "Central Texas Angel Network", False,
                NEWS("boxer", "Boxer Snags"), "press"),
            rnd("2013-10", "Seed", 3_000_000, "Sutter Hill Ventures", True, NEWS("boxer", "Boxer Snags"), "press")],
    country="US", city="Austin", focus="SaaS", flags=("model_disputes_source",),
    note="Boxer, a mobile email and task client (Boxer Inc., Austin; Form D of 2013-10-15 at 701 Brazos, "
         f"{BOXER_D}). Silicon Hills News (2013-10-22): a $3 million seed round led by Sutter Hill Ventures (the "
         "Form D: first sale 2013-10-02, $2,889,398 sold of $3,089,398); the predecessor TaskBox had raised "
         "$600,000 from angels. Sam Pullara (at SHV from 2012) is the firm's managing director for it. Acquired by "
         "VMware (AirWatch) in October 2015 (Data Center Dynamics). Country disputed: the Wikidata value belongs to "
         "another Boxer, a wrong join on a one-word name. Graduation left for the graduation pass."))
L.append(cls(
    "bracket-computing", status="acquired", rng="below_1b", stage="undetermined",
    rounds=[rnd("2015-10", "Series C", 46_400_000, "Fidelity; Goldman Sachs", True,
                NEWS("bracket-computing", "raises $46.4M"), "press")],
    country="US", city="Mountain View", focus="Security",
    note="Bracket Computing, Mountain View, founded 2011 by Tom Gillis and Jason Lango (Wikipedia; VentureBeat). "
         "The firm's 2015 team page files it under Mike Speiser. SHV was in the October 2015 $46.4M round "
         "(VentureBeat; SiliconANGLE calls it the Series C) that brought total funding to $131.4M; the earlier "
         "rounds and SHV's entry are not named in any source found, so the stage is undetermined (sibling a16z's "
         "Series A is a model label). VMware took its IP and staff in May 2018 (Wikipedia); aligned with sibling "
         "a16z (acquired, US, Security)."))
L.append(cls(
    "brierley-partners", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="Dallas", focus="SaaS",
    note="Brierley+Partners, loyalty marketing and loyalty technology, founded 1985 by Hal Brierley, Dallas. Sold "
         "to Nomura Research Institute in 2015 (Dallas Innovates; Dallas Morning News, "
         f"{NEWS('brierley-partners', 'Brierley+Partners sold')}) and acquired by Capillary Technologies in April "
         "2023 (Dallas Innovates; Business Wire). The firm listed it 2010 to 2016 under Business & Financial "
         "Services; the round and size of SHV's position are not on record."))
L.append(cls(
    "buzznet-com", status="acquired", rng="below_1b", stage="undetermined",
    rounds=[rnd("2005", "private funding", None, "Anthem Venture Partners", None, W("Buzznet"), "press"),
            rnd("2007-05", "venture round", 6_000_000, "Redpoint Ventures", None, W("Buzznet"), "press"),
            rnd("2008-03", "venture round", 25_000_000, None, None, W("Buzznet"), "press")],
    country="US", city="Los Angeles", focus="Media, Gaming & Advertising",
    note="Buzznet, music and pop-culture social network, Los Angeles; later Buzz Media and SpinMedia. Wikipedia: "
         "'$35 million in four rounds' by 2008 from Focus Ventures, Anthem, NEA, Redpoint and Sutter Hill "
         "Ventures; the round SHV joined is not named. SpinMedia sold Buzznet, Idolator and PureVolume to Hive "
         "Media in September 2016, an asset sale out of a wind-down, so acquired."))
L.append(cls(
    "c3-energy", status="public", rng="1b_plus", usd=1_670_000_000, val_src="web_verified", val_cite=C3_CAP,
    asof="2026-09-28", extra={"valuation_range_source": "web_verified"},
    stage="undetermined",
    rounds=[rnd("2016-09", "venture round", 70_000_000, None, None,
                NEWS("c3-energy", "Injects More Funding"), "press"),
            rnd("2018-01", "venture round", 100_000_000, None, True,
                NEWS("c3-energy", "C3 IoT Raises $100 Million"), "company")],
    country="US", city="Redwood City", focus="AI & Applied AI",
    note="C3 Energy is C3.ai (NYSE: AI): founded 2009 by Thomas Siebel as C3, renamed C3 Energy, C3 IoT (2016) "
         "and C3.ai (2019), Redwood City (Wikipedia). Market cap $1.67B on 2026-09-28 (stockanalysis.com), so "
         "1b_plus. Fund position: Sutter Hill Ventures, A California Limited Partnership is a party to the "
         f"registration rights agreement filed with the 2020 S-1 (exhibit 4.2, {C3_S1}), and C3's January 2018 "
         "$100M release names Sutter Hill among existing investors. The firm listed it from 2013 with Jim White as "
         "managing director. The S-1 names no SHV purchase (its Series A converts into 21,000,000 Class B shares), "
         "so the round SHV entered is undetermined."))
L.append(cls(
    "cardiometrics", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Mountain View", focus="Healthcare & Bio",
    note="Cardiac measurement catheters, Mountain View (EDGAR registrant address; its public filings run 1996 to "
         "1997). The firm's 1999 table: 'Acquired by Endosonics'. The round SHV joined is not on record."))
L.append(cls(
    "ceon-corporation", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="Redwood City", focus="SaaS",
    note="Ceon, service fulfilment and product-lifecycle software for communications providers, Redwood City "
         "(EDGAR; paper Form Ds 2002 and 2003). Acquired by Convergys in October 2008 (Venture Capital Journal, "
         "'Convergys Buys VC-Backed Ceon Corp.'; Light Reading). The firm's 1999 table lists it as private; the "
         "round SHV joined is not on record."))
L.append(cls(
    "claimcard-inc", status="acquired", rng="below_1b", stage="undetermined",
    rounds=[rnd("1998-12", "second round", 3_300_000, "Sutter Hill Ventures", True, CLAIMCARD_PC, "press")],
    country="US", city="Sunrise", focus="Fintech & Payments",
    note="ClaimCard, payment cards and software for insurance claims, Sunrise, Florida; later renamed WildCard "
         "Systems, a prepaid card processor (PropertyandCasualty.com). SHV provided ClaimCard's $3.3 million "
         "second round in December 1998 as the only named investor; the source names no series and SHV's part in "
         "any first round is unknown, and a 'second round' does not collapse onto one stage, so the stage is "
         "undetermined. eFunds agreed to acquire WildCard Systems in June 2005 (Finextra, "
         f"{NEWS('claimcard-inc', 'EFunds to acquire WildCard')}), so acquired."))
L.append(cls(
    "closedloop-solutions", status="acquired", rng="below_1b", stage="undetermined",
    country="US", focus="SaaS", flags=("city_unknown",),
    note="Budgeting and planning (performance management) software. Acquired by Lawson Software for about $4 "
         f"million in October 2003 (The Register, {NEWS('closedloop-solutions', 'swooping in on Closedloop')}; the "
         "firm's 2004 and 2013 pages). The article and the firm's pages give no location and EDGAR has no filing "
         "under its name, so the city is unplaced. The round SHV joined is not on record."))
L.append(cls(
    "cohesive-network", status="acquired", rng="below_1b", stage="undetermined",
    country="US", focus="Data Infrastructure", flags=("city_unknown",),
    note="T1 multiplexers; the firm's 1999 table: 'Acquired by DCA' (Digital Communications Associates), a deal "
         "before EDGAR. No source found gives its location or the round SHV joined."))
L.append(cls(
    "concept-shopping", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="Lisle", focus="SaaS",
    note="Customer loyalty software and targeted marketing for retailers (the firm's 1999 line: 'Customer loyalty "
         "software'), Lisle, Illinois (EDGAR registrant address; paper Form Ds 2002 and 2005). A vendor profile "
         "(PitchBook) records its sale to DS-IQ, Inc. on 2010-04-14, consistent with the firm dropping it after "
         "2012; no press confirmation found, so the sale rests on that profile. The round SHV joined is not on "
         "record."))
L.append(cls(
    "consorte-media", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="San Francisco", focus="Media, Gaming & Advertising",
    note="Online advertising network for the US Hispanic market, San Francisco (EDGAR registrant address; paper "
         "Form Ds 2005 to 2007). Acquired by AudienceScience (the firm's 2013 page). No source found names the "
         "round SHV joined."))
L.append(cls(
    "copper-mountain", status="acquired", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=CM_424B4, stage_conf="high", entry_date="1996-04",
    rounds=[rnd("1996-04-10", "Series A", 2_723_000, None, True, CM_424B4, "filing"),
            rnd("1997-01-14", "Series B", None, None, True, CM_424B4, "filing")],
    country="US", city="Palo Alto", focus="Data Infrastructure",
    note="DSL access equipment, Palo Alto (EDGAR registrant address; operations in San Diego). IPO prospectus "
         "(424B4, 1999-05-13), Certain Transactions: in April 1996 the company sold 2,723,000 shares of Series A "
         "preferred at $1.00 under an agreement dated 1996-04-10, 1,250,000 of them to entities affiliated with "
         "Sutter Hill Ventures and 1,250,000 to Greylock; SHV also bought Series B ($3.39) in January 1997. Tench "
         "Coxe has been a director since March 1996, the company's inception. Acquired by Tut Systems in 2005 "
         "(merger proxy DEFM14A on EDGAR, April 2005); IPO'd then acquired reads acquired."))
L.append(cls(
    "cor-therapeutics", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="South San Francisco", focus="Healthcare & Bio",
    note="Cardiovascular drugs (Integrilin), South San Francisco (EDGAR registrant address). Merged into "
         "Millennium Pharmaceuticals in February 2002 (merger communications on EDGAR from December 2001; the "
         "firm's 2013 page: 'merged with Millenium Pharmaceuticals'). IPO 1991, before EDGAR; the firm's 2013 list "
         "names Len Baker as its managing director. The round SHV joined is not on record."))
L.append(cls(
    "cytel", status="acquired", rng="below_1b", stage="undetermined", city="Irvine", focus="Healthcare & Bio",
    note="Cytel Corporation (cell adhesion drugs, San Diego) is the EDGAR registrant CIK 822206, renamed Epimmune "
         "in 1999 and IDM Pharma in 2005 (Irvine, California). Takeda bought IDM Pharma by tender offer in June "
         "2009 (SC TO-T and 25-NSE filings), so acquired; the city is the registrant's last address. The round "
         "SHV joined is not on record (IPO before EDGAR)."))
L.append(cls(
    "datis", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
    country="US", focus="Healthcare & Bio", flags=("city_unknown",),
    note="Datis Corporation, databases and analyses for hospitals. HCIA acquired all of its capital stock on "
         "1995-04-28 for $14,250,000 in cash (HCIA's 1996 prospectus, 424B4); the firm's 1999 table says 'Acquired "
         "by HCIA'. The prospectus gives no location for Datis, so the city is unplaced. The round SHV joined is "
         "not on record."))
L.append(cls(
    "digidesign", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Menlo Park", focus="Media, Gaming & Advertising",
    note="Digital audio workstations (Pro Tools), founded 1984 as Digidrums, Menlo Park (EDGAR registrant "
         "address). Acquired by Avid Technology in 1995 (Wikipedia; the firm's 1999 table: 'Acquired by Avid'). "
         "The round SHV joined is not on record."))
L.append(cls(
    "digital-chocolate", rng="below_1b", stage="undetermined",
    rounds=[rnd("2011-02", "Series D", 12_000_000, None, None, NEWS("digital-chocolate", "Series D"), "press")],
    city="San Mateo", focus="Media, Gaming & Advertising",
    note="Mobile and social games studio founded 2003 by Trip Hawkins, San Mateo (Wikipedia); closed in 2014 "
         "after selling its games to RockYou (status defunct as prefilled, aligned with sibling Sequoia). The firm "
         "listed it 2008 to 2016 with Jim White as managing director. A February 2011 Series D ($12M) is on "
         "record, but no source names the round SHV entered (its 2004 Form Ds are paper filings), so the stage is "
         "undetermined."))
L.append(cls(
    "dionex", rng="below_1b", stage="undetermined",
    country="US", city="Sunnyvale", focus="Industrial & Robotics",
    note="Ion chromatography and analytical instruments, Sunnyvale (Wikipedia). Thermo Fisher Scientific announced "
         "its acquisition for $2.1B in December 2010 (acquired, as prefilled). SHV's David Anderson was a director "
         "through the 2000s (Dionex proxy statements on EDGAR); the founding-era round SHV joined is not on "
         "record."))
L.append(cls(
    "directag-com", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
    country="US", city="Saint Paul", city_src="web_verified", focus="Consumer & Marketplaces",
    note="Agricultural e-commerce portal founded 1999. Acquired by AgriStar Global Networks in August 2001 and "
         "relaunched as AgriStar (trade press headline 'DirectAg acquired, relaunches as AgriStar'); headquarters "
         "Saint Paul, Minnesota per a vendor profile. The firm's 1999 table lists it as private; the round SHV "
         "joined is not on record."))
L.append(cls(
    "echo-online", status="unknown", rng="below_1b", stage="undetermined",
    country="US", focus="Media, Gaming & Advertising", flags=("city_unknown",),
    note="Web affiliate network; the firm's 1999 table lists it as private and no later page carries it. Google "
         "News and web search find nothing on the company (the name collides with unrelated products), so status "
         "is unknown and the city unplaced; US is inferred from the firm's 1999 portfolio. The round SHV joined is "
         "not on record."))

if __name__ == "__main__":
    jl.write(f"batch-{N:03d}", L)
