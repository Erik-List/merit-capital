#!/usr/bin/env python3
"""Expand compact judge decisions into the batch .out.jsonl `record` expects.

COLLECTION.md §8: "`record` routes a line by the presence of `verdict`, so a
MEMBER needs TWO lines" -- the verdict line and a classification line. A single
line carrying both is recorded as a verdict and every classification key on it
is dropped silently. This helper enforces that split so the judge cannot make
that mistake by hand, and stamps the boilerplate (`who`, the *_source and
*_confidence keys) that would otherwise be retyped 600 times.

Used as a library from a per-batch script:

    from emit import Batch
    b = Batch(7)                       # writes batch-007.out.jsonl
    b.member("plaid", "site_listing", "Listed every era; $12.5M Series A 2014.")
    b.cls("plaid", status="private", entry_stage="Series A",
          entry_stage_source="web_verified",
          entry_stage_citation="https://www.felicis.com/companies/plaid",
          valuation_range="1b_plus", valuation_usd=6_100_000_000,
          valuation_source="web_verified", valuation_citation="...")
    b.not_member("uldaman-capital-corp", "homonym",
                 "'John Anderson' name-match on a Vancouver shell.")
    b.write()
"""
import json
from pathlib import Path

WHO = "agent-judge-pro94"
QUEUE = Path(__file__).resolve().parents[1] / "scratch" / "queue"

# Keys that carry their own confidence/source when the judge does not say.
DEFAULT_CONF = {
    "status": "status_confidence",
    "valuation_range": "valuation_confidence",
    "entry_stage": "entry_stage_confidence",
    "hq_country": "hq_country_confidence",
}


class Batch:
    def __init__(self, n: int):
        self.n = n
        self.lines: list[dict] = []

    # ---- membership -------------------------------------------------
    def member(self, slug, evidence_class, basis, confidence="high", citation=None):
        row = {"slug": slug, "who": WHO, "verdict": "member",
               "evidence_class": evidence_class, "basis": basis,
               "confidence": confidence}
        if citation:
            row["citation"] = citation
        self.lines.append(row)

    def not_member(self, slug, klass, basis, confidence="high", evidence_class="web"):
        self.lines.append({"slug": slug, "who": WHO, "verdict": "not_member",
                           "evidence_class": evidence_class, "basis": basis,
                           "confidence": confidence, "exclusion_class": klass})

    def uncertain(self, slug, basis, evidence_class="web"):
        self.lines.append({"slug": slug, "who": WHO, "verdict": "uncertain",
                           "evidence_class": evidence_class, "basis": basis,
                           "confidence": "low"})

    # ---- classification ---------------------------------------------
    def cls(self, slug, *, conf="high", **kw):
        """One classification line. `conf` fills any *_confidence the caller
        did not set explicitly, for the columns actually present."""
        row = {"slug": slug, "who": WHO}
        row.update({k: v for k, v in kw.items() if v is not None})
        for col, ckey in DEFAULT_CONF.items():
            if col in row and ckey not in row:
                row[ckey] = conf
        self.lines.append(row)

    # ---- output ------------------------------------------------------
    def write(self):
        out = QUEUE / f"batch-{self.n:03d}.out.jsonl"
        out.write_text("\n".join(json.dumps(r, ensure_ascii=False)
                                 for r in self.lines) + "\n")
        v = sum(1 for r in self.lines if "verdict" in r)
        print(f"wrote {out.name}: {len(self.lines)} lines "
              f"({v} verdicts, {len(self.lines) - v} classification)")
        return out
