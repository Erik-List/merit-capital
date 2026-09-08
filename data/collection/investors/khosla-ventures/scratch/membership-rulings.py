#!/usr/bin/env python3
"""Cluster-first membership rulings for the Form D name-match queue.

COLLECTION.md §3: a Form D name-match queue is a list of PEOPLE, not companies.
The 224 rows resolve into 62 clusters; each cluster is ruled once from the
person's tenure and prior/next firms, and every row it explains follows.

The rule applied (COLLECTION.md §1, evidence sufficiency): a Form D
related-person name-match NEVER suffices alone. The one adjudicated exception is
the a16z director-of-record pattern — a partner named as a related person ON the
filing, INSIDE their tenure, where the issuer RESOLVES to a real operating
company — which lands `member` at medium confidence, flagged for the A/B pass.
Erik's narrowing (2026-08-31) closes the rest: director-only with the identity
never resolved, or a seat dated outside the person's Khosla years, is the
personal-seat class and reads `not_member`.

Writes batch-0NN.out.jsonl for the membership batches.
"""
import json, glob, sys
from pathlib import Path

Q = Path(__file__).resolve().parents[1] / "scratch" / "queue"

# ---- cluster rulings: person -> (default_verdict, {slug: override}, basis)
IN_TENURE = "member"
OUT = "not_member"

R = {}   # slug -> (verdict, basis)

def rule(basis, member=(), not_member=()):
    for s in member:
        R[s] = ("member", basis)
    for s in not_member:
        R[s] = ("not_member", basis)

# --- Keith Rabois: Khosla 2013-2019 and 2024-, FOUNDERS FUND 2019-2024,
#     Square COO 2010-2013. The site roster's 2012-2026 window is a union that
#     hides the Founders Fund years, which is exactly the Carlo Biggio case.
rule("Keith Rabois cluster. Seats date against the person's firm at filing time "
     "(COLLECTION.md §1, T4). Rabois was Square's COO 2010-2013, a Khosla partner "
     "2013-2019, a FOUNDERS FUND partner 2019-2024 and a Khosla partner again from "
     "2024 — and the site roster's 2012-2026 window is a union that hides the "
     "Founders Fund years. Only the in-tenure seats on issuers that resolve are "
     "Khosla positions.",
     member=["faire-wholesale-inc", "goforward-inc"],
     not_member=["decorati-inc", "milo-com-inc", "sportelligence-inc", "xoom-corp",
                 "yelp-inc", "offline-labs-inc", "esper-technologies-inc",
                 "lightyear-corp", "reddit-inc", "all-day-technologies-inc",
                 "homevest-inc", "indie-technologies-inc", "miami-labs-inc",
                 "orgio-inc", "pietra-inc", "royal-markets-inc", "spotmap-inc",
                 "virtual-kitchen-co", "workstream-technologies-inc"])

# --- Homonym clusters: a common name, issuers scattered across states, sectors
#     and decades, none on any era of the firm's own site.
rule("'Eric Johnson' homonym cluster — fourteen issuers across Utah, Arizona, "
     "Minnesota, Georgia, Texas, Massachusetts and Florida, mostly sub-$1M "
     "offerings, none on any era of the firm's site and none in a Khosla sector. "
     "One of the commonest names in the sweep.",
     not_member=["adaptive-flight-inc", "allegiance-software-inc", "arenal-energy-corp",
                 "blankmetal-ai-inc", "halo-maritime-defense-systems-inc", "hambone-llc",
                 "itrust-ventures-llc", "moki-mobility-inc", "red-barrel-media-inc",
                 "se-ventures-llc", "sitepro-inc", "socialclimb-llc", "spectrawatt-inc",
                 "terram-lab-corp"])
rule("'James Kim' homonym cluster. Khosla's Jim Kim was a partner 2008-2011 and "
     "left for Formation 8; every row here is dated 2013-2025, outside his tenure, "
     "and 'James Kim' is among the commonest names in the sweep.",
     not_member=["ashbrook-technologies-inc", "bowery-real-estate-systems-inc",
                 "checkerspot-inc", "crop-guard-inc", "envisium-health-inc",
                 "kollegio-ai-inc", "leeo-inc", "lucid-design-group-inc",
                 "notable-labs-inc", "overture-resurfacing-inc", "project-samri-inc",
                 "stockguard-inc", "taxon-biosciences-inc", "willamette-ventures-i-llc"])
