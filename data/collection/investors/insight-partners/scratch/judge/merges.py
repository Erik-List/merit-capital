#!/usr/bin/env python3
"""Write companies/identity-merges.json from the run's merge decisions.

Canonicals are given by the firm's own site slug and resolved to the base slug
through the row's site_url, because the base derives its slug from the display
name ("Candy Fanatics (fka Candy Digital)") and the site from its permalink
("candy-capital"). Duplicates are base slugs. Re-runnable: the list below is
the whole file.
Usage: python3 .../scratch/judge/merges.py"""
import json, sys
from pathlib import Path
INV = Path(__file__).resolve().parents[2]
ROOT = INV.parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import write_atomic  # noqa: E402

base = json.load(open(INV / "companies/base.json"))
rows = base if isinstance(base, list) else list(base.values())
by_site = {r["site_url"].rstrip("/").split("/")[-1]: r["slug"] for r in rows if r.get("site_url")}
slugs = {r["slug"] for r in rows}

# (site slug of the canonical, [duplicate base slugs], reason, pinned name or None)
M = [
 ("airwatch", ["a-w-s-holding-llc"], "A.W.S. Holding, LLC (Atlanta) is AirWatch's holding company; its 2013 Form D is the $200M round the firm's post of 2013-02-24 announces", None),
 ("abnormal-ai", ["abnormal-security-corp"], "Abnormal Security Corp renamed itself Abnormal AI in 2025", None),
 ("achieve3000", ["ac-holdco-inc"], "AC HoldCo, Inc. files from the firm's own address with Achieve3000's officers (Lakewood and Red Bank, NJ): Achieve3000's holding company", None),
 ("alma", ["arlozorov9-inc"], "Arlozorov9, Inc. is Alma's registered name (its Form Ds name Alma's founder and board); the 2021 rounds are Alma's Series B and C", None),
 ("inspiren", ["all-inspire-health-inc"], "All Inspire Health, Inc. is Inspiren's registered name (Brooklyn)", None),
 ("conga", ["appextremes-group-holdings-llc"], "AppExtremes Group Holdings, LLC (Broomfield) is the holding company of AppExtremes, LLC, which trades as Conga", None),
 ("apprentice-io", ["apprentice-fs-inc"], "Apprentice FS, Inc. (Jersey City) trades as Apprentice.io", None),
 ("a-team", ["ateams-inc"], "ATeams, Inc. trades as A.Team", None),
 ("kinetic-social", ["azoogle-com-inc"], "Azoogle.com, Inc. became Epic Media Group, from which Kinetic Social was spun out in 2011; the firm lists Kinetic Social under Epic's own web address, so the 2010 Form D and the listing are one investment", None),
 ("alteryx", ["azurite-software-holdings-inc"], "Azurite Software Holdings, Inc. (Irvine) is the vehicle of the 2024 take-private of Alteryx by Clearlake and Insight; the row is Alteryx, a member on its 2014 round", None),
 ("keeper-security", ["callpod-inc"], "Callpod, Inc. (Chicago) trades as Keeper Security", None),
 ("fuze", ["callwave-inc"], "CallWave, Inc. renamed itself Fuze; the funds' ownership filings from 2004 are the CallWave position", None),
 ("candy-capital", ["candy-digital-inc"], "Candy Digital, Inc. is the company the firm lists as Candy Fanatics (fka Candy Digital)", None),
 ("capella-university", ["capella-education-co"], "Capella Education Company is the listed parent of Capella University; the funds' 2006 filings are the position the firm lists", "Capella Education"),
 ("ceresai", ["ceres-imaging-inc"], "Ceres Imaging, Inc. renamed itself Ceres AI", None),
 ("colab-software", ["colab-ai-inc"], "CoLab AI Inc. is CoLab Software's US entity", None),
 ("xchange-formerly-exchange-applications-inc", ["exchange-applications-inc"], "Exchange Applications, Inc. renamed itself Xchange; the firm lists it as 'xchange (Formerly Exchange Applications Inc.)'", "Xchange"),
 ("averna-therapeutics", ["exsilio-therapeutics-inc"], "Exsilio Therapeutics renamed itself Averna Therapeutics (the firm's own panel says so)", None),
 ("fiddler-ai", ["fiddler-labs-inc"], "Fiddler Labs, Inc. trades as Fiddler AI", None),
 ("openenglish", ["foxyp2-inc-f-k-a-thinkglish-inc", "open-education-holdings-inc"], "FOXYP2, Inc. (formerly Thinkglish) and Open Education Holdings Inc. (Miami) are Open English's parent companies; both Form Ds name the firm's partners", "Open English"),
 ("glia-fka-salemove", ["glia-technologies-inc"], "Glia Technologies, Inc. is Glia (fka SaleMove)", None),
 ("gtmhub", ["gtmhub-usa-inc"], "Gtmhub USA, Inc. is Quantive (fka Gtmhub)", None),
 ("healthcaresource-com", ["healthcaresource-hr-inc"], "HealthcareSource HR, Inc. is the company the firm lists as Healthcaresource.com", "HealthcareSource"),
 ("honeycomb-io", ["hound-technology-inc"], "Hound Technology, Inc. trades as Honeycomb", None),
 ("imperfect-foods", ["imperfect-foods-inc"], "Imperfect Foods, Inc. is the company the firm lists as Misfits Market (fka Imperfect Foods)", None),
 ("project-canary", ["international-environmental-standards-pbc"], "International Environmental Standards, PBC (Denver) trades as Project Canary; its 2022 Form D is the $111M round the firm's post announces", None),
 ("iterative-scopes", ["iterative-scopes-inc"], "Iterative Scopes, Inc. renamed itself Iterative Health", None),
 ("ntop", ["ntopology-inc"], "nTopology Inc. renamed itself nTop", None),
 ("own-company", ["ownbackup-ltd"], "OwnBackup Ltd renamed itself Own Company", None),
 ("pictorlabs-ai", ["pictor-labs-inc"], "Pictor Labs, Inc. trades as PictorLabs.ai", None),
 ("prophecy-io", ["simpledatalabs-inc"], "SimpleDataLabs Inc trades as Prophecy", None),
 ("sentinelone", ["sentinel-labs-inc"], "Sentinel Labs, Inc. is SentinelOne's former registered name", None),
 ("6-waves", ["six-waves-inc"], "Six Waves Inc. is the company the firm lists as 6 Waves", None),
 ("mural", ["tactivos-inc"], "Tactivos, Inc. trades as MURAL", None),
 ("trialjectory", ["trialmatch-me-inc"], "trialmatch.me, Inc. (Closter, NJ) traded as TrialJectory, now Leal Health", None),
 ("nymbus", ["vensure-enterprises-llc"], "Vensure Enterprises, LLC is the holding company of NYMBUS's founder through which the firm's 2015 money went into NYMBUS; its one Form D names two of the firm's partners", None),
 ("vts", ["view-the-space-inc"], "View The Space, Inc. trades as VTS", None),
 ("fleetworthy", ["great-dane-holding-llc", "tollpass-llc"], "Great Dane Holding, LLC (Latham, NY and Atlanta) and Tollpass, LLC (care of Bestpass, Albany) are the holding companies of Bestpass, now Fleetworthy; the firm's post calls its investment a minority one, beside Susquehanna Growth Equity", None),
 ("appriss-retail", ["alert-holding-company-inc"], "Alert Holding Company, Inc. (Louisville) is Appriss's holding company; the firm lists Appriss Retail and Bamboo Health (formerly Appriss Health), the two businesses it was split into", None),
 ("bamboo-health", ["appriss-health-holdings-inc"], "Appriss Health Holdings, Inc. is the holding company of Appriss Health, renamed Bamboo Health in 2021", None),
 ("marigold-fka-campaign-monitor", ["campaign-monitor-holdings-pty-ltd", "campaign-monitor-holdings-uk-ltd"], "Campaign Monitor Holdings Pty Ltd (Sydney) and Campaign Monitor Holdings (UK) Ltd are the holding companies of Campaign Monitor, now Marigold; their Form Ds name the firm's partners and the two founders", None),
 ("pdi", ["pds-parent-inc"], "PDS Parent, Inc. (Alpharetta) is PDI's holding company, which the firm's partners joined in 2019 beside the directors of its existing owners", None),
 ("gradial", ["panorama-artificial-intelligence-corp"], "Panorama Artificial Intelligence Corp. (Seattle) trades as Gradial; its 2026 Form D is the $65M Series C the firm's post announces", None),
 ("recorded-future", ["rf-parent-inc", "rf-ultimate-parent-inc"], "RF Parent, Inc. and RF Ultimate Parent, Inc. are the vehicles of the 2019 acquisition of Recorded Future; the row is Recorded Future, a member on its 2017 round", None),
]
NEVER = [
 {"slugs": ["resolve", "resolve-systems"], "reason": "Resolve (resolvepay.com, San Francisco, B2B net terms) and Resolve Systems (Irvine, IT incident response, bought by the firm in 2017) are two companies; the Form D joined to 'resolve' is Resolve Systems'"},
]
out, problems = [], []
# A holding company whose platform was ruled a control position is not merged:
# the build applies exclusions before merges, so each takes its own verdict
# (control pass, 2026-09-27).
CONTROL = {"conga", "healthcaresource-com", "appriss-retail", "bamboo-health", "pdi"}
M = [m for m in M if m[0] not in CONTROL]

for site_slug, dups, reason, name in M:
    canon = by_site.get(site_slug)
    if not canon:
        problems.append(f"no base row for site slug {site_slug}")
        continue
    miss = [d for d in dups if d not in slugs]
    if miss:
        problems.append(f"{site_slug}: duplicates not in the base: {miss}")
    m = {"canonical": canon, "duplicates": [d for d in dups if d in slugs], "reason": reason}
    if name:
        m["name"] = name
    out.append(m)
if problems:
    print("\n".join(problems))
doc = {"insight-partners": {
    "_readme": ("Identity merges for Insight Partners. The EDGAR layers name a company by its registered or holding-company "
                "name while the firm's site uses the brand, and the firm's buyout vehicles file Form D as 'X Parent' or "
                "'X HoldCo'. Canonical is the rendering on the firm's live site. A holding company whose platform is a "
                "control position is not merged: it takes its own control verdict, because the build applies exclusions "
                "before merges and a merge onto an excluded canonical never runs (COLLECTION.md 8)."),
    "merges": out, "rejects": [], "never_merge": NEVER}}
write_atomic(INV / "companies/identity-merges.json", json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
print(f"{len(out)} merges written, {len(problems)} problems")
