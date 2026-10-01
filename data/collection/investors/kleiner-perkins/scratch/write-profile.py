#!/usr/bin/env python3
"""Assemble Kleiner Perkins' researched profile fields into investor/investor.json and investor/sources.json
(COLLECTION.md s11; PRO-99). Re-runnable (GV's pattern): every value is either a constant researched in
scratch/profile-research.json or recomputed here from the files on disk, so a second run after a rebuild restates
the base-dependent fields (stage counts, geo, scope, range) and leaves what the shared scripts own alone.

What this script writes: name, investor_type, website, founding_year, history, investment_concept, aum, funds,
icon_url (until an upload replaced it), investment_stage, investment_geo, investment_scope, investment_range,
notable_investments, and the sidecar's top-level `flags` (what a reviewer should rule on).
What it never writes: hq_location (scripts/firm-offices.py), individuals and updated_at (scripts/build-firm-profile.py).

After a run, in this order from the repo root:
  python3 scripts/site-portfolio.py kleiner-perkins --no-fetch-profiles
  python3 scripts/firm-offices.py kleiner-perkins
  python3 scripts/build-firm-profile.py kleiner-perkins     (rewrites the investment_scope and individuals bases)
  python3 scripts/profile_copy.py kleiner-perkins
Usage: python3 write-profile.py
"""
import collections
import importlib.util
import json
import statistics
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parents[4] / "scripts"
sys.path.insert(0, str(SCRIPTS))
from paths import Paths, write_atomic  # noqa: E402
import profile_copy  # noqa: E402

SLUG = "kleiner-perkins"
P = Paths(SLUG)
REL = f"data/collection/investors/{SLUG}"
SITE = "https://www.kleinerperkins.com"
WIKI = "https://en.wikipedia.org/wiki/Kleiner_Perkins"
ADV_PDF = "https://reports.adviserinfo.sec.gov/reports/ADV/161035/PDF/161035.pdf"
POST_2026 = f"{SITE}/perspectives/our-new-funds-kp22-select-iv-flex/"
POST_2024 = f"{SITE}/perspectives/announcing-kp21-and-select-iii/"
POST_2022 = f"{SITE}/perspectives/announcing-kp20-and-kp-selectii/"
POST_SELECT = f"{SITE}/perspectives/kleiner-perkins-select/"
POST_KP19 = f"{SITE}/perspectives/announcing-kp19/"
CB_2019 = ("https://news.crunchbase.com/venture/kleiner-perkins-raises-a-600m-early-stage-fund-as-the-storied-firm-"
           "enters-a-new-chapter/")
REUTERS_2014 = "https://www.yahoo.com/news/kleiner-perkins-files-raise-1-002240762.html"
TC_2012 = "https://techcrunch.com/2012/05/17/kleiner-perkins-closes-on-525-million-kpcb-15/"
TC_2008 = "https://techcrunch.com/2008/05/01/kleiner-perkins-goes-green-with-12-billion-in-two-new-funds/"
VB_2006 = "https://venturebeat.com/2006/02/15/kleiner-perkins-surprises-with-200-million-pandemic-fund/"

inv = json.loads(P.investor.read_text()) if P.investor.exists() else {"slug": SLUG}
src = json.loads(P.investor_sources.read_text()) if P.investor_sources.exists() else {"slug": SLUG, "fields": {}}
src.setdefault("slug", SLUG)
src["run"] = "PRO-99"
F = src.setdefault("fields", {})


def put(key, value, source, basis, **extra):
    inv[key] = value
    F[key] = {"value": value, "source": source, "basis": basis, **extra}


def usd(x):
    return f"${x:,.0f}"


def musd(x):
    return f"${x / 1e9:.2f}B" if x >= 1e9 else f"${x / 1e6:.1f}M"


# ---------------------------------------------------------------- the landed base (members only, merged view)
base_rows = json.loads(P.base_json.read_text())
verdicts = json.loads(P.ledger.read_text())[SLUG]["verdicts"]
resolved = json.loads(P.resolved.read_text())
classification = json.loads(P.classification.read_text())


def merged(slug):
    row = dict(resolved.get(slug) or {})
    row.update(classification.get(slug) or {})        # run.py merge_rows: the overlay key wins
    return row


member_names = {r["slug"]: r["name"] for r in base_rows
                if (verdicts.get(r["slug"]) or {}).get("verdict") == "member"}
members = {s: merged(s) for s in member_names}
N = len(members)

