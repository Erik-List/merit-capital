"""PRO-100 NEA stage pass, tag s4, first half (51 rows). Entry-round research per STAGE-BRIEF.md.
Rounds already on file are kept and the new ones appended (funding_rounds replaces on record)."""
import json

import judge_lib as jl
from judge_lib import cls, rnd, NEWS, GNEWS, POST, FORMD_ROUNDS

CLS = json.loads((jl.INV / "companies/classification.json").read_text())
BASE = {r["slug"]: r for r in json.loads((jl.INV / "companies/base.json").read_text())}


def R(slug, *new):
    """Rounds on file plus the new ones (deduplicated on date and round)."""
    out = list((CLS.get(slug) or {}).get("funding_rounds") or [])
    for n in new:
        if not any(o.get("date") == n["date"] and o.get("round") == n["round"] for o in out):
            out.append(n)
    return out


def FD(slug, i=0):
    """The i-th Form D link on the row itself (base.json formd_links)."""
    return [x.strip() for x in (BASE[slug].get("formd_links") or "").split(";") if x.strip()][i]


# SEC documents read this pass (URLs printed by scratchpad/s4/edg.py from each registrant's EDGAR index)
NEVRO_424B4 = "https://www.sec.gov/Archives/edgar/data/1444380/000104746914008881/a2222100z424b4.htm"
ROKA_S1 = "https://www.sec.gov/Archives/edgar/data/1472343/000119312514208158/d623882ds1.htm"
BLOOM_424B4 = "https://www.sec.gov/Archives/edgar/data/1664703/000119312518227590/d96446d424b4.htm"
ACTELIS_424B4 = "https://www.sec.gov/Archives/edgar/data/1141284/000121390022027163/f424b40522_actelisnetwork.htm"
SENSE_424B4 = "https://www.sec.gov/Archives/edgar/data/1616543/000104746916011346/a2227881z424b4.htm"
# press pages read this pass (WebSearch result, then WebFetch)
TC_MASTERCLASS = "https://techcrunch.com/2016/02/23/masterclass-raises-15-million-for-online-classes-taught-by-celebrities/"
TT_TRANSFIX = "https://www.ttnews.com/articles/transfix-receives-22-million-funding"

GN = "Google News (nq.py)"
L = []

# ---- staged rows
L.append(cls("masterclass", stage="Growth", stage_src="web_verified", stage_cite=TC_MASTERCLASS, stage_conf="high",
             entry_date="2016-02-23",
             rounds=R("masterclass",
                      rnd(None, "Series A", 4500000, "Javelin Venture Partners", None, TC_MASTERCLASS, "press"),
                      rnd("2016-02-23", "Series B", 15000000, "NEA", True, TC_MASTERCLASS, "press")),
             note="Stage pass (s4): TechCrunch (2016-02-23) names the $15M Series B led by NEA and says it follows a "
                  "previously undisclosed $4.5M Series A led by Javelin; NEA's own posts show nothing earlier, so the "
                  "entry is the Series B (Growth). The firm's 2015 year reads as the close year."))

L.append(cls("transfix", stage="Growth", stage_src="web_verified", stage_cite=TT_TRANSFIX, stage_conf="high",
             entry_date="2016", clear=["stage_disputes_band"],
             rounds=R("transfix", rnd("2016", "Series B", 22000000, "NEA", True, TT_TRANSFIX, "press")),
             note="Stage pass (s4): Transport Topics reports the $22M Series B led by NEA in 2016, the year the firm "
                  "gives for its first investment, and NEA's posts show nothing earlier; the entry is that Series B "
                  "(Growth), which agrees with the band, so the band dispute flag is cleared."))

L.append(cls("splicebio", stage="Series A", stage_src="web_verified", stage_cite=NEWS("splicebio", "pile into SpliceBio"),
             stage_conf="high", entry_date="2022-02-16",
             rounds=R("splicebio", rnd("2022-02-16", "Series A", 57000000, "UCB Ventures, Ysios Capital", True,
                                       NEWS("splicebio", "pile into SpliceBio"), "press")),
             note="Stage pass (s4): Fierce Biotech (2022-02-16) names the EUR 50M ($57M) Series A co-led by UCB Ventures "
                  "and Ysios with NEA participating and Asabys as the only existing investor, so NEA entered at the "
                  "Series A; the firm's 2021 reads as the close year."))

