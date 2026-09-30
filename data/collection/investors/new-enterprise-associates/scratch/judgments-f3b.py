"""f3b: the status pass over the 71 members whose status is unknown (FIX-CANON-BRIEF.md Part B, status-unknown.json).
One bounded attempt per row: Google News through nq.py (the brief's status query, then the plain name), EDGAR
full-text search (efts, through secget's throttle), the company's own domain where the record carries one, and
Wikipedia. Acquired, defunct and unknown rows carry below_1b; gaov and gtel stay undetermined (identity unresolved).
Run: NQ_TAG=f3 python3 judgments-f3b.py"""
import json

import judge_lib as jl
from judge_lib import cls

SEC = "https://www.sec.gov/Archives/edgar/data/"
DONE = "Status pass 2026-09-30: "
NONE = "Google News and EDGAR full-text search found no sale, shutdown or recent operation"


def acq(slug, note):
    return cls(slug, status="acquired", rng="below_1b", note=DONE + note)


def dead(slug, note):
    return cls(slug, status="defunct", rng="below_1b", note=DONE + note)


def unk(slug, extra="", rng="below_1b"):
    return cls(slug, status="unknown", rng=rng,
               note=DONE + NONE + (f"; {extra}" if extra else "") + ", so the state stays unknown.")


NETSOL = SEC + "1039280/000149315224038751/form10-k.htm"
WRLD = (f"NetSol Technologies, the investor in WRLD3D (eeGeo renamed), booked the loss on the liquidation of WRLD3D "
        f"in its year to June 2023 (10-K, {NETSOL}), so the company is defunct")

