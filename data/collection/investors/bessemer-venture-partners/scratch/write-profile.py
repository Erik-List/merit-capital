#!/usr/bin/env python3
"""Assemble Bessemer Venture Partners' researched profile fields into investor/investor.json and
investor/sources.json (COLLECTION.md s11; PRO-80). Re-runnable (the Kleiner Perkins pattern): every value is either a
constant researched in scratch/profile-research.json and re-read in the firm's own pages, or recomputed here from the
files on disk, so a second run after the base is final restates the base-dependent fields (stage counts, geo, scope,
range, the reviewer flags) and leaves what the shared scripts own alone.

What this script writes: name, investor_type, website, founding_year, history, investment_concept, aum, funds,
icon_url (until an upload replaced it), investment_stage, investment_geo, investment_scope, investment_range,
notable_investments, and the sidecar's top-level `flags` (what a reviewer should rule on).
What it never writes: hq_location (scripts/firm-offices.py), individuals and updated_at (scripts/build-firm-profile.py).
It refuses to write when a company named in the history, a notable or the range ceiling is not a member.

After a run, in this order from the repo root:
  python3 scripts/site-portfolio.py bessemer-venture-partners --no-fetch-profiles
  python3 scripts/firm-offices.py bessemer-venture-partners
  python3 scripts/build-firm-profile.py bessemer-venture-partners   (rewrites the scope and individuals bases)
  python3 scripts/profile_copy.py bessemer-venture-partners
Usage: python3 write-profile.py
"""
import collections
import datetime
import importlib.util
import json
import re
import statistics
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parents[4] / "scripts"
sys.path.insert(0, str(SCRIPTS))
from paths import ROOT, Paths, write_atomic  # noqa: E402
import profile_copy  # noqa: E402

SLUG = "bessemer-venture-partners"
P = Paths(SLUG)
REL = f"data/collection/investors/{SLUG}"
SITE = "https://www.bvp.com"
ABOUT = f"{SITE}/about"
WIKI = "https://en.wikipedia.org/wiki/Bessemer_Venture_Partners"
ADV_PDF = "https://reports.adviserinfo.sec.gov/reports/ADV/159279/PDF/159279.pdf"
HISTORY_2008 = "http://www.bvp.com/port/onepage.asp"        # Common Crawl capture of 2008-11-20
POST_2026 = f"{SITE}/news/5-75-billion-to-back-the-founders-building-what-s-next"
POST_INDIA_2 = f"{SITE}/news/350-million-for-our-next-india-fund"
POST_XII = f"{SITE}/news/expanding-opportunities-with-3-85-billion-for-early-stage-investments"
POST_2021 = f"{SITE}/news/backing-entrepreneurs-with-3-3b-in-new-funds"
POST_INDIA = f"{SITE}/news/introducing-our-india-fund"
POST_GROWTH = f"{SITE}/news/bessemer-growth"
POST_X = f"{SITE}/news/bvp-x-our-tenth-fund"
POST_FORGE = f"{SITE}/news/bvp-forge-raises-780-million-inaugural-fund"
POST_FORGE_2 = f"{SITE}/news/bvp-forge-closes-1-billion-forge-ii"
POST_INERTIA = f"{SITE}/news/powering-the-future-the-path-to-commercial-fusion-energy-with-inertia-enterprises"
POST_DRIVENETS = f"{SITE}/news/drivenets-the-ai-networking-fabric-for-heterogeneous-ai"
FINSMES_2015 = "http://www.finsmes.com/2015/02/bessemer-venture-partners-closes-1-6-billion-fund.html"
WEALTH_2011 = ("https://www.wealthbriefing.com/html/article.php/"
               "bessemer-venture-partners-closes-$1.6-billion-fund,-targets-india")
ALTASSETS_2007 = "https://www.altassets.net/private-equity-news/bessemer-venture-partners-vii-closes-on-1bn.html"
VCJ_2009 = "https://www.venturecapitaljournal.com/bessemer-venture-partners-raises-350-million-annex-fund/"

inv = json.loads(P.investor.read_text()) if P.investor.exists() else {"slug": SLUG}
src = json.loads(P.investor_sources.read_text()) if P.investor_sources.exists() else {"slug": SLUG, "fields": {}}
src.setdefault("slug", SLUG)
src["run"] = "PRO-80"
F = src.setdefault("fields", {})


def put(key, value, source, basis, **extra):
    inv[key] = value
    F[key] = {"value": value, "source": source, "basis": basis, **extra}


def usd(x):
    return f"${x:,.0f}"


def musd(x):
    return f"${x / 1e9:.2f}B" if x >= 1e9 else f"${x / 1e6:.1f}M"


def share(n, d):
    return f"{n / d:.1%}" if d else "n/a"


def vehicle(name):
    """A Form ADV fund name (all capitals) as it reads in a sentence."""
    t = name.title().replace("Bvp", "BVP")
    return re.sub(r"(Co-Invest )(\w\w)\b", lambda m: m.group(1) + m.group(2).upper(), t)


# ---------------------------------------------------------------- the landed base (members only, merged view)
def rows_of(obj):
    """classification.json and resolved.json are keyed by company slug, flat or nested under the investor slug."""
    inner = obj.get(SLUG)
    if isinstance(inner, dict) and not ({"entry_stage", "hq_country", "name", "status", "focus"} & set(inner)):
        return inner
    return obj


base_rows = json.loads(P.base_json.read_text())
verdicts = json.loads(P.ledger.read_text())[SLUG]["verdicts"]
resolved = rows_of(json.loads(P.resolved.read_text()))
classification = rows_of(json.loads(P.classification.read_text()))


def merged(slug):
    row = dict(resolved.get(slug) or {})
    row.update(classification.get(slug) or {})        # run.py merge_rows: the overlay key wins
    return row


member_names = {r["slug"]: r["name"] for r in base_rows
                if (verdicts.get(r["slug"]) or {}).get("verdict") == "member"}
members = {s: merged(s) for s in member_names}
N = len(members)
UNJUDGED = sum(1 for r in base_rows if r["slug"] not in verdicts)
if not N:
    raise SystemExit("no member rows in the ledger: nothing to compute the base-dependent fields from")
if UNJUDGED:
    print(f"WARNING: {UNJUDGED} of {len(base_rows)} base rows carry no verdict yet; the base-dependent fields are "
          f"interim and this script must be re-run when the base is final")


def year_of(m):
    y = str(m.get("entry_date") or "")[:4]
    return int(y) if y.isdigit() else None


# ---------------------------------------------------------------- identity
adv = json.loads((P.sources / "adv" / "adv-7b-funds.json").read_text())
CRD = "159279"
adv_funds = adv["advisers"][CRD]["funds_7b1"]
adv_sum = adv["sum_by_adviser"][CRD]
if adv_sum != sum(f["gav"] or 0 for f in adv_funds):
    raise SystemExit("adv-7b-funds.json: sum_by_adviser does not equal the sum of its own fund rows")