TOKENZ_A = [x["source"] for x in (CLS["tokenz"].get("funding_rounds") or []) if x.get("round") == "Series A"][0]
L.append(cls("tokenz", stage="Seed", stage_src="web_verified", stage_cite=NEWS("tokenz", "From Hardcore Gamer"),
             stage_conf="high", entry_date="2025",
             grad="graduated", grad_src="web_verified", grad_cite=TOKENZ_A, grad_conf="high",
             rounds=R("tokenz", rnd("2025", "Seed", None, "Coral Capital", True,
                                    NEWS("tokenz", "From Hardcore Gamer"), "press")),
             note="Stage pass (s4): AsiaTechDaily (2025-04-22) reports the JPY 200M seed led by Coral Capital with NEA "
                  "participating, the firm's 2025 entry; the company's June 2026 JPY 1B Series A names NEA as an "
                  "existing investor, a later named round, so the seed graduated."))

L.append(cls("nevro", stage="Growth", stage_src="web_verified", stage_cite=NEVRO_424B4, stage_conf="high",
             entry_date="2013",
             rounds=R("nevro",
                      rnd("2011-07", "Series B", 58593714, None, False, NEVRO_424B4, "filing"),
                      rnd("2013-02", "Series C", 47991245, None, True, NEVRO_424B4, "filing")),
             note="Stage pass (s4): the IPO prospectus (certain transactions, principal stockholders) shows NEA 14 and "
                  "NEA Ventures 2013 holding only Series C preferred, sold at $11.11 in February and March 2013; NEA "
                  "was not in the July 2011 Series B, so the entry is the Series C (Growth)."))

L.append(cls("roka-bioscience-inc", stage="Growth", stage_src="web_verified", stage_cite=ROKA_S1, stage_conf="medium",
             entry_date="2009",
             rounds=R("roka-bioscience-inc", rnd("2009", "Series B", None, None, True, ROKA_S1, "filing")),
             note="Stage pass (s4): the S-1's principal-stockholder note shows NEA 13 and NEA Ventures 2009 holding "
                  "Series B preferred, the earliest series any investor holds (Series A appears only as common stock "
                  "and a warrant class), bought at the 2009 spin-out from Gen-Probe. The record calls that round "
                  "Series B, so it reads Growth by label although it was the formation financing; medium for that."))

# ---- undetermined, with what this pass found
L.append(cls("nektar-therapeutics", stage="undetermined", rounds=R("nektar-therapeutics"),
             note="Stage pass (s4): the firm labels its 2011 purchase Public/PIPES into a company listed since the 1990s; "
                  "a PIPE names no venture round, so the rounds list stays empty."))

L.append(cls("bloom-energy", stage="undetermined",
             rounds=R("bloom-energy",
                      rnd("2016-09", "6% convertible notes", 12500000, None, True, BLOOM_424B4, "filing"),
                      rnd("2018-07-25", "IPO (concurrent purchase by existing holders)", None, None, True, BLOOM_424B4,
                          "filing")),
             note="Stage pass (s4): the 2018 IPO prospectus has Scott Sandell on the board since August 2003 and NEA 10 "
                  "and NEA Ventures 2003 as holders, but its related-party section starts in 2015 and names no series; "
                  "Kleiner Perkins was the first investor in 2002, and no source read names the 2003 round NEA joined."))

L.append(cls("yubico", stage="undetermined", rounds=R("yubico"),
             note="Stage pass (s4): Google News ('Yubico' with NEA, and with funding) returned nothing naming a 2017 "
                  "round with NEA."))

