/**
 * Taxonomy validation for ingest.
 *
 * The taxonomy files only describe the vocabulary; this is what enforces it.
 * Stage, focus and scope type are closed, so out-of-vocabulary labels are
 * errors and the row is not written. Geography is open by design, so unknown
 * labels are normalised and reported as warnings, never rejected.
 *
 * Values are rewritten to their canonical spelling in place, so an aggregated
 * file carrying "seriesA" or "NYC" is ingested as "Series A" and "New York"
 * rather than being rejected for a spelling difference.
 */

import {
  canonicalizeFocus,
  canonicalizeGeo,
  canonicalizeScopeType,
  canonicalizeStage,
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
 * Validate and canonicalise the taxonomy-bound fields on a company row.
 * `focus` is a single value from the closed twelve-value taxonomy (null means
 * outside it, which is legitimate); `hq_country` is an ISO 3166-1 alpha-2
 * code or null. Mutates `row` with the canonical focus spelling.
 */
export function validateCompanyFields(row: Record<string, any>): TaxonomyIssues {
  const errors: string[] = [];
  const warnings: string[] = [];

  if (typeof row.focus === "string" && row.focus.trim()) {
    const match = canonicalizeFocus(row.focus);
    if (match) {
      row.focus = match;
    } else {
      errors.push(`focus: "${row.focus}" is not in the focus taxonomy`);
    }
  } else if (row.focus != null) {
    errors.push("focus: expected a string or null");
  }

  if (typeof row.hq_country === "string") {
    if (!/^[A-Z]{2}$/.test(row.hq_country)) {
      errors.push(`hq_country: "${row.hq_country}" is not an ISO 3166-1 alpha-2 code`);
    }
  } else if (row.hq_country != null) {
    errors.push("hq_country: expected a string or null");
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

  return { errors, warnings };
}

export const GRADUATION_STATUSES = [
  "graduated",
  "not_graduated",
  "censored",
  "undetermined",
] as const;