# ---------------------------------------------------------------- identity
put("name", "Kleiner Perkins", f"{SITE}/",
    "The firm's own brand on kleinerperkins.com. Legal name Kleiner Perkins Caufield & Byers, LLC, primary business "
    "name 'Kleiner Perkins' (Form ADV Item 1.A and 1.B, CRD 161035, signed 2026-03-31). The firm traded as Kleiner "
    "Perkins Caufield & Byers (KPCB) until the rebrand: the last kpcb.com captures are 2018-03 and kleinerperkins.com "
    "is captured from 2018-07-17 (sources/wayback/cc-manifest-kp.json), so the archive dates the rename to 2018, "
    "while decisions.md says 'until the 2019 rebrand'; no press article dating it was found. Fund vehicles kept the "
    "long name through XIX (2020) and dropped it from Kleiner Perkins XX (2022).")
put("investor_type", "Institutional", ADV_PDF,
    "A venture capital firm investing outside capital through its own funds (42 private funds on Schedule D "
    "Section 7.B.(1) of its Form ADV, CRD 161035).")
put("website", SITE, f"{SITE}/", "The firm's own site, read 2026-09-30 (kpcb.com until the 2018 rebrand).")
put("founding_year", 1972, WIKI,
    "Wikipedia, 'Kleiner Perkins' (scratch/wiki/Kleiner_Perkins.txt): founded in 1972 by Eugene Kleiner and Tom "
    "Perkins in Menlo Park. The firm's own 2026 post agrees ('For 54 years', 2026 less 54 is 1972).")

# ---------------------------------------------------------------- reader-facing copy
THESIS = "“Make history.”"
put("investment_concept", THESIS, f"{SITE}/",
    "The hero headline of the firm's homepage, 'Make History' (the tagline in the hero's company ticker, and the "
    "description of the page's own WebSite schema), read 2026-09-30; set in sentence case with one closing period "
    "and published in quotation marks as the firm's own words. Competing line: the meta description, 'Kleiner "
    "Perkins is an American venture capital firm headquartered on Sand Hill Road in Menlo Park in Silicon Valley.' "
    "The About page's mission also carries the phrase: 'To be the first call for founders who want to make history "
    "and to partner with them as company builders in pursuit of that goal.'")

HISTORY_BETS = [("Genentech", "genentech"), ("Compaq", "compaq-computer-corporation"),
                ("Sun Microsystems", "sun-microsystems"), ("Netscape", "netscape"), ("Amazon", "amazon"),
                ("Google", "google"), ("Twitter", "twitter"), ("Spotify", "spotify"), ("Slack", "slack"),
                ("DoorDash", "doordash"), ("Figma", "figma")]
not_members = [n for n, s in HISTORY_BETS if s not in members]
if not_members:
    raise SystemExit(f"history names a company that is not a member in the ledger: {not_members}")
HISTORY = ("Kleiner Perkins was founded in 1972 in Menlo Park by Eugene Kleiner and Tom Perkins. The bets that made it "
           "were Genentech, Compaq, Sun Microsystems, Netscape, Amazon and Google, followed later by Twitter, Spotify, "
           "Slack, DoorDash and Figma. In 2026 it raised $3.5 billion: a $1 billion early-stage fund, its "
           "twenty-second, and $2.5 billion for growth investments.")
put("history", HISTORY, WIKI,
    "Founding (1972, Menlo Park, Eugene Kleiner and Tom Perkins) from Wikipedia, 'Kleiner Perkins'; the firm's 2026 "
    "post says 'For 54 years'. The bets are the firm's own company pages on kleinerperkins.com, each with its "
    "'Partnered Since' year: Genentech 1976 (co-founded by 'a young KP partner' with the firm's seed capital), "
    "Compaq 1982 ('one of the most important bets in KP history') and Sun Microsystems 1982, Netscape 1994, Amazon "
    "1996, Google 1999 ('We wrote our largest check ever'), Twitter 2010, Spotify 2011, Slack 2014, DoorDash 2015, "
    "Figma 2017; all eleven are verified portfolio companies. The raise is the firm's post of 2026-03-24 "
    f"({POST_2026}): 'KP22, a $1 billion fund to back early-stage companies' and '$2.5 billion in growth funds', "
    "$3.5 billion in all (TechCrunch, 2026-03-24, 'With $3.5B in fresh capital, Kleiner Perkins is going all in on "
    "AI'). Moved to this sidecar, not the page: the name Kleiner Perkins Caufield & Byers (Frank Caufield and Brook "
    "Byers became name partners; Byers joined in 1977) and the rebrand to Kleiner Perkins; the growth team under "
    "Mary Meeker, which left in September 2018 to form Bond, and the return to early-stage investing under Mamoon "
    "Hamid (joined 2017) and Ilya Fushman (joined 2018) with the $600M KP18 in January 2019; the green technology "
    "years (Green Growth Fund, 2008); KPCB China (2007, provisionally inside the portfolio on this page, "
    "decisions.md X1); the fund ladder (funds field); the firm's own count of over 1,000 companies backed and over "
    "$35 billion returned to its limited partners (post of 2022-01-11); the gross assets of its private funds (aum "
    "field).")

