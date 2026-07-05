/**
 * Shared helpers for normalizing a fund's `size` value to an integer USD number.
 *
 * The `size` field inside the institutional `funds` jsonb is stored as an integer
 * number of USD (e.g. 430000000), matching the sibling `aum` field. These helpers
 * coerce any legacy or LLM-produced string values (e.g. "$430M") into that shape,
 * mirroring the SQL migration 20251103120000_convert_fund_size_to_number.sql:
 * strip non-numeric characters, then apply a B/M/K multiplier.
 */

export function parseFundSize(value: unknown): number | null {
  if (typeof value === 'number') {
    return Number.isFinite(value) ? value : null;
  }

  if (typeof value === 'string') {
    const trimmed = value.trim();
    const numeric = Number.parseFloat(trimmed.replace(/[^0-9.]/g, ''));
    if (!Number.isFinite(numeric)) {
      return null;
    }
    if (/b/i.test(trimmed)) {
      return numeric * 1_000_000_000;
    }
    if (/m/i.test(trimmed)) {
      return numeric * 1_000_000;
    }
    if (/k/i.test(trimmed)) {
      return numeric * 1_000;
    }
    return numeric;
  }

  return null;
}

/**
 * Coerce every `size` inside a `funds` jsonb value (shape `{ funds: [...] }`) to an
 * integer USD number using {@link parseFundSize}. Non-object inputs and unexpected
 * shapes are returned unchanged so callers can pass through null/legacy data safely.
 */
export function normalizeFundSizes<T>(funds: T): T {
  if (!funds || typeof funds !== 'object') {
    return funds;
  }

  const record = funds as Record<string, unknown>;
  const list = record.funds;
  if (!Array.isArray(list)) {
    return funds;
  }

  return {
    ...record,
    funds: list.map((entry) => {
      if (!entry || typeof entry !== 'object') {
        return entry;
      }
      const fund = entry as Record<string, unknown>;
      if (!('size' in fund)) {
        return fund;
      }
      return { ...fund, size: parseFundSize(fund.size) };
    }),
  } as T;
}
