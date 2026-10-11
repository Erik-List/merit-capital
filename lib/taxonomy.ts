/**
 * Single source of truth for the stage, category, focus and geography vocabularies.
 *
 * The lists themselves live in `data/taxonomy/*.json` so the Python side of the
 * evidence layer can read the same files. Nothing in the app or in the scripts
 * should define these values inline: import from here instead.
 *
 * Stage and focus are closed, ingest rejects anything outside them. Geography is
 * deliberately open, so `canonicalizeGeo` normalises spelling and casing but lets
 * unknown labels through.
 */

// Relative, not the "@/" alias: this module is imported both by the Next.js
// app and by the tsx-run scripts.
import stageTaxonomy from '../data/taxonomy/stage.json';
import focusTaxonomy from '../data/taxonomy/focus.json';
import categoryTaxonomy from '../data/taxonomy/category.json';
import geoTaxonomy from '../data/taxonomy/geo.json';

// ---------------------------------------------------------------------------
// Stage
// ---------------------------------------------------------------------------

export const CANONICAL_STAGES = stageTaxonomy.values as readonly string[];

export type CanonicalStage = string;

export const STAGE_ALIAS_TO_LABEL: Record<string, string> = stageTaxonomy.aliases;

/** Sort key for anything that is not a canonical stage: keeps it last. */
export const FALLBACK_STAGE_INDEX = 10_000;

export type StageBucket = 'preseed' | 'seed' | 'seriesA' | 'growth';

export const STAGE_BUCKET_ORDER = stageTaxonomy.buckets.order as readonly StageBucket[];

export const STAGE_BUCKET_LABELS = stageTaxonomy.buckets.labels as Record<StageBucket, string>;

/** Canonical stage -> the coarse bucket the leaderboard filter exposes. */
export const STAGE_TO_BUCKET: Record<string, StageBucket> = Object.entries(
  stageTaxonomy.buckets.members as Record<string, string[]>
).reduce<Record<string, StageBucket>>((acc, [bucket, members]) => {
  members.forEach((stage) => {
    acc[stage] = bucket as StageBucket;
  });
  return acc;
}, {});

const CANONICAL_STAGE_BY_LOWER = new Map(
  CANONICAL_STAGES.map((stage) => [stage.toLowerCase(), stage])
);

export function canonicalizeStage(value: string): string | null {
  const normalized = value.trim().toLowerCase();
  if (!normalized) return null;
  return STAGE_ALIAS_TO_LABEL[normalized] ?? CANONICAL_STAGE_BY_LOWER.get(normalized) ?? null;
}

/** Position in the canonical ordering, or FALLBACK_STAGE_INDEX when unrecognised. */
export function stageIndex(value: string): number {
  const canonical = canonicalizeStage(value);
  if (!canonical) return FALLBACK_STAGE_INDEX;
  const index = CANONICAL_STAGES.indexOf(canonical);
  return index >= 0 ? index : FALLBACK_STAGE_INDEX;
}

export function isCanonicalStage(value: string): boolean {
  return CANONICAL_STAGES.includes(value);
}

// ---------------------------------------------------------------------------
// Category (companies.categories, PRO-173): up to three per company from the
// closed list of 25, judged once per company across every investor's book.
// ---------------------------------------------------------------------------

export const CATEGORY_VALUES = categoryTaxonomy.values as readonly string[];

export type CategoryKind = 'market' | 'technology' | 'customer' | 'business model';

export const CATEGORY_KINDS = categoryTaxonomy.kinds as Record<CategoryKind, readonly string[]>;

export const MAX_CATEGORIES = categoryTaxonomy.max_per_company as number;

export function isCanonicalCategory(value: string): boolean {
  return CATEGORY_VALUES.includes(value);
}

// ---------------------------------------------------------------------------
// Focus: the investor's own stated focus (investors.investment_scope.focus),
// read by the index search only. The company column `focus` is replaced by
// `categories` above.
// ---------------------------------------------------------------------------

export const FOCUS_VALUES = focusTaxonomy.values as readonly string[];

/** The subset the leaderboard filter shows above the "see all" fold. */
export const PRIMARY_FOCUS_VALUES = focusTaxonomy.primary as readonly string[];

export const SCOPE_TYPES = focusTaxonomy.scope_types.values as readonly string[];

const FOCUS_ALIASES: Record<string, string> = focusTaxonomy.aliases;
const SCOPE_TYPE_ALIASES: Record<string, string> = focusTaxonomy.scope_types.aliases;

const CANONICAL_FOCUS_BY_LOWER = new Map(
  FOCUS_VALUES.map((focus) => [focus.toLowerCase(), focus])
);

export function canonicalizeFocus(value: string): string | null {
  const normalized = value.trim().toLowerCase();
  if (!normalized) return null;
  return FOCUS_ALIASES[normalized] ?? CANONICAL_FOCUS_BY_LOWER.get(normalized) ?? null;
}

export function isCanonicalFocus(value: string): boolean {
  return FOCUS_VALUES.includes(value);
}

export function canonicalizeScopeType(value: string): string | null {
  const normalized = value.trim().toLowerCase();
  if (!normalized) return null;
  return SCOPE_TYPE_ALIASES[normalized] ?? null;
}

// ---------------------------------------------------------------------------
// Geography (open vocabulary)
// ---------------------------------------------------------------------------

/** The labels the geography filter always offers, whether or not data uses them. */
export const GEO_PRIMARY_LABELS = geoTaxonomy.primary as readonly string[];

/** Known-good labels. Not a constraint: geography accepts new values. */
export const GEO_SEED_VALUES = geoTaxonomy.values as readonly string[];

const GEO_ALIASES: Record<string, string> = geoTaxonomy.aliases;

const GEO_SEED_BY_LOWER = new Map(GEO_SEED_VALUES.map((geo) => [geo.toLowerCase(), geo]));

/**
 * Normalise a geography label. Unknown labels are kept, trimmed, because the
 * geography vocabulary is open by design: an investor may market a region we
 * have not seen before and that is not an error.
 */
export function canonicalizeGeo(value: string): string | null {
  const trimmed = value.trim();
  if (!trimmed) return null;
  const normalized = trimmed.toLowerCase();
  return GEO_ALIASES[normalized] ?? GEO_SEED_BY_LOWER.get(normalized) ?? trimmed;
}

/** True when the label is one we already know about, used for ingest warnings. */
export function isKnownGeo(value: string): boolean {
  const normalized = value.trim().toLowerCase();
  return GEO_ALIASES[normalized] !== undefined || GEO_SEED_BY_LOWER.has(normalized);
}