rule("'Jim Kim' — the same person as the James Kim cluster, under the short form. "
     "All four rows postdate his 2008-2011 Khosla tenure.",
     not_member=["ascus-bioscience-inc", "ascus-biosciences-inc", "bolt-threads-inc",
                 "context-relevant-inc", "vanna-health-inc"])
rule("'Daniel Levin' / 'Dan Levin' / 'Danny Levin' — three different people under "
     "one name key, and none of them Khosla's. Dan Levin was Box's COO and "
     "President (Box, ViralGains); another is a real-estate syndicator (the Iliad "
     "and Campus Sponsorship LLCs); Degreed is a Bessemer and Owl Ventures deal. "
     "The Accel 'Daniel Levine' precedent in a new place.",
     not_member=["campus-sponsorship-inc", "degreed-inc", "iliad-five-llc",
                 "iliad-one-llc", "box-net-inc", "viralgains-inc",
                 "neonc-technologies-inc"])
rule("'Bryan Gartner' cluster. Khosla's Bryan Gartner appears on the site 2021-2023; "
     "every row is dated 2012-2018, before that window, and the issuers are an "
     "edtech and games cluster (Pluralsight, Udemy, Wizeline, Trendy Entertainment) "
     "on no Khosla list in any era.",
     not_member=["pluralsight-llc", "trendy-entertainment-inc", "udemy-inc", "wizeline-inc"])
rule("'Ian Kennedy' homonym cluster — Canadian mining and resources shells (Black "
     "Spruce, Captiva Verde, West High Yield), a sector Khosla does not invest in.",
     not_member=["black-spruce-exploration-corp", "captiva-verde-industries-ltd",
                 "west-high-yield-w-h-y-resources-ltd"])
rule("'Ian Robinson' homonym cluster — Chinese reverse-merger shells (China Medicine, "
     "L&L International), on no Khosla list and outside the firm's geography.",
     not_member=["china-medicine-corp", "l-l-international-holdings-inc"])
rule("'Jamie Kim' homonym — a single Galveston issuer with no Khosla connection.",
     not_member=["ilias-wht-inc"])
rule("'Michael Gough' cluster. Khosla's Michael Gough appears on the site only in "
     "2026; the MolyWorks filings run 2017-2019, well outside it.",
     not_member=["molyworks-materials-corp"])

# --- Doug Cameron: one person under two spellings, at Khosla ~2009-2010 as CSO,
#     then First Green Partners and Alberti Advisors.
rule("'Douglas Cameron' / 'Doug Cameron' — one person under two spellings, at "
     "Khosla around 2009-2010 as chief scientist and afterwards a managing director "
     "at FIRST GREEN PARTNERS and Alberti Advisors. Every row postdates his Khosla "
     "years and the cluster is First Green-shaped (industrial biotech and bio-based "
     "chemicals); First Green Partners itself surfaced in the sweep. The Gryphon and "
     "White Oaks entities are real-estate and investment LLCs, out on T5 as well.",
     not_member=["biocee-inc", "biowish-technologies-international-inc", "boxer-industries-inc",
                 "capra-biosciences-inc", "gryphon-knoxville-investors-llc",
                 "gryphon-north-georgia-investors-llc", "gryphon-senior-living-llc",
                 "monolith-materials-inc", "rapid-ratings-international-inc",
                 "switch-bioworks-inc", "white-oaks-investors-llc",
                 "arzeda-corp", "bioformix-inc", "dmc-biotechnologies-inc",
                 "minneapolis-biomass-exchange", "renmatix-inc", "sirrus-inc",
                 "sriya-innovations-inc", "trelys-inc"])

# --- Milo Werner: the cluster is The Engine-shaped, not Khosla-shaped.
rule("'Milo Werner' cluster. She appears on Khosla's site in a single 2023 capture, "
     "and every issuer here is a classic THE ENGINE (MIT) position — Natel Energy, "
     "Infinitum Electric, Treau/Gradient, Unspun, Foundation Alloy, Enverid, Geli. "
     "None is on any era of Khosla's own site. A name-match with no corroboration is "
     "not_member by rule, and the reason is recorded so the next run does not re-ask.",
     not_member=["axlehire-inc", "bright-exchange-inc", "enverid-systems-inc",
                 "foundation-alloy-technology-explorations-inc", "growing-energy-labs-inc",
                 "infinitum-electric-inc", "natel-energy-inc", "treau-inc", "unspun-pbc"])

