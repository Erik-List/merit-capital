"""Answer emitter for the grind: emits ONLY the keys the queue asked for.

COLLECTION.md §8: "Emit only the keys for the needs asked (plus flags, note) —
extra keys clobber filing-grade facts at merge time." This enforces that
mechanically instead of by care, and prints what it dropped so a judgment
meant as a deliberate dispute is visible rather than silently discarded.
"""
import json, sys
from pathlib import Path
ROOT = Path("/Users/erik/Developer/merit-capital")
QP = ROOT / "data/collection/investors/benchmark/scratch/queue"
Q = {r["slug"]: r for r in json.loads((QP / "queue.json").read_text())}
COMPANION = {"status": [], "membership": [],
             "hq_country": ["hq_country_source", "hq_country_citation"],
             "entry_stage": ["entry_stage_source", "entry_stage_confidence",
                             "entry_stage_citation", "seed_to_a_graduation",
                             "graduation_source", "graduation_confidence"],
             "valuation_range": ["valuation_usd", "valuation_source",
                                 "valuation_confidence", "valuation_citation"]}
EXTRA = {"focus", "focus_source", "hq_city", "hq_city_source", "note", "flags",
         "who", "slug", "clear_flags"}
VERDICT_KEYS = {"slug", "verdict", "evidence_class", "confidence", "basis",
                "citation", "who"}

class Batch:
    def __init__(self, n):
        self.n, self.recs, self.verdicts = n, [], []
    def V(self, slug, verdict, evidence_class, confidence, basis, citation=None):
        r = {"slug": slug, "verdict": verdict, "evidence_class": evidence_class,
             "confidence": confidence, "basis": basis, "who": "agent-judge-pro88"}
        if citation: r["citation"] = citation
        self.verdicts.append(r)
    def R(self, slug, st=None, cc=None, ccsrc="model_knowledge", stage=None, ssrc="model",
          sconf="low", cite=None, vr="below_1b", vusd=None, vsrc=None, vconf="high",
          vcite=None, focus=None, note="", flags=None, city=None, grad=None,
          gsrc="model", gconf="medium", clear=None, dispute=None):
        kw = {"slug": slug, "who": "agent-judge-pro88"}
        if st: kw["status"] = st
        if cc: kw["hq_country"] = cc; kw["hq_country_source"] = ccsrc
        if stage:
            kw["entry_stage"] = stage; kw["entry_stage_source"] = ssrc
            kw["entry_stage_confidence"] = sconf
            if cite: kw["entry_stage_citation"] = cite
            if grad is not None:
                kw["seed_to_a_graduation"] = grad
                kw["graduation_source"] = gsrc; kw["graduation_confidence"] = gconf
        if vr:
            kw["valuation_range"] = vr; kw["valuation_usd"] = vusd
            kw["valuation_confidence"] = vconf
            if vsrc: kw["valuation_source"] = vsrc
            if vcite: kw["valuation_citation"] = vcite
        if focus: kw["focus"] = focus; kw["focus_source"] = "model"
        if city: kw["hq_city"] = city; kw["hq_city_source"] = "model_knowledge"
        if note: kw["note"] = note
        if flags: kw["flags"] = flags
        if clear: kw["clear_flags"] = clear
        # COLLECTION.md §8's one exception: a deliberate dispute may carry a key
        # the queue did not ask for. It must be named, so it can never happen by
        # accident, and the flag says so on the row.
        kw["_dispute"] = set(dispute or [])
        self.recs.append(kw)
    def write(self):
        lines = [json.dumps({k: v for k, v in r.items() if k in VERDICT_KEYS})
                 for r in self.verdicts]
        for rec in self.recs:
            need = set(Q[rec["slug"]]["need"])
            keep = set(EXTRA)
            for n in need:
                keep.add(n); keep.update(COMPANION.get(n, []))
            for d in rec.get("_dispute", ()):
                keep.add(d); keep.update(COMPANION.get(d, []))
            out = {k: v for k, v in rec.items() if k in keep and k != "_dispute"}
            dropped = sorted(set(rec) - set(out) - {"who", "_dispute"})
            if dropped:
                print(f"  {rec['slug']}: not asked, dropped {dropped}", file=sys.stderr)
            if len(out) <= 2:
                print(f"  {rec['slug']}: EMPTY after filter (need={sorted(need)})", file=sys.stderr)
            lines.append(json.dumps(out))
        p = QP / f"batch-{self.n:03d}.out.jsonl"
        p.write_text("\n".join(lines) + "\n")
        print(f"batch {self.n}: {len(self.verdicts)} verdicts + {len(self.recs)} rows -> {p.name}")
