"""Second pass s24, file a: rows first seen 1970 to 1997 (queue/s2-4.json). Only rows that change."""
import judge_lib as jl
from judge_lib import cls, verdict, rnd, ARCH, W

FP, WV = "first_party", "web_verified"
BVP = "Bessemer Venture Partners"
PLACEHOLDER = ("the lower year on the firm's 2013 to 2015 listings and on the live site is the January 1 "
               "placeholder rendered one year early")
# VeriSign's IPO registration statement (January 1998), the citation the Kleiner Perkins row carries; read here.
VRSN_S1 = "https://www.sec.gov/Archives/edgar/data/1014473/0000898430-98-000012.txt"
# Tumbleweed's S-1 of 2000-07-11 (EDGAR filing index printed by the listing query; the full text was read).
TMWD_S1 = "https://www.sec.gov/Archives/edgar/data/1022509/000091205700031540/0000912057-00-031540-index.htm"

L = []

L.append(cls("four-phase-systems", entry_date="1971",
             note="Entry date corrected to 1971: the firm's own sentence says Neill Brownstein invested in 1971, and "
                  + PLACEHOLDER + ". The sentence names no round, so the stage stays undetermined."))

L.append(cls("telenet", stage="Series A", stage_src=FP, stage_cite=ARCH("telenet"), stage_conf="medium",
             city="McLean", city_src="web_verified",
             rounds=[rnd("1975", "first of three rounds", None, None, True, ARCH("telenet"), "firm")],
             note="The firm's archived text says BVP invested in all three of Telenet's rounds, starting in 1975; the "
                  "first round reads Series A because nothing in the record suggests an earlier seed (Wikipedia: the "
                  "company announced its venture capital in January 1975 after a two-year search). Wikipedia places "
                  "it in McLean, Virginia before GTE bought it in 1979 and moved it to Reston."))

L.append(cls("gartner-group", stage="Series A", stage_src=FP, stage_cite=ARCH("gartner-group"), stage_conf="medium",
             rounds=[rnd("1979", "original venture round", None, BVP, True, ARCH("gartner-group"), "firm")],
             note="The firm's archived text says Neill Brownstein participated in Gartner's original venture round in "
                  "1979, and its older text that he led the initial investment; Gartner was founded that year and "
                  "nothing suggests an earlier seed, so the first round reads Series A."))

L.append(cls("dysan", status="acquired", stage="Growth", stage_src=FP, stage_cite=ARCH("dysan"), stage_conf="high",
             entry_date="1979",
             rounds=[rnd("1979", "expansion round", None, None, True, ARCH("dysan"), "firm")],
             note="The firm's archived text says BVP invested in Dysan's 1979 expansion round, seven years after the "
                  "founding, so Growth. Status corrected to acquired: Dysan merged with Xidex in spring 1984 "
                  "(Wikipedia), as the Menlo row reads; Sequoia's row still reads defunct."))

L.append(cls("trenwick", stage="Series A", stage_src=FP, stage_cite=ARCH("trenwick"), stage_conf="medium",
             rounds=[rnd("1979", "first round", None, None, True, ARCH("trenwick"), "firm")],
             note="The firm's archived text says BVP invested in the first round in 1979; with no sign of an earlier "
                  "seed that reads Series A."))

L.append(cls("maxim-integrated-products", stage="Series A", stage_src=FP,
             stage_cite=ARCH("maxim-integrated-products"), stage_conf="medium",
             rounds=[rnd("1983", "first of three rounds", None, None, True, ARCH("maxim-integrated-products"), "firm")],
             note="The firm's archived text says BVP invested in Maxim's first three rounds, starting in 1983, the "
                  "year the company was founded; the first round reads Series A, with no sign of an earlier seed."))

L.append(cls("staples", stage="Series A", stage_src=FP, stage_cite=ARCH("staples"), stage_conf="medium",
             entry_date="1986-01",
             rounds=[rnd("1986-01", "first of four rounds", None, None, True, ARCH("staples"), "firm")],
             note="The firm's archived text and its 2008 history page say Felda Hardymon and Bill Burgin invested in "
                  "each of Staples' four rounds, starting in 1986; the first round reads Series A, with no sign of an "
                  "earlier seed. The firm's 2002 site dates the investment January 1986."))

L.append(cls("enzytech", stage="Series A", stage_src=FP, stage_cite=ARCH("enzytech"), stage_conf="medium",
             entry_date="1987",
             rounds=[rnd("1987", "first of six rounds", None, None, True, ARCH("enzytech"), "firm")],
             note="The firm's archived text says Chris Gabrieli invested in all six of Enzytech's rounds, so from the "
                  "first, which reads Series A with no sign of an earlier seed. Entry date corrected to 1987, the "
                  "year the firm gives for the founding and for its investment; " + PLACEHOLDER + "."))

L.append(cls("pillar", entry_date="1988",
             note="Entry date corrected to 1988, the year on the firm's 2010 to 2012 and 2016 to 2017 listings; "
                  + PLACEHOLDER + ". The firm's text names no round and no city."))

L.append(cls("focus-healthcare-management", status="acquired", rng="below_1b", country="US", city="Brentwood",
             focus="Healthcare & Bio", clear=["identity_unresolved", "country_unknown"],
             note="Identified from the firm's archived description: a manager of the healthcare cost of workers' "
                  "compensation, founded in 1986; BVP invested in its early rounds (no round named, so the stage "
                  "stays undetermined) and exited in 1994; Focus merged with CRA Managed Care in 1996, which became "
                  "Concentra, and Wikipedia's Concentra article still lists Focus Healthcare Management as a "
                  "subsidiary. Brentwood, Tennessee is from memory."))

