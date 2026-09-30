"""PRO-100 NEA, judge c6, queue batch 12: listed members, classification only."""
import csv

import judge_lib as jl
from judge_lib import cls, rnd, SITE, ARCH, POST, W, NEWS, FTS

ROOT = jl.ROOT


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

# letgo
L.append(cls("letgo", status="acquired", rng="below_1b", country="US", city="New York", stage="undetermined",
             entry_date="2016", focus="Consumer & Marketplaces", rounds=[],
             note="Classifieds app; OfferUp's acquisition became official on 2020-09-21 (Wikipedia, Letgo). The firm "
                  "lists it as 'Letgo (Wallapop)' from 2016, the year Wallapop's US business merged into Letgo (May) "
                  "and Letgo raised $100M after the merger; whether NEA's stake came as merger consideration (D8) or "
                  "in that round is not settled, so the stage is undetermined. Aligned with the Insight and "
                  "Northzone rows."))

# lexicon-pharmaceuticals
L.append(cls("lexicon-pharmaceuticals", city="The Woodlands", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2008", focus="Healthcare & Bio",
             note="Nasdaq-listed since 2000, before the firm's 2008 first year; market cap $852M on 2026-09-30 "
                  "(stockanalysis), still below $1B. " + X1))

# lianlian
LL_CO = "https://stockanalysis.com/quote/hkg/2598/company/"
L.append(cls("lianlian", status="public", rng="below_1b", usd=449912449, val_src="web_verified",
             val_cite="https://stockanalysis.com/quote/hkg/2598/market-cap/", asof="2026-09-30", country="CN",
             country_src="web_verified", country_cite=LL_CO, city="Hangzhou", stage="undetermined",
             entry_date="2006", focus="Fintech & Payments", rounds=[],
             note="Lianlian DigiTech, listed in Hong Kong (2598.HK) since 2025; market cap HKD 3.53B on 2026-09-30 "
                  "(stockanalysis), HKD 3.53B @ ECB 2026-09-29 (HKD/EUR 8.9091, EUR/USD 1.1355) = $449.9M. "
                  "Headquartered in Hangzhou. The archive's 'acquired (by Amex)' is the payments joint venture with "
                  "American Express, not a sale. No source names the round of the firm's 2006 entry."))

# life-technologies
L.append(cls("life-technologies", city="Rockville", stage="undetermined", entry_date="1983", rng="below_1b",
             focus="Healthcare & Bio", rounds=[],
             note="Life Technologies Inc. (GIBCO BRL), Rockville, Maryland, merged into Invitrogen in 2000 (the "
                  "firm's own exit line). No source names the round of the firm's 1983 entry."))

# lily-ai
LILY_B = NEWS("lily-ai", "Lily AI Secures $25 Million Series B")
L.append(cls("lily-ai", status="private", rng="below_1b", country="US", city="Mountain View", stage="Seed",
             stage_src="first_party", stage_cite=SITE("lily-ai"), stage_conf="medium", entry_date="2017",
             grad="graduated", grad_src="web_verified", grad_cite=LILY_B, grad_conf="medium",
             focus="AI & Applied AI",
             rounds=[rnd("2022-08-24", "Series B", 25000000, lead=None, firm_in_round=None, source=LILY_B,
                         source_type="press"),
                     rnd("2024-03-14", "Series B-1", 20000000, lead=None, firm_in_round=None, source=None,
                         source_type="press")],
             note="Product-attribute AI for retailers; the firm's own listing labels its 2017 entry Seed. WWD's "
                  "headline (2022-08-24) names a $25M Series B, a later named round, so the row graduated (the page "
                  "is paywalled; the headline is the visible surface). A $20M Series B-1 followed in March 2024."))

