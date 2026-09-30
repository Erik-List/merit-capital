"""PRO-100 NEA, judge g3b, delta batch 3: recall additions (membership + full classification), leftover
status/country/city/band rows, and two X1 re-judgments (connetics-corp, inventiva-s-a)."""
import json
import re

import judge_lib as jl
from judge_lib import cls, rnd, verdict, W, FTS, NEWS, GNEWS

TODAY = "2026-09-30"
WV = {"valuation_range_source": "web_verified"}
BASE = {r["slug"]: r for r in json.loads((jl.INV / "companies/base.json").read_text())}
LEDGER = json.loads((jl.INV / "companies/membership-ledger.json").read_text())["new-enterprise-associates"]["verdicts"]


def NOTEURL(slug, sub):
    """A URL from the row's own recall note (base.json), by substring; refuses none or several."""
    urls = [u.rstrip(").;,") for u in re.findall(r"https?://[^\s]+", BASE[slug].get("notes") or "") if sub in u]
    urls = list(dict.fromkeys(urls))
    if len(urls) != 1:
        raise SystemExit(f"NOTEURL({slug!r}, {sub!r}) matched {urls}")
    return urls[0]


# URLs printed by tools run in this session (secget, GNEWS/NEWS decodes, WebFetch reads)
CONNETICS_S3 = "https://www.sec.gov/Archives/edgar/data/1004960/0000891618-98-005364.txt"
INNOVASIVE_8K = "https://www.sec.gov/Archives/edgar/data/1003608/0000927016-99-003847.txt"
LUMISYS_8K = "https://www.sec.gov/Archives/edgar/data/1001289/0001012870-00-005625.txt"
MEDICALOGIC_8KA = "https://www.sec.gov/Archives/edgar/data/923899/000091205702015342/a2076689z8-ka.htm"
NETRIX_8K = "https://www.sec.gov/Archives/edgar/data/889237/000102677702000023/nx8k.txt"
NETCENTIVES_8K = "https://www.sec.gov/Archives/edgar/data/1081404/000089843001503766/d8k.txt"
GLIATECH_8K = "https://www.sec.gov/Archives/edgar/data/885741/000095015202004012/l94459ae8-k.txt"
IASIA_8K = "https://www.sec.gov/Archives/edgar/data/1110992/000101287002001090/d8k.txt"
ESSENTIAL_8K = "https://www.sec.gov/Archives/edgar/data/1010915/000119312503065283/d8k.htm"
CITYBIZ_CONNECT = "https://www.citybiz.co/article/798399/nicole-quinn-and-michael-blank-to-lead-connect-ventures/"
BLOCK_OS_B = "https://www.theblock.co/news/web3/2021-07-20-opensea-secures-100-million-in-series-b-round-at-1-5-billion-valuation-111977"
TC_OS_C = "https://techcrunch.com/2022/01/04/nft-kingpin-opensea-lands-13-3b-valuation-in-300m-raise-from-paradigm-and-coatue/"
TC_OS_A = "https://techcrunch.com/2021/03/18/nft-marketplace-opensea-raises-23-million-from-a16z/"
TC_DV = "https://techcrunch.com/2022/12/21/south-park-creators-deepfake-video-startup-deep-voodoo-conjures-20m-in-new-funding/"
KROLL_COMPIERE = "https://www.kroll.com/en/transactions/consona-corporation-acquires-open-source-and-cloud-erp-software-provider-compiere-inc"
FOS_JOMBOY = "https://frontofficesports.com/mlb-investing-in-jomboy-media-in-effort-to-reach-more-baseball-fans/"
BIZJ_JOMBOY = "https://www.bizjournals.com/newyork/news/2021/02/18/jomboy-media-gets-1-million-in-funding-eyes-full.html"
SA_IVA = "https://stockanalysis.com/stocks/iva/market-cap/"

L = []

# ================= Recall additions: membership + full classification =================

# ---- Compiere
L.append(verdict("compiere", "member",
                 "Compiere, Inc. raised its first outside round, $6M, from New Enterprise Associates in June 2006, with "
                 "NEA partners joining the board (the company's release of 2006-06-20; Wikipedia says the same).",
                 ec="web", conf="high", cite=W("Compiere")))
