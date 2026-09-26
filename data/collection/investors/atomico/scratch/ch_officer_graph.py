#!/usr/bin/env python3
"""The Companies House officer graph: every UK directorship of the firm's people.

The register's forward enumeration (COLLECTION.md §5 country table, UK row:
"Officer graph only"). For each roster person: search the register's officer
index by name, anchor the person's officer identities, and read every
appointment with its dates and service address. The output is the UK
analogue of the Form D related-person sweep, judged the same way (§1 T4: a
seat is dated against the person's firm at the appointment date).

Identity anchoring (one natural person appears under several officer ids,
one per appointment identity, and a common name collides with strangers):
  1. an id holding an appointment at one of the firm's own entities
     (config registers.uk.firm_entities) or whose appointments carry a firm
     office as the service address (registers.uk.firm_addresses) is the
     person — anchored;
  2. the anchored ids' birth month is the person's; any other id with the
     same full name tokens AND that birth month is the person too;
  3. an id matching neither is left out and counted, never guessed.
A seat whose service address is a firm office is flagged `firm_address`:
the register itself says the director sat there from the firm's office,
which is the strongest attribution the register can give short of a
shareholder list.

Usage: python3 ch_officer_graph.py <investor-slug> [--names "A B" ...]
Reads:  sources/registers/companies-house/roster-input.json (list of
        {name, slug, group}) unless --names is given
Writes: sources/registers/companies-house/officer-graph.json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[3].parent / "scripts"))
import companies_house as ch  # noqa: E402
from paths import Paths, write_atomic  # noqa: E402


def fold(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return " ".join(re.sub(r"[^a-z ]+", " ", s.lower()).split())


def tokens(name: str) -> list[str]:
    """Register names read 'SURNAME, Given Names'; site names 'Given Surname'."""
    n = fold(name.replace(",", " , "))
    return [t for t in n.split() if t]


NICK = {"ben": "benjamin", "chris": "christopher", "alex": "alexander", "tom": "thomas",
        "will": "william", "dan": "daniel", "andy": "andrew", "mike": "michael",
        "nick": "nicholas", "rob": "robert", "sam": "samuel", "hiro": "hiroyuki",
        "sasha": "alexander", "teddie": "edward", "jim": "james", "matt": "matthew",
        "kate": "katherine", "liz": "elizabeth", "steve": "stephen", "fred": "frederick"}


def name_matches(site_name: str, reg_name: str) -> bool:
    """First and last token of the site name both appear in the register name.
    Register officer names carry middle names ('Mattias Lennart Seve
    LJUNGMAN'); the site carries first + last, often a short form ('Ben'
    for Benjamin), so the first name also matches its long form or as a
    prefix of a register given name (3+ letters)."""
    s = [t for t in tokens(site_name) if len(t) > 1]
    r = tokens(reg_name)
    if len(s) < 2:
        return False
    first, last = s[0], s[-1]
    if last not in r:
        return False
    forms = {first, NICK.get(first, first)}
    return any(t in forms or (len(first) >= 3 and t.startswith(first)) for t in r if t != last)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("investor")
    ap.add_argument("--names", nargs="*")
    ap.add_argument("--max-candidates", type=int, default=12)
    ap.add_argument("--refresh", action="store_true", help="re-read people already done")
    args = ap.parse_args()
    p = Paths(args.investor)
    cfg = p.config().get("registers", {}).get("uk", {})
    firm_entities = set(cfg.get("firm_entities") or [])
    firm_addr = [re.compile(a, re.I) for a in cfg.get("firm_addresses") or []]
    outdir = p.sources / "registers" / "companies-house"
    outdir.mkdir(parents=True, exist_ok=True)
    out_path = outdir / "officer-graph.json"
    prior = json.loads(out_path.read_text()) if out_path.exists() else {"people": {}}

    if args.names:
        roster = [{"name": n, "slug": re.sub(r"[^a-z0-9]+", "-", fold(n)).strip("-"), "group": ""}
                  for n in args.names]
    else:
        roster = json.loads((outdir / "roster-input.json").read_text())

    def is_firm_addr(a: str) -> bool:
        return any(r.search(a or "") for r in firm_addr)

    people = prior.get("people", {})
    firm_officers = [o for num in sorted(firm_entities) for o in ch.officers(num)
                     if o.get("officer_id")]
    for person in roster:
        name, slug = person["name"], person["slug"]
        if slug in people and people[slug].get("status") == "done" and not args.refresh:
            continue
        rec = {"name": name, "group": person.get("group", ""), "ids": [], "rejected_ids": [],
               "seats": [], "status": "open"}
        try:
            cands = [c for c in ch.search_officers(name, pages=2) if name_matches(name, c["name"])]
            cands = cands[: args.max_candidates]
            # Seed from the firm's own entities: an LLP member or director of
            # a firm entity is the person whatever the search ranks first
            # (a common name like Christopher Barnes sits past page 2).
            ids = {c["officer_id"] for c in cands}
            for o in firm_officers:
                if name_matches(name, o["name"]) and o["officer_id"] not in ids:
                    cands.append(o)
                    ids.add(o["officer_id"])
            detail = {}
            for c in cands:
                detail[c["officer_id"]] = ch.appointments(c["officer_id"])
            anchored_born = set()
            for oid, d in detail.items():
                if any(a["company_number"] in firm_entities or is_firm_addr(a["address"])
                       for a in d["appointments"]):
                    if d.get("born"):
                        anchored_born.add(d["born"])
                    d["_anchor"] = True
            for oid, d in detail.items():
                keep = d.get("_anchor") or (d.get("born") and d["born"] in anchored_born)
                (rec["ids"] if keep else rec["rejected_ids"]).append(
                    {"officer_id": oid, "name": d.get("name"), "born": d.get("born"),
                     "total": d.get("total"), "anchor": bool(d.get("_anchor"))})
                if not keep:
                    continue
                for a in d["appointments"]:
                    rec["seats"].append({
                        **a, "officer_id": oid,
                        "firm_entity": a["company_number"] in firm_entities,
                        "firm_address": is_firm_addr(a["address"]),
                    })
            rec["born"] = sorted(anchored_born)
            rec["status"] = "done"
        except ch.Unavailable as e:
            rec["status"] = f"unavailable: {e}"
        people[slug] = rec
        write_atomic(out_path, json.dumps({
            "_readme": ("Companies House officer graph (scratch/ch_officer_graph.py): per roster "
                        "person, the officer identities anchored to the firm (an appointment at a firm "
                        "entity or a firm office as service address, then same name + birth month) and "
                        "every appointment of those identities, flagged firm_address / firm_entity. "
                        "Seats are dated; judge them against the person's tenure (COLLECTION.md §1 T4)."),
            "swept_at": time.strftime("%Y-%m-%d"),
            "firm_entities": sorted(firm_entities),
            "firm_addresses": [r.pattern for r in firm_addr],
            "people": people}, indent=1, ensure_ascii=False) + "\n")
        n_seats = len(rec["seats"])
        n_firm = sum(s["firm_address"] for s in rec["seats"])
        print(f"{name:32} ids {len(rec['ids'])} (rejected {len(rec['rejected_ids'])}) "
              f"seats {n_seats} firm-address {n_firm} {rec['status'] if rec['status'] != 'done' else ''}",
              flush=True)


if __name__ == "__main__":
    main()