# limitless
TC_REWIND = SIBCITE("first-round-capital", "Limitless", "entry_stage_citation")
L.append(cls("limitless", status="acquired", rng="below_1b", country="US", city="San Francisco", stage="Series A",
             stage_src="model", stage_conf="medium", entry_date="2023", focus="AI & Applied AI",
             flags=["stage_uncited"],
             rounds=[rnd("2023", "Series A", None, lead=None, firm_in_round=None, source=TC_REWIND,
                         source_type="press")],
             note="Formerly Rewind AI; Meta acquired it in December 2025 (the firm's own exit line, Google News). "
                  "TechCrunch (2024-04-17) calls the 2023 round pitched by video on X a Series A and lists NEA among "
                  "the backers; it is the round of the firm's 2023 first year but no read page ties NEA to it, so "
                  "model at medium."))

# linekong
LK_CO = "https://stockanalysis.com/quote/hkg/8267/company/"
L.append(cls("linekong", status="public", rng="below_1b", usd=9272275, val_src="web_verified",
             val_cite="https://stockanalysis.com/quote/hkg/8267/market-cap/", asof="2026-09-30", country="CN",
             country_src="web_verified", country_cite=LK_CO, city="Beijing", stage="undetermined", entry_date="2008",
             focus="Media, Gaming & Advertising", rounds=[],
             note="Linekong Interactive Group, listed in Hong Kong (8267.HK); market cap HKD 72.75M on 2026-09-30, "
                  "HKD 72.8M @ ECB 2026-09-29 (HKD/EUR 8.9091, EUR/USD 1.1355) = $9.3M. Headquartered in Beijing "
                  "(stockanalysis; its Cayman registration is a haven and falls through), which confirms the CN claim. "
                  "No source names the round of the firm's 2008 entry."))

# liquidia-corporation
L.append(cls("liquidia-corporation", country="US", city="Morrisville", stage="undetermined", entry_date="2007",
             rng="1b_plus", usd=4760000000, val_src="web_verified", val_cite=CAP("lqda"), asof="2026-09-30",
             focus="Healthcare & Bio", flags=["model_disputes_source"], rounds=[],
             note="Market cap $4.76B on 2026-09-30 (stockanalysis) replaces the stale $847M float, so the band moves "
                  "to 1b_plus. NEA 12 has held Liquidia since 2007 (the firm's own year); no source read names that "
                  "round. The same company as the liquidia-technologies row (Liquidia Technologies became a "
                  "subsidiary of the Liquidia Corporation holding company in the 2020 RareGen merger)."))

# liquidia-technologies
L.append(cls("liquidia-technologies", city="Morrisville", rng="below_1b", focus="Healthcare & Bio",
             flags=["identity_conflated"],
             note="Liquidia Technologies, Morrisville, North Carolina, is the operating company of the listed "
                  "Liquidia Corporation (the liquidia-corporation row), whose holding company it became in the 2020 "
                  "RareGen merger; the two rows are one company and should merge."))

# lithium-technologies
L.append(cls("lithium-technologies", status="acquired", rng="below_1b", city="San Francisco",
             city_src="formd_address", focus="SaaS", flags=["model_disputes_source"],
             note="Acquired by Vista Equity Partners (the firm's own exit line) and merged with Spredfast into Khoros. "
                  "The pre-filled public status and $4.8M float come from a wrong join (the Benchmark row carries the "
                  "same one); San Francisco per its Form D."))

# liveloop
L.append(cls("liveloop", status="acquired", rng="below_1b", country="US", city="San Francisco",
             city_src="web_verified", stage="Seed",
             stage_src="first_party", stage_cite=SITE("liveloop"), stage_conf="medium", entry_date="2010",
             focus="SaaS",
             note="Real-time PowerPoint collaboration in San Francisco; Microsoft acquired and shut it in March 2015 "
                  "(VentureBeat). The firm's own listing labels its 2010 entry Seed. " + GRAD_LEFT))

# liza-health
L.append(cls("liza-health", status="private", rng="below_1b", country="US", stage="Seed", stage_src="first_party",
             stage_cite=SITE("liza-health"), stage_conf="medium", entry_date="2025", grad="censored",
             focus="Healthcare & Bio", flags=["city_unknown"],
             note="AI primary-care company; the firm's own listing labels its 2025 entry Seed, inside the 24-month "
                  "window. Google News and its site place no office; US is the firm's US healthcare desk reading."))

