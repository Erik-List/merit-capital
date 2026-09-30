"""PRO-100 NEA, judge c6, queue batch 11: listed members, classification only."""
import csv

import judge_lib as jl
from judge_lib import cls, rnd, SITE, ARCH, POST, W, NEWS, FTS

ROOT = jl.ROOT


def FTSU(reg_sub, url_sub):
    """A full-text hit's document URL, chosen by registrant and a URL substring (exactly one)."""
    fl = {f["url"] for r in jl._FTS if reg_sub.lower() in r["registrant"].lower()
          for f in r.get("filings", []) if url_sub in f["url"]}
    if len(fl) != 1:
        raise SystemExit(f"FTSU({reg_sub!r}, {url_sub!r}) matched {len(fl)}")
    return fl.pop()


def SIBCITE(inv, name, col):
    """A citation read off a sibling book's row (rule 10 alignment), never typed."""
    p = ROOT / "data/collection/investors" / inv / "companies/base.csv"
    m = [r[col] for r in csv.DictReader(open(p)) if r["name"] == name and r.get(col)]
    if len(m) != 1:
        raise SystemExit(f"SIBCITE({inv!r}, {name!r}, {col!r}) matched {len(m)}")
    return m[0]


def CAP(t):
    return f"https://stockanalysis.com/stocks/{t}/market-cap/"


GRAD_LEFT = "Graduation left for the graduation pass."
X1 = ("The firm labels it Public/PIPES: NEA's first position was a purchase into the listed company, the X1 class "
      "(out unless Erik rules a PIPE a venture entry, in which case it enters at Growth as recorded here).")

L = []

# inozyme-pharma
L.append(cls("inozyme-pharma", rng="below_1b", city="Boston", focus="Healthcare & Bio",
             note="Acquired by BioMarin Pharmaceutical in 2025 (the firm's own exit line), so the row carries no mark; "
                  "headquartered in Boston."))

# insoft
L.append(cls("insoft", status="acquired", rng="below_1b", country="US", city="Mechanicsburg", stage="undetermined",
             entry_date="1995", focus="SaaS", rounds=[],
             note="Desktop videoconferencing software maker in Mechanicsburg, Pennsylvania, sold to Netscape on "
                  "1996-04-25 for about $161M (Wikipedia, InSoft Inc.). Wikipedia names NEA only among the backers of "
                  "Adams Capital's financing and no round word, so the stage is undetermined; entry year is the firm's "
                  "own 1995."))

# instabase
L.append(cls("instabase", stage="Series A", stage_src="first_party",
             stage_cite=POST("what-the-world-needs-now-why-instabase"), stage_conf="high", city="San Francisco",
             focus="AI & Applied AI", flags=["stage_disputes_band"],
             rounds=[rnd("2015-08", "Series A", 3750000, lead="NEA and Greylock", firm_in_round=True,
                         source=POST("what-the-world-needs-now-why-instabase"), source_type="firm")],
             note="The firm's own post (2019-10-21) says NEA co-led the Series A with Greylock as Instabase's first "
                  "financing, the $3.75M round of August 2015 the Form D band read as a seed; the stage is disputed to "
                  "Series A, so no seed-to-A column applies. The Greylock book still carries Seed from the band."))

# intact-vascular
L.append(cls("intact-vascular", status="acquired", rng="below_1b", city="Wayne", focus="Healthcare & Bio",
             note="Acquired by Royal Philips in 2020 (the firm's own exit line); Wayne, Pennsylvania."))

# intarcia-therapeutics-inc
S1_INTARCIA = FTSU("INTARCIA", "a2150613zs-1.htm")
L.append(cls("intarcia-therapeutics-inc", status="acquired", rng="below_1b", country="US", city="Boston",
             stage="Growth", stage_src="web_verified", stage_cite=S1_INTARCIA, stage_conf="high",
             entry_date="2003-06", focus="Healthcare & Bio",
             rounds=[rnd("2003-06", "Series D", 43000000, firm_in_round=True, source=S1_INTARCIA, source_type="filing"),
                     rnd("2004-11", "Series E", None, firm_in_round=True, source=S1_INTARCIA, source_type="filing")],
             note="The 2005 S-1's related-party table shows NEA 10 buying Series D preferred at $0.48 in June 2003 "
                  "and Series E in November 2004, nothing earlier, so the entry is the Series D. i2o Therapeutics "
                  "bought Intarcia's assets (the ITCA 650 implant and its platform) in August 2023 (BioPharma Dive, "
                  "2023-08-30): acquired, with i2o as successor. Headquartered in Boston since 2013 (Wikipedia)."))