L.append(cls("compiere", status="acquired", rng="below_1b", country="US", city="Redwood City",
             stage="Series A", stage_src="model", stage_conf="medium", stage_cite=W("Compiere"), entry_date="2006-06",
             focus="SaaS",
             rounds=[rnd("2006-06-20", "unnamed (first outside round)", 6000000, "New Enterprise Associates", True,
                         NOTEURL("compiere", "compiere.com"), "company")],
             note="Open-source ERP vendor of Redwood City. NEA's $6M of June 2006 was the company's first outside round, "
                  "above the era's $1.5M seed ceiling, so Series A. Consona bought Compiere on 2010-06-16 (Kroll "
                  "transaction note; Wikipedia), terms not disclosed."))

# ---- Deep Voodoo
L.append(verdict("deep-voodoo", "member",
                 "Connect Ventures, the CAA and NEA partnership, led Deep Voodoo's $20M round of December 2022, its "
                 "first outside capital (TechCrunch, Variety, Wikipedia). Connect Ventures I, L.P. is on NEA's Form ADV "
                 "Schedule 7.B, so this is NEA fund money (decisions.md, Connect Ventures re-derivation).",
                 ec="web", conf="high", cite=W("Deep Voodoo")))
L.append(cls("deep-voodoo", status="private", rng="below_1b", country="US", city="Los Angeles",
             stage="Series A", stage_src="model", stage_conf="medium", stage_cite=TC_DV, entry_date="2022-12",
             focus="AI & Applied AI",
             rounds=[rnd("2022-12-20", "unnamed (first outside round)", 20000000, "Connect Ventures", True, TC_DV, "press")],
             note="AI visual effects studio of Trey Parker and Matt Stone, spun out of Park County, which funded it "
                  "until the $20M Connect Ventures round of December 2022; an unnamed first outside round above the "
                  "2022 seed ceiling ($8M), so Series A. Momentum check 2026-09-30 (Google News): no later priced round "
                  "and no $1B+ round; still operating (THR, 2026-03-31)."))

# ---- Everest Design Automation
EVEREST_S3 = NOTEURL("everest-design-automation", "sec.gov")
L.append(verdict("everest-design-automation", "member",
                 "Synopsys' S-3 of 1998-11-25 registers the Synopsys shares Everest's stockholders received when "
                 "Synopsys bought Everest Design Automation in November 1998, and lists New Enterprise Associates VII "
                 "(163,400 shares), NEA Presidents Fund and NEA Ventures 1998 among them: NEA funds held Everest. The "
                 "firm's archived Synopsys page adds 'Acquired Everest Design for stock 10/98' (D8).",
                 ec="fund_filing", conf="high", cite=EVEREST_S3))
L.append(cls("everest-design-automation", status="acquired", rng="below_1b", country="US",
             stage="undetermined", focus="Industrial & Robotics", flags=["city_unknown"],
             note="Private developer of shape-based physical design (routing) software for chips, bought by Synopsys "
                  "for stock under a merger agreement of 1998-10-26, closed 1998-11-20 (the S-3). No source names NEA's "
                  "round or dates its entry, and none places the company's city."))

# ---- Jomboy Media
L.append(verdict("jomboy-media", "member",
                 "Jomboy Media's $5M round of May 2022 'came by way of Connect Ventures, a partnership with Creative "
                 "Artists Agency (CAA) and global venture capital firm New Enterprise Associates (NEA)', with Connect's "
                 "Adam Friedman joining the board (Dodger Blue, 2022-05-06). Connect Ventures I is an NEA fund (Form ADV).",
                 ec="web", conf="high", cite=NOTEURL("jomboy-media", "dodgerblue")))
L.append(cls("jomboy-media", status="private", rng="below_1b", city="New York", stage="undetermined",
             focus="Media, Gaming & Advertising",
             rounds=[rnd("2021-02-18", "unnamed", 1000000, None, False, BIZJ_JOMBOY, "press"),
                     rnd("2022-05-05", "unnamed", 5000000, "Connect Ventures", True,
                         NOTEURL("jomboy-media", "dodgerblue"), "press"),
                     rnd("2025-06-10", "strategic minority stake (MLB), undisclosed", None, "Major League Baseball", None,
                         FOS_JOMBOY, "press")],
             note="New York baseball media company (Business Journals: 'Jomboy Media of New York'). Connect's entry was an "
                  "unnamed $5M round that followed the founder's 2018 raise and $1M in February 2021, so it is not the "
                  "first round and no source names it; the stage stays undetermined. MLB took an undisclosed minority "
                  "stake in June 2025; still operating (Fubo channel, April 2026)."))

