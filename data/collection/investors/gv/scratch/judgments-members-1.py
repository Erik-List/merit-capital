"""PRO-75 membership pass 1: the 95 rows the base carries on a partner's Form D name alone (tier C) plus the two
EDGAR-only rows, judged cluster-first (COLLECTION.md s3): one ruling per person, then every row that person
explains. Evidence: the roster windows (sources/wayback/partner-roster.json, the firm's own people pages by year),
the related persons and their filed addresses on each Form D (scratch/formd-addr.json), the firm's lists.

Rulings used: T4 (a seat is dated against the person's firm at filing time), the director-of-record pattern and
Erik's narrowing (the identity must resolve), the Sutter Hill address reading (a partner filing from the firm's own
office is the firm's seat; Ben Robbins filed from 1600 Amphitheatre Parkway and from 355 Main Street, Cambridge,
Google's Kendall Square building), and decisions.md D11 (sale consideration).
Legal-name twins of listed companies are members and fold into the listed row at the one scheduled rebuild
(companies/identity-merges.json)."""
import importlib.util
import json
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
verdict = jl.verdict
base = {r["slug"]: r for r in json.loads((jl.INV / "companies/base.json").read_text())}


def fd(slug):
    """The first Form D index link on the row (the filing that carries the name-match)."""
    return ((base[slug].get("formd_links") or "").split(";")[0] or "").strip() or None


L = []


def out(slug, basis, conf="high", ec="formd_adjudicated"):
    if slug not in base:
        return
    L.append(verdict(slug, "not_member", basis, ec=ec, conf=conf, cite=fd(slug)))


def twin(slug, canonical, basis):
    if slug not in base:          # already folded by the pre-prepare rebuild
        return
    L.append(verdict(slug, "member", f"Legal-name twin of the listed {canonical}: {basis} Folds into {canonical} at the "
                                     "scheduled rebuild (identity-merges.json).", ec="formd_adjudicated", conf="high",
                     cite=fd(slug)))


# ---- legal-name twins of companies on the firm's own lists
twin("1life-healthcare-inc", "one-medical", "1Life Healthcare, Inc. is One Medical's legal name; Krishna Yeshwant, "
     "who led GV's investment, is a director on its Form Ds (2013-18).")
twin("fog-pharmaceuticals-inc", "parabilis-medicines", "Fog Pharmaceuticals, Inc. is FogPharma (now Parabilis "
     "Medicines); Krishna Yeshwant is a director on its 2021-22 Form Ds.")
twin("neutron-holdings-inc", "lime", "Neutron Holdings, Inc. is Lime's legal name; Joe Kraus and Blake Byers sit on "
     "its 2018-20 Form Ds.")
twin("pencil-pixel-inc", "modsy", "Pencil & Pixel, Inc. is Modsy's legal name; Shanna Tellerman, its founder and a "
     "former GV partner, is on the Form Ds.")
twin("altana-technologies-inc", "altana-ai", "Altana Technologies, Inc. is Altana AI; Karim Faris is a director "
     "(2021-24).")
twin("groupay-inc", "gocardless", "Groupay, Inc. is GoCardless's US issuer; Tom Hulme, who leads GV's position, is a "
     "director (2020-22).")
twin("udisense-inc", "nanit", "UdiSense Inc. is Nanit's legal name; Frederique Dame is a director (2021).")
twin("rosa-foods-inc", "soylent", "Rosa Foods, Inc. is Soylent's legal name; its 2017 Form D names Robert Rhinehart "
     "as executive officer and Andrew Wheeler (GV), Chris Dixon and David Friedberg as directors.")
twin("denver-technologies-inc", "warp", "Denver Technologies, Inc. is Warp's legal name; its 2020 Form D names Zachary "
     "Lloyd, Warp's founder, as executive officer and Erik Nordlander as director.")
twin("noho-dental-inc", "tend", "NoHo Dental, Inc. is Tend's legal name; its 2020-21 Form Ds name Larson Hudson, "
     "Tend's founder, as executive officer and John Lyman (GV partner 2017-22) as director.")
twin("asset-blue-pharmacy-services-inc", "waltz-health", "Asset Blue Pharmacy Services, Inc. is Waltz Health's legal "
     "entity: its 2022 Form D names Mark Thierer, Waltz Health's CEO, as executive officer and Benjamin Robbins as "
     "director, filing from Google's Cambridge office (355 Main Street); Ben Robbins's own GV bio lists Waltz Health.")
twin("dianthus-therapeutics-inc-de", "magenta-therapeutics", "the GV vehicles' filings under the Dianthus name are on "
     "Magenta Therapeutics' own CIK (1690585), renamed after its 2023 reverse merger with Dianthus.")

# ---- the one unlisted seat the firm's own address corroborates
L.append(verdict("synapse-health-inc", "member",
                 "Director-of-record with the firm's address: Benjamin Robbins, a GV general partner since 2014 (the "
                 "firm's own people pages, and in tenure in 2023), is a director on Synapse Health's two 2023 Form Ds, "
                 "the second filed from 1600 Amphitheatre Parkway, Mountain View (the GV vehicles' own address). The "
                 "issuer resolves (Synapse Health, Evanston, a durable-medical-equipment ordering platform; the $15M "
                 "and $25M rounds of 2023). Not on the firm's lists; kept at medium and flagged for the A/B pass.",
                 ec="formd_adjudicated", conf="medium", cite=fd("synapse-health-inc")))