# intelligencenode
TC_INODE = "https://techcrunch.com/2015/08/19/intelligencenode/"
L.append(cls("intelligencenode", status="acquired", rng="below_1b", country="IN", country_src="web_verified",
             country_cite=TC_INODE, city="Mumbai", city_src="web_verified", stage="Series A",
             stage_src="web_verified", stage_cite=TC_INODE, stage_conf="high", entry_date="2015-08-19",
             focus="SaaS",
             rounds=[rnd("2015-08-19", "Series A", 4000000, lead="NEA and Orios Venture Partners", firm_in_round=True,
                         source=TC_INODE, source_type="press")],
             note="TechCrunch (2015-08-19): 'Mumbai-based IntelligenceNODE' raised a $4M Series A led by NEA and "
                  "Orios, the firm's 2015 entry. Interpublic Group bought it, announced 2024-12-05 (about $100M, "
                  "Inc42); its site now reads 'an Omnicom Company'."))

# intellisys
THEORG = "https://theorg.com/org/vennfer"
L.append(cls("intellisys", status="private", rng="below_1b", country="IN", country_src="web_verified",
             country_cite=THEORG, city="Kolkata", city_src="web_verified", stage="undetermined", entry_date="2011",
             focus="SaaS", rounds=[],
             note="Intellisys Technologies & Research, maker of the Vennfer unified-communications product, "
                  "headquartered in Kolkata (theorg.com); private with no exit found. The live listing says Early and "
                  "the archived one says growth, a conflict no round record settles, so the stage is undetermined."))

# interleukin-genetics
S1_ILI = FTSU("INTERLEUKIN", "v348745_s1.htm")
L.append(cls("interleukin-genetics", country="US", city="Waltham", stage="Growth", stage_src="web_verified",
             stage_cite=S1_ILI, stage_conf="high", entry_date="2013-05-17", rng="below_1b", focus="Healthcare & Bio",
             rounds=[rnd("2013-05-17", "PIPE", None, lead=None, firm_in_round=True, source=S1_ILI,
                         source_type="filing")],
             note="Growth Equity Opportunities Fund III bought in the private placement completed 2013-05-17 into "
                  "the already listed company (resale S-1, Waltham, Massachusetts). " + X1))

# intermune
L.append(cls("intermune", country="US", city="Brisbane", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2011", rng="below_1b", focus="Healthcare & Bio",
             note="Nasdaq-listed since 2000; acquired by Roche in 2014. " + X1))

# intrinsic
CRN = SIBCITE("first-round-capital", "Intrinsic", "entry_stage_citation")
L.append(cls("intrinsic", status="acquired", rng="below_1b", country="US", city="San Francisco", stage="Seed",
             stage_src="web_verified", stage_cite=CRN, stage_conf="high", entry_date="2016-08", focus="Security",
             rounds=[rnd("2016-08", "Seed", None, lead=None, firm_in_round=True, source=CRN, source_type="press")],
             note="The firm's own record for this slug is Intrinsic, the San Francisco application-security tool "
                  "(external link to VMware security), not Intrinsic Therapeutics, which the evidence pack joined by "
                  "name. CRN: seed funding in August 2016 from a16z, First Round, NEA and StartX; VMware bought it in "
                  "August 2019. Aligned with the First Round and a16z rows. " + GRAD_LEFT))

# intrinsic-therapeutics
L.append(cls("intrinsic-therapeutics", status="private", rng="below_1b", city="Woburn", stage="undetermined",
             entry_date="2001", focus="Healthcare & Bio", rounds=[],
             note="Barricaid maker, still private and filing Form Ds through 2023; Woburn, Massachusetts. The firm's "
                  "own first-invested year is 2001 and no source names the round NEA entered (its partners' Form D "
                  "seats start in 2010), so the stage is undetermined."))