# ---------------------------------------------------------------- aum (an exempt reporting adviser: no Item 5.F)
adv = json.loads((P.sources / "adv" / "adv-7b-funds.json").read_text())
KP_CRD, CHINA_CRD = "161035", "161470"
kp_sum, china_sum = adv["sum_by_adviser"][KP_CRD], adv["sum_by_adviser"][CHINA_CRD]
kp_funds = adv["advisers"][KP_CRD]["funds_7b1"]
china_funds = adv["advisers"][CHINA_CRD]["funds_7b1"]
if kp_sum != sum(f["gav"] or 0 for f in kp_funds) or china_sum != sum(f["gav"] or 0 for f in china_funds):
    raise SystemExit("adv-7b-funds.json: sum_by_adviser does not equal the sum of its own fund rows")
unvalued = [f["name"] for f in kp_funds if f["gav"] is None]
china_ii = next(f["gav"] for f in kp_funds if f["name"].startswith("KPCB CHINA FUND II"))
put("aum", {"bottom": kp_sum, "top": kp_sum + china_sum}, ADV_PDF,
    "Kleiner Perkins (Kleiner Perkins Caufield & Byers, LLC; CRD 161035, SEC 802-75571) is an EXEMPT REPORTING "
    "ADVISER, so it files no Item 5.F and no regulatory assets under management exist. The sworn substitute is "
    "Schedule D Section 7.B.(1) of its Form ADV signed 2026-03-31 (data/filings/adv/161035.pdf, parsed into "
    f"sources/adv/adv-7b-funds.json). BOTTOM: {usd(kp_sum)}, the sum of the current gross asset values of the "
    f"{len(kp_funds)} private funds Kleiner Perkins itself reports ({len(kp_funds) - len(unvalued)} with a parsed "
    f"value; {', '.join(unvalued) or 'none'} has no parsed value in that file and adds nothing, although the ADV "
    "text prints $18,659,493 beneath its name, so the floor is understated by about that much). It includes KPCB "
    f"China Fund II, L.P. ({usd(china_ii)}), which is on Kleiner Perkins' own 7.B.(1). TOP: {usd(kp_sum + china_sum)}, "
    f"the bottom plus the {usd(china_sum)} that KPCB China Management, Ltd. (CRD 161470, SEC 802-75570, its own "
    "exempt reporting adviser) reports on its own 7.B.(1) for "
    + " and ".join(f"{f['name'].title().replace('Kpcb', 'KPCB')} ({usd(f['gav'])})" for f in china_funds)
    + ". KPCB China is provisionally inside the firm's boundary (decisions.md X1) and both of those funds are on "
    "Kleiner Perkins' own 7.B.(2) as funds it advises that another adviser reports, so the affiliated adviser's "
    "gross assets are added for the top only (COLLECTION.md s11, the Accel London shape); no fund is counted twice, "
    "the rosters are deduplicated by private fund ID. If Erik rules KPCB China out, the top falls to the bottom "
    "(and KPCB China Fund II would leave the bottom as well). Gross asset value is not net assets and not "
    "commitments: the 2026 funds are carried at the amounts they raised (XXII $995,000,000, Select Fund IV "
    "$1,920,000,000), which reads as commitments, not invested assets. Bond Capital "
    "Management (CRD 304391) is a separate firm since 2018 and is in neither end. No press figure is used.",
    flags=["era_7b_composite", "top_includes_kpcb_china_provisional"])

# ---------------------------------------------------------------- funds
def edgar(cik, accession):
    return f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession.replace('-', '')}/{accession}-index.htm"


def fund(name, size, vintage, source, note, accession=None, cik=None):
    entry = {"name": name, "size": size, "vintage": vintage}
    if accession:                       # asserted against TOTALAMOUNTSOLD at build time
        entry["accession"] = accession
    entry["sources"] = [{"source": source, "note": note}]
    if accession:
        entry["sources"].append({"source": edgar(cik, accession),
                                 "note": f"Form D {accession}: {usd(size)} sold of {usd(size)} offered."})
    return entry


