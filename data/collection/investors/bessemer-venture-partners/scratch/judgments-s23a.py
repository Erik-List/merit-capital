"""PRO-80 Bessemer, second pass s23, file a: the pre-2005 rows of queue/s2-3.json that change.
Run as NQ_TAG=s23 python3 judgments-s23a.py."""
import judge_lib as jl
from judge_lib import ARCH, W, cls, rnd, verdict

BVP = "Bessemer Venture Partners"
GRAD = " Graduation left for the graduation pass."

L = []

# ---- entry date only: the firm's own archived sentence gives the year
L.append(cls("intersil-advanced-memory-systems", entry_date="1970",
             note="Entry date set to 1970: the firm's archived sentence says BVP invested in Advanced Memory Systems in 1970."))
L.append(cls("immulogic-pharmaceuticals", entry_date="1988",
             note="Entry date set to 1988: the firm's archived sentence says Chris Gabrieli invested in 1988; it names no round."))
L.append(cls("oclassen-pharmaceuticals", entry_date="1991",
             note="Entry date set to 1991: the firm's archived sentence says Chris Gabrieli participated in the 1991 financing, which names no round; acq. by Watson Pharmaceuticals, 1997, is the firm's own record."))
L.append(cls("impact-telecommunications", entry_date="1992",
             note="Entry date set to 1992: the firm's archived sentence says BVP invested in International Pacific Holdings in 1992; it names no round."))
L.append(cls("individual", entry_date="1993",
             note="Entry date set to 1993: the firm's 2000 listing says 'In 1993 BVP invested in Individual'; its later text adds the 1995 financing round, a follow-on. Neither names the round."))

# ---- first-party stage sentences
A = ARCH("oximetrix")
L.append(cls("oximetrix", stage="Growth", stage_src="first_party", stage_cite=A, stage_conf="high", entry_date="1978",
             city="Mountain View",
             rounds=[rnd("1978", "later financing", None, None, True, A, "firm")],
             note="The firm's archived sentence: 'BVP participated in the later financings of this medical device manufacturer, starting in 1978', a later round, so Growth. Oximetrix was based in Mountain View, California (from knowledge)."))

A = ARCH("syntrex")
L.append(cls("syntrex", status="defunct", stage="Series A", stage_src="first_party", stage_cite=A, stage_conf="medium",
             entry_date="1979",
             rounds=[rnd("1979", "first financing round", None, None, True, A, "firm")],
             note="The firm's archived sentence says BVP participated in all three of Syntrex's financing rounds before the IPO, so it entered in the first round of a company founded in 1979; read as Series A, nothing suggests an earlier seed. "
                  "Wikipedia: Syntrex went bankrupt and its assets were sold off in pieces in 1992 (" + W("Syntrex") + "), so defunct."))

A = ARCH("kronos")
L.append(cls("kronos", stage="Series A", stage_src="first_party", stage_cite=A, stage_conf="medium", entry_date="1980",
             rounds=[rnd("1980", "first round", None, None, True, A, "firm")],
             note="The firm's archived sentence: 'BVP participated in its first two rounds, starting in 1980'; the first round reads Series A, nothing suggests an earlier seed. Entry date follows that sentence."))

A = ARCH("perseptive-biosystems")
L.append(cls("perseptive-biosystems", stage="Growth", stage_src="first_party", stage_cite=A, stage_conf="high",
             entry_date="1989-12",
             rounds=[rnd("1989-12", "second round", None, None, True, A, "firm")],
             note="The firm's archived sentence: Chris Gabrieli 'invested in the company's second round in December 1989', so Growth."))

A = ARCH("chrysalis-symbolic-design")
L.append(cls("chrysalis-symbolic-design", stage="Seed", stage_src="first_party", stage_cite=A, stage_conf="high",
             entry_date="1994",
             rounds=[rnd("1994", "Seed", None, None, True, A, "firm")],
             note="The firm's archived sentence: 'BVP participated in the 1994 seed round of Chrysalis ... and in each of its subsequent four financings'. Those later financings are not named." + GRAD))

CASC = "https://www.sec.gov/Archives/edgar/data/887763/0000887763-97-000007.txt"
A = ARCH("sahara-networks")
L.append(cls("sahara-networks", stage="Series A", stage_src="first_party", stage_cite=A, stage_conf="medium",
             entry_date="1995", city="Wallingford", city_src="web_verified",
             rounds=[rnd("1995", "first round", None, None, True, A, "firm")],
             note="The firm's archived sentence: 'BVP's Felda Hardymon invested in the company's first round'; read as Series A, nothing suggests an earlier seed. "
                  "Cascade's annual report places Sahara in Wallingford, Connecticut (" + CASC + "), which differs from the Greylock row's Sunnyvale."))

COWAN = "https://www.bvp.com/team/david-cowan"
L.append(cls("good-technology", stage="Seed", stage_src="first_party", stage_cite=COWAN, stage_conf="high",
             entry_date="1996",
             rounds=[rnd("1996", "founding round (incubated at the firm)", None, BVP, True, COWAN, "firm")],
             note="The firm's own page for David Cowan says he co-founded Good Technology (fka Visto) as one of three companies 'incubated within Bessemer's offices', serving as its CEO; the firm's 2000 listing dates Visto to 1996, its founding year. An incubation at founding reads Seed." + GRAD))

A = ARCH("newport-communications")
L.append(cls("newport-communications", stage="Growth", stage_src="first_party", stage_cite=A, stage_conf="high",
             entry_date="1999",
             rounds=[rnd("1999", "expansion round", None, None, True, A, "firm")],
             note="The firm's archived sentence: 'BVP invested in its 1999 expansion round', a later round, so Growth."))

