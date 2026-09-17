// Mirrors scripts/paths.py for the TypeScript scripts: every per-investor
// path derives from here, nothing builds "data/collection/investors/<slug>/…"
// by hand. ROOT is the working directory, as every npm script runs from the
// repo root.
import path from "node:path";

export const INVESTORS_DIR = path.join(process.cwd(), "data", "collection", "investors");

/** All file locations for one investor, derived from the slug. */
export class Paths {
  readonly root: string;
  readonly base_json: string;        // companies/: the evidence layer
  readonly base_csv: string;         // companies/: the one merged CSV, read by ingest-companies.ts
  readonly investor: string;         // investor/: the ingest row
  readonly investor_sources: string; // investor/: its provenance sidecar

  constructor(readonly slug: string) {
    this.root = path.join(INVESTORS_DIR, slug);
    this.base_json = path.join(this.root, "companies", "base.json");
    this.base_csv = path.join(this.root, "companies", "base.csv");
    this.investor = path.join(this.root, "investor", "investor.json");
    this.investor_sources = path.join(this.root, "investor", "sources.json");
  }
}
