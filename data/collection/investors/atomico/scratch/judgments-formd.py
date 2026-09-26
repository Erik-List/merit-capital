"""PRO-79 grind: the 28 Form D-only candidates (batches 4-5, tier C), ruled
cluster-first by the matched person, plus Skype (decisions.md ruling 12)."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
verdict = jl.verdict
FD = "formd_adjudicated"

WARDI = ("https://investors.sentinelone.com/governance/board-of-directors/person-details/"
         "default.aspx?ItemId=e12487c0-dc6f-42e7-8233-2a69c7afa6ec")
WARDI_BASIS = ("ex-partner filing: Teddie Wardi was a Partner at Atomico (UK) Partners LLP from "
               "March 2016 to October 2017 and has been at Insight Partners since 2017 "
               "(SentinelOne board biography); this filing ({}) postdates the move and is an "
               "Insight deal, so it carries no Atomico position (decisions.md D4: a seat is "
               "dated against the person's firm at filing time)")

L = []
for slug, when in [("6sense-insights-inc", "2021-2022"), ("contentstack-llc", "2019-2022"),
                   ("intenseye-inc", "2021-2023"),
                   ("panorama-artificial-intelligence-corp", "2026"),
                   ("project44-inc", "2021-2022"), ("semperis-ltd", "2020-2022"),
                   ("sentinel-labs-inc", "2020-2021"), ("sisense-ltd", "2019"),
                   ("uniform-systems-inc", "2022")]:
    L.append(verdict(slug, "not_member", WARDI_BASIS.format(when), FD, "high", WARDI))

GOODMAN = ("namesake: the related person 'Jason Goodman' on this filing is the Brooklyn "
           "entrepreneur (3rd Ward / Artists Wanted / Bathhouse founder) or the Goodman Networks "
           "family, not the Atomico staff member seen on the firm's 2016 team page; no site "
           "listing, no Atomico fund filing - a name-match never suffices")
for slug in ["3rd-ward-holding-llc", "artists-wanted-inc", "bathhouse-holdings-inc",
             "gnet-escrow-corp", "goodman-networks-inc"]:
    L.append(verdict(slug, "not_member", GOODMAN, FD, "high"))

L.append(verdict("duo-oncology-inc", "not_member",
                 "namesake: the related person Stephen Thorne on these oncology filings "
                 "(2021-2026) is the oncolytic-virus scientist, not Atomico's former principal; "
                 "no site listing, no fund filing - a name-match never suffices", FD, "high"))
L.append(verdict("western-oncolytics-ltd", "not_member",
                 "namesake: Western Oncolytics (2015) is an oncolytic-virus biotech whose related "
                 "person Stephen Thorne is the scientist founder, not Atomico's principal; no site "
                 "listing, no fund filing", FD, "high"))
L.append(verdict("1910-genetics-inc", "not_member",
                 "namesake: the filing's director is Marc Foster of Brookline MA (1910 Genetics' "
                 "board, Form D 0001855990-21-000001), not the Marcus Foster of Atomico's 2014-2016 "
                 "team page; no site listing, no fund filing", FD, "high"))
L.append(verdict("klarismo-inc", "not_member",
                 "founder filing: Marcus Foster is Klarismo's own executive officer and director at "
                 "the company's London address (Form D 0001648677-15-000001), not an Atomico "
                 "director; Klarismo appears on no era of the firm's site and no Atomico vehicle "
                 "filed - a name-match never suffices", FD, "high"))
L.append(verdict("aerology-products-llc", "not_member",
                 "namesake: a 2012 filing, before Chris Barnes joined Atomico (LLP member from "
                 "2015-02-23, register); no site listing, no fund filing", FD, "high"))
L.append(verdict("virginia-carbon-products-llc", "not_member",
                 "namesake: a Virginia carbon-products LLC whose related person Christopher Barnes "
                 "is not Atomico's partner; no site listing, no fund filing - a name-match never "
                 "suffices", FD, "high"))
L.append(verdict("bound-rates-inc", "not_member",
                 "ex-partner filing: Mattias Ljungman left Atomico (LLP member until 2019-12-31, "
                 "register) and co-founded Moonfire Ventures; this 2021-2022 filing is a "
                 "post-Atomico seat (decisions.md D4)", FD, "high"))
L.append(verdict("cactus-app-inc", "not_member",
                 "namesake: Miguel Perez is Cactus App's own Denver executive officer and director "
                 "(Form D 0001862773-21-000001); Atomico's Miguel Rodrigo Perez joined in 2024; no "
                 "site listing, no fund filing", FD, "high"))
L.append(verdict("just-eat-takeaway-com-n-v", "not_member",
                 "personal board seat at a listed company: Jambu Palaniappan, then Atomico's "
                 "executive-in-residence, was appointed a non-executive director of Just Eat in "
                 "June 2019 (RNS); the 2020 Form D is Just Eat Takeaway.com's own issuance around "
                 "the Grubhub deal, not an Atomico position (T3/T4)", FD, "high",
                 "https://www.lse.co.uk/rns/just-eat-non-executive-director-appointment-520jr4s00zzzrh2.html"))
L.append(verdict("openst-ltd", "not_member",
                 "ex-staff filing: Chris Dark was on Atomico's team in 2011-2012; OpenST (Hong Kong, "
                 "2017) lists him beside Jason Goldberg and Allen Morgan as a director five years "
                 "later; no site listing, no fund filing", FD, "high"))
L.append(verdict("shoreline-software-inc", "not_member",
                 "ex-staff filing: Evgenia Plotnikova left Atomico and joined Dawn Capital in 2018 "
                 "(General Partner 2021, Tech.eu); the 2022 filing is a Dawn seat", FD, "high",
                 "https://tech.eu/2021/09/17/dawn-capital-welcomes-evgenia-plotnikova-to-the-rank-of-general-partner/"))
L.append(verdict("sinobiopharma-inc", "not_member",
                 "namesake: a 2009 $35K filing by a small Chinese biopharma whose related person "
                 "Yuanwei Chen is not Atomico's 2012 team member Yuan Chen; no site listing, no fund "
                 "filing", FD, "high"))
L.append(verdict("starship-technologies-holdings-inc", "not_member",
                 "founder position: Janus Friis co-founded Starship Technologies (with Ahti Heinla, "
                 "2014) and sits on its filings as a founder; his Atomico LLP membership ended "
                 "2009-09-08 (register) and no Atomico vehicle filed; personal positions are out "
                 "(T4, decisions.md D2)", FD, "high"))
L.append(verdict("digital-therapeutics-inc", "member",
                 "Pelago's legal entity: the 2024 Form D names the Quit Genius founders Sherwani, "
                 "Siddiqui and Ahmed as executive officers and Atomico partner Ben Blume as director "
                 "- the Series C Atomico led; merged into pelago at the rebuild "
                 "(identity-merges.json)", FD, "high",
                 "https://www.sec.gov/Archives/edgar/data/1805173/000180517324000001/0001805173-24-000001-index.htm"))
L.append(verdict("skype", "not_member",
                 "T3 control, re-derived (decisions.md ruling 12): the firm's CMS dates Skype to 2009, "
                 "and the only 2009 transaction was the Silver Lake-led consortium buying 65% of Skype "
                 "from eBay with the founders' Joltid as a party - a control acquisition, OUT whatever "
                 "vehicle took part; the 2010 S-1 shows no Atomico vehicle among the holders and Skype "
                 "committing $10M into Atomico Ventures II; T4 (the founders' personal stake) is the "
                 "second ground", "site_listing", "high", "https://atomico.com/partners/skype"))

if __name__ == "__main__":
    jl.write("formd-c", L)