FUNDS = [
    fund("Kleiner Perkins XXII, LLC", 995_000_000, 2026, POST_2026,
         "Firm post 2026-03-24: 'KP22, a $1 billion fund to back early-stage companies'. The Form D (first sale "
         "2026-03-23) and the ADV both carry $995,000,000, which is the size published; the firm rounds to $1 billion.",
         "0002115014-26-000001", 2115014),
    fund("Kleiner Perkins Select Fund IV, LLC", 1_920_000_000, 2026, POST_2026,
         "Firm post 2026-03-24: '$2.5 billion in growth funds'; Select Fund IV is $1.92B of it (Form D, first sale "
         "2026-03-23), Flex I the rest.", "0002114651-26-000001", 2114651),
    fund("Kleiner Perkins Flex I, LLC", 555_000_000, 2026, POST_2026,
         "The second of the 2026 growth funds: the post's address ends 'select-iv-flex', its text does not name "
         "Flex. Form D, first sale 2026-03-23; the ADV carries $550,000,000. Select Fund IV and Flex I together are "
         "$2.475B, the firm's '$2.5 billion'.", "0002114646-26-000001", 2114646),
    fund("Kleiner Perkins XXI, LLC", 825_000_000, 2024, POST_2024,
         "Firm post 2024-06-28: 'KP21, an $825M fund to back early stage companies'. Form D, first sale 2024-06-28.",
         "0002027881-24-000002", 2027881),
    fund("Kleiner Perkins Select Fund III, LLC", 1_200_000_000, 2024, POST_2024,
         "Firm post 2024-06-28: 'KP Select III, a $1.2 billion fund to back high inflection investments'. The Form D "
         "carries XXI's filer prefix; the issuer is Select Fund III (CIK 2027882).",
         "0002027881-24-000001", 2027882),
    fund("Kleiner Perkins XX, LLC", 800_000_000, 2022, POST_2022,
         "Firm post 2022-01-11: 'KP 20, an $800m fund to back early stage companies'. Form D 0001894867-22-000001: "
         "$800M offered, $0 sold (filed before the close), so the size is the firm's and no accession is asserted."),
    fund("Kleiner Perkins Select Fund II, LLC", 1_000_000_000, 2022, POST_2022,
         "Firm post 2022-01-11: 'KP Select II, a $1 billion fund'. Form D 0001894699-22-000001: $1B offered, $0 sold."),
    fund("Kleiner Perkins Select Fund, LLC", 750_000_000, 2021, POST_SELECT,
         "Firm post 2021-04-19: 'Kleiner Perkins Select, a new $750M fund' (Select I). Form D 0001853994-21-000001: "
         "$750M offered, $0 sold."),
    fund("Kleiner Perkins Caufield & Byers XIX, LLC", 700_000_000, 2020, POST_KP19,
         "Firm post 2020-03-05: 'KP19, with $700M to focus on early-stage investments'. Form D "
         "0001801167-20-000001: $700M offered, $0 sold."),
    fund("Kleiner Perkins Caufield & Byers XVIII, LLC", 600_000_000, 2019, CB_2019,
         "Crunchbase News 2019-01-31: the firm 'had raised $600 million in new capital for its 18th venture fund'; "
         "the firm's KP19 post: 'When we announced KP18 in January of last year'. Form D 0001764543-19-000001: $600M "
         "offered, $0 sold."),
    fund("Kleiner Perkins Caufield & Byers XVII, LLC", 400_000_000, 2016, CB_2019,
         "Crunchbase News 2019-01-31: Fund XVII (2016) was $400 million. Form D 0001678018-16-000001: $400M offered, "
         "$0 sold."),
    fund("KPCB Digital Growth Fund III, LLC", 1_000_000_000, 2016, CB_2019,
         "Crunchbase News 2019-01-31: '$1 billion for its third Digital Growth Fund', raised beside XVII in 2016. "
         "Form D 0001678000-16-000001: $1B offered, $0 sold. Managed by the growth team that left to form Bond in "
         "September 2018; the vehicle stayed a Kleiner Perkins fund (decisions.md D2)."),
    fund("Kleiner Perkins Caufield & Byers XVI, LLC", 450_000_000, 2014, REUTERS_2014,
         "Reuters 2014-06-28: filed for 'an early-stage growth fund of $450 million'; Fortune 2014-04-14 gave the "
         "same target. Form D 0001611731-14-000001: $450M offered, $0 sold. The size is the offering; no close "
         "announcement was found."),
    fund("KPCB Digital Growth Fund II, LLC", 750_000_000, 2014, REUTERS_2014,
         "Reuters 2014-06-28: 'a later-stage fund of $750 million'; Fortune 2014-04-14: '$750 million for its second "
         "digital growth fund'. Form D 0001611731-14-000002 (XVI's filer prefix, issuer CIK 1611736): $750M offered, "
         "$0 sold. The size is the offering."),
    fund("Kleiner Perkins Caufield & Byers XV, LLC", 525_000_000, 2012, TC_2012,
         "TechCrunch 2012-05-17: 'closed on a $525 million round for its fifteenth venture fund, dubbed KPCB 15'. "
         "Form D 0001547840-12-000001: $525M offered, $0 sold."),
    fund("KPCB China Fund II, L.P.", 250_000_000, 2011, "https://venturebeat.com/business/kleiner-perkins-china-fun",
         "VentureBeat 2011-11-03: 'Kleiner Perkins has raised a $250 million fund to invest in Chinese companies, "
         "according to a filing'. Form D 0001533831-11-000001: $250M offered, $0 sold; no close announcement was "
         "found, so the size is the offering. On Kleiner Perkins' own 7.B.(1). Listed under the provisional reading "
         "of decisions.md X1."),
    fund("Kleiner Perkins Caufield & Byers XIV, LLC", 650_000_000, 2010,
         "https://fortune.com/2010/10/27/kleiner-perkins-goes-big-vc-firm-raising-more-than-1-billion",
         "Fortune 2010-10-27: KPCB XIV 'is targeting $650 million'; Fortune 2011-02-16: 'sources say that the final "
         "figure will be slightly higher'. Form D 0001505781-10-000001: $650M offered, $0 sold. The final close was "
         "not published, so the size is the offering."),
    fund("KPCB Digital Growth Fund, LLC", 1_000_000_000, 2010,
         "https://fortune.com/2011/02/16/kleiners-digital-fund-passes-1-billion-mark",
         "Fortune 2011-02-16: 'KP recently increased the Digital Growth Fund's size to more than $1 billion' (the "
         "first target was $750M); TechCrunch 2012-05-17: 'In late 2010 the firm raised $1 billion for its digital "
         "growth fund'. The amended Form D 0001505782-11-000001 shows $932,326,251 sold of $1,000,000,000 offered "
         "(first sale 2010-11-17), not the full size, so no accession is asserted."),
    fund("Kleiner Perkins Caufield & Byers XIII, LLC", 700_000_000, 2008, TC_2008,
         "TechCrunch 2008-05-01: 'KPCB XIII, which will invest $700 million in greentech, information technology and "
         "life sciences ventures'. A paper Form D (2008-05-19), no machine-readable amount. Conflict: TechCrunch "
         "2012-05-17 says 'its 13th fund's offering was sized at $950 million'; the 2008 announcement is published."),
    fund("KPCB Green Growth Fund, LLC", 500_000_000, 2008, TC_2008,
         "TechCrunch 2008-05-01: 'a standalone $500 million Green Growth Fund'. The announced size; a paper Form D "
         "(2008-05-19)."),
    fund("KPCB China Fund, L.P.", 360_000_000, 2007,
         "https://siliconangle.com/2011/11/03/asia-a-favorable-investment-destination-for-kleiner-perkins-and-others/",
         "SiliconANGLE 2011-11-03: 'Kleiner raised $360 million fund in its first round of investment conducted in "
         "year 2007' (decisions.md X1 also cites VentureBeat 2007-04-23). A paper Form D (2007-05-11). Reported by "
         "KPCB China Management, Ltd. (CRD 161470) and on Kleiner Perkins' 7.B.(2). Listed under the provisional "
         "reading of decisions.md X1."),
    fund("Kleiner Perkins Caufield & Byers XII, LLC", 600_000_000, 2006, VB_2006,
         "VentureBeat 2006-02-15: the firm 'has also finished raising its twelfth fund, at $600 million'; TechCrunch "
         "2008-05-01: 'It raised $600 million for its twelfth fund just two years ago'. A paper Form D (2006-03-03)."),
]
put("funds", FUNDS, POST_2026,
    f"{len(FUNDS)} funds and sleeves from 2006 on, newest first: the numbered funds XII to XXII, the Digital Growth "
    "Funds I to III, the Green Growth Fund, the Select Funds I to IV, Flex I, and KPCB China Fund and Fund II (the "
    "last two under the provisional reading of decisions.md X1). Sizes are the firm's own announcements where it "
    "made one (2020 on), press otherwise, each with its source. FILING STYLE: until 2022 the firm filed a fixed "
    "total-offering amount before first close ($0 sold) and rarely amended, and in every such case (XIV to XX, "
    "Select I and II, Digital Growth II and III, China Fund II) the offering equals the announced size to the "
    "dollar, which corroborates the size but cannot be asserted against an amount sold. From 2024 it files at close "
    "with the full amount sold, so exactly five entries carry an accession, asserted against the filing at build "
    "time: XXI, Select Fund III, XXII, Select Fund IV and Flex I. The funds before 2009 (XII, XIII, Green Growth, "
    "China Fund) filed on paper. NOT LISTED: the Founders Funds and Friends funds beside each main fund (KPCB XII to "
    "XIX Founders Fund, Kleiner Perkins XX and XXI Founders Fund, Select Founders Funds I to III, Digital Growth "
    "Founders Funds I to III, XIX to XXII Friends, Select II to IV Friends, KPCB China Founders Fund): side vehicles "
    "for the partners and their circle (XX Friends and Select II Friends both report $37,575,000 sold, a likely "
    "co-issued filing); KP Sightglass I, LLC and KP Sightglass II, LLC, which have no public description and no "
    "Form D (ADV: gross assets $70,038,106 with 3 owners and $10,000,000 with 2 owners, read as bespoke vehicles "
    "for one or two investors, an inference); the KPCB Pandemic and Bio Defense Fund ($200M, 2006, VentureBeat "
    "2006-02-15; no longer on the ADV); the sFund (announced at $250M in 2010 with Facebook, Amazon and Zynga, "
    "TechCrunch 2010-10-21, while KPCB sFund, LLC offered $50M and reported $0 sold) and the iFund ($100M in 2008, "
    "doubled to $200M in 2010, an allocation from the main funds with no vehicle of its own); KPCB I to XI, the "
    "Java Fund, the Zaibatsu funds and KPCB Edge, which predate 2006 or were not researched. Bond's funds are "
    "another firm's (decisions.md D2).")