# ---- Logic Modeling
L.append(verdict("logic-modeling", "member",
                 "The firm's own archived Synopsys page (first investment 1994, Historic) reads 'Acquired Logic Modeling "
                 "for stock 3/94': NEA's Synopsys stock was the consideration for its Logic Modeling position, so Logic "
                 "Modeling is the member and Synopsys stays out (D8).",
                 ec="site_listing", conf="medium", cite=NOTEURL("logic-modeling", "commoncrawl")))
L.append(cls("logic-modeling", status="acquired", rng="below_1b", country="US", city="Beaverton",
             stage="undetermined", focus="Industrial & Robotics",
             note="Beaverton, Oregon maker of simulation models and hardware modeling systems for chip design, bought by "
                  "Synopsys for stock in March 1994 (the firm's Synopsys page; EEJournal's EDA history). NEA's entry round "
                  "and year are not on record. Aligned with the Sutter Hill and Sequoia rows (acquired, US, Beaverton)."))

# ---- Mojito
MOJ = NOTEURL("mojito", "ntb.no")
L.append(verdict("mojito", "member",
                 "Mojito's $20M first round (release of 2021-10-21, led by Future Perfect Ventures) had a strategic "
                 "investment from 'Connect Ventures, an investment partnership between ... CAA and global venture capital "
                 "firm New Enterprise Associates (NEA)'. Connect Ventures I is an NEA fund (Form ADV).",
                 ec="web", conf="high", cite=MOJ))
L.append(cls("mojito", status="private", rng="below_1b", country="US", city="New York", city_src="web_verified",
             stage="Series A", stage_src="model", stage_conf="medium", stage_cite=MOJ, entry_date="2021-10-21",
             focus="Crypto & Web3",
             rounds=[rnd("2021-10-21", "unnamed (first round)", 20000000, "Future Perfect Ventures", True, MOJ, "company")],
             note="NFT commerce suite spun out of Serotonin, dateline New York. Its first round, $20M, is unnamed and above "
                  "the 2021 seed ceiling ($6M), so Series A. The last dated trace of the company is the Coinbase case "
                  "study of August 2023 and its president's Wikipedia page still names it; no sale or shutdown found "
                  "(Google News, 2026-09-30), so private."))

# ---- Music AI (Moises)
MBW = NOTEURL("music-ai-moises", "musicbusinessworldwide")
L.append(verdict("music-ai-moises", "member",
                 "Music AI's $40M Series A 'was led by Connect Ventures, an investment partnership between CAA and "
                 "venture capital firm New Enterprise Associates (NEA)', with monashees (Music Business Worldwide, "
                 "2025-01-22; LatamList the same). Connect Ventures I is an NEA fund (Form ADV).",
                 ec="web", conf="high", cite=MBW))
L.append(cls("music-ai-moises", status="private", rng="below_1b", country="US", city="Salt Lake City",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=MBW, entry_date="2025-01-22",
             focus="AI & Applied AI",
             rounds=[rnd("2022", "Seed", 8600000, "monashees", False, MBW, "press"),
                     rnd("2025-01-22", "Series A", 40000000, "Connect Ventures; monashees", True, MBW, "press")],
             note="Music AI (the Moises app), Salt Lake City, founded by Brazilians. Connect Ventures entered as lead of "
                  "the $40M Series A ($30M primary, $10M secondary) after monashees' $8.6M seed of 2022. Momentum check "
                  "2026-09-30 (Google News): no later round and no $1B+ priced round."))

# ---- Niroda Therapeutics
NIRODA_CITE = re.search(r"\((https://statamic\.nea\.com[^)]*\))\)", BASE["niroda-therapeutics"]["notes"]).group(1)
L.append(verdict("niroda-therapeutics", "member",
                 "The firm's own CMS carries an entry for Niroda Therapeutics (draft dated 2026-07-22, not yet published): "
                 "'developing non-opioid pain treatments', status Private, investment type Current, NEA team Scott "
                 "Gottlieb, Ali Behbahani and J.C. Lopez. BB Biotech's Q2 2026 slides add Niroda as a new private "
                 "position, so a 2026 private round exists. The firm's own listing, read from an unpublished draft.",
                 ec="site_listing", conf="medium", cite=NIRODA_CITE))
L.append(cls("niroda-therapeutics", status="private", rng="below_1b", country="US", city="Short Hills",
             city_src="web_verified", stage="undetermined", focus="Healthcare & Bio",
             note="U.S. biotech (Korea Biomedical Review) that in-licensed Daewoong affiliate iN Therapeutics' NaV1.7 "
                  "non-opioid pain candidate in December 2025; Dun & Bradstreet's directory lists it in Short Hills, New "
                  "Jersey. No round is announced (Google News and web search, 2026-09-30) and the firm's label is Early, "
                  "which is not a round word, so the stage is undetermined."))