L.append(cls("actelis-networks-inc", stage="undetermined", rounds=R("actelis-networks-inc"),
             note="Stage pass (s4): the 2022 IPO prospectus does not name NEA, EDGAR holds only paper Regulation D "
                  "notices from 2002, and Google News carries no early round; NEA's Peter Morris already sat on "
                  "Actelis's board in 2000 (iAsiaWorks prospectus), so NEA was in well before the 2008 first seen."))

L.append(cls("senseonics", stage="undetermined", rounds=R("senseonics"),
             note="Stage pass (s4): the 2014 and 2016 prospectuses name NEA as a principal stockholder but carry no "
                  "series history back to the 1997 entry."))

L.append(cls("habitat-health", stage="undetermined", rounds=R("habitat-health"),
             note="Stage pass (s4): Google News ('Habitat Health' NEA) shows only the September 2024 launch capital "
                  "(more than $50M from Town Hall, NEA and Kaiser), which names no round."))

L.append(cls("launchpad-therapeutics-inc", stage="undetermined", rounds=R("launchpad-therapeutics-inc"),
             note="Stage pass (s4): the firm's posts carry no round word for it; the December 2022 launch financing "
                  "stays unnamed."))

L.append(cls("vimaan-robotics", stage="undetermined",
             rounds=R("vimaan-robotics", rnd("2022-01-26", "Seed and Series A (combined)", 25000000, None, True,
                                             NEWS("vimaan-robotics", "Emerges from Stealth"), "company")),
             note="Stage pass (s4): the company's stealth-exit release (2022-01-26) reports $25M in seed and Series A "
                  "financing from NEA, Wing VC and Neotribe without saying which round NEA entered in 2020."))

L.append(cls("gen-g", stage="undetermined", rounds=R("gen-g"),
             note="Stage pass (s4): the April 2019 $46M headlines (ESPN, CNBC, Hollywood Reporter) name no round; the "
                  "CNBC page refused the fetch."))

L.append(cls("tidal-therapeutics", stage="undetermined", rounds=R("tidal-therapeutics"),
             note="Stage pass (s4): Google News ('Tidal Therapeutics' with NEA, and with launches) returned nothing "
                  "naming the 2019 round."))

L.append(cls("plato", stage="undetermined", rounds=R("plato"),
             note="Stage pass (s4): Google News ('Plato Systems' seed, spatial intelligence funding) found only the "
                  "2024 NVIDIA release; no round is named."))

L.append(cls("affimed", stage="undetermined", rounds=R("affimed"),
             note="Stage pass (s4): nothing to add; the 2017 purchase was in an underwritten public offering."))

L.append(cls("nordsense", stage="undetermined", rounds=R("nordsense"),
             note="Stage pass (s4): Google News ('Nordsense' funding) shows pilots and a 2024 partnership, no round."))

L.append(cls("uhana", stage="undetermined", rounds=R("uhana"),
             note="Stage pass (s4): Google News ('Uhana' with NEA, and with funding) returned only namesakes."))

L.append(cls("frontier-car-group", stage="undetermined", rounds=R("frontier-car-group"),
             note="Stage pass (s4): Google News ('Frontier Car Group' with NEA, and raises) shows the 2019 OLX deal and "
                  "a 2017 Series A of its Pakistan unit CarFirst, nothing naming NEA's 2016 round."))

L.append(cls("moneytap", stage="undetermined",
             rounds=R("moneytap", rnd("2020-01-28", "Series B", 70000000, None, None,
                                      NEWS("moneytap", "USD 70 million Series B"), "press")),
             note="Stage pass (s4): Google News adds the January 2020 Series B ($70M, equity and debt); the June 2017 "
                  "$12.3M round with NEA stays unnamed and NEA's 2016 entry round is not on record."))

L.append(cls("golden-state-medical-supply", stage="undetermined", rounds=R("golden-state-medical-supply"),
             note="Stage pass (s4): Google News ('Golden State Medical Supply' with NEA, and investment) returned "
                  "nothing on the 2015 transaction."))

L.append(cls("miim", stage="undetermined", rounds=R("miim"),
             note="Stage pass (s4): Google News ('MiiM' funding) returned only namesakes."))

