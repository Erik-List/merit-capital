#!/usr/bin/env python3
"""Write companies/identity-merges.json: name-variant merges, the Digital East
desk assignment (decisions.md D2) and the non-company rejects.

Run before every rebuild; it only names slugs that exist in base.json and says
which listed slugs it could not find.  python3 scratch/eb_overlay.py
"""
from __future__ import annotations

import collections
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = "earlybird-venture-capital"

# canonical <- duplicates, the published name, and why they are one company
MERGES = [
    ("carpooling-com", ["mikini-media-gmbh"], "Carpooling.com", "one company: Mikini Media GmbH was renamed carpooling.com GmbH in June 2011 (deutsche-startups 2011-06-07; one register entry)"),
    ("parima", ["gourmey"], "Parima", "one company: Gourmey (Paris) bought Vital Meat in October 2025 and renamed itself Parima"),
    ("aiperia", ["planerai-gmbh", "planerai"], "Aiperia", "one company: PlanerAI GmbH was renamed AIPERIA GmbH on 2024-06-27 (AG Mannheim HRB 739160)"),
    ("carto", ["cartodb-inc"], "Carto", "one company: CartoDB Inc. renamed itself CARTO in 2016; the firm's list keeps the old name, its job board the new one"),
    ("arago-inc", ["arago"], "Arago", "one company: the firm's list ('Arago') and its job board ('Arago Inc.')"),
    ("everoad-by-sennder", ["everoad"], "Everoad", "one company: Everoad S.A.S. (Convargo until 2018), 'Everoad by sennder' on the job board. Sennder is NOT merged in: Earlybird put new money into Sennder's June 2020 round on top of the shares it took in the merger, so Sennder is its own row (decisions.md R2)"),
    ("greenlyte", ["greenlyte-carbon-technologies"], "Greenlyte", "one company: Greenlyte Carbon Technologies GmbH"),
    ("obligate-ex-fqx", ["obligate", "fqx"], "Obligate", "one company: FQX AG renamed itself Obligate in 2022 (the firm's own label: 'Obligate (ex FQX)')"),
    ("korial", ["energy-robotics", "energy-robotics-gmbh"], "Korial", "one company: the firm's page at /companies/energy-robotics-gmbh is now titled Korial (Energy Robotics GmbH renamed)"),
    ("hive-technologies", ["hive"], "Hive", "one company: Hive Technologies GmbH, 'Hive' on the job board"),
    ("matchory", ["matchory-com"], "Matchory", "one company, two renderings"),
    ("nosh-bio", ["nosh-biofoods"], "Nosh.bio", "one company: Nosh Biofoods GmbH trades as Nosh.bio"),
    ("spaitial-ai", ["spaitial"], "SpAItial", "one company, two renderings"),
    ("alantos-pharmaceuticals", ["alantos-pharmaceutical", "alantos-pharmaceuticals-ag", "therascope"], "Alantos Pharmaceuticals", "one company, three renderings (Therascope AG until 2004)"),
    ("arga-medtech", ["arg-medtech-sa", "arg-medtech"], "Arga Medtech", "one company: the accented rendering slugs differently"),
    ("b-nalyze", ["binalyze"], "Binalyze", "one company: 'b!nalyze' is the 2025 list's rendering"),
    ("nuri-bitwala-gmbh", ["bitwala", "nuri"], "Nuri", "one company: Bitwala GmbH renamed itself Nuri in 2021 (the firm's own label: 'Nuri (Bitwala GmbH)')"),
    ("conjectag", ["conject-ag", "conject"], "Conject", "one company, three renderings of conject AG"),
    ("dcs-travel-technologies", ["dcs-plus"], "dcs plus", "one company: dcs plus (Bucharest) is 'dcs travel technologies' on the 2018+ lists"),
    ("fitetv", ["flipps", "fite"], "FITE", "one company: Flipps Media Inc. renamed its product and itself FITE"),
    ("forto", ["freight-hub"], "Forto", "one company: FreightHub renamed itself Forto in 2020"),
    ("conny", ["lexfox"], "Conny", "one company: LexFox renamed itself CONNY in 2020"),
    ("m0", ["m-zero-labs", "m-zero"], "M0", "one company: M^ZERO Labs, 'M0' on the 2025 list"),
    ("n26", ["number26"], "N26", "one company: NUMBER26 renamed itself N26 in 2016"),
    ("onefootball", ["the-football-app"], "OneFootball", "one company: 'The Football App' renamed itself Onefootball in 2013"),
    ("6-wunderkinder-gmbh", ["wunderlist", "6wunderkinder"], "6Wunderkinder", "one company: 6Wunderkinder GmbH, maker of Wunderlist (the 2014-2023 lists name the product)"),
    ("simr", ["ubercloud"], "Simr", "one company: UberCloud renamed itself Simr (the firm's own label: 'Simr (formerly UberCloud)')"),
    ("alokai-formerly-vue-storefront", ["vue-storefront"], "Alokai", "one company: Vue Storefront renamed itself Alokai in 2024"),
    ("xayn-ag", ["xain-ag"], "Xayn", "one company: XAIN AG renamed itself Xayn"),
    ("colibri", ["colibritd"], "ColibriTD", "one company: ColibrITD (Paris, quantum software), 'Colibri' on the 2025 list"),
    ("myriad-ag", ["esmertec-ag", "esmertec", "myriad-software-group-ag"], "Myriad Group", "one company: Esmertec AG (the 2001 investment) renamed itself Myriad Group AG in 2009 after merging with Purple Labs; Purple Labs stays its own row"),
    ("bigchaindb", ["ascribe"], "BigchainDB", "one company: ascribe GmbH built BigchainDB and took its name"),
    ("simfy", ["music-networx-gmbh"], "Simfy", "one company: Music Networx GmbH (later simfy AG) operates simfy"),
    ("ebs", ["ebs-technologies"], "EBS Technologies", "one company, two renderings"),
    ("zonare-medical-systems", ["zonare-inc", "zonare"], "Zonare Medical Systems", "one company, two renderings"),
    ("obilet-com", ["obilet"], "Obilet", "one company, two renderings"),
    ("picus", ["picus-security"], "Picus Security", "one company, two renderings"),
    ("mikro-yazilim", ["mikrogrup"], "Mikro Yazilim", "one company: Mikro Yazilim (Mikrogrup)"),
    ("urbia-com", ["urbia"], "urbia.com", "one company, two renderings"),
    ("interhyp", ["interhyp-ag"], "Interhyp", "one company, two renderings"),
    ("tipp24-ag", ["tipp-24", "tipp24"], "Tipp24", "one company, three renderings"),
    ("peak-games", ["peak"], "Peak Games", "one company: Peak Games, 'Peak' on the 2020-2023 lists"),
    ("tasty-urban", ["tastyurban-gmbh", "tastyurban"], "Tasty Urban", "one company, two renderings"),
    ("nortech", ["nortech-ai"], "Nortech", "one company, two renderings"),
    ("junto-education-gmbh", ["junto"], "Junto", "one company, two renderings"),
    ("b2x-gmbh", ["b2x", "b2x-care-solutions"], "B2X", "one company: B2X Care Solutions GmbH"),
    ("azeti", ["azeti-networks-gmbh", "azeti-networks"], "azeti", "one company: azeti Networks"),
    ("versus", ["versus-io"], "Versus", "one company: versus.com (Versus IO)"),
    ("miracor", ["miracor-medical"], "Miracor Medical", "one company, two renderings"),
    ("greywolf-therapeutics", ["grey-wolf-therapeutics"], "Greywolf Therapeutics", "one company, two renderings"),
    ("calypso-medical", ["calypso-medical-technologies-inc", "calypso"], "Calypso Medical", "one company, two renderings"),
    ("mayd-meds-at-your-doorstep", ["mayd"], "MAYD", "one company: MAYD, the list adds its tagline"),
    ("crosslend-gmbh-the-thing-gmbh", ["crosslend"], "CrossLend", "one company: CrossLend GmbH, renamed The Thing GmbH after its 2023 wind-down (the firm's own label)"),
    ("allthings-technologies-ag", ["allthings"], "Allthings", "one company, two renderings"),
    ("ariceum-therapeutics-gmbh", ["ariceum-therapeutics"], "Ariceum Therapeutics", "one company, two renderings"),
]