put("name", "Bessemer Venture Partners", f"{SITE}/",
    "The firm's own brand on bvp.com (the page title and the header logo's label). The adviser's legal name is Deer "
    "Management Co. LLC, primary business name 'BESSEMER VENTURE PARTNERS' (Form ADV Item 1, CRD 159279, SEC "
    "801-125875, amendment of 2026-05-13). The general partners are the Deer VI to Deer XII & Co. entities; "
    "Bessemer Securities, Bessemer Trust and Lindsay Goldberg & Bessemer are separate businesses (decisions.md D3).")
put("investor_type", "Institutional", ADV_PDF,
    f"A venture capital firm investing through its own funds ({len(adv_funds)} private funds on Schedule D Section "
    "7.B.(1) of its Form ADV, CRD 159279). Outside investors since Bessemer Venture Partners VII (2007); until then "
    "the money came from the Phipps family and Bessemer Securities (Wikipedia, 'Bessemer Venture Partners').")
put("website", SITE, f"{SITE}/", "The firm's own site, read 2026-10-06; bvp.com has been its one domain since the "
    "1990s (config.json wayback).")
put("founding_year", 1981, ABOUT,
    "1981 is the year the firm itself came into being. Its own About page timeline (the Sanity aboutPage document, "
    "read 2026-10-06): '1981: The high-risk, high-growth investment group operating within the family office formally "
    "spins out into an independent venture firm: Bessemer Venture Partners.' COLLECTION.md s11 has every profile "
    "field answer a question about the firm, and the firm on this page is the adviser and fund family of "
    "decisions.md D1; Bessemer Securities, the family office, is a separate business that still exists and is "
    "outside that boundary (D3). The same reading as IVP (1980, not the 1974 of its predecessor) and ICONIQ Growth "
    "(2013, not ICONIQ's 2011). THE OTHER YEAR IS 1911: the timeline starts with 'Henry Phipps establishes a family "
    "office, which he names Bessemer Securities', and the firm has long presented that history as its own: a "
    "partner's biography in a portfolio company's proxy statements calls it 'the nation's oldest venture capital "
    "firm' (infoUSA, DEF 14A of 2001-04-20 and 2002-03-29, in sources/edgar/fts-hits.json), and its 2019 growth "
    "post says 'Since the formation of our fund nearly a century ago'. Wikipedia starts the firm's history in 1911 "
    "too and gives the spin-out no year ('Eventually the venture capital investment operation of Bessemer "
    "Securities was spun out'); the firm's own date is used. The history sentence on the page names both years. "
    "Intermediate dates: Pete Bancroft joined in 1967 'to lead the venture practice' (the firm's 2008 history page) "
    "and the California office "
    "opened in 1976. Flagged for a ruling, with decisions.md X1 (positions from before the spin-out).")

# ---------------------------------------------------------------- reader-facing copy
THESIS = "“Forged in steel. Building what's next.”"
put("investment_concept", THESIS, f"{SITE}/",
    "The hero headline (the page's h1) of the firm's homepage, 'Forged in steel. / Building what's next.', read "
    "2026-10-06 on the live page and in the Sanity homePage document (sources/site/sanity/homePage.json, "
    "hero.headline); set on one line with a straight apostrophe and published in quotation marks as the firm's own "
    "words. Competing lines on the same page: the hero subhead, 'We exist to back audacious founders through "
    "dedicated early and growth practices.', which says more about what the firm does but is not the line it leads "
    "with (the rule takes the homepage headline first); and the meta description, which says the firm is 'Global in "
    "reach and decentralized by design' and 'backs founders in any sector', 'from seed to growth and beyond', 'with "
    "any check size'. The title tag is the firm's name alone.")

HISTORY_BETS = [("Staples", "staples"), ("Ciena", "ciena"), ("VeriSign", "verisign"), ("Skype", "skype"),
                ("LinkedIn", "linkedin"), ("Yelp", "yelp"), ("Shopify", "shopify"), ("Twilio", "twilio"),
                ("Pinterest", "pinterest"), ("Toast", "toast"), ("Anthropic", "anthropic")]
not_members = [n for n, s in HISTORY_BETS if s not in members]
if not_members:
    raise SystemExit(f"history names a company that is not a member in the ledger: {not_members}")
HISTORY = ("Bessemer Venture Partners grew out of Bessemer Securities, the family office Henry Phipps founded in New "
           "York in 1911, and became an independent venture firm in 1981. The bets that made it were Staples, Ciena, "
           "VeriSign and Skype, followed by LinkedIn, Yelp, Shopify, Twilio, Pinterest, Toast and Anthropic. In "
           "September 2026 it raised $5.75 billion, $1.75 billion for early-stage companies and $4 billion for "
           "growth; the track record on this page leaves out its buyout arm, BVP Forge.")
if any(n not in HISTORY for n, _ in HISTORY_BETS):
    raise SystemExit("HISTORY_BETS and the history text disagree")
PRE_SPINOUT = sum(1 for m in members.values() if "pre_spinout" in (m.get("flags") or []))
put("history", HISTORY, ABOUT,
    "Founding: the firm's own About page timeline (read 2026-10-06): '1911: Henry Phipps establishes a family "
    "office, which he names Bessemer Securities in honor of the Bessemer process' and '1981: ... formally spins out "
    "into an independent venture firm: Bessemer Venture Partners'. New York: the firm's 2008 history page "
    f"({HISTORY_2008}, Common Crawl capture of 2008-11-20, sources/site/history-narrative.json), 'Bessemer initially "
    "operated out of offices on Park Avenue, co-located with Bessemer Securities, its primary limited partner', and "
    "Wikipedia. The bets, each a verified portfolio company with the firm's own account of it: Staples ('invested in "
    "each of the company's four rounds, starting in 1986'), Ciena ('David Cowan invested for Bessemer in the B "
    "round'), VeriSign ('David Cowan co-founded the company in 1995 as a spin-out from RSA') and Skype (Rob Stavis "
    "'led the A round'), all four on the 2008 history page; LinkedIn (memo of 2006-12-11, leading the Series C with "
    "$12.5 million), Yelp (memo of 2005-10-03), Shopify (memo of 2010-10-12, the Series A), Twilio (memo of "
    "2009-11-06, a $125,000 seed cheque), Pinterest (memo of 2011-04-03, 'a term sheet to lead a $10m Series A'), "
    "Toast (memo of 2015-12-14, $17.5M of the $24M first institutional round), all at bvp.com/memos/<company>; "
    "Anthropic (posts of 2024-10-22, 'Why we backed Anthropic', and 2025-03-03, '$3.5 billion more for Anthropic'). "
    f"The raise is the firm's post of 2026-09-22 ({POST_2026}): 'we're announcing $5.75 billion in new capital ... "
    "$1.75 billion for seed and early-stage investing and $4 billion for growth, raised in a single close'. The "
    "last clause is the portfolio boundary of decisions.md D2: BVP Forge, which the firm's timeline calls 'a private "
    "equity firm' (2022), buys majority or significant minority stakes and is outside the portfolio on this page. "
    "Moved to this sidecar, not the page: the Carnegie Steel origin (Phipps and Carnegie, 1872; the Bessemer "
    "process); Pete Bancroft leading the venture practice from 1967 and the Silicon Valley office of 1976; fund VII "
    "of 2007 as the first with outside investors (Wikipedia); the offices in Bangalore (2006), Tel Aviv (2007) and "
    "London (2021); the growth practice and the first Century fund (2019); the $1 billion AI commitment of 2023; the "
    "firm's own counts of '$20B' under management, '155+' IPOs and deSPACs and '450+' active portfolio companies "
    "(About page); the anti-portfolio; the fund ladder (funds field). "
    f"{PRE_SPINOUT} portfolio companies on this page date from before the 1981 spin-out and are in under the "
    "provisional reading of decisions.md X1.")