inv["funds"] = {"funds": FUNDS}        # the table shape investor.json carries; the sidecar keeps the list

# ---------------------------------------------------------------- icon
ICON = f"{REL}/sources/site/kp-mark.svg"
if not str(inv.get("icon_url") or "").startswith("https://"):      # uploaded at ingest: keep the bucket URL
    put("icon_url", ICON, ICON,
        "Source chosen by measurement (COLLECTION.md s11). --discover on https://www.kleinerperkins.com (2026-09-30) "
        "offers: an SVG that is a portfolio company's takeover logo (Analog x Alif), not the firm's; the og:image "
        "kp-logo-social-white.png (1300x729, the mark beside the wordmark); the site icon cropped-Frame-1.png "
        "(512x512, which WordPress enlarged from a 136x136 original, Frame-1.png; its dry run measures a 1.74 px "
        "ramp); a 180x180 apple-touch icon, a 116x116 favicon.png and a 48 px favicon.ico, all too small; and a "
        "favicon.svg and two manifest icons that return 404. The vector wins: the source is the square mark from the "
        "header's own inline <svg> (a.kp-site-logo, viewBox 0 0 208 19; the four paths left of the wordmark, x 0 to "
        "19.2337), saved with a black fill as sources/site/kp-mark.svg. Dry run 2026-09-30 (scratch/icon-dry-run.png, "
        "nothing uploaded): vector, a synthesized #ffffff plate behind the bare glyph, artwork scaled 0.596 into the "
        "keyline (box 60%, radius 80%), contrast 19.7:1, ramp 0.56 px. To be uploaded at ingest with "
        f"`npx tsx scripts/fetch-investor-icon.ts {SLUG} {ICON}`, which replaces this value with the bucket URL.")