L.append(cls("strongbridge-biopharma", stage="undetermined", rounds=R("strongbridge-biopharma"),
             note="Stage pass (s4): the 2015 F-1 says only that it raised over $70M since December 2014 from RA "
                  "Capital, NEA and others while quoted on the Norwegian OTC list; no round word."))

L.append(cls("wallapop", stage="undetermined",
             rounds=R("wallapop",
                      rnd("2013-10", "unnamed (Antai and angels, EUR 1.6M)", None, None, None,
                          NEWS("wallapop", "History of Wallapop"), "press"),
                      rnd("2014", "unnamed (Accel, about EUR 3.5M)", None, "Accel", None,
                          NEWS("wallapop", "History of Wallapop"), "press"),
                      rnd("2015-04", "unnamed (Insight-led)", 40000000, "Insight Venture Partners", False,
                          NEWS("wallapop", "best kept secret"), "press"),
                      rnd("2016", "merger with letgo (about EUR 90M added)", None, None, None,
                          NEWS("wallapop", "History of Wallapop"), "press")),
             note="Stage pass (s4): Novobrief (April 2015) lists the $40M Insight-led round with Caixa, Accel and "
                  "Bonsai and no NEA, and Marketing4eCommerce's history names no NEA round either; the firm writes "
                  "'Letgo (Wallapop)', so its stake may have come through the 2016 letgo combination, which is not "
                  "established."))

L.append(cls("bonsai", stage="undetermined", rounds=R("bonsai"),
             note="Stage pass (s4): the Electronics Weekly piece (read) names no round and no lead for the earlier $6M; "
                  "Google News adds nothing on the 2014 entry."))

L.append(cls("mighty-ai", stage="undetermined", rounds=R("mighty-ai"),
             note="Stage pass (s4): the GeekWire article on the December 2014 $3.25M round refused the fetch (403); "
                  "the headline names no round."))

L.append(cls("topia", stage="undetermined", entry_date="2014-10",
             rounds=R("topia", rnd("2014-10-09", "unnamed (NEA's announced investment)", None, None, True,
                                   POST("the-last-mile-of-enterprise"), "firm")),
             note="Stage pass (s4): NEA's own post of 2014-10-09 announces its newest investment, MOVE Guides, and "
                  "dates the entry, but names no round; Google News ('MOVE Guides' with NEA, raises, funding) found "
                  "no round coverage (the one vator roundup is gone, 404)."))

L.append(cls("willow", stage="undetermined",
             rounds=R("willow",
                      rnd("2019-12-20", "unnamed", 20000000, None, None,
                          NEWS("willow", "Additional $20 Million"), "company"),
                      rnd("2020-09-22", "Series C", 55000000, None, None,
                          NEWS("willow", "Series C to Fund Future"), "company")),
             note="Stage pass (s4): Google News carries the 2019 $20M and 2020 $55M Series C releases, nothing on the "
                  "2014 entry NEA made."))

L.append(cls("cellgate-inc", stage="undetermined", rounds=R("cellgate-inc"),
             note="Stage pass (s4): EDGAR has a CellGate registrant but no prospectus; the firm's posts carry no round."))

L.append(cls("edimer-pharmaceuticals", stage="undetermined", rounds=R("edimer-pharmaceuticals"),
             note="Stage pass (s4): Google News ('Edimer' Series A, 'Edimer Pharmaceuticals') returned no round "
                  "coverage; the 2013 Form D stays unnamed."))

L.append(cls("folloze", stage="undetermined", rounds=R("folloze"),
             note="Stage pass (s4): Google News finds a 2015 Vox roundup (fetch refused) and the 2016 vator item "
                  "(page gone, 404); no source read names the 2013 round."))

L.append(cls("maxiscale-inc", stage="undetermined", rounds=R("maxiscale-inc"),
             note="Stage pass (s4): EDGAR has a MaxiScale registrant but no prospectus; nothing names a round."))

L.append(cls("pixelberry", stage="undetermined", rounds=R("pixelberry"),
             note="Stage pass (s4): no EDGAR registrant, and Wikipedia names no round."))

