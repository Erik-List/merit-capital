/**
 * Taxonomy validation for ingest.
 *
 * The taxonomy files only describe the vocabulary; this is what enforces it.
 * Stage, category, focus and scope type are closed, so out-of-vocabulary
 * labels are errors and the row is not written. Geography is open by design, so unknown
 * labels are normalised and reported as warnings, never rejected.
 *
 * Values are rewritten to their canonical spelling in place, so an aggregated
 * file carrying "seriesA" or "NYC" is ingested as "Series A" and "New York"
 * rather than being rejected for a spelling difference.
 */

import {
  MAX_CATEGORIES,
  canonicalizeFocus,
  canonicalizeGeo,
  canonicalizeScopeType,
  canonicalizeStage,
  isCanonicalCategory,
  isKnownGeo,
} from "../../lib/taxonomy";

export type TaxonomyIssues = {
  errors: string[];
  warnings: string[];
};

function asStringArray(value: unknown): string[] | null {
  if (!Array.isArray(value)) return null;
  return value.filter((item): item is string => typeof item === "string");
}

/**
 * Validate and canonicalise every taxonomy-bound field on an investor row.
 * Mutates `row` with the canonical spellings and returns what was wrong.
 */
export function validateTaxonomyFields(row: Record<string, any>): TaxonomyIssues {
  const errors: string[] = [];
  const warnings: string[] = [];

  // --- stage: closed ---
  const stages = asStringArray(row.investment_stage);
  if (stages) {
    const canonical: string[] = [];
    stages.forEach((stage) => {
      const match = canonicalizeStage(stage);
      if (match) {
        if (!canonical.includes(match)) canonical.push(match);
      } else {
        errors.push(`investment_stage: "${stage}" is not in the stage taxonomy`);
      }
    });
    row.investment_stage = canonical;
  } else if (row.investment_stage != null) {
    errors.push("investment_stage: expected a JSON array of stage strings");
  }

  // --- focus: closed. Lives on investment_scope.focus. ---
  const canonicalizeFocusList = (values: string[], field: string): string[] => {
    const canonical: string[] = [];
    values.forEach((value) => {
      const match = canonicalizeFocus(value);
      if (match) {
        if (!canonical.includes(match)) canonical.push(match);
      } else {
        errors.push(`${field}: "${value}" is not in the focus taxonomy`);
      }
    });
    return canonical;
  };

  const scope = row.investment_scope;
  if (scope && typeof scope === "object" && !Array.isArray(scope)) {
    const focus = asStringArray(scope.focus);
    if (focus) {
      scope.focus = canonicalizeFocusList(focus, "investment_scope.focus");
    } else if (scope.focus != null) {
      errors.push("investment_scope.focus: expected a JSON array of focus strings");
    }

    if (typeof scope.type === "string" && scope.type.trim()) {
      const type = canonicalizeScopeType(scope.type);
      if (type) {
        scope.type = type;
      } else {
        errors.push(`investment_scope.type: "${scope.type}" is not "Generalist" or "Specialist"`);
      }
    }
  } else if (scope != null) {
    errors.push("investment_scope: expected a JSON object {type, focus}");
  }

  // --- geography: open. Normalise, warn on labels we have not seen before. ---
  const canonicalizeGeoList = (values: string[], field: string): string[] => {
    const canonical: string[] = [];
    values.forEach((value) => {
      const match = canonicalizeGeo(value);
      if (!match) return;
      if (!isKnownGeo(value)) {
        warnings.push(`${field}: "${match}" is not a known geography label, adding it as new`);
      }
      if (!canonical.includes(match)) canonical.push(match);
    });
    return canonical;
  };

  const geo = row.investment_geo;
  if (geo && typeof geo === "object" && !Array.isArray(geo)) {
    const core = asStringArray(geo.core);
    if (core) geo.core = canonicalizeGeoList(core, "investment_geo.core");
    const other = asStringArray(geo.other);
    if (other) geo.other = canonicalizeGeoList(other, "investment_geo.other");
  } else if (Array.isArray(geo)) {
    // Legacy flat-array shape: normalise into {core, other}.
    row.investment_geo = {
      core: canonicalizeGeoList(asStringArray(geo) ?? [], "investment_geo"),
      other: [],
    };
  } else if (geo != null) {
    errors.push("investment_geo: expected a JSON object {core, other}");
  }

  return { errors, warnings };
}

/**
 * Validate the taxonomy-bound fields on a company row. `categories` is an
 * array of at most MAX_CATEGORIES values from the closed category list, exact
 * spelling (the shared file is the author, so nothing is canonicalised; an
 * empty array is a company that fits no category); `hq_country` is an ISO
 * 3166-1 alpha-2 code or null.
 */
