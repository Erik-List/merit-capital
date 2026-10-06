"""PRO-80 Bessemer, delta judge d3, file a: rows allegro-networks to moxie-beauty (25 rows; 5 recall verdicts)."""
import re

import judge_lib as jl

N = jl.NEWS
_BASE = jl._base()


def RC(slug):
    """The citation URL carried by the row's own 'recall addition:' note (read from disk, never typed)."""
    m = re.findall(r"\((https?://[^)\s]+)\)", _BASE[slug].get("notes") or "")
    if not m:
        raise SystemExit(f"RC({slug!r}): no URL in the row's note")
    return m[-1]


def PRIOR(extra=None):
    """A country inferred from the firm's US desk: low confidence, flagged."""
    d = {"hq_country_confidence": "low"}
    d.update(extra or {})
    return d


# Light Reading pages, each found through the publisher's own search and read 2026-10-06
LR = "https://www.lightreading.com"
ALLEGRO_R1 = LR + "/cable-technology/ex-alcatel-crew-raises-25m"
ALLEGRO_B = LR + "/business-management/allegro-networks-nets-60m"
ENGIM_B = LR + "/business-management/engim-pockets-18-5m"
HATTERAS_2 = LR + "/business-management/hatteras-closes-second-round"
KIRANA = LR + "/cable-technology/what-s-kooking-at-kirana-"
# other pages read 2026-10-06
CTECH_DUALBIRD = N("dualbird", "DualBird raises $17M Series A")
VCND_EARTHLY = "https://vcnewsdaily.com/earthly-technologies/venture-capital-funding/ftdvqrybbp"   # WebSearch result, read
TC_EARTHLY = "https://techcrunch.com/2023/02/23/earthly-wants-to-reinvent-continuous-integration-to-make-it-faster-and-cheaper/"  # TechCrunch's own search, read
ENTRACKR_MOXIE = N("moxie-beauty", "Haircare startup Moxie Beauty raises")
MOXIE_POST = jl.POST("powering-inclusive-beauty-innovation-in-india-with-moxie-beauty")
FIRST_YEAR = "The firm's {y} page gives no investment year, so the entry date is the first year the firm listed it (a capture year)"

