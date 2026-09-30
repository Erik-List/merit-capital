"""Form D name-match rows and the listed acquirers (PRO-102 grind). D2, D7."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import verdict, write, LISTING  # noqa: E402

E = "https://www.sec.gov/Archives/edgar/data"
L = []


def nm(slug, basis, acc_url=None):
    L.append(verdict(slug, "not_member", basis, ec="formd_adjudicated", conf="high", cite=acc_url))


nm("allevion-therapeutics-inc",
   "Form D name-match only (D7): the related person 'Jack Wang', director of an Irvine, CA biotech (2021, 2024), "
   "is a US biotech director; Project A's Jack Wang is a London partner who joined in 2021 and invests in European "
   "software and defence. No Project A listing, post or press ties the company to the firm.")
nm("digitail-inc",
   "Form D name-match only (D7): Andreas Helbig is a director on Digitail's 2025 Form D; he appears on Project A's "
   "team pages only in 2020, so a 2025 seat is dated outside his tenure (T4, seat dating). No Project A listing, post "
   "or press names Digitail.")
nm("efficient-drivetrains-inc",
   "Form D name-match only (D7): 'Jack Wang', director of a Milpitas, CA drivetrain maker on its 2016-2017 Form Ds, "
   "predates Project A's Jack Wang (on the team from 2021). No Project A listing or post names the company.")
nm("klein-ndoh-acquisitions-fund-ii-llc",
   "Form D name-match only (D7): a 2013 New York acquisitions fund with a 'Jack Wang' as executive officer; a fund "
   "vehicle, not an operating company (T5), and not Project A's partner (on the team from 2021).")
nm("verifyme-inc",
   "Form D name-match only (D7): VerifyMe, Inc. (Lake Mary, FL, a listed company) names a 'Jack Wang' as executive "
   "officer on its 2023 Form D; an officer of the issuer, not Project A's London partner, and no Project A listing "
   "or post names the company.")
nm("grande-west-transportation-group-inc",
   "Form D name-match only (D7): 'John Wang', executive officer of a Canadian bus maker (2020), matched the roster's "
   "Jack Wang loosely; a different person, no Project A evidence.")
nm("noodoe-group-inc",
   "Form D name-match only (D7): 'John Wang', executive officer of a Houston EV-charging company (2023), a different "
   "person from Project A's Jack Wang; no Project A listing or post names the company.")
nm("statics-inc",
   "Form D name-match only (D7): 'Johnny Wang', executive officer of a Laguna Beach company (2024), a different "
   "person from Project A's Jack Wang; no Project A listing or post names the company.")

L.append(verdict("modernizing-medicine", "not_member",
                 "Sale consideration (D2; COLLECTION.md s1, Erik 2026-09-22): the CMS files ModMed under Fund II, 2022, with "
                 "no entry round because Project A holds it only through ModMed's purchase of Klara (the firm's own post "
                 "'Exit: Patient collaboration platform Klara is acquired by ModMed', 2022-02-08). The investment is Klara.",
                 ec="site_listing", conf="high", cite="https://www.project-a.vc/blog/patient-collaboration-platform-klara-is-acquired-by-modmed"))
L.append(verdict("navan", "not_member",
                 "Sale consideration (D2): the CMS files Navan (formerly TripActions) under Fund II, 2022, with no entry round; "
                 "Navan bought Project A's Comtravo in 2022, and Project A holds Navan stock only as consideration. The "
                 "investment is Comtravo.", ec="site_listing", conf="high", cite=LISTING))

if __name__ == "__main__":
    write("formd-and-acquirers", L)