# ---- OpenSea
L.append(verdict("opensea", "member",
                 "Connect Ventures, which 'originally began as an investment partnership between CAA and NEA in 2020', "
                 "has made investments in 'TMRW Sports, OpenSea, Slash, and Jomboy Media' (citybiz and THR, 2026-01-26). "
                 "Connect Ventures I is an NEA fund (Form ADV Schedule 7.B).",
                 ec="web", conf="medium", cite=CITYBIZ_CONNECT))
L.append(cls("opensea", status="private", rng="10b_plus", usd=13300000000, val_src="web_verified", val_cite=TC_OS_C,
             asof="2022-01-04", extra=WV, city="New York", stage="Growth", stage_src="model", stage_conf="medium",
             stage_cite=BLOCK_OS_B, entry_date="2021-07", focus="Crypto & Web3", flags=["stale"],
             rounds=[rnd("2021-03-18", "Series A", 23000000, "Andreessen Horowitz", None, TC_OS_A, "press"),
                     rnd("2021-07-20", "Series B", 100000000, "Andreessen Horowitz", True, BLOCK_OS_B, "press"),
                     rnd("2022-01-04", "Series C", 300000000, "Paradigm; Coatue", None, TC_OS_C, "press")],
             note="NFT marketplace. The Block names Creative Artists Agency among the participants in the $100M Series B "
                  "of July 2021 at $1.5B; Tracxn (vendor, listed not cited) places Connect Ventures in that round, so the "
                  "entry reads the Series B, Growth, at medium. Mark: the $300M Series C at $13.3B of 2022-01-04 led by "
                  "Paradigm and Coatue (TechCrunch), the last priced primary; stale. City aligned with the a16z, Coatue, "
                  "Tiger and YC rows (Wikipedia's lede now says Miami, undated)."))

# ================= Leftovers: status, country, city, band =================

# ---- Connetics: X1 re-judgment (NEA's only position is a November 1998 private placement into the listed company)
L.append(verdict("connetics-corp", "not_member",
                 "Connetics (Connective Therapeutics) listed in February 1996. NEA's only position is the 1,250,000 shares "
                 "New Enterprise Associates VIII (a 1998 fund), NEA Presidents Fund and NEA Ventures 1998 bought in the "
                 "November 1998 private placement (the S-3 of 1998-12-16 registering the 'November 1998 Investors'), and "
                 "NEA's 13G of 1999-02-16 names only those vehicles. X1: a PIPE into an already listed company with no "
                 "earlier NEA private round; if Erik rules a PIPE a venture entry, this row enters at Growth.",
                 ec="fund_filing", conf="high", cite=CONNETICS_S3))

# ---- GeneMedicine
L.append(cls("genemedicine-inc", status="acquired", rng="below_1b", country="US", city="The Woodlands",
             city_src="web_verified", focus="Healthcare & Bio",
             note="Gene medicine developer of The Woodlands, Texas (its EDGAR address). It merged with Megabios in March "
                  "1999 to form Valentis (DEFM14A of 1999-02-22, deregistered 1999-03-18), so acquired."))

# ---- Gliatech
L.append(cls("gliatech-inc", status="defunct", rng="below_1b", country="US", city="Cleveland", city_src="web_verified",
             focus="Healthcare & Bio",
             note="Maker of ADCON anti-adhesion gels, Cleveland, Ohio (its EDGAR address). It filed Chapter 11 on "
                  "2002-05-09 (8-K of 2002-05-10) and deregistered on 2002-05-15; no sale of the business is on record, so "
                  "defunct."))

# ---- iAsiaWorks
L.append(cls("iasiaworks-inc", status="defunct", rng="below_1b", country="US", city="San Mateo", city_src="web_verified",
             focus="Data Infrastructure",
             note="Asian web hosting and data center operator headquartered in San Mateo. It sold its Korean and Taiwan "
                  "operations in 2001-02 and its board authorized dissolution and wind-up on 2002-03-07 (8-K of "
                  "2002-03-08). Aligned with the IVP row."))

