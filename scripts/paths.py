#!/usr/bin/env python3
"""The one PATHS helper for data/collection/.

Every pipeline script derives its paths from here, keyed by investor slug, so
adding an investor touches nothing outside `data/collection/investors/<slug>/`.
Cross-investor caches (SEC public float, CIK lookup, unicorn lists) live in
`data/collection/shared/`; everything per-investor lives under the investor
root. Per-investor constants (site domain, wayback era map, desk rules, seed
CIK queries, own-vehicle regex, ...) live in the investor's `config.json`,
loaded via `Paths.config()` — the scripts themselves carry none.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COLLECTION = ROOT / "data" / "collection"
SHARED = COLLECTION / "shared"
SEC_CACHE = SHARED / "sec"                    # public-float/, cik-lookup-data.txt
UNICORN_DIR = SHARED / "unicorns"
INVESTORS = COLLECTION / "investors"
PLAYBOOK = COLLECTION / "COLLECTION.md"


class Paths:
    """All file locations for one investor, derived from the slug."""

    def __init__(self, slug: str):
        self.slug = slug
        self.root = INVESTORS / slug

        # published surfaces
        self.base_json = self.root / "base.json"          # the evidence layer
        self.base_csv = self.root / "base.csv"            # the one merged CSV
        self.review_html = self.root / "review.html"

        # curated / durable state
        self.decisions = self.root / "decisions.md"
        self.report = self.root / "report.md"
        self.golden = self.root / "golden.json"
        self.ledger = self.root / "base-verification.json"
        self.identity_merges = self.root / "identity-merges.json"
        self.resolved = self.root / "resolved.json"
        self.classification = self.root / "classification.json"
        self.entities = self.root / "entities.json"
        self.excluded = self.root / "excluded.csv"        # reason: build_filter | other_desk | not_member
        self.investor = self.root / "investor.json"       # the ingest row
        self.investor_sources = self.root / "investor.sources.json"
        self.config_file = self.root / "config.json"

        # run scratch (regenerated; layer-b holds live Wikidata answers)
        self.queue = self.root / "queue"
        self.issuer_evidence = self.root / "issuer-evidence.json"
        self.layer_a = self.root / "layer-a.json"
        self.layer_b = self.root / "layer-b.json"
        self.graduation = self.root / "graduation-formd.json"

        # extracted evidence snapshots
        self.sources = self.root / "sources"
        self.wayback = self.sources / "wayback"
        self.site = self.sources / "site"
        self.edgar = self.sources / "edgar"
        self.formd_rounds = self.edgar / "formd-issuer-rounds.json"

    def config(self) -> dict:
        if not self.config_file.exists():
            raise SystemExit(f"no investor config at {self.config_file}")
        return json.loads(self.config_file.read_text())

    def rel(self, p: Path) -> str:
        return str(p.relative_to(ROOT))
