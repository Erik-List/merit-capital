"""PRO-162 membership pass 1: rows that came only through the roster Form D sweep, judged cluster-first
by person (COLLECTION.md s3). A name match never suffices alone (s1): the seat is dated against the
person's firm at filing time (T4), and a name shared by another businessperson is a namesake.
Windows: sources/wayback/partner-roster.json (archived people pages, bios, fund Form Ds)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
verdict = jl.verdict
L = []


def out(slug, why, conf="high"):
    L.append(verdict(slug, "not_member", why, ec="formd_adjudicated", conf=conf))


def dup(slug, canonical, why):
    L.append(verdict(slug, "member",
        f"Same company as the listed member '{canonical}': {why} Recorded as a member so the row is not left unjudged; "
        f"identity-merges.json folds it into '{canonical}' at the scheduled rebuild.", ec="site_listing", conf="high"))


# Aaref Hilaly joined BCV from Sequoia; his 2013-2016 seats are Sequoia's.
for s in ("guardant-health-inc", "keen-labs-inc", "mobile-iron-inc", "thousandeyes-inc"):
    out(s, "Aaref Hilaly's Form D seat dates from his years at Sequoia Capital (2013-2016), before he joined BCV; the money behind the "
           "seat was Sequoia's (COLLECTION.md s1 T4, seats dated against the person's firm at filing time). No BCV listing or fund filing.")
out("fireeye-inc", "Enrique Salem sat on FireEye's board personally from 2013, the year of its IPO, before joining BCV in 2014; no BCV fund "
                   "held the position (T4, the personal-seat class).")
out("valente-sherman-inc", "Enrique Salem's 2021 filing seat on a small private Marin County company with no BCV listing, post or fund "
                           "filing: a personal seat (T4).", conf="medium")
for s in ("direct-vet-marketing-inc", "payspan-holding-corp", "spinal-kinetics-inc"):
    out(s, "Yumin Choi's Form D seat (2013-2016) predates his joining BCV in January 2017; the seat belongs to his previous firm (T4).")
for s in ("cardurion-pharmaceuticals-inc", "iambic-therapeutics-inc", "orsobio-inc"):
    out(s, "Evan Rachlin was at BCV in 2012-2013; these 2023-2024 biotech seats date from a later firm (T4; biotech is outside BCV's book).")
out("building-engines-inc", "Deepak Sindwani left BCV by 2013 (last on its people pages); the 2016 filing seat is from after his tenure (T4).")
out("sidecar-technologies-inc", "Justin Caldbeck left BCV in 2010 for Lightspeed; the 2012 Sidecar seat is Lightspeed's (T4).")
for s in ("activecampaign-holdings-llc", "geofeedia-inc"):
    out(s, "Todd MacLean left BCV by 2015 to co-found Silversmith Capital Partners, which made this 2016 Chicago investment (T4).")
for s in ("mavenlink-inc", "tastemade-inc"):
    out(s, "Mark Midle was at BCV until 2013; the 2015-2016 filing seat is from a later firm (T4).")
for s in ("perfect-health-inc", "springtide-child-development-inc"):
    out(s, "Steve Anastos was at BCV until 2017; the 2020 filing seat is from after his tenure (T4).")
out("cloud-security-corp", "Amanda Huang joined BCV in 2024; the 2017 filing names a namesake or her earlier career, not a BCV position (T4).")
out("credit-precision-inc", "Jeff Schwartz left BCV by 2015; the 2017 seat is from after his tenure (T4).")
for s in ("rapid-micro-biosystems-inc", "springworks-therapeutics-llc"):
    out(s, "Jeffrey Schwartz co-founded Bain Capital Life Sciences after BCV; these 2017-2018 life-sciences seats are that strategy's, "
           "under its own adviser (decisions.md D1, external; T4).")
for s in ("bluearchive-inc", "carbonite-inc", "cyracom-international-inc", "health-integrated-inc", "netblazr-inc", "sagecloud-inc",
          "storiant-inc", "wasabi-technologies-inc"):
    out(s, "The David Friend on this filing is the Boston serial entrepreneur (Carbonite, Wasabi, Storiant), a namesake of BCV's "
           "former associate David Friend; no BCV listing or fund filing (T4 namesake).")
for s in ("adt-f-f-llc", "adt-investment-llc", "adt-management-llc", "b-m-big-dough-llc", "boston-interiors-home-furnishings-llc",
          "micorp-holdings-llc"):
    out(s, "Ryan Kim joined BCV in 2025; this 2011-2018 filing names a namesake (a common name; small local businesses), not a BCV position.")
for s in ("b-door-holdings-inc", "ensysce-biosciences-inc", "hightimes-holding-corp", "reddy-solutions-inc", "visionary-vr-inc"):
    out(s, "Adam Levin was at BCV only in 2018-2019; this seat falls outside that window or is the namesake who runs High Times "
           "(Oreva Capital). No BCV listing or fund filing (T4).")
for s in ("coolgreens-holdings-l-l-c", "coolgreens-ii-llc", "ctx-virtual-technologies-inc", "epicore-biosystems-inc",
          "local-co-llc", "medipines-corp"):
    out(s, "A 'Stephen/Steve Lee' seat outside Steven Lee's 2019-2020 BCV tenure, or on a small local company: a common-name namesake with no "
           "BCV listing or fund filing (T4).")
for s in ("ameritrust-financial-technologies-inc", "binoptics-corp", "happy-inspector-inc", "leverege-holdings-llc", "opternative-inc",
          "plato-networks-inc", "scanscout-inc", "tremor-video-inc", "trxade-group-inc", "agora-intelligence-inc", "visibly-inc",
          "ianacare-inc"):
    out(s, "Steven Lee was BCV's Director of Strategic Investing only in 2019-2020; this 'Steven Lee' seat either falls outside that window "
           "or, inside it, is an uncorroborated match on a very common name with no BCV listing, post or fund filing (s1: a name match "
           "never suffices alone).")
for s in ("consumers-united-inc", "iloop-mobile-inc", "metamarkets-group-inc", "zipmark-inc", "vico-software-inc"):
    out(s, "Matt Harris joined BCV in September 2012 (Justworks' S-1); this 2009-2011 seat is from his years running Village Ventures (T4).")
out("appconomy-inc", "Kevin Zhang joined BCV in 2018; the 2011 filing names a namesake (T4).")
out("switch-therapeutics-inc", "A biotech 'Kevin Zhang' seat (2022): a common-name namesake with no BCV listing or fund filing; BCV does not "
                              "invest in therapeutics.")
for s in ("amec-plc", "ci-holding-co-of-georgia", "connolly-holdings-inc"):
    out(s, "A namesake John Connolly (AMEC's chairman; an Atlanta family holding company), not BCV's John M. Connolly (T4).")
for s in ("cloud-guru-group-inc", "iboss-inc", "liquidx-inc", "7park-data-inc"):
    out(s, "John M. Connolly was at BCV until 2017 (Senior Advisor in its last years); this 2018-2020 filing seat is from after his tenure (T4).")
out("98point6-technologies-inc", "Sarah Smith left BCV in 2021; the 2022 Seattle filing seat is from after her tenure (T4).")
out("theragen-inc", "Alex Evans joined BCV's crypto team in 2021; the 2016 medical-device filing names a namesake (T4).")
out("trilogy-international-partners-llc", "An 'Alexander Evans' on a 2010 telecom holding company's filing: a namesake of BCV's Alex Evans, who "
                                          "joined in 2021 (T4).")
for s in ("pay-with-spire-inc", "rainforest-beverages-llc"):
    out(s, "Matthew Brennan was at BCV in 2013-2017; this 2010 or 2025 filing seat is outside that window (T4).")

dup("factor-systems-inc", "billtrust", "Factor Systems, Inc. is Billtrust's legal name ('Factor Systems, Inc. (d/b/a Billtrust)', Justworks' S-1 "
                                       "on Matt Harris's directorships).")
dup("thorley-industries-llc", "4moms", "Thorley Industries LLC is 4moms' legal entity (Pittsburgh), the Form D issuer for its rounds.")
dup("sm-holdco-llc", "surveymonkey", "SM Holdco LLC is the Palo Alto holding company of SurveyMonkey's 2009 recapitalisation, the vehicle BCV "
                                    "invested through.")
dup("cellular-longevity-inc", "loyal", "Cellular Longevity, Inc. is Loyal's legal name (the dog-longevity company, San Francisco).")
dup("material-technologies-corp", "material-bank", "Material Technologies Corp (Boca Raton) is Material Bank's legal entity.")
dup("shop-my-shelf-inc", "shopmy", "Shop My Shelf, Inc. is ShopMy's legal name.")
dup("m-c-acquisition-corp", "m-c-communications", "M|C Acquisition Corp is the acquisition vehicle for M|C Communications, which the firm listed.")

if __name__ == "__main__":
    jl.write("members-1", L)