# lizzyai
LZ = NEWS("lizzyai", "LizzyAI Raises $5M Seed Round Led by NEA")
L.append(cls("lizzyai", status="private", rng="below_1b", stage="Seed", stage_src="first_party",
             stage_cite=SITE("lizzyai"), stage_conf="medium", entry_date="2025-12", grad="censored",
             focus="AI & Applied AI", flags=["city_unknown"],
             rounds=[rnd("2025-12-02", "Seed", 5000000, lead="NEA", firm_in_round=True, source=LZ,
                         source_type="company")],
             note="AI interviewing platform; 'LizzyAI Raises $5M Seed Round Led by NEA' (Business Wire, 2025-12-02; "
                  "the page refused the fetch). Momentum check 2026-09-30: that seed is the only round found, no $1B "
                  "mark. No read source places its office, so country and city stay open."))

# logikcull
L.append(cls("logikcull", status="acquired", rng="below_1b", country="US", city="San Francisco",
             stage="undetermined", entry_date="2018", rounds=[],
             focus="SaaS",
             note="E-discovery SaaS; Reveal acquired Logikcull and IPRO, announced 2023-08-29 (Business Wire). "
                  "No source read names the round of the firm's 2018 entry (Rick Yang sat on the board), so the "
                  "stage is undetermined; San Francisco."))

# long-term-care-group
L.append(cls("long-term-care-group", status="acquired", rng="below_1b", country="US", city="Eden Prairie",
             stage="undetermined", entry_date="1996", focus="Healthcare & Bio", rounds=[],
             note="Long-term-care insurance administrator (now illumifin), acquired by Univita Health (the firm's own "
                  "exit line); Eden Prairie, Minnesota. No source names the round of the firm's 1996 entry."))

# loopt
L.append(cls("loopt", city="Mountain View", stage="Series A", stage_src="web_verified", stage_cite=W("Loopt"),
             stage_conf="high", entry_date="2005", rng="below_1b", focus="Consumer & Marketplaces",
             rounds=[rnd("2006", "Series A", 5000000, lead="Sequoia Capital and NEA", firm_in_round=True,
                         source=W("Loopt"), source_type="press"),
                     rnd("2007-07", "Series B", 8250000, lead=None, firm_in_round=None, source=W("Loopt"),
                         source_type="press")],
             note="Wikipedia: the $5M Series A came from Sequoia and NEA (then a Series B in July 2007); entry date is "
                  "the firm's own 2005, not the 2009 Form D, which is a follow-on. Acquired by Green Dot in 2012; "
                  "Mountain View, as in the Sequoia row."))

# loxo-oncology
L.append(cls("loxo-oncology", city="Stamford", rng="below_1b", focus="Healthcare & Bio",
             note="Acquired by Eli Lilly in 2019 (the firm's own exit line); Stamford, Connecticut."))

# lumena
L.append(cls("lumena", status="acquired", rng="below_1b", city="San Diego", focus="Healthcare & Bio",
             note="Acquired by Shire in 2014 (the firm's own exit line); San Diego. The firm's own post says Ed "
                  "Mathers led the $45M Series B, which matches the pre-filled Growth."))

# luminary
L.append(cls("luminary", status="private", rng="below_1b", city="New York", focus="Media, Gaming & Advertising",
             note="Podcast subscription network that raised about $100M from NEA and Sinai before its 2019 launch "
                  "(Wikipedia); a new CEO and an India launch in 2022 (Variety), no exit found. New York; the Chicago "
                  "address on its Form D is not an operating office. The 8VC 'Luminary' row is another company."))

# luminary-micro
L.append(cls("luminary-micro", city="Austin", stage="undetermined", entry_date="2006", rng="below_1b",
             focus="Industrial & Robotics", rounds=[],
             note="Microcontroller maker in Austin, acquired by Texas Instruments in 2009. No source names the round "
                  "of the firm's 2006 entry."))

