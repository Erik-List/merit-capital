"""The private equity practice (decisions.md D3, R1). Sources: scratch/pe-research.json
(every URL re-loaded by the research agent, quote checked on the page)."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import verdict, cls, rnd, write, LISTING  # noqa: E402

R = json.loads((Path(__file__).resolve().parent / "pe-research.json").read_text())["companies"]


def src(name, i=0):
    return R[name]["sources"][i]["url"]


L = []


def control(slug, name, basis, conf="high"):
    L.append(verdict(slug, "not_member", basis + " Control position (decisions.md D3, R1; COLLECTION.md s1 T3).",
                     ec="web", conf=conf, cite=src(name), exclusion="control_position"))


control("kfzteile24", "kfzteile24",
        "EQT Mid Market bought the majority from the founders (announced 2015-10-05, completed Dec 2015); Project A joined "
        "EQT's position with a seven-figure co-investment in March 2016 ('With its seven-figure investment Project A joins "
        "the EQT Mid Market Fund', eu-startups), and in April 2023 was part of the management buy-out consortium that "
        "bought kfzteile24 from EQT.")
control("onlineprinters", "Onlineprinters",
        "Bregal Unternehmerkapital completed a majority buyout in early October 2016; Project A put a seven-figure sum into "
        "a minority stake beside Bregal in November 2016, its 'second private equity co-investment' (VC Magazin).")
control("luqom-group", "Lampenwelt / LUQOM Group",
        "3i bought the majority of Lampenwelt in March 2017; Project A agreed with 3i to invest in October 2017, 'the third "
        "private equity co-investment' (Private Equity News). 3i still holds the majority of LUQOM Group.")
control("trendtours", "trendtours",
        "Bregal Unternehmerkapital bought trendtours from its founder as a succession arrangement in October 2018; Project "
        "A Services GmbH & Co. KG joined weeks later as an operational co-investor (VC Magazin, 2018-11-21); the firm's own "
        "archived record reads 'Succession Arrangement', 'PE Co-Investment'.")
control("ydeon-group", "GartenHaus / YDEON Group",
        "3i agreed in September 2020 to buy a majority of A-Z Gartenhaus (renamed YDEON); Project A's October 2020 "
        "investment 'was made as a co-investment with the private equity firm 3i Group' (Deutsche Startups dealmonitor).")
control("pdsg", "PDSG",
        "Bregal Unternehmerkapital bought the majority of Perfect Drive Sports Group (All4Golf, Clubhouse Golf) in March "
        "2021; Project A's July 2021 investment was a PE co-investment beside Bregal (YPOG).")
control("perfect-drive-sports-group", "Perfect Drive Sports Group",
        "The same company as the CMS row PDSG, listed 2021-2024 under its full name: Bregal holds the majority and Project "
        "A's July 2021 stake was a PE co-investment beside it (YPOG).")
control("windstar-medical", "WindStar Medical",
        "Oakley Capital bought WindStar Medical from ProSiebenSat.1's NuCom in October 2020, and Project A invested "
        "together with Oakley in December 2020 (FYB); the Merz Group took the majority of the combined holding in 2024.")
control("inwerk", "Inwerk",
        "Triton completed a majority acquisition of Inwerk on 2020-12-23; Project A invested in the Triton-controlled "
        "company in May 2021, recorded by the firm as a 'PE Co-Investment' (the archived Contentful record).", conf="medium")
control("amann-girrbach", "Amann Girrbach",
        "Capvis has held the majority since April 2018; Project A's May 2020 investment in the Capvis portfolio company "
        "(Capvis's own release) is recorded by the firm as a 'PE Co-Investment', 'Later Stage Acceleration' (the archived "
        "Contentful record): a stake beside the controlling sponsor.", conf="medium")
control("konges-sl-jd", "Konges Sløjd",
        "3i bought the majority from the founder in June-August 2022 (FIH Partners); Project A's 2022 position, from Fund "
        "IV, is recorded by the firm as private_equity (live CMS) and 'PE Co-Investment' (archived record), a stake beside "
        "3i. No public source names Project A in the deal.", conf="low")
control("nwt", "NWT Group",
        "KLAR Partners' funds invested in NWT Group in 2022 with the founders re-investing after selling ('rückbeteiligt', "
        "M&A Review); Project A's November 2022 co-investment 'joins KLAR Partners as a growth partner' (YPOG). KLAR's stake "
        "is not stated; the firm records the position as private_equity.", conf="medium")
control("primutec", "Primutec",
        "Held by the firm's 'Buyout Fund I' (live CMS), a buyout-strategy vehicle (strategy desks, T1); Trill Impact took "
        "the majority in May 2025. Project A's PE practice describes itself as a partner for 'Management teams looking for "
        "an active majority partner' (project-a.pe).", conf="medium")

L.append(verdict("hometogo", "not_member",
                 "HomeToGo SE has been listed in Frankfurt since the September 2021 SPAC merger; Project A's position dates to "
                 "2025 (live CMS, private_equity) and Florian Heinemann joined the supervisory board in May 2025. A purchase "
                 "of shares in a listed company is not a venture entry (T3, public-market purchase; decisions.md D3).",
                 ec="web", conf="high", cite=src("HomeToGo", 1)))
L.append(verdict("helloprint", "not_member",
                 "HelloPrint's 2017 minority investment was made 'via their printing holding Onlineprinters' (Bregal "
                 "Unternehmerkapital): a position of the Bregal-controlled Onlineprinters group, not of a Project A fund (T2, "
                 "fund money), and inside the control position excluded as onlineprinters.",
                 ec="web", conf="high", cite=src("HelloPrint", 0)))

# Minority growth positions of the PE practice: members, Growth.
L.append(verdict("amboss", "member",
                 "Listed on the firm's live CMS (Fund IV, 2025, private_equity) and named among the investors in Amboss's EUR "
                 "240M round of March 2025 (YPOG, FYB): a minority stake in a company financing with no controlling sponsor "
                 "(decisions.md D3, R1).", ec="site_listing", conf="high", cite=LISTING))
L.append(cls("amboss", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="medium",
             stage_cite=src("Amboss", 0), entry_date="2025-03", country="DE", country_cite=LISTING, city="Berlin",
             focus="Healthcare & Bio",
             note="Medical knowledge and clinical decision platform, Berlin (founded 2012). Project A came in at the EUR 240M "
                  "round of March 2025 (KIRKBI, M&G, Lightrock new; part of the money bought out Target Global and Holtzbrinck "
                  "Digital), a late-stage entry through the PE practice; no company-stated valuation (Bloomberg reported "
                  "over EUR 800M, below $1B either way).",
             rounds=[rnd("2025-03", "Growth round", 260_000_000, "KIRKBI, M&G, Lightrock", True, src("Amboss", 1))]))
L.append(verdict("yoummday", "member",
                 "Listed on the firm's live CMS (Fund IV, 2022, private_equity); Project A co-led Yoummday's EUR 30M growth "
                 "round of February 2022 with Armira Growth, a minority investor (tech.eu): a company financing with no "
                 "controlling sponsor (decisions.md D3, R1).", ec="site_listing", conf="high", cite=LISTING))
L.append(cls("yoummday", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="medium",
             stage_cite=src("Yoummday", 0), entry_date="2022-02", country="DE", country_cite=LISTING, city="Munich",
             focus="Consumer & Marketplaces",
             note="Platform for remote customer-service agents, Munich (founded 2015). Project A entered at the EUR 30M "
                  "growth round of February 2022, co-led with Armira Growth (tech.eu); its counsel calls it a private "
                  "equity co-investment, but no sponsor holds control.",
             rounds=[rnd("2022-02", "Growth round", 34_000_000, "Armira Growth, Project A", True, src("Yoummday", 0))]))

if __name__ == "__main__":
    write("pe-class", L)