# ---------------------------------------------------------------- aum (one registered adviser: Item 5.F)
RAUM = 20_239_213_324            # Item 5.F.(2)(c), read from data/filings/adv/159279.pdf with pypdf on 2026-10-06
forge_rows = [f for f in adv_funds if re.match(r"(BVP FORGE|GATOR CO-INVEST)\b", f["name"])]
forge_sum = sum(f["gav"] or 0 for f in forge_rows)
if len(forge_rows) != 8 or not forge_sum:
    raise SystemExit(f"adv-7b-funds.json: expected the 3 BVP Forge and 5 Gator Co-Invest vehicles, found "
                     f"{len(forge_rows)}")
newer = [f["name"] for f in adv_funds if re.search(r"\bXIII\b|CENTURY FUND III\b|FORGE II\b", f["name"])]
if newer:
    raise SystemExit(f"adv-7b-funds.json now carries {newer}: a newer Form ADV was parsed, so re-read Item 5.F (RAUM) "
                     f"and rewrite the 'floor' sentences of the aum basis and flag")
put("aum", {"bottom": RAUM, "top": RAUM}, ADV_PDF,
    f"BOTTOM and TOP: {usd(RAUM)}, the regulatory assets under management that Bessemer Venture Partners (Deer "
    "Management Co. LLC, CRD 159279, SEC 801-125875) swears in Item 5.F of its Form ADV, the other-than-annual "
    "amendment of 2026-05-13: all discretionary, across 36 accounts (data/filings/adv/159279.pdf, also "
    "sources/adv/159279.pdf). One registered adviser covers every office and every fund (decisions.md D1: no "
    "relying adviser, no affiliated adviser inside the boundary), so both ends are the one sworn number, the "
    "Battery Ventures and Insight Partners shape. Schedule D Section 7.B.(1) lists "
    f"{len(adv_funds)} private funds with {usd(adv_sum)} of gross assets (sources/adv/adv-7b-funds.json), "
    f"{usd(abs(adv_sum - RAUM))} {'above' if adv_sum > RAUM else 'below'} the Item 5.F figure, so the roster does "
    "not prove the parse to the dollar here. INCLUDES BVP FORGE: "
    f"{usd(forge_sum)} of that gross ({share(forge_sum, adv_sum)}) sits in the buyout strategy, which is outside the "
    "portfolio on this page (decisions.md D2, R5): "
    + "; ".join(f"{vehicle(f['name'])} {usd(f['gav'])}" for f in sorted(forge_rows, key=lambda f: -(f["gav"] or 0)))
    + ". Item 5.F does not split by strategy, so the sworn figure is published whole and the Forge share is flagged. "
    "A FLOOR in two respects: the $5.75 billion the firm announced on 2026-09-22 and BVP Forge II ($1 billion, "
    "closed 2025-11) have no vehicle on this roster. The firm's own figure agrees: 'AUM $20B' in the hero of its "
    f"About page ({ABOUT}, read 2026-10-06). No press figure is used.",
    flags=["single_adviser_5f", "includes_forge_outside_portfolio", "floor_predates_2026_funds"])


# ---------------------------------------------------------------- funds
def fund(name, size, vintage, source, note, accession=None, cik=None):
    entry = {"name": name, "size": size, "vintage": vintage}
    if accession:                       # asserted against TOTALAMOUNTSOLD at build time
        entry["accession"] = accession
    entry["sources"] = [{"source": source, "note": note}]
    if accession:
        entry["sources"].append({
            "source": ("https://www.sec.gov/Archives/edgar/data/"
                       f"{cik}/{accession.replace('-', '')}/{accession}-index.htm"),
            "note": f"Form D {accession}: {usd(size)} sold of {usd(size)} offered."})
    return entry


MAPPING_2026 = ("The post names no fund: the mapping is INFERRED from the Form Ds the firm filed on 2026-09-14 for two "
                "new fund families, Bessemer Venture Partners XIII and Bessemer Venture Partners Century Fund III, and "
                "from the numbered funds being the early-stage line and the Century funds the growth line since 2019. "
                "Those filings state an indefinite offering with $0 sold, so no accession is asserted.")