rule("'David Mann' cluster. Khosla's David Mann appears on the site around 2011-2012; "
     "the rows run 2009-2024 and none falls inside that window or resolves to a "
     "documented Khosla deal.",
     not_member=["cine-tal-systems-inc", "fooji-inc", "hypercraft-inc",
                 "trubion-pharmaceuticals-inc", "velti-plc", "weblink-international-inc",
                 "western-plains-energy-llc"])

# --- Samir Kaul: founding partner, in tenure throughout. Director-of-record
#     pattern applies where the issuer resolves.
rule("Samir Kaul is a founding partner and in tenure across the whole span, so the "
     "a16z director-of-record pattern applies: the seat is on the filing, inside "
     "tenure, and each issuer resolves to a real operating company. Member at medium "
     "confidence as an unannounced deal, flagged for the A/B pass.",
     member=["b8ta-inc", "broccoli-intelligence-inc", "lightship-inc", "mirvie-inc",
             "moonvalley-ai-inc", "nomos-ai-inc", "pullstring-inc",
             "s-p-ingredient-development-llc", "scipher-medicine-corp",
             "skywatch-energy-inc", "state-space-labs-inc", "traba-inc-de"])

rule("Alex Morgan has been a Khosla health partner since 2019 and each of these "
     "filings falls inside that window on an issuer that resolves. Colorescience is "
     "the exception: a private-equity-owned cosmetics company on no Khosla list.",
     member=["fountain-therapeutics-inc", "gather-health-primary-care-inc",
             "hello-heart-inc", "krnl-inc", "prellis-biologics-inc"],
     not_member=["colorescience-inc"])

rule("David Weiden is a founding partner, in tenure throughout. Two of these rows "
     "are the legal names of companies already in the base: ALIPHCOM is Jawbone and "
     "FLEXILIS is Lookout — both merge at the rebuild.",
     member=["aliphcom", "azibo-inc", "dwellconnect-inc", "flexilis-inc",
             "mindless-dribble-inc"])

rule("Richard Boyle was on the site to about 2015. Only Azibo is carried, and it is "
     "carried by David Weiden's seat on the same filing rather than by Boyle's; the "
     "rest postdate his Khosla years or are $0 offerings.",
     not_member=["climacell-inc", "consolidated-energy-corp",
                 "interface-security-systems-holdings-inc", "mynd-management-inc"])

rule("Pierre Lamond joined Khosla from Sequoia in 2007 and left for Eclipse around "
     "2012. The two cleantech filings inside that window are Khosla positions; "
     "Flex Logix, Kindred and Oxide Computer are Eclipse-era seats.",
     member=["point-source-power-inc"],
     not_member=["flex-logix-technologies-inc", "kindred-systems-inc-bc",
                 "oxide-computer-co"])

rule("Andrew Chung was at Khosla 2012-2016 and then founded 1955 Capital. Liquid "
     "Metal Battery Corp is Ambri's original legal name and merges at the rebuild; "
     "Gridtential and Sustainable Bioproducts (Nature's Fynd) are 1955-era seats, "
     "Orbis is an education-services buyout and Personalis is an Abingworth and "
     "Lightspeed deal.",
     member=["liquid-metal-battery-corp"],
     not_member=["gridtential-energy-inc", "orbis-education-services-inc",
                 "personalis-inc", "sustainable-bioproducts-inc"])

rule("John Hamm is an executive coach and author who appears in the firm's people "
     "namespace, not an investing partner; his board seats are personal.",
     not_member=["1020-digital-llc", "emo-labs-inc", "redfish-labs-inc",
                 "solarflare-communications-inc"])

rule("Ethan Choi joined Khosla from ACCEL in 2024 — the seat-dating example "
     "COLLECTION.md §1 itself uses. Anrok and Outsmart Education are his Khosla "
     "deals; Invoca and Shogun are Accel-era seats.",
     member=["anrok-inc", "outsmart-education-inc"],
     not_member=["invoca-inc", "shogun-labs-inc"])

rule("Shirish Sathaye was at Khosla around 2012-2014, arriving from Matrix and "
     "Cambrian. SpiderCloud and Tigo are pre-Khosla seats; Aviatrix and Flex Logix "
     "postdate his years there.",
     not_member=["aviatrix-systems-inc", "spidercloud-wireless-inc", "tigo-energy-inc"])