A = ARCH("catena-networks")
L.append(cls("catena-networks", stage="Growth", stage_src="first_party", stage_cite=A, stage_conf="high",
             entry_date="1999", city="Redwood City",
             rounds=[rnd("1999", "later round", None, None, True, A, "firm")],
             note="The firm's archived sentence: 'BVP invested in the company's later rounds', so Growth. Catena was headquartered in Redwood Shores (Redwood City), California, with engineering in Kanata, Ontario (from knowledge); the stored Atlanta was a mistake."))

A = ARCH("wavesmith-networks")
L.append(cls("wavesmith-networks", stage="Series A", stage_src="first_party", stage_cite=A, stage_conf="medium",
             entry_date="2000-04-13",
             rounds=[rnd("2000-04-13", "first round", None, None, True, A, "firm")],
             note="The firm's archived sentence: 'BVP invested in every round' of a company founded in 2000, and its own date is 2000-04-13; the first round reads Series A, nothing suggests an earlier seed. Acton, Massachusetts is confirmed by Wikipedia's Ciena article."))

# ---- cited rounds
E14 = W("Element 14 Ltd.")
L.append(cls("element-14", stage="Series A", stage_src="web_verified", stage_cite=E14, stage_conf="medium",
             entry_date="1999",
             rounds=[rnd("1999", "first round", None, None, True, E14, "press"),
                     rnd("2000", "expansion rounds (two)", None, None, True, ARCH("element-14"), "firm")],
             note="Wikipedia: the company created in July 1999 'secured GBP 8.25 million in first-round funding from Bessemer Venture Partners, Atlas Ventures and Herman Hauser's Amadeus Capital Partners'; the first round of a new spin-out reads Series A. "
                  "The firm's own text adds that BVP took part in both expansion rounds of early 2000, which were follow-ons."))

# ---- status, city, rounds found without a stage
L.append(cls("echelon-systems", entry_date="1989", city="Santa Clara", city_src="web_verified",
             note="Entry date set to 1989 (the firm's archived sentence: 'BVP invested in 1989', no round named). Wikipedia places Echelon in Santa Clara, California at its 2018 sale to Adesto (" + W("Echelon Corporation") + ")."))

VX = W("Vision Express")
L.append(cls("vision-express-group", status="acquired", city="Ruddington", city_src="web_verified",
             note="Acq. by Grand Vision (Grand Optical Photoservices), 1997, the firm's own exit year; headquartered in Ruddington, Nottinghamshire (" + VX + "). The firm names no round."))

MAIN = "https://www.sec.gov/Archives/edgar/data/1068851/000119312503046720/d425.htm"
L.append(cls("mainbancorp", status="acquired", city="Dallas", city_src="web_verified",
             note="Read as MainBancorp, Inc., the privately held parent of Dallas based mainbank, n.a., which agreed in July 2003 to merge into Prosperity Bancshares (" + MAIN + "); acq. by Prosperity Bancshares, 2003, matching the firm's exit year. "
                  "No filing names Bessemer as a holder, so the identification rests on the name and the exit year. Outside the focus taxonomy."))

L.append(cls("aptis-communications", city="Chelmsford",
             note="Aptis was based in Chelmsford, Massachusetts when Nortel bought it in 1998 (from knowledge). The firm says it took part in both 1997 rounds, which names no round."))

L.append(cls("obsidian", entry_date="1998", city="Fremont",
             note="Entry date set to 1998 (the firm's archived sentence: 'BVP invested ... in 1998', no round named). Obsidian was based in Fremont, California when Applied Materials bought it (from knowledge)."))

SON = "https://www.sec.gov/Archives/edgar/data/1105472/0000912057-00-025719.txt"
L.append(cls("sonus-networks",
             rounds=[rnd("1997-11", "Series A (second close July 1998)", 7180000, None, None, SON, "filing"),
                     rnd("1998-09", "Series B (closes to May 1999)", 16021435, None, None, SON, "filing"),
                     rnd("1999-09", "Series C", None, None, None, SON, "filing"),
                     rnd("2000-03", "Series D", None, None, None, SON, "filing")],
             note="Sonus's 2000 registration statement lists the Series A (November 1997 and July 1998), B, C and D rounds and their large holders (Matrix, North Bridge, Charles River, Bedrock) and never names Bessemer, whose holding was below the disclosure line. "
                  "The firm says only that Hardymon invested in 1997, so the round stays undetermined."))

MF = W("Multiflow")
L.append(cls("multiflow-computers",
             rounds=[rnd("1985-01", "first round", None, None, None, MF, "press")],
             note="Wikipedia: Multiflow closed its first round of financing in January 1985 and shut down in March 1990; no source names Bessemer in a round, and the firm gives only the year 1985, so the stage stays undetermined."))

# ---- membership: a 1992 purchase of a company listed since 1984
CFC = "https://www.sec.gov/Archives/edgar/data/744778/0000950130-95-001946.txt"
L.append(verdict("commercial-federal", "not_member",
                 "Public-market purchase with no earlier private round (decisions.md D5 and R3, T3): Commercial Federal Corporation of Omaha "
                 "has been a public company since the bank's conversion from mutual to stock ownership on 1984-12-31 and its shares trade on the "
                 "New York Stock Exchange (its annual report), while the firm's list dates the Bessemer investment to 1992 and gives no round, "
                 "description or exit. The annual report names no Bessemer holding.",
                 ec="web", conf="medium", cite=CFC))

jl.write("s23a", L)