L = [
    # acquired
    acq("amplica-inc", "acq. by COMSAT (the firm's own 2008 listing reads Public/Acquired by COMSAT, "
        f"{jl.ARCH('amplica-inc')}); the year of the sale is not on record."),
    acq("apnex-medical-inc", "acq. by Cyberonics, 2013: Cyberonics bought most of the assets of Apnex Medical, "
        f"which had ceased operations, for $2.1M ({SEC}864683/000086468313000044/cybx-20131025x10q.htm), an asset "
        "sale after the business stopped, read as acquired with Cyberonics as successor."),
    acq("blackbird", "acq. by Surf Air, 2020 (WSJ, 2020-02-12, "
        f"{jl.NEWS('blackbird', 'Surf Air Buys BlackBird')})."),
    acq("hospital-group-of-america-inc", "acq. by NuMED (the firm's own 2008 listing reads Private/Acquired by "
        f"NUMED, {jl.ARCH('hospital-group-of-america-inc')}); HGA later sat inside The Cooper Companies, which sold "
        f"it in 1999 ({SEC}711404/000095011701000155/0000950117-01-000155.txt). The year NuMED bought it is not on "
        "record."),
    acq("lifemetrix-inc", "acq. by Matria Healthcare, 2002: Matria agreed in April 2002 to buy LifeMetrix's "
        "cancer disease management business, Quality Oncology, with LifeMetrix's related software and contracts "
        f"({SEC}1007228/000100722802000006/qo8k.txt), and the firm's listing reads Acquired by Matria Healthcare."),
    acq("maxiscale-inc", "acq. by Overland Storage, 2010: Overland completed the purchase of MaxiScale's "
        f"intellectual property and folded it into its Snap Server line ({SEC}889930/000119312510258775/dex991.htm), "
        "an asset sale read as acquired with Overland as successor."),
    acq("pacificdental-benefits-inc", "acq. by UnitedHealth Group, 2005: UnitedHealth's results note "
        f"PacificDental Benefits, Inc., acquired in June 2005 ({SEC}731766/000119312505141940/dex99.htm)."),
    acq("primax-recoveries-inc", "acq. by Affiliated Computer Services, 2006, for $40M plus up to $10M contingent "
        f"({SEC}2135/000095013406015536/d38652exv99w1.htm)."),
    acq("think3-inc", "acq. by Versata, 2010 (Digital Engineering 24/7, 2010-10-07, "
        "https://www.digitalengineering247.com/article/think3-inc-acquired-by-versata-enterprises)."),
    # defunct
    dead("autoimmune-inc", "AutoImmune deregistered in March 2010 and put a Plan of Complete Liquidation and "
         f"Dissolution to its shareholders for 2010-05-11 ({SEC}879106/000119312510082615/ddef14a.htm), so it reads "
         "defunct."),
    dead("eegeo", WRLD + "; eegeo, kimble-inc and recce are one company in the base."),
    dead("kimble-inc", WRLD + "; kimble-inc is eeGeo's US issuer, the same company as eegeo and recce."),
    dead("recce", WRLD + "; Recce was eeGeo's map product, the same company as eegeo and kimble-inc."),
    dead("fetchr", "its top backer BECO Capital called Fetchr insolvent after a $100M Saudi tax bill, with "
         f"liquidation on the table (Bloomberg, 2021-10-06, {jl.NEWS('fetchr', 'Liquidation - Yahoo')}), and no "
         "report shows it operating since, so it reads defunct."),
    dead("peptimmune-inc", "Peptimmune filed Chapter 7 in March 2011 after its Series D fell through (Fierce "
         "Biotech, 2011-03-22, https://www.fiercebiotech.com/biotech/peptimmune-heads-into-bankruptcy-after-venture-"
         "round-fizzles)."),
    dead("satori-pharmaceuticals", "Satori shut down in 2013 after its gamma-secretase modulators damaged the "
         "kidneys of monkeys in preclinical work (Alzforum, 2013-06-07, https://www.alzforum.org/news/research-news/"
         "satori-pharmaceuticals-shuts-down-abandons-g-secretase-modulators)."),
    dead("skyline-solar-inc", "Wikipedia records that Skyline Solar's operation appears to have ceased in late "
         f"2012 and its website was deactivated ({jl.W('Skyline Solar')})."),
    dead("solfocus-inc", "Wikipedia lists SolFocus among the concentrator PV makers whose manufacturing closed "
         f"({jl.W('Concentrator photovoltaics')}); its Form D filings stop and solfocus.com is gone (HTTP 410)."),
    # left unknown
    unk("3jam-inc", "3jam.com does not resolve"),
    unk("ajax-vascular", "EDGAR names it only in a director biography (Ulthera's 2014 S-1)"),
    unk("astrowatt", "EDGAR names it only in director biographies (Audience's 2012 S-1)"),
    unk("avos", "news covers only the founders and the 2011 Delicious purchase"),
    unk("azuray-technologies-inc", "EDGAR names it only in director biographies"),
    unk("bandgap-engineering", "the name returns only unrelated research articles"),
    unk("bariatric-partners-inc", "bariatricpartners.com does not resolve"),
    unk("bedrocket-media-sportsrocket", "coverage ends in 2017 (Forbes on Sportsrocket) and sportsrocket.com now "
        "redirects to a parked page"),
    unk("benu-inc", "an eBenX 10-Q shows Benu (formerly Emerge HealthCare) raising a Series B in 2002 and "
        "benu.com is parked for sale"),
    unk("braincells-inc", "nothing after its 2011 Form D"),
    unk("cape", "coverage of Cape Productions ends by 2018"),
    unk("captora", "the last report is its $22M round of May 2014 (Marketing Dive)"),
    unk("china-gtel-limited", "EDGAR names it only in a director biography (Tuniu)"),
    unk("compass-labs-inc", "the EDGAR hits are unrelated companies"),
    unk("complexa", "the last report is its $62M Series C of July 2017"),
    unk("cydan", "the last reports are its 2017 financing and the 2019 launch of Tiburio, and cydan.com does not "
        "resolve"),
    unk("denali-medical-ii", "an incubator entity with nothing after its 2011 filing"),
    unk("edimer-pharmaceuticals", "only the 2018 NEJM report on EDI200, nothing on the company"),
    unk("gaov", "the company still cannot be identified", rng=None),
    unk("gtel", "the company still cannot be identified", rng=None),
    unk("hdmessaging", "the firm's link brightkite.com does not resolve"),
    unk("hospital-partners-of-america-inc", "2008 Houston Chronicle coverage calls it a troubled owner selling "
        "St. Joseph Medical Center, and hospitalpartners.com is parked for sale"),
    unk("huddler", "the EDGAR hits are a director biography"),
    unk("hyperfair", "only its 2014 convertible round, and the firm's link hyperverseinternational.com does not "
        "resolve"),
    unk("illumitex-inc", "it ended its LED lighting business in February 2020 to become a FarmVisionAI software "
        "company (https://www.newswire.com/news/illumitex-pivots-to-a-pure-play-agtech-farmvisionai-company-"
        "21097963) and nothing later is on record"),
    unk("intarvo", "the name returns only unrelated items"),
    unk("koozoo"),
    unk("learnup", "nothing after 2015"),
    unk("legato-medical"),
    unk("likelihood"),
    unk("lsf-network", "the EDGAR hits are unrelated"),
    unk("luminate-wireless", "a web search found no sale; vendor profiles list it closed, which does not settle "
        "it (aligned with the GV row)"),
    unk("lytmus", "the only hits are the unrelated 2026 Indian Lytmus AI"),
    unk("mayan-networks", "Ariel's 2001 filings show the merger pending (10-K of 2001-03-30, S-4/A of July 2001) "
        "but no completion or later record (aligned with the TCV row)"),
    unk("mnectar", "the last report is from 2016"),
    unk("nazomi-communications-inc", "EDGAR shows only its 2003-04 dispute with ARM and nazomi.com is parked for "
        "sale"),
    unk("poggled"),
    unk("primary-health-inc", "the EDGAR hits are other companies of the same name"),
    unk("rapid-mobile-media-limited"),
    unk("reshape-inc", "EDGAR names it only in director biographies"),
    unk("sengled", "its cloud service failed in 2025, Amazon ended its Alexa skill (The Verge, 2025-08-04, "
        f"{jl.NEWS('sengled', 'downfall')}) and its US store reads Store unavailable, but no shutdown or sale of "
        "the company is on record"),
    unk("serious-energy", "the 2012 SFGATE report of its troubles is the last news and seriousenergy.com shows "
        "only a contact line"),
    unk("serious-materials-inc", "the same company as serious-energy, whose state is unknown"),
    unk("svaya-nanotechnologies", "EDGAR shows only venture loans to it in 2010-12"),
    unk("t-ram-semiconductor-inc", "EDGAR names it only in director biographies"),
    unk("united-medical-plan"),
    unk("viacor-inc", "nothing after its 2010 Form D"),
    unk("vibrynt-inc", "EDGAR names it only in director biographies"),
    unk("visual-edge-technology-inc", "the EDGAR hits are other companies"),
    unk("waltz-networks", "the only item is a 2016 Fortune Term Sheet mention"),
    unk("zyngenia", "the last reports are from 2011-12"),
]
L = [x for x in L if x]

# exploramed-iv and prospex-medical-iii-inc are left out: F2 ruled both not_member under R3 (incubator vehicles).
want = set(json.load(open(jl.INV / "scratch" / "status-unknown.json"))) - {"exploramed-iv", "prospex-medical-iii-inc"}
got = [x["slug"] for x in L]
assert len(got) == len(set(got)), [s for s in got if got.count(s) > 1]
assert set(got) == want, (sorted(want - set(got)), sorted(set(got) - want))

jl.write("f3b", L)