# ---------------------------------------------------------------- stage, geo, scope, range (reconciled with the base)
stages = collections.Counter(m.get("entry_stage") or "none recorded" for m in members.values())
recent = collections.Counter(m.get("entry_stage") or "none recorded" for m in members.values()
                             if str(m.get("entry_date") or "")[:4].isdigit() and int(str(m["entry_date"])[:4]) >= 2019)
put("investment_stage", ["Seed", "Series A", "Growth"], f"{SITE}/partnerships/",
    "The firm's own two stages, Early and Growth (the 'first investment stage' of each company in its CMS: Early "
    "341, Growth 73 of the 416 companies on the live list; sources/site/raw/stage.json), crosswalked: Early "
    "straddles Seed and Series A (decisions.md D7), Growth is Growth. The fund architecture agrees: numbered "
    "early-stage funds beside the Select and Flex growth funds; the KP19 post names seeds, Series As and "
    "'high-inflection Series Bs', the 2026 post 'At the early stage ... At growth, we remain selective'. "
    f"Reconciled with the landed entry stages over the {N} verified members: "
    + ", ".join(f"{k} {v}" for k, v in stages.most_common())
    + "; entries dated 2019 or later: " + ", ".join(f"{k} {v}" for k, v in recent.most_common())
    + ". No disagreement: all three stages appear, and the large undetermined share is the era before 2006, where "
    "the record does not give the round.")

EUROPE = {"GB", "DE", "FR", "SE", "DK", "NO", "FI", "NL", "BE", "CH", "AT", "ES", "IT", "IE", "PT", "PL", "CZ", "EE",
          "LT", "LV", "BG", "RO", "HU", "GR", "LU", "IS", "HR", "SI", "SK", "UA", "RS", "CY", "MT"}
countries = collections.Counter(m.get("hq_country") for m in members.values() if m.get("hq_country"))
known = sum(countries.values())
europe = sum(v for k, v in countries.items() if k in EUROPE)
china = countries.get("CN", 0)
china_desk = sum(1 for m in members.values() if "kpcb_china" in (m.get("flags") or []))
recent_c = collections.Counter(m.get("hq_country") for m in members.values()
                               if m.get("hq_country") and str(m.get("entry_date") or "")[:4].isdigit()
                               and int(str(m["entry_date"])[:4]) >= 2019)
