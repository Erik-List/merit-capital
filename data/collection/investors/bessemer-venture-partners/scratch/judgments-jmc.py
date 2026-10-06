"""PRO-80 Bessemer, judge jm, file c: alumni seats dated outside the Bessemer window and homonyms (batches 21 to 25):
Ambar Bhattacharyya, Anna Khan, David Cowan (mining), John Drake, Matthew Salzberg, Michael Horowitz, Adam Fisher,
Justin Label, Kristina Shen, Mackey Craven, Mark Lurie. All not_member: none of these issuers is on the firm's own
list (live or archived) or its deal-partner map, and no source ties a Bessemer fund to any of them.
"""
import judge_lib as jl

NM = "not_member"
EC = "formd_adjudicated"
lines = []
TAIL = " The issuer is not on the firm's own list or deal-partner map and no Bessemer fund appears in its rounds."


def nm(slug, basis, conf="high"):
    lines.append(jl.verdict(slug, NM, basis + TAIL, ec=EC, conf=conf))


# ---- Ambar Bhattacharyya: vice president in the Cambridge office (team pages 2014 to 2015); then Maverick Ventures
AB = ("Seat outside the person's Bessemer window (decisions.md D6): Ambar Bhattacharyya is on the firm's team pages in "
      "2014 and 2015 only and then moved to Maverick Ventures. ")
nm("cityblock-health-inc", AB + "His Cityblock board seat runs from the 2018 filing to 2021, his Maverick years.")
nm("daymark-health-inc", AB + "The 2025 filing dates from his Maverick years.")
nm("tulea-health-inc", AB + "The 2025 filing dates from his Maverick years.")
nm("blueflag-security-inc", AB + "The 2026 filing dates from his Maverick years.")

# ---- Anna Khan: team pages 2013 to 2019; then CRV (decisions.md D6 / the brief's seat list)
AK = ("Seat outside the person's Bessemer window (decisions.md D6): Anna Khan is last on the firm's team page in 2019 and "
      "then became a general partner at CRV. ")
nm("figure-solutions-inc", AK + "The 2021 filing dates from her CRV years.")
nm("cord-technologies-inc", AK + "The 2021 and 2024 filings date from her CRV years.")
nm("bateau-inc", AK + "The 2022 filing dates from her CRV years.")
nm("northspyre-inc", AK + "The 2022 filing dates from her CRV years.")

# ---- David Cowan: the Bessemer partner's namesake on Canadian mining issuers
DC = ("Form D name match only, a homonym (decisions.md D6 names David Cowan as a common roster name): the director of "
      "this Canadian junior mining issuer is another David Cowan, not the Bessemer partner, whose seats are technology "
      "companies on the firm's deal-partner map. ")
nm("kincora-copper-ltd", DC + "Kincora Copper is a listed Vancouver explorer (filings 2011 to 2014).")
nm("khayyam-minerals-ltd", DC + "Khayyam Minerals is a Canadian explorer (filing 2012).")
nm("forum-energy-metals-corp", DC + "Forum Energy Metals is a listed Vancouver uranium explorer (filings 2021 to 2023).")

# ---- John Drake: Investor on the team pages 2022 to 2026
JD = ("Form D name match only, a homonym (decisions.md D6 / the brief's homonym list): Bessemer's John Drake is an "
      "investor on the team pages from 2022, and this filing predates his window and names another person. ")
nm("critical-outcome-technologies-inc", JD + "The director of this London, Ontario drug developer (2013 to 2017) is a Canadian namesake.")
nm("cotinga-pharmaceuticals-inc", JD + "Cotinga is Critical Outcome Technologies renamed (the same SEC registrant); its 2018 director is a Canadian namesake.")
nm("faction-holdings-inc", JD + "The 2015 to 2018 filings name an executive officer of the issuer, an operator.")
nm("voxtur-analytics-corp", JD + "The 2021 director of this listed Canadian company is a namesake.")
nm("pathfinder-therapeutics-inc", JD + "The 2013 filing names a 'Johnny Drake' as an executive officer of the issuer, an operator.")

# ---- Matthew Salzberg: on the team page in 2012, then founder of Blue Apron (a Bessemer company); later his own seats
MZ = ("Seat outside the person's Bessemer window (decisions.md D6): Matt Salzberg is on the firm's team page in 2012 only "
      "and left to found Blue Apron; his later board seats are his own. ")