# luminate-wireless
L.append(cls("luminate-wireless", status="unknown", rng="below_1b", country="US", stage="undetermined",
             entry_date="2013", focus="Data Infrastructure", flags=["city_unknown"], rounds=[],
             note="Mobile-network densification platform; Google News finds nothing under the name and no source "
                  "gives its fate or office, aligned with the GV row (unknown). No round source for the 2013 entry."))

# lumos-pharma
L.append(cls("lumos-pharma", city="Austin", rng="below_1b", focus="Healthcare & Bio",
             note="Public after its 2020 merger with NewLink Genetics and acquired in 2024 (the row's status is "
                  "acquired); Austin, Texas."))

# lungpacer-medical
L.append(cls("lungpacer-medical", status="private", rng="below_1b", city="Exton", city_src="formd_address",
             focus="Healthcare & Bio",
             note="Diaphragm-pacing device company, still raising (Form Ds to 2026), no exit found; Exton, "
                  "Pennsylvania per its Form D."))

# luxtera
L.append(cls("luxtera", status="acquired", rng="below_1b", city="Carlsbad", stage="undetermined", entry_date="2003",
             focus="Industrial & Robotics", rounds=[],
             note="Silicon-photonics chip maker founded in 2001, acquired by Cisco for $660M in 2019 (Wikipedia). No "
                  "source names the round of the firm's 2003 entry; Carlsbad, as in the Lux row."))

# lxa
LXA_SEED = NEWS("lxa", "LXA Raises US$10M in Seed Funding Round Led by NEA")
L.append(cls("lxa", status="acquired", rng="below_1b", country="SG", country_src="web_verified",
             country_cite=NEWS("lxa", "Singapore-based FinTech LXA"), city="Singapore", stage="Seed",
             stage_src="web_verified", stage_cite=LXA_SEED, stage_conf="high", entry_date="2023-11-08",
             focus="Fintech & Payments",
             rounds=[rnd("2023-11-08", "Seed", 10000000, lead="NEA", firm_in_round=True, source=LXA_SEED,
                         source_type="company")],
             note="Singapore mortgage-to-insurer capital platform; 'LXA Raises US$10M in Seed Funding Round Led by "
                  "NEA' (PR Newswire, 2023-11-08). CapitaLand acquired LXA Capital (KrASIA, 2025-12-02; the firm's "
                  "exit line 'Acquired by CLI PE PTE'). " + GRAD_LEFT))

# lyric
L.append(cls("lyric", status="acquired", rng="below_1b", city="San Francisco", city_src="formd_address",
             focus="Consumer & Marketplaces",
             note="Flexible-stay hospitality startup: it shut most locations in 2020, handed its last one to Mint "
                  "House, spun out Wheelhouse (2022), and Black Swan bought the Lyric business in June 2023 (Hotel "
                  "News Resource), so acquired with Black Swan as successor. The Insight 'Lyric' row (supply-chain "
                  "AI) is another company."))

# macromedia
L.append(cls("macromedia", status="acquired", rng="below_1b", city="San Francisco", stage="undetermined",
             entry_date="1989", focus="SaaS", flags=["model_disputes_source"], rounds=[],
             note="Adobe acquired Macromedia in 2005 in a stock swap of about $3.4B (Wikipedia), so the pre-filled "
                  "defunct is wrong; aligned with the Accel row. Kramlich led the investment (the firm's own post) "
                  "but no source names the round; the firm's year is 1989, before Macromedia's 1992 formation from "
                  "its predecessors."))

# magenta-medical
MAG = NEWS("magenta-medical", "Israeli heart pump co Magenta Medical")
L.append(cls("magenta-medical", status="private", rng="below_1b", country="IL", country_src="web_verified",
             country_cite=MAG, city="Kadima", stage="undetermined", entry_date="2019", focus="Healthcare & Bio",
             rounds=[rnd("2024-07-23", None, 105000000, lead="Novo Holdings", firm_in_round=None, source=MAG,
                         source_type="press")],
             note="Israeli heart-pump developer (Globes, 2024-07-23: 'Israeli heart pump co Magenta Medical raises "
                  "$105m', led by Novo Holdings); no valuation disclosed. No source read names the round of the "
                  "firm's 2019 entry."))

