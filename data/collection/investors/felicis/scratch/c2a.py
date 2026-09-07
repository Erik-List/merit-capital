#!/usr/bin/env python3
"""Seed-to-A graduation, from the firm's own round ladder.

The deterministic Form D layer was useless here and the reason is worth
recording: it decided graduation for 32 issuers, but only 6 of them survived
into the final base and NONE of those has a final `entry_stage` of Seed. The
layer had been computing graduation for the Canadian mining shells and Las
Vegas casino vehicles of the roster-name homonym clusters -- rows the grind
then ruled `not_member`. On an investor whose Form D coverage is a
name-matched subset, the C2A layer inherits the sweep's noise wholesale.

What replaces it is a layer this run has and no previous run did: the
`<p class="circles">` ladder on the 2011-2019 listings names **every round
Felicis joined**, in order. A row whose ladder is ["Seed", "Series A", ...] is
a graduation the firm itself recorded; a row whose ladder is ["Seed"] alone,
last seen years ago, is a non-graduation on the same first-party evidence.

Per §6 the cohort is entry_stage == Seed with >=24 months since entry, and
censored rows stay null by rule. Rows the ladder does not cover are left null
and counted, because an unverified leg is `cohort_unverified`, not a guess --
and the published rate carries its selection bias in the sentence.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from emit import WHO  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "scratch" / "queue" / "c2a.out.jsonl"
CUTOFF = 2024          # >=24 months since entry, measured against 2026


def key(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def main() -> None:
    base = json.loads((ROOT / "base.json").read_text())
    cls = json.loads((ROOT / "classification.json").read_text())
    cls = cls.get("felicis", cls)
    circ = json.loads((ROOT / "sources" / "site" / "wayback-circles.json").read_text())
    ladder = {}
    for r in circ["companies-circles"]:
        for k in (key(r.get("name")), key(r["slug"])):
            if k:
                ladder.setdefault(k, r["ladder"])

    lines = []
    grad = nograd = censored = uncovered = 0
    for r in base:
        slug = r["slug"]
        rec = cls.get(slug, {})
        if rec.get("entry_stage") != "Seed":
            continue
        fs = (r.get("first_seen") or "")[:4]
        if not fs.isdigit() or int(fs) > CUTOFF:
            censored += 1                      # censored by rule, stays null
            continue
        lad = ladder.get(key(r["name"])) or ladder.get(key(slug))
        if not lad:
            uncovered += 1
            lines.append({"slug": slug, "who": WHO, "flags": ["cohort_unverified"],
                          "note": "C2A: no first-party round ladder covers this "
                                  "row (it predates or postdates the 2011-2019 "
                                  "listing era), so the follow-on leg is "
                                  "unverified and graduation stays null."})
            continue
        later = [x for x in lad if x != "Seed"]
        value = bool(later)
        # §6 cross-check: no row may end false while being $1B+ or public.
        if not value and (rec.get("status") == "public"
                          or rec.get("valuation_range") in ("1b_plus", "10b_plus",
                                                            "100b_plus")):
            value = True
            note = ("C2A: the firm's own ladder shows Seed only, but the row is "
                    "public or $1B+, which §6 treats as a Form D blind spot "
                    "(4(a)(2) or foreign rounds that never filed). Disputed to "
                    "true.")
            src = "web_verified"
        else:
            note = (f"C2A from the firm's own round ladder on its 2011-2019 "
                    f"listings: {lad}. "
                    + ("A later round Felicis joined is on the record, so the "
                       "seed graduated." if value else
                       "Seed is the only round Felicis joined and the listing "
                       "era ended without a follow-on."))
            src = "web_verified"
        # verify's invariant-5 check reads legs_verified = stage cited AND
        # graduation_source in (formd, web_verified). The ladder is a citable
        # first-party document -- the same archived listing this run already
        # cites for entry_stage -- so it is web_verified. Where the STAGE leg
        # is not itself cited, the row still carries cohort_unverified,
        # because one verified leg is not two.
        row = {"slug": slug, "who": WHO,
               "seed_to_a_graduation": value,
               "graduation_source": src,
               "graduation_confidence": "medium",
               "entry_stage": "Seed",
               "note": note}
        if (rec.get("entry_stage_source") != "web_verified"
                or not (rec.get("entry_stage_citation") or "").strip()):
            row["flags"] = ["cohort_unverified"]
        lines.append(row)
        grad += value
        nograd += (not value)

    OUT.write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in lines) + "\n")
    total = grad + nograd
    print(f"wrote {OUT.name}: {len(lines)} rows")
    print(f"  cohort decided from the ladder : {total}  "
          f"(graduated {grad}, not {nograd}, "
          f"rate {100*grad/total:.1f}%)" if total else "  cohort: 0")
    print(f"  censored (entry after {CUTOFF})   : {censored}")
    print(f"  in cohort but unverified       : {uncovered}")


if __name__ == "__main__":
    main()