FUNDS = [
    fund("Bessemer Venture Partners Century Fund III", 4_000_000_000, 2026, POST_2026,
         "Firm post 2026-09-22: '$4 billion for growth, raised in a single close'. " + MAPPING_2026 + " Vehicles: "
         "Century Fund III L.P., Parallel, Institutional, Institutional A, Advisors & Influencers and Associates "
         "(CIKs 2147344, 2147345, 2147346, 2147525, 2147507, 2153766; e.g. Form D 0002147344-26-000001)."),
    fund("Bessemer Venture Partners XIII", 1_750_000_000, 2026, POST_2026,
         "Firm post 2026-09-22: '$1.75 billion for seed and early-stage investing'. " + MAPPING_2026 + " Vehicles: "
         "XIII L.P., Parallel, Institutional, Institutional Feeder, Advisors & Influencers and Associates (CIKs "
         "2147342, 2147343, 2147506, 2147552, 2147526, 2153753; e.g. Form D 0002147342-26-000001)."),
    fund("Bessemer Venture Partners India II", 350_000_000, 2025, POST_INDIA_2,
         "Firm post 2025-03-11: 'our second dedicated India fund with $350 million of capital'. Form D "
         "0001012975-25-000149 (Bessemer Venture Partners India 2 Institutional L.P., 2025-03-04): indefinite "
         "offering, $0 sold, so no accession."),
    fund("Bessemer Venture Partners XII", 3_850_000_000, 2022, POST_XII,
         "Firm post 2022-09-08: 'we've raised $3.85 billion for our twelfth flagship fund, BVP XII'. Form Ds of "
         "2022-06 (XII Institutional 0001932100-22-000001, Institutional Feeder, Advisors & Influencers): indefinite "
         "offering, $0 sold, so no accession."),
    fund("Bessemer Venture Partners XI", 2_475_000_000, 2021, POST_2021,
         "Firm post 2021-02-25: 'we raised $3.3 billion across two new funds'; 'At $2.475 billion, BVP XI will focus "
         "on early-stage companies'. Form D 0001012975-21-000118 (XI Institutional): indefinite offering, $0 sold."),
    fund("Bessemer Venture Partners Century Fund II", 825_000_000, 2021, POST_2021,
         "Firm post 2021-02-25: 'Our $825 million Century II fund is specifically designed for growth-stage "
         "companies'. Form D 0001012975-21-000117 (Century Fund II Institutional): indefinite offering, $0 sold."),
    fund("Bessemer Venture Partners India", 220_000_000, 2021, POST_INDIA,
         "Firm post 2021-11-30: 'the launch of a $220 million dedicated fund'. Form D 0001892914-21-000001 (India "
         "Institutional): indefinite offering, $0 sold."),
    fund("Bessemer Venture Partners Century Fund", 525_000_000, 2019, POST_GROWTH,
         "Firm post 2019-10-08: 'a $525 million dollar fund specifically designed to invest in the companies that "
         "will define the next century'. The post does not name the fund; the vehicles filed on 2019-09-18 are "
         "Bessemer Venture Partners Century Fund L.P. and Century Fund Institutional L.P. (Form Ds "
         "0001012975-19-000610 and -000609, indefinite offering, $0 sold), and the 2021 post calls the successor "
         "'Century II'."),
    fund("Bessemer Venture Partners X", 1_850_000_000, 2018, POST_X,
         "Firm post 2018-10-25: 'a new, $1.85 billion fund: BVP X'. Form D 0001748910-18-000001 (X Institutional): "
         "indefinite offering, $0 sold."),
    fund("Bessemer Venture Partners IX", 1_600_000_000, 2015, FINSMES_2015,
         "FinSMEs 2015-02-19: 'BVP IX', $1.6 billion (read by the profile research of 2026-10-01, "
         "scratch/profile-research.json; the page refused a second read on 2026-10-06), and TechCrunch 2015-02-18 "
         "by its headline. The amended Form D 0001624149-15-000002 (IX Institutional, first sale 2015-02-13) shows "
         "$711,000,000 sold of $711,000,000: one vehicle of the fund, not the full size, so no accession (a sister "
         "amendment, 0001624149-15-000001, carries a typing error, $7.11 billion)."),
    fund("Bessemer Venture Partners VIII", 1_600_000_000, 2011, WEALTH_2011,
         "WealthBriefing 2011-04-01: 'Bessemer Venture Partners has closed its largest fund to date, at some $1.6 "
         "billion', with 'around a quarter of the money set to be invested in India'. The article does not number "
         "the fund; the amended Form Ds of 2011-04 (first sale 2010-12-30) tie it to VIII: VIII Institutional "
         "$885,000,000 sold of $885,000,000 (0001509022-11-000004) and VIII L.P. $615,100,000 sold of $715,000,000 "
         "(0001509022-11-000003), two offerings that sum to $1.6 billion. No single filing shows the full size, so "
         "no accession."),
    fund("Bessemer Venture Partners VII", 1_000_000_000, 2007, ALTASSETS_2007,
         "AltAssets 2007-07-20: headline 'Bessemer Venture Partners VII closes on $1bn'; lead 'has closed its latest "
         "fund, Bessemer Venture Partners VII, on about $1' (the rest is behind a paywall, read 2026-10-06). "
         "Wikipedia: the first fund to take capital from outside investors. Filed on paper: no machine-readable "
         "Form D."),
]
if [f["vintage"] for f in FUNDS] != sorted((f["vintage"] for f in FUNDS), reverse=True):
    raise SystemExit("FUNDS is not newest first")
if any("accession" in f for f in FUNDS):
    raise SystemExit("no Bessemer Form D shows a full published size sold: no fund may carry an accession")
put("funds", FUNDS, POST_2026,
    f"{len(FUNDS)} venture and growth funds from 2007 on, newest first: the numbered early-stage funds VII to XIII, "
    "the three Century growth funds and the two India funds. Each entry is a fund family (its L.P., Institutional, "
    "Parallel, feeder, Associates and Advisors & Influencers vehicles are parts of it, not rows). Sizes are the "
    "firm's own announcements from 2018 on and press before that, each with its source. FILING STYLE: since 2018 "
    "every Bessemer fund files Form D with an indefinite offering and $0 sold and does not amend, so no size can be "
    "asserted against a filing and NO entry carries an accession; the only filings with an amount sold are single "
    "vehicles of VIII ($885,000,000 and $615,100,000) and IX ($711,000,000), which corroborate those funds without "
    "showing the full size. THE 2026 MAPPING IS INFERRED: the firm's post gives '$1.75 billion for seed and "
    "early-stage investing' and '$4 billion for growth' and names no fund; XIII and Century Fund III are the two "
    "fund families it filed for on 2026-09-14. NOT LISTED: BVP Forge ($780 million, 2022, "
    f"{POST_FORGE}) and BVP Forge II ($1 billion, closed 2025-11, {POST_FORGE_2}), the buyout strategy, outside the "
    "portfolio on this page (decisions.md D2), and the five Gator Co-Invest vehicles, which are Forge's (R5); "
    "Bessemer Venture Partners VI (about 2004), whose size is not confirmed by any source read (the $296.9 million "
    "an aggregator gives is the gross asset value of the VI vehicle on the 2026 Form ADV, not a fund size); the 2009 "
    f"annex fund, $350 million by the headline of Venture Capital Journal, 2009-02-26 ({VCJ_2009}; the body is "
    "behind a registration wall), read as BVP VII Special Opportunity Fund L.P. (CIK 1459524) by its date and name "
    "only, an inference, and left out until a source names the vehicle; the single-company and co-investment "
    "vehicles (Cloud All Star Fund, AN I, SG I, VS, PR, Co-Investment L.P.; decisions.md D7); funds I to V and the "
    "Bessec Ventures vehicles, family money from before 2004, not researched.")
inv["funds"] = {"funds": FUNDS}        # the table shape investor.json carries; the sidecar keeps the list

