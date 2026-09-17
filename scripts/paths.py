#!/usr/bin/env python3
"""The one PATHS helper for data/collection/.

Every pipeline script derives its paths from here, keyed by investor slug, so
adding an investor touches nothing outside `data/collection/investors/<slug>/`.
Cross-investor caches (SEC public float, CIK lookup, unicorn lists) live in
`data/collection/shared/`; everything per-investor lives under the investor
root. Per-investor constants (site domain, wayback era map, desk rules, seed
CIK queries, own-vehicle regex, ...) live in the investor's `config.json`,
loaded via `Paths.config()` — the scripts themselves carry none.
`scripts/utils/paths.ts` mirrors this class for the TypeScript scripts.
"""
import contextlib
import json
import os
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COLLECTION = ROOT / "data" / "collection"
SHARED = COLLECTION / "shared"
SEC_CACHE = SHARED / "sec"                    # public-float/, cik-lookup-data.txt
UNICORN_DIR = SHARED / "unicorns"
INVESTORS = COLLECTION / "investors"
PLAYBOOK = COLLECTION / "COLLECTION.md"


def write_atomic(path: Path, text: str, encoding: str = "utf-8") -> None:
    """Write `text` so a concurrent reader sees the old file or the new one, never
    a torn one: temp file in the same directory, fsync, then an atomic rename.

    Every shared cache and published surface is read by other sessions while a
    run writes it (several investors collect at once on one machine), and
    `Path.write_text` truncates before it writes. The temp suffix is `.tmp` so
    directory globs on the real suffix (`*.txt`, `*.json`) never pick it up;
    `newline=""` keeps CSV bytes exactly as the csv module produced them.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding=encoding, newline="") as f:
            f.write(text)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    except BaseException:
        with contextlib.suppress(FileNotFoundError):
            os.unlink(tmp)
        raise


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
        self.ledger = self.root / "membership-ledger.json"
        self.identity_merges = self.root / "identity-merges.json"
        self.resolved = self.root / "resolved.json"
        self.classification = self.root / "classification.json"
        self.entities = self.root / "entities.json"
        self.excluded = self.root / "excluded.json"       # reason: build_filter | other_desk | not_member
        self.investor = self.root / "investor.json"       # the ingest row
        self.investor_sources = self.root / "investor.sources.json"
        self.config_file = self.root / "config.json"
        self.cross_rulings = self.root / "cross-rulings.json"  # this investor's invariant-10 rulings

        # run scratch, under scratch/: everything here regenerates, so the
        # investor's top level holds only curated inputs and published
        # outputs. (layer-b holds live Wikidata answers — regenerating it
        # re-queries the web, hence scratch stays tracked.)
        self.scratch = self.root / "scratch"
        self.queue = self.scratch / "queue"
        self.issuer_evidence = self.scratch / "issuer-evidence.json"
        self.layer_a = self.scratch / "layer-a.json"
        self.layer_b = self.scratch / "layer-b.json"
        self.graduation = self.scratch / "graduation-formd.json"
        self.in_flight = self.scratch / "in-flight.json"      # present while a run is under way

        # extracted evidence snapshots
        self.sources = self.root / "sources"
        self.wayback = self.sources / "wayback"
        self.site = self.sources / "site"
        self.team = self.site / "team.json"                # the live team, profile input
        self.edgar = self.sources / "edgar"
        self.web = self.sources / "web"                    # fts / wikipedia sweeps
        self.formd_rounds = self.edgar / "formd-issuer-rounds.json"

    def config(self) -> dict:
        if not self.config_file.exists():
            raise SystemExit(f"no investor config at {self.config_file}")
        return json.loads(self.config_file.read_text())

    def rel(self, p: Path) -> str:
        return str(p.relative_to(ROOT))
