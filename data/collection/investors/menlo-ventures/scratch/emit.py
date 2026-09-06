#!/usr/bin/env python3
"""Turn a compact judge spec into a validated batch .out.jsonl.

Row spec: (slug, status, country, city, stage, note, extra)
  stage: "Seed" | "Series A" | "Growth" | "Pre-Seed" | None (pre-window or unknown)
  extra: dict merged last — valuation_usd/source/citation, flags, verdict, ...
Defaults: valuation_range below_1b; entry_stage cited to the firm's own company
page when SITE marks it; hq_country_source model_knowledge; who = the run tag.
"""
import glob, json, sys
from pathlib import Path
D = Path(__file__).resolve().parent.parent

# COLLECTION.md 8: "Emit only the keys for the needs asked — extra keys clobber
# filing-grade facts at merge time." The queue is the authority on what each row
# still needs, so the spec is filtered against it rather than trusted.
NEED = {}
for f in glob.glob(str(D / "scratch/queue/batch-*.json")):
    for it in json.loads(Path(f).read_text()):
        NEED[it["slug"]] = set(it.get("need") or [])
SATELLITES = {
    "status": ("status",),
    "hq_country": ("hq_country", "hq_country_source", "hq_country_confidence",
                   "hq_country_citation", "hq_city", "hq_city_source", "hq_city_confidence"),
    "entry_stage": ("entry_stage", "entry_stage_source", "entry_stage_confidence",
                    "entry_stage_citation", "seed_to_a_graduation", "graduation_confidence"),
    "valuation_range": ("valuation_range", "valuation_usd", "valuation_source",
                        "valuation_citation", "valuation_confidence", "valuation_range_source"),
}
# hq_city is never pre-filled by a deterministic layer, so writing it can never
# clobber a filing-grade fact; it is always allowed through.
ALWAYS = {"slug", "who", "note", "flags", "clear_flags", "focus", "focus_source",
          "verdict", "evidence_class", "confidence", "basis", "citation",
          "hq_city", "hq_city_source", "hq_city_confidence"}
WHO = "agent-judge-pro91"
SITE = "https://menlovc.com/portfolio/{}/"


CLASS_KEYS = {"status", "hq_country", "hq_country_source", "hq_country_confidence",
              "hq_city", "hq_city_source", "hq_city_confidence", "entry_stage",
              "entry_stage_source", "entry_stage_confidence", "entry_stage_citation",
              "valuation_range", "valuation_usd", "valuation_source",
              "valuation_confidence", "seed_to_a_graduation", "graduation_confidence",
              "note", "flags"}
DROPPED = []


def build(rows, dest):
    out = []
    for slug, status, country, city, stage, note, extra in rows:
        r = {"slug": slug, "who": WHO}
        if status: r["status"] = status
        if country:
            r["hq_country"] = country
            r.setdefault("hq_country_source", "model_knowledge")
            r["hq_country_confidence"] = "high"
        if city:
            r["hq_city"] = city
            r["hq_city_source"] = "model_knowledge"
            r["hq_city_confidence"] = "high"
        if stage:
            r["entry_stage"] = stage
        if note: r["note"] = note
        r.setdefault("valuation_range", "below_1b")
        r.update(extra or {})
        if r.get("entry_stage") and "entry_stage_source" not in r:
            r["entry_stage_source"] = "model"
            r["entry_stage_confidence"] = r.get("entry_stage_confidence", "medium")
        if r.get("entry_stage_source") == "web_verified" and not r.get("entry_stage_citation"):
            r["entry_stage_citation"] = SITE.format(slug)
        # A deliberate dispute is the one licensed exception to "emit only the
        # keys for the needs asked" (COLLECTION.md 8): a formd_band stage the
        # judge overrules has to be written even though the queue did not ask.
        forced = set(r.pop("_override", ()) or ())
        for k in list(forced):
            forced |= set(SATELLITES.get(k, ()))
        need = NEED.get(slug)
        if need is not None and not r.get("verdict"):
            keep = set(ALWAYS) | forced
            for n in need:
                keep |= set(SATELLITES.get(n, (n,)))
            dropped = sorted(k for k in r if k not in keep)
            for k in dropped:
                del r[k]
            if dropped:
                DROPPED.append(slug)
        # COLLECTION.md 8: a member gets the verdict line PLUS one classification
        # line — `record` routes by the presence of "verdict", so a single line
        # carrying both would drop every classification key on the floor.
        if r.get("verdict") == "member":
            cls = {k: v for k, v in r.items() if k in CLASS_KEYS}
            if cls:
                cls["slug"], cls["who"] = r["slug"], r["who"]
                out.append({k: v for k, v in r.items() if k not in CLASS_KEYS})
                out.append(cls)
                continue
        out.append(r)
    p = D / "scratch/queue" / dest
    p.write_text("\n".join(json.dumps(x) for x in out) + "\n")
    print(f"wrote {p.name}: {len(out)} rows; {len(DROPPED)} rows had un-asked keys filtered")
    DROPPED.clear()