# ---------------------------------------------------------------- icon
ICON = f"{REL}/sources/site/bvp-mark.svg"
ICON_UPLOAD = f"npx tsx scripts/fetch-investor-icon.ts {SLUG} {ICON}"
ICON_BASIS = (
    "Source chosen by measurement (COLLECTION.md s11). --discover on https://www.bvp.com (2026-10-06) offers three "
    "declared assets and none is the mark: the og:image (a 1200x630 png on cdn.sanity.io, which passes the size "
    "check but is a social share card, not a logo); favicon.ico with 16, 32 and 48 px members, too small (it would "
    "be enlarged); and an og:image:alt value that is not a file (404). It also reports 11 inline svg logo elements. "
    "The vector wins: the source is the mark from the header's own inline svg (a[aria-label='Bessemer Venture "
    "Partners home'] > svg, viewBox 0 0 28 40, two paths, the angular B left of the wordmark; the wordmark is a "
    "second svg, viewBox 42 0 167 40, and is left out because a mark exists). Saved as sources/site/bvp-mark.svg "
    "with both paths as served and the fill set to the site's own foreground colour on its light surface (#11172d, "
    "the stylesheet's color-foreground; the page draws it with currentColor). One element, not two: nothing is "
    "composed. Dry run 2026-10-06 (scratch/icon-dry-run.png, NOTHING UPLOADED OR PUBLISHED): svg 28x40, vector, "
    "rendered at 2x and exempt from the enlargement rule; a synthesized #ffffff plate behind the bare glyph (the "
    "source was 86% transparent); artwork scaled 0.657 into the keyline (box 100% to 66%, radius 122% to 80%); "
    "master 256x256, opaque plate, contrast 13.0:1, ramp 0.82 px, artwork 168 px. To be uploaded at ingest with "
    f"`{ICON_UPLOAD}`, which replaces this value with the bucket URL and writes the provenance.")
if not str(inv.get("icon_url") or "").startswith("https://"):      # uploaded at ingest: keep the bucket URL
    put("icon_url", ICON, ICON, ICON_BASIS)

# ---------------------------------------------------------------- stage, geo, scope, range (reconciled with the base)
stages = collections.Counter(m.get("entry_stage") or "none recorded" for m in members.values())
recent = collections.Counter(m.get("entry_stage") or "none recorded" for m in members.values()
                             if (year_of(m) or 0) >= 2019)
STAGE = ["Seed", "Series A", "Growth"]
EARLY = ("Pre-Seed", "Seed", "Series A")
known_stage = sum(v for k, v in stages.items() if k not in ("undetermined", "none recorded"))
early_n = sum(stages.get(k, 0) for k in EARLY)
absent = [s for s in STAGE if not stages.get(s)]
STAGE_GAP = ((f"DISAGREEMENT, flagged and not overwritten: no entry at {', '.join(absent)} is recorded. " if absent
              else "All three stages appear. ")
             + f"Of the {known_stage} entries whose round the record gives, {early_n} ({share(early_n, known_stage)}) "
             "are early (Pre-Seed, Seed or Series A) and the rest Growth, against the firm's own 'Roughly 70 percent "
             "of our investments are made at the early stage' (post of 2026-09-22). The two are not the same measure: "
             "the share here counts companies by the round the firm entered and reads every secondary, tender and "
             "later round as Growth.")
put("investment_stage", STAGE, f"{SITE}/",
    "The firm's own two practices, crosswalked. Homepage (read 2026-10-06): 'We exist to back audacious founders "
    "through dedicated early and growth practices' and 'With two dedicated practices, seed/early and growth'; the "
    "meta description says 'from seed to growth and beyond'. Seed is Seed, early is Series A (the firm's "
    "early-stage funds lead first institutional rounds), growth is Growth. The fund architecture agrees: numbered "
    "early-stage funds beside the Century growth funds since 2019, and in 2026 '$1.75 billion for seed and "
    "early-stage investing and $4 billion for growth'. The site's own per-company stage field is not used: it reads "
    "'seed' on 500 of 534 companies, a default of the site's migration (decisions.md D9). "
    f"Reconciled with the landed entry stages over the {N} verified members: "
    + ", ".join(f"{k} {v}" for k, v in stages.most_common())
    + "; entries dated 2019 or later: " + ", ".join(f"{k} {v}" for k, v in recent.most_common()) + ". " + STAGE_GAP
    + " The undetermined share is mostly the era before the record names rounds.")

REGIONS = {      # label -> ISO codes; a label publishes at GEO_MIN of the members with a known country
    "India": {"IN"}, "Israel": {"IL"}, "Canada": {"CA"}, "China": {"CN", "HK"},
    "Europe": {"GB", "DE", "FR", "SE", "DK", "NO", "FI", "NL", "BE", "CH", "AT", "ES", "IT", "IE", "PT", "PL", "CZ",
               "EE", "LT", "LV", "BG", "RO", "HU", "GR", "LU", "IS", "HR", "SI", "SK", "UA", "RS", "CY", "MT"},
    "Latin America": {"BR", "AR", "MX", "CL", "CO", "PE", "UY"},
    "Southeast Asia": {"SG", "ID", "VN", "TH", "MY", "PH"},
    "Oceania": {"AU", "NZ"},
}
countries = collections.Counter(m.get("hq_country") for m in members.values() if m.get("hq_country"))
known = sum(countries.values())
region_n = {label: sum(countries.get(c, 0) for c in codes) for label, codes in REGIONS.items()}
recent_c = collections.Counter(m.get("hq_country") for m in members.values()
                               if m.get("hq_country") and (year_of(m) or 0) >= 2019)
GEO_MIN = 0.02
other = [label for label, n in sorted(region_n.items(), key=lambda kv: -kv[1]) if n >= GEO_MIN * known]
us = countries.get("US", 0)
if us < 0.5 * known:
    raise SystemExit(f"geo: the US holds {us} of {known} members with a known country; 'core US' no longer follows")
site_rows = json.loads((P.site / "company-list.json").read_text())
site_rows = site_rows["rows"] if isinstance(site_rows, dict) else site_rows
site_regions = collections.Counter(r for row in site_rows for r in (row.get("regions") or []))
FIRM_REGIONS = {"India", "Israel", "Europe"}                 # the firm's own filter, beside 'us'
extra_geo = [g for g in other if g not in FIRM_REGIONS]
missing_geo = [g for g in sorted(FIRM_REGIONS) if g not in other]
put("investment_geo", {"core": ["US"], "other": other}, "companies/classification.json",
    "Derived from the portfolio's headquarters and reconciled with the firm's own words. The firm's About page says "
    "'We invest wherever great companies are being built' and lists offices in Silicon Valley, San Francisco, "
    "Boston, New York, Westchester, Bangalore, Tel Aviv and London; its portfolio filter has four regions, on the "
    f"{len(site_rows)} listed companies: " + ", ".join(f"{k} {v}" for k, v in site_regions.most_common())
    + f" (the region is the Bessemer team's, so its Canadian companies read 'us'). Headquarters: US {us} of the "
    f"{known} verified members with a known country ({share(us, known)}); "
    + "; ".join(f"{label} {n} ({share(n, known)})" for label, n in sorted(region_n.items(), key=lambda kv: -kv[1]) if n)
    + "; Europe by country: " + ", ".join(f"{k} {v}" for k, v in countries.most_common() if k in REGIONS["Europe"])
    + f". A region is published at {GEO_MIN:.0%} of those members or more, most companies first. Core is the US "
    "alone: the core carries at most two labels (COLLECTION.md s1) and India and Israel, each with its own office "
    "and a like share, have an equal claim to the second, so neither is promoted. Entries dated 2019 or later: "
    + ", ".join(f"{k} {v}" for k, v in recent_c.most_common(8)) + "."
    + (f" Published on the 2% rule although not a region of the firm's own filter: {', '.join(extra_geo)}."
       if extra_geo else "")
    + (f" DISAGREEMENT, flagged: the firm's filter carries {', '.join(missing_geo)}, which stays under the 2% line "
       "here." if missing_geo else ""),
    derived=True, flags=["derived"])

