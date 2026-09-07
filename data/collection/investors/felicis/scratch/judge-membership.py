#!/usr/bin/env python3
"""The 93 membership rows, judged CLUSTER-FIRST (COLLECTION.md §3).

"A Form D name-match queue is a list of people, not companies: resolve the
person once -- tenure window, prior and next firms, operator jobs, founder-era
paper -- then sweep every row that person explains against the decisions file."

Every one of these 93 rows reached the base through the roster-name Form D
sweep ALONE: none carries a listing on any Felicis surface in any era, and
none carries a fund vehicle on the filing. §1's evidence rule is therefore
decisive before any individual row is considered -- "A Form D related-person
name-match NEVER suffices alone... Absence of corroboration on a name-match is
a `not_member` verdict, not an `uncertain` one".

So the work is not 93 judgments, it is 19 people. Three rows survived the one
pattern that CAN promote a bare name-match -- the a16z director-of-record
pattern, a current partner listed as Director on the filing itself, in tenure
-- and all three then resolved to companies the base already holds under their
trading names, so they are identity merges rather than new members
(identity-merges.json).

Writes verdict lines into the batch .out.jsonl files each slug belongs to.
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from emit import WHO  # noqa: E402

QUEUE = Path(__file__).resolve().parents[1] / "scratch" / "queue"

# ---------------------------------------------------------------------------
# One ruling per person. `klass` is the exclusion class for the report.
# ---------------------------------------------------------------------------
CLUSTERS = {
    "John Anderson": dict(
        klass="homonym",
        basis="Cluster ruling: 'John Anderson' is the largest homonym cluster in "
              "the sweep (45 rows). Felicis's John Anderson is a Venture Partner "
              "listed from 2021; these issuers are Vancouver mining and resource "
              "shells, Texas food LLCs, Oklahoma reinsurance, Mississippi "
              "healthcare co-ops and Santos Ltd (an Adelaide oil major filing a "
              "$376M offering) -- filed 2009-2026, most of them outside his "
              "tenure, none a venture-backed operating company, none listed on "
              "any Felicis surface in any era. Name-match with no corroboration "
              "is not_member (COLLECTION.md §1)."),
    "Danny Lee": dict(
        klass="homonym",
        basis="Cluster ruling: ten Vancouver mining and energy issuers "
              "(Guanajuato Silver, Newcore Gold, NuLegacy, Southern Arc, LNG "
              "Energy, Edgewater, Eagle Hill, Enterprise Energy, Carbonone, "
              "Interfield Global). Same British Columbia small-cap filer "
              "population as the John Anderson cluster. No Felicis listing, no "
              "fund vehicle on any filing."),
    "Daniel Lee": dict(
        klass="homonym",
        basis="Cluster ruling: Las Vegas casino vehicles (AREH MLK, Creative "
              "Casinos, Full House Resorts), Ohio and Texas industrials (Myers "
              "Industries, Aperion Biologics), an Illinois SaaS and a Vancouver "
              "miner. 'Daniel Lee' is not a Felicis investing name at all -- the "
              "roster slug is the archived 'dan-lee' page of 2019. No listing, "
              "no corroboration."),
    "Dan Lee": dict(
        klass="homonym",
        basis="Cluster ruling: same person-name problem as 'Daniel Lee' and "
              "'Danny Lee'; Arrow App, Breakpoint Health and Span America "
              "Medical Systems have no Felicis listing and no fund vehicle on "
              "the filing."),
    "Jack Abraham": dict(
        klass="ex_partner_next_firm",
        basis="Cluster ruling: Jack Abraham founded and runs Atomic, the venture "
              "studio, and every issuer here is an Atomic company or an Atomic "
              "studio entity (Miami Labs, Natomas Labs, Butter Payments, "
              "Raydiant, Neurawell). On Raydiant and the Labs entities he files "
              "as EXECUTIVE OFFICER, which locates his own operating role; on "
              "Butter Payments he files as Director, which is his Atomic seat. "
              "T4 asks whose money sat behind the seat and the answer is "
              "Atomic's. None is listed on a Felicis surface."),
    "Wesley Chan": dict(
        klass="seat_dating",
        basis="Cluster ruling, and the textbook §1 seat-dating case in BOTH "
              "directions from one person. Wesley Chan was at Google Ventures "
              "before Felicis (roster 2015-2022) and left to co-found FPV "
              "Ventures. Transphorm's Form Ds run 2010-2014 with him as Director "
              "-- his GV-era board seat, a PRIOR-firm deal. YENDO's run 2023 -- "
              "a NEXT-firm deal, after he had gone. Wellness Express Healthcare "
              "(2010) is neither. A seat is dated against the person's firm at "
              "filing time, not against the roster."),
    "Eric Wagner": dict(
        klass="homonym",
        basis="Cluster ruling: two Ohio issuers (Agility Inc of Brecksville, "
              "Converge Ventures LLC of Hilliard, the second fund-shaped). No "
              "Felicis listing, no corroboration."),
    "Kim Vogel": dict(
        klass="operator_role",
        basis="Cluster ruling: 'Kim Vogel' files at mfoundry as EXECUTIVE "
              "OFFICER, which is her own operating job, not a Felicis seat; "
              "Base Venture Investing is fund-shaped. §1: a Section 16 or "
              "related-person filing by a natural person locates the person, "
              "never a firm position."),
    "Kimberly Vogel": dict(
        klass="operator_role",
        basis="Same person as the 'Kim Vogel' cluster. At Medina Medical she "
              "files as Executive Officer in 2012-2013 and as Director in 2015 "
              "-- an operator who joined her own company's board. Medina Medical "
              "(Menlo Park, neurovascular devices, acquired by Medtronic in "
              "2015) appears on no Felicis listing."),
    "Mike Chen": dict(
        klass="homonym",
        basis="Cluster ruling: Channel Ledger and Vyopta, neither listed by "
              "Felicis; a two-token common name with no corroboration."),
    "Michael Chen": dict(
        klass="operator_role",
        basis="Cluster ruling: files as EXECUTIVE OFFICER at both Seaport "
              "Therapeutics (a Boston biotech whose $226M round is a Third "
              "Rock/ARCH-shaped syndicate) and SUR-SEAL Holding. Operating "
              "roles, not Felicis seats."),
    "John Abraham": dict(
        klass="homonym",
        basis="Cluster ruling: 'John Abraham' is not a Felicis roster name; "
              "Critical Telephone Applications and Daily Juice Group are Texas "
              "issuers with no Felicis connection."),
    "Jian Chen": dict(
        klass="operator_role",
        basis="Files as EXECUTIVE OFFICER at Nanosys across 2015-2018 -- an "
              "operating role. Nanosys is a Lux Capital position, not a Felicis "
              "one, and appears on no Felicis surface."),
    "Tim Bertrand": dict(
        klass="homonym",
        basis="Placester (Boston real-estate SaaS, $50M in 2017) with 'Tim "
              "Bertrand' as Director. Not a Felicis investing name and the "
              "company is on no Felicis listing."),
    "Jameson Detweiler": dict(
        klass="operator_role",
        basis="Fantasmo Studios' 2017 Form D lists him as EXECUTIVE OFFICER, "
              "which is his own founder/operator role, not a Felicis board "
              "seat. No listing."),
    "Jack Anderson": dict(
        klass="homonym",
        basis="Rock Springs Mineral Processing (Casper, Wyoming) -- the same "
              "small-cap resource filer population as the John Anderson "
              "cluster."),
}

# The three rows that DID pass the director-of-record test, and then turned out
# to be the base's own companies filing under their registered names. They are
# members, and identity-merges.json folds them into the canonical row at the
# scheduled rebuild.
DUPLICATES = {
    "atlas-labs-inc": (
        "atlas-health",
        "Registered entity of Atlas Health. Form D 0001790561-22-000001 "
        "($41,499,962) lists SUNDEEP PEECHU as Director in tenure; the round is "
        "the $40M Series A of Jan 2022 that Felicis LED. Merged into "
        "atlas-health at the rebuild; flagged, never silently merged.",
        "https://www.businesswire.com/news/home/20220125005225/en/Atlas-Health-Raises-%2440M-Series-A-to-Expand-AI-Powered-Patient-Advocacy-Solution"),
    "prm-solutions-inc": (
        "proton",
        "Files 'dba Proton.ai'. Form D 0001849278-22-000001 ($24,041,802) lists "
        "NIKI PEZESHKI as Director in tenure. Merged into the base row `proton`.",
        "https://www.intelligence360.news/cambridge-massachusetts-based-prm-solutions-dba-proton-ai-is-raising-24041802-00-in-new-equity-investment/"),
    "hippo-analytics-inc": (
        "hippo-insurance",
        "Registered entity of Hippo Insurance. Form D 0001178913-18-003000 "
        "($62,000,000) lists VICTORIA TREYGER as Director. The base already "
        "carries hippo-insurance from the firm's own site (2019, 2020, 2023).",
        None),
}


def main() -> None:
    queue = json.loads((QUEUE / "queue.json").read_text())
    mem = {x["slug"]: x for x in queue if "membership" in x["need"]}

    # slug -> batch number
    where = {}
    for f in sorted(QUEUE.glob("batch-[0-9][0-9][0-9].json")):
        for x in json.loads(f.read_text()):
            where[x["slug"]] = int(f.stem.split("-")[1])

    by_batch = defaultdict(list)
    unresolved = []
    counts = defaultdict(int)

    for slug, item in mem.items():
        if slug in DUPLICATES:
            canonical, basis, cite = DUPLICATES[slug]
            row = {"slug": slug, "who": WHO, "verdict": "member",
                   "evidence_class": "formd_adjudicated",
                   "basis": basis, "confidence": "high",
                   "flags": ["duplicate_suspected"],
                   "note": f"Duplicate of {canonical}; see identity-merges.json."}
            if cite:
                row["citation"] = cite
            by_batch[where[slug]].append(row)
            counts["member (duplicate)"] += 1
            continue

        person = (item.get("partners_formd") or "").strip()
        rule = CLUSTERS.get(person)
        if not rule:
            unresolved.append((slug, person))
            continue
        by_batch[where[slug]].append({
            "slug": slug, "who": WHO, "verdict": "not_member",
            "evidence_class": "web", "confidence": "high",
            "exclusion_class": rule["klass"],
            "basis": rule["basis"],
        })
        counts[rule["klass"]] += 1

    for n, rows in sorted(by_batch.items()):
        out = QUEUE / f"batch-{n:03d}.out.jsonl"
        prev = out.read_text().splitlines() if out.exists() else []
        seen = {json.loads(l)["slug"] for l in prev if l.strip()}
        new = [json.dumps(r, ensure_ascii=False) for r in rows
               if r["slug"] not in seen]
        out.write_text("\n".join(prev + new) + "\n")
        print(f"  batch-{n:03d}.out.jsonl: +{len(new)} verdict lines")

    print(f"\njudged {sum(counts.values())} membership rows as "
          f"{len(CLUSTERS)} person clusters + {len(DUPLICATES)} duplicates")
    for k, v in sorted(counts.items(), key=lambda kv: -kv[1]):
        print(f"   {k:22} {v}")
    if unresolved:
        print(f"\n  UNRESOLVED ({len(unresolved)}): {unresolved}")


if __name__ == "__main__":
    main()