# magma-design-automation
S1_MAGMA = FTS("MAGMA", "S-1")
L.append(cls("magma-design-automation", status="acquired", rng="below_1b", country="US", city="San Jose",
             stage="Growth", stage_src="web_verified", stage_cite=S1_MAGMA, stage_conf="high", entry_date="1998-05",
             focus="SaaS",
             rounds=[rnd("1998-05", "Series B", 1000000, lead=None, firm_in_round=True, source=S1_MAGMA,
                         source_type="filing"),
                     rnd("1999-03-01", "Series C", None, lead=None, firm_in_round=True, source=S1_MAGMA,
                         source_type="filing")],
             note="The 2001 S-1's related-party table shows Mark Perry's NEA funds buying Series B (May-June 1998, "
                  "$1.24 a share), C and D, and none of the founders' Series A: the entry is the Series B. EDA "
                  "software maker in San Jose, acquired by Synopsys in 2012."))

# mainstream-data
L.append(cls("mainstream-data", status="private", rng="below_1b", country="US", city="Salt Lake City",
             stage="undetermined", entry_date="2002", focus="Data Infrastructure", rounds=[],
             note="Satellite and IP delivery of news and data feeds, Salt Lake City; still operating in 2019 (Via "
                  "Satellite: it bought a new IP service hub), no exit found. No source names the round of the "
                  "firm's 2002 entry."))

# maisonette
MAIS = SIBCITE("thrive-capital", "Maisonette", "entry_stage_citation")
L.append(cls("maisonette", status="private", rng="below_1b", city="New York", stage="Seed", stage_src="web_verified",
             stage_cite=MAIS, stage_conf="high", entry_date="2017", grad="graduated", grad_src="web_verified",
             grad_cite=MAIS, grad_conf="high", focus="Consumer & Marketplaces", flags=["stage_disputes_band"],
             rounds=[rnd("2018-05-17", "Series A", 15000000, lead="NEA", firm_in_round=True, source=MAIS,
                         source_type="company")],
             note="Maisonette's release (2018-05-17): 'the company's previous seed investor, New Enterprise "
                  "Associates (NEA)' returned to lead the $15M Series A. The firm's own listing labels its 2017 entry "
                  "Seed; the Form D band had read the 2018 round as the entry. Graduated; New York, aligned with "
                  "the Thrive row."))

# mapr-technologies-inc
L.append(cls("mapr-technologies-inc", status="acquired", rng="below_1b", city="Santa Clara",
             focus="Data Infrastructure",
             note="Hewlett Packard Enterprise bought MapR's business in 2019 after it failed to raise; Santa Clara, "
                  "as in the Lightspeed row."))

# marker-therapeutics
MRKR = FTS("Marker", "8-K")
L.append(cls("marker-therapeutics", country="US", city="Houston", stage="Growth", stage_src="web_verified",
             stage_cite=MRKR, stage_conf="high", entry_date="2018-10-17", focus="Healthcare & Bio",
             rounds=[rnd("2018-10-17", "PIPE", None, lead=None, firm_in_round=True, source=MRKR,
                         source_type="filing")],
             note="NEA bought 5,000,000 shares in the private placement of the listed company (formerly TapImmune) "
                  "effective 2018-10-17 (8-K exhibit); Houston. " + X1))

# martian
L.append(cls("martian", status="private", rng="below_1b", country="US", city="San Francisco", stage="Seed",
             stage_src="first_party", stage_cite=SITE("martian"), stage_conf="medium", entry_date="2023-11",
             focus="AI & Applied AI",
             rounds=[rnd("2023-11-15", "Seed", 9000000, lead=None, firm_in_round=None, source=None,
                         source_type="press")],
             note="LLM model router; the firm's own listing labels its 2023 entry Seed, the $9M seed announced "
                  "2023-11-15. Accenture made a strategic investment in September 2024 (unpriced). Momentum check "
                  "2026-09-30: no later priced round and no $1B mark. " + GRAD_LEFT))