# ---- sale consideration (decisions.md D11)
L.append(verdict("starco-brands-inc", "not_member",
                 "Sale consideration: the GV vehicles' Starco Brands filings (Forms 3/4 and 13D/G from 2023-02) are the "
                 "stock Starco paid for GV-backed Soylent, which the firm lists as 'Acquired by Starco Brands, 2023' "
                 "(COLLECTION.md s1, the a16z Starco precedent; decisions.md D11). Soylent is the member.",
                 ec="fund_filing", conf="high", cite=jl.LISTING))

# ---- departed partners' seats at their next firms (T4)
for s in ("aligned-co", "deel-inc", "forward-lending-inc", "mosaic-building-group-inc", "payall-payment-systems-inc",
          "somo-labs-inc", "thingy-thing-inc"):
    out(s, "T4: Anish Acharya's seat after GV. The firm's archived listings name him as a deal partner in 2014-15 only; "
           "these filings (2020-26) date from his years as a general partner at Andreessen Horowitz, and none of the "
           "companies is on GV's lists.")
for s in ("bighat-biosciences-inc", "pearl-health-inc", "rezo-therapeutics-inc", "thyme-care-inc", "waymark-inc-de"):
    out(s, "T4: Vineeta Agarwala's seat after GV. Her GV people pages run 2017-19 (Venture Partner); these filings "
           "(2021-25) date from her years at Andreessen Horowitz, and none of the companies is on GV's lists.")
for s in ("echoar-inc", "kadence-inc"):
    out(s, "T4: Eze Vidra's seat after GV. His GV page is 2015 only (General Partner, London); these filings (2020-22) "
           "date from his own firm (Remagine Ventures), and neither company is on GV's lists.")
out("culture-amp-pty-ltd", "T4: Wesley Chan's seat after GV. His GV pages run 2012-14 (the tenure rule's window); "
    "Culture Amp's 2017 filing dates from his years at Felicis, and GV does not list the company.")
out("wellness-express-healthcare-inc", "Homonym: a 2010 executive officer of a Danville, CA home-health issuer; GV's "
    "Wesley Chan was a Google Ventures partner then and served no issuer as an officer. Not on GV's lists.")
out("newlimit-inc", "T4: Blake Byers's seat after GV. His GV pages end in 2020; NewLimit's 2023-25 filings date from "
    "his own fund (Byers Capital), and GV does not list NewLimit.")
out("celularity-inc", "T4: Bill Maris's seat after GV. He left GV in 2016 (his last GV page, as CEO); Celularity's "
    "2017-18 filings date from his own fund, Section 32. Not on GV's lists.")
out("dave-inc", "T4: Bill Maris (William Maris) after GV; Dave's 2017 round was led by his own fund, Section 32. Not "
    "on GV's lists.")
out("steadymd-inc", "T4: Deena Shakir's seat after GV. Her GV pages run 2017-19; SteadyMD's 2021 filing dates from "
    "her years at Lux Capital, and GV does not list the company.")
out("vise-technologies-inc", "T4: Shaun Maguire's seat after GV. His GV pages run 2017-19; Vise's 2020 filing dates "
    "from his years at Sequoia, and GV does not list the company.")
out("expanse-inc", "T4: Shaun Maguire's founder seat. He co-founded Qadium (renamed Expanse in 2019, one CIK) before "
    "joining GV; the 2015-16 filings predate his GV pages and the 2019 filings carry the same seat. No GV vehicle "
    "filing and no GV list carries Qadium or Expanse.", conf="medium")
out("qadium-inc", "The same company as expanse-inc (Qadium renamed Expanse, CIK 1642992): Shaun Maguire's founder "
    "seat, no GV position (T4).", conf="medium")

# ---- the person's own operating career or personal boards (T4)
for s in ("2seventy-bio-inc", "avila-therapeutics-inc", "bind-biosciences-inc", "bluebird-bio-inc",
          "eleven-biotherapeutics-inc", "proclara-biosciences-inc", "rana-therapeutics-llc",
          "springworks-therapeutics-llc", "stromedix-inc", "translate-bio-inc", "xilio-therapeutics-inc",
          "blueprint-medicines-corp"):
    out(s, "T4: Dan Lynch's own boards and operating roles. He joined GV in 2021 as an Executive Venture Partner (his "
           "GV bio: 'since 2007, Dan has advised and served as an executive chair or member of the board' of life "
           "sciences companies); these seats (2009-22) are his own, filed from each company's address, and none of the "
           "companies is on GV's lists.")
out("ember-therapeutics-inc", "T4: Dan Lynch's own 2011 board seat, a decade before he joined GV (2021).")
out("helper-bees-inc", "Homonym: 'Danny Lynch' as executive officer of an Austin eldercare company (2019-25) is not "
    "GV's Dan Lynch, a life sciences executive who joined in 2021. Not on GV's lists.")