# inventiva-pharma
IVA_CO = "https://stockanalysis.com/stocks/iva/company/"
L.append(cls("inventiva-pharma", status="public", rng="below_1b", usd=768410000, val_src="web_verified",
             val_cite=CAP("iva"), asof="2026-09-29", country="FR", country_src="web_verified", country_cite=IVA_CO,
             city="Daix", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2019",
             focus="Healthcare & Bio",
             note="Market cap $768.41M on 2026-09-29 (stockanalysis); headquartered in Daix, France. Listed on "
                  "Euronext Paris since 2017 and Nasdaq since 2020, before the firm's 2019 first year. " + X1))

# inversago
NOVO = NEWS("inversago", "Novo Nordisk to acquire Inversago Pharma to develop new")
L.append(cls("inversago", status="acquired", rng="below_1b", country="CA", country_src="web_verified",
             country_cite=NOVO, city="Montreal", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2022-10", focus="Healthcare & Bio", flags=["stage_uncited"],
             rounds=[rnd("2022-10-17", "Series C", None, lead=None, firm_in_round=None,
                         source=NEWS("inversago", "Inversago Pharma Raises $95 million"), source_type="press")],
             note="Montreal company Novo Nordisk agreed to buy for up to $1.075B in August 2023 (GlobeNewswire). The "
                  "CAD 95M Series C of October 2022 is the only round in the firm's first year (2022); its release "
                  "could not be read (403), so NEA's part in it is inferred and the stage is model at medium."))

# iobeam
TSC = NEWS("iobeam", "Valued at Over $1B")
L.append(cls("iobeam", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified", val_cite=TSC,
             asof="2022-02-22", country="US", city="New York", stage="undetermined", entry_date="2015",
             focus="Data Infrastructure", flags=["stale"],
             rounds=[rnd("2022-02-22", "Series C", 110000000, lead=None, firm_in_round=None, source=TSC,
                         source_type="press")],
             note="iobeam became Timescale (the firm's own link is timescale.com) and rebranded TigerData in 2025. "
                  "The $110M Series C of February 2022 valued it at over $1B (FinSMEs headline; the floor is the "
                  "figure recorded), a mark older than 24 months. NEA's 2015 entry round is not named anywhere read, "
                  "so the stage is undetermined."))

# iomai-corporation
S1_IOMAI = FTSU("IOMAI", "w13079sv1.htm")
L.append(cls("iomai-corporation", status="acquired", rng="below_1b", country="US", city="Gaithersburg",
             stage="Growth", stage_src="web_verified", stage_cite=S1_IOMAI, stage_conf="high", entry_date="2002-12",
             focus="Healthcare & Bio",
             rounds=[rnd("2002-12", "Series C", 54300000, lead=None, firm_in_round=True, source=S1_IOMAI,
                         source_type="filing")],
             note="The 2005 S-1 shows NEA 10 and NEA Ventures 2002 holding only Series C preferred, sold in December "
                  "2002 ($54.3M) when Barrett joined the board. Acquired by Intercell in 2008 (the firm's own exit "
                  "line); Gaithersburg, Maryland."))

# ionq
L.append(cls("ionq", city="College Park", grad="graduated", grad_src="formd", focus="Industrial & Robotics",
             note="The Form D sequence graduates the row: $2.0M at entry, then a $20.3M round in 2017. College Park, "
                  "Maryland, as in the GV book."))

# iopipe
L.append(cls("iopipe", status="acquired", rng="below_1b", country="US", city="Seattle", stage="Seed",
             stage_src="first_party", stage_cite=SITE("iopipe"), stage_conf="medium", entry_date="2016",
             focus="DevTools & APIs",
             rounds=[rnd("2017-08-14", None, 2500000, lead=None, firm_in_round=True, source=None,
                         source_type="press")],
             note="The firm's own listing labels it Seed (2016); GeekWire (2017-08-14) reported the $2.5M round from "
                  "Madrona, NEA and Underscore. Acquired by New Relic in 2019. " + GRAD_LEFT))

# iridex-corporation
L.append(cls("iridex-corporation", country="US", city="Mountain View", stage="undetermined", entry_date="1991",
             focus="Healthcare & Bio", rounds=[],
             note="NEA special partner John Nehra chaired the board from 1989 (proxy); no source names the round of "
                  "the firm's 1991 entry, so the stage is undetermined."))