L.append(cls("reshape-inc", stage="undetermined", rounds=R("reshape-inc"),
             note="Stage pass (s4): EDGAR has a ReShape registrant but no prospectus; nothing names a round."))

L.append(cls("tabula-inc", stage="undetermined", rounds=R("tabula-inc"),
             note="Stage pass (s4): Wikipedia gives only the $215M total raised; no round is named."))

L.append(cls("united-medical-plan", stage="undetermined", rounds=R("united-medical-plan"),
             note="Stage pass (s4): no EDGAR registrant found; nothing names a round."))

L.append(cls("aerospike", stage="undetermined", rounds=R("aerospike"),
             note="Stage pass (s4): Google News ('Aerospike' Series A with NEA, raises) and Wikipedia give only the "
                  "2014 Series C and later rounds, nothing on the 2012 entry."))

L.append(cls("edmodo", stage="undetermined", rounds=R("edmodo"),
             note="Stage pass (s4): Google News ('Edmodo' NEA Series, raises) and Wikipedia name no round with NEA."))

L.append(cls("relievant-medsystems", stage="undetermined",
             rounds=R("relievant-medsystems",
                      rnd("2016-10-11", "unnamed", 36000000, None, None,
                          NEWS("relievant-medsystems", "raises $36m"), "press"),
                      rnd("2023-04-20", "unnamed", 50000000, None, None,
                          NEWS("relievant-medsystems", "Raises $50 Million to Advance"), "press")),
             note="Stage pass (s4): Google News carries the 2016 $36M and 2023 $50M rounds, neither named, and nothing "
                  "on the 2012 entry."))

AGNI_FD = FD("agni-corporation")
L.append(cls("agni-corporation", stage="undetermined", entry_date="2011-03-11",
             rounds=R("agni-corporation", rnd("2011-03-11", "unnamed (Form D)", 14000000, None, True, AGNI_FD,
                                              "filing")),
             note="Stage pass (s4): biofuels developer; the March 2011 Form D ($14M, NEA's Rohini Chakravarthy a "
                  "director) is the only round on record and names no series; Google News found nothing."))

L.append(cls("embrane", stage="undetermined", rounds=R("embrane"),
             note="Stage pass (s4): Google News ('Embrane' Series A, NEA) shows only the 2015 Cisco acquisition."))

L.append(cls("ketra", stage="undetermined", rounds=R("ketra"),
             note="Stage pass (s4): Google News ('Ketra' Series A, lighting funding) returned only namesakes and "
                  "product news."))

L.append(cls("tarveda-therapeutics", stage="undetermined", rounds=R("tarveda-therapeutics"),
             note="Stage pass (s4): Google News ('Blend Therapeutics' Series A, NEA) shows only a 2014 hire; the 2011 "
                  "round stays unnamed."))

L.append(cls("enverv", stage="undetermined", rounds=R("enverv"),
             note="Stage pass (s4): Google News ('EnVerv' funding) and EDGAR company search returned nothing."))

L.append(cls("nova-medical-centers", stage="undetermined", rounds=R("nova-medical-centers"),
             note="Stage pass (s4): Google News shows the 2012 rebrand and the 2015 Apollo deal, no round with NEA."))

L.append(cls("apprenda-inc", stage="undetermined", rounds=R("apprenda-inc"),
             note="Stage pass (s4): Google News ('Apprenda' Series A, NEA) shows only the 2013 Series C and the 2018 "
                  "shutdown; the 2009 round stays unnamed."))

L.append(cls("huddler", stage="undetermined", rounds=R("huddler"),
             note="Stage pass (s4): Google News ('Huddler' funding) and EDGAR company search returned nothing."))

L.append(cls("actional-corporation", stage="undetermined", rounds=R("actional-corporation"),
             note="Stage pass (s4): EDGAR has an Actional registrant but no prospectus; nothing names a round."))

L.append(cls("agility-design-solutions", stage="undetermined", rounds=R("agility-design-solutions"),
             note="Stage pass (s4): EDGAR has an Agility Design Solutions registrant but no prospectus; nothing names a "
                  "round."))

jl.write("s4a", L)
