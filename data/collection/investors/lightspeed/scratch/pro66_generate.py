#!/usr/bin/env python3
"""PRO-66 batch generator (the Accel PRO-65 pattern, Lightspeed parameters).

Merges the deterministic layers already in resolved.json (which flow into
export by themselves and are NOT re-emitted), the site card's first-party
fields (Stage Invested passed the 31/31 gate -> class-1 with the company
page URL as citation), and the hand-authored judgment table in
pro66_judgment.py, emitting only the keys each row still needs, in
record-sized JSONL batches under scratch/queue/pro66-*.out.jsonl.

Precedence per column: judgment override > card (gate-validated mapping) >
structural Form D > band (as ceiling, §8 escalations flagged) > convention/
prior (always flagged). Emits seed_to_a_graduation: null where a det-layer
band cohort value would ride a non-Seed final stage (verify invariant).
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from pro66_judgment import JUDGMENT  # noqa: E402

ROOT = HERE.parent
BATCH = 60

CARD_MAP = {"Pre-Seed": "Pre-Seed", "Seed": "Seed", "Seed-2": "Seed",
            "Series A": "Series A", "A-1": "Series A"}
GROWTH_CARDS = {"Series B", "Series C", "Series D", "Series E", "Series F",
                "Series G", "Series H", "Series I", "Common", "Ordinary"}
STATUS_MAP = {"Private": "private", "Acquired": "acquired", "IPO": "public",
              "Public": "public", "SPAC": "public"}


def main() -> None:
    base = json.load(open(ROOT / "base.json"))
    resolved = json.load(open(ROOT / "resolved.json"))
    site = {r["slug"]: r for r in json.load(open(ROOT / "sources/site/companies.json"))}
    ev = json.load(open(HERE / "issuer-evidence.json")).get("accessions", {})

    out, missing_status, missing_focus = [], [], []
    for r in base:
        s = r["slug"]
        det = resolved.get(s, {})
        c = site.get(s, {})
        J = JUDGMENT.get(s, {})
        rec: dict = {"slug": s}
        flags: list[str] = list(J.get("flags", []))
        notes: list[str] = [J["note"]] if J.get("note") else []

        accs = [a.strip() for a in (r.get("formd_accessions") or "").split(";") if a.strip()]
        e = next((ev[a] for a in accs if a in ev), {})

        # ---------------- entry_stage ----------------
        card_stage = c.get("stage_invested")
        card_url = c.get("url") or r.get("site_url")
        stage = conf = src = cite = None
        if "entry_stage" in J:
            stage = J["entry_stage"]
            src = J.get("entry_stage_source", "model")
            conf = J.get("entry_stage_confidence", "medium")
            cite = J.get("entry_stage_citation")
        elif card_stage in CARD_MAP:
            stage, src, conf, cite = CARD_MAP[card_stage], "web_verified", "high", card_url
            if c.get("invest_year"):
                notes.append(f"firm's own card: {card_stage}, backed since {c['invest_year']}")
        elif card_stage in GROWTH_CARDS:
            stage, src, conf, cite = "Growth", "web_verified", "high", card_url
            label = f"firm's own card: {card_stage}, backed since {c.get('invest_year') or '?'}"
            if card_stage in ("Common", "Ordinary"):
                label += " — instrument-typed entry at scale"
            notes.append(label)
        elif card_stage == "Early" and (c.get("invest_year") or "9999") <= "2002":
            stage, src, conf = "Series A", "model", "low"
            notes.append(f"card 'Early'/{c.get('invest_year')}: pre-2003 first institutional "
                         f"round is Series A by convention")
        elif (det.get("prior_rounds") or 0) >= 2:
            stage, src, conf = "Growth", "formd_structural", "high"
            notes.append(f"{det['prior_rounds']} filed rounds precede the partner-anchored entry")
        elif det.get("prior_rounds") == 1 and det.get("entry_stage"):
            stage = det["entry_stage"] if det["entry_stage"] in ("Series A", "Growth") else "Series A"
            src, conf = "formd_structural", "medium"
            notes.append("one filed round precedes the partner-anchored entry; band "
                         f"reads the ${(det.get('entry_offering_usd') or 0)/1e6:.1f}M entry as {det.get('entry_stage')}")
        elif det.get("entry_stage") and det.get("prior_rounds") == 0 \
                and (e.get("year_inc") or "").isdigit() and int(e["year_inc"]) >= 2008 \
                and det.get("entry_date") and int(det["entry_date"][:4]) - int(e["year_inc"]) <= 4:
            stage, src, conf = det["entry_stage"], "formd_band", "medium"
            flags.append("stage_band")
        elif str(r.get("first_seen", "")).isdigit() and int(r["first_seen"]) <= 2002:
            stage, src, conf = "Series A", "model", "low"
            notes.append("pre-2003 entry: first institutional round is Series A by convention")
        else:
            stage, src, conf = "Series A", "model", "low"
            flags.append("stage_prior")
            notes.append("unidentifiable stray: the firm's classic entry stage as prior")
        rec.update({"entry_stage": stage, "entry_stage_source": src,
                    "entry_stage_confidence": conf})
        if cite:
            rec["entry_stage_citation"] = cite

        # band-vs-label dispute marker (the ceiling rule): a filed structure
        # reading Growth under a card Seed/A label is a flagged tension.
        if (det.get("prior_rounds") or 0) >= 2 and stage in ("Pre-Seed", "Seed", "Series A") \
                and src == "web_verified":
            flags.append("stage_disputes_band")
            notes.append(f"card label kept over {det['prior_rounds']}-prior filing structure "
                         f"(first filed round is a ceiling, not the entry)")

        # ---------------- status ----------------
        status = J.get("status")
        st_conf = J.get("status_confidence")
        if status is None:
            if c.get("status_site") in STATUS_MAP:
                status = STATUS_MAP[c["status_site"]]
                st_conf = "medium"
                if det.get("status") and det["status"] != status and det.get("is_public") is not None:
                    # float layer disagrees with the card -> the filing-grade layer wins
                    status, st_conf = det["status"], det.get("valuation_confidence", "high")
                    flags.append("model_disputes_source")
                    notes.append(f"card status '{c['status_site']}' overridden by the SEC layer")
            elif det.get("status"):
                status = None  # deterministic layer already carries it; emit nothing
            else:
                missing_status.append(s)
        if status is not None and status != det.get("status"):
            rec["status"] = status
            if st_conf:
                rec["status_confidence"] = st_conf
        elif status is not None and J.get("status") and J["status"] != det.get("status"):
            rec["status"] = status

        # ---------------- valuation ----------------
        for k in ("valuation_usd", "valuation_asof", "valuation_source",
                  "valuation_confidence", "valuation_citation", "valuation_range",
                  "valuation_range_source"):
            if k in J:
                rec[k] = J[k]
        if "valuation_range" not in rec and not det.get("valuation_range") \
                and "needs_web_value" not in flags:
            rec["valuation_range"] = "below_1b"

        # ---------------- hq_country ----------------
        if "hq_country" in J:
            rec["hq_country"] = J["hq_country"]
            rec["hq_country_source"] = J.get("hq_country_source", "model_knowledge")
            if J.get("hq_country_citation"):
                rec["hq_country_citation"] = J["hq_country_citation"]
        elif not det.get("hq_country"):
            if e.get("state_desc"):
                rec["hq_country"] = e["state_desc"]  # canon at the record door
                rec["hq_country_source"] = "formd_address"
            else:
                rec["hq_country"] = "US"
                rec["hq_country_source"] = "model_knowledge"
                flags.append("country_prior")

        # ---------------- hq_city ----------------
        if "hq_city" in J:
            rec["hq_city"] = J["hq_city"]
            rec["hq_city_source"] = J.get("hq_city_source", "model_knowledge")
        elif e.get("city"):
            rec["hq_city"] = " ".join(w.capitalize() for w in e["city"].strip().lower().split())
            rec["hq_city_source"] = "formd_address"
            rec["hq_city_confidence"] = "medium"
        else:
            flags.append("city_unknown")

        # ---------------- focus ----------------
        if "focus" in J:
            rec["focus"] = J["focus"]
            rec["focus_source"] = J.get("focus_source", "model")
        else:
            missing_focus.append(s)

        # ---------------- C2A consistency ----------------
        if "seed_to_a_graduation" in J:
            rec["seed_to_a_graduation"] = J["seed_to_a_graduation"]
            if J.get("graduation_source"):
                rec["graduation_source"] = J["graduation_source"]
            if J.get("graduation_confidence"):
                rec["graduation_confidence"] = J["graduation_confidence"]
        elif det.get("seed_to_a_graduation") is not None and stage != "Seed":
            rec["seed_to_a_graduation"] = None  # band cohort value must not ride a non-Seed stage

        if flags:
            rec["flags"] = sorted(set(flags))
        if notes:
            rec["note"] = " | ".join(notes)
        out.append(rec)

    qdir = ROOT / "scratch" / "queue"
    for f in qdir.glob("pro66-*.out.jsonl"):
        f.unlink()
    for i in range(0, len(out), BATCH):
        chunk = out[i:i + BATCH]
        (qdir / f"pro66-{i // BATCH + 1:03d}.out.jsonl").write_text(
            "\n".join(json.dumps(x) for x in chunk) + "\n")
    print(f"emitted {len(out)} records in {(len(out)+BATCH-1)//BATCH} batches")
    print(f"rows still missing status: {len(missing_status)}")
    print(f"rows still missing focus : {len(missing_focus)}")
    if missing_status[:10]:
        print("  e.g.", missing_status[:10])


if __name__ == "__main__":
    main()