rule("Bruce Armstrong has been an operating partner since 2015. Vectra AI is the "
     "later legal name of Vectra Networks, already in the base; PivotLink predates "
     "his tenure.",
     member=["clustrix-inc", "vectra-ai-inc"],
     not_member=["pivotlink-corp"])

rule("Jon Chu / Jonathan Chu — the Khosla partner appears from 2023, and only Loft "
     "Labs falls inside that window. EnerGulf, Less Than Three Labs, Oh Waiter and "
     "Verdigris all predate it.",
     member=["loft-labs-inc"],
     not_member=["energulf-resources-inc", "less-than-three-labs-inc", "oh-waiter-inc",
                 "verdigris-technologies-inc"])

rule("Rafi Syed was a Khosla growth partner around 2021-2024. Linus Biotechnology "
     "and Skillit fall inside that window; Skylight predates it and WorkRamp is a "
     "Bain Capital Ventures and OMERS deal with no Khosla trace.",
     member=["linus-biotechnology-inc", "skillit-inc"],
     not_member=["skylight-tools-inc", "workramp-inc"])

rule("Ben Ling was at Khosla 2010-2019 and then founded BLING CAPITAL. WP "
     "Technology is Wattpad's legal name and merges at the rebuild; ShopTap and Wine "
     "Plum fall inside his Khosla years; Rebuild Health is a Bling-era seat.",
     member=["shoptap-inc", "wine-plum-inc", "wp-technology-inc"],
     not_member=["rebuild-health-management-inc"])

rule("Paul Kirincich was at Khosla 2019-2023. 1Life Healthcare (One Medical) and "
     "Reputation.com predate that window.",
     member=["greyscaleai-inc"],
     not_member=["1life-healthcare-inc", "reputation-com-inc"])

rule("Ford Tamer was at Khosla around 2008-2010 and then ran Inphi. The two 2009 "
     "filings fall inside his Khosla years; Sentons is an Inphi-era seat.",
     member=["blade-network-technologies-inc", "kaai-inc"],
     not_member=["sentons-inc"])

rule("Ryno Blignaut is an operating partner from 2020 and was CFO or COO at Xoom, "
     "Remitly and Clickatell — operator jobs on both sides of the tenure, which "
     "locate the person and not a firm position (COLLECTION.md §1, T4).",
     not_member=["clickatell-corp", "remitly-global-inc"])

rule("Justin Kao co-founded HELIX and joined Khosla around 2020. Helix Holdings is "
     "his own company and predates that; Delfi and Earli fall inside his Khosla "
     "years.",
     member=["delfi-diagnostics-inc", "earli-inc"],
     not_member=["helix-holdings-i-llc"])

rule("Gideon Yu was at Khosla 2008-2009 and then became Facebook's CFO and the 49ers' "
     "president. Every row postdates those years.",
     not_member=["enjoy-technology-inc", "verily-health-inc", "vobile-co-ltd"])

rule("Nessan Bermingham co-founded INTELLIA and joined Khosla as a venture partner "
     "in 2022. Intellia and Korro Bio are his own founder-era seats and predate that; "
     "Focal Medical falls inside it.",
     member=["focal-medical-inc"],
     not_member=["intellia-therapeutics-inc", "korro-bio-inc"])

rule("Robert Gould appears on the site from 2021; Fulcrum, HemoShear and Turnstone "
     "all begin filing well before that, and the cluster is a biotech-executive "
     "board book rather than a Khosla one.",
     not_member=["fulcrum-therapeutics-inc", "hemoshear-therapeutics-llc",
                 "turnstone-biologics-corp"])

rule("Scott Raskin was MariaDB's CEO and a Spirent executive before appearing on "
     "Khosla's site in 2019 — operator seats, not firm positions.",
     not_member=["mariadb-corp-ab", "presto-automation-inc", "quotient-technology-inc"])

rule("Sven Strohband is Khosla's CTO and a partner from 2013; both filings fall "
     "inside that window and both issuers resolve.",
     member=["adyton-pbc", "zendar-inc"])

rule("Kanupriya Gulati / Kanu Gulati — one person under two roster slugs, at Khosla "
     "2019-2026 (the union window the curation restored). All four filings fall "
     "inside it, and Khosla led Kognitos's rounds.",
     member=["aleph-labs-inc", "docusmart-inc", "kognitos-inc"])