# mashgin
MASH = SIBCITE("y-combinator", "Mashgin", "valuation_citation")
L.append(cls("mashgin", status="private", rng="1b_plus", usd=1500000000, val_src="web_verified", val_cite=MASH,
             asof="2022-05-09", country="US", city="Palo Alto", city_src="web_verified", stage="Growth",
             stage_src="web_verified", stage_cite=MASH, stage_conf="high", entry_date="2022-05-09",
             focus="AI & Applied AI", flags=["stale"],
             rounds=[rnd("2022-05-09", "Series B", 62500000, lead="NEA", firm_in_round=True, source=MASH,
                         source_type="company")],
             note="NEA, new to the cap table, led the $62.5M Series B at a $1.5B post-money (release, Palo Alto, "
                  "2022-05-09), a mark older than 24 months. Momentum check 2026-09-30: no newer priced round. The YC "
                  "row's San Francisco is its directory field; the release dateline is Palo Alto."))

# mashlogic-inc
L.append(cls("mashlogic-inc", status="acquired", rng="below_1b", country="US", city="Menlo Park",
             city_src="formd_address", stage="undetermined", entry_date="2009-08-19",
             focus="Consumer & Marketplaces", rounds=[],
             note="Browser-extension navigation startup; the firm's archived listing says 'Acquired By: Groupon'. "
                  "NEA's Krishna Kolluri sat on the board at its $2.5M 2009 Form D round, but the company was four "
                  "years old then and no source names the round (the band was withheld), so the stage is "
                  "undetermined. Menlo Park per the Form D."))

# masterclass
L.append(cls("masterclass", city="San Francisco", stage="undetermined", entry_date="2015",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2017-03-28", "Series C", 35000000, lead="IVP", firm_in_round=None,
                         source=SIBCITE("ivp", "MasterClass", "entry_stage_citation"), source_type="firm"),
                     rnd("2021-05-13", "Series F", 225000000, lead=None, firm_in_round=None,
                         source=SIBCITE("atomico", "MasterClass", "valuation_citation"), source_type="press")],
             note="The firm entered in 2015, before IVP's $35M Series C (2017) and the $225M Series F at $2.75B "
                  "(2021); Rick Yang sits on the board, but no source read names NEA's first round, so the stage is "
                  "undetermined. San Francisco, as in the Atomico and IVP rows."))

# matroid
MATP = POST("matroid-bringing-the-future-into-focus")
L.append(cls("matroid", status="private", rng="below_1b", country="US", city="Palo Alto", stage="Seed",
             stage_src="first_party", stage_cite=MATP, stage_conf="high", entry_date="2016", grad="graduated",
             grad_src="first_party", grad_cite=MATP, grad_conf="high", focus="AI & Applied AI",
             rounds=[rnd("2016", "Seed", None, lead="NEA", firm_in_round=True, source=MATP, source_type="firm"),
                     rnd(None, "Series A", None, lead="NEA", firm_in_round=True, source=MATP, source_type="firm"),
                     rnd("2020-10-13", "Series B", 20000000, lead="Energize", firm_in_round=True, source=None,
                         source_type="press")],
             note="The firm's own post (2018-03-22): the partner talked with Reza Zadeh 'about seeding Matroid a "
                  "couple years ago' and the company has since 'raised a Series A round from NEA', so a Seed entry "
                  "that graduated. A $20M Series B followed in October 2020 (Business Wire). Still private."))

# mbx-biosciences
L.append(cls("mbx-biosciences", city="Carmel", rng="1b_plus", usd=2820000000, val_src="web_verified",
             val_cite=CAP("mbx"), asof="2026-09-30", focus="Healthcare & Bio", flags=["model_disputes_source"],
             note="Market cap $2.82B on 2026-09-30 (stockanalysis) replaces the stale $237M float, so the band moves "
                  "to 1b_plus; Carmel, Indiana."))