_spec = importlib.util.spec_from_file_location("build_firm_profile", SCRIPTS / "build-firm-profile.py")
_build = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_build)
config = P.config()
cfg = config["profile"]
if not cfg.get("focus_crosswalk"):
    raise SystemExit("config.json profile.focus_crosswalk is empty: fill it before the profile is written")
focus, mapped, unmapped = _build.focus_from_site_tags(base_rows, cfg["focus_crosswalk"], cfg["focus_min_companies"])
if not focus:
    raise SystemExit("the focus recompute publishes nothing: check profile.focus_crosswalk and focus_min_companies")
tagged = sum(1 for r in base_rows if (r.get("sector") or "").strip())
raw_tags = collections.Counter(t.strip() for r in base_rows for t in (r.get("sector") or "").split(",") if t.strip())
grind_focus = collections.Counter(m.get("focus") for m in members.values() if m.get("focus"))
below_line = [f"{k} {v}" for k, v in mapped.most_common() if v < cfg["focus_min_companies"]]
unseen = [f"{k} {v}" for k, v in grind_focus.most_common() if k not in mapped]
SCOPE_NOTE = (
    f"The firm's own sector tags sit on {tagged} of the {len(base_rows)} portfolio rows (the live list only; a "
    "company can carry several): " + ", ".join(f"{k} {v}" for k, v in raw_tags.most_common())
    + ". Crosswalked (config.json profile.focus_crosswalk): " + ", ".join(f"{k} {v}" for k, v in mapped.most_common())
    + (("; left unmapped: " + ", ".join(f"{k} {v}" for k, v in unmapped.most_common())) if unmapped else "")
    + f". Published at {cfg['focus_min_companies']} companies or more"
    + ((", so these stay below the line: " + ", ".join(below_line)) if below_line else "")
    + ". DISAGREEMENT, flagged and not overwritten (COLLECTION.md s11): 'AI' is a tag the firm puts across its "
    "whole list ('AI is reshaping every one of them', homepage), so it leads here while the per-company focus puts "
    "far fewer companies in AI; 'Vertical' and 'Enterprise', the firm's two software practices, both land in SaaS; "
    "and the firm's vocabulary has no sector for "
    + (", ".join(unseen) if unseen else "none of the portfolio's sectors")
    + " (per-company counts), the Lightspeed signal. The per-company focus over the verified members reads: "
    + ", ".join(f"{k} {v}" for k, v in grind_focus.most_common())
    + ". Generalist: the firm says it 'backs founders in any sector' (meta description) and no sector carries the "
    "portfolio.")
put("investment_scope", {"type": "Generalist", "focus": focus}, "companies/base.json", SCOPE_NOTE)

rounds = sorted((m["entry_offering_usd"], s) for s, m in members.items() if m.get("entry_offering_usd"))
vals = [v for v, _ in rounds]
if len(vals) < 30:
    raise SystemExit(f"range: only {len(vals)} members carry a Form D entry round; the median needs another source")


def pct(p):
    return vals[min(len(vals) - 1, max(0, round(p / 100 * (len(vals) - 1))))]


def rounded(x):
    return int(round(x / 1e6) * 1e6)


median = statistics.median(vals)
by_year = collections.Counter(str(members[s].get("entry_quarter") or "")[:4] for _, s in rounds)
LOWER = 1_000_000
CEILINGS = [      # the largest rounds the firm led in the last five years, largest first; the first member row wins
    ("inertia", "Inertia Enterprises", 450_000_000, "Series A", "2026-02-11", POST_INERTIA,
     "Bessemer Venture Partners leads Inertia Enterprises $450M Series A to bring proven fusion science to the grid."),
    ("drivenets", "DriveNets", 410_000_000, "Series D", "2026-06-01", POST_DRIVENETS,
     "Bessemer Venture Partners leads DriveNets' $410M Series D to deliver large-scale AI infrastructure solutions."),
]
ceiling = next((c for c in CEILINGS if c[0] in members), None)
if ceiling is None:
    raise SystemExit("range ceiling: neither Inertia nor DriveNets is a member in the ledger")
c_slug, c_name, UPPER, c_round, c_date, c_url, c_quote = ceiling
skipped = [c[1] for c in CEILINGS if c[0] not in members and CEILINGS.index(c) < CEILINGS.index(ceiling)]
five_years_ago = str(datetime.date.today().year - 5)
led = sorted(((fr["amount_usd"], member_names[s], fr.get("round") or "round", str(fr.get("date"))[:7])
              for s, m in members.items() for fr in (m.get("funding_rounds") or [])
              if fr.get("amount_usd") and str(fr.get("date") or "")[:4] >= five_years_ago
              and re.fullmatch(r"Bessemer( Venture Partners)?", str(fr.get("lead") or "").strip())
              and s != c_slug), reverse=True)[:5]