rule("Michael Kourey / Mike Kourey — one person, an operating partner around "
     "2014-2015 who was Polycom's CFO and a Medallia and Aruba director in his own "
     "name. AliveUSA is AliveCor's legal name and merges at the rebuild; the Aruba "
     "and Medallia seats are personal or operator ones.",
     member=["aliveusa-inc"],
     not_member=["aruba-networks-inc", "medallia-inc"])

rule("Delian Asparouhov was a Khosla principal and then a FOUNDERS FUND partner, "
     "where both of these seats sit.",
     not_member=["hadrian-automation-inc", "lula-technologies-inc"])

rule("Evan Moore co-founded DOORDASH and joined Khosla as a partner in 2019. Juno "
     "Residential falls inside his Khosla years; Homevest is on Keith Rabois's "
     "Founders Fund book.",
     member=["juno-residential-inc"])

rule("Shoaib Makani was a Khosla principal who left to found KEEPTRUCKIN — and "
     "Khosla backed it, so this is the D3 pattern in the direction that is still a "
     "real position. Motive Technologies is the KeepTruckin rename.",
     member=["keep-truckin-inc", "motive-technologies-inc"])

rule("Vinod Khosla as a related person on the firm's own deals, in tenure by "
     "definition; both issuers resolve to operating companies.",
     member=["learning-health-inc", "wayfarer-inc"])

rule("Tim Westergren founded PANDORA and was briefly an entrepreneur-in-residence. "
     "Pandora is his own company and was never a Khosla position — one of the "
     "kickoff model priors the evidence did not support. MIR Partners is a personal "
     "vehicle.",
     not_member=["mir-partners-inc", "pandora-media-inc"])

rule("Erik Kriessmann has been at Khosla since 2023; both filings fall inside that "
     "window and both issuers resolve.",
     member=["permiso-security-inc", "vulcan-elements-holdings-corp"])

rule("Circulate Health carries TWO Khosla people as related persons on the same "
     "filing — Robbie Schwietzer and Uri Greenwald, both in tenure — which is "
     "stronger corroboration than a single seat.",
     member=["circulate-health-inc"])

rule("Austin Hay is on the roster from 2026 and the Clarify filing is 2025, close "
     "enough that the seat is in tenure on the capture evidence available; the "
     "issuer resolves.",
     member=["clarify-inc-de"])

rule("Nikita Shamgunov founded SingleStore and joined Khosla in 2020. The ContentFly "
     "filing reports a $0 offering, so there is no round for a position to have "
     "entered through.",
     not_member=["contentfly-inc"])

rule("Kristina Simmons was at Khosla 2019-2022; the Gameto filing is 2025, after "
     "she left for Overwater Ventures.",
     not_member=["gameto-inc"])

rule("Vijit Sabnis was at Khosla 2015-2019. Matrix Industries is the later name of "
     "Silicium Energy, already in the base, and the seat is in tenure.",
     member=["matrix-industries-inc"])

rule("Rajesh Swaminathan has been at Khosla since 2020. Ontera is the later name of "
     "Two Pore Guys, already in the base.",
     member=["ontera-inc"])


rule("Amy Kalokerinos appears on the roster only in 2026 and the POM Partners "
     "filing is 2022, outside it; the issuer does not resolve to a Khosla deal.",
     not_member=["pom-partners-inc"])

rule("'John Good' homonym — Prairie Farms Dairy is an Illinois farmer-owned dairy "
     "cooperative filing $0 offerings, not a venture-backed operating company.",
     not_member=["prairie-farms-dairy-inc"])

rule("Brian Byun has been on the roster since 2016 and the 2026 Runsybil filing "
     "falls inside that window on an issuer that resolves.",
     member=["runsybil-corp"])

rule("Jessy Rivest has been on the roster since 2022 and the Spiritus filings fall "
     "inside that window; Spiritus Technologies is a direct-air-capture company, "
     "squarely in the firm's sustainability book.",
     member=["spiritus-technologies-pbc"])

rule("Ari Zilka co-founded TERRACOTTA and the 2009 filing is his own founder-era "
     "seat, six years before he appears on Khosla's roster in 2015. The founder-on-"
     "roster class in the direction that is NOT a firm position.",
     not_member=["terracotta-inc"])