# iron-port
L.append(cls("iron-port", status="acquired", rng="below_1b", country="US", city="San Bruno", stage="Growth",
             stage_src="first_party", stage_cite=SITE("iron-port"), stage_conf="medium", entry_date="2004",
             focus="Security",
             note="IronPort Systems, acquired by Cisco in 2007; the firm's own listing labels its 2004 entry Growth. "
                  "Aligned with the Menlo row."))

# isgn-technologies-ltd
L.append(cls("isgn-technologies-ltd", status="acquired", rng="below_1b", stage="Growth", stage_src="first_party",
             stage_cite=SITE("isgn-technologies-ltd"), stage_conf="medium", entry_date="2007",
             focus="Fintech & Payments",
             note="Mortgage processing software and services; rebranded Sourcepoint in 2019 and bought by Sagent "
                  "Lending Technologies, announced 2019-12-23 (HousingWire). The firm's own listing labels its 2007 "
                  "entry Growth. No source read places its headquarters (a US mortgage business with an Indian "
                  "Ltd. entity), so country and city stay open."))

# ivantis
L.append(cls("ivantis", status="acquired", rng="below_1b", city="Irvine", stage="undetermined", entry_date="2007",
             focus="Healthcare & Bio", rounds=[],
             note="Hydrus microstent maker, acquired by Alcon (the firm's own exit line); Irvine, California. The firm "
                  "entered in 2007, the founding year, and no source names that round (the Form D band was withheld), "
                  "so the stage is undetermined."))

# jet-com
L.append(cls("jet-com", status="acquired", rng="below_1b", city="Hoboken", focus="Consumer & Marketplaces",
             note="Acquired by Walmart in 2016 for about $3.3B; aligned with the Coatue and General Catalyst rows."))

# juniper-networks
L.append(cls("juniper-networks", city="Sunnyvale", stage="undetermined", entry_date="1996", rng="below_1b",
             focus="Data Infrastructure", rounds=[],
             note="Acquired by Hewlett Packard Enterprise in 2025. Kramlich led the 1996 investment (the firm's own "
                  "post) but no source names the round, so the stage is undetermined."))

# juvo
JUVO = NEWS("juvo", "Juvo Raises $40M In Series B")
L.append(cls("juvo", status="private", rng="below_1b", country="US", city="San Francisco", city_src="web_verified",
             stage="Growth", stage_src="web_verified", stage_cite=JUVO, stage_conf="high", entry_date="2017-08-01",
             focus="Fintech & Payments",
             rounds=[rnd("2017-08-01", "Series B", 40000000, lead="NEA and Wing Venture Capital", firm_in_round=True,
                         source=JUVO, source_type="company")],
             note="NEA co-led the $40M Series B with Wing (Juvo's release, 2017-08-01, San Francisco), the round of "
                  "the firm's 2017 first year; still private, no later mark."))

# kaazing
L.append(cls("kaazing", status="private", rng="below_1b", city="Mountain View", city_src="formd_address",
             focus="Data Infrastructure",
             note="WebSocket real-time data platform; still announcing products in 2020 (Google News), no exit found. "
                  "Mountain View per its 2014 Form D."))

# kaizen
KZ = NEWS("kaizen", "Kaizen raises $21 million to re-build")
L.append(cls("kaizen", status="private", rng="below_1b", country="US", city="New York", city_src="web_verified",
             stage="Series A", stage_src="web_verified", stage_cite=KZ, stage_conf="high", entry_date="2025-10-30",
             focus="SaaS", flags=["model_disputes_source"],
             rounds=[rnd(None, "Seed", 11000000, lead="Accel and a16z", firm_in_round=False, source=KZ,
                         source_type="company"),
                     rnd("2025-10-30", "Series A", 21000000, lead="NEA", firm_in_round=True, source=KZ,
                         source_type="company")],
             note="Govtech software (kaizenlabs.co). NEA led the $21M Series A after an $11M seed co-led by Accel and "
                  "a16z (GlobeNewswire, 2025-10-30, New York dateline). The MA country was a one-word name match and "
                  "is replaced by US. Momentum check 2026-09-30: no round after the Series A, no $1B mark."))

# ketra
L.append(cls("ketra", status="acquired", rng="below_1b", country="US", city="Austin", stage="undetermined",
             entry_date="2011", focus="Industrial & Robotics", rounds=[],
             note="LED lighting semiconductor company in Austin, acquired by Lutron in April 2018 (CE Pro). No "
                  "source names the round of the firm's 2011 entry."))