nm("embark-veterinary-inc", MZ + "He is a director of Embark on the 2015 to 2021 filings, a personal seat.")
nm("suma-brands-inc", MZ + "He is a director and executive officer of Suma Brands (2021 to 2024), a company he co-founded.")
nm("unlimited-funds-inc", MZ + "The 2023 filing names him a director, a personal seat.")
nm("coldcart-inc", MZ + "The 2024 filing names him a director, a personal seat.")

# ---- Michael Horowitz: investor in the New York office from July 2010 (team pages 2013 to 2014); a common name
MH = ("Form D name match only: Bessemer's Michael Horowitz was an investor in the New York office (team pages 2013 to "
      "2014), a common name; the filing names an executive officer of the issuer, an operator and not an investor seat. ")
nm("ebrisk-video-inc", MH + "eBrisk Video is a Canadian company (2012 filing).")
nm("bridg-inc", MH + "The Bridg filing is from 2017, after his window.")
nm("notable-labs-inc", MH + "The Notable Labs filing is from 2019, after his window.")
nm("modulo-bio-inc", MH + "The Modulo Bio filings are from 2021 to 2024, after his window.")

# ---- Adam Fisher: partner in the Israel office since 2007; a common name
AF = ("Form D name match only, a homonym (decisions.md D6 names Adam Fisher as a common roster name): Bessemer's Adam "
      "Fisher leads the Israel office and his seats are Israeli technology companies on the firm's deal-partner map. ")
nm("glycobia-inc", AF + "The director of this Ithaca, New York biotech (2010) is another person.")
nm("katerra-inc", AF + "The Katerra director on the 2018 filings (rounds of $0.8B and $1.0B led by SoftBank) is another person.")
nm("one-river-digital-asset-management-llc", AF + "The executive officer of this Connecticut asset manager (2021) is another person, and the issuer is a fund manager, not a venture round.")

# ---- Justin Label: on the firm's team page until 2010; then Inovia Capital
JL = ("Seat outside the person's Bessemer window (decisions.md D6): Justin Label is last on the firm's team page in 2010 "
      "and then joined another venture firm (Inovia). ")
nm("redbooth-inc", JL + "The Redbooth filing is from 2014.")
nm("greynoise-intelligence-inc", JL + "The GreyNoise filing is from 2020.")
nm("phin-security-inc", JL + "The Phin Security filing is from 2026.")

# ---- Kristina Shen: team pages 2014 to 2019; Andreessen Horowitz from 2019
KS = ("Seat outside the person's Bessemer window (decisions.md D6): Kristina Shen is last on the firm's team page in 2019 "
      "and joined Andreessen Horowitz that year. ")
nm("mux-inc", KS + "Her Mux seat is on the 2020 and 2021 filings, her Andreessen Horowitz years (that book carries Mux).")
nm("matik-inc", KS + "Her Matik seat is on the 2021 filing, her Andreessen Horowitz years (that book carries Matik).")
nm("rutterapi-inc", KS + "Her Rutter seat is on the 2022 filing, her Andreessen Horowitz years.")

# ---- Mackey Craven: team pages 2013 to 2014; then OpenView
MC = ("Seat outside the person's Bessemer window (decisions.md D6): Mackey Craven is last on the firm's team page in 2014 "
      "and then became a partner at OpenView. ")
nm("jumpcloud-inc", MC + "His JumpCloud seat is on the 2017 to 2022 filings, his OpenView years.")
nm("gitprime-inc", MC + "His GitPrime seat is on the 2018 filing, his OpenView years.")
nm("kintent-inc", MC + "His Kintent seat is on the 2022 filing, his OpenView years.")

# ---- Mark Lurie: on the firm's team page in 2010 only; then a founder
ML = ("Mark Lurie is on the firm's team page in 2010 only and went on to found companies; the filing names him as an "
      "officer of the issuer, an operator job and not a fund position (decisions.md D4, D6). ")
nm("westonian-group-inc", ML + "He is a director and executive officer of Westonian Group in 2009 to 2011, his own company.")
nm("hammerless-inc", ML + "He is an executive officer of Hammerless in 2014.")
nm("codex-labs-inc", ML + "He is an executive officer of Codex Labs in 2018.")

assert len(lines) == 39, len(lines)
jl.write("jmc", lines)