export function validateCompanyFields(row: Record<string, any>): TaxonomyIssues {
  const errors: string[] = [];
  const warnings: string[] = [];

  if (Array.isArray(row.categories)) {
    const bad = row.categories.filter(
      (value: unknown) => typeof value !== "string" || !isCanonicalCategory(value)
    );
    if (bad.length > 0) {
      errors.push(`categories: ${JSON.stringify(bad)} not in the category taxonomy`);
    }
    if (row.categories.length > MAX_CATEGORIES) {
      errors.push(`categories: ${row.categories.length} values, at most ${MAX_CATEGORIES}`);
    }
    if (new Set(row.categories).size !== row.categories.length) {
      errors.push("categories: a category twice");
    }
  } else if (row.categories != null) {
    errors.push("categories: expected an array of category strings");
  }

  if (row.company_key != null && typeof row.company_key !== "string") {
    errors.push("company_key: expected a string or null");
  }

  if (typeof row.hq_country === "string") {
    if (!/^[A-Z]{2}$/.test(row.hq_country)) {
      errors.push(`hq_country: "${row.hq_country}" is not an ISO 3166-1 alpha-2 code`);
    }
  } else if (row.hq_country != null) {
    errors.push("hq_country: expected a string or null");
  }

  if (typeof row.entry_stage === "string") {
    if (!(ENTRY_STAGES as readonly string[]).includes(row.entry_stage)) {
      errors.push(`entry_stage: "${row.entry_stage}" is not an entry stage (${ENTRY_STAGES.join(", ")})`);
    }
  } else if (row.entry_stage != null) {
    errors.push("entry_stage: expected a stage string");
  }

  if (typeof row.valuation_range === "string") {
    if (!(VALUATION_RANGES as readonly string[]).includes(row.valuation_range)) {
      errors.push(`valuation_range: "${row.valuation_range}" is not a valuation range`);
    }
  } else if (row.valuation_range != null) {
    errors.push("valuation_range: expected a range string");
  }

  // No cascade between the stage and the band is enforced here. It holds only
  // when the REASON is that the company cannot be named, and the reason lives
  // in a flag this table does not carry: a token-funded company (Erik,
  // 2026-09-19) has an undetermined stage because no priced round exists, yet
  // it is named and bandable. run.py's verify holds the cascade where the
  // flags are visible.
  // The figure belongs to the BAND, so only an undetermined band refuses one
  // (PRO-135). A nameable company whose entry round the record does not give
  // keeps its band, and above below_1b a band is required to carry a figure by
  // invariant 2 -- Lux's Cognition is $10B+ with an unknown entry round, and
  // this check used to reject it.
  if (row.valuation_usd != null && row.valuation_range === UNDETERMINED) {
    errors.push("undetermined: an undetermined valuation_range cannot carry a valuation_usd");
  }
  // An undetermined stage means the row is not a Seed entry, so the graduation
  // column does not apply and reads null -- or `undetermined`, which says a
  // judge looked and found no priced round to stage (the token-funded ruling,
  // Erik 2026-09-19). Both are what `public.companies`'s own CHECK accepts and
  // what run.py's verify accepts; only this validator demanded the second.
  if (row.entry_stage === UNDETERMINED
      && row.seed_to_a_graduation != null
      && row.seed_to_a_graduation !== UNDETERMINED) {
    errors.push(
      "undetermined: an undetermined entry_stage takes no graduation (null), or "
      + "`undetermined` where a judge looked and found no priced round"
    );
  }

  // seed_to_a_graduation is a closed status (public.graduation_status); the
  // pipeline's own verify enforces the evidence behind each value, this only
  // keeps a stray spelling or a legacy boolean cell out of the table.
  if (typeof row.seed_to_a_graduation === "string") {
    if (!(GRADUATION_STATUSES as readonly string[]).includes(row.seed_to_a_graduation)) {
      errors.push(
        `seed_to_a_graduation: "${row.seed_to_a_graduation}" is not a graduation status ` +
          `(${GRADUATION_STATUSES.join(", ")})`
      );
    }
  } else if (row.seed_to_a_graduation != null) {
    errors.push("seed_to_a_graduation: expected a status string or null");
  }
  // A Seed entry is always decided (PRO-132): a company past the censoring
  // window with no evidence of a later round did not graduate (Erik,
  // 2026-09-17), so a Seed row carries graduated, not_graduated or censored.
  // `undetermined` stays legal only on an undetermined stage (above), and the
  // database's own CHECK says the same from migration 20260920120000 on.
  if (row.entry_stage === "Seed"
      && !(DECIDED_GRADUATIONS as readonly unknown[]).includes(row.seed_to_a_graduation)) {
    errors.push(
      `seed_to_a_graduation: a Seed row must be decided (${DECIDED_GRADUATIONS.join(", ")}); `
      + `got ${JSON.stringify(row.seed_to_a_graduation ?? null)}`
    );
  }

  return { errors, warnings };
}

export const DECIDED_GRADUATIONS = ["graduated", "not_graduated", "censored"] as const;

export const GRADUATION_STATUSES = [
  "graduated",
  "not_graduated",
  "censored",
  "undetermined",
] as const;

// An unresolvable company carries `undetermined` in every outcome column
// (Erik, 2026-09-18). The three move together, so a row is undetermined in all
// of them or in none, and the database rejects any other combination.
const UNDETERMINED = "undetermined";
export const ENTRY_STAGES = [
  "Pre-Seed",
  "Seed",
  "Series A",
  "Growth",
  UNDETERMINED,
] as const;
export const VALUATION_RANGES = [
  "below_1b",
  "1b_plus",
  "10b_plus",
  "100b_plus",
  UNDETERMINED,
] as const;