# kindred
L.append(cls("kindred", status="private", rng="below_1b", city="San Francisco", city_src="formd_address",
             focus="Consumer & Marketplaces",
             note="Home-swapping network. Its $125M raise (a Series B co-led by NEA and Dylan Field and an Index-led "
                  "Series C, the company's blog, 2026-02-03) discloses no valuation, so no mark. The First Round and "
                  "GV 'Kindred' rows are Kindred Systems, the robotics company."))

# kira
KIRA = POST("kira-learning-democratizing-ai-literacy")
L.append(cls("kira", status="private", rng="below_1b", city="New York", city_src="web_verified", stage="Seed",
             stage_src="first_party", stage_cite=KIRA, stage_conf="high", entry_date="2022", grad="graduated",
             grad_src="first_party", grad_cite=KIRA, grad_conf="high", focus="AI & Applied AI",
             flags=["stage_disputes_band"],
             rounds=[rnd("2022-06", "Seed", 6000000, lead="NEA and AI Fund", firm_in_round=True, source=KIRA,
                         source_type="firm"),
                     rnd("2023-05", "Series A", 15000000, lead="NEA", firm_in_round=True, source=KIRA,
                         source_type="firm")],
             note="The firm's own post (2023-06-14): 'After leading Kira Learning's seed financing in 2022', NEA "
                  "leads its Series A ($15M, the 2023 Form D the band read as the entry). Stage disputed to Seed, "
                  "graduated. HQ moved from Palo Alto (Form D) to Lower Manhattan in 2026 (Business Journals). "
                  "Momentum check 2026-09-30: no round after the 2023 Series A found, no $1B mark."))

# knotch
KN = NEWS("knotch", "Knotch Raises $20 Million in Series B Funding to Power")
L.append(cls("knotch", status="private", rng="below_1b", country="US", city="New York", stage="Growth",
             stage_src="web_verified", stage_cite=KN, stage_conf="high", entry_date="2019-01-28", focus="SaaS",
             rounds=[rnd("2019-01-28", "Series B", 20000000, lead="NEA", firm_in_round=True, source=KN,
                         source_type="company")],
             note="NEA led the $20M Series B, announced 2019-01-28 (the firm's listing year is 2018, the close); "
                  "earlier investors are named as returning, NEA as the new lead. SoHo, New York."))

# kong
KONG_VAL = SIBCITE("balderton-capital", "Kong", "valuation_citation")
KONG_18 = SIBCITE("a16z", "Kong, Inc.", "entry_stage_citation")
L.append(cls("kong", status="private", rng="1b_plus", usd=2000000000, val_src="web_verified", val_cite=KONG_VAL,
             asof="2024-11-19", country="US", city="San Francisco", stage="Seed", stage_src="first_party",
             stage_cite=SITE("kong"), stage_conf="medium", entry_date="2011", grad="graduated",
             grad_src="web_verified", grad_cite=KONG_18, grad_conf="medium", focus="DevTools & APIs",
             flags=["model_disputes_source"],
             rounds=[rnd("2017-03-23", None, 18000000, lead="Andreessen Horowitz", firm_in_round=None,
                         source=KONG_18, source_type="press"),
                     rnd("2024-11-19", "Series E", 175000000, lead=None, firm_in_round=None, source=KONG_VAL,
                         source_type="firm")],
             note="Kong (formerly Mashape): the firm's own listing labels its 2011 entry Seed. The $18M round led by "
                  "a16z in March 2017 (SiliconANGLE) clears the step-up on an era seed ceiling of $2.5M, so the row "
                  "graduated. $175M Series E at $2B, 2024-11-19 (Balderton), the mark the a16z, Balderton and Tiger "
                  "rows share. The IT country was a wrong one-word join; San Francisco, US."))

# konux
L.append(cls("konux", status="private", rng="below_1b", country="DE", country_src="web_verified",
             country_cite=W("Konux"), city="Munich", stage="Series A", stage_src="model", stage_conf="medium",
             entry_date="2016-04", focus="Industrial & Robotics", flags=["stage_uncited"],
             rounds=[rnd("2016-04-15", "Series A", 7500000, lead=None, firm_in_round=None, source=None,
                         source_type="press")],
             note="Headquartered in Munich (Wikipedia, which names NEA among its investors). The $7.5M Series A of "
                  "April 2016 (FinSMEs headline, page not readable) is the round of the firm's 2016 first year; no "
                  "read page ties NEA to it, so model at medium. The DE claim is confirmed."))