# mediaocean
L.append(cls("mediaocean", status="acquired", rng="below_1b", country="US", city="New York", stage="Growth",
             stage_src="first_party", stage_cite=SITE("mediaocean"), stage_conf="medium", entry_date="2007",
             focus="SaaS",
             note="Advertising software company formed in 2012 from Donovan Data Systems and MediaBank (NEA's 2007 "
                  "entry predates the merger); Vista took a majority in 2015 and sold it to CVC and TA in 2020 "
                  "(Wikipedia, Mediaocean). The firm's exit line 'Acquired by AOL' does not match that record. The "
                  "firm's own listing labels the entry Growth."))

# medisys-edutech
L.append(cls("medisys-edutech", status="private", rng="below_1b", stage="undetermined", entry_date="2013",
             focus="Healthcare & Bio", flags=["city_unknown"], rounds=[],
             note="The firm's own link (app.smarteach.com/medrc) now serves MEdRC EduTech Ltd, a medical-education "
                  "company whose listed faculty are all in Indian cities; no read source gives its headquarters, so "
                  "country and city stay open. No source names the round of the firm's 2013 entry."))

# mei-pharma
MEIP = FTS("MEI Pharma", "8-K")
L.append(cls("mei-pharma", country="US", city="San Diego", stage="Growth", stage_src="web_verified",
             stage_cite=MEIP, stage_conf="high", entry_date="2018-05-16", focus="Healthcare & Bio",
             rounds=[rnd("2018-05-16", "PIPE", None, lead="Vivo Capital and CAM Capital", firm_in_round=True,
                         source=MEIP, source_type="filing")],
             note="NEA took part in the private placement led by Vivo and CAM announced 2018-05-16 (8-K). Renamed "
                  "Lite Strategy in 2025 (market cap $40.9M on 2026-09-30, stockanalysis). " + X1))

# mejuri
MEJP = POST("for-women-by-women-mejuri")
L.append(cls("mejuri", status="private", rng="below_1b", country="CA", country_src="web_verified",
             country_cite=NEWS("mejuri", "Canadian Jewelry Brand Mejuri Plans"), city="Toronto", stage="Growth",
             stage_src="first_party", stage_cite=MEJP, stage_conf="high", entry_date="2019-05",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2019-05", "Series B", 23000000, lead="NEA", firm_in_round=True, source=MEJP,
                         source_type="firm")],
             note="The firm's own post (2019-05-06): 'NEA led a $23M Series B in Mejuri', its 2019 entry. Toronto "
                  "fine-jewelry brand (JCK: 'Canadian Jewelry Brand Mejuri'), still private with no later priced "
                  "mark found."))

# merge
MERGE_B = NEWS("merge", "Merge raises $55M Series B for its unified API")
L.append(cls("merge", status="private", rng="below_1b", country="US", city="San Francisco", stage="Seed",
             stage_src="first_party", stage_cite=SITE("merge"), stage_conf="medium", entry_date="2021",
             grad="graduated", grad_src="web_verified", grad_cite=MERGE_B, grad_conf="high",
             focus="DevTools & APIs",
             rounds=[rnd("2021", "Seed", 4500000, lead="NEA", firm_in_round=True, source=SITE("merge"),
                         source_type="firm"),
                     rnd("2022-10-24", "Series B", 55000000, lead="Accel", firm_in_round=None, source=MERGE_B,
                         source_type="press")],
             note="Unified integrations API; the firm's own listing labels its 2021 entry Seed (the $4.5M seed, per "
                  "the 20VC row). TechCrunch's 'Merge raises $55M Series B for its unified API' (2022-10-24) is a "
                  "later named round, so the row graduated (a Series A came between them in late 2021). Aligned with "
                  "the 20VC and Accel rows on San Francisco."))

# mersana
L.append(cls("mersana", city="Cambridge", rng="below_1b", focus="Healthcare & Bio",
             note="Acquired (the row's status); Cambridge, Massachusetts."))

jl.write("c6b", L)