lines = [
    jl.cls("allegro-networks", status="defunct", rng="below_1b",
           stage="Series A", stage_src="web_verified", stage_cite=ALLEGRO_R1, stage_conf="medium", entry_date="2000-11",
           country="US", city="San Jose", city_src="web_verified", focus="Data Infrastructure",
           rounds=[jl.rnd("2000-11", "first round", 25_000_000, None, True, ALLEGRO_R1, "press"),
                   jl.rnd("2002-02", "Series B", 60_000_000, "Thomas Weisel Venture Partners", True, ALLEGRO_B, "press")],
           note="Edge router maker, San Jose (the firm's 2002 listing). Light Reading (2000-11-28): $25M in 'its first round of funding' with Bessemer, Columbia Capital and Infinity Capital; the next round is reported as the Series B (2002-02-19, Bessemer an existing investor) and the company raised $86M 'in two rounds', so the first round is read as the Series A at medium confidence. Light Reading (2003-03-18): it laid off nearly all staff and 'is officially winding down operations'; by July 2003 it 'went out of business back in March'."),
    jl.cls("avia-health", status="unknown", rng="below_1b", stage="undetermined", entry_date="2000",
           country="US", focus="Healthcare & Bio", flags=["city_unknown", "country_prior"], extra=PRIOR(), rounds=[],
           note="Web sites for pediatric practices, listed by the firm in 2000 and 2002 (its investment year 2000, Gautam Prakash). Wikipedia, Google News and EDGAR full text (2001 on) carry no trace of the company, so the status reads unknown and no round is named. The country is inferred from the firm's US desk of 2000; no source places the company."),
    jl.cls("bestoffer-com", status="unknown", rng="below_1b", stage="undetermined", entry_date="2000",
           country="US", focus="Consumer & Marketplaces", flags=["city_unknown"], rounds=[],
           note="Online used-car auction marketplace listed by the firm in 2000 (its investment year 2000, Joanna Strober). Autobytel's 10-K/A of April 2001 says its new finance chief had been CFO of Bestoffer.com, Inc. from July to November 2000; nothing read says what became of the company, so the status reads unknown. No round named; city not established."),
    jl.cls("cetacean-networks", status="unknown", rng="below_1b", stage="undetermined", entry_date="2002",
           country="US", city="Portsmouth", focus="Data Infrastructure", rounds=[],
           note="Real-time IP routing start-up led by Steven Rogers, the founder of Video Network Communications (that company's SB-2 of March 2001); Portsmouth, New Hampshire, from knowledge. A First Virtual Communications proxy of April 2003 still names it as a director's private company; nothing read says what became of it, so the status reads unknown. "
                + FIRST_YEAR.format(y="2002") + "; no round named."),
    jl.cls("cohesive-networks", status="acquired", rng="below_1b", stage="undetermined", entry_date="1983",
           country="US", focus="Data Infrastructure", flags=["city_unknown"], rounds=[],
           note="Digital switches and networks for voice, data and video. The firm's own 2005 text: 'BVP first invested in the company in 1983. It was acquired by Digital Communications in 1986' (acq. by Digital Communications Associates, 1986; Sutter Hill's row for Cohesive Network carries the same exit). The text names no round, and no source read places the company's city."),
    jl.cls("comanage", status="acquired", rng="below_1b", stage="undetermined", entry_date="1999",
           country="US", city="Wexford", focus="Data Infrastructure", rounds=[],
           note="Network service management software for carriers, Wexford, Pennsylvania (city from knowledge; its 2003 releases are datelined Pittsburgh). Light Reading (2005-08-16): Syndesis 'has agreed to acquire CoManage Corp.', with Bessemer named among CoManage's investors (acq. by Syndesis, 2005). The entry year 1999 is the firm's own; no round named."),
    jl.cls("dental-x-change", status="acquired", rng="below_1b", stage="undetermined", entry_date="1999",
           country="US", city="Irvine", focus="Healthcare & Bio", rounds=[],
           note="Online services and e-commerce for dental practices; Irvine, California, from knowledge. The company's own site dates 'the acquisition by EDI Health Group in 2004' and still signs as 'EDI Health Group, dba DentalXChange' (acq. by EDI Health Group, 2004). The entry year 1999 is the firm's own; no round named."),

    jl.verdict("dualbird", "member",
               "CTech (2025-11-05): DualBird's $17M Series A was 'led by Lightspeed Venture Partners with participation from Bessemer Venture Partners, Uncork Capital, and Angular Ventures'; the company's release of the same day names Bessemer in the combined $25M of seed and Series A. The citybiz page in the recall note would not open (403), so the press report read is cited.",
               ec="web", conf="high", cite=CTECH_DUALBIRD),
    jl.cls("dualbird", status="private", rng="below_1b",
           stage="Series A", stage_src="web_verified", stage_cite=CTECH_DUALBIRD, stage_conf="medium", entry_date="2025-11-05",
           country="IL", country_src="web_verified", country_cite=CTECH_DUALBIRD, city="Tel Aviv", focus="Data Infrastructure",
           rounds=[jl.rnd("2025-11-05", "Seed", 8_000_000, None, None, CTECH_DUALBIRD, "press"),
                   jl.rnd("2025-11-05", "Series A", 17_000_000, "Lightspeed Venture Partners", True, CTECH_DUALBIRD, "press")],
           note="FPGA-based acceleration of data processing. CTech (2025-11-05) ties Bessemer to the $17M Series A that Lightspeed led; the $8M seed announced with it names no investors, and the company's release speaks only of 'combined Seed and Series A funding' from the same four firms, so the Series A is read as the entry at medium confidence. CTech calls it an Israeli startup; Tel Aviv as the Lightspeed row carries, while the company's release is datelined Boston. Momentum check (nq, 2026-10-06): no round after November 2025 and nothing near $1B."),

    jl.verdict("earthly", "member",
               "VC News Daily (2020-10-12), carrying the company's release: 'Earthly Technologies has received a $2M Seed funding round led by 468 Capital', which 'led the round, joined by Uncorrelated Ventures, Bessemer Venture Partners, Hack VC' and founders of developer platforms. The FinSMEs page in the recall note would not open (403), so the copy read is cited.",
               ec="web", conf="high", cite=VCND_EARTHLY),
    jl.cls("earthly", status="private", rng="below_1b",
           stage="Seed", stage_src="web_verified", stage_cite=VCND_EARTHLY, stage_conf="high", entry_date="2020-10",
           country="US", city="Redwood City", city_src="web_verified", focus="DevTools & APIs",
           rounds=[jl.rnd("2020-10", "Seed", 2_100_000, "468 Capital", True, VCND_EARTHLY, "press"),
                   jl.rnd("2021", "Seed+", 6_500_000, "Innovation Endeavors", False, TC_EARTHLY, "press")],
           note="Build automation and CI tooling; the seed release is datelined Redwood City and the company's site is live (2026-10-06, now selling Earthly Lunar). Bessemer joined the seed of October 2020 that 468 Capital led ($2M in the release, $2.1M by the company's later count). TechCrunch (2023-02-23) reports a $6.5M 'seed plus' round closed in 2021, led by Innovation Endeavors with 468 Capital and Uncorrelated: a seed extension, not a named later round. Graduation left for the graduation pass."),

    jl.cls("engim", status="defunct", rng="below_1b", stage="undetermined", entry_date="2002",
           country="US", city="Acton", city_src="web_verified", focus="Industrial & Robotics", flags=["model_disputes_source"],
           rounds=[jl.rnd("2003-08-19", "Series B", 18_500_000, "Benchmark Capital", True, ENGIM_B, "press")],
           note="Fabless wireless LAN chip developer, Acton, Massachusetts (Light Reading, 2003-08-19); the prefilled IT is a wrong name match. That report has Benchmark leading the $18.5M Series B with 'existing investors Matrix Partners and Bessemer Venture Partners', so Bessemer entered in an earlier round that no source read names; "
                + FIRST_YEAR.format(y="2002")[0].lower() + FIRST_YEAR.format(y="2002")[1:]
                + ". The status follows the Benchmark row (defunct): no closure report was read in this pass, and Light Reading's last item is from September 2005, when its co-founding technologist left."),
    jl.cls("excara", status="unknown", rng="below_1b", stage="undetermined", entry_date="1999",
           country="US", focus="SaaS", flags=["city_unknown", "country_prior"], extra=PRIOR(), rounds=[],
           note="Online content and commerce software for manufacturers, listed by the firm in 2000 only (its investment year 1999, Joanna Strober). Wikipedia, Google News and EDGAR full text carry no trace of it, so the status reads unknown and no round is named. The country is inferred from the firm's US desk of 1999; no source places the company."),
    jl.cls("express-action", status="unknown", rng="below_1b", stage="undetermined", entry_date="2000",
           country="US", focus="SaaS", flags=["city_unknown", "country_prior"], extra=PRIOR(), rounds=[],
           note="Global e-commerce fulfillment services, listed by the firm in 2000 only (its investment year 2000, David Cowan). Wikipedia and Google News carry no trace of it and the name is too generic for EDGAR full text, so the status reads unknown and no round is named. The country is inferred from the firm's US desk of 2000; no source places the company."),
    jl.cls("formation-systems", status="acquired", rng="below_1b", stage="undetermined", entry_date="1998",
           country="US", city="Southborough", focus="SaaS", rounds=[],
           note="Product development software for process manufacturers; Southborough, Massachusetts, as the Bain Capital Ventures row carries. Engineering.com (2015-03-05) on Infor: 'It acquired Formation Systems in 2005 that led to its Optiva PLM process solution' (acq. by Infor, 2005; the Lightspeed row dates the sale 2006). The entry year 1998 is the firm's own; no round named."),

    jl.verdict("fuel-me", "member",
               "The company's own release (PR Newswire, 2024-03-20): the $18M Series A was 'co-led by Pritzker Group Venture Capital and Tribeca Venture Partners', and 'Other new investors include Bessemer Venture Partners, Interplay Venture Capital, FJ Labs, HPA (Hyde Park Angels)'.",
               ec="web", conf="high", cite=RC("fuel-me")),
    jl.cls("fuel-me", status="private", rng="below_1b",
           stage="Series A", stage_src="web_verified", stage_cite=RC("fuel-me"), stage_conf="high", entry_date="2024-03-20",
           country="US", city="Chicago", city_src="web_verified", focus="SaaS",
           rounds=[jl.rnd("2024-03-20", "Series A", 18_000_000, "Pritzker Group Venture Capital and Tribeca Venture Partners", True,
                          RC("fuel-me"), "company")],
           note="Fuel procurement and management platform for fleets, Chicago (the release's dateline). The company's release of 2024-03-20 names Bessemer among the new investors in the $18M Series A, so that round is the entry. Google News (2026-10-06) shows no later round."),

    jl.cls("genoa", status="acquired", rng="below_1b", stage="undetermined", entry_date="2002",
           city="Fremont", city_src="web_verified", focus="Industrial & Robotics", rounds=[],
           note="Linear optical amplifier chips, headquartered in Fremont, California. Light Reading (2003-04-01): Finisar agreed to acquire Genoa for about seven million Finisar shares, roughly $5.5M (acq. by Finisar, 2003). "
                + FIRST_YEAR.format(y="2002") + "; no round named."),
    jl.cls("gotham-networks", status="defunct", rng="below_1b", stage="undetermined", entry_date="2002",
           country="US", city="Acton", focus="Data Infrastructure", rounds=[],
           note="High-speed networking equipment for carriers; Acton, Massachusetts, from knowledge. Light Reading (2002-06-28) quotes an investor: 'the company shut down this week'; its report of 2003-01-23 on the Bessemer partner on the deal says Gotham 'has closed its doors'. "
                + FIRST_YEAR.format(y="2002") + "; the investment itself was earlier, and no round is named."),
    jl.cls("hatteras-networks", status="acquired", rng="below_1b", stage="undetermined",
           country="US", city="Durham", focus="Data Infrastructure",
           rounds=[jl.rnd("2001-03", "second round", None, None, True, HATTERAS_2, "press")],
           note="Ethernet-over-copper access equipment, Research Triangle Park, North Carolina (written Durham; from knowledge). Light Reading (2001-03-07): the second round came from 'Bessemer Venture Partners, Columbia Capital, and ComVentures', all investors in the first round, so Bessemer entered at a first round that no source read names or dates; no entry date is written (the firm first listed it in 2002, after that). Merged into Overture Networks in March 2011, the combined company keeping the Overture name (Light Reading, 2011-03-01; Wikipedia, Overture Networks): acq. by Overture Networks, 2011."),
    jl.cls("infiniswitch", status="unknown", rng="below_1b", stage="undetermined", entry_date="2002",
           country="US", city="Westborough", focus="Data Infrastructure", rounds=[],
           note="InfiniBand switch maker; Westborough, Massachusetts, from knowledge. Voltaire's 2007 prospectus has its sales chief there in 2003 and a venture lender's 10-K still carried a loan to it for that year; a merger with Lane15 Software is recalled but no source read confirms it, so the status reads unknown. "
                + FIRST_YEAR.format(y="2002") + "; no round named."),
    jl.cls("intersect-software", status="unknown", rng="below_1b", stage="undetermined", entry_date="2002",
           country="US", focus="SaaS", flags=["city_unknown", "country_prior"], extra=PRIOR(), rounds=[],
           note="Project management software for engineering departments, listed by the firm in 2002 and 2003 (Rob Soni). EDGAR full text shows it only in a venture investor's list of board seats (2005); nothing read says what became of it, so the status reads unknown. The country is inferred from the firm's US desk; "
                + FIRST_YEAR.format(y="2002")[0].lower() + FIRST_YEAR.format(y="2002")[1:] + ". No round named."),
    jl.cls("itc-deltacom", rng="below_1b", stage="undetermined", entry_date="1996",
           country="US", city="Huntsville", focus="Data Infrastructure", clear=["stale"], rounds=[],
           note="Regional telecom carrier funded by ITC Holding (a row of its own), public from October 1997 and acquired by EarthLink in December 2010 (Wikipedia, Deltacom). Based in West Point, Georgia at the listing and in Huntsville, Alabama when it was sold (from knowledge). The entry year 1996 is the firm's own; no round named."),
    jl.cls("kirana-networks", status="unknown", rng="below_1b", stage="undetermined", entry_date="2001-01",
           country="US", city="Red Bank", focus="Data Infrastructure",
           rounds=[jl.rnd("2001-01", "first round", 20_000_000, None, True, KIRANA, "press")],
           note="All-optical switch start-up; Red Bank, New Jersey, from knowledge. Light Reading (2003-01-27): a $20M first round in January 2001 with Bessemer and Columbia Capital, the company then hiring and seeking a second round of $30M. Nothing read after that says what became of it, so the status reads unknown, and the first round carries no name, so the stage stays undetermined."),
    jl.cls("lumerx", status="unknown", rng="below_1b", stage="undetermined", entry_date="2004",
           country="US", focus="Healthcare & Bio", flags=["city_unknown", "country_prior"], extra=PRIOR(), rounds=[],
           note="Visible-light therapy for peptic ulcer disease, listed by the firm from 2004 to 2007 (Christopher Gabrieli). Wikipedia, Google News and EDGAR full text carry no trace of it, so the status reads unknown. The country is inferred from the firm's US desk; "
                + FIRST_YEAR.format(y="2004")[0].lower() + FIRST_YEAR.format(y="2004")[1:] + ". No round named."),

    jl.verdict("measurex", "member",
               "Named on the firm's own history page (bvp.com, captured 2008-11-20): 'Pete Bancroft joined Bessemer in 1967 to lead the venture practice. Some of his signature deals were Measurex, Fotomat, and Interdata.' A deal of the venture group before the 1981 spin-out, IN under decisions.md R2 and X1.",
               ec="web", conf="high", cite=RC("measurex")),
    jl.cls("measurex", status="acquired", rng="below_1b", stage="undetermined",
           country="US", city="Cupertino", city_src="web_verified", focus="Industrial & Robotics",
           flags=["pre_spinout", "model_disputes_source"], rounds=[],
           note="Process control systems for paper making, Cupertino, California. Wikipedia (Measurex): it opened in January 1968, went public in March 1972 and 'was acquired by Honeywell in March 1997' for almost $600M, so the prefilled defunct is disputed (acq. by Honeywell, 1997), as the Sutter Hill row reads. The firm's history page names the deal without a year or a round: the entry falls between 1968 and the 1972 listing and no date is written."),

    jl.cls("mindshift-technologies", status="acquired", rng="below_1b", stage="undetermined", entry_date="2002",
           country="US", city="Waltham", focus="SaaS", rounds=[],
           note="Managed IT services for small and medium businesses; Waltham, Massachusetts, from knowledge. Best Buy bought it in 2011 (Wired headline, 2011-11-07) and sold it on in 2014: 'Ricoh today announced that the company has reached an agreement to buy mindSHIFT Technologies Inc.' from Best Buy (Yahoo Finance, 2014-01-21). Acq. by Best Buy, 2011. "
                + FIRST_YEAR.format(y="2002") + "; no round named."),

    jl.verdict("moxie-beauty", "member",
               "The firm's own post of 2025-12-16 announces that Bessemer led Moxie Beauty's $15M Series A; Entrackr (same day): the round was 'led by Bessemer Venture Partners', with existing backer Fireside Ventures.",
               ec="web", conf="high", cite=RC("moxie-beauty")),
    jl.cls("moxie-beauty", status="private", rng="below_1b",
           stage="Series A", stage_src="first_party", stage_cite=MOXIE_POST, stage_conf="high", entry_date="2025-12-16",
           country="IN", country_src="web_verified", country_cite=ENTRACKR_MOXIE, city="Gurugram", city_src="web_verified",
           focus="Consumer & Marketplaces",
           rounds=[jl.rnd("2023-04", "Seed", 669_000, "Amplify Partners and OTP Venture Partners", False, ENTRACKR_MOXIE, "press"),
                   jl.rnd("2024-07", "venture round", 2_100_000, "Fireside Ventures", False, ENTRACKR_MOXIE, "press"),
                   jl.rnd("2025-12-16", "Series A", 15_000_000, "Bessemer Venture Partners", True, MOXIE_POST, "firm")],
           note="Haircare brand for Indian hair, 'the Gurugram-based brand' (Entrackr, 2025-12-16). The firm's own post announces the $15M Series A it led in December 2025; Entrackr lists the two earlier rounds (April 2023 and July 2024) without Bessemer, so the Series A is the entry."),
]

jl.write("d3a", lines)