# korro
L.append(cls("korro", country="US", city="Cambridge", stage="Series A", stage_src="model", stage_conf="medium",
             entry_date="2019", focus="Healthcare & Bio", flags=["stage_uncited"],
             note="RNA-editing biotech, public since the 2023 merger with Frequency Therapeutics (One Kendall Square, "
                  "Cambridge, per the S-1/A). Behbahani has sat on Legacy Korro's board since August 2019, NEA's "
                  "entry at the company's launch Series A; no read page names that round with NEA."))

# koudai
TC_KOUDAI = NEWS("koudai", "Tencent Leads $350M Investment")
L.append(cls("koudai", status="private", rng="below_1b", country="CN", country_src="web_verified",
             country_cite=TC_KOUDAI, city="Beijing", stage="Growth", stage_src="first_party",
             stage_cite=SITE("koudai"), stage_conf="medium", entry_date="2014", focus="Consumer & Marketplaces",
             flags=["needs_web_value"],
             rounds=[rnd("2014-10-23", "Series C", 350000000, lead="Tencent", firm_in_round=None, source=TC_KOUDAI,
                         source_type="press")],
             note="Koudai Gouwu (Weidian), the Chinese mobile marketplace; the firm's own listing labels its 2014 "
                  "entry Growth. TechCrunch's report of the Tencent-led $350M Series C (2014-10) does not name NEA "
                  "or give a valuation, so no figure is recorded and the band waits on a cited mark."))

# kumu-networks
L.append(cls("kumu-networks", status="private", rng="below_1b", city="Santa Clara", city_src="formd_address",
             focus="Industrial & Robotics",
             note="Full-duplex radio chips; raised a $25M Series C in 2016 and announced a 5G chip in 2022 (Business "
                  "Wire), no exit found. Kifer Road, Santa Clara (Form D), as in the Khosla row."))

# landit
L.append(cls("landit", status="private", rng="below_1b", country="US", city="New York", stage="Seed",
             stage_src="first_party", stage_cite=SITE("landit"), stage_conf="medium", entry_date="2014",
             focus="SaaS",
             note="Career-pathing platform for women at work; the firm's own listing labels its 2014 entry Seed. "
                  "ImpactAlpha (2019-02-28) reports a $13M raise. " + GRAD_LEFT))

# latitude
LAT_A = NEWS("latitude", "Latitude raises $35M in Series A funding led by Oak")
L.append(cls("latitude", status="private", rng="below_1b", country="US", city="Spring", city_src="web_verified",
             stage="Seed", stage_src="first_party", stage_cite=SITE("latitude"), stage_conf="medium",
             entry_date="2024", grad="graduated", grad_src="web_verified", grad_cite=LAT_A, grad_conf="high",
             focus="Fintech & Payments", flags=["model_disputes_source"],
             rounds=[rnd("2026-03", "Seed", 8000000, lead=None, firm_in_round=True, source=SITE("latitude"),
                         source_type="firm"),
                     rnd("2026-09-09", "Series A", 35000000, lead="Oak HC/FT", firm_in_round=None, source=LAT_A,
                         source_type="press")],
             note="Stablecoin-to-fiat payments infrastructure (latitude.xyz, whose own address is in Spring, Texas; "
                  "the team sits in New York, San Francisco and London). The firm's own listing labels its 2024 entry "
                  "Seed, the $8M seed announced out of stealth in 2026; the $35M Series A led by Oak HC/FT "
                  "(Crypto Briefing, 2026-09-09) graduates it. FR was a wrong one-word join. Momentum check "
                  "2026-09-30: no valuation disclosed, no $1B mark."))

# lattice-engines
L.append(cls("lattice-engines", status="acquired", rng="below_1b", city="San Mateo", focus="SaaS",
             note="Acquired by Dun & Bradstreet in 2019 (the firm's own exit line); San Mateo, as in the Battery and "
                  "Sequoia rows."))