REJECTS = [
    ("earlybird-venture-capital", "the firm's own entry on its job board, not a portfolio company"),
]

# rows that are Digital East Fund positions by evidence the tags do not carry
DE_EXTRA = {
    "tjobs": "Tjobs Recruit (Targu-Mures, Romania), on the 2014-2016 one-page list, which carried no fund tags; a Digital East Fund 2013 SCA SICAR company (Dan Lupu)",
    "draftwise": "on the firm's job board only; Bek Ventures lists DraftWise as its own 2023 investment",
}
# rows the tags call Digital East but an Earlybird fund financed itself
DE_NOT = {"peak-games": "tagged 'Digital West, Digital East' by the firm: Fund IV entered in 2011, before the Digital East Fund existed",
          "socialbakers": "tagged Digital West by the firm: 2011 entry"}


def loose(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\((formerly|ex|former)[^)]*\)", " ", s)
    s = re.sub(r"\b(gmbh|ag|inc|ltd|sa|security|ai|com|io|tv|yazilim|travel technologies|plus)\b", " ", s)
    return re.sub(r"[^a-z0-9]+", "", s)


def main() -> None:
    base = json.loads((ROOT / "companies/base.json").read_text())
    slugs = {r["slug"]: r for r in base}
    # The overlay must come out the same whether the base on disk is the raw
    # build or one this overlay already shaped (found 2026-10-07: run against the
    # partitioned base it emitted no desk rows and dropped merged duplicates).
    # So the slug universe is base + excluded rows + the duplicates a previous
    # build absorbed (the builder leaves "absorbed <slug> (...)" in the notes).
    exc = ROOT / "companies/excluded.json"
    prior_desk, prior_rejects, absorbed = {}, {}, set()
    if exc.exists():
        for x in json.loads(exc.read_text()):
            if x.get("reason") == "other_desk":
                prior_desk[x["slug"]] = x
                slugs.setdefault(x["slug"], x)
            elif x.get("reason") == "build_filter":
                prior_rejects[x["slug"]] = x
                slugs.setdefault(x["slug"], x)
    for r in list(slugs.values()):
        absorbed.update(re.findall(r"absorbed ([a-z0-9-]+) \(", r.get("notes") or ""))
    merges, missing = [], []
    for canon, dups, name, reason in MERGES:
        present = [d for d in dups if d in slugs or d in absorbed]
        if canon not in slugs:
            # the canonical may be absent while a duplicate is the row: promote it
            if present:
                canon, present = present[0], present[1:]
            else:
                missing.append(canon)
                continue
        merges.append({"canonical": canon, "duplicates": present, "name": name, "reason": reason})

    # ---- the Digital East desk
    ev = json.loads((ROOT / "sources/wayback/archive-evidence.json").read_text())["companies"]
    site = json.loads((ROOT / "sources/site/companies-2026.json").read_text())["rows"]
    bek = json.loads((ROOT / "sources/site/bek-portfolio.json").read_text())["rows"]
    team = json.loads((ROOT / "sources/wayback/team-years.json").read_text())["detail"]
    why: dict[str, list[str]] = collections.defaultdict(list)
    tag_of = {}
    for k, c in ev.items():
        tags = collections.Counter(cl["desk_tag"] for cl in c["claims"]
                                   if cl.get("desk_tag") and cl["surface"] == "wp-portfolio")
        if tags:
            tag_of[k] = tags.most_common(1)[0]
    key_of_slug = {}
    for s, r in slugs.items():
        key_of_slug[s] = loose(r["name"])
    by_key = collections.defaultdict(list)
    for s, k in key_of_slug.items():
        by_key[k].append(s)

    def mark(name: str, reason: str):
        for s in by_key.get(loose(name), []):
            why[s].append(reason)

    for k, (tag, n) in tag_of.items():
        if tag == "Digital East":
            for nm in ev[k]["names"]:
                mark(nm, f"the firm's own 2018-2023 portfolio page tags it 'Digital East' ({n} captures)")
    for r in site:
        if r.get("digital_east"):
            mark(r["name"], "the firm's live page carries 'Digital East Fund*': 'The investment decision for this company was made by the separate company Digital East Fund which was operating under the licensed Earlybird brand'")
        if "Earlybird Digital East" in (r.get("partners_site") or []):
            mark(r["name"], "the firm's live page names 'Earlybird Digital East' as the deal team")
    for r in bek:
        mark(re.sub(r"\s*\(.*\)$", "", r["name"]), "Bek Ventures (the former Earlybird Digital East Fund) lists it as its own investment")
    de_people = [n for n, d in team.items() if set(d["team_tags"].values()) == {"Digital East"}]
    for n in de_people:
        for comp in set(team[n]["companies"].values()):
            for nm in re.split(r",\s*", comp):
                if nm.strip():
                    mark(nm.strip(), f"on the archived /team page a Digital East partner ({n}) lists it among 'Companies I work with'")
    for s, reason in DE_EXTRA.items():
        if s in slugs:
            why[s].append(reason)
    merged_into = {d: m["canonical"] for m in merges for d in m["duplicates"]}
    desk = {}
    for s, reasons in why.items():
        target = merged_into.get(s, s)
        if target in DE_NOT or s in DE_NOT:
            continue
        k = loose(slugs[s]["name"])
        tg = tag_of.get(next((kk for kk in ev if loose(ev[kk]["name"]) == k), ""), ("", 0))[0]
        if "Digital West" in tg and "Digital East" not in tg:
            continue          # the firm tags it as its own (a partner's list alone does not move it)
        desk.setdefault(target, []).extend(reasons)
        if s != target:
            desk.setdefault(s, []).extend(reasons)
    for s_ in prior_desk:                      # already partitioned: stays partitioned
        desk.setdefault(s_, ["partitioned on the first build (the firm's own Digital East tag, marker or Bek Ventures' list)"])
    desk_rows = [{"slug": s, "lineage": "digital-east",
                  "reason": "; ".join(sorted(set(r)))[:700]} for s, r in sorted(desk.items()) if s in slugs]

    out = {SLUG: {
        "_readme": ("Durable identity corrections consumed by build-company-base.py on every rebuild "
                    "(COLLECTION.md s8), written by scratch/eb_overlay.py: one company rendered under "
                    "different names across Earlybird's surfaces (the live Framer lists, the job board, "
                    "the 2018-2023 WordPress list, the 2014-2017 one-page site, the 2002-2013 pages) and "
                    "its renames; the rows that are Digital East Fund positions (decisions.md D2: 'desk', "
                    "lineage digital-east, partitioned as other_desk and preserved in excluded.json); "
                    "and the non-company rejects."),
        "merges": merges,
        "rejects": [{"slug": s, "reason": r} for s, r in REJECTS if s in slugs or s in prior_rejects],
        "desk": desk_rows,
        "never_merge": [],
    }}
    (ROOT / "companies/identity-merges.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(f"merges {len(merges)} (canonical missing: {missing}) | desk rows {len(desk_rows)} | rejects {len(out[SLUG]['rejects'])}")
    for d in desk_rows:
        print("  DE", d["slug"], "|", slugs[d["slug"]]["name"])
    for canon, dups, *_ in MERGES:
        absent = [d for d in dups if d not in slugs]
        # informational only: a listed variant that the base does not carry


if __name__ == "__main__":
    main()