GEO_MIN = 0.02                                   # a region is published at 2% of the members with a known country
other = [label for label, n in (("China", china), ("Europe", europe)) if n >= GEO_MIN * known]
put("investment_geo", {"core": ["US"], "other": other}, "companies/classification.json",
    "Derived from the portfolio's headquarters, because the firm's site has no geography filter (its About page "
    f"says only 'bold ideas that span industries and continents'). US {countries.get('US', 0)} of the {known} "
    f"verified members with a known country; China {china}; Europe {europe} ("
    + ", ".join(f"{k} {v}" for k, v in countries.most_common() if k in EUROPE) + "); others: "
    + ", ".join(f"{k} {v}" for k, v in countries.most_common() if k not in EUROPE and k not in ("US", "CN"))
    + f". A region is published at {GEO_MIN:.0%} of those members or more. The China rows are the KPCB China desk "
    f"({china_desk} rows flagged kpcb_china), inside the portfolio only under the provisional reading of "
    "decisions.md X1, and none is recent: entries dated 2019 or later are "
    + ", ".join(f"{k} {v}" for k, v in recent_c.most_common()) + ". If Erik rules KPCB China out, 'China' leaves "
    "this field with the rows.", derived=True, flags=["derived", "china_rests_on_kpcb_china_provisional"])

_spec = importlib.util.spec_from_file_location("build_firm_profile", SCRIPTS / "build-firm-profile.py")
_build = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_build)
cfg = P.config()["profile"]
focus, mapped, unmapped = _build.focus_from_site_tags(base_rows, cfg["focus_crosswalk"], cfg["focus_min_companies"])
tagged = sum(1 for r in base_rows if (r.get("sector") or "").strip())
grind_focus = collections.Counter(m.get("focus") for m in members.values() if m.get("focus"))
SCOPE_NOTE = (
    f"The firm's own sector tags sit on {tagged} of the {len(base_rows)} portfolio rows (the live list only), "
    "crosswalked: " + ", ".join(f"{k} {v}" for k, v in mapped.most_common()) + "; left unmapped on purpose: "
    + ", ".join(f"{k} {v}" for k, v in unmapped.most_common()) + f". Published at {cfg['focus_min_companies']} "
    "companies or more, so Fintech & Payments stays below the line although the firm names fintech in its 2024 "
    "post ('enterprise software, consumer, healthcare, fintech and hardtech'). DISAGREEMENT, flagged and not "
    "overwritten (COLLECTION.md s11): the firm's largest sector, Enterprise, names no single value of the closed "
    "taxonomy, and the site has no Security and no Crypto sector although the portfolio holds security companies "
    "(the Lightspeed signal). The per-company focus over the verified members reads: "
    + ", ".join(f"{k} {v}" for k, v in grind_focus.most_common()) + ". Generalist: no sector carries the portfolio.")
put("investment_scope", {"type": "Generalist", "focus": focus}, "companies/base.json", SCOPE_NOTE)

rounds = sorted((m["entry_offering_usd"], s) for s, m in members.items() if m.get("entry_offering_usd"))
vals = [v for v, _ in rounds]


def pct(p):
    return vals[min(len(vals) - 1, max(0, round(p / 100 * (len(vals) - 1))))]


def rounded(x):
    return int(round(x / 1e6) * 1e6)


median = statistics.median(vals)
by_year = collections.Counter(str(members[s].get("entry_quarter") or "")[:4] for _, s in rounds)
SARONIC = 1_750_000_000
if "saronic-technologies" not in members:
    raise SystemExit("range ceiling: Saronic is not a member in the ledger")
put("investment_range", {"lower_limit": rounded(pct(10)), "median": rounded(median), "upper_limit": SARONIC},
    "companies/resolved.json",
    f"MEDIAN: {musd(median)}, the median entry round over the {len(vals)} verified members whose entry round is "
    f"on a Form D (p10 {musd(pct(10))}, p25 {musd(pct(25))}, p75 {musd(pct(75))}, p90 {musd(pct(90))}), published "
    f"as {musd(rounded(median))}. It is a round size, not a cheque size, fair only for a lead investor with high "
    f"ownership, and the coverage is uneven: electronic Form D starts in 2008-09 and {by_year.get('2009', 0)} of "
    f"the {len(vals)} rounds are from 2009 alone. LOWER: the firm publishes no programme floor (KP Fellows is a "
    "student work programme with no investment; KPCB Edge, the seed programme of 2015 to 2018, is discontinued), so "
    f"the p10 entry round, {musd(pct(10))}, stands in, flagged. The firm states no typical cheque; the one it "
    "names is 'the $25 million check that Kleiner wrote to lead Rippling's A round in 2019 ... to that point the "
    "largest early-stage investment that Kleiner had ever made'. UPPER (press-based): the largest round the firm "
    "led in the last five years, Saronic's $1.75 billion Series D of 2026-03-31 ('The round was led by Kleiner "
    "Perkins and values the company at $9.25 billion', PR Newswire, "
    "https://www.prnewswire.com/news-releases/saronic-closes-1-75b-series-d-at-9-25b-valuation-to-accelerate-a-new-"
    "era-of-maritime-autonomy-302729238.html; the firm's own post: 'We're proud to lead their Series D'). It is the "
    "round, not the firm's cheque, which is undisclosed: at a 10 to 15% single position the largest fund, Select "
    "Fund IV at $1.92B, supports $192M to $288M, and the whole 2026 growth pool of $2.475B supports $248M to "
    "$371M. Other led rounds read: K2 Space $500M (2026), Mind Robotics $400M (2026), Rogo $160M (2026). REJECTED: "
    "aggregator claims of $1M to $3M seed cheques and a $500K to $75M range (vcsheet.com, investormatch.pro), "
    "unconfirmed.",
    flags=["median_round_size_proxy", "lower_p10_proxy", "upper_press_based", "upper_round_size_not_cheque"])