LARGEST_FUND = max(FUNDS, key=lambda f: f["size"])
lo_pos, hi_pos = 0.10 * LARGEST_FUND["size"], 0.15 * LARGEST_FUND["size"]
put("investment_range", {"lower_limit": LOWER, "median": rounded(median), "upper_limit": UPPER},
    "companies/resolved.json",
    f"MEDIAN: {musd(median)}, the median entry round over the {len(vals)} verified members whose entry round is on "
    f"a Form D (p10 {musd(pct(10))}, p25 {musd(pct(25))}, p75 {musd(pct(75))}, p90 {musd(pct(90))}), published as "
    f"{musd(rounded(median))}. It is a round size, not a cheque size, fair only for a lead investor with high "
    f"ownership; electronic Form D starts in 2009 ({by_year.get('2009', 0)} of the rounds are from that year) and "
    "many recent companies file none. LOWER: $1,000,000, the firm's own words. Growth post of 2019-10-08 "
    f"({POST_GROWTH}): 'Each of our partners now has the decision-making autonomy to support founders with their "
    "first $1 million or their last $250 million check'; the fund X post of 2018-10-25 has 'their first $1 million "
    "(or $50,000) as well as support growth-stage companies with a $100 million check'. A firm statement is taken "
    "as the floor as on Insight Partners and Menlo Ventures (COLLECTION.md s11: programme floors give the lower "
    "limit; the firm runs no seed programme with a published cheque size). Smaller cheques are on the record and "
    "are not the published floor: the '(or $50,000)' of 2018, and the $125,000 seed cheque into Twilio (memo of "
    f"2009-11-06). The p10 entry round, {musd(pct(10))}, is the proxy it replaces. UPPER: {usd(UPPER)}, the largest "
    f"round the firm led in the last five years, the {c_round} of {c_name} ('{c_quote}', the firm's post of {c_date}, "
    f"{c_url}; a verified portfolio company)."
    + (f" Passed over because not a portfolio company on this page: {', '.join(skipped)}." if skipped else "")
    + " It is the round, not the firm's cheque, which is undisclosed (the post calls the investment "
    "'milestone-based'): at a 10 to 15% single position the largest fund, "
    f"{LARGEST_FUND['name'].replace('Bessemer Venture Partners ', '')} at {musd(LARGEST_FUND['size'])}, supports "
    f"{musd(lo_pos)} to {musd(hi_pos)}, so the figure is "
    + ("inside" if lo_pos <= UPPER <= hi_pos else "below" if UPPER < lo_pos else "above")
    + " what the funds support. The firm's own ceiling in words is older and lower: 'their last $250 million check' "
    "(2019). Other rounds it led alone, from the portfolio's round records: "
    + ("; ".join(f"{n} {musd(a)} ({r}, {d})" for a, n, r, d in led) or "none recorded")
    + ". Not used, because the firm did not lead alone: EliseAI $350M (co-led), Waymo $16B (joined), Anthropic $3.5B "
    "(took part). REJECTED: 'with any check size' (meta description), a slogan with no figure.",
    flags=["median_round_size_proxy", "lower_firm_stated", "upper_round_size_not_cheque"])

NOTABLE = [("LinkedIn", "linkedin"), ("Pinterest", "pinterest"), ("Shopify", "shopify"), ("Skype", "skype"),
           ("Twitch", "twitch")]
NEXT_NOTABLE = [("Anthropic", "anthropic"), ("Canva", "canva"), ("Yelp", "yelp"), ("Staples", "staples"),
                ("Waymo", "waymo"), ("Wix", "wix"), ("DocuSign", "docusign"), ("Twilio", "twilio"),
                ("Toast", "toast")]
put("notable_investments", [n for n, _ in NOTABLE], "companies/membership-ledger.json",
    "The five best known of the verified portfolio companies to a general reader, most recognised first "
    "(COLLECTION.md s11, PRO-152), each with the firm's own account of its entry: LinkedIn (memo of 2006, leading "
    "the Series C), Pinterest (memo of 2011, leading the $10M Series A), Shopify (memo of 2010, the Series A), Skype "
    "(the A round, the firm's 2008 history page) and Twitch (memo of 2012, leading the Series B). Fame is the "
    "model's judgement, the one licensed use of it. Next in line, left out by the cap of five: "
    + ", ".join(n for n, s in NEXT_NOTABLE if s in members) + "; the history names several of them.",
    slugs=[s for _, s in NOTABLE])

# ---------------------------------------------------------------- the team as the shared scripts will publish it
_spec = importlib.util.spec_from_file_location("site_portfolio", SCRIPTS / "site-portfolio.py")
_site = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_site)
api = config["site_api"]
team_rows = []
for source in api.get("team_sources") or []:
    if source.get("parser") == "file_list":
        data = json.loads((ROOT / source["path"]).read_text())
        team_rows += data["rows"] if isinstance(data, dict) else data
published = [(r, _site.bucket_of(r, api)) for r in team_rows]
published = [(r, b) for r, b in published if b]
by_bucket = collections.Counter(b[0] for _, b in published)


_OVR = api.get("team_social_overrides") or {}       # search-verified links, by name (COLLECTION.md s11)


def linked(rows):
    return sum(1 for r in rows if r.get("linkedin_url") or r.get("x_url")
               or any((_OVR.get(r.get("name")) or {}).values()))


investors = [r for r in team_rows if r.get("role") == "investor" and not r.get("is_alumni")]
pub_rows = [r for r, _ in published]
SOCIALS_FLOOR = 0.80
gap = cfg.get("socials_gap")

# ---------------------------------------------------------------- what a reviewer should rule on
ever_public = sum(1 for m in members.values()
                  if m.get("public_since") or m.get("is_public") or m.get("status") == "public")