# ---- Innovasive Devices
L.append(cls("innovasive-devices-inc", status="acquired", rng="below_1b", country="US", city="Marlborough",
             city_src="web_verified", focus="Healthcare & Bio",
             note="Sports medicine device maker of Marlborough, Massachusetts. It signed a merger agreement with Johnson & "
                  "Johnson on 1999-11-08 (8-K of 1999-11-19) and was absorbed as a J&J subsidiary."))

# ---- Inventiva S.A.: X1, the same company as the excluded inventiva-pharma row
INV_424 = LEDGER["inventiva-pharma"]["citation"]
L.append(verdict("inventiva-s-a", "not_member",
                 "The same company as the inventiva-pharma row, already not_member under X1: Inventiva has been listed "
                 "on Euronext Paris since February 2017, and NEA's first purchase was the capital increase of 2019-09-20, "
                 "priced at the Euronext close and subscribed beside BVF and Novo (the July 2020 Nasdaq prospectus); "
                 "the 13D filings behind this row come after that. If Erik rules a PIPE a venture entry, the company "
                 "enters at Growth once, on one of the two slugs.",
                 ec="fund_filing", conf="high", cite=INV_424))

# ---- Lumisys
L.append(cls("lumisys-inc-de", status="acquired", rng="below_1b", country="US", city="Sunnyvale", city_src="web_verified",
             focus="Healthcare & Bio",
             note="Maker of laser film digitizers for medical imaging, Sunnyvale. Eastman Kodak agreed to acquire it on "
                  "2000-11-09 (8-K of 2000-11-13; deregistered January 2001)."))

# ---- MedicaLogic/Medscape
L.append(cls("medicalogic-medscape-inc", status="acquired", rng="below_1b", country="US", city="Hillsboro",
             city_src="web_verified", focus="Healthcare & Bio",
             note="Electronic health record company of Hillsboro, Oregon. After its Chapter 11 filing of 2002-01-24, the "
                  "court approved the sale of substantially all of its Digital Health Records business to GE Medical "
                  "Systems Information Technologies for about $35.3M, closed 2002-03-25 (8-K/A of 2002-04-16); GE is the "
                  "successor."))

# ---- Microcide Pharmaceuticals
L.append(cls("microcide-pharmaceuticals-inc", status="defunct", rng="below_1b", country="US", city="Mountain View",
             focus="Healthcare & Bio",
             note="Antibacterial drug developer of Mountain View, renamed Essential Therapeutics after its 2001 merger "
                  "with Althexis and Maret (later Waltham). It filed Chapter 11 on 2003-05-01; the plan effective "
                  "2003-10-21 cancelled the common stock and left the company with its preferred holders (8-K of "
                  "2003-10-22), and no later operation is on record. Aligned with the IVP row."))

# ---- Netcentives
L.append(cls("netcentives-inc", status="defunct", rng="below_1b", country="US", city="San Francisco",
             city_src="web_verified", focus="Media, Gaming & Advertising",
             note="Online loyalty and rewards marketing company (ClickRewards), San Francisco. It filed Chapter 11 on "
                  "2001-10-05 and its assets were auctioned piecemeal to six high bidders in November 2001 (8-K of "
                  "2001-12-03); no buyer took the business as a whole, so defunct."))

# ---- Netrix (NX Networks)
L.append(cls("netrix-corp", status="acquired", rng="below_1b", country="US", city="Herndon", city_src="web_verified",
             focus="Data Infrastructure",
             note="Network equipment maker of Herndon, Virginia, renamed NX Networks after its 2000 merger with OpenROUTE "
                  "Networks. It filed Chapter 11 on 2001-11-01, and on 2002-03-06 the court approved the sale of its "
                  "business to nsgdata.com (8-K of 2002-03-14); nsgdata.com is the successor."))

# ---- Object Design (eXcelon)
L.append(cls("object-design-inc", status="acquired", rng="below_1b", country="US", city="Burlington",
             city_src="web_verified", focus="Data Infrastructure",
             note="Maker of the ObjectStore object database, Burlington, Massachusetts; renamed eXcelon in January 2000 and "
                  "bought by Progress Software in December 2002 (DEFM14A of 2002-11-18; Wikipedia)."))

# ---- Occam Networks
L.append(cls("occam-networks-inc", status="acquired", rng="below_1b", country="US", city="Santa Barbara",
             city_src="web_verified", focus="Data Infrastructure",
             note="Broadband access equipment maker of Santa Barbara (reverse-merged into Accelerated Networks in 2002). "
                  "Calix acquired it in February 2011 (DEFM14A of 2010-12-15; delisted 2011-02-22)."))

jl.write("g3b", L)