NOTABLE = [("Google", "google"), ("Amazon", "amazon"), ("Twitter", "twitter"), ("Spotify", "spotify"),
           ("Airbnb", "airbnb")]
put("notable_investments", [n for n, _ in NOTABLE], "companies/membership-ledger.json",
    "The five best known of the verified portfolio companies to a general reader, most recognised first "
    "(COLLECTION.md s11, PRO-152), each on the firm's own list with its year: Google (1999, the Series A), Amazon "
    "(1996), Twitter (2010) and Spotify (2011), and Airbnb (2015, a growth round). Next in line, left out by the "
    "cap of five: Uber, Slack, DoorDash, Netscape, Genentech and Figma; the history names most of them.",
    slugs=[s for _, s in NOTABLE])

# ---------------------------------------------------------------- what a reviewer should rule on
src["flags"] = [
    {"field": "aum", "severity": "medium",
     "note": "Both ends are sworn gross asset values of an exempt reporting adviser, not regulatory assets under "
             "management. The top adds KPCB China Management's own two funds and stands only while decisions.md X1 "
             "(KPCB China provisionally inside the firm) stands. One fund, Kleiner Perkins Select Founders Fund III, "
             "has no parsed value in sources/adv/adv-7b-funds.json."},
    {"field": "investment_geo", "severity": "medium",
     "note": "'China' rests on the KPCB China desk (provisional, decisions.md X1) and on no entry since 2019."},
    {"field": "investment_scope.focus", "severity": "medium", "note": SCOPE_NOTE},
    {"field": "investment_range", "severity": "medium",
     "note": "The ceiling is a round size from a press release ($1.75B, Saronic), far above what the funds support "
             "as a single cheque ($192M to $371M at 10 to 15%); the median is a Form D round-size proxy weighted to "
             "2009 to 2016; the lower limit is the p10 of that distribution, not a stated floor."},
    {"field": "funds", "severity": "low",
     "note": "KPCB XIII is published at the $700M of the 2008 announcement; TechCrunch 2012 says its offering was "
             "$950M, and the paper filing cannot settle it. XIV, XVI, Digital Growth Fund II and China Fund II carry "
             "their filed offering, not an announced close. XXII is published at the filed $995M, which the firm "
             "rounds to $1 billion (the history uses the firm's figure)."},
    {"field": "name", "severity": "low",
     "note": "The rebrand from KPCB to Kleiner Perkins dates to 2018 on the archive, 2019 in decisions.md; the "
             "history names no year."},
]

# ---------------------------------------------------------------- checks, then write
if bad := profile_copy.problems(inv, F):
    raise SystemExit("the thesis or history breaks the shape rule: " + "; ".join(bad))
if bad := profile_copy.notable_problems(inv, F, member_names):
    raise SystemExit("; ".join(bad))

ORDER = ["slug", "name", "investor_type", "website", "icon_url", "hq_location", "founding_year", "history",
         "investment_concept", "investment_stage", "investment_geo", "investment_scope", "investment_range",
         "notable_investments", "aum", "funds", "individuals", "updated_at"]
inv = {k: inv[k] for k in ORDER if k in inv} | {k: v for k, v in inv.items() if k not in ORDER}
write_atomic(P.investor, json.dumps(inv, indent=2, ensure_ascii=False) + "\n")
write_atomic(P.investor_sources, json.dumps(src, indent=2, ensure_ascii=False) + "\n")
print("wrote", P.rel(P.investor), "and", P.rel(P.investor_sources))
print("thesis ", inv["investment_concept"])
print("history", f"{len(profile_copy.sentences(HISTORY))} sentences, {profile_copy.words(HISTORY)} words")
print("aum    ", inv["aum"], "| funds", len(FUNDS), "| notables", inv["notable_investments"])
print("stage  ", inv["investment_stage"], "| geo", inv["investment_geo"], "| scope", inv["investment_scope"])
print("range  ", inv["investment_range"])