out("agios-pharmaceuticals-inc", "T4: David Schenkein's own company. He was Agios's CEO (his GV bio) and files as its "
    "executive officer in 2010-11, a decade before joining GV. GV does not list Agios.")
out("sherlock-biosciences-inc", "T4: Issi Rozen's founder seat. He co-founded Sherlock at the Broad Institute (his GV "
    "bio: 'spinning out more than 20 companies and co-founding another five'); the filings (2019-22) give the company's "
    "address, no GV vehicle filing exists, and GV does not list Sherlock.", conf="medium")
out("izotope-inc", "T4: Issi Rozen's 2016 board seat at an audio-software company, before he joined GV. Not on GV's "
    "lists.")
out("cedilla-therapeutics-inc", "T4: Rosana Kapeller's own board seat (2020-21), filed from the company's address; she "
    "was a GV entrepreneur in residence in 2019 and is a GV advisor today. GV does not list Cedilla.", conf="medium")
out("remix-therapeutics-inc", "T4: Scott Biller's own board seat. His GV bio lists Remix among the boards he serves on "
    "beside GV companies; the 2024 Form D gives the company's address, no GV vehicle filing exists, and GV does not "
    "list Remix.", conf="medium")
out("bonum-therapeutics-inc", "T4: Samuel Blackman's own board seat. He joined GV as an entrepreneur in residence in "
    "2025 (his GV bio: a physician-scientist and cancer drug developer); Bonum's 2026 Form D gives the company's "
    "address, no GV vehicle filing exists, and GV does not list Bonum.", conf="medium")
for s in ("comicbook-com-llc", "elemental-technologies-inc", "nuvocargo-inc"):
    out(s, "Homonym or pre-tenure: 'Samuel Blackman' on this filing is Elemental Technologies' co-founder and a "
           "technology executive, not GV's Samuel Blackman (a pediatric neuro-oncologist and drug developer who joined "
           "in 2025, his GV bio). Not on GV's lists.")
for s in ("gretel-labs-inc", "neeva-inc", "snowflake-inc"):
    out(s, "T4: Sridhar Ramaswamy's own operating and board roles (Neeva's founder, Snowflake's executive, a Gretel "
           "director from his Greylock years); his GV pages date from 2019 as an entrepreneur in residence and venture "
           "partner, and no GV vehicle or GV list carries these companies.")
out("covertree-inc", "T4: Rishie Modi's own operating role (executive officer and director of CoverTree, Detroit, 2021) "
    "before he joined GV as an associate. Not on GV's lists.")
out("prosky-inc", "Homonym or pre-tenure: 'Crystal Huang' as executive officer of a Lehi, Utah staffing company (2019) "
    "is not GV's Crystal Huang, whose GV pages start in 2021. Not on GV's lists.")
out("sim-ops-studios-inc", "T4: Shanna Tellerman's own company (2009-10), before GV. Not on GV's lists.")
out("viacor-inc", "Homonym: 'Chris Hutchins' as executive officer of a Massachusetts medical-device company (2009-10) "
    "is not the Chris Hutchins GV's 2014-15 listings name as a deal partner. Not on GV's lists.")
out("nuepath-2-llc", "Homonym: 'Kevin Rose' as executive officer of a Kansas health-care LLC (2010) is not GV's Kevin "
    "Rose. Not on GV's lists.")

# ---- Andrew Wheeler: three filings, no GV corroboration
out("seekops-inc", "Name-match without corroboration: 'Andrew Wheeler' is a director on SeekOps's 2021 Form D, filed "
    "from the company's Austin address. The name is common, no GV vehicle filing exists, and GV's lists (live and "
    "archived, 2012-2026) never carried SeekOps; a name-match needs affirmative corroboration (COLLECTION.md s1).",
    conf="medium")
out("skyword-inc", "Homonym: 'Andrew Wheeler' as executive officer and director of Skyword, Boston (2021), not GV's "
    "general partner. Not on GV's lists.")
out("nsca-llc", "Homonym: 'Andrew Wheeler' as executive officer of an Alexandria, VA LLC (2024). Not on GV's lists.")

# ---- common-name clusters: homonyms
for s in ("4040-llc", "gray-media-inc", "monster-medic-inc", "pete-inc"):
    out(s, "Homonym: 'Luis Garcia' (GV's Luis Garcia was a 2012 associate) on a filing in another year, city and "
           "industry. Not on GV's lists.")
for s in [k for k, r in base.items() if (r.get("partners_formd") or "") == "Scott Davis"
          and not r.get("site_url") and not r.get("wayback_years")]:
    out(s, "Homonym cluster: 'Scott Davis' (GV's Scott Davis is a life sciences venture partner) as an executive officer "
           "or director of mining, energy, media and data-center issuers (Vancouver, Dallas, Denver and elsewhere). No "
           "filing fits GV and none of the companies is on GV's lists.")

import sys
if "--dry" in sys.argv:
    print(len(L), sorted({x["slug"] for x in L}))
else:
    jl.write("members-1", L)