L.append(verdict("centocor", "not_member",
                 "Public-market purchase (decisions.md D5 and R3, T3): the firm's own list dates its Centocor "
                 "investment 1989, and Centocor had been a publicly traded company since 1982 (Wikipedia, Centocor); "
                 "no Bessemer round from before the listing is on record.",
                 ec="site_listing", cite=ARCH("centocor"), conf="medium"))

L.append(cls("opta-food-ingredients", entry_date="1991",
             note="Entry date corrected to 1991: the firm's own sentence says Chris Gabrieli led BVP's 1991 investment "
                  "in Opta, the year Enzytech spun it out; " + PLACEHOLDER + ". No round is named."))

L.append(cls("cascade-communications", entry_date="1992-08",
             note="Entry date set to August 1992, the month the firm's 2002 site gives. The firm's older text calls "
                  "Felda Hardymon one of the initial investors and its later text says he invested in the early "
                  "rounds; the company was founded in 1990, so the wording does not settle whether that was the "
                  "first round, and the stage stays undetermined."))

L.append(cls("verisign", stage="Seed", stage_src=FP, stage_cite=ARCH("verisign"), stage_conf="medium",
             entry_date="1995-04", grad="graduated", grad_src=WV, grad_cite=VRSN_S1, grad_conf="high",
             rounds=[rnd("1995-04", "common stock at formation and Series A preferred", 5168260, None, True, VRSN_S1, "filing"),
                     rnd("1996-02", "Series B", 5142851, None, None, VRSN_S1, "filing"),
                     rnd("1996-11", "Series C", None, None, None, VRSN_S1, "filing")],
             note="The firm's archived text says David Cowan co-founded VeriSign and that BVP seeded it as a spin-out "
                  "from RSA, so Seed. The IPO registration statement shows Bessemer Venture Partners DCI buying "
                  "258,333 common shares at $0.12 at formation in April 1995 and 850,000 shares of the Series A "
                  "preferred sold the same month at $1.20; the filing's own label for that preferred is Series A, "
                  "which a reviewer may prefer. Graduated: the same filing records the Series B of February 1996 "
                  "and the Series C of November 1996."))

L.append(cls("netsys", stage="Series A", stage_src=FP, stage_cite=ARCH("netsys"), stage_conf="high",
             entry_date="1995",
             rounds=[rnd("1995", "Series A", None, BVP, True, ARCH("netsys"), "firm")],
             note="The firm's archived text says David Cowan and Felda Hardymon led the company's Series A round in "
                  "1995. Entry date corrected to 1995; " + PLACEHOLDER + "."))

L.append(cls("travcorps", stage="Series A", stage_src=FP, stage_cite=ARCH("travcorps"), stage_conf="medium",
             rounds=[rnd("1995", "first institutional round", None, None, True, ARCH("travcorps"), "firm")],
             note="The firm's archived text says BVP invested in TravCorps' first institutional round in 1995, which "
                  "reads Series A; in 1999 the company merged with Cross Country Staffing."))

L.append(cls("zany-brainy", rng="below_1b",
             note="Band filled: the company went through Chapter 11 in 2001 and its last stores closed in 2003 "
                  "(Wikipedia), so below $1B. The firm's listing gives only the year 1995 and no round."))

L.append(cls("nbx", stage="Growth", stage_src=FP, stage_cite=ARCH("nbx"), stage_conf="medium", entry_date="1997",
             city="Andover",
             rounds=[rnd("1997", "later-stage round", None, None, True, ARCH("nbx"), "firm")],
             note="The firm's archived text says Rob Chandra invested in the later stages of the company in 1997, so "
                  "Growth. Entry date corrected to 1997; " + PLACEHOLDER + ". City corrected to Andover, "
                  "Massachusetts, where NBX was based when 3Com bought it (from memory)."))

L.append(cls("tumbleweed", stage="Growth", stage_src=FP, stage_cite=ARCH("tumbleweed"), stage_conf="medium",
             rng="below_1b",
             rounds=[rnd("1997", "recapitalization", None, None, True, ARCH("tumbleweed"), "firm"),
                     rnd("1997-08", "Series B", None, None, None, TMWD_S1, "filing")],
             note="The firm's archived text says David Cowan participated in the company's 1997 recapitalization, "
                  "which reads Growth. Tumbleweed's S-1 of July 2000 shows the only preferred sold in 1997 was the "
                  "Series B of August and September 1997 (August Capital, Draper Fisher, Adobe Ventures among "
                  "others; Bessemer is not named among the 5% holders). Band filled: acquired by Axway in 2008."))

L.append(cls("castle-networks", stage="Series A", stage_src=FP, stage_cite=ARCH("castle-networks"),
             stage_conf="medium",
             rounds=[rnd("1998", "first institutional financing (first of two venture rounds)", None, None, True,
                         ARCH("castle-networks"), "firm")],
             note="The firm's archived text says the company raised only two venture rounds and BVP participated in "
                  "both, the first being its first institutional financing just over a year before the 1999 sale to "
                  "Siemens' Unisphere; that first round reads Series A."))

L.append(cls("quantum-effect-devices", status="acquired",
             note="Status filled: the firm lists the company as acquired by PMC-Sierra in 2000, the year of its IPO, "
                  "as the Lightspeed row reads."))

L.append(cls("epic-therapeutics", entry_date="1999",
             note="Entry date corrected to 1999, the year on the firm's 2010 to 2012 and 2016 to 2019 listings; "
                  + PLACEHOLDER + ". The firm's text names no round."))

jl.write("s24a", L)