# laurel-networks
L.append(cls("laurel-networks", status="acquired", rng="below_1b", city="Pittsburgh", stage="undetermined",
             entry_date="2000", focus="Data Infrastructure", rounds=[],
             note="IP edge router maker in Pittsburgh, acquired by ECI Telecom in 2005. No source names the round of "
                  "the firm's 2000 entry."))

# learnup
L.append(cls("learnup", status="unknown", rng="below_1b", city="San Francisco", stage="Seed", stage_src="first_party",
             stage_cite=ARCH("learnup"), stage_conf="medium", entry_date="2012", focus="SaaS",
             note="The firm's own archived listing labels its 2012 entry Seed (the $1.9M 2012 Form D round). NEA and "
                  "Shasta led an $8M round in September 2015 (TechCrunch, per the a16z row); no trace after 2016, "
                  "status unknown. " + GRAD_LEFT))

# ledge
LEDGE = POST("ledge-automating-payment-operations")
L.append(cls("ledge", status="private", rng="below_1b", country="US", city="New York", city_src="web_verified",
             stage="Seed", stage_src="first_party", stage_cite=LEDGE, stage_conf="high", entry_date="2023-02",
             focus="Fintech & Payments",
             rounds=[rnd("2023-02-16", "Seed", 9000000, lead="NEA", firm_in_round=True, source=LEDGE,
                         source_type="firm")],
             note="The firm's own post (2023-02-16): NEA led Ledge's $9M seed (TechCrunch adds Vertex, FJ Labs and "
                  "Picus). The company's site lists New York first, with a Tel Aviv office. Momentum check "
                  "2026-09-30 (Google News): no later round and no $1B mark found. " + GRAD_LEFT))

# ledgy
LEDGY_P = POST("growing-equity-in-europe-our-series-b-investment-in-ledgy")
L.append(cls("ledgy", status="private", rng="below_1b", country="CH", country_src="web_verified",
             country_cite=NEWS("ledgy", "Zurich-based Ledgy secures"), city="Zurich", stage="Growth",
             stage_src="first_party", stage_cite=LEDGY_P, stage_conf="high", entry_date="2022-09",
             focus="Fintech & Payments",
             rounds=[rnd("2021-09-07", "Series A", 10000000, lead="Sequoia", firm_in_round=False, source=None,
                         source_type="press"),
                     rnd("2022-09-21", "Series B", None, lead="NEA", firm_in_round=True, source=LEDGY_P,
                         source_type="firm")],
             note="The firm's own post (2022-09-21) announces NEA's Series B investment, the EUR 22M round "
                  "(EU-Startups: 'Zurich-based Ledgy'); the Sequoia-led Series A of 2021 predates NEA. Momentum check "
                  "2026-09-30: no later round or $1B mark found."))

# legato-medical
L.append(cls("legato-medical", status="unknown", rng="below_1b", country="US", stage="undetermined",
             entry_date="2012", focus="Healthcare & Bio", flags=["city_unknown"], rounds=[],
             note="GERD disease-management company on the firm's healthcare list (2012). Google News returns nothing "
                  "for it and no filing names it, so status, round and city are unknown; US is the firm's own "
                  "healthcare desk reading, not a placed address."))

# lemonade-io
L.append(cls("lemonade-io", status="acquired", rng="below_1b", country="US", stage="Seed", stage_src="first_party",
             stage_cite=SITE("lemonade-io"), stage_conf="medium", entry_date="2015", focus="SaaS",
             flags=["city_unknown"],
             note="Creativity-measurement startup, acquired by Evernote (the firm's own exit line); the firm's own "
                  "listing labels its 2015 entry Seed. No source read places its city. " + GRAD_LEFT))

# leonabio
LEONA = FTS("LeonaBio", "8-K")
L.append(cls("leonabio", country="US", city="Bothell", stage="Growth", stage_src="web_verified", stage_cite=LEONA,
             stage_conf="high", entry_date="2026-01-09", focus="Healthcare & Bio",
             rounds=[rnd("2026-01-09", "PIPE", 90000000, lead="Commodore Capital, Perceptive Advisors and TCGX",
                         firm_in_round=True, source=LEONA, source_type="filing")],
             note="Formerly Athira Pharma, renamed LeonaBio in January 2026; Bothell, Washington (S-1/A). NEA took "
                  "part in the $90M private placement announced 2026-01-09 (8-K). " + X1))

jl.write("c6a", L)