flags = [
    {"field": "founding_year", "severity": "medium",
     "note": "Published 1981, the year the venture group left Bessemer Securities and became Bessemer Venture "
             "Partners (the firm's own timeline). The firm also claims 1911, the year the family office was set up, "
             "and Wikipedia starts the firm's history there. The history names both years. Rule which year the page "
             f"should carry; it is the same seam as decisions.md X1 ({PRE_SPINOUT} companies from before 1981 are in "
             "provisionally)."},
    {"field": "aum", "severity": "medium",
     "note": f"Both ends are the one sworn figure, {usd(RAUM)} (Item 5.F, 2026-05-13). It includes {usd(forge_sum)} "
             f"of gross assets ({share(forge_sum, adv_sum)} of the 7.B roster) in BVP Forge and its Gator Co-Invest "
             "vehicles, the buyout strategy that is outside the portfolio on this page; without them the venture "
             f"and growth funds hold about {musd(adv_sum - forge_sum)} gross. Item 5.F cannot be split, so rule "
             "whether the whole figure stands. It is also a floor: the $5.75 billion of September 2026 and Forge II "
             f"are not in it. The 7.B roster sums to {usd(adv_sum)}, {usd(abs(adv_sum - RAUM))} off Item 5.F."},
    {"field": "funds", "severity": "medium",
     "note": "The 2026 mapping is inferred: the firm's post gives $1.75 billion for seed and early stage and $4 "
             "billion for growth and names no fund; XIII and Century Fund III are the fund families it filed for on "
             "2026-09-14. No fund carries an accession (Bessemer files indefinite offerings with $0 sold). Left "
             "out: fund VI (size not confirmed), the 2009 annex fund ($350 million by a headline; that it is BVP "
             "VII Special Opportunity Fund is inferred), BVP Forge and Forge II (outside the portfolio). IX rests "
             "on FinSMEs as the research read it; the page refused a second read."},
    {"field": "investment_range", "severity": "medium",
     "note": f"The ceiling, {usd(UPPER)}, is the size of a round the firm led ({c_name}, {c_round}), not a cheque; "
             f"the largest fund supports {musd(lo_pos)} to {musd(hi_pos)} at 10 to 15%, and the firm's own words "
             "stop at a '$250 million check' (2019). The lower limit, $1 million, is the firm's stated first "
             "cheque; its 2018 post adds '(or $50,000)' and its Twilio memo records a $125,000 seed cheque, so rule "
             f"whether the smallest stated figure should stand instead. The median, {musd(rounded(median))}, is a "
             f"Form D round-size proxy over {len(vals)} of {N} companies."},
    {"field": "investment_scope.focus", "severity": "medium", "note": SCOPE_NOTE},
    {"field": "investment_stage", "severity": "low", "note": STAGE_GAP},
    {"field": "investment_geo", "severity": "low",
     "note": "Core is the US alone under the two-label cap; India and Israel have an equal claim to a second core "
             "label."
             + (f" {', '.join(extra_geo)} is published on the 2% rule and is not a region of the firm's own filter."
                if extra_geo else "")
             + (f" The firm's filter carries {', '.join(missing_geo)}, under the 2% line here." if missing_geo
                else "")},
    {"field": "notable_investments", "severity": "low",
     "note": "Fame is a judgement: LinkedIn, Pinterest, Shopify, Skype and Twitch are published; Anthropic, Canva, "
             "Yelp and Staples are the nearest alternatives. Skype shut down in 2025."},
    {"field": "history", "severity": "low",
     "note": "The firm counts '155+' IPOs and deSPACs and '450+' active portfolio companies (About page); the "
             f"portfolio on this page records a public listing for {ever_public} of its {N} companies. The gap is "
             "not explained here; listing data is thinner for the older companies (decisions.md D8). Neither count "
             "is on the page."},
]
others = {b: n for b, n in by_bucket.items() if b != "investing"}
if others:
    PLAIN = {"advisor": "operating advisors", "operations": "firm staff (assistants, accounting, legal, marketing)"}
    flags.insert(0, {
        "field": "individuals", "severity": "high",
        "note": f"As config.json stands, {len(pub_rows)} people publish: {by_bucket.get('investing', 0)} investors, "
                + " and ".join(f"{n} {PLAIN.get(b, b)}" for b, n in sorted(others.items(), key=lambda kv: kv[1]))
                + f". The profile should carry the {len(investors)} investors only (role investor, not alumni). "
                "The fix is outside the profile block and was not made by this script: remove the operatingAdvisor "
                "and firmInfrastructure keys from site_api.team_buckets (an unmapped group does not publish, "
                "COLLECTION.md s11), then re-run site-portfolio.py --no-fetch-profiles and build-firm-profile.py."})
cover_rows = pub_rows or investors
if cover_rows and linked(cover_rows) < SOCIALS_FLOOR * len(cover_rows):
    flags.append({
        "field": "individuals.socials", "severity": "medium" if gap else "high",
        "note": f"{linked(cover_rows)} of the {len(cover_rows)} published people carry a LinkedIn or X link "
                f"({share(linked(cover_rows), len(cover_rows))}), under the 80% floor; investors alone: "
                f"{linked(investors)} of {len(investors)} ({share(linked(investors), len(investors))}). The links are "
                "the CMS's own, cleaned to the profile address by site-portfolio.py (a query string is cut). "
                + (f"Recorded exception, config.json profile.socials_gap (checked {gap.get('checked')}): "
                   f"{gap.get('cause')}" if gap else "No exception is recorded in config.json profile.socials_gap.")})
if P.offices.exists() and inv.get("hq_location"):       # both written by firm-offices.py on an earlier pass
    record = json.loads(P.offices.read_text())
    office = record.get("adv") or {}
    site_places = [o["place"] for o in (record.get("site") or {}).get("offices", [])]
    if office.get("principal"):
        principal = office["principal"]["place"]
        flags.append({
            "field": "hq_location", "severity": "medium",
            "note": f"The shared rule publishes {inv['hq_location']}. The Form ADV principal office is {principal}"
                    + (", and the firm's contact page lists that office among its own, so the site agrees"
                       if principal in site_places else ", which the firm's site does not list")
                    + ". No override is set: an override is for a flaw in the reading, never a preference, and "
                    "the reading has none. What a reviewer may still rule on: the same filing counts advisory "
                    "staff at the other offices ("
                    + ", ".join(f"{o['place']} {o['advisory_staff']}" for o in office.get("others", [])
                                if o.get("advisory_staff"))
                    + f"; {sum(o.get('advisory_staff') or 0 for o in office.get('others', []))} in all, against 83 "
                    "firm-wide in Item 5.B.(1), so some are counted at two offices) and gives no count for the "
                    "principal office; Wikipedia calls the firm 'headquartered in San Francisco'; and the site "
                    "lists Silicon Valley first and labels no headquarters. A recorded site statement (config.json "
                    "profile.site_office) needs the firm's own words, and none were found."})
if UNJUDGED:
    flags.insert(0, {"field": "base", "severity": "high",
                     "note": f"{UNJUDGED} of {len(base_rows)} rows carried no verdict when this profile was "
                             "written; stage, geo, scope and range are interim."})
src["flags"] = flags

# ---------------------------------------------------------------- checks, then write
if bad := profile_copy.problems(inv, F):
    raise SystemExit("the thesis or history breaks the shape rule: " + "; ".join(bad))
if bad := profile_copy.notable_problems(inv, F, member_names):
    raise SystemExit("; ".join(bad))
if "@@" in json.dumps(F):
    raise SystemExit("a placeholder is left in a basis")

ORDER = ["slug", "name", "investor_type", "website", "icon_url", "hq_location", "founding_year", "history",
         "investment_concept", "investment_stage", "investment_geo", "investment_scope", "investment_range",
         "notable_investments", "aum", "funds", "individuals", "updated_at"]
inv = {k: inv[k] for k in ORDER if k in inv} | {k: v for k, v in inv.items() if k not in ORDER}
write_atomic(P.investor, json.dumps(inv, indent=2, ensure_ascii=False) + "\n")
write_atomic(P.investor_sources, json.dumps(src, indent=2, ensure_ascii=False) + "\n")
print("wrote", P.rel(P.investor), "and", P.rel(P.investor_sources))
print("members", N, "of", len(base_rows), "rows;", UNJUDGED, "unjudged")
print("thesis ", inv["investment_concept"])
print("history", f"{len(profile_copy.sentences(HISTORY))} sentences, {profile_copy.words(HISTORY)} words")
print("aum    ", inv["aum"], "| funds", len(FUNDS), "| notables", inv["notable_investments"])
print("stage  ", inv["investment_stage"], "| geo", inv["investment_geo"], "| scope", inv["investment_scope"])
print("range  ", inv["investment_range"])
print("team   ", f"{len(pub_rows)} would publish ({dict(by_bucket)}); investors {len(investors)}, "
      f"{linked(investors)} with a link ({share(linked(investors), len(investors))})")
print("flags  ", [f"{f['field']}:{f['severity']}" for f in flags])