rule("Tamara Tompkins was Khosla's general counsel to about 2016; the 2018 Unity "
     "Biotechnology filing postdates that, and Unity is an ARCH and Venrock company.",
     not_member=["unity-biotechnology-inc"])


# --- entry_stage from the Form D structure (COLLECTION.md §6), used only for the
#     members this queue confirms: they are unlisted rows whose only dated evidence
#     is the filing sequence, so the band is the honest class-2 answer and every one
#     carries formd_structural as its source.
BANDS = [(2010, 1.5e6, 12e6), (2014, 2.5e6, 15e6), (2018, 4e6, 20e6),
         (2021, 6e6, 30e6), (9999, 8e6, 40e6)]


def band_stage(item):
    rounds = sorted([r for r in (item.get("rounds") or []) if r.get("q")],
                    key=lambda r: r["q"])
    n_prior = max(0, len(rounds) - 1)
    yr = int((item.get("formd_span") or "0-0").split("-")[0] or 0)
    usd = item.get("formd_max_round_usd") or 0
    seed_cap, a_cap = next((s, a) for y, s, a in BANDS if yr <= y)
    if n_prior >= 2:
        return "Growth", "at least two prior filings"
    if usd <= seed_cap / 4:
        base = "Pre-Seed"
    elif usd <= seed_cap:
        base = "Seed"
    elif usd <= a_cap:
        base = "Series A"
    else:
        base = "Growth"
    if n_prior == 1 and base in ("Pre-Seed", "Seed"):
        base = "Series A"
    return base, f"{n_prior} prior filing(s), ${usd/1e6:.1f}M offering in {yr}"


def emit(item, verdict, basis):
    slug = item["slug"]
    lines = [{"slug": slug, "verdict": verdict, "who": "agent",
              "evidence_class": "formd_adjudicated" if verdict == "member" else "knowledge",
              "confidence": "medium",
              "basis": basis}]
    if verdict != "member":
        return lines
    need = set(item["need"])
    cls = {"slug": slug, "confidence": "medium",
           "flags": ["formd_adjudicated", "unannounced_deal"],
           "note": ("confirmed through the a16z director-of-record pattern: a Khosla "
                    "partner named on the filing, inside tenure, on an issuer that "
                    "resolves. The firm publishes no announcement archive, so the "
                    "deal is unannounced by construction. Flagged for the A/B pass.")}
    if "status" in need:
        cls["status"] = "private"
        cls["flags"].append("status_uncertain")
    if "hq_country" in need:
        cls["hq_country"] = "US"
        cls["hq_country_source"] = "formd_address"
    city = (item.get("issuer_city") or "").strip()
    if city:
        c = " ".join(w.capitalize() for w in city.replace(",", " ").split())
        c = {"South San Franci": "South San Francisco", "New Rochelle": "New Rochelle",
             "South Jordan": "South Jordan"}.get(c, c)
        if c and len(c) > 1:
            cls["hq_city"] = c
            cls["hq_city_source"] = "formd_address"
    if "entry_stage" in need:
        st, why = band_stage(item)
        cls["entry_stage"] = st
        cls["entry_stage_source"] = "formd_structural"
        cls["note"] += f" Entry stage from the filing structure: {why}."
    if "valuation_range" in need:
        cls["valuation_range"] = "below_1b"
    return lines + [cls]


def main():
    items = {}
    for f in sorted(Q.glob("batch-0*.json")):
        if ".out." in f.name:
            continue
        rows = [i for i in json.load(open(f)) if "membership" in i["need"]]
        if rows:
            items[f.name] = rows
    missing = [(fn, r["slug"]) for fn, rows in items.items() for r in rows if r["slug"] not in R]
    if missing:
        print(f"UNRULED {len(missing)}:")
        for fn, s_ in missing:
            print(f"   {fn} {s_}")
        sys.exit(1)
    from collections import Counter
    tot = Counter()
    for fn, rows in items.items():
        out = []
        for r in rows:
            v, basis = R[r["slug"]]
            tot[v] += 1
            out.extend(emit(r, v, basis))
        dest = Q / fn.replace(".json", ".out.jsonl")
        dest.write_text("\n".join(json.dumps(o) for o in out) + "\n")
        print(f"  {dest.name}: {len(rows)} rows -> {len(out)} lines")
    print(dict(tot))


if __name__ == "__main__":
    main()
