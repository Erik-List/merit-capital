#!/usr/bin/env python3
"""The programme years' invested cohorts, as the firm announced them, into
sources/site/views-cohorts.json (a site_api `file_list` source).

Hand-curated at kickoff (PRO-83, 2026-09-30) by reading every Views post that
announces investments, 2007-2017 (decisions.md D2, D3): the Seedcamp Week
winners pages, the "join the Seedcamp family" posts after each Seedcamp Week
and Mini Seedcamp, the Fund III seed list of 2015-09-21. Only names the firm
names as INVESTMENTS are here; attendee, finalist and "Meet the teams" posts
are not (2009's "talented tourists" invited on the US trip, the 2009 Tel Aviv
Mini winners, the 2013-11-20 and 2015-05-13 attendee lists). Each row carries
the post as its url, the post date, the location the post gives, and the
kind of entry the firm names:
  programme  the standard deal of its era (EUR 50K 2007-2013; EUR 75K for 7%
             2014-2017; sources/site/programme-terms.json)
  seed       a seed-round investment the firm announces as such ("investments
             made through our Seed Fund", "Seedcamp participated in the $1.8m
             seed round")
Names follow the base row where one exists (the live list's rendering); the
post's own spelling is kept in `as_posted` where it differs.

Usage: python3 views-cohorts.py
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
INV = HERE.parent
POSTS = {p["title"]: p for p in json.loads((INV / "sources" / "site" / "views-posts.json").read_text())["rows"]}
OUT = INV / "sources" / "site" / "views-cohorts.json"

# (post title, kind, [(name, location, as_posted or None)])
C = [
 ("Seedcamp '07 winners announced", "programme", [
   ("MyBuilder", "UK", "Buildersite"), ("RentMineOnline", "Netherlands", None), ("Tablefinder", "Sweden", "TableFinder"),
   ("Zemanta", "Slovenia", None), ("Kublax", "UK", None), ("Hypernumbers", "Scotland", "Project Playfair")]),
 ("Our Seedcamp Week 2008 winners", "programme", [
   ("Basekit", "Chepstow, UK", None), ("Kyko", "Oxford, UK", None), ("Mobclix", "San Francisco, US", None),
   ("Soup", "Vienna, Austria", None), ("Stupeflix", "Paris, France", None), ("Toksta", "Berlin, Germany", None),
   ("uberVU", "Bucharest, Romania", None)]),
 ("And the winners are….Seedcamp congratulates the 2009 winning teams", "programme", [
   ("Server Density", "Birmingham, UK", "Boxed Ice"), ("Brainient", "Bucharest, Romania", None),
   ("Codility", "Warsaw, Poland", None), ("Erply", "Tallinn, Estonia", None),
   ("Patients Know Best", "Cambridge, UK", None), ("Talasim", "Amman, Jordan", "Talasim.com"),
   ("Kwaga", "Paris, France", None), ("Platogo", "Vienna, Austria", "Platago")]),
 ("Seedcamp 2010 – One for the history books", "programme", [
   ("Albia", "Sarajevo, Bosnia and Herzegovina", None), ("EDITD", "London, UK", None),
   ("Finance A Car", "London, UK", None), ("Garmz", "Vienna, Austria", None), ("GIS Cloud", "Zagreb, Croatia", None),
   ("Ineze", "Tel Aviv, Israel", None), ("Nuji", "London, UK", None), ("Profitero", "Dublin, Ireland", None),
   ("Sparkeo", "Tel Aviv, Israel", None), ("Trebax", "London, UK", None), ("Uberblic Labs", "Berlin, Germany", None),
   ("Wordy", "Copenhagen, Denmark", None)]),
 ("Seedcamp London 2011 – the winners", "programme", [
   ("GrabCAD", "Tallinn, Estonia", None), ("Psykosoft", "Tours, France", None), ("Vox.io", "Ljubljana, Slovenia", None)]),
 ("Mini Seedcamp Berlin 2011 – adding two new members to the family", "programme", [
   ("Mopapp", "Bologna, Italy", None), ("The Efficient Cloud", "Vienna, Austria", None)]),
 ("Seedcamp grows and grows; we have two more great founding teams joining our family.", "programme", [
   ("Holvi", "Helsinki, Finland", None), ("Crashpadder", "London, UK", None)]),
 ("Seedcamp – Big in the Big Apple with 4 new investments", "programme", [
   ("Bilbus", "London, UK", None), ("Campalyst", "Riga, Latvia", None), ("Compilr", "Halifax, Canada", None),
   ("Zin.gl", "Russia", None)]),
 ("Mini Seedcamp Ljubljana – Two new teams join Seedcamp", "programme", [
   ("Oust.me", "Ljubljana, Slovenia", None), ("Sportlyzer", "Tallinn, Estonia", None)]),
 ("Straight out of Mini Seedcamp London: 3 new Seedcamp Teams", "programme", [
   ("Farmeron", "Osijek, Croatia", None), ("Fractal", "London, UK", None), ("Wise", "London, UK", "TransferWise")]),
 ("Seedcamp Week 2011 – New teams and winners, plus a bonus!", "programme", [
   ("Appextras", "Canada / Brazil", None), ("Blossom", "Austria", None), ("Crowd", "France", None),
   ("Rentlord", "London, UK", None)]),
 ("Post Seedcamp Prague – welcoming two new teams to the Seedcamp family!", "programme", [
   ("Milk.ly", "Netherlands", None), ("Qminder", "Tallinn, Estonia", None)]),
 ("Seedcamp Barcelona – Welcome another brother!", "programme", [("SocialBro", "Spain", "Socialbro")]),
 ("A new team from Seedcamp Paris", "programme", [("Archivme", "Paris, France", None)]),
 ("Four fantastic teams joining us after Seedcamp London", "programme", [
   ("24Symbols", "Madrid, Spain", "24symbols"), ("Bluefields", "London, UK", None), ("Checkthis", "Brussels, Belgium", None),
   ("Pult", "Tallinn, Estonia", None)]),
 ("Seedcamp Paris – Meet the Teams", "programme", [("Sush.io", "Paris, France", None)]),
 ("From Tel Aviv to Tallinn", "programme", [
   ("Antavo", "Budapest, Hungary", None), ("Bukit", "UK", None), ("MightyFingers", "Riga, Latvia", None),
   ("Sayduck", "Helsinki, Finland", None)]),
 ("Berlin ’12 – Meet the 2 winners", "programme", [
   ("Repairy", "Riga, Latvia", None), ("Trait Perception", "Madrid, Spain", None)]),
 ("Four New Companies Join the Seedcamp Family", "programme", [
   ("BRANDiD", "London, UK", None), ("Poq", "London, UK", "poq Studio"), ("Rawstream", "Malta", None),
   ("TRData", "Kiev, Ukraine", None)]),
 ("Over 75 Seedcamp Family Members!", "programme", [("Futurelytics", "Brno, Czech Republic", None)]),
 ("4 new teams joining the Seedcamp Family", "programme", [
   ("SimpleTax", "Portugal", "Simpletax"), ("CrowdProcess", "Portugal", None), ("Hole19", "Portugal", None),
   ("Qamine", "Portugal", None), ("Home on Demand", "London, UK", None)]),
 ("Codeship joins the Seedcamp Family", "programme", [("Codeship", "Berlin, Germany", None)]),
 ("SeedPeek", "programme", [("Subscrib", "London, UK", None), ("Planvine", "London, UK", None)]),
 ("Seedcamp Week Berlin", "programme", [
   ("Countly", "Istanbul, Turkey", None), ("FishBrain", "Stockholm, Sweden", None), ("SmartWard", "London, UK", None),
   ("TruckTrack", "Belgrade, Serbia", None)]),
 ("New Teams Joining our Seedcamp Family: 100+ Strong", "programme", [
   ("Ctrlio", "London, UK", None), ("BorrowMyDoggy", "London, UK", None), ("GoPixel", "Newcastle upon Tyne, UK", None),
   ("Hype", "London, UK", "Hype!"), ("Spreddit", "London, UK", None), ("Legal Tender", "London, UK", None),
   ("Revision App", "London, UK", None), ("Saberr", "London, UK", None), ("ShareLaTeX", "London, UK", None),
   ("Stamplay", "London, UK", None), ("Teddy The Guardian", "Zagreb, Croatia", None),
   ("Winnow", "London, UK", "Winnow Solutions"), ("Unifyo", "Cambridge, UK", None)]),
 ("Seedcamp Week Berlin: Seven Teams Joining the Seedcamp Family", "programme", [
   ("BuzzTale", "Riga, Latvia", "Buzztale"), ("Cashtag", "Lisbon, Portugal", None), ("myTips", "Kiev, Ukraine", None),
   ("Popcorn Metrics", "Lisbon, Portugal", None), ("Satago", "London, UK", None), ("SquadMail", "Berlin, Germany", None),
   ("Zercatto", "Porto, Portugal", None)]),
 ("Guest Post: Questions to Build a Brand – by Kei Karlson", "programme", [("GoWorkaBit", "Tallinn, Estonia", None)]),
 ("Meet Our Latest Family Members", "programme", [
   ("BridgeU", "London, UK", None), ("DoxOut", "Skopje, Macedonia", None), ("FabAllThings", "Dublin, Ireland", None),
   ("Farmhopping", "Sofia, Bulgaria", "farmhopping"), ("GamingLive", "Warsaw, Poland", "Gaming Live"),
   ("Oradian", "Zagreb, Croatia", None), ("Reedsy", "Nottingham, UK", None)]),
 ("Announcing 11 New Seedcamp Investments", "programme", [
   ("Carbon Voyage", "London, UK", None), ("Homeshift", "London, UK", None), ("Make Works", "Glasgow, UK", None),
   ("Medefer", "London, UK", None), ("Newsfixed", "London, UK", None), ("Shoprocket", "London, UK", None),
   ("Wriggle", "Bristol, UK", None)]),
 ("Announcing 11 New Seedcamp Investments", "seed", [
   ("eMoov", "Brentwood, UK", None), ("Mailcloud", "London, UK", None), ("Property Partner", "London, UK", None),
   ("Teleport", "Palo Alto, US / Tallinn, Estonia", None)]),
 ("Announcing 7 New Investments Following Seedcamp Week Berlin", "programme", [
   ("BranchTrack", "Riga, Latvia", None), ("Cronofy", "Nottingham, UK", None), ("Lateral", "Berlin, Germany", None),
   ("Now Native", "London, UK", None), ("Fluttr", None, None), ("Divido", "London, UK", None)]),
 ("Seedcamp Family Grows to Over 150 as 11 New Startups Join", "programme", [
   ("Car Quids", "London, UK", None), ("Clowdy", "Manchester, UK", None), ("Data Smoothie", "London, UK", None),
   ("Hoko", "Lisbon, Portugal", "HOKO"), ("Jobdoh", "Hong Kong", "JOBDOH"), ("MagicTab", "London, UK", None),
   ("Opinion", "Stockholm, Sweden", None), ("Queueco", "London, UK", None), ("Revolut", "London, UK", None),
   ("Gamewheel", "Berlin, Germany", None)]),
 ("8 Startups Join Seedcamp After a Successful Seedcamp Week Berlin", "programme", [
   ("ByeBuy", "London, UK", None), ("Intelliment Security", "Seville, Spain", None), ("Kasko", "London, UK", "Kasko Tech"),
   ("Oinky", "London, UK", None), ("Reinfer", "London, UK", "reinfer"), ("Rialto", "London, UK", None),
   ("Wanna", "Tel Aviv, Israel", None)]),
 ("Announcing the startups joining our family at Seedcamp Week", "programme", [
   ("API Changelog", "London, UK", None), ("Captini", "London, UK", "CAPTINI"), ("DeviceHub", "Krakow, Poland", None),
   ("Much Better Adventures", "London, UK", None), ("MyRecovery", "London, UK", None), ("Talkpush", "Hong Kong", "TalkPush"),
   ("Traderion", "Bucharest, Romania", None)]),
 ("Your First Round Fund", "seed", [
   ("Curve", "London, UK", None), ("Cymmetria", "US / Estonia", None), ("Edgefolio", "Norway", None),
   ("Findify", "Stockholm, Sweden", None), ("Fractal Labs", "London, UK", None), ("GetAgent", "London, UK", "Get Agent"),
   ("Hubble", "London, UK", None), ("incrediblue", "Greece", "Incrediblue"), ("Kukimi", "Germany", None),
   ("LandInsight", "London, UK", "Land Insight"), ("MarcoPolo Learning", "New York, US", None), ("Monese", "London, UK", None),
   ("Podo Labs", "San Francisco, US", None), ("Pointy", "Dublin, Ireland", None), ("Priori Data", "Berlin, Germany", None),
   ("Pronto", "London, UK", None), ("Splittable", "London, UK", None), ("Spoke", "London, UK", None),
   ("Trussle", "London, UK", None), ("UiPath", "Bucharest, Romania", "Uipath")]),
 ("Meet the new startups to join the Seedcamp family!", "programme", [
   ("Alterest", "UK", "Alterest Investment"), ("Authentiq", "Netherlands", None), ("Beeline", "UK", None),
   ("Buildcon", "Serbia", None), ("Cardlife", "UK", None), ("Finance Fox", "Switzerland", None), ("Greenhouse", "Estonia", None),
   ("Nanoget", "UK", None), ("Open Sensors", "UK", None), ("Repositive", "UK", None), ("Rock Pamper Scissors", "UK", None),
   ("SwiftShift", "Israel", None), ("ThingThing", "Spain", None), ("Unlease", "UK", None), ("Unmanned Systems", "Belgium", None)]),
 ("The latest teams to join Seedcamp!", "programme", [
   ("Charlie HR", "UK", "CharlieHR"), ("Juro", "UK", None), ("Microscaling Systems", "UK / Spain", None),
   ("Oratio", "Austria", "oratio"), ("Thriva", "UK", "thriva")]),
 ("Here are the latest additions to the Seedcamp portfolio", "programme", [
   ("ActionBar", "Tel Aviv, Israel", None), ("Anvajo", "Dresden, Germany", None), ("Avalio", "London, UK", None),
   ("KareInn", "London, UK", None), ("Real Funds", "London, UK", None), ("Vinterior", "London, UK", None),
   ("YodelTalk", "Vienna, Austria", None)]),
 ("Introducing the newest teams in the Seedcamp portfolio", "programme", [
   ("Viz.ai", "US", None), ("Libryo", "South Africa", None), ("Clause", "US", None), ("Sunlight", "UK", None),
   ("AI Build", "UK", "Ai Build"), ("NextChef", "UK", None)]),
 ("Announcing new teams in the Seedcamp family – January 2017", "programme", [
   ("Telleroo", "UK", None), ("Vchain", "UK", None), ("Wevat", "UK", None), ("Stowga", "UK", None)]),
]


def main():
    rows, missing = [], []
    for title, kind, items in C:
        p = POSTS.get(title)
        if not p:
            missing.append(title)
            continue
        for name, loc, as_posted in items:
            r = {"name": name, "url": p["link"], "invest_year": p["date"][:4], "post_date": p["date"][:10],
                 "cohort": title, "entry_kind": kind}
            if loc:
                r["location"] = loc
            if as_posted:
                r["as_posted"] = as_posted
            rows.append(r)
    OUT.write_text(json.dumps({
        "_readme": __doc__.strip(), "read": "2026-09-30", "rows": rows}, indent=1, ensure_ascii=False) + "\n")
    print(len(rows), "rows;", len({r['name'] for r in rows}), "companies; missing posts:", missing)


if __name__ == "__main__":
    main()
